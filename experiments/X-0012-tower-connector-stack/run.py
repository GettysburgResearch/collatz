#!/usr/bin/env python3
"""Exact checks for L-0016--L-0018 and T-0021.

The experiment reconstructs the four self-return mismatch towers at phase -34
of the negative eleven-cycle, verifies their binary-to-ternary tail replacement,
constructs every finite mixed-radix connector in a bounded census, and checks
the finite-ray decomposition for bounded high tails.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def P(v: int) -> int:
    return v // 2 if v % 2 == 0 else (3 * v - 1) // 2


def C(v: int) -> int:
    return 3 * v // 2 if v % 2 == 0 else (v + 1) // 2


def iterate(n: int, steps: int) -> int:
    for _ in range(steps):
        n = T(n)
    return n


@dataclass(frozen=True)
class TowerType:
    k0: int
    phase: int
    r: int
    b: int
    g0: int
    target: int


@dataclass(frozen=True)
class Tower:
    typ: TowerType
    t: int
    k: int
    g: int
    mu: int
    c: int
    A: int
    K: int
    B: int
    G: int
    length: int
    odd_count: int


def cycle_from(v0: int, length: int) -> list[int]:
    values = []
    v = v0
    for _ in range(length):
        values.append(v)
        v = P(v)
    assert v == v0
    return values


V11 = cycle_from(34, 11)
SELECTED = set(V11 + [5, 7, 10, 1])


def basin_data(w: int) -> tuple[int, int, int]:
    """Return recovery length, odd count, and first selected target after C(w)."""
    x = C(w)
    r = 0
    b = 0
    while x not in SELECTED:
        b += x & 1
        x = P(x)
        r += 1
    return r, b, x


def self_return_types() -> list[TowerType]:
    out = []
    odd_prefix = 0
    for k0, w in enumerate(V11):
        r, b, target = basin_data(w)
        delta = 1 - (w & 1)
        g0 = odd_prefix + delta
        if target == 34:
            out.append(TowerType(k0, w, r, b, g0, target))
        odd_prefix += w & 1
    assert [x.k0 for x in out] == [5, 6, 7, 8]
    return out


TYPES = self_return_types()


def tower(typ: TowerType, t: int) -> Tower:
    ell = 11
    a = 7
    k = typ.k0 + ell * t
    g = typ.g0 + a * t
    modulus = 1 << (typ.r + 1)
    mu = (-pow(pow(3, g, modulus), -1, modulus)) % modulus
    assert mu & 1
    c = (3**g * mu + 1) // modulus
    A = (1 << k) * mu
    K = k + typ.r + 1
    B = 3**typ.b * c
    G = g + typ.b
    length = K
    odd_count = G
    assert 0 <= A < 1 << K
    assert 0 <= B < 3**G
    return Tower(typ, t, k, g, mu, c, A, K, B, G, length, odd_count)


def replacement_check(edge: Tower, h: int) -> tuple[int, int]:
    q = edge.A + (1 << edge.K) * h
    qp = edge.B + 3**edge.G * h
    physical = q - 34
    target = qp - edge.typ.target
    assert physical > 0
    assert iterate(physical, edge.length) == target
    return q, qp


def connector(left: Tower, right: Tower) -> tuple[int, int]:
    """Canonical connector h=eta+2^K z, h'=theta+3^G z."""
    modulus = 1 << right.K
    eta = (
        (right.A - left.B)
        * pow(pow(3, left.G, modulus), -1, modulus)
    ) % modulus
    numerator = left.B + 3**left.G * eta - right.A
    assert numerator % modulus == 0
    theta = numerator // modulus
    assert 0 <= eta < modulus
    assert theta >= 0
    return eta, theta


def order_three_power(exponent: int, bits: int) -> int:
    """ord_{2^bits}(3^exponent), using the exact 2-adic order formula."""
    assert exponent >= 1 and bits >= 1
    if bits == 1:
        return 1
    if bits == 2:
        return 1 if exponent % 2 == 0 else 2
    twos = 0
    x = exponent
    while x % 2 == 0:
        twos += 1
        x //= 2
    return 1 << max(0, bits - 2 - twos)


def verify_periods() -> list[tuple[int, int]]:
    rows = []
    for typ in TYPES:
        period = order_three_power(7, typ.r + 1)
        values = [tower(typ, t).mu for t in range(period)]
        assert len(set(values)) == period
        for t in range(4 * period):
            assert tower(typ, t + period).mu == tower(typ, t).mu
        rows.append((typ.k0, period))
    assert rows == [(5, 16), (6, 8), (7, 4), (8, 2)]
    return rows


def verify_replacements() -> None:
    samples = (0, 1, 2, 17, 1000)
    for typ in TYPES:
        for t in range(12):
            edge = tower(typ, t)
            for h in samples:
                replacement_check(edge, h)


def verify_connectors() -> tuple[int, list[tuple[int, int, int, int]]]:
    count = 0
    lane_rows = []
    samples = (0, 1, 3, 17)
    for left_type in TYPES:
        for right_type in TYPES:
            for t in range(8):
                for u in range(8):
                    left = tower(left_type, t)
                    right = tower(right_type, u)
                    eta, theta = connector(left, right)
                    for z in samples:
                        h = eta + (1 << right.K) * z
                        hp = theta + 3**left.G * z
                        lhs = left.B + 3**left.G * h
                        rhs = right.A + (1 << right.K) * hp
                        assert lhs == rhs

                        q, qp = replacement_check(left, h)
                        assert qp == rhs
                        # The connector places the output in the next tower's
                        # binary input cylinder. Replaying the next block is exact.
                        q2, _ = replacement_check(right, hp)
                        assert q2 == qp
                    count += 1

    # Canonical same-type t -> t+1 connector seeds.
    for typ in TYPES:
        eta, theta = connector(tower(typ, 0), tower(typ, 1))
        lane_rows.append((typ.k0, eta, theta, tower(typ, 1).K))
    assert lane_rows == [
        (5, 2241439, 1168, 22),
        (6, 865722, 451, 22),
        (7, 577148, 300, 22),
        (8, 1782866, 929, 22),
    ]
    return count, lane_rows


def verify_inverse_prefix_nonperiodicity() -> None:
    """Finite check of the exact order obstruction used in L-0018."""
    for K in range(3, 64):
        order = order_three_power(1, K)
        assert order == 1 << (K - 2)

    # No fixed P <= 2^12 can repeat 3^(-7t) at all growing precisions.
    for period in range(1, 1 << 12):
        K = 15 + period.bit_length()
        assert pow(3, 7 * period, 1 << K) != 1


def verify_bounded_tail_rays() -> None:
    tails = (0, 1, 5)
    for typ in TYPES:
        period = order_three_power(7, typ.r + 1)
        scale = 1 << (11 * period)
        for residue in range(period):
            for h in tails:
                base = tower(typ, residue)
                q0 = base.A + (1 << base.K) * h
                for j in range(1, 5):
                    tj = residue + period * j
                    edge = tower(typ, tj)
                    qj = edge.A + (1 << edge.K) * h
                    assert qj == q0 * scale**j
                    # Physical state is the exact affine-geometric ray -34 + qj.
                    assert qj - 34 == -34 + q0 * scale**j


def main() -> None:
    periods = verify_periods()
    print("verified tower-core periods:", periods)

    verify_replacements()
    print("verified exact binary-to-ternary tail replacements")

    count, lane_rows = verify_connectors()
    print(f"verified {count} canonical connector families")
    print("same-type t->t+1 seeds:", lane_rows)

    verify_inverse_prefix_nonperiodicity()
    print("verified growing inverse-prefix order obstruction")

    verify_bounded_tail_rays()
    print("verified bounded-tail finite-ray decomposition")
    print("all tower-connector-stack checks passed")


if __name__ == "__main__":
    main()
