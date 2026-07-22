#!/usr/bin/env python3
"""Exact standard-library checks for L-0033, T-0037, and L-0034."""

from __future__ import annotations

from fractions import Fraction
from itertools import product

P = (5, 30, 20, 56)
B = (9, 54, 36, 24)
P_TO_TYPE = {value: index for index, value in enumerate(P)}

EXPECTED = {
    12: ("0311", "1330", "2013", "2111", "2303"),
    13: ("0203", "2202", "2300"),
    14: ("2111", "2231", "3010", "3222"),
}


def room_filter(scale: int) -> tuple[tuple[str, ...], int, int]:
    """Return surviving four-symbol heads and address-size diagnostics."""

    if scale < 12:
        raise ValueError("stabilized audit requires scale >= 12")

    d = 1 << (scale - 8)
    heights = [(256 + j) * d for j in range(4)]
    precision = 11 * sum(height + 1 for height in heights[1:4])

    modulus = 1 << precision
    lifted_modulus = modulus << 6

    odd_factors = [
        pow(3, 7 * (height + 1), lifted_modulus)
        for height in heights[:3]
    ]
    odd_product = (
        odd_factors[0] * odd_factors[1] * odd_factors[2]
    ) % lifted_modulus
    odd_inverse = pow(odd_product, -1, lifted_modulus)

    binary_1 = 1 << (11 * (heights[1] + 1))
    binary_2 = 1 << (11 * (heights[2] + 1))

    survivors: list[str] = []
    minimum_address = modulus

    for a, b, c in product(range(4), repeat=3):
        toll = (
            odd_factors[1] * odd_factors[2] * B[a]
            + binary_1 * odd_factors[2] * B[b]
            + binary_1 * binary_2 * B[c]
        ) % lifted_modulus

        lifted_address = (-toll * odd_inverse) % lifted_modulus
        address = lifted_address % modulus
        minimum_address = min(minimum_address, address)

        high_six = lifted_address >> precision
        output_residue = (-(odd_product & 63) * (high_six & 63)) % 64
        next_type = P_TO_TYPE.get(output_residue)
        if next_type is not None:
            survivors.append(f"{a}{b}{c}{next_type}")

        # Directly reconstruct the canonical output modulo 64.
        output = (odd_product * address + toll) >> precision
        assert output % 64 == output_residue

    assert len(set(survivors)) == len(survivors)
    return tuple(survivors), precision, minimum_address.bit_length()


def verify_defect_expansion() -> None:
    """Check the finite version of the exact defect-digit recurrence."""

    types = (0, 1, 3, 2, 0, 3, 1)
    heights = (160, 176, 192, 208, 224, 240, 256)

    # Impose zero terminal defect and solve the recurrence backward exactly.
    defect = Fraction(0)
    defects = [Fraction(0)] * len(types)
    for index in range(len(types) - 1, -1, -1):
        odd = 3 ** (7 * (heights[index] + 1))
        if index + 1 < len(types):
            binary = 2 ** (11 * (heights[index + 1] + 1))
        else:
            binary = 0
        defect = Fraction(B[types[index]], odd) + Fraction(binary, odd) * defect
        defects[index] = defect

    for index in range(len(types) - 1):
        odd = 3 ** (7 * (heights[index] + 1))
        binary = 2 ** (11 * (heights[index + 1] + 1))
        assert odd * defects[index] == B[types[index]] + binary * defects[index + 1]

    normalized = 3 ** (7 * (heights[0] + 1)) * defects[0]
    assert B[types[0]] < normalized < B[types[0]] + Fraction(1, 16)

    ratio = Fraction(2048, 2187)
    assert ratio**128 < Fraction(1, 1024)


def verify_completion_gap(scale: int) -> None:
    """Check the exact rational coefficient in L-0033/(15)."""

    lhs_num = 4257
    lhs_den = 128
    room_num = 1083
    room_den = 41
    gap = Fraction(lhs_num, lhs_den) - Fraction(room_num, room_den)
    assert gap == Fraction(35913, 5248)
    assert gap * (1 << scale) > 0


def main() -> None:
    for scale in sorted(EXPECTED):
        survivors, precision, min_bits = room_filter(scale)
        assert survivors == EXPECTED[scale]
        verify_completion_gap(scale)
        print(
            f"m={scale} precision={precision} "
            f"survivors={len(survivors)} heads={','.join(survivors)} "
            f"minimum_address_bits={min_bits}"
        )

    verify_defect_expansion()
    print("verified exact defect-digit recurrence and leading interval")
    print("all three-symbol room-filter checks passed")


if __name__ == "__main__":
    main()
