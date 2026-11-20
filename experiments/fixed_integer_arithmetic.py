#!/usr/bin/env python3
"""Exact finite cores for bounded binary one-run count in odd Collatz orbits.

This is a bounded certificate, not a decision procedure for unrestricted
Collatz.  The written proof is research/fixed-integer-descent/arithmetic.md.
No third-party packages, floating point, or stopping-time conjecture is used.
"""

from __future__ import annotations

import argparse
from collections import deque
import hashlib
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def runs(n: int) -> int:
    require(n >= 0, "run count is defined here only for nonnegative integers")
    return (n ^ (n << 1)).bit_count() // 2


def runs_reference(n: int) -> int:
    return bin(n)[2:].count("01") + (n > 0)


def odd_step(n: int) -> int:
    require(n > 0 and n & 1, "positive odd source required")
    z = 3 * n + 1
    return z // (z & -z)


def homogeneous_hit(u: int, delta: int, cap: int) -> int:
    require(u > 0 and u & 1 and delta in (0, 1), "invalid homogeneous source")
    j = 0
    z = u
    while runs(z - delta) <= cap:
        z *= 3
        j += 1
        require(j <= (1 << (2 * cap + 1)) - 1, "homogeneous theorem bound failed")
    return j


def core(cap: int):
    """Unique maximal-run parse, traversed from the most significant end."""
    require(cap >= 1, "positive cap required")

    def extend(prefix: int, bit: int, one_runs: int):
        if bit:
            h = homogeneous_hit(prefix + 1, 1, cap)
            limit = (3**h).bit_length() - 1
        else:
            h = homogeneous_hit(prefix, 0, cap)
            limit = 2 * h - 1
        for length in range(1, limit + 1):
            value = (prefix << length) + ((1 << length) - 1 if bit else 0)
            if bit:
                yield value
                if one_runs < cap:
                    yield from extend(value, 0, one_runs)
            else:
                yield from extend(value, 1, one_runs + 1)

    yield from extend(0, 1, 1)


def capped_replay(source: int, cap: int):
    """Direct replay from each source; no path memoization."""
    seen = set()
    n = source
    clock = 0
    while n != 1 and runs(n) <= cap:
        require(n not in seen, f"nontrivial capped cycle discovered at {n}")
        seen.add(n)
        n = odd_step(n)
        clock += 1
    return ("one" if n == 1 else "exit"), clock, n


def inverse_capped_basin(cap: int):
    """Separate complete inverse construction of the basin inside the cap."""
    basin = {1}
    queue = deque([1])
    edges = 0
    while queue:
        target = queue.popleft()
        if target % 3 == 0:
            continue
        exponent = 2 if target % 3 == 1 else 1
        source = ((1 << exponent) * target - 1) // 3
        while runs(source) <= cap:
            require(odd_step(source) == target, "inverse edge does not replay")
            edges += 1
            if source not in basin:
                basin.add(source)
                queue.append(source)
            next_source = 4 * source + 1
            require(runs(next_source) == runs(source) + 1, "inverse fan run increment failed")
            source = next_source
    return basin, edges


def signed_shadow_checks():
    checks = 0
    for upper in range(1, 32, 2):
        for lower in range(-31, 32, 2):
            for length in range(1, 13):
                source = (upper << length) + lower
                if source <= 0 or abs(lower) >= 1 << length:
                    continue
                v = lower
                accumulated = 0
                actual = source
                for j in range(9):
                    credit = (1 << accumulated) * abs(v)
                    if credit >= 1 << length:
                        break
                    require(accumulated < length, "strict cut lost its valuation reserve")
                    predicted = ((3**j * upper) << (length - accumulated)) + v
                    require(actual == predicted, "signed shadow identity failed")
                    comparison = 3**j * upper - (lower < 0)
                    require(runs(actual) >= runs(comparison), "run projection failed")
                    require(credit <= (4**j if lower > 0 else 3**j) * abs(lower),
                            "signed credit bound failed")
                    checks += 1
                    z = 3 * v + 1
                    power = abs(z) & -abs(z)
                    accumulated += power.bit_length() - 1
                    v = z // power
                    actual = odd_step(actual)
    # A guard equality is not a valid strict cut: 5 -> 1 has valuation 4.
    require(4 * 1 == 1 << 2 and odd_step(5) == 1, "strict-boundary control changed")
    # Boundaries concern *all* states in an orbit, not the initial run count.
    require(runs(3) == 1 and runs(odd_step(3)) == 2, "cap-exit control changed")
    return checks


def build_report(max_cap: int):
    for n in range(1 << 16):
        require(runs(n) == runs_reference(n), "independent binary-run definition differs")
    shadow_checks = signed_shadow_checks()
    rows = []
    for cap in range(1, max_cap + 1):
        digest = hashlib.sha256()
        successes = set()
        count = 0
        total_steps = 0
        max_clock = -1
        max_witness = 0
        max_value = 0
        max_bits = 0
        for source in core(cap):
            require(source & 1 and runs_reference(source) <= cap, "invalid core member")
            outcome, clock, endpoint = capped_replay(source, cap)
            count += 1
            total_steps += clock
            max_value = max(max_value, source)
            max_bits = max(max_bits, source.bit_length())
            if outcome == "one":
                successes.add(source)
            if clock > max_clock:
                max_clock, max_witness = clock, source
            digest.update(f"{source},{outcome},{clock},{endpoint}\n".encode("ascii"))
        backward, inverse_edges = inverse_capped_basin(cap)
        require(successes == backward, "complete forward and inverse basins differ")
        rows.append({
            "cap": cap,
            "core_sources": count,
            "reaches_one_inside_cap": len(successes),
            "exits_cap": count - len(successes),
            "nontrivial_cycles": 0,
            "max_core_bitlength": max_bits,
            "largest_core_source": str(max_value),
            "max_core_odd_clock": max_clock,
            "first_clock_witness_in_dfs_order": str(max_witness),
            "direct_replayed_odd_steps": total_steps,
            "independent_inverse_edges": inverse_edges,
            "largest_capped_basin_source": str(max(successes)),
            "canonical_dfs_replay_sha256": digest.hexdigest(),
            "unconditional_outside_core_clock_bound": (1 << (2 * cap + 1)) - 1,
        })
    return {
        "schema": "collatz-binary-runs-core-v1",
        "map": "U(n)=(3n+1)/2^v2(3n+1), positive odd n; stop at 1 or cap exit",
        "claim_scope": "bounded run-count orbits only; unrestricted Collatz remains open",
        "run_definition_crosschecks": 1 << 16,
        "signed_shadow_checks": shadow_checks,
        "core_rows": rows,
        "implementation": "literal per-source forward replay and separate inverse BFS; no memoized paths",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-cap", type=int, default=5)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compare", type=Path)
    args = parser.parse_args()
    require(1 <= args.max_cap <= 6, "this replay command supports caps 1 through 6")
    report = build_report(args.max_cap)
    if args.compare:
        require(report == json.loads(args.compare.read_text(encoding="utf-8")),
                "regenerated report differs from frozen report")
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        require(not args.output.exists(), "refusing to overwrite an existing evidence report")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
