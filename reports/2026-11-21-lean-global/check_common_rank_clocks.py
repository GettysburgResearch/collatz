#!/usr/bin/env python3
"""Exact affine endpoint and clock guard check for the eight frozen templates.

This program does not run a Collatz convergence search. It verifies each
retained prefix on its entire affine progression by constant/slope arithmetic.
The source template data are copied from the pinned author program; the
constant/slope and no-padding checks below are a separate implementation.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def affine_prefix(constant, slope, exponents):
    require(constant > 0 and constant % 2 == 1, 'invalid ordinary source')
    require(slope > 0 and slope % 2 == 0, 'invalid cylinder slope')
    for a in exponents:
        require(a > 0, 'nonpositive exponent')
        constant, remainder = divmod(3*constant+1, 2**a)
        require(remainder == 0, 'nonintegral endpoint constant')
        slope, remainder = divmod(3*slope, 2**a)
        require(remainder == 0, 'nonintegral endpoint slope')
        require(constant > 0 and constant % 2 == 1 and slope % 2 == 0,
                'valuation does not hold on the entire progression')
    require(constant > 1, 'a supplied witness may need terminal padding')
    require(slope > 0, 'endpoint lower bound is not monotone')
    return constant, slope


def main():
    raw = (HERE/'common-rank-clock-inputs.json').read_bytes()
    inputs = json.loads(raw)
    results = []
    for row in inputs['rows']:
        a,b,c,K,rho = [row[k] for k in ('a','b','c','K','residue')]
        modulus = 3**b
        multiplier = ((rho+1)*pow(2**K,-1,modulus)) % modulus
        if multiplier == 0:
            multiplier = modulus
        M = 2**K*multiplier-1
        N,remainder = divmod(2**a*M+c,modulus)
        require(remainder == 0 and 0 < N < M, 'ordinary parameter guard failed')
        require(M % 2**K == 2**K-1 and M % modulus == rho, 'CRT guard failed')
        step_M,step_N = 2**K*modulus, 2**(K+a)
        arms = {}
        for label,coefficient in [('source',128),('target',64)]:
            old_word,new_word = row[label+'_old'],row[label+'_new']
            old,old_slope = affine_prefix(coefficient*M+1, coefficient*step_M, old_word)
            new,new_slope = affine_prefix(coefficient*N+1, coefficient*step_N, new_word)
            shift = row[label+'_J']
            factor = Fraction(4)**shift
            require(old == factor*new+(factor-1)/3, 'endpoint J identity failed')
            require(old_slope == factor*new_slope, 'whole-cylinder J slope failed')
            delta = sum(new_word)-sum(old_word)-2*shift
            require(delta == a, 'clock increment differs from the rank guard')
            arms[label] = {'minimum_old':old,'minimum_new':new,
                           'slope_old':old_slope,'slope_new':new_slope,
                           'exact_old_to_new_clock_change':delta}
        require(402**a < 200**a * 3**b, 'common-rank scale guard failed')
        require(64*c+3**b < 2**a, 'shifted source height guard failed')
        require(27*c+3**b < 2**a, 'psi-source shifted height guard failed')
        results.append({'reference':row['reference'],'a':a,'b':b,'arms':arms})
    require((21091+1)*200**30 < (19483+1)*201**30,
            'expanding balanced return does not pass the score guard')
    print(json.dumps({'status':'PASS','scope':'exact affine tables and supplied-clock guards; no global coverage',
                      'inputs_sha256':hashlib.sha256(raw).hexdigest(),
                      'source':inputs['source'],'rows':results,
                      'affine_prefix_tables':4*len(results),
                      'no_terminal_padding_required':True,
                      'binary_source_height_guard':True,
                      'psi_source_height_guard':True,
                      'general_padded_templates_covered':False,
                      'expanding_return_score_guard':True},indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
