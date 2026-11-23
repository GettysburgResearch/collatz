#!/usr/bin/env python3
"""Exact all-certificate source optimization at one original target.

The mathematical last-exit reduction is in FiniteSourceBoundary.lean.
This executable searches the complete finite ordinary graph below B=(t-1)/2;
it does not bound a supplied word's length or exponents and does not decide
convergence of t.  The finite graph and algorithmic interpretation are written
mathematics, not asserted to be part of the Lean theorem count.
"""

from __future__ import annotations

import argparse
from collections import deque
import hashlib
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def v2(n: int) -> int:
    require(n > 0, "valuation requires a positive input")
    return (n & -n).bit_length() - 1


def predecessors(n: int) -> tuple[int, ...]:
    odd_numerator = 2 * n - 1
    if odd_numerator % 3 == 0:
        return 2 * n, odd_numerator // 3
    return (2 * n,)


def retained_graph(floor: int) -> dict[int, int]:
    """First-hitting clocks for every source reaching 1 entirely below B."""
    require(floor > 2, "the terminal 1,2 cycle must lie below the floor")
    distance = {1: 0}
    frontier = deque([1])
    while frontier:
        n = frontier.popleft()
        for parent in predecessors(n):
            if 0 < parent < floor and parent not in distance:
                distance[parent] = distance[n] + 1
                frontier.append(parent)
    return distance


def check_graph(floor: int, distance: dict[int, int]) -> None:
    """Distance labels prove soundness; inverse closure proves completeness."""
    require(distance.get(1) == 0, "missing terminal root")
    for n, clock in distance.items():
        require(0 < n < floor, "graph vertex outside the retained interval")
        require(isinstance(clock, int) and clock >= 0, "invalid clock label")
        if n != 1:
            require(clock > 0, "nonterminal zero clock")
            require(distance.get(shortcut(n)) == clock - 1,
                    "distance does not follow the ordinary map")
        for parent in predecessors(n):
            if 0 < parent < floor:
                require(parent in distance, "inverse closure is incomplete")


def first_hit_certificate(source: int, distance: dict[int, int]) -> dict:
    e = v2(source)
    odd = source >> e
    q = odd
    gaps: list[int] = []
    while q != 1:
        require(q in distance, "odd source is outside the retained graph")
        a = v2(3 * q + 1)
        next_q = (3 * q + 1) >> a
        require(distance[next_q] == distance[q] - a,
                "gap does not consume the actual first-hit clock")
        gaps.append(a)
        q = next_q
    grade = sorted(([2 * e + 1] if e else []) + [2 * a for a in gaps],
                   reverse=True)
    correction = 0
    depth = 0
    for a in reversed(gaps):
        correction = 3 ** depth + (1 << a) * correction
        depth += 1
    require(3 ** len(gaps) * odd + correction == 1 << sum(gaps),
            "complete arithmetic identity failed")
    return {"source": source, "initial_even": e, "odd_source": odd,
            "gaps": gaps, "grade_descending": grade,
            "ordinary_first_hit_clock": e + sum(gaps)}


def optimize(target: int) -> dict:
    require(target >= 7 and target % 2 == 1, "target must be odd and at least 7")
    floor = (target - 1) // 2
    distance = retained_graph(floor)
    check_graph(floor, distance)
    boundary = sorted(2 * n for n in distance if floor <= 2 * n)
    require(bool(boundary), "dyadic boundary source is missing")
    candidates = [first_hit_certificate(n, distance) for n in boundary]
    minimum_grade = min(tuple(c["grade_descending"]) for c in candidates)
    minimizers = [c for c in candidates
                  if tuple(c["grade_descending"]) == minimum_grade]
    selected = max(minimizers, key=lambda c: c["source"])
    graph_bytes = json.dumps(sorted(distance.items()), separators=(",", ":")).encode()
    return {
        "target": target,
        "floor": floor,
        "scope": "minimum over all complete capturing certificates; no target convergence claim",
        "retained_vertices": len(distance),
        "retained_max_first_hit_clock": max(distance.values()),
        "boundary_sources": len(boundary),
        "same_minimum_grade_sources": sorted(c["source"] for c in minimizers),
        "selected": selected,
        "graph_sha256": hashlib.sha256(graph_bytes).hexdigest(),
        "graph_sound_and_inverse_closed": True,
        "all_first_hit_identities_checked": len(candidates),
    }


def controls() -> dict:
    """Reject damaged soundness/completeness evidence, also under python -O."""
    floor = 1023
    original = retained_graph(floor)
    damaged: list[tuple[str, dict[int, int]]] = []
    without_two = dict(original)
    del without_two[2]
    damaged.append(("missing legal predecessor", without_two))
    wrong_clock = dict(original)
    wrong_clock[2] += 1
    damaged.append(("false first-hit clock", wrong_clock))
    false_vertex = dict(original)
    false_vertex[floor] = 1
    damaged.append(("vertex outside floor", false_vertex))
    rejected = []
    for label, candidate in damaged:
        try:
            check_graph(floor, candidate)
        except ValueError:
            rejected.append(label)
        else:
            raise RuntimeError(f"accepted damaged graph: {label}")
    return {"rejected": rejected, "count": len(rejected)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("targets", nargs="*", type=int, default=[2047, 3711])
    parser.add_argument("--controls", action="store_true")
    args = parser.parse_args()
    output = {"schema": "collatz-finite-source-boundary/v1",
              "normalization": "shortcut T; original target t=2B+1",
              "results": [optimize(target) for target in args.targets]}
    if args.controls:
        output["controls"] = controls()
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
