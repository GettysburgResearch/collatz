#!/usr/bin/env python3
"""Exact exclusion checker for LIT-KTHM-0052.

The alternating 92-local-minimum family is parameterized by sixteen unit
height jumps at nondecreasing block positions j_0,...,j_15 in {1,...,92}.
The cycle divisibility condition is equivalent to

    sum_r 2^r * 9^(92-j_r) * 8^j_r = m * ((2^292-3^184)/5).

For fixed m, successive 2-adic valuations recover every j_r uniquely.
This script scans the exact finite multiplier interval and finds no solution.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any

K = 184
A = 292
BLOCKS = 92
EXTRA = 16
D = (1 << A) - 3**K
DP = D // 5
FACTORS = (
    5,
    11,
    13,
    17,
    83,
    89,
    179,
    1097,
    1301,
    2963,
    4547,
    5113,
    13457,
    28697,
    1626211,
    192491569,
    177790780231,
    314328249709,
    167385996821689,
)
Q = (None,) + tuple(9 ** (BLOCKS - j) * 8**j for j in range(1, BLOCKS + 1))


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 requires a positive integer")
    return (n & -n).bit_length() - 1


def is_prime_64(n: int) -> bool:
    """Deterministic Miller-Rabin for n < 2^64."""
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def decode_multiplier(m: int) -> tuple[bool, str, int, list[int], int]:
    """Recover the only possible jump positions for one multiplier m."""
    remainder = m * DP
    positions: list[int] = []
    for r in range(EXTRA):
        if remainder <= 0:
            return False, "nonpositive", r, positions, remainder
        valuation = v2(remainder)
        if (valuation - r) % 3:
            return False, "valuation_mod3", r, positions, remainder
        j = (valuation - r) // 3
        if not 1 <= j <= BLOCKS:
            return False, "position_range", r, positions, remainder
        if positions and j < positions[-1]:
            return False, "position_order", r, positions, remainder
        term = (1 << r) * Q[j]
        if term > remainder:
            return False, "term_overshoot", r, positions, remainder
        remainder -= term
        positions.append(j)
    if remainder:
        return False, "nonzero_remainder", EXTRA, positions, remainder
    return True, "solution", EXTRA, positions, 0


def run() -> dict[str, Any]:
    assert D % 5 == 0
    assert math.prod(FACTORS) == D
    assert len(set(FACTORS)) == len(FACTORS)
    assert all(is_prime_64(p) for p in FACTORS)

    j_min = ((1 << EXTRA) - 1) * Q[BLOCKS]
    j_max = ((1 << EXTRA) - 1) * Q[1]
    m_min = (j_min + DP - 1) // DP
    m_max = j_max // DP
    assert (m_min, m_max) == (23, 1005828)

    failures: Counter[str] = Counter()
    depths: Counter[int] = Counter()
    transcript = hashlib.sha256()
    eligible = 0
    solutions: list[dict[str, Any]] = []
    near_misses: list[dict[str, Any]] = []

    for m in range(m_min, m_max + 1):
        initial_v = v2(m)
        if initial_v < 3 or initial_v % 3:
            failures["initial_v2_filter"] += 1
            continue

        eligible += 1
        ok, reason, depth, positions, remainder = decode_multiplier(m)
        failures[reason] += 1
        depths[depth] += 1
        transcript.update(
            f"{m}:{reason}:{depth}:{','.join(map(str, positions))}\n".encode("ascii")
        )

        if ok:
            solutions.append({"m": m, "jump_positions": positions})
        elif reason == "nonzero_remainder":
            near_misses.append(
                {
                    "m": m,
                    "jump_positions": positions,
                    "remainder": remainder,
                    "remainder_bits": remainder.bit_length(),
                    "gcd_with_denominator_over_5": math.gcd(remainder, DP),
                }
            )

    assert not solutions

    return {
        "claim_id": "LIT-KTHM-0052",
        "conclusion": (
            "no alternating 92-local-minimum accelerated cycle "
            "at (k,A)=(184,292)"
        ),
        "multiplier_scan": {
            "eligible_after_initial_v2": eligible,
            "failure_counts": dict(sorted(failures.items())),
            "failure_depth_counts": {
                str(k): value for k, value in sorted(depths.items())
            },
            "m_max": m_max,
            "m_min": m_min,
            "solution_count": len(solutions),
            "total_m": m_max - m_min + 1,
            "transcript_sha256": transcript.hexdigest(),
        },
        "parameters": {
            "accelerated_length": K,
            "blocks": BLOCKS,
            "denominator": D,
            "denominator_over_5": DP,
            "extra_mass": EXTRA,
            "factorization": [[p, 1] for p in FACTORS],
            "largest_factor_bits": max(p.bit_length() for p in FACTORS),
            "total_valuation": A,
        },
        "terminal_near_misses": near_misses,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"

    if args.check_results is not None:
        expected = args.check_results.read_text(encoding="utf-8")
        if text != expected:
            raise SystemExit("canonical result mismatch")

    if args.output is not None:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
