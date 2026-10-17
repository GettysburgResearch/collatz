#!/usr/bin/env python3
"""Exact checks for L-0031 and the native interfaces of T-0032."""

from __future__ import annotations

from dataclasses import dataclass


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

P_CONST = (5, 30, 20, 56)
B_CONST = (9, 54, 36, 24)
ALPHA = (0, 1, 2, 3)
BETA = (2, 3, 2, 1)


@dataclass(frozen=True)
class Tower:
    typ: int
    t: int
    mu: int
    A: int
    K: int
    B: int
    G: int


def tower(typ_index: int, t: int) -> Tower:
    typ = TYPES[typ_index]
    k = typ.k0 + 11 * t
    g = typ.g0 + 7 * t
    core_modulus = 1 << (typ.r + 1)
    mu = (-pow(pow(3, g, core_modulus), -1, core_modulus)) % core_modulus
    c = (3**g * mu + 1) // core_modulus
    return Tower(
        typ=typ_index,
        t=t,
        mu=mu,
        A=(1 << k) * mu,
        K=k + typ.r + 1,
        B=3**typ.b * c,
        G=g + typ.b,
    )


def connector(left: Tower, right: Tower) -> tuple[int, int]:
    modulus = 1 << right.K
    eta = (
        (right.A - left.B)
        * pow(pow(3, left.G, modulus), -1, modulus)
    ) % modulus
    theta = (left.B + 3**left.G * eta - right.A) // modulus
    assert 0 <= eta < modulus
    assert 0 <= theta < 3**left.G
    return eta, theta


def compose_tiles(tiles: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    multiplier = 1
    depth = 0
    offset = 0
    for odd, local_depth, local_offset in tiles:
        offset = odd * offset + (1 << depth) * local_offset
        multiplier *= odd
        depth += local_depth
    return multiplier, depth, offset


def verify_stabilized_anchors() -> None:
    for typ_index in range(4):
        for t in (0, 16, 32):
            item = tower(typ_index, t)
            binary_radix = 1 << item.K
            odd_multiplier = 3**item.G
            assert 64 * item.A == binary_radix * P_CONST[typ_index]
            assert (
                64 * item.B
                == odd_multiplier * P_CONST[typ_index] + B_CONST[typ_index]
            )
            assert (
                B_CONST[typ_index]
                == (1 << ALPHA[typ_index]) * 3 ** BETA[typ_index]
            )


def verify_actual_scaled_chains() -> int:
    patterns = (
        (0, 1, 2, 3, 0, 1, 2, 3, 0, 1),
        (3, 3, 2, 2, 1, 1, 0, 0, 3, 2),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (1, 3, 0, 2, 1, 3, 0, 2, 1, 3),
    )
    heights = tuple(160 + 16 * j for j in range(10))
    checked_transitions = 0

    for type_word in patterns:
        towers = [tower(i, t) for i, t in zip(type_word, heights)]
        connectors = [
            connector(towers[j], towers[j + 1])
            for j in range(len(towers) - 1)
        ]
        chain_length = len(towers) - 2

        tiles: list[tuple[int, int, int]] = []
        for j in range(chain_length):
            _, theta = connectors[j]
            eta_next, _ = connectors[j + 1]
            tiles.append(
                (
                    3 ** towers[j].G,
                    towers[j + 2].K,
                    theta - eta_next,
                )
            )

        multiplier, depth, offset = compose_tiles(tiles)
        modulus = 1 << depth
        correction = (-offset * pow(multiplier, -1, modulus)) % modulus
        cap = (multiplier * correction + offset) // modulus
        assert cap >= 0

        for high_tail in (0, 1, 3):
            residual = correction + modulus * high_tail
            residuals = [residual]
            for odd, local_depth, local_offset in tiles:
                numerator = odd * residual + local_offset
                assert numerator % (1 << local_depth) == 0
                residual = numerator >> local_depth
                assert residual >= 0
                residuals.append(residual)
            assert residual == cap + multiplier * high_tail

            scaled: list[int] = []
            for j in range(chain_length + 1):
                eta, _ = connectors[j]
                x = P_CONST[type_word[j]] + 64 * eta
                next_binary_radix = 1 << towers[j + 1].K
                scaled.append(x + 64 * next_binary_radix * residuals[j])

            for j in range(chain_length):
                odd = 3 ** towers[j].G
                binary = 1 << towers[j + 1].K
                assert (
                    binary * scaled[j + 1]
                    == odd * scaled[j] + B_CONST[type_word[j]]
                )
                checked_transitions += 1

            odd_product = 1
            binary_product = 1
            toll = 0
            for j in range(chain_length):
                odd_product *= 3 ** towers[j].G
                binary_product *= 1 << towers[j + 1].K

                prior_binary_depth = sum(
                    towers[r + 1].K for r in range(j)
                )
                later_odd_depth = sum(
                    towers[r].G for r in range(j + 1, chain_length)
                )
                toll += (
                    (1 << (prior_binary_depth + ALPHA[type_word[j]]))
                    * 3 ** (later_odd_depth + BETA[type_word[j]])
                )

            assert (
                binary_product * scaled[chain_length]
                == odd_product * scaled[0] + toll
            )

    return checked_transitions


def verify_stage_exponents_and_scale_injection() -> None:
    seen_ratios: set[tuple[int, int]] = set()
    fixed_first_two_types = (0, 1)

    for m in range(12, 25):
        scale = 1 << m
        delta = scale >> 8
        heights = [scale + j * delta for j in range(257)]

        odd_exponent = 7 * (sum(heights[:256]) + 256)
        binary_exponent = 11 * (sum(heights[1:257]) + 256)

        assert odd_exponent == (5369 * scale) // 2 + 1792
        assert binary_exponent == (8459 * scale) // 2 + 2816

        t1 = heights[1]
        ratio_exponents = (
            ALPHA[fixed_first_two_types[0]]
            - ALPHA[fixed_first_two_types[1]]
            - 11 * (t1 + 1),
            BETA[fixed_first_two_types[0]]
            - BETA[fixed_first_two_types[1]]
            + 7 * (t1 + 1),
        )
        assert ratio_exponents not in seen_ratios
        seen_ratios.add(ratio_exponents)


def main() -> None:
    verify_stabilized_anchors()
    print("verified stabilized two-prime tower anchors")

    checked = verify_actual_scaled_chains()
    print(f"verified {checked} actual scaled-tail connector transitions")

    verify_stage_exponents_and_scale_injection()
    print("verified 256-stage exponents and scale-injective toll ratios")

    print("all scaled-tail S-unit checks passed")


if __name__ == "__main__":
    main()
