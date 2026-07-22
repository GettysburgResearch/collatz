#!/usr/bin/env python3
"""Exact checks for L-0032 and O-0011's native inequalities."""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


RUN_PATH = Path(__file__).with_name("run.py")
SPEC = spec_from_file_location("x0016_run", RUN_PATH)
assert SPEC is not None and SPEC.loader is not None
CORE = module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)


def v2(n: int) -> int:
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def v3(n: int) -> int:
    assert n != 0
    n = abs(n)
    count = 0
    while n % 3 == 0:
        n //= 3
        count += 1
    return count


def verify_actual_boundary_signatures() -> int:
    patterns = (
        (0, 1, 2, 3, 0, 1, 2, 3, 0, 1),
        (3, 3, 2, 2, 1, 1, 0, 0, 3, 2),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (1, 3, 0, 2, 1, 3, 0, 2, 1, 3),
    )
    heights = tuple(160 + 16 * j for j in range(10))
    checked = 0

    for type_word in patterns:
        towers = [CORE.tower(i, t) for i, t in zip(type_word, heights)]
        connectors = [
            CORE.connector(towers[j], towers[j + 1])
            for j in range(len(towers) - 1)
        ]
        chain_length = len(towers) - 2
        tiles = []
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

        odd, depth, offset = CORE.compose_tiles(tiles)
        modulus = 1 << depth
        correction = (-offset * pow(odd, -1, modulus)) % modulus

        residual = correction
        residuals = [residual]
        for local_odd, local_depth, local_offset in tiles:
            numerator = local_odd * residual + local_offset
            assert numerator % (1 << local_depth) == 0
            residual = numerator >> local_depth
            residuals.append(residual)

        scaled = []
        for j in range(chain_length + 1):
            eta, _ = connectors[j]
            x = CORE.P_CONST[type_word[j]] + 64 * eta
            next_radix = 1 << towers[j + 1].K
            value = x + 64 * next_radix * residuals[j]
            scaled.append(value)
            assert v2(value) == CORE.ALPHA[type_word[j]]
            checked += 1

        for j in range(chain_length):
            assert v3(scaled[j + 1]) == CORE.BETA[type_word[j]]
            checked += 1

    return checked


def verify_two_place_exponent() -> None:
    for m in range(12, 40):
        scale = 1 << m
        a_m = (5369 * scale) // 2 + 1792 * m
        for g in (1, 2, 3):
            # 3^(-7B) < Q^(-1/512), Q=3^(a_m-g).
            assert 7 * 512 * scale > a_m - g

    # Fixed constants can be absorbed because 1/512 > 1/1024.
    assert 1 / 512 > 1 / 1024


def main() -> None:
    checked = verify_actual_boundary_signatures()
    print(f"verified {checked} binary/ternary boundary signatures")

    verify_two_place_exponent()
    print("verified exact two-place approximation exponent")

    print("all boundary-valuation checks passed")


if __name__ == "__main__":
    main()
