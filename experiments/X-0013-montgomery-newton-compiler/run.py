#!/usr/bin/env python3
"""Exact checks for L-0026, L-0027, T-0025, and O-0010."""

from __future__ import annotations

from dataclasses import dataclass


def v2(n: int) -> int:
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def montgomery_lift(
    N: int,
    C: int,
    eta: int,
    k: int,
    s: int,
) -> tuple[int, int, int, int]:
    """Lift C + N*eta = 2^k theta by s binary digits."""
    assert N > 0 and N & 1
    assert k >= 1 and s >= 1
    assert 0 <= eta < 1 << k
    total = C + N * eta
    assert total >= 0 and total % (1 << k) == 0
    theta = total >> k

    modulus = 1 << s
    digit = (-theta * pow(N, -1, modulus)) % modulus
    phi = (theta + N * digit) >> s
    lifted = eta + (1 << k) * digit

    assert 0 <= digit < modulus
    assert phi >= 0
    assert 0 <= lifted < 1 << (k + s)
    assert C + N * lifted == (1 << (k + s)) * phi
    return theta, digit, phi, lifted


def verify_montgomery_lifts() -> None:
    for N in range(1, 40, 2):
        for C in range(-24, 25):
            for k in range(1, 8):
                eta = (-C * pow(N, -1, 1 << k)) % (1 << k)
                if C + N * eta < 0:
                    continue
                for s in range(1, 8):
                    _, _, _, lifted = montgomery_lift(N, C, eta, k, s)
                    direct = (-C * pow(N, -1, 1 << (k + s))) % (
                        1 << (k + s)
                    )
                    assert lifted == direct


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


def stage_precision(m: int) -> int:
    assert m >= 8
    target_height = (1 << m) + (1 << (m - 8))
    return 11 * (target_height + 1)


def newton_workspace(m: int, inverse: int) -> tuple[int, int]:
    """Return the 2Q_m-bit inverse and exact next-stage prefix."""
    q = stage_precision(m)
    q_next = stage_precision(m + 1)
    assert q_next == 2 * q - 11
    assert 0 <= inverse < 1 << q

    N = 3 ** (7 * (1 << m))
    assert N * inverse % (1 << q) == 1

    full = inverse * (2 - N * inverse) % (1 << (2 * q))
    assert N * full % (1 << (2 * q)) == 1

    next_inverse = full * full % (1 << q_next)
    assert N * N * next_inverse % (1 << q_next) == 1
    return full, next_inverse


def verify_cycle_newton_compiler() -> None:
    for m in range(8, 11):
        q = stage_precision(m)
        q_next = stage_precision(m + 1)
        B = 1 << m
        d = 1 << (m - 8)
        N = 3 ** (7 * B)

        inverse = pow(N, -1, 1 << q)
        full, generated = newton_workspace(m, inverse)
        assert generated == pow(N * N, -1, 1 << q_next)

        # The full Newton workspace covers the deepest target in the stage.
        max_target_depth = 11 * (2 * B + 1)
        assert max_target_depth < 2 * q

        step_inverse = pow(3 ** (7 * d), -1, 1 << (2 * q))
        fixed_inverse = pow(3, -7, 1 << (2 * q))

        # Test the first, internal, near-boundary, and deepest connectors.
        for j in (0, 1, 127, 255):
            source_height = B + j * d
            target_height = source_height + d
            source_inverse = full * pow(step_inverse, j, 1 << (2 * q))
            source_inverse %= 1 << (2 * q)

            target_depth = 11 * (target_height + 1)
            assert target_depth <= 2 * q
            direct = pow(3 ** (7 * source_height), -1, 1 << target_depth)
            assert source_inverse % (1 << target_depth) == direct

            inverse_G = fixed_inverse * source_inverse % (1 << target_depth)

            for source_type in TYPES:
                left = tower(source_type, source_height)
                for target_type in TYPES:
                    right = tower(target_type, target_height)
                    eta, theta = connector(left, right)
                    compiled = (
                        (right.A - left.B)
                        * (inverse_G % (1 << right.K))
                    ) % (1 << right.K)
                    assert eta == compiled
                    assert (
                        left.B + 3**left.G * eta
                        == right.A + (1 << right.K) * theta
                    )


def u_m_mod(m: int, bits: int) -> int:
    precision = bits + m + 2
    modulus = 1 << precision
    inverse = pow(3 ** (7 * (1 << m)), -1, modulus)
    assert (inverse - 1) % (1 << (m + 2)) == 0
    return ((inverse - 1) >> (m + 2)) % (1 << bits)


def u_infinity_mod(bits: int) -> int:
    """7*sum_{n>=1} 4^(n-1)/n modulo 2^bits."""
    modulus = 1 << bits
    total = 0
    n = 1
    while True:
        valuation = 2 * (n - 1) - v2(n)
        if valuation < bits:
            odd_part = n >> v2(n)
            term = 7 * (1 << valuation) * pow(odd_part, -1, modulus)
            total = (total + term) % modulus
        if n > bits + 2 and 2 * (n - 1) - n.bit_length() >= bits:
            break
        n += 1
    return total


def verify_logarithmic_bulk() -> None:
    for m in range(2, 14):
        bits = m + 12
        finite = u_m_mod(m, bits)
        limit = u_infinity_mod(bits)
        difference = (limit - finite) % (1 << bits)
        assert v2(difference) == m + 1

        finite_next = u_m_mod(m + 1, bits)
        predicted = (finite + (1 << (m + 1)) * finite * finite) % (
            1 << bits
        )
        assert finite_next == predicted

    assert u_infinity_mod(64) == 0x5522E8F2837EE855


def main() -> None:
    verify_montgomery_lifts()
    print("verified offset Montgomery precision lifts")

    verify_cycle_newton_compiler()
    print("verified full Newton workspace, deepest connectors, and eleven-bit slack")

    verify_logarithmic_bulk()
    print("verified 2-adic logarithmic bulk and exact convergence rate")

    print("all Montgomery-Newton compiler checks passed")


if __name__ == "__main__":
    main()
