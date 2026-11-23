#!/usr/bin/env python3
"""Exact finite controls for the resultant detector, using only the standard library.

Literal rational cycles and positive rational preperiods are replayed.  They
are not presented as ordinary integer cycles.  The all-period proof is in
FINITE_JET_BOUND.md; these selected cases check its finite certificates.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from math import comb, gcd
import json


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def valuation(n: int, prime: int) -> int:
    require(n != 0, "valuation of zero is not used")
    n = abs(n)
    result = 0
    while n % prime == 0:
        n //= prime
        result += 1
    return result


def prime_divisors(n: int) -> list[int]:
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            result.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result.append(n)
    return result


def carry(word: tuple[int, ...]) -> list[int]:
    remaining = sum(word)
    coefficients = []
    for bit in word:
        remaining -= bit
        coefficients.append(bit * 3**remaining)
    return coefficients


def evaluate(poly: list[int], value: int) -> int:
    answer = 0
    for c in reversed(poly):
        answer = answer * value + c
    return answer


def remainder(poly: list[int], degree: int, constant: int) -> list[int]:
    result = [0] * degree
    for i, c in enumerate(poly):
        power, index = divmod(i, degree)
        result[index] += c * constant**power
    return result


def determinant(matrix: list[list[int]]) -> int:
    """Fraction-free elimination, with exact division and pivot checks."""
    a = [row[:] for row in matrix]
    size = len(a)
    previous = 1
    sign = 1
    for k in range(size - 1):
        if a[k][k] == 0:
            pivot_row = next((i for i in range(k + 1, size) if a[i][k]), None)
            if pivot_row is None:
                return 0
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                quotient, residual = divmod(numerator, previous)
                require(residual == 0, "nonexact Bareiss division")
                a[i][j] = quotient
        for i in range(k + 1, size):
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def permutation_determinant(matrix: list[list[int]]) -> int:
    answer = 0
    size = len(matrix)
    for permutation in permutations(range(size)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(size) for j in range(i + 1, size))
        product = -1 if inversions % 2 else 1
        for i, j in enumerate(permutation):
            product *= matrix[i][j]
        answer += product
    return answer


def resultant(poly: list[int], degree: int, constant: int) -> tuple[int, bool]:
    # Multiplication by C in Z[z]/(z^degree-constant) has determinant Res(F,C).
    reduced = remainder(poly, degree, constant)
    columns = [remainder([0] * j + reduced, degree, constant)
               for j in range(degree)]
    matrix = [[columns[j][i] for j in range(degree)] for i in range(degree)]
    answer = determinant(matrix)
    independent = degree <= 6
    if independent:
        require(answer == permutation_determinant(matrix), "determinant mismatch")
    return answer, independent


def taylor(numerator: list[int], denominator: list[int], count: int) -> list[Fraction]:
    def translated(poly: list[int], j: int) -> int:
        return sum(poly[k] * comb(k, j) * 2 ** (k - j)
                   for k in range(j, len(poly)))
    q = [translated(denominator, j) for j in range(min(count, len(denominator)))]
    require(q[0] != 0, "Taylor center is a pole")
    result = []
    for j in range(count):
        residual = Fraction(translated(numerator, j))
        residual -= sum((q[k] * result[j - k] for k in range(1, min(j + 1, len(q)))),
                        Fraction(0))
        result.append(residual / q[0])
    return result


def actual_step(value: Fraction) -> tuple[int, Fraction]:
    require(value > 0 and value.denominator % 2, "not a positive binary-integral rational")
    bit = value.numerator % 2
    return bit, (3**bit * value + bit) / 2


def multiply(a: list[int], b: list[int]) -> list[int]:
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def run_checks() -> dict[str, object]:
    words = [tuple(map(int, text)) for text in
             ("01", "10", "0101", "100", "110000", "101000", "11100000",
              "10000", "10101000", "100100010000", "110100000", "11110000000")]
    words += [tuple(map(int, "100" * (m - 1) + "010")) for m in (4, 14, 39)]
    totals = {"cycle_words": 0, "literal_rational_steps": 0, "prime_certificates": 0,
              "independent_determinants": 0, "positive_preperiods": 0,
              "prefix_coefficient_comparisons": 0, "prefix_prime_order_checks": 0}
    certificates = []
    for word in words:
        length, odd = len(word), sum(word)
        require(2**length > 3**odd, "cycle denominator is not positive")
        c = carry(word)
        q = [3**odd] + [0] * (length - 1) + [-1]
        source = Fraction(evaluate(c, 2), 2**length - 3**odd)
        state = source
        for expected in word:
            bit, state = actual_step(state)
            require(bit == expected, "literal rational parity mismatch")
            totals["literal_rational_steps"] += 1
        require(state == source, "rational itinerary did not close")
        divisor = gcd(length, odd)
        u, v = length // divisor, odd // divisor
        reduced_clock = 2**u - 3**v
        norm, independent = resultant(c, u, 3**v)
        require(norm != 0, "unexpected cancellation of the reduced clock")
        totals["independent_determinants"] += int(independent)
        coarse = u * u * (2 * odd - 1)
        primes = prime_divisors(reduced_clock)
        bounds = {p: u * valuation(norm, p) // valuation(reduced_clock, p) for p in primes}
        count = max(bounds.values(), default=4) + 4
        coefficients = taylor(c, q, count)
        require(coefficients[0] == -source, "wrong actual Taylor constant")
        first = {}
        for p, bound in bounds.items():
            bad = next((j for j, a in enumerate(coefficients) if a.denominator % p == 0), None)
            require(bad is not None and bad <= bound and bad < coarse,
                    "finite prime certificate failed")
            first[p] = bad
            certificates.append({"length": length, "odd_count": odd, "prime": p,
                                 "first_forbidden_order": bad, "resultant_bound": bound,
                                 "period_only_count": coarse})
            totals["prime_certificates"] += 1

        # Build an actual positive mixed preperiod backwards from this cycle.
        backward = [0] * 8 + [1, 0, 1, 0, 0, 1]
        head = source
        transported = coefficients[:]
        for bit in backward:
            head = (2 * head - bit) / 3**bit
            require(head > 0, "chosen inverse step is not positive")
            transported = [(bit + 2 * transported[0]) / 3**bit] + [
                (2 * transported[j] + transported[j - 1]) / 3**bit
                for j in range(1, count)]
        prefix = tuple(reversed(backward))
        state = head
        for expected in prefix:
            bit, state = actual_step(state)
            require(bit == expected, "preperiod is not the literal itinerary")
        require(state == source, "preperiod has the wrong endpoint")
        full_numerator = multiply(carry(prefix), q)
        if len(full_numerator) < len(prefix) + len(c):
            full_numerator += [0] * (len(prefix) + len(c) - len(full_numerator))
        for k, coefficient in enumerate(c):
            full_numerator[len(prefix) + k] += coefficient
        direct = taylor(full_numerator, [3**sum(prefix) * a for a in q], count)
        require(direct == transported and direct[0] == -head, "prefix Taylor mismatch")
        totals["prefix_coefficient_comparisons"] += count
        prefixed_norm, _ = resultant(full_numerator, u, 3**v)
        for p, bad in first.items():
            require(valuation(prefixed_norm, p) == valuation(norm, p), "prefix changed norm valuation")
            observed = next((j for j, a in enumerate(direct) if a.denominator % p == 0), None)
            require(observed == bad, "actual preperiod hid the first forbidden order")
            totals["prefix_prime_order_checks"] += 1
        totals["cycle_words"] += 1
        totals["positive_preperiods"] += 1
    require(any(c["first_forbidden_order"] >= 3 for c in certificates), "delay control missing")
    return {"status": "pass", "scope": "selected exact rational cycles and positive rational preperiods",
            "totals": totals, "certificates": certificates,
            "unproved": "construction of the actual rational germ and eventual periodicity for every ordinary source"}


if __name__ == "__main__":
    print(json.dumps(run_checks(), sort_keys=True, indent=2))
