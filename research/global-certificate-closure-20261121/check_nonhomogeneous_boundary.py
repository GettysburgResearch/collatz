#!/usr/bin/env python3
"""Exact replay of NB1--NB3; does not test unknown convergence to infer it."""
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json


def need(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut(n):
    need(n > 0, 'positive ordinary input')
    return (3*n+1)//2 if n % 2 else n//2


def odd_replay(n, word, terminal=False):
    for a in word:
        need(n > 1 and n % 2, 'positive odd preterminal state')
        z = 3*n+1
        actual = (z & -z).bit_length()-1
        need(actual == a, 'exact accelerated exponent')
        n = z >> a
    if terminal:
        need(n == 1, 'first-hit endpoint')
    return n


def correction(word):
    acc, clock = 0, 0
    for exponent in word:
        acc = 3*acc + 2**clock
        clock += exponent
    return acc, clock


def lift_exponent(p, c):
    s, period, modulus = 1, 2, 3
    goal = 1 + c*3**p
    for _ in range(p):
        modulus *= 3
        choices = [s + j*period for j in range(3)
                   if 5*pow(2, s+j*period, modulus) % modulus == goal % modulus]
        need(len(choices) == 1, 'unique ternary exponent lift')
        s = choices[0]
        period *= 3
    need(period == 2*3**p and s % 2 == 1, 'full exponent class')
    return s, period


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    prefix_checks = 0
    for m in range(41):
        for b in (4, 5, 7, 16):
            word = (1,) + (3,)*m + (b,)
            B, L = correction(word)
            p, h = m+2, 3*m+4
            need(5*B == 3**p + 2**h, 'correction identity')
            modulus = 3**p
            q = B*pow(2**L, -1, modulus) % modulus
            if q % 2 == 0:
                q += modulus
            for extra in (0, 2):
                endpoint = q + extra*modulus
                x = (2**L*endpoint-B)//modulus
                need(odd_replay(x, word) == endpoint, 'source prefix endpoint')
                K = (5*2**(b-3)*endpoint-1)//modulus
                need(K > 0 and K % 2 and 5*x+1 == 2**h*K, 'exact binary valuation')
                y = 5*x
                for t in range(h):
                    need(y == 2**(h-t)*3**t*K-1 and y > 1 and y % 2,
                         'forced odd shortcut input')
                    y = shortcut(y)
                need(y == 3**(2*m+2)*(5*2**(b-3)*endpoint-1)-1,
                     'nonhomogeneous endpoint debt')
                need(y > 1 and y % 2 == 0, 'even endpoint after the forced run')
                prefix_checks += 1
    terminal_examples = []
    for m in range(9):
        p, h = m+2, 3*m+4
        c = 2 if h % 2 == 0 else 1
        s, period = lift_exponent(p, c)
        for j in (0, 1):
            gap = s + j*period + 3
            word = (1,) + (3,)*m + (gap,)
            B, L = correction(word)
            numerator = 2**L-B
            need(numerator % 3**p == 0, 'complete ordinary source integrality')
            x = numerator//3**p
            need(x % 3 == 2 and x % 2, 'odd ternary-unit source')
            odd_replay(x, word, terminal=True)
            K = (5*x+1)//2**h
            need(K % 3 == c and K % 2, 'prescribed final ternary residue')
            E = 3**h*K-1
            grade = L-2*p
            bound = Fraction(45,16)*Fraction(9,16)**m
            need(Fraction(E, 2**(h+grade)) < bound < 4,
                 'exact grade obstruction')
            terminal_examples.append({'source_rank': p, 'source_bits': x.bit_length(),
                                      'last_gap': gap, 'forced_target_odd_inputs': h})
    report = {'status':'PASS: NB1-NB3 only; no full Collatz proof',
              'arbitrary_endpoint_prefix_checks':prefix_checks,
              'actual_first_hit_examples':terminal_examples,
              'proof_sha256':hashlib.sha256(Path(__file__).with_name('NONHOMOGENEOUS_BOUNDARY.md').read_bytes()).hexdigest(),
              'full_collatz_proved':False}
    payload = json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(payload)
    print(json.dumps({'status':report['status'],'prefix_checks':prefix_checks,
                      'actual_first_hit_examples':len(terminal_examples),
                      'report_sha256':hashlib.sha256(payload.encode()).hexdigest()},sort_keys=True))


if __name__ == '__main__':
    main()
