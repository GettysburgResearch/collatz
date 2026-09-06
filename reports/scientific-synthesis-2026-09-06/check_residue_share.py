#!/usr/bin/env python3
"""One bounded reproduction of the rejected one-third survivor-mass ceiling.

Uses the tail inequalities in ROUTE1_MELLIN.md, (7)--(8), and exact rational
arithmetic. It imports no source generator or verifier. This is neither a
full protocol replay nor independent proof verification of the tail bounds.
No files are written. All checks remain active under optimized Python.
"""
from fractions import Fraction as F
from math import isqrt
import json

H, K, N, B = 64, 19, 65536, 2**96


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def numerator(n: int) -> int:
    # floor(B / n**(3/2)), with integer verification of the enclosure.
    d = n**3
    a = isqrt(B*B // d)
    need(a*a*d <= B*B < (a+1)*(a+1)*d, 'weight enclosure')
    return a


def encoded(x: F) -> list[int]:
    return [x.numerator, x.denominator]


def main() -> None:
    cone = set(range(1, H+1))
    for _ in range(K):
        cone |= {2*y for y in cone} | {(2*y-1)//3 for y in cone if y % 3 == 2}
    need(len(cone) == 18847, 'complete inverse-cone size')
    need(max(cone) == H*2**K, 'inverse-cone maximum')

    root = isqrt(N)
    need(root*root == N, 'rational zeta-tail endpoint')
    finite = sum(numerator(n) for n in range(1, N+1))
    tail = F(2, root) - F(1, 2*root**3)
    zlo = F(finite, B) + tail
    zhi = F(finite+N, B) + tail + F(3, 16*root**5)
    cone_sum = sum(numerator(n) for n in cone)
    mlo = zlo - F(cone_sum+len(cone), B)
    mhi = zhi - F(cone_sum, B)

    first = 98  # smallest y=2 mod3 with y>(3H+1)/2
    terms = range(first, N+1, 3)
    finite_q = sum(numerator(y) for y in terms)
    m = first + 3*len(terms)
    a = numerator(m)
    coefficient = F(2*m, 3) + F(1, 2)
    qlo = F(finite_q, B) + coefficient*F(a, B)
    qhi = F(finite_q+len(terms), B) + (coefficient+F(9, 16*m))*F(a+1, B)
    eligible = [y for y in cone if y >= first and y % 3 == 2]
    eligible_sum = sum(numerator(y) for y in eligible)
    qlo -= F(eligible_sum+len(eligible), B)
    qhi -= F(eligible_sum, B)

    need(0 < mlo <= mhi and 0 < qlo <= qhi, 'positive directed intervals')
    margin = 3*qlo-mhi
    need(margin > 0, 'one-third counterexample not certified')
    print(json.dumps({
        'scope': 'H=64, k=19, s=3/2 only; source tail inequalities used, no all-time claim',
        'cone_vertices': len(cone), 'cone_maximum': max(cone),
        'source_sum_cutoff': N, 'fixed_point_denominator': B,
        'M_interval': [encoded(mlo), encoded(mhi)],
        'Q_interval': [encoded(qlo), encoded(qhi)],
        'certified_3Q_lower_minus_M_upper': encoded(margin),
        'verdict': 'PASS: Q_19 > M_19/3; uniform one-third ceiling is false'
    }, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
