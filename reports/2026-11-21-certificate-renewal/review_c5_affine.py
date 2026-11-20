#!/usr/bin/env python3
"""Independent all-lift replay, without importing the submitted C5 checker."""
from fractions import Fraction
import json

ROWS = [
    ('A', (1889568, 1686382), (524288, 467911),
     (2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 3, 1, 3, 1),
     (2, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2),
     7656401, 8177135),
    ('B', (1889568, 1196494), (1048576, 663969),
     (2, 2, 2, 1, 1, 3, 2, 1, 2, 2, 3, 1, 3, 1),
     (2, 2, 4, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2),
     4822049, 7645694),
]


def run(coefficients, word):
    slope, base = coefficients
    for exponent in word:
        numerator = 3*base+1
        if (numerator & -numerator).bit_length()-1 != exponent:
            raise ValueError('incorrect base valuation')
        slope = Fraction(3*slope, 1 << exponent)
        base = numerator >> exponent
        if slope.denominator != 1 or slope.numerator % 2 or base <= 1:
            raise ValueError('nonphysical affine lift')
    return int(slope), base


def main():
    results = []
    for name, (modulus, residue), (child_slope, child_base), ws, wt, e, q in ROWS:
        traces = [
            run((128*modulus, 128*residue+1), (2, 2, 2, 5)),
            run((128*child_slope, 128*child_base+1), ws),
            run((64*modulus, 64*residue+1), (2, 2, 2, 1, 2)),
            run((64*child_slope, 64*child_base+1), wt),
        ]
        if traces[0] != traces[1] or traces[2] != traces[3]:
            raise ValueError('paired endpoint mismatch')
        if not (modulus > child_slope > 0 and residue > child_base > 0):
            raise ValueError('strict height decrease fails')
        if pow(2, e, 3**15) != q or e % 162 != 119:
            raise ValueError('Mersenne exponent residue fails')
        results.append({
            'rule': name,
            'source_endpoint': traces[0],
            'target_endpoint': traces[2],
            'source_odd_steps': len(ws),
            'target_odd_steps': len(wt),
        })
    print(json.dumps({'status': 'PASS', 'independent_affine_replay': results},
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
