#!/usr/bin/env python3
"""Exact identities and one ordinary control for the cyclotomic norm attack.

This is not a cycle census. The all-parameter argument is written in
CYCLOTOMIC_ZERO_FIBER.md. No external symbolic-algebra package is needed.
"""
from fractions import Fraction
from math import gcd
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly or [0]


def add(a, b):
    result = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        result[i] += value
    for i, value in enumerate(b):
        result[i] += value
    return trim(result)


def mul(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            result[i + j] += av * bv
    return trim(result)


def scale(a, value):
    return trim([value * x for x in a])


def mono(degree, coefficient=1):
    return [0] * degree + [coefficient]


def evaluate(poly, x):
    result = 0
    for value in reversed(poly):
        result = result * x + value
    return result


def expect_rejected(fn):
    try:
        fn()
    except ValueError:
        return 1
    raise ValueError('damaged control was accepted')


def replay_gaps(source, gaps):
    q = source
    require(q > 0 and q % 2 == 1, 'positive odd source')
    for gap in gaps:
        require(gap >= 1, 'positive gap')
        numerator = 3 * q + 1
        divisor = 1 << gap
        require(numerator % divisor == 0, 'gap divisibility')
        q = numerator // divisor
        require(q > 0 and q % 2 == 1, 'exact valuation and positive odd next state')
    return q


def main():
    heights = [0, 0, 1, 1, 0, 2, 1, 0, 0, 1, 1, 2]
    r = [1 << k for k in heights]
    phi12 = [1, 0, -1, 0, 1]
    t = [1, 1, 3, 3, 3, 6, 2, 4]
    tr = list(reversed(t))
    f = mul([-1, 0, 0, 0, 0, 0, 1], [1, 0, 1])
    u = [-1353, -1926, -931, -1365, -971, -600, -392]
    v = [-137, -413, -159, -21, 186, -21, 208, 392]
    require(mul(phi12, t) == r, 'exact Phi12 numerator factor')
    require(mul(phi12, f) == add(mono(12), [-1]), 'whole denominator factor')
    require(add(mul(u, f), mul(v, tr)) == [805], 'integer Bezout identity')

    a, b = 5, 3
    aa, pp = 12 * a, 12 * b
    positions = [a * j + i + heights[j] for j in range(12) for i in range(b)]
    require(positions[0] == 0 and positions[-1] < aa, 'position endpoints')
    require(all(x < y for x, y in zip(positions, positions[1:])), 'strict positions')
    gaps = [y - x for x, y in zip(positions, positions[1:])]
    gaps.append(aa - positions[-1])
    require(all(x >= 1 for x in gaps) and sum(gaps) == aa, 'complete positive gap word')
    word = [int(i in positions) for i in range(aa)]
    period = next(d for d in range(1, aa + 1)
                  if aa % d == 0 and all(word[i] == word[i % d] for i in range(aa)))
    require(period == aa and 4 * aa < 7 * pp, 'primitive word in the nontrivial-cycle cone')

    qpoly = [0] * pp
    for i, position in enumerate(positions):
        qpoly[pp - 1 - i] = 1 << position
    fpoly = add(mono(pp), [-(1 << aa)])
    gpoly = add(add(mono(4 * b), mono(2 * b, -(1 << (2 * a)))), [1 << (4 * a)])
    hpoly = [1 << (b - 1 - i) for i in range(b)]
    bpoly = [0] * (7 * b + 1)
    for j, coefficient in enumerate(tr):
        bpoly[j * b] = coefficient * (1 << (a * (7 - j)))
    frem = mul(add(mono(6 * b), [-(1 << (6 * a))]),
               add(mono(2 * b), [1 << (2 * a)]))
    require(mul(gpoly, frem) == fpoly, 'complete degree36 polynomial factorization')
    require(mul(mul(hpoly, gpoly), bpoly) == qpoly, 'complete numerator factorization')

    ss, tt = 1 << a, 3 ** b
    denominator = (1 << aa) - 3 ** pp
    numerator = sum((1 << position) * 3 ** (pp - 1 - i)
                    for i, position in enumerate(positions))
    require(numerator == evaluate(qpoly, 3), 'position/polynomial carry agreement')
    gg = tt ** 4 - ss ** 2 * tt ** 2 + ss ** 4
    residual = (ss ** 6 - tt ** 6) * (ss ** 2 + tt ** 2)
    bb = evaluate(bpoly, 3)
    require(denominator == gg * residual, 'full denominator retained')
    require(numerator == (tt - (1 << b)) * gg * bb, 'full numerator retained')
    require(gcd(residual, bb) != 0 and 805 % gcd(residual, bb) == 0,
            'residual gcd divides805')
    require(residual >= 12 * tt ** 7 > 805 * tt, 'strict size contradiction')
    require(numerator % denominator != 0, 'nonintegral positive rational cycle')
    require(denominator == 1002826869309847855 and numerator == 8287225771885636121,
            'frozen complete values')
    require(gg == 833521 and gcd(numerator, denominator) == 5834647,
            'retained cyclotomic/common factors')

    # One extra binary condition makes the last accelerated endpoint odd.
    modulus = 1 << (aa + 1)
    source = (((1 << aa) - numerator) * pow(3 ** pp, -1, modulus)) % modulus
    endpoint = replay_gaps(source, gaps)
    require(endpoint != source, 'ordinary source does not close')
    require((1 << aa) * endpoint == 3 ** pp * source + numerator,
            'unchanged ordinary source affine identity')

    damaged_r = r[:]
    damaged_r[3] += 1
    damaged_v = v[:]
    damaged_v[1] += 1
    damaged_gaps = gaps[:]
    damaged_gaps[0] += 1
    rejected = expect_rejected(lambda: require(mul(phi12, t) == damaged_r,
                                                'damaged Phi12 identity'))
    rejected += expect_rejected(lambda: require(add(mul(u, f), mul(damaged_v, tr)) == [805],
                                                 'damaged Bezout identity'))
    rejected += expect_rejected(lambda: replay_gaps(source, damaged_gaps))
    require(rejected == 3, 'damage rejection count')
    print(json.dumps({
        'status': 'PASS', 'A': aa, 'p': pp, 'least_parity_period': period,
        'full_denominator': denominator, 'full_numerator': numerator,
        'common_cyclotomic_factor': gg, 'full_gcd': gcd(numerator, denominator),
        'reduced_rational_cycle': str(Fraction(numerator, denominator)),
        'bezout_constant': 805, 'ordinary_source': source, 'ordinary_endpoint': endpoint,
        'exact_odd_gaps': len(gaps), 'damaged_controls_rejected': rejected,
        'scope': 'Exact polynomial identities and one positive ordinary source; all-parameter family exclusion is written, unrestricted cycle exclusion remains open.'
    }, indent=2))


if __name__ == '__main__':
    main()
