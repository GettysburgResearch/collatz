#!/usr/bin/env python3
"""Independent bounded audit of the memoized first-hit implementation."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess


def reference(cutoff: int, horizon: int) -> dict:
    """Direct arbitrary-integer trajectories; no imported implementation."""
    scores: list[tuple[int, int, int, int]] = []
    missed = 0
    candidates = [n for n in range(1, cutoff + 1) if n % 2 and n % 3]
    for initial in candidates:
        value = initial
        depth = 0
        total = 0
        while value != 1 and depth < horizon:
            value = 3 * value + 1
            gap = 0
            while value % 2 == 0:
                gap += 1
                value //= 2
            total += gap
            depth += 1
        if value == 1:
            scores.append((initial, 8 * depth - 5 * total, depth, total))
        else:
            missed += 1
    best_score, best_source = 0, 1
    for initial, score, _, _ in scores:
        if score > best_score:
            best_score, best_source = score, initial
    nonroots = [(initial, score) for initial, score, _, _ in scores if initial != 1]
    nonroot_score = max((score for _, score in nonroots), default=None)
    nonroot_source = next((initial for initial, score in nonroots if score == nonroot_score), 0)
    return {
        "candidate_odd_units": len(candidates),
        "first_hit_within_horizon": len(scores),
        "no_first_hit_within_horizon": missed,
        "maximum_first_hit_depth": max((depth for _, _, depth, _ in scores), default=0),
        "maximum_first_hit_total_exponent": max((total for _, _, _, total in scores), default=0),
        "maximum_score_with_zero": best_score,
        "maximum_score_source": best_source,
        "maximum_nonroot_score": nonroot_score,
        "maximum_nonroot_score_source": nonroot_source,
    }


def check(executable: Path) -> dict:
    cases = 0
    candidates = 0
    for cutoff in (0, 1, 5, 27, 101, 1001):
        for horizon in (0, 1, 2, 3, 5, 10, 50, 100, 2000):
            wanted = reference(cutoff, horizon)
            run = subprocess.run(
                [str(executable.resolve()), str(cutoff), str(horizon)],
                capture_output=True, text=True, check=True,
            )
            got = json.loads(run.stdout)
            if any(got[key] != value for key, value in wanted.items()):
                raise ValueError(f"bounded first-hit mismatch at cutoff={cutoff}, horizon={horizon}")
            cases += 1
            candidates += wanted["candidate_odd_units"]

    # Reconstruct the inverse exponent-one word and the two bounded-ratio
    # comparisons used in O1-local without floating-point logarithms.
    local_pairs = 0
    inverse_letters = 0
    for k in range(2, 202, 2):
        source = 2 * 3**k - 1
        current = source
        for _ in range(k):
            numerator = 2 * current - 1
            if numerator % 3:
                raise ValueError("nonintegral inverse-one letter")
            current = numerator // 3
            if current <= 0 or current % 2 == 0 or current % 3 == 0:
                raise ValueError("inverse-one unit guard failed")
            inverse_letters += 1
        if current != 2**(k + 1) - 1:
            raise ValueError("inverse-one endpoint identity failed")
        ell = 0
        while 3**(ell + 2) <= 2**k:
            ell += 2
        if ell >= 2:
            lower = 2 * 3**ell - 1
            if not lower <= current < 16 * lower:
                raise ValueError("lower local-ratio guard failed")
            local_pairs += 1
        exponent = 2
        previous = None
        while (2**exponent - 1) // 3 < source:
            previous = exponent
            exponent += 2
            if exponent % 6 == 0:
                exponent += 2
        upper = (2**exponent - 1) // 3
        if previous is None or exponent - previous not in (2, 4):
            raise ValueError("permitted exponent predecessor failed")
        if not source <= upper < 16 * source or upper % 3 == 0:
            raise ValueError("upper local-ratio guard failed")
        local_pairs += 1

    beta_lower = (3 * sum((Fraction(41, 65)**j for j in range(1, 13)), Fraction(0)) - 5) / 13
    if not 3**41 < 2**65 or not beta_lower > Fraction(1, 125):
        raise ValueError("exact all-scale oscillation coefficient guard failed")

    return {
        "status": "PASS",
        "independent_cpp_comparisons": cases,
        "ordinary_candidate_cases": candidates,
        "inverse_one_letters_replayed": inverse_letters,
        "local_oscillation_pairs_replayed": local_pairs,
        "all_scale_coefficient_rational_lower": str(beta_lower),
        "executable_sha256": hashlib.sha256(executable.read_bytes()).hexdigest(),
        "scope": "Bounded arithmetic and implementation audit; no infinite-depth or Collatz conclusion",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--executable", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(check(args.executable), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
