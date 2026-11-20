#!/usr/bin/env python3
"""Bounded exact replay for STOPPING_BURDEN.md; never certifies W(1)."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def shortcut_first_hit(n: int, cap: int = 10000) -> tuple[int, int, list[int]]:
    x, d, a, inputs = n, 0, 0, []
    while x != 1 and d < cap:
        if x & 1:
            inputs.append(x)
            a += 1
            x = (3 * x + 1) // 2
        else:
            x //= 2
        d += 1
    require(x == 1, f"Unfinished sample at {n}; cap {cap}")
    return d, a, inputs


def odd_first_hit(n: int) -> tuple[int, int]:
    x, d, a = n, 0, 0
    seen: set[int] = set()
    while x != 1:
        require(x not in seen, f"Repeated odd value at {n}")
        seen.add(x)
        z = 3 * x + 1
        g = (z & -z).bit_length() - 1
        d += g
        a += 1
        x = z >> g
    return d, a


def exceeds(n: int, bound: int, a: int) -> bool:
    require(isinstance(n, int) and n >= 1, "Positive integer source required")
    require(isinstance(bound, int) and bound >= 0, "Nonnegative integer bound required")
    require(isinstance(a, int) and a >= 0, "Nonnegative integer clock required")
    return (1 << (72 * a)) > (1 << (9 * bound)) * 3 ** (45 * a) * n**45 * (3 * a + 1) ** 5


def deadline(n: int, bound: int) -> int:
    require(isinstance(n, int) and n >= 1, "Positive integer source required")
    require(isinstance(bound, int) and bound >= 0, "Nonnegative integer bound required")
    lo, hi = 9, 10
    while not exceeds(n, bound, hi):
        lo, hi = hi, 2 * hi
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if exceeds(n, bound, mid):
            hi = mid
        else:
            lo = mid
    require(exceeds(n, bound, hi), "Deadline does not cross")
    require(hi == 10 or not exceeds(n, bound, hi - 1), "Deadline is not first")
    return hi


def inverse_checks(depth: int = 7, cap: int = 10) -> int:
    frontier = [(1, 0)]
    count = 0
    for k in range(1, depth + 1):
        new = []
        for target, cost in frontier:
            for g in range(1, cap + 1):
                value = (target << g) - 1
                if value % 3:
                    continue
                source = value // 3
                if not source or source % 3 == 0:
                    continue
                d, a = odd_first_hit(source)
                r = k - a
                require(r >= 0, "Inverse source needs more first-hit edges")
                require(cost + g == d + 2 * r, "Inverse first-hit clock identity")
                require(8 * k - 5 * (cost + g) == 8 * a - 5 * d - 2 * r, "Score identity")
                new.append((source, cost + g))
                count += 1
        frontier = new
    return count


def run(limit: int) -> dict:
    require((1 << 8) > 3**5, "Critical rational gap")
    require((1 << 72) * 31**5 > 3**45 * 34**5, "Deadline monotonicity threshold")
    population = 0
    products = 0
    deadlines = 0
    maximum_score = 0
    maximum_odd_count = 0
    deadline_examples = []
    for n in range(1, limit + 1, 2):
        if n % 3 == 0:
            continue
        d, a, odd_inputs = shortcut_first_hit(n)
        require((d, a) == odd_first_hit(n), "Independent clock disagreement")
        require(len(set(odd_inputs)) == a, "First-hit repetition")
        require(all(u > 1 and u % 3 for u in odd_inputs), "First-hit unit domain")
        require(all(u >= 3 * i + 1 for i, u in enumerate(sorted(odd_inputs), 1)), "Sorted unit floor")
        require((1 << (9 * d)) <= 3 ** (9 * a) * n**9 * (3 * a + 1), "Distortion bound")
        score = 8 * a - 5 * d
        maximum_score = max(maximum_score, score)
        maximum_odd_count = max(maximum_odd_count, a)
        population += 1
        if n <= 769:
            product = Fraction(1)
            for u in odd_inputs:
                product *= Fraction(3 * u + 1, 3 * u)
            require(product == Fraction(1 << d, 3**a * n), "Direct product identity")
            require(1 <= product**9 <= 3 * a + 1, "Direct rational distortion")
            products += 1
        if n <= 601:
            # This is a path-specific bound, not a claim about the supremum W(1).
            local_bound = max(0, score)
            cut = deadline(n, local_bound)
            require(a < cut, "Conditional deadline fails on a qualifying path")
            deadlines += 1
            if n in (1, 5, 7, 31, 97, 601):
                deadline_examples.append({"n": n, "path_score": score, "assumed_bound": local_bound, "odd_first_hit": a, "deadline": cut})
    inverse_words = inverse_checks()
    return {
        "status": "PASS",
        "scope": "Bounded exact arithmetic; no bound on W(1) is certified.",
        "integer_limit": limit,
        "positive_odd_unit_sources": population,
        "independent_clock_comparisons": population,
        "exact_distortion_checks": population,
        "direct_rational_product_checks": products,
        "inverse_words_depth_at_most_7_gap_at_most_10": inverse_words,
        "conditional_deadline_checks": deadlines,
        "maximum_observed_first_hit_score": maximum_score,
        "maximum_observed_odd_first_hit": maximum_odd_count,
        "deadline_examples": deadline_examples,
        "unresolved": "Neither all-source W(1) finiteness nor universal convergence is tested or established.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=30000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    require(args.limit >= 1, "Positive limit required")
    report = run(args.limit)
    data = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(data, encoding="utf-8")
    print(data, end="")


if __name__ == "__main__":
    main()
