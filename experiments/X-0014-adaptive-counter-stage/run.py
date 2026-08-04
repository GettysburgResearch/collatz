#!/usr/bin/env python3
"""Exact checks for L-0028 and T-0027--T-0029."""

from __future__ import annotations

from dataclasses import dataclass


def v2(n: int) -> int:
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def compose_tiles(tiles: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    """Compose (odd multiplier, binary depth, offset) chronologically."""
    multiplier = 1
    depth = 0
    offset = 0
    for odd, local_depth, local_offset in tiles:
        offset = odd * offset + (1 << depth) * local_offset
        multiplier *= odd
        depth += local_depth
    return multiplier, depth, offset


def replay_tiles(
    tiles: list[tuple[int, int, int]],
    value: int,
) -> tuple[bool, int | None]:
    current = value
    for odd, depth, offset in tiles:
        numerator = odd * current + offset
        if numerator % (1 << depth):
            return False, None
        current = numerator >> depth
    return True, current


def verify_generic_composition() -> None:
    systems = [
        [(3, 1, -1), (5, 2, 3), (7, 1, -4)],
        [(1, 0, 2), (9, 3, -5)],
        [(11, 2, 7), (3, 3, -2), (5, 0, 1), (13, 2, -9)],
    ]

    for tiles in systems:
        multiplier, depth, offset = compose_tiles(tiles)
        for value in range(-100, 101):
            local_ok, local_output = replay_tiles(tiles, value)
            composite_ok = (
                multiplier * value + offset
            ) % (1 << depth) == 0
            assert local_ok == composite_ok
            if local_ok:
                assert local_output == (
                    multiplier * value + offset
                ) // (1 << depth)


@dataclass(frozen=True)
class TowerType:
    k0: int
    r: int
    b: int
    g0: int


TYPES = (
    TowerType(5, 5, 2, 5),
    TowerType(6, 4, 3, 4),
    TowerType(7, 3, 2, 5),
    TowerType(8, 2, 1, 6),
)


@dataclass(frozen=True)
class Tower:
    typ: TowerType
    t: int
    mu: int
    A: int
    K: int
    B: int
    G: int


def tower(typ: TowerType, t: int) -> Tower:
    k = typ.k0 + 11 * t
    g = typ.g0 + 7 * t
    core_modulus = 1 << (typ.r + 1)
    mu = (-pow(pow(3, g, core_modulus), -1, core_modulus)) % core_modulus
    c = (3**g * mu + 1) // core_modulus
    A = (1 << k) * mu
    K = k + typ.r + 1
    B = 3**typ.b * c
    G = g + typ.b
    assert K == 11 * (t + 1)
    assert G == 7 * (t + 1)
    return Tower(typ, t, mu, A, K, B, G)


def connector(left: Tower, right: Tower) -> tuple[int, int]:
    modulus = 1 << right.K
    eta = (
        (right.A - left.B)
        * pow(pow(3, left.G, modulus), -1, modulus)
    ) % modulus
    theta = (left.B + 3**left.G * eta - right.A) // modulus
    assert theta >= 0
    return eta, theta


def residual_tile(
    t0: int,
    t1: int,
    t2: int,
    i0: int,
    i1: int,
    i2: int,
) -> tuple[int, int, int]:
    first = tower(TYPES[i0], t0)
    second = tower(TYPES[i1], t1)
    third = tower(TYPES[i2], t2)
    _, theta = connector(first, second)
    eta_next, _ = connector(second, third)
    return 3**first.G, third.K, theta - eta_next


def verify_actual_tower_slice() -> None:
    scale = 1 << 8
    types = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1]
    tiles = [
        residual_tile(
            scale + j,
            scale + j + 1,
            scale + j + 2,
            types[j],
            types[j + 1],
            types[j + 2],
        )
        for j in range(8)
    ]

    multiplier, depth, offset = compose_tiles(tiles)
    correction = (-offset * pow(multiplier, -1, 1 << depth)) % (1 << depth)
    cap = (offset + multiplier * correction) >> depth
    assert cap >= 0

    for high_tail in (0, 1, 3):
        value = correction + (1 << depth) * high_tail
        valid, output = replay_tiles(tiles, value)
        assert valid
        assert output == cap + multiplier * high_tail


def omega_mod(typ: TowerType, t: int, bits: int) -> int:
    g = typ.g0 + 7 * t
    precision = bits + typ.r + 1
    modulus = 1 << precision
    inverse = pow(pow(3, g, modulus), -1, modulus)

    core_modulus = 1 << (typ.r + 1)
    mu = (-pow(pow(3, g, core_modulus), -1, core_modulus)) % core_modulus
    assert (mu + inverse) % core_modulus == 0
    return ((mu + inverse) >> (typ.r + 1)) % (1 << bits)


def verify_counter_isometries() -> None:
    for typ in TYPES:
        period = 1 << (typ.r - 1)
        for bits in range(1, 8):
            values = [
                omega_mod(typ, period * address, bits)
                for address in range(1 << bits)
            ]
            assert len(set(values)) == 1 << bits

            for address, value in enumerate(values):
                low_lift = omega_mod(typ, period * address, bits + 1)
                high_lift = omega_mod(
                    typ,
                    period * (address + (1 << bits)),
                    bits + 1,
                )
                assert low_lift % (1 << bits) == value
                assert high_lift % (1 << bits) == value
                assert ((low_lift >> bits) & 1) != ((high_lift >> bits) & 1)

        for left in range(1, 20):
            for right in range(left + 1, 25):
                bits = 12
                difference = (
                    omega_mod(typ, period * right, bits)
                    - omega_mod(typ, period * left, bits)
                ) % (1 << bits)
                assert v2(difference) == v2(right - left)


def verify_adaptive_512_chart() -> None:
    for typ in TYPES:
        address_bits = 4
        m = address_bits + typ.r + 8
        scale = 1 << m
        width = 1 << (m - 9)
        period = 1 << (typ.r - 1)
        core_residue = 0
        assert width == period * (1 << address_bits)

        heights = []
        for cell in range(512):
            base = scale + cell * width + core_residue
            inverse_table = {
                omega_mod(
                    typ,
                    base + period * address,
                    address_bits,
                ): address
                for address in range(1 << address_bits)
            }
            assert len(inverse_table) == 1 << address_bits

            desired = (37 * cell + 5) % (1 << address_bits)
            address = inverse_table[desired]
            height = base + period * address
            assert scale + cell * width <= height < scale + (cell + 1) * width
            assert omega_mod(typ, height, address_bits) == desired
            heights.append(height)

        for cell in range(511):
            jump = heights[cell + 1] - heights[cell]
            assert period <= jump <= 2 * width - period

        for cell in range(510):
            assert heights[cell + 2] - heights[cell] < 4 * width
            # 84/53 is a rigorous lower bound for log_2(3).
            assert (
                7 * 84 * (heights[cell] + 1)
                > 11 * 53 * (heights[cell + 2] + 1)
            )

    assert 5 * 128 > 11 * 53


def verify_stage_scale_squaring() -> None:
    for m in range(8, 16):
        scale = 1 << m
        odd_exponent = (5369 * scale) // 2 + 1792
        binary_depth = (1085579 * scale) // 256 + 2816

        next_scale = 2 * scale
        next_odd = (5369 * next_scale) // 2 + 1792
        next_depth = (1085579 * next_scale) // 256 + 2816

        assert next_odd == 2 * odd_exponent - 1792
        assert next_depth == 2 * binary_depth - 2816
        assert next_odd - 1792 == 2 * (odd_exponent - 1792)
        assert next_depth - 2816 == 2 * (binary_depth - 2816)


def main() -> None:
    verify_generic_composition()
    verify_actual_tower_slice()
    print("verified offset Montgomery composition and exact path domains")

    verify_counter_isometries()
    print("verified padding-counter isometries and one-bit lifts")

    verify_adaptive_512_chart()
    print("verified adaptive 512-cell prefix routing and robust growth")

    verify_stage_scale_squaring()
    print("verified exact stage compression and normalized scale squaring")

    print("all adaptive-counter stage checks passed")


if __name__ == "__main__":
    main()
