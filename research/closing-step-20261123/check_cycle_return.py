#!/usr/bin/env python3
"""Exact small controls for complete cycle returns and coupled products.

The controls are not a search for unknown cycles or a proof of the qualified
global packing theorem. All assertions remain active under python -O.
"""

from fractions import Fraction
from math import gcd
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def step(value: Fraction) -> Fraction:
    require(value.denominator % 2 == 1, "non-odd denominator")
    return (3 * value + 1) / 2 if value.numerator % 2 else value / 2


def replay(source: Fraction, count: int) -> tuple[Fraction, list[int]]:
    bits = []
    value = source
    for _ in range(count):
        bits.append(value.numerator % 2)
        value = step(value)
    return value, bits


def carry(bits: list[int]) -> int:
    result = 0
    for index, bit in enumerate(bits):
        result = 3**bit * result + bit * 2**index
    return result


def main() -> None:
    legal_cases = inverse_grid_cases = nonintegral_rejections = 0
    for q, word in ((1, [1, 0]), (2, [0, 1])):
        length, odd = len(word), sum(word)
        for laps in range(1, 7):
            for offset in (0, 1, 2, 7):
                source = q + 2 ** (laps * length) * offset
                expected = q + 3 ** (laps * odd) * offset
                endpoint, bits = replay(Fraction(source), laps * length)
                require(bits == word * laps, "literal parity mismatch")
                require(endpoint == expected, "ordinary endpoint mismatch")
                legal_cases += 1
            for endpoint in range(q + 1, q + 13):
                inverse = q + Fraction(2 ** (laps * length), 3 ** (laps * odd)) * (endpoint - q)
                integral = (endpoint - q) % 3 ** (laps * odd) == 0
                require((inverse.denominator == 1) == integral, "inverse lattice mismatch")
                if integral:
                    actual, bits = replay(inverse, laps * length)
                    require(actual == endpoint and bits == word * laps, "inverse legality mismatch")
                inverse_grid_cases += 1
            if laps >= 2:
                damaged = q + Fraction(2 ** (laps * length), 3 ** (laps * odd)) * 3
                require(damaged.denominator != 1, "false extra ordinary lap")
                nonintegral_rejections += 1

    word = [1, 1, 0, 1, 1, 0, 1, 0]
    complement = [1 - bit for bit in word]
    length, odd = len(word), sum(word)
    original_denominator = 2**length - 3**odd
    companion_denominator = 2**length - 3 ** (length - odd)
    original = Fraction(carry(word), original_denominator)
    companion = Fraction(carry(complement), companion_denominator)
    denominator = companion.denominator
    require(original == Fraction(319, 13), "wrong rational control")
    require(gcd(carry(word), original_denominator) == 1, "control cancellation changed")
    shifted = ordinary = Fraction(1)
    states = []
    x, y = original, companion
    for bit in word:
        require(x > 21 and y > 0, "positive floor changed")
        require(x.numerator % 2 == bit and y.numerator % 2 == 1 - bit,
                "complementary parity mismatch")
        require(y.denominator == denominator, "companion denominator changed")
        w = y.numerator
        xn, yn = step(x), step(y)
        expected_product = (3*x*w+w)/4 if bit else (3*x*w+denominator*x)/4
        require(xn * yn.numerator == expected_product, "paired product mismatch")
        if bit:
            ordinary *= 1 + 1/(3*x)
        else:
            shifted *= (x+2)/(x+1)
        states.append(str(x))
        x, y = xn, yn
    require(x == original and y == companion, "rational cycles do not close")
    require(len(set(states)) == length, "control is not primitive")
    require(ordinary == shifted == Fraction(2**length, 3**odd), "shifted product mismatch")
    print(json.dumps({
        "status": "PASS",
        "scope": "Exact finite controls only; no unknown-cycle census or proof of input (P)",
        "legal_return_cases": legal_cases,
        "inverse_lattice_cases": inverse_grid_cases,
        "false_extra_lap_rejections": nonintegral_rejections,
        "fixed_endpoint_example": {"cycle_phase": 1, "endpoint": 4,
                                   "one_lap_inverse": "5", "two_lap_inverse": "19/3"},
        "positive_rational_control": {
            "original": str(original),
            "original_states": states,
            "full_original_denominator": original_denominator,
            "original_carry": carry(word),
            "original_gcd": 1,
            "companion": str(companion),
            "full_companion_denominator": companion_denominator,
            "reduced_companion_denominator": denominator,
            "ordinary_and_shifted_product": str(ordinary),
        },
    }, indent=2))


if __name__ == "__main__":
    main()
