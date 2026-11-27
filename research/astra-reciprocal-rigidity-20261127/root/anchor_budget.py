#!/usr/bin/env python3
"""Exact finite-to-infinite inverse-clock budget data at the ordinary anchor 1.

All orbit calculations are explicit finite integer calculations. This program
does not certify convergence outside its stated input range and does not prove
Collatz. The extrapolation is the separate theorem in ANCHOR_BUDGET.md.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def odd_step(n: int) -> tuple[int, int]:
    if n <= 0 or n % 2 != 1:
        raise ValueError("positive odd source required")
    z = 3*n + 1
    e = (z & -z).bit_length() - 1
    return z >> e, e


def compute(max_b: int) -> dict:
    if not 0 <= max_b <= 36:
        raise ValueError("explicit reproducibility budget is 0 <= b <= 36")
    maximum_source = (3**max_b - 1)//(2**max_b)
    # The pair is (first odd hit clock, total division exponent).
    memo: dict[int, tuple[int, int]] = {1: (0, 0)}
    maxima: list[dict] = []
    next_b = 1
    max_score = 0
    max_score_source = 1
    max_odd_clock = 0
    checked = 0
    sample_paths = {}

    def append_row(b: int) -> None:
        limit = (3**b - 1)//(2**b)
        k = max(1, (max_score + 1)//2)
        while 2**(2*k-max_score+b) < 3**(k+b):
            k += 1
        if 2*k < max_score:
            raise ArithmeticError("negative natural exponent")
        numerator = 2**(2*k-max_score+b)
        denominator = 3**(k+b)
        if numerator < denominator:
            raise ArithmeticError("budget threshold not certified")
        if k > max(1, (max_score+1)//2):
            if 2**(2*(k-1)-max_score+b) >= 3**(k-1+b):
                raise ArithmeticError("threshold is not the first supported one")
        maxima.append({
            "extra_odd_budget": b,
            "exclusive_source_cap": f"3^{b}/2^{b}",
            "largest_source_in_cap": limit,
            "odd_sources_checked": checked,
            "maximum_score_2p_minus_E": max_score,
            "attaining_source": max_score_source,
            "attaining_first_hit": list(memo[max_score_source]),
            "maximum_first_odd_clock": max_odd_clock,
            "all_K_at_least": k,
            "threshold_left": str(numerator),
            "threshold_right": str(denominator),
        })

    for n in range(1, maximum_source+1, 2):
        # Finish earlier source caps before admitting this source.
        while next_b <= max_b and (3**next_b-1)//(2**next_b) < n:
            append_row(next_b)
            next_b += 1
        chain: list[tuple[int, int]] = []
        seen: set[int] = set()
        x = n
        while x not in memo:
            if x in seen:
                raise ArithmeticError(f"nontrivial positive odd cycle from {n}")
            seen.add(x)
            y, e = odd_step(x)
            chain.append((x, e))
            x = y
        p, total = memo[x]
        for x, e in reversed(chain):
            p += 1
            total += e
            memo[x] = (p, total)
        p, total = memo[n]
        score = 2*p-total
        if score > max_score:
            max_score = score
            max_score_source = n
        max_odd_clock = max(max_odd_clock, p)
        checked += 1

    while next_b <= max_b:
        append_row(next_b)
        next_b += 1

    # Independent direct replay of every extremizing source, without memo.
    for n in sorted({row["attaining_source"] for row in maxima}):
        states, exponents = [n], []
        x = n
        while x != 1:
            x, e = odd_step(x)
            states.append(x)
            exponents.append(e)
        if (len(exponents), sum(exponents)) != memo[n]:
            raise ArithmeticError("direct and memoized clocks disagree")
        sample_paths[str(n)] = {"states": states, "exponents": exponents}

    return {
        "schema": "collatz-anchor-clock-budgets/v1",
        "status": "EXACT FINITE CONTROL; global consumers retain explicit premises",
        "map": "U(n)=(3n+1)/2^v2(3n+1), positive odd n",
        "max_extra_odd_budget": max_b,
        "largest_source": maximum_source,
        "distinct_odd_states_memoized": len(memo),
        "rows": maxima,
        "independent_extremizer_replays": sample_paths,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-b", type=int, default=34)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    result = compute(args.max_b)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.check is not None:
        if json.loads(args.check.read_text()) != result:
            raise SystemExit("control artifact differs from complete regeneration")
    if args.output is not None:
        args.output.write_text(encoded)
    print(json.dumps({"rows": result["rows"],
                      "largest_source": result["largest_source"],
                      "memoized": result["distinct_odd_states_memoized"]},
                     sort_keys=True))


if __name__ == "__main__":
    main()
