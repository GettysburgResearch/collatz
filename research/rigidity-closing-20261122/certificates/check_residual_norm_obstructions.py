#!/usr/bin/env python3
"""Targeted exact checks of two losses in a whole-denominator norm strategy.

No cycle search is performed. The unbounded family is proved symbolically
in CYCLOTOMIC_ZERO_FIBER.md, Sections 8--9. Standard library only.
"""
from fractions import Fraction
from math import gcd
import json
from check_cyclotomic_zero_fiber import (
    add, evaluate, expect_rejected, mono, mul, require, scale, trim,
)


def divrem(a, b):
    a = [Fraction(x) for x in trim(a)]
    b = [Fraction(x) for x in trim(b)]
    require(b != [0], 'nonzero polynomial divisor')
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        degree = len(a) - len(b)
        coefficient = a[-1] / b[-1]
        q[degree] += coefficient
        for i, value in enumerate(b):
            a[degree + i] -= coefficient * value
        a = trim(a)
    return trim(q), trim(a)


def exact_div(a, b):
    q, r = divrem(a, b)
    require(r == [0], 'exact polynomial division')
    require(all(x.denominator == 1 for x in q), 'integer quotient')
    return [int(x) for x in q]


def polynomial_gcd(a, b):
    while b != [0]:
        _, remainder = divrem(a, b)
        a, b = b, remainder
    return scale(a, Fraction(1, a[-1]))


def homogeneous_substitution(poly, power, s):
    degree = len(poly) - 1
    result = [0] * (degree * power + 1)
    for i, coefficient in enumerate(poly):
        result[i * power] = coefficient * s ** (degree - i)
    return trim(result)


def bareiss_determinant(matrix):
    matrix = [row[:] for row in matrix]
    n = len(matrix)
    require(all(len(row) == n for row in matrix), 'square Bareiss matrix')
    previous, sign = 1, 1
    for k in range(n - 1):
        if matrix[k][k] == 0:
            pivot_row = next((i for i in range(k + 1, n) if matrix[i][k]), None)
            if pivot_row is None:
                return 0
            matrix[k], matrix[pivot_row] = matrix[pivot_row], matrix[k]
            sign = -sign
        pivot = matrix[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = matrix[i][j] * pivot - matrix[i][k] * matrix[k][j]
                require(numerator % previous == 0, 'Bareiss exact division')
                matrix[i][j] = numerator // previous
            matrix[i][k] = 0
        previous = pivot
    return sign * matrix[-1][-1]


def resultant(a, b):
    m, n = len(a) - 1, len(b) - 1
    require(m > 0 and n > 0, 'positive degrees in displayed resultant')
    aa, bb = list(reversed(a)), list(reversed(b))
    matrix = [[0] * (m + n) for _ in range(m + n)]
    for shift in range(n):
        matrix[shift][shift:shift + m + 1] = aa
    for shift in range(m):
        matrix[n + shift][shift:shift + n + 1] = bb
    return bareiss_determinant(matrix), m + n


def least_period(word):
    length = len(word)
    return next(d for d in range(1, length + 1)
                if length % d == 0
                and all(word[j] == word[j % d] for j in range(length)))


def profile_control(m, n):
    require(m >= 2 and n >= 2 and m != n and gcd(m, n) == 1, 'profile parameters')
    ll = 2 * m * n
    coeffs = [1 + int(j % (2 * m) == 0) + int(j % (2 * n) == 1)
              for j in range(ll)]
    require(set(coeffs) == {1, 2}, 'disjoint support gives powers of two')
    require(least_period(coeffs) == ll, 'primitive coefficient profile control')
    full = add(mono(ll), [-1])
    hm = add(mono(2 * m), [-1])
    hn = add(mono(2 * n), [-1])
    intersection = [-1, 0, 1]
    hh = exact_div(mul(hm, hn), intersection)
    gg = exact_div(full, hh)
    require(len(hh) - 1 == 2 * m + 2 * n - 2, 'exact residual degree')
    require(polynomial_gcd(full, coeffs) == gg, 'exact profile gcd control')
    geometric = exact_div(full, [-1, 1])
    geometric = add(geometric, exact_div(full, hm))
    geometric = add(geometric, mul([0, 1], exact_div(full, hn)))
    require(geometric == coeffs, 'exact profile geometric identity')

    aa, pp, ss, tt = 5 * ll, 3 * ll, 32, 27
    positions = [5 * j + r + (coeffs[j] - 1) for j in range(ll) for r in range(3)]
    require(positions[0] == 1 and positions[-1] < aa, 'valid position endpoints')
    require(all(a < b for a, b in zip(positions, positions[1:])), 'strict one positions')
    word = [int(j in positions) for j in range(aa)]
    require(least_period(word) == aa and 4 * aa < 7 * pp, 'primitive cone word')
    ff = add(mono(pp), [-(1 << aa)])
    qq = [0] * pp
    for i, d in enumerate(positions):
        qq[pp - 1 - i] = 1 << d
    ghom = homogeneous_substitution(gg, 3, ss)
    hhom = homogeneous_substitution(hh, 3, ss)
    require(mul(ghom, hhom) == ff, 'whole denominator polynomial')
    require(polynomial_gcd(ff, qq) == ghom, 'complete polynomial gcd after embedding')
    residual_q = exact_div(qq, ghom)
    residual_d = abs(evaluate(hhom, 3))
    expected = ((ss ** (2 * m) - tt ** (2 * m)) *
                (ss ** (2 * n) - tt ** (2 * n))) // (ss * ss - tt * tt)
    require(residual_d == expected, 'exact residual denominator')
    denominator, numerator = (1 << aa) - 3 ** pp, evaluate(qq, 3)
    require(denominator // gcd(denominator, numerator) ==
            residual_d // gcd(residual_d, abs(evaluate(residual_q, 3))),
            'distinguish polynomial cancellation from integer evaluation gcd')
    if n == m + 1:
        require(aa == 10 * m * (m + 1) and residual_d < 1 << (20 * m + 2),
                'subexponential residual-size inequality')
    return {'m': m, 'n': n, 'A': aa, 'p': pp,
            'polynomial_residual_degree': len(hhom) - 1,
            'polynomial_residual_denominator': residual_d,
            'reduced_rational_denominator': denominator // gcd(denominator, numerator)}


def main():
    profiles = [profile_control(2, 3), profile_control(3, 4)]
    aa, pp, positions = 13, 8, (0, 1, 2, 3, 4, 6, 8, 9)
    ff = add(mono(pp), [-(1 << aa)])
    qq = [0] * pp
    for i, d in enumerate(positions):
        qq[pp - 1 - i] = 1 << d
    require(polynomial_gcd(ff, qq) == [1], 'coprime full polynomials')
    word = [int(j in positions) for j in range(aa)]
    require(least_period(word) == aa and 4 * aa < 7 * pp, 'primitive norm control')
    determinant, dimension = resultant(ff, qq)
    expected_resultant = -(1 << 71) * 7 * 233 ** 2
    require(dimension == 15 and determinant == expected_resultant, 'exact Sylvester resultant')
    denominator = (1 << aa) - 3 ** pp
    numerator = evaluate(qq, 3)
    require(denominator == 1631 == 7 * 233 and numerator == 7553, 'full carry values')
    require(determinant % denominator == 0 and numerator % denominator != 0,
            'norm contains full denominator but distinguished evaluation does not')
    require(gcd(numerator, denominator) == 7, 'evaluation gcd')
    require(evaluate(ff, 3) % 7 == evaluate(qq, 3) % 7 == 0, 'root3 at prime7')
    require(evaluate(ff, -3) % 233 == evaluate(qq, -3) % 233 == 0,
            'conjugate root negative3 at prime233')
    require(evaluate(qq, 3) % 233 == 97, 'distinguished root3 fails at prime233')
    rotated_word, rotated_q = word[:], qq[:]
    for _ in range(aa):
        first_letter = rotated_word[0]
        rotated_word = rotated_word[1:] + rotated_word[:1]
        rotated_positions = [j for j, digit in enumerate(rotated_word) if digit]
        next_q = [0] * pp
        for i, d in enumerate(rotated_positions):
            next_q[pp - 1 - i] = 1 << d
        expected_twice = (add(mul([0, 1], rotated_q), scale(ff, -1))
                          if first_letter else rotated_q)
        require(scale(next_q, 2) == expected_twice, 'exact cyclic rotation polynomial identity')
        require(evaluate(next_q, 3) % 7 == 0 and evaluate(next_q, -3) % 233 == 0,
                'same conjugate roots across rotations')
        require(evaluate(next_q, 3) % 233 != 0,
                'distinguished evaluation still fails across rotations')
        rotated_q = next_q
    require(rotated_q == qq, 'complete cyclic return of the word')
    rejected = expect_rejected(lambda: require(determinant == expected_resultant + 233,
                                                'damaged resultant certificate'))
    print(json.dumps({
        'status': 'PASS', 'profile_identity_controls': profiles,
        'norm_control': {'A': aa, 'p': pp, 'D': denominator, 'C': numerator,
                         'polynomial_gcd': 1, 'sylvester_dimension': dimension,
                         'resultant': determinant,
                         'resultant_factorization': '-2^71 * 7 * 233^2',
                         'full_denominator_divides_resultant': True,
                         'evaluation_gcd': gcd(denominator, numerator),
                         'Q3_mod233': evaluate(qq, 3) % 233,
                         'cyclic_rotation_identities_checked': aa},
        'damaged_controls_rejected': rejected,
        'scope': 'Exact controls of two structural norm obstructions; no cycle census and no unrestricted cycle exclusion.'
    }, indent=2))


if __name__ == '__main__':
    main()
