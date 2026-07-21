#!/usr/bin/env python3
"""Exact checks for L-0013 and T-0017.

The script uses only the Python standard library. It verifies:
* the rounded physical-parity phase update;
* complementarity of the two phase branches;
* finite phase-Kraft identities;
* the exact Doob h-transform and path-density formula;
* uniform positive drift bounds under the escape transform; and
* finite-depth absorption/survival data from phase 136.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import log


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def down(v: int) -> int:
    """Physical-even phase branch S_0(v)=ceil(v/2)."""
    return (v + 1) // 2


def up(v: int) -> int:
    """Physical-odd phase branch S_1(v)=floor(3v/2)."""
    return 3 * v // 2


def phase_step(v: int, physical_parity: int) -> int:
    return up(v) if physical_parity else down(v)


def coupled_step(q: int, v: int) -> tuple[int, int, int]:
    """One exact T-0014 step, returning q', v', and physical parity."""
    p = q & 1
    r = v & 1
    e = p ^ r
    q1 = (3**e * q + p) // 2
    v1 = (3**e * v + (2 * p - 1) * r) // 2
    assert T(q - v) == q1 - v1
    return q1, v1, e


def endpoint(v: int, word: tuple[int, ...]) -> int:
    for bit in word:
        v = phase_step(v, bit)
    return v


def phase_kraft(
    code: list[tuple[int, ...]], v: int
) -> tuple[Fraction, Fraction, Fraction]:
    kraft = sum(Fraction(1, 2 ** len(word)) for word in code)
    endpoint_mean = sum(
        Fraction(endpoint(v, word), 2 ** len(word)) for word in code
    )
    harmonic_mean = sum(
        Fraction(endpoint(v, word) - 1, 2 ** len(word)) for word in code
    )
    return kraft, endpoint_mean, harmonic_mean


def escape_probabilities(v: int) -> tuple[Fraction, Fraction]:
    """Doob h-transform probabilities for h(v)=v-1."""
    if v <= 1:
        raise ValueError("escape transform is defined on v > 1")
    h = v - 1
    p_down = Fraction(down(v) - 1, 2 * h)
    p_up = Fraction(up(v) - 1, 2 * h)
    assert p_down >= 0 and p_up >= 0 and p_down + p_up == 1
    return p_down, p_up


def verify_path_density(v0: int, length: int) -> None:
    """Check Q_v([w])=2^-L (V_w-1)/(v0-1) on every word."""
    total = Fraction(0)
    for word in product((0, 1), repeat=length):
        v = v0
        probability = Fraction(1)
        for bit in word:
            p_down, p_up = escape_probabilities(v)
            probability *= p_up if bit else p_down
            v = phase_step(v, bit)
            if v == 1:
                assert probability == 0
                break

        expected = Fraction(v - 1, (v0 - 1) * 2**length)
        assert probability == expected
        total += probability

    assert total == 1


def fair_distribution(v0: int, length: int) -> dict[int, int]:
    counts = {v0: 1}
    for _ in range(length):
        next_counts: dict[int, int] = defaultdict(int)
        for v, count in counts.items():
            next_counts[down(v)] += count
            next_counts[up(v)] += count
        counts = dict(next_counts)
    return counts


def main() -> None:
    # L-0013: exact rounded phase update and complementarity.
    for v in range(1, 501):
        assert down(v) + up(v) == 2 * v
        for q in range(1, 1001):
            _, v1, physical_parity = coupled_step(q, v)
            assert v1 == phase_step(v, physical_parity)
    print("verified rounded physical-parity phase coupling")

    # T-0017: finite phase-Kraft identities.
    complete_codes = [
        [(0,), (1,)],
        [(0,), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (1, 0), (1, 1)],
        [(0,), (1, 0), (1, 1, 0), (1, 1, 1)],
    ]
    for v in (2, 3, 5, 7, 136, 1000):
        for code in complete_codes:
            kraft, endpoint_mean, harmonic_mean = phase_kraft(code, v)
            assert kraft == 1
            assert endpoint_mean == v
            assert harmonic_mean == v - 1
    print("verified finite phase-Kraft identities")

    # Exact escape-transform probabilities and positive drift bounds.
    collatz_drift_floor = Fraction(3, 4)
    gamma = 0.75 * log(3) - log(2)
    delta = 0.75 * log(Fraction(4, 3)) + 0.25 * log(Fraction(1, 2))
    assert gamma > 0 and delta > 0

    for v in range(2, 10_001):
        p_down, p_up = escape_probabilities(v)
        if v % 2:
            assert p_up == Fraction(3, 4)
        else:
            assert p_up == Fraction(3, 4) + Fraction(1, 4 * (v - 1))
        assert p_up >= collatz_drift_floor

        physical_log_drift = float(p_up) * log(3) - log(2)
        phase_log_drift = (
            float(p_down) * log(Fraction(down(v), v))
            + float(p_up) * log(Fraction(up(v), v))
        )
        assert physical_log_drift >= gamma - 1e-15
        assert phase_log_drift >= delta - 1e-15

    print(
        "verified escape-transform drift bounds:",
        f"physical>={gamma:.12g}",
        f"phase>={delta:.12g}",
    )

    verify_path_density(136, 12)
    print("verified exact escape path-density formula through depth 12")

    # Finite-depth absorption data. The harmonic first moment stays exactly 135
    # while fair survival mass falls and rare escaping phases carry the mean.
    for length in (8, 12, 16, 20, 24, 28, 32):
        counts = fair_distribution(136, length)
        total = 2**length
        survival = sum(count for v, count in counts.items() if v > 1)
        harmonic = sum((v - 1) * count for v, count in counts.items())
        assert harmonic == 135 * total
        print(
            f"depth={length:2d} states={len(counts):5d} "
            f"survival={survival}/{total} "
            f"max_phase={max(counts)}"
        )

    print("all rounded-phase martingale checks passed")


if __name__ == "__main__":
    main()
