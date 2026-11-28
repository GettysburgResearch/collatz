"""Exact finite certificates for Mersenne crest comparisons at a supplied exponent.

The pivot is 3**(p-width) reduced modulo 2**budget.  Counts include the
distance from that pivot exponent.  Equality of the two reduced endpoints
is an actual-source equality precisely when the augmented counts also agree.
"""
from math import isqrt
import json


def is_prime(n):
    if n < 2 or n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def crt_candidates(k, j):
    odd_modulus = 3 ** (k - 1)
    binary_modulus = 2 ** (j - 2)
    period = odd_modulus * binary_modulus
    first = 1 + odd_modulus * ((-2 * pow(odd_modulus, -1, binary_modulus)) % binary_modulus)
    return first, period


def walk_step(state, odds):
    if state % 2:
        return (3 * state + 1) // 2, odds + 1
    return state // 2, odds


def first_meeting(p, width, budget):
    if not 0 < width < p or budget < 1:
        raise ValueError("positive shorter crests and budget required")
    anchor = pow(3, p - width, 2**budget)
    rows = [(3**j * anchor - 1, j) for j in range(width + 1)]
    for clock in range(1, budget + 1):
        rows = [walk_step(x, q) for x, q in rows]
        if all(row == rows[0] for row in rows[1:]):
            value, q = rows[0]
            return clock, q, value
    return None


def exact_reference(p, width, budget):
    rows = [(3 ** (p - width + j) - 1, j) for j in range(width + 1)]
    for clock in range(1, budget + 1):
        rows = [walk_step(x, q) for x, q in rows]
        if all(row == rows[0] for row in rows[1:]):
            return clock, rows[0][1]
    return None


def terminating_grade(p):
    x = 3**p - 1
    q, t = 0, 0
    while x != 1 and t < 10_000:
        x, q = walk_step(x, q)
        t += 1
    if x != 1:
        raise RuntimeError("verification budget exhausted")
    return 2 * (p + q) - t


if __name__ == "__main__":
    for p in range(3, 90):
        for width in range(1, min(p, 6)):
            reduced = first_meeting(p, width, 120)
            exact = exact_reference(p, width, 120)
            if (reduced and reduced[:2]) != exact:
                raise AssertionError((p, width, reduced, exact))
    grades = [terminating_grade(r) for r in range(1, 20)]
    if grades[-1] in grades[:-1]:
        raise AssertionError("expected weighted obstruction at prime exponent 19")
    positive = []
    for k, j, width, p, horizon, expected_q in [
        (3, 7, 4, 25759, 24, 12),
        (5, 12, 8, 7436287, 103, 49),
        (8, 14, 12, 878845951, 422, 214),
        (10, 17, 12, 48768057343, 748, 378),
    ]:
        residue, modulus = crt_candidates(k, j)
        if not is_prime(p) or p % modulus != residue or p < 21*j + 9*k + 3:
            raise AssertionError(("source conditions", p))
        row = first_meeting(p, width, horizon)
        if row is None or row[:2] != (horizon, expected_q):
            raise AssertionError(("meeting", p, row))
        # 3^p/2^horizon > 2^p: use 3^2>2^3, without giant exponents.
        if not 2*horizon < p:
            raise AssertionError(("upper original height", p))
        positive.append(dict(prime_exponent=p, ternary_precision=k, protected_postcrest=j,
                             lower_sources=width, first_simultaneous_clock=horizon,
                             full_odd_count=p-width+expected_q))
    print(json.dumps(dict(first_nineteen_first_hit_grades=grades,
                          positive_return_certificates=positive), indent=2))
