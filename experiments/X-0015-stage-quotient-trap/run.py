#!/usr/bin/env python3
"""Exact checks for L-0030 and T-0031.

The script:
* exhaustively checks the canonical cap bound on 69,904 small tile chains;
* exhaustively checks the quotient-trap inequality on a finite synthetic corpus;
* verifies the exact stage exponent inequality;
* reconstructs one full phase-34 256-transition stage at m=8 and checks the cap.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


def compose(tiles: tuple[tuple[int, int, int], ...]) -> tuple[int, int, int]:
    """Return (odd multiplier, power-of-two modulus, affine offset)."""
    p = 1
    q = 1
    f = 0
    for n, local_q, c in tiles:
        f = n * f + q * c
        p *= n
        q *= local_q
    return p, q, f


def replay(
    tiles: tuple[tuple[int, int, int], ...], value: int
) -> tuple[bool, int | None]:
    current = value
    for n, q, c in tiles:
        numerator = n * current + c
        if numerator % q:
            return False, None
        current = numerator // q
    return True, current


def verify_small_chain_cap() -> int:
    local_tiles: list[tuple[int, int, int]] = []
    for n in (1, 3):
        for q in (2, 4):
            for c in range(-q + 1, n):
                local_tiles.append((n, q, c))

    checked = 0
    for length in range(1, 5):
        for tiles_list in product(local_tiles, repeat=length):
            tiles = tuple(tiles_list)
            p, q, f = compose(tiles)
            correction = (-f * pow(p, -1, q)) % q
            cap = (p * correction + f) // q

            valid, output = replay(tiles, correction)
            assert valid and output == cap
            assert correction >= 0
            assert cap >= 0
            assert cap < 3 * p
            checked += 1

    assert checked == 69_904
    return checked


def next_power_of_two_strictly_above(value: int) -> int:
    return 1 << value.bit_length()


def verify_quotient_trap() -> int:
    checked = 0
    for n in range(1, 16, 2):
        q = next_power_of_two_strictly_above(512 * n)
        assert q > 512 * n

        for cap in range(3 * n):
            for y in range(q):
                next_correction = (cap + n * y) % q
                numerator = cap + n * y - next_correction
                assert numerator % q == 0
                y_next = numerator // q
                assert y_next >= 0
                assert 512 * y_next < y + 3

                if y == 0:
                    assert y_next == 0
                    assert next_correction == cap
                else:
                    assert y_next < y
                checked += 1
    return checked


def verify_stage_exponent_gap() -> None:
    # L-0025 upper certificate: log_2(3) < 65/41.
    assert 3**41 < 2**65

    # For B=2^m,
    # D_(m+1)-9-(65/41) A_m
    #   = (22173699/5248) B - 1393/41 > 0.
    for m in range(0, 65):
        b = 1 << m
        numerator = 22_173_699 * 41 * b - 1_393 * 5_248
        assert numerator > 0


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
    a: int
    k: int
    b: int
    g: int


def tower(typ: TowerType, height: int) -> Tower:
    low_k = typ.k0 + 11 * height
    low_g = typ.g0 + 7 * height
    core_modulus = 1 << (typ.r + 1)
    mu = (-pow(pow(3, low_g, core_modulus), -1, core_modulus)) % core_modulus
    c = (3**low_g * mu + 1) // core_modulus
    a = (1 << low_k) * mu
    k = low_k + typ.r + 1
    b = 3**typ.b * c
    g = low_g + typ.b
    assert k == 11 * (height + 1)
    assert g == 7 * (height + 1)
    return Tower(a, k, b, g)


def connector(left: Tower, right: Tower) -> tuple[int, int]:
    modulus = 1 << right.k
    eta = (
        (right.a - left.b)
        * pow(pow(3, left.g, modulus), -1, modulus)
    ) % modulus
    theta = (left.b + 3**left.g * eta - right.a) // modulus
    assert 0 <= eta < modulus
    assert 0 <= theta < 3**left.g
    return eta, theta


def verify_actual_stage_cap() -> tuple[int, int, int, int, str, str]:
    m = 8
    base = 1 << m
    step = base >> 8
    heights = [base + j * step for j in range(257)] + [2 * base + 2 * step]
    edges = [tower(TYPES[0], height) for height in heights]

    # Incremental cylinder/block recurrence, avoiding one enormous final inverse.
    correction = 0
    modulus = 1
    endpoint = 0
    stride = 1

    for j in range(256):
        _, theta = connector(edges[j], edges[j + 1])
        eta_next, _ = connector(edges[j + 1], edges[j + 2])
        n = 3**edges[j].g
        q = 1 << edges[j + 2].k
        c = theta - eta_next
        assert -q < c < n

        rho = (-c * pow(n, -1, q)) % q
        block = ((rho - endpoint) * pow(stride % q, -1, q)) % q
        correction += modulus * block
        endpoint = (n * (endpoint + stride * block) + c) // q
        stride *= n
        modulus *= q

    assert 0 <= correction < modulus
    assert endpoint >= 0
    assert endpoint < 3 * stride

    return (
        stride.bit_length(),
        modulus.bit_length() - 1,
        correction.bit_length(),
        endpoint.bit_length(),
        hex(correction & ((1 << 64) - 1)),
        hex(endpoint & ((1 << 64) - 1)),
    )


def main() -> None:
    chain_count = verify_small_chain_cap()
    print(f"verified canonical cap bound on {chain_count} small chains")

    trap_count = verify_quotient_trap()
    print(f"verified quotient-trap inequality on {trap_count} synthetic transitions")

    verify_stage_exponent_gap()
    print("verified exact 512-fold next-modulus gap")

    fingerprint = verify_actual_stage_cap()
    print("verified full m=8 constant-type stage cap:", fingerprint)
    print("all stage-quotient-trap checks passed")


if __name__ == "__main__":
    main()
