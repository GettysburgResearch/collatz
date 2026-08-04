#!/usr/bin/env python3
"""Exact checks for L-0014, T-0018, and T-0019.

The script uses only the Python standard library. It verifies:

* finite-interval Collatz renormalization and its fixed/diagonal gauges;
* the ordered two-child particle rewrite and exact branch populations;
* total descendant mass 2**L * x;
* the distinguished ordinary Collatz spine;
* exact phase-escape cylinder weights along ordinary trajectories; and
* likelihood-ratio and finite-+1 correction identities.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def T(n: int) -> int:
    """Shortcut Collatz map on positive integers."""
    if n <= 0:
        raise ValueError("n must be positive")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def lower_endpoint(v: int, physical_parity: int) -> int:
    """Lower endpoint of the interval lift."""
    if physical_parity:
        return 3 * v // 2
    return (v + 1) // 2


def upper_endpoint(q: int, physical_parity: int) -> int:
    """Upper endpoint of the interval lift."""
    if physical_parity:
        return (3 * q + 1) // 2
    return (q + 1) // 2


def phase_population(x: int, bit: int) -> int:
    """R_0(x)=floor(x/2), R_1(x)=ceil(3x/2)."""
    return (3 * x + 1) // 2 if bit else x // 2


def children(parent: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return the two (branch_bit, child_rank) descendants of one particle."""
    if parent <= 0:
        raise ValueError("parent rank must be positive")
    if parent % 2 == 0:
        k = parent // 2
        return (0, k), (1, 3 * k)
    k = (parent + 1) // 2
    return (1, 3 * k - 2), (1, 3 * k - 1)


def endpoint_population(x: int, word: tuple[int, ...] | list[int]) -> int:
    for bit in word:
        x = phase_population(x, bit)
    return x


def verify_interval_lift() -> None:
    for n in range(1, 501):
        bit = n & 1
        for v in range(1, 501):
            q = v + n
            v1 = lower_endpoint(v, bit)
            q1 = upper_endpoint(q, bit)
            assert q1 - v1 == T(n)

    for n0 in range(1, 2_001):
        n = n0
        fixed_v, fixed_q = 1, n + 1
        diagonal_v, diagonal_q = n + 1, 2 * n + 1

        for _ in range(50):
            bit = n & 1
            fixed_v = lower_endpoint(fixed_v, bit)
            fixed_q = upper_endpoint(fixed_q, bit)
            diagonal_v = lower_endpoint(diagonal_v, bit)
            diagonal_q = upper_endpoint(diagonal_q, bit)
            n = T(n)

            assert (fixed_v, fixed_q) == (1, n + 1)
            assert (diagonal_v, diagonal_q) == (n + 1, 2 * n + 1)


def verify_particle_split() -> None:
    for x in range(1, 5_001):
        for bit in (0, 1):
            ranks: list[int] = []
            for parent in range(1, x + 1):
                ranks.extend(
                    child_rank
                    for branch_bit, child_rank in children(parent)
                    if branch_bit == bit
                )
            assert ranks == list(range(1, phase_population(x, bit) + 1))

    for x in range(1, 101):
        for length in range(0, 11):
            total = sum(
                endpoint_population(x, word)
                for word in product((0, 1), repeat=length)
            )
            assert total == (1 << length) * x


def verify_distinguished_spines() -> None:
    for start in range(1, 1_001):
        state = start
        word: list[int] = []

        for _ in range(100):
            bit = state & 1
            word.append(bit)

            if state % 2 == 0:
                distinguished = (0, state // 2)
            else:
                distinguished = (1, (3 * state + 1) // 2)

            assert distinguished in children(state)
            state = T(state)
            assert distinguished[1] == state
            assert endpoint_population(start, word) == state


def verify_likelihood_identities() -> None:
    for start in range(1, 501):
        state = start
        odd_steps = 0
        correction_product = Fraction(1)

        for length in range(1, 61):
            if state % 2:
                odd_steps += 1
                correction_product *= Fraction(3 * state + 1, 3 * state)

            state = T(state)

            escape_mass = Fraction(state, (1 << length) * start)
            growth_mass = Fraction(3**odd_steps, 4**length)

            assert escape_mass / growth_mass == correction_product
            assert escape_mass / Fraction(1, 1 << length) == Fraction(state, start)

            # One distinguished descendant of the rightmost root among all
            # depth-length descendants, and one distinguished descendant per root.
            marked_root_mass = Fraction(1, (1 << length) * start)
            any_ordinary_root_mass = Fraction(1, 1 << length)
            assert marked_root_mass * start == any_ordinary_root_mass


def main() -> None:
    verify_interval_lift()
    print("verified finite interval lift and fixed/diagonal gauges")

    verify_particle_split()
    print("verified ordered particle split and 2^L mass conservation")

    verify_distinguished_spines()
    print("verified distinguished ordinary Collatz spines")

    verify_likelihood_identities()
    print("verified escape/growth likelihood and marked-spine identities")

    print("all interval-particle-spine checks passed")


if __name__ == "__main__":
    main()
