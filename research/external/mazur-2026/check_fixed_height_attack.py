#!/usr/bin/env python3
"""Small exact checks for the fixed-height theorem-development note.

This script checks finite combinatorial interfaces and exact numerical constants.
It does not prove the fixed-height contraction (C) and does not verify Collatz.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def all_supercritical_count(length: int) -> int:
    """Count words with q_j >= alpha*j for every prefix, using exact integers.

    Since alpha=log(2)/log(3) is irrational, q_j >= alpha*j is equivalent to
    3**q_j >= 2**j.
    """
    dp = {0: 1}
    for j in range(1, length + 1):
        nxt: dict[int, int] = {}
        for q, count in dp.items():
            # Append zero.
            if 3**q >= 2**j:
                nxt[q] = nxt.get(q, 0) + count
            # Append one.
            q1 = q + 1
            if 3**q1 >= 2**j:
                nxt[q1] = nxt.get(q1, 0) + count
        dp = nxt
    return sum(dp.values())


def has_good_rotation(bits: tuple[int, ...]) -> bool:
    """Check the cycle-lemma rotation using exact inequalities 3^q >= 2^j."""
    length = len(bits)
    for shift in range(length):
        q = 0
        good = True
        for j in range(1, length + 1):
            q += bits[(shift + j - 1) % length]
            if 3**q < 2**j:
                good = False
                break
        if good:
            return True
    return False


def verify_rotation_exhaustively(max_length: int) -> int:
    checked = 0
    for length in range(1, max_length + 1):
        for mask in range(1 << length):
            bits = tuple((mask >> i) & 1 for i in range(length))
            q = sum(bits)
            if 3**q > 2**length:
                checked += 1
                if not has_good_rotation(bits):
                    raise AssertionError(
                        f"rotation lemma failed at L={length}, mask={mask}, q={q}"
                    )
    return checked


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--max-rotation-length", type=int, default=15)
    args = parser.parse_args()

    alpha = math.log(2.0) / math.log(3.0)
    eta = -alpha * math.log2(alpha) - (1.0 - alpha) * math.log2(1.0 - alpha)
    rho = 0.5 * math.log2(3.0)

    # Exact closure inequality: (93/100)*2^(1/10) < 1 iff 2*93^10 < 100^10.
    closure_lhs = 2 * 93**10
    closure_rhs = 100**10
    if not closure_lhs < closure_rhs:
        raise AssertionError("exact 0.900 closure inequality failed")

    lengths = [8, 16, 32, 64, 96, 128]
    word_rows = []
    for length in lengths:
        count = all_supercritical_count(length)
        entropy_upper = (length + 1) * 2.0 ** (eta * length)
        if count > entropy_upper * (1.0 + 1e-12):
            raise AssertionError(f"entropy upper bound failed at L={length}")
        word_rows.append(
            {
                "length": length,
                "exact_prefix_supercritical_words": count,
                "log2_count_over_length": math.log2(count) / length,
                "entropy_upper": entropy_upper,
            }
        )

    rotation_cases = verify_rotation_exhaustively(args.max_rotation_length)

    result = {
        "status": "checks_passed",
        "scope": "finite interfaces only; contraction (C) remains unproved",
        "constants": {
            "alpha_log2_over_log3": alpha,
            "binary_entropy_eta": eta,
            "rho_log2_sqrt3": rho,
            "theta_93_over_100_decay_exponent": -math.log2(0.93),
            "theta_93_over_100_times_2_pow_1_over_10": 0.93 * 2.0**0.1,
        },
        "exact_closure_check": {
            "inequality": "2*93^10 < 100^10",
            "lhs": closure_lhs,
            "rhs": closure_rhs,
            "margin": closure_rhs - closure_lhs,
        },
        "word_counts": word_rows,
        "rotation_cases_checked": rotation_cases,
        "max_rotation_length": args.max_rotation_length,
    }

    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
