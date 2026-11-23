#!/usr/bin/env python3
"""Exact receipt for the sign-sensitive full-denominator control.

This checks one displayed control and its full affine/product identities.
It does not prove the universal convex-integral bound or exclude cycles.
"""

from fractions import Fraction
from math import gcd
import json


def carry(bits: list[int]) -> int:
    result = 0
    for clock, bit in enumerate(bits):
        result = 3**bit * result + bit * 2**clock
    return result


def step(value: Fraction) -> Fraction:
    assert value.denominator % 2
    return (3 * value + 1) / 2 if value.numerator % 2 else value / 2


def main() -> None:
    original = list(map(Fraction, [-17, -25, -37, -55, -82, -41, -61, -91, -136, -68, -34]))
    assert len(set(original)) == len(original)
    assert all(step(x) == original[(i + 1) % len(original)] for i, x in enumerate(original))
    bits = [x.numerator % 2 for x in original]
    complement = [1 - bit for bit in bits]
    length, odd = len(bits), sum(bits)
    co, cc = carry(bits), carry(complement)
    do = 2**length - 3**odd
    ec = 2**length - 3 ** (length - odd)
    assert (co, do, cc, ec) == (2363, -139, 5296, 1967)
    assert Fraction(co, do) == original[0]
    denominator = ec // gcd(ec, cc)
    companion: list[Fraction] = []
    value = Fraction(cc, ec)
    ratio = Fraction(1)
    for bit in complement:
        assert value > 0 and value.denominator == denominator
        assert value.numerator % 2 == bit
        companion.append(value)
        if bit:
            w = value.numerator
            ratio *= Fraction(3 * w + denominator, 4 * w)
        value = step(value)
    assert value == companion[0]
    assert len(set(companion)) == length
    assert ratio == Fraction(2) ** (2 * odd - length)
    assert denominator == 1967 and denominator > 3 * (2 * odd - length)
    print(json.dumps({
        "status": "PASS",
        "scope": "Exact negative-cycle control; not a Collatz proof or universal-bound formalization",
        "length": length,
        "original_odd_count": odd,
        "original_complete_carry": co,
        "original_complete_denominator": do,
        "companion_complete_carry": cc,
        "companion_complete_denominator": ec,
        "companion_reduced_denominator": denominator,
        "companion_product": str(ratio),
        "companion_cycle": [str(x) for x in companion],
    }, indent=2))


if __name__ == "__main__":
    main()
