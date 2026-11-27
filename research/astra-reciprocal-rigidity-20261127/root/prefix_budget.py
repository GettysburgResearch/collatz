#!/usr/bin/env python3
"""Exact finite source budgets consumed by RampShadow.prepaid_ramp.

Every row uses a finite set of ordinary integer starts and an exact integer
power inequality. No convergence assertion outside that finite set is used.
The separate Lean theorem, not this computation, proves the unbounded-clock
consequence. All checks remain active under python -O.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def compute(max_b: int) -> dict:
    if not 0 <= max_b <= 36:
        raise ValueError("reproducibility budget: 0 <= max_b <= 36")
    caps = [(4 * 3**b - 1) // 2**b for b in range(max_b + 1)]
    # For a positive odd source, store the largest native prefix excess
    # 2*(odd departures) - (all departures), including every future clock.
    # The trivial 1 -> 2 -> 1 cycle has maximum excess 1.
    memo: dict[int, int] = {1: 1}
    rows, replays = [], {}
    largest, attaining, checked, next_b = 0, 1, 0, 0

    def finish(b: int) -> None:
        K = b
        while 4**(K + 1 - b) * 2**b < 3**(K + 1 - b) * 2**(largest + 1) * 3**b:
            K += 1
        rows.append({
            "extra_odd_budget": b,
            "largest_source_in_cap": caps[b],
            "odd_sources_checked": checked,
            "maximum_prefix_excess": largest,
            "attaining_source": attaining,
            "all_K_at_least": K,
            "threshold_left": str(3**(K + 1 - b) * 2**(largest + 1) * 3**b),
            "threshold_right": str(4**(K + 1 - b) * 2**b),
        })

    for n in range(1, caps[-1] + 1, 2):
        while next_b <= max_b and caps[next_b] < n:
            finish(next_b)
            next_b += 1
        path, seen, x = [], set(), n
        while x not in memo:
            if x in seen:
                raise ArithmeticError(f"nontrivial positive cycle from {n}")
            seen.add(x)
            y = 3*x + 1
            e = (y & -y).bit_length() - 1
            path.append((x, e))
            x = y >> e
        bound = memo[x]
        for x, e in reversed(path):
            bound = max(1, 2-e+bound)
            memo[x] = bound
        if memo[n] > largest:
            largest, attaining = memo[n], n
        checked += 1
    while next_b <= max_b:
        finish(next_b)
        next_b += 1

    for n in sorted({row["attaining_source"] for row in rows}):
        x, steps, odds, excess, max_at = n, 0, 0, 0, 0
        path = [n]
        while x != 1:
            odd = x & 1
            x = (3*x+1)//2 if odd else x//2
            steps += 1
            odds += odd
            path.append(x)
            if 2*odds-steps > excess:
                excess, max_at = 2*odds-steps, steps
        # Include the first future odd step of the trivial cycle.
        if 2*odds-steps+1 > excess:
            excess, max_at = 2*odds-steps+1, steps+1
        if excess != memo[n]:
            raise ArithmeticError("native and accelerated prefix maxima disagree")
        replays[str(n)] = {"maximum_prefix_excess": excess,
                           "maximum_at_native_clock": max_at,
                           "first_hit_1_clock": steps,
                           "native_path_to_1": path}

    return {
        "schema": "collatz-prefix-clock-budgets/v2",
        "status": "EXACT FINITE CONTROL; global consumers retain explicit premises",
        "map": "T(x)=x/2 if even, (3x+1)/2 if odd",
        "source_domain": "positive integers q with 2^b*q < 4*3^b",
        "max_extra_odd_budget": max_b,
        "largest_source": caps[-1],
        "distinct_odd_states_memoized": len(memo),
        "rows": rows,
        "independent_native_replays": replays,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-b", type=int, default=34)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    result = compute(args.max_b)
    if args.check is not None and json.loads(args.check.read_text()) != result:
        raise SystemExit("control artifact differs from complete regeneration")
    if args.output is not None:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"largest_source": result["largest_source"],
                      "memoized": result["distinct_odd_states_memoized"],
                      "rows": [{k: row[k] for k in ("extra_odd_budget", "maximum_prefix_excess", "attaining_source", "all_K_at_least")} for row in result["rows"]]}, sort_keys=True))


if __name__ == "__main__":
    main()
