#!/usr/bin/env python3
"""Exact new controls for the polynomial countermodel, not a cycle census."""

from fractions import Fraction
from functools import reduce
from math import gcd
import json


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def evaluate_desc(coeffs, x):
    value = 0
    for coefficient in coeffs:
        value = value * x + coefficient
    return value


def power_two_exponent(n):
    require(n > 0 and n & (n - 1) == 0, "not a positive power of two")
    return n.bit_length() - 1


def floor_log2_fraction(q):
    e = q.numerator.bit_length() - q.denominator.bit_length()
    if e >= 0:
        return e - (q.numerator < q.denominator * (1 << e))
    return e - (q.numerator * (1 << (-e)) < q.denominator)


def check(A, d):
    three_d = 3**d
    D = 2**A - three_d
    require(d >= 16 and gcd(A, d) == 1, "reduced degree hypotheses")
    require(D > 0 and 192 * D <= three_d, "near-critical clock hypothesis")
    lower = (4 * three_d + D - 1) // D
    m = 7 + 192 * ((lower - 7 + 191) // 192)
    require(m >= lower and m % 192 == 7, "minimum coefficient choice")
    require(4 * three_d <= m * D <= 5 * three_d, "m eta bounds")

    y = [m]
    for _ in range(d - 1):
        y.append(3 * y[-1] // 2 + 1)
    v = [(1 << j) * value for j, value in enumerate(y)]
    carry = [v[j] - 3 * v[j - 1] for j in range(1, d)]
    exponents = [power_two_exponent(c) for c in carry]
    last = m * (2**A) - 3 * v[-1]
    q = carry + [last]
    require(len(q) == d and q[0] == 1, "monic residual numerator")
    require(all(c > 0 for c in q), "positive numerator coefficients")
    require(last >= 2 * three_d + 3 * 2**d, "terminal positivity lower bound")

    require(reduce(gcd, v) == 1, "primitive J")
    require(all(c > 0 for c in v), "positive J coefficients")
    require(v[0] == m and v[1] == 3 * m + 1, "leading Bezout certificate")
    require(all(c % 3 != 0 for c in v), "three-adic coefficient units")
    require(all(c % (1 << j) == 0 for j, c in enumerate(v)), "two-adic root certificate")

    M = Fraction(3, 2) ** (d - 1) * (m + 1) - 1
    for j in range(1, d):
        ratio = Fraction(v[j], v[j - 1])
        require(3 + 1 / M <= ratio <= 3 + Fraction(1, m), "exact root-annulus certificate")
    require(Fraction(3, 2) ** (d - 1) * m <= M, "maximum normalization bound")

    # Direct coefficient comparison of (X-3)J - mF0 = Q0.
    product = [0] * (d + 1)
    for j, coefficient in enumerate(v):
        product[j] += coefficient
        product[j + 1] -= 3 * coefficient
    product[0] -= m
    product[-1] += m * 2**A
    require(product[0] == 0 and product[1:] == q, "complete polynomial identity")

    q3 = evaluate_desc(q, 3)
    require(q3 == m * D, "complete distinguished evaluation")
    require(gcd(D, q3) == D, "full numerical cancellation")
    ratio = Fraction(D, 1) / M
    eta = Fraction(D, three_d)
    require(ratio >= eta * eta * 2**d / 4, "exponential separation lower bound")
    require(exponents[:6] == [0, 1, 2, 4, 5, 5], "retained zero-gap failure")

    # These powered comparisons certify the binomial root radius as well.
    require(Fraction(2**A, 1) <= (3 + Fraction(1, m)) ** d, "binomial upper annulus")
    require(Fraction(2**A, 1) >= (3 + 1 / M) ** d, "binomial lower annulus")

    return {
        "A": A,
        "d": d,
        "m": m,
        "D_bits": D.bit_length(),
        "floor_log2_D_over_M": floor_log2_fraction(ratio),
        "adjacent_root_certificates": d - 1,
        "full_numerical_gcd": "D",
        "first_six_carry_exponents": exponents[:6],
        "status": "PASS: polynomial model; NOT a positive-gap Collatz word",
    }


def main():
    controls = [(401, 253), (485, 306), (886, 559)]
    rows = [check(A, d) for A, d in controls]
    print(json.dumps({
        "scope": "new exact positive-numerator polynomial models only",
        "models": rows,
        "total_adjacent_root_certificates": sum(r["adjacent_root_certificates"] for r in rows),
        "assert_statements_used": False,
        "cycle_search_or_old_control_replay": False,
    }, indent=2))


if __name__ == "__main__":
    main()
