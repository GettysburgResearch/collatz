#!/usr/bin/env python3
"""Finite exact checks for the room normalization used in T-0033."""

from __future__ import annotations

from fractions import Fraction


def compose_maps(
    multipliers: list[int],
    radices: list[int],
    tolls: list[int],
) -> tuple[int, int, int]:
    odd_product = 1
    radix_product = 1
    offset = 0
    for odd, radix, toll in zip(multipliers, radices, tolls):
        offset = odd * offset + radix_product * toll
        odd_product *= odd
        radix_product *= radix
    return odd_product, radix_product, offset


def verify_finite_room_floor() -> None:
    # A small positive expanding affine chain.  It is not asserted to be a
    # Collatz stage; it isolates the exact normalization/floor algebra of
    # T-0033 without enormous exponents.
    multipliers = [27] * 5
    radices = [2] * 5
    tolls = [1] * 5

    odd_product, radix_product, offset = compose_maps(
        multipliers,
        radices,
        tolls,
    )
    correction = (-offset * pow(odd_product, -1, radix_product)) % radix_product

    current = correction
    values = [current]
    scales = [Fraction(1, 1)]
    rooms = [Fraction(current, 1)]

    for odd, radix, toll in zip(multipliers, radices, tolls):
        numerator = odd * current + toll
        assert numerator % radix == 0
        current = numerator // radix
        values.append(current)

        scales.append(scales[-1] * Fraction(odd, radix))
        rooms.append(Fraction(current, 1) / scales[-1])

    for j in range(len(multipliers)):
        expected_increment = Fraction(tolls[j], 1) / (
            multipliers[j] * scales[j]
        )
        assert rooms[j + 1] - rooms[j] == expected_increment
        assert rooms[j + 1] > rooms[j]

    terminal_room = rooms[-1]
    for value, scale in zip(values[:-1], scales[:-1]):
        defect = terminal_room * scale - value
        assert 0 < defect < 1
        assert value == (terminal_room * scale).numerator // (
            terminal_room * scale
        ).denominator


def verify_stage_bound_ingredients() -> None:
    assert 144 * 2048**128 < 2187**128

    for m in range(12, 25):
        scale = 1 << m
        a_m = (5369 * scale) // 2 + 1792 * m
        e_m = (8459 * scale) // 2 + 2816 * m
        a_next = (5369 * (2 * scale)) // 2 + 1792 * (m + 1)
        e_next = (8459 * (2 * scale)) // 2 + 2816 * (m + 1)

        stage_odd = (5369 * scale) // 2 + 1792
        stage_binary = (8459 * scale) // 2 + 2816
        assert a_next - a_m == stage_odd
        assert e_next - e_m == stage_binary

        # The exact lower bound log_2(3) > 84/53 makes the homogeneous
        # scale strictly expanding without floating-point arithmetic.
        assert 84 * stage_odd > 53 * stage_binary


def main() -> None:
    verify_finite_room_floor()
    print("verified exact finite-room increments and floor identities")

    verify_stage_bound_ingredients()
    print("verified shrinking-target bound ingredients")

    print("all fixed-room checks passed")


if __name__ == "__main__":
    main()
