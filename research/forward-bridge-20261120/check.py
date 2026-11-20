#!/usr/bin/env python3
"""Exact bounded checks for FB-001--004; no all-integer convergence claim."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def step(n: int) -> int:
    return (3 * n + 1) // 2 if n & 1 else n // 2


def walk(n: int, steps: int) -> tuple[int, int]:
    odd = 0
    for _ in range(steps):
        odd += n & 1
        n = step(n)
    return n, odd


def first_arrival(n: int, limit: int = 100000) -> tuple[int, int]:
    elapsed = odd = 0
    seen: set[int] = set()
    while n != 1:
        require(n not in seen, "a nontrivial cycle occurred in the bounded replay")
        require(elapsed < limit, "a bounded trajectory did not finish")
        seen.add(n)
        odd += n & 1
        n = step(n)
        elapsed += 1
    return elapsed, odd


def grade(record: tuple[int, int]) -> int:
    elapsed, odd = record
    return 2 * odd - elapsed


def product_height(n: int) -> Fraction:
    product = Fraction(1)
    elapsed = 0
    while n != 1:
        require(elapsed < 100000, "product replay exceeded its finite bound")
        if n & 1:
            product *= Fraction(4 * n, 3 * n + 1)
        n = step(n)
        elapsed += 1
    return product


def scaled_height(n: int, g: int) -> Fraction:
    return Fraction(n << g) if g >= 0 else Fraction(n, 1 << -g)


def nonpositive_minimum(g: int) -> int:
    require(g <= 0, "the classification does not include positive grades")
    if g % 2 == 0:
        return 1 << -g
    if g == -1:
        return 7
    return 5 * (1 << (-g - 2))


def odd_core(n: int) -> int:
    while n % 2 == 0:
        n //= 2
    return n


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bound", type=int, default=25000)
    args = parser.parse_args()
    bound = args.bound
    require(bound >= 3079, "use a bound at least 3079 to include all finite arms")

    records = {n: first_arrival(n) for n in range(1, bound + 1)}
    grades = {n: grade(record) for n, record in records.items()}
    common_clock = max(record[0] for record in records.values())
    fingerprints: dict[int, tuple[int, int]] = {}
    reverse_fingerprints: dict[tuple[int, int], int] = {}
    for n, g in grades.items():
        fingerprint = walk(n, common_clock)
        require(fingerprints.setdefault(g, fingerprint) == fingerprint,
                f"same-grade balanced equality failed at {n}")
        require(reverse_fingerprints.setdefault(fingerprint, g) == g,
                f"different grades acquired the same balanced fingerprint at {n}")
        h = scaled_height(n, g)
        if n & (n - 1) == 0:
            require(h == 1, f"power-of-two equality failed at {n}")
        else:
            require(h >= Fraction(5, 4), f"sharp gap failed at {n}")
            require((h == Fraction(5, 4)) == (odd_core(n) == 5),
                    f"sharp equality classification failed at {n}")

    product_checks = min(bound, 2048)
    for n in range(1, product_checks + 1):
        require(product_height(n) == scaled_height(n, grades[n]),
                f"exact product identity failed at {n}")

    observed_minima: dict[int, int] = {}
    for n in range(1, bound + 1, 3):
        observed_minima.setdefault(grades[n], n)
    classified_sources = 0
    for n in range(1, bound + 1, 3):
        g = grades[n]
        if g <= 0:
            expected = nonpositive_minimum(g)
            require(expected <= n, f"minimum is not a smaller candidate at {n}")
            require(observed_minima[g] == expected,
                    f"nonpositive grade minimum failed at grade {g}")
            require(walk(n, common_clock) == walk(expected, common_clock),
                    f"classified source and minimum failed to merge at {n}")
            classified_sources += 1

    finite_arms = [11, 17, 29] + [7 + 3 * (1 << h) for h in range(2, 11)]
    finite_arm_receipts = [
        {"start": n, "shortcut_steps": records[n][0], "odd_inputs": records[n][1]}
        for n in finite_arms
    ]

    lift_checks = 0
    for m in range(8):
        base = 10 * 4**m
        for h in range(2 * m + 5, 2 * m + 45):
            ell = h - 2 * m - 1
            r, e = divmod(ell - 4, 2)
            clock = 2 * m + 1 + 4 + 2 * r + e
            endpoint = 1 + 3 ** (r + 2) if e == 0 else 2 + 3 ** (r + 3)
            require(walk(base + 3 * (1 << h), clock)[0] == endpoint,
                    f"second-family high-bit identity failed at m={m}, h={h}")
            lift_checks += 1
    for h in range(11, 101):
        r, e = divmod(h - 11, 2)
        clock = 11 + 2 * r + e
        endpoint = 1 + 3 ** (r + 6) if e == 0 else 2 + 3 ** (r + 7)
        require(walk(7 + 3 * (1 << h), clock)[0] == endpoint,
                f"row-seven high-bit identity failed at h={h}")
        lift_checks += 1

    # Negative controls distinguish a merger on the cycle from a balanced
    # merger, and reject the stronger false gap with constant 3/2.
    require(walk(1, 2)[0] == walk(4, 2)[0], "negative-control endpoint changed")
    require(walk(1, 2)[1] != walk(4, 2)[1], "odd counts were accidentally ignored")
    require(grades[1] != grades[4], "different-grade negative control failed")
    require(scaled_height(5, grades[5]) < Fraction(3, 2),
            "false strengthened-gap negative control did not fail")

    print(json.dumps({
        "status": "PASS",
        "bounded_first_arrivals": bound,
        "balanced_common_clock": common_clock,
        "distinct_grades": len(fingerprints),
        "exact_product_checks": product_checks,
        "classified_nonpositive_sources_1_mod_3": classified_sources,
        "observed_nonpositive_grade_minima": {
            str(g): observed_minima[g] for g in sorted(observed_minima) if g <= 0
        },
        "finite_upper_arm_receipts": finite_arm_receipts,
        "high_bit_identity_checks": lift_checks,
        "negative_controls": 2,
        "scope": "Finite exact replay; the written proof supplies the all-family conclusions.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
