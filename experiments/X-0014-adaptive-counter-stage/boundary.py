#!/usr/bin/env python3
"""Exact scale-boundary audit for T-0029's adaptive 512-cell chart."""

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


def verify_boundary() -> int:
    checked = 0
    for typ in TYPES:
        address_bits = 4
        m = address_bits + typ.r + 8
        b = 1 << m
        d = b >> 9
        period = 1 << (typ.r - 1)
        tau = 0
        assert d == period * (1 << address_bits)

        current_addresses = range(1 << address_bits)
        next_addresses = range(1 << (address_bits + 1))

        # Source cell 510: two connectors ahead is next scale cell 0.
        for s in current_addresses:
            t = b + 510 * d + tau + period * s
            for s0 in next_addresses:
                t2 = 2 * b + tau + period * s0
                assert 0 < t2 - t < 4 * d
                assert 7 * 84 * (t + 1) > 11 * 53 * (t2 + 1)
                checked += 1

        # Source cell 511: two connectors ahead is next scale cell 1.
        for s in current_addresses:
            t = b + 511 * d + tau + period * s
            for s1 in next_addresses:
                t2 = 2 * b + 2 * d + tau + period * s1
                assert 0 < t2 - t < 5 * d
                assert 7 * 84 * (t + 1) > 11 * 53 * (t2 + 1)
                checked += 1

        # Exact final-boundary coefficient:
        # (5/53)(2B-d) - 55d = (275/3392)B > 0.
        assert 10 * 512 - 5 - 55 * 53 == 2200
        assert 2200 == 275 * 8

    return checked


def main() -> None:
    checked = verify_boundary()
    print(f"verified {checked} arbitrary adaptive scale-boundary cases")
    print("all adaptive 512-cell boundary checks passed")


if __name__ == "__main__":
    main()
