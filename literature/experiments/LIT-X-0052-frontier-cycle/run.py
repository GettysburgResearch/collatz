#!/usr/bin/env python3
"""Exact exclusion checker for LIT-KTHM-0052.

At accelerated odd length 184, a cycle with the first unexcluded count of
92 local minima must alternate valuations 1 and >=2.  Writing the total
valuation as 276+H, the entire word is parameterized by H nondecreasing
unit-jump positions.  For fixed multiplier m, successive 2-adic valuations
recover the only possible jump sequence.

The script checks H=16,...,20 directly.  For every larger H, the decoder is
2-adically stable in one of two gcd classes and a finite reference scan proves
that every candidate fails before position 21.
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
BLOCKS = 92
BASELINE_A = 276
Q0 = 9**BLOCKS
Q92 = 8**BLOCKS
Q = (None,) + tuple(9 ** (BLOCKS - j) * 8**j for j in range(1, BLOCKS + 1))

H16_FACTORS = (
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


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 requires a positive integer")
    return (n & -n).bit_length() - 1


def is_prime_64(n: int) -> bool:
    """Deterministic Miller-Rabin for n < 2^64."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
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


def denominator(extra: int) -> int:
    return (1 << extra) * Q92 - Q0


def decode(
    m: int,
    denominator_reduced: int,
    jump_count: int,
) -> tuple[bool, str, list[int], int, int]:
    """Decode at most jump_count positions from one multiplier."""
    remainder = m * denominator_reduced
    positions: list[int] = []
    maximum_v = 0

    for r in range(jump_count):
        if remainder <= 0:
            return False, "nonpositive", positions, remainder, maximum_v
        valuation = v2(remainder)
        maximum_v = max(maximum_v, valuation)
        if (valuation - r) % 3:
            return False, "valuation_mod3", positions, remainder, maximum_v
        j = (valuation - r) // 3
        if not 1 <= j <= BLOCKS:
            return False, "position_range", positions, remainder, maximum_v
        if positions and j < positions[-1]:
            return False, "position_order", positions, remainder, maximum_v
        term = (1 << r) * Q[j]
        if term > remainder:
            return False, "term_overshoot", positions, remainder, maximum_v
        remainder -= term
        positions.append(j)

    if remainder:
        return False, "nonzero_remainder", positions, remainder, maximum_v
    return True, "solution", positions, 0, maximum_v


def exact_height_scan(extra: int) -> dict[str, Any]:
    d = denominator(extra)
    if d <= 0:
        raise ValueError("positive cycle denominator required")
    gcd5 = math.gcd(d, 5)
    reduced = d // gcd5
    j_min = ((1 << extra) - 1) * Q92
    j_max = ((1 << extra) - 1) * Q[1]
    m_min = (j_min + reduced - 1) // reduced
    m_max = j_max // reduced

    failures: Counter[str] = Counter()
    depths: Counter[int] = Counter()
    transcript = hashlib.sha256()
    eligible = 0
    solutions: list[dict[str, Any]] = []

    for m in range(m_min, m_max + 1):
        initial_v = v2(m)
        if initial_v < 3 or initial_v % 3:
            failures["initial_v2_filter"] += 1
            continue
        eligible += 1
        ok, reason, positions, _, _ = decode(m, reduced, extra)
        failures[reason] += 1
        depths[len(positions)] += 1
        transcript.update(
            f"{m}:{reason}:{len(positions)}:{','.join(map(str, positions))}\n".encode(
                "ascii"
            )
        )
        if ok:
            solutions.append({"m": m, "jump_positions": positions})

    assert not solutions
    return {
        "eligible_after_initial_v2": eligible,
        "extra_mass": extra,
        "failure_counts": dict(sorted(failures.items())),
        "failure_depth_counts": {str(k): value for k, value in sorted(depths.items())},
        "gcd_with_5": gcd5,
        "m_max": m_max,
        "m_min": m_min,
        "solution_count": 0,
        "total_m": m_max - m_min + 1,
        "total_valuation": BASELINE_A + extra,
        "transcript_sha256": transcript.hexdigest(),
    }


def reference_scan(gcd5: int, m_max: int, reference_extra: int) -> dict[str, Any]:
    d = denominator(reference_extra)
    assert math.gcd(d, 5) == gcd5
    reduced = d // gcd5

    failures: Counter[str] = Counter()
    depths: Counter[int] = Counter()
    transcript = hashlib.sha256()
    eligible = 0
    maximum_v = 0
    survivors: list[dict[str, Any]] = []

    for m in range(1, m_max + 1):
        initial_v = v2(m)
        if initial_v < 3 or initial_v % 3:
            failures["initial_v2_filter"] += 1
            continue
        eligible += 1

        # Every candidate is expected to fail well before 32 positions.  We do
        # not demand a zero final remainder in this reference scan: the purpose
        # is to find a stable early valuation contradiction.
        remainder = m * reduced
        positions: list[int] = []
        reason = "survived_reference_window"
        for r in range(32):
            valuation = v2(remainder)
            maximum_v = max(maximum_v, valuation)
            if (valuation - r) % 3:
                reason = "valuation_mod3"
                break
            j = (valuation - r) // 3
            if not 1 <= j <= BLOCKS:
                reason = "position_range"
                break
            if positions and j < positions[-1]:
                reason = "position_order"
                break
            remainder -= (1 << r) * Q[j]
            positions.append(j)

        failures[reason] += 1
        depths[len(positions)] += 1
        transcript.update(
            f"{m}:{reason}:{len(positions)}:{','.join(map(str, positions))}\n".encode(
                "ascii"
            )
        )
        if reason == "survived_reference_window":
            survivors.append({"m": m, "jump_positions": positions})

    assert not survivors
    return {
        "eligible_after_initial_v2": eligible,
        "failure_counts": dict(sorted(failures.items())),
        "failure_depth_counts": {str(k): value for k, value in sorted(depths.items())},
        "gcd_class": gcd5,
        "m_max": m_max,
        "maximum_decoded_positions": max(depths),
        "maximum_observed_v2": maximum_v,
        "reference_height": reference_extra,
        "survivor_count": 0,
        "transcript_sha256": transcript.hexdigest(),
    }


def run() -> dict[str, Any]:
    h16_d = denominator(16)
    assert h16_d == (1 << 292) - 3**184
    assert math.prod(H16_FACTORS) == h16_d
    assert len(set(H16_FACTORS)) == len(H16_FACTORS)
    assert all(is_prime_64(p) for p in H16_FACTORS)

    small = [exact_height_scan(extra) for extra in range(16, 21)]
    assert [item["solution_count"] for item in small] == [0, 0, 0, 0, 0]

    ref_g1 = reference_scan(1, 73778, 501)
    ref_g5 = reference_scan(5, 1005828, 500)
    assert ref_g1["maximum_observed_v2"] == 31
    assert ref_g5["maximum_observed_v2"] == 42

    # For H>=21 in the gcd-1 class, changing H changes m*D_H by a
    # number divisible by at least 2^(H+276+3), hence by 2^300.
    # For H>=24 in the gcd-5 class the corresponding margin is 2^303.
    # Both margins exceed every valuation read by the reference decoders.
    stability = {
        "gcd_1_heights": "H>=21 and H mod4 !=0",
        "gcd_1_max_observed_v2": 31,
        "gcd_1_min_perturbation_v2": 300,
        "gcd_5_heights": "H>=24 and H mod4 ==0",
        "gcd_5_max_observed_v2": 42,
        "gcd_5_min_perturbation_v2": 303,
        "uniform_m_max_gcd_1": 73778,
        "uniform_m_max_gcd_5": 1005828,
    }

    return {
        "claim_id": "LIT-KTHM-0052",
        "conclusion": "no positive accelerated Collatz cycle has accelerated odd length 184",
        "exact_small_heights": small,
        "fixed_data": {
            "baseline_total_valuation": BASELINE_A,
            "blocks": BLOCKS,
            "h16_denominator": h16_d,
            "h16_factorization": [[p, 1] for p in H16_FACTORS],
            "minimum_positive_extra_mass": 16,
            "q_0": Q0,
            "q_92": Q92,
        },
        "stability_certificate": stability,
        "stable_reference_classes": [ref_g1, ref_g5],
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
