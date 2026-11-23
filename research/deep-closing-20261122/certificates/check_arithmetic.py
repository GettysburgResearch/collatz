#!/usr/bin/env python3
"""Exact finite controls for ARITHMETIC_ATTACK; the all-k proof is written."""
from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def complete(q, word):
    for a in word:
        require(a >= 1, 'positive gap')
        numerator = 3*q+1
        require(numerator % (1 << a) == 0, 'gap divisibility')
        q = numerator >> a
        require(q > 0 and q % 2 == 1, 'positive odd endpoint/exact valuation')
    require(q == 1, 'complete endpoint')


def main():
    R = Fraction(4, 3)
    original = R-R**4
    differences = [R**a-R**4-original for a in (1,2,3)]
    differences += [(R**4-R**a)/2-original for a in (1,2,3)]
    expected = [Fraction(0), Fraction(4,9), Fraction(28,27),
                Fraction(74,27), Fraction(68,27), Fraction(20,9)]
    require(differences == expected, 'six exact permutation differences')
    require([i for i,x in enumerate(differences) if x.denominator == 1] == [0],
            'unique integral difference')
    word = [3,2,2,3,2,3,2,2,2,3,3,2,2,2,2,3,2,3,1,1,2,2,2,3,1,3,
            2,3,2,2,1,3,3,2,2,4,1,1,2,3,4]
    complete(219565229, word)
    require(len(word) == 41 and word.count(4) == 2 and max(word) == 4,
            'replacement histogram')
    require(2*219565229 > 4*58849709, 'strict source enlargement')
    bad = word.copy()
    bad[0] = 2
    rejected = False
    try:
        complete(219565229, bad)
    except ValueError:
        rejected = True
    require(rejected, 'wrong gap control must fail')
    rejected = False
    try:
        complete(219565229, word[:-1])
    except ValueError:
        rejected = True
    require(rejected, 'incomplete endpoint control must fail')
    print(json.dumps({
        'success': True,
        'six_shift_differences': [str(x) for x in differences],
        'replacement_odd_source': 219565229,
        'replacement_powered_source': 439130458,
        'source_to_replace': 235398836,
        'complete_odd_gaps': len(word),
        'four_count': word.count(4),
        'rejected_damaged_controls': 2,
        'scope': 'Finite arithmetic controls only; the all-length permutation theorem is written.'
    }, sort_keys=True))


if __name__ == '__main__':
    main()
