#!/usr/bin/env python3
"""Exact, bounded replay for SIGNED_TARGET_ARITHMETIC.md.

This checks finite claims and examples. The infinite quantified statements
are proved in the accompanying note; no search cutoff represents a proof.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def require(condition: bool, explanation: str) -> None:
    if not condition:
        raise AssertionError(explanation)


def t(x: int) -> int:
    require(x > 0, "T requires a positive integer")
    return (3 * x + 1) // 2 if x & 1 else x // 2


def s(x: int) -> int:
    require(x > 0, "S requires a positive integer")
    return (3 * x - 1) // 2 if x & 1 else x // 2


def iterate(function, x: int, length: int) -> tuple[int, int]:
    odd = 0
    for _ in range(length):
        odd += x & 1
        x = function(x)
    return x, odd


def inverse_s(states: set[tuple[int, int]], *, first_hit: bool) -> set[tuple[int, int]]:
    result = set()
    for x, q in states:
        result.add((2 * x, q))
        if (2 * x + 1) % 3 == 0:
            predecessor = (2 * x + 1) // 3
            require(predecessor & 1 == 1, "integral odd inverse has wrong parity")
            if not first_hit or predecessor != 5:
                result.add((predecessor, q + 1))
    if first_hit:
        result = {(x, q) for x, q in result if x != 5}
    return result


def terminal_set(k: int) -> tuple[set[int], set[tuple[int, int]]]:
    states = {(5, 0)}
    for _ in range(3 * k):
        states = inverse_s(states, first_hit=False)
    values = set()
    for u, q in states:
        require(q <= 2 * k, "signed odd count exceeds checkpoint bound")
        require(iterate(s, u, 3 * k) == (5, q), "inverse enumeration is not legal")
        target = 5 * 3 ** (2 * k - q) - u
        require(target >= 0, "signed terminal target is negative")
        if target:
            values.add(target)
    return values, states


def first_hit_data(magnitude: int, cap: int) -> tuple[int, int] | None:
    x, h = magnitude, 0
    for length in range(cap + 1):
        if x == 5:
            return length, h
        h += x & 1
        x = s(x)
    return None


def hitting_time_one(x: int, cap: int = 1000) -> int:
    for length in range(cap + 1):
        if x == 1:
            return length
        x = t(x)
    raise AssertionError("finite positive target did not hit 1 within the replay cap")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON report path; default is standard output only.")
    args = parser.parse_args()
    require(169**32 > 3 * 162**32, "theta^64 > 3 failed")
    require(5 * 169**32 < 2**64 * 162**32, "theta*5^(1/64) < 2 failed")
    require(4 * 3 + 160 < 64 * 3, "logarithmic-error constant failed")

    terminal_sets = {}
    terminal_report = []
    previous = set()
    for k in range(1, 7):
        values, states = terminal_set(k)
        terminal_sets[k] = values
        require(previous <= values, "terminal sets are not nested")
        require(max(values) == 5 * (9**k - 8**k), "terminal maximum is incorrect")
        terminal_report.append({
            "k": k,
            "signed_inverse_states": len(states),
            "positive_targets": len(values),
            "maximum": max(values),
        })
        previous = values

    require(terminal_sets[1] == {1, 5}, "F_1 was not fully recovered")
    expected_f2 = {1, 2, 5, 7, 23, 27, 28, 85}
    require(terminal_sets[2] == expected_f2, "F_2 was not fully recovered")
    times = {x: hitting_time_one(x) for x in sorted(expected_f2)}
    require(list(times.values()) == [0, 1, 4, 11, 11, 70, 13, 8], "hitting-time table mismatch")

    states = {(5, 0)}
    replays = 0
    dyadic_replays = 0
    strict_descents = 0
    endpoint_cases = set()
    count_by_h = {}
    for length in range(1, 31):
        states = inverse_s(states, first_hit=True)
        for magnitude, h in sorted(states):
            if not h or h & 1 or h > 12:
                continue
            b = length - 3 * (h // 2)
            if b < 0:
                continue
            c = 5 * 2**b - magnitude
            if c <= 0:
                continue
            require(first_hit_data(magnitude, length) == (length, h), "first-hit label is false")
            u, r = iterate(s, magnitude, b)
            endpoint, ordinary_r = iterate(t, c, b)
            q = h - r
            require(ordinary_r == r, "shared binary prefix changed its odd count")
            require(iterate(s, u, 3 * (h // 2)) == (5, q), "signed suffix has wrong terminal data")
            require(endpoint == 5 * 3**r - u, "exact shared-prefix identity failed")
            require(endpoint in terminal_sets[h // 2], "ordinary endpoint is outside its finite target set")
            bound = 5 * (9 ** (h // 2) - 8 ** (h // 2))
            require(1 <= endpoint <= bound, "ordinary endpoint height bound failed")
            if c > bound:
                require(endpoint < c, "claimed strict descent failed")
                strict_descents += 1
            require(first_hit_data(2 * magnitude, length + 1) == (length + 1, h), "dyadic enlargement changed first-hit data")
            require(5 * 2 ** (b + 1) - 2 * magnitude == 2 * c, "dyadic enlargement changed target")
            dyadic_replays += 1
            if c % 2 == 0:
                require(b >= 1 and magnitude % 2 == 0, "dyadic reduction parity failed")
                require(first_hit_data(magnitude // 2, length - 1) == (length - 1, h), "dyadic reduction changed first-hit data")
                require(5 * 2 ** (b - 1) - magnitude // 2 == c // 2, "dyadic reduction changed target")
                dyadic_replays += 1
            if h <= 4:
                require(hitting_time_one(endpoint) <= (4 if h == 2 else 70), "small-complexity convergence certificate failed")
            endpoint_cases.add((h, endpoint))
            count_by_h[h] = count_by_h.get(h, 0) + 1
            replays += 1

    require(first_hit_data(143, 8) == (8, 2), "explicit signed example failed")
    require(iterate(t, 17, 5)[0] == 5, "explicit ordinary example failed")
    require(replays > 100, "replay population unexpectedly small")
    report = {
        "source_head": "561d48a4d3a793a59b1cdf0406062ae1a6d47515",
        "scope": "Finite exact replay; no extrapolation to all signed complexities or escaping orbits.",
        "terminal_sets": terminal_report,
        "small_terminal_hitting_times": times,
        "signed_first_hit_replays": replays,
        "dyadic_replays": dyadic_replays,
        "strict_descents": strict_descents,
        "distinct_h_endpoint_pairs": len(endpoint_cases),
        "replays_by_signed_odd_count": count_by_h,
        "exact_constant_inequalities": 3,
        "passed": True,
    }
    report_text = json.dumps(report, indent=2)
    if args.output is not None:
        args.output.write_text(report_text + "\n")
    print(report_text)


if __name__ == "__main__":
    main()
