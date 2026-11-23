#!/usr/bin/env python3
"""Generate an exact continued-fraction certificate for P^m Q^n cycle exclusion.

The proof that this finite certificate covers every m,n uses Matveev's
published theorem and the written physical-divisibility argument. This
program neither tests a large finite sample nor claims to formalize Matveev.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import json
import math


def interval(r, terms):
    lo = sum((2*r**(2*j+1)/(2*j+1) for j in range(terms)), F(0))
    hi = lo+2*r**(2*terms+1)/((2*terms+1)*(1-r*r))
    return lo, hi


def pair(x):
    return [str(x.numerator), str(x.denominator)]


def generate():
    terms, c, cutoff = 96, 10**12, 10**14
    l2, u2 = interval(F(1,3), terms)
    l3, u3 = interval(F(1,2), terms)
    lo, hi = l3/u2, u3/l2
    pa, pb, qa, qb = 0, 1, 1, 0
    rows = []
    while True:
        digit, other = math.floor(lo), math.floor(hi)
        if digit != other:
            raise ValueError('insufficient rational logarithm precision')
        p, q = digit*pb+pa, digit*qb+qa
        row = {'partial_quotient':digit, 'p':p, 'q':q}
        if q > 8*cutoff:
            row['status'] = 'terminal-denominator'
            rows.append(row)
            break
        low, high = p*l2-q*u3, p*u2-q*l3
        if high < 0:
            row['status'] = 'lower-convergent'
        elif low > 0:
            scale = 3//math.gcd(3,2*q-p)
            m, n = scale*(2*q-p)//3, scale*(7*p-11*q)//3
            row.update(scale=scale, min_m=m, min_n=n)
            if m <= 0 or n <= 0 or n >= m:
                row['status'] = 'outside-positive-parameter-cone'
            elif m >= cutoff:
                row['status'] = 'above-pin-cutoff'
            else:
                exponent = min(11*m,66)
                if scale*low <= F(84,2**exponent):
                    raise ValueError('candidate not excluded')
                row.update(status='separated', dyadic_exponent=exponent)
        else:
            raise ValueError('uncertain convergent side')
        rows.append(row)
        pa, pb, qa, qb = pb, p, qb, q
        lo, hi = 1/(hi-digit), 1/(lo-digit)
    return {
        'schema':'collatz-independent-pin-cycle-exclusion/v1',
        'pin_word':[1,1,4,1,1,1,2], 'twos_word':[2],
        'parameters':'independent integers m>=1,n>=1',
        'matveev_constant':c, 'pin_cutoff_exclusive':cutoff,
        'denominator_cutoff_exclusive':8*cutoff,
        'log_series_terms':terms,
        'log2':{'lower':pair(l2),'upper':pair(u2)},
        'log3':{'lower':pair(l3),'upper':pair(u3)},
        'continued_fraction':rows,
        'scope':'Exact finite arithmetic closure of the written Matveev and physical-legality proof; no universal Collatz claim.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    data=generate()
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'convergents':len(data['continued_fraction']),
        'terminal_denominator':data['continued_fraction'][-1]['q']},indent=2))


if __name__=='__main__':
    main()
