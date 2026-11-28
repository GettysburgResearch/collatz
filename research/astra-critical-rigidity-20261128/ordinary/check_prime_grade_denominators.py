"""Exact controls for the sharp primitive word families and their complete denominators."""
from collections import Counter
from fractions import Fraction
from math import gcd
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def carry(dates):
    value = 0
    for date in dates:
        value = 3*value+(1 << date)
    return value


def replay(length, dates, counts):
    raw = 2**length-3**len(dates)
    require(raw > 0, "positive determinant required")
    z = Fraction(carry(dates), raw)
    initial = z
    positions = set(dates)
    for t in range(length):
        bit = z.numerator % 2
        require(bit == (t in positions), "incorrect native calendar")
        require(z.denominator == initial.denominator and z.numerator % 3,
                "nonconstant denominator or ternary nonunit")
        z = (3*z+1)/2 if bit else z/2
        require((z == initial) == (t == length-1), "wrong primitive period")
    counts["true_rational_native_steps"] += length
    counts["primitive_words"] += 1
    return initial.denominator


def sharp_cycle(prime, grade, n, counts):
    require(grade % prime == 0 and n >= 3, "invalid sharp calendar")
    b = grade//prime
    x = 2**n
    dates = [i*n+int(i < b) for i in range(grade)]
    q = replay(grade*n, dates, counts)
    # Both geometric sums are homogeneous integer polynomials at (2^n,3).
    common = (x**b-3**b)//(x-3)
    raw = x**grade-3**grade
    numerator = carry(dates)
    reduced_raw, rem_d = divmod(raw, common)
    reduced_carry, rem_a = divmod(numerator, common)
    require(rem_d == rem_a == 0, "missing predicted cyclotomic factor")
    require(q == reduced_raw//gcd(reduced_raw, reduced_carry), "wrong complete denominator")
    expected_factor = gcd(x-3, prime+1)
    remainder_factor = gcd(reduced_raw, reduced_carry)
    require(remainder_factor == expected_factor, "wrong exact residual common factor")
    require(q == (x-3)*(x**grade-3**grade)//((x**b-3**b)*expected_factor),
            "wrong closed denominator")
    counts["largest_observed_extra_common_factor"] = max(
        counts["largest_observed_extra_common_factor"], remainder_factor)
    return q.bit_length()


def main():
    counts = Counter()
    cases = []
    for prime, grade in ((2, 2), (3, 3), (2, 4), (5, 5), (7, 7), (19, 19), (5, 25), (7, 49)):
        rows = []
        for n in (3, 5, 11, 23):
            rows.append([n, sharp_cycle(prime, grade, n, counts)])
        cases.append({"prime": prime, "grade": grade, "n_and_denominator_bit_length": rows})
    for n in (3, 7, 11, 23):
        q = replay(4*n+1, [0, 1, 2, 3], counts)
        raw = 2**(4*n+1)-81
        require(raw//q == gcd(raw, 65), "full-exponent grade-four carry")
    require(counts["largest_observed_extra_common_factor"] > 1, "missing nontrivial residual gcd")
    print(json.dumps({"counts": dict(counts), "sharp_families": cases}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
