"""Exact dyadic reciprocal budget for injective U-invariant sets above 2^68."""

from fractions import Fraction
from math import comb
import json


def phase_control(min_length):
    length = min_length
    while True:
        ternary = 3 ** length
        clock = ternary.bit_length()
        if 2 ** (2 * clock) < 2 * ternary ** 2:
            break
        length += 1
    ones = 2 * length - clock
    twos = clock - length
    # Anchor the primitive two-run word at the end of its increasing ones.
    word = [2] * twos + [1] * ones
    carry = 0
    dyadic = 1
    for letter in word:
        carry = 3 * carry + dyadic
        dyadic <<= letter
    denominator = dyadic - ternary
    quotient, remainder = divmod(carry, denominator)
    if not (ones and twos and remainder and quotient > 2 ** 71):
        raise ValueError("expected a nonintegral rational phase above the floor")
    return {"length": length, "clock": clock, "ones": ones, "twos": twos,
            "canonical_max_floor_bits": quotient.bit_length(),
            "has_integral_cycle": False}


def main():
    partial = Fraction(0)
    m = 0
    for n in range(69, 512):
        while 3 ** (m + 1) <= 2 ** (n - 2):
            m += 1
        if not 3 ** m <= 2 ** (n - 2) < 3 ** (m + 1):
            raise ValueError("incorrect dyadic shell clock")
        numer = sum(comb(n - 1, j) for j in range(m, n))
        partial += Fraction(numer, 3 * 2 ** (n - 1))
    r = Fraction(5, 4) ** 8 / Fraction(3, 2) ** 5
    tail = 8 * r ** 64 / (3 * (1 - r))
    if not (2 ** 27 > 3 ** 17 and r < 1
            and partial < Fraction(335142, 10**6)
            and tail < Fraction(3, 10**6)
            and partial + tail < Fraction(17, 50)):
        raise ValueError("certificate failed")
    print(json.dumps({"first_shell": 69, "last_exact_shell": 511,
                      "geometric_ratio": str(r),
                      "partial_upper_ppm": -(-partial * 10**6 // 1),
                      "tail_upper_ppm": -(-tail * 10**6 // 1),
                      "total_strict_upper": "17/50",
                      "phase_examples": [phase_control(n) for n in (512, 1024, 4096)]}, indent=2))


if __name__ == "__main__":
    main()
