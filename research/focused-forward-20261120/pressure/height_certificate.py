#!/usr/bin/env python3
"""Exact all-word root-potential computation by a finite ordinary height cutoff."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess


def integer_fifth_root(n: int) -> int:
    if n < 0:
        raise ValueError("nonnegative radicand required")
    lo, hi = 0, 1 << ((n.bit_length() + 4) // 5)
    while lo < hi:
        middle = (lo + hi + 1) // 2
        if middle**5 <= n:
            lo = middle
        else:
            hi = middle - 1
    if not lo**5 <= n < (lo + 1)**5:
        raise ValueError("integer fifth-root postcondition failed")
    return lo


def height_cutoff(horizon: int) -> int:
    if horizon < 0:
        raise ValueError("nonnegative horizon required")
    numerator = 256**horizon
    denominator = 2 * 243**horizon
    cutoff = integer_fifth_root((numerator - 1) // denominator)
    if not denominator * cutoff**5 < numerator <= denominator * (cutoff + 1)**5:
        raise ValueError("strict height cutoff postcondition failed")
    return cutoff


def replay_python(cutoff: int, horizon: int) -> dict:
    """Independent direct, uncached, arbitrary-integer forward replay."""
    maximum = 0
    best_source = 1
    hit = 0
    no_hit = 0
    nonroot_score = None
    nonroot_source = 0
    for start in range(1, cutoff + 1, 2):
        if start % 3 == 0:
            continue
        n, depth, total = start, 0, 0
        while n != 1 and depth < horizon:
            y = 3 * n + 1
            exponent = (y & -y).bit_length() - 1
            n = y >> exponent
            total += exponent
            depth += 1
        if n != 1:
            no_hit += 1
            continue
        hit += 1
        score = 8 * depth - 5 * total
        if score > maximum:
            maximum, best_source = score, start
        if start != 1 and (nonroot_score is None or score > nonroot_score):
            nonroot_score, nonroot_source = score, start
    return {
        "candidate_odd_units": hit + no_hit,
        "first_hit_within_horizon": hit,
        "no_first_hit_within_horizon": no_hit,
        "maximum_score_with_zero": maximum,
        "maximum_score_source": best_source,
        "maximum_nonroot_score": nonroot_score,
        "maximum_nonroot_score_source": nonroot_source,
    }


def inverse_dfs(horizon: int) -> tuple[int, int]:
    """Independent finite inverse search, without a height reduction."""
    maximum, visits = 0, 0
    stack = [(1, 0, 0)]
    while stack:
        n, depth, score = stack.pop()
        visits += 1
        maximum = max(maximum, score)
        if depth == horizon:
            continue
        remaining = horizon - depth - 1
        largest_gap = (score + 8 + 3 * remaining - maximum - 1) // 5
        for exponent in range(1, largest_gap + 1):
            numerator = (n << exponent) - 1
            if numerator % 3:
                continue
            child = numerator // 3
            if child % 3 == 0:
                continue
            if n == 1 and exponent == 2:
                continue  # Removing the root self-loop improves the score by 2.
            stack.append((child, depth + 1, score + 8 - 5 * exponent))
    return maximum, visits


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--horizon", type=int, default=1500)
    parser.add_argument("--executable", type=Path)
    parser.add_argument("--python", action="store_true", help="use the independent uncached Python replay")
    parser.add_argument("--controls", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cutoff = height_cutoff(args.horizon)
    if args.python:
        result = replay_python(cutoff, args.horizon)
    else:
        if args.executable is None:
            parser.error("supply --executable or --python")
        run = subprocess.run(
            [str(args.executable.resolve()), str(cutoff), str(args.horizon)],
            check=True, capture_output=True, text=True,
        )
        result = json.loads(run.stdout)
        if result["cutoff"] != cutoff or result["horizon"] != args.horizon:
            raise ValueError("replay parameters changed")
        result["executable_sha256"] = sha256(args.executable)
    result.update({
        "horizon": args.horizon,
        "exact_height_cutoff": cutoff,
        "potential_at_one": result["maximum_score_with_zero"],
        "scope": "Exact W_N(1) for the reported finite horizon; no conclusion about W(1), escaping orbits, or Collatz",
        "cutoff_formula": "floor_fifth_root(floor((256^N-1)/(2*243^N)))",
    })
    if args.controls:
        controls = []
        for horizon in (0, 1, 10, 20, 30, 40):
            direct = replay_python(height_cutoff(horizon), horizon)
            inverse, visits = inverse_dfs(horizon)
            if direct["maximum_score_with_zero"] != inverse:
                raise ValueError("independent forward/inverse disagreement")
            controls.append({"horizon": horizon, "inverse_nodes": visits, "potential": inverse})
        result["independent_inverse_controls"] = controls
        # Exact first-hit examples distinguish the odd clock and division clock.
        control = replay_python(27, 1000)
        if control["maximum_nonroot_score"] != -12 or control["maximum_nonroot_score_source"] != 5:
            raise ValueError("first-hit normalization control failed")
        if not 3**5 < 2**8:
            raise ValueError("growth ratio sign failed")
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
