#!/usr/bin/env python3
"""Exact finite controls for the infinite-optimal-ray attempted closure.

The tested positive trajectories are finite known examples. The real coefficient
is a finite later partial sum, so this is not an execution of an escaping orbit.
"""
from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def valuation(n, p):
    require(n != 0, 'valuation input must be nonzero')
    n = abs(n)
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def padic_abs(q, p):
    q = Fraction(q)
    if q == 0:
        return Fraction(0)
    e = valuation(q.numerator, p) - valuation(q.denominator, p)
    return Fraction(1, p ** e) if e >= 0 else Fraction(p ** (-e))


def path(n, count):
    states, gaps, clocks, carries = [n], [], [0], [0]
    for _ in range(count):
        v = 3 * states[-1] + 1
        a = valuation(v, 2)
        require(a >= 1, 'positive odd state has a positive gap')
        q = v // 2 ** a
        gaps.append(a)
        states.append(q)
        carries.append(3 * carries[-1] + 2 ** clocks[-1])
        clocks.append(clocks[-1] + a)
    return states, gaps, clocks, carries


def text(q):
    return str(Fraction(q))


def main():
    starts = [1, 3, 7, 27, 31, 97, 871]
    lengths = [2, 3, 8, 17, 32, 64]
    counts = dict(physical_prefixes=0, binary_valuations=0,
                  finite_tail_products=0, geometric_tail_bounds=0,
                  negative_anchor_congruences=0, negative_cycle_phases=0)
    examples = []
    for n in starts:
        for total in lengths:
            q, gaps, A, C = path(n, total)
            S = [Fraction(C[k], 3 ** k) for k in range(total + 1)]
            for k in range(1, total + 1):
                require(2 ** A[k] * q[k] == 3 ** k * n + C[k], 'physical identity')
                counts['physical_prefixes'] += 1
                require(valuation(3 ** k * n + C[k], 2) == A[k], 'exact binary valuation')
                require(C[k] % 3 != 0, 'primitive vector')
                counts['binary_valuations'] += 1
                if k < total:
                    tail = sum((Fraction(2 ** (A[j] - A[k]), 3 ** (j - k + 1))
                                for j in range(k, total)), Fraction(0))
                    require(S[total] - S[k] == Fraction(2 ** A[k], 3 ** k) * tail,
                            'same-clock shifted tail')
                    X, Y = 3 ** k, C[k]
                    product = (abs(X * (S[total] * X - Y))
                               * padic_abs(X * (n * X + Y), 2)
                               * padic_abs(X * Y, 3))
                    require(product == tail, 'finite analogue of exact all-place product')
                    counts['finite_tail_products'] += 1
                    require(tail >= 1 - Fraction(2, 3) ** (total - k), 'geometric tail bound')
                    counts['geometric_tail_bounds'] += 1
                if 2 ** A[k] < 3 ** k:
                    anchor = Fraction(-C[k], 3 ** k - 2 ** A[k])
                    require(padic_abs(Fraction(q[k]) - anchor, 3) <= Fraction(1, 3 ** k),
                            'actual endpoint/negative-anchor congruence')
                    require(anchor.denominator % 6 in (1, 5), 'anchor denominator is a 6-unit')
                    counts['negative_anchor_congruences'] += 1
                    z = anchor
                    for a in gaps[:k]:
                        require(z < 0 and padic_abs(z, 2) == 1, 'negative odd rational phase')
                        z_next = (3 * z + 1) / 2 ** a
                        require(padic_abs(z_next, 2) == 1, 'exact rational gap')
                        counts['negative_cycle_phases'] += 1
                        z = z_next
                    require(z == anchor, 'rational cycle closes')
                    if n == 27 and k in (1, 3, 6, 8) and total == 17:
                        examples.append(dict(start=n, odd_clock=k, gap_sum=A[k], target=q[k],
                                             carry=C[k], anchor=text(anchor)))
    print(json.dumps(dict(
        scope='Finite exact identities only; no escaping input, infinite real limit, or universal repair is asserted.',
        starts=starts, lengths=lengths, counts=counts, anchor_examples=examples,
        success=True), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
