#!/usr/bin/env python3
"""Exact integer replay of the translated-interval bootstrap in FID-DRIFT-005.

The full recursive minimum is computed through width 4096. Larger widths
use a separately labeled three-level policy, which is a valid upper bound
but is not advertised as the full recursive minimum.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import json
from math import comb
from pathlib import Path


def require(value: bool, message: str) -> None:
    if not value:
        raise ValueError(message)


def image_width(width: int, clock: int, odds: int) -> int:
    return (3**odds * (width + (1 << (clock - odds))) - 1) // (1 << clock)


def candidates(width: int):
    for clock in range(1, width.bit_length() + 1):
        residues = 1 << clock
        high_words = residues
        children = []
        for odds in range(clock + 1):
            child = image_width(width, clock, odds)
            if child >= width:
                break
            children.append(child)
            high_words -= comb(clock, odds)
            terminal_and_high = clock + ((width + residues - 1) // residues) * high_words
            yield clock, odds, terminal_and_high, tuple(children)


def complete_table(limit: int):
    table = [0]
    choices = [None]
    inspected = 0
    for width in range(1, limit + 1):
        best = width
        choice = None
        for clock, odds, external, children in candidates(width):
            require(all(0 <= child < width for child in children), "nondecreasing recursion")
            value = external + sum(table[child] for child in children)
            inspected += 1
            if value < best:
                best = value
                choice = (clock, odds)
        require(1 <= best <= width, "invalid universal occupancy upper bound")
        table.append(best)
        choices.append(choice)
    return table, choices, inspected


def simple_path(n: int):
    path = []
    seen = set()
    while n not in seen:
        seen.add(n)
        path.append(n)
        if n == 1:
            break
        n = (3 * n + 1) // 2 if n & 1 else n // 2
    return path


def build_report():
    # Exact witnesses for theta=200/317 and alpha=19/20.
    require(3**200 < 2**317, "multiplicative contraction certificate failed")
    require(317**6340 < 2**6023 * 200**4000 * 117**2340,
            "entropy exponent certificate failed")
    table, choices, inspected = complete_table(4096)
    encoded = ",".join(map(str, table)).encode("ascii")

    @lru_cache(None)
    def policy(width: int, depth: int):
        if width < len(table):
            return table[width]
        if depth == 0:
            return width
        best_base = width
        selected = None
        for clock, odds, external, children in candidates(width):
            base = external + sum(children)
            if base < best_base:
                best_base = base
                selected = (clock, odds, external, children)
        if selected is None:
            return width
        _, _, external, children = selected
        bound = external + sum(policy(child, depth - 1) for child in children)
        require(bound <= best_base <= width, "recursive policy lost its bound")
        return bound

    windows = 0
    states = 0
    widths = (16, 32, 64, 128, 256, 512, 1024, 2048, 4096)
    for source in range(1, 2049):
        path = simple_path(source)
        require(len(path) == len(set(path)), "path is not simple")
        states += len(path)
        for width in widths:
            for left in (1, max(1, source - width // 2), max(1, max(path) - width + 1)):
                count = sum(left <= n < left + width for n in path)
                require(count <= table[width], "literal window exceeds recursive envelope")
                windows += 1

    # Independent reconstruction of image widths by integer-point counting,
    # including translated endpoints and the half-open upper boundary.
    image_checks = 0
    for width in range(1, 65):
        for clock in range(1, 8):
            modulus = 1 << clock
            for odds in range(clock + 1):
                constant = (3**odds - 2**odds) * (1 << (clock - odds))
                for left in (1, 7, 41):
                    lower_numerator = 3**odds * left
                    upper_numerator = 3**odds * (left + width) + constant
                    count = max(0, (upper_numerator - 1) // modulus -
                                ((lower_numerator + modulus - 1) // modulus) + 1)
                    require(count <= image_width(width, clock, odds), "image envelope too short")
                    image_checks += 1

    selected = []
    for width in (32, 64, 128, 256, 512, 1024, 2048, 4096):
        selected.append({"width": width, "exact_recursive_minimum": table[width],
                         "chosen_clock_and_cut": list(choices[width]) if choices[width] else None})
    policy_rows = [{"width": width, "depth": 3, "certified_upper_bound": policy(width, 3)}
                   for width in (100000, 10000000000)]
    # An explicitly repeated cycle would violate a finite occupancy bound.
    repeated = [1, 2] * (table[16] + 1)
    require(sum(1 <= x < 17 for x in repeated) > table[16],
            "repeated-cycle negative control was ineffective")
    return {"schema": "collatz-translated-interval-bootstrap-v1",
            "scope": "uniform occupancy of one finite simple ordinary path, never a basin count",
            "full_recursive_table_widths": 4096,
            "full_table_sha256": hashlib.sha256(encoded).hexdigest(),
            "candidate_recurrences_checked": inspected,
            "selected_exact_minima": selected,
            "larger_width_policy_bounds_not_full_minima": policy_rows,
            "policy_cache_nodes": policy.cache_info().currsize,
            "literal_sources": 2048, "literal_path_states": states,
            "literal_window_checks": windows, "integer_image_checks": image_checks,
            "rational_power_certificates": 2, "repeated_cycle_control_rejected": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compare", type=Path)
    args = parser.parse_args()
    report = build_report()
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.compare:
        require(report == json.loads(args.compare.read_text(encoding="utf-8")),
                "recursive interval report differs")
    if args.output:
        require(not args.output.exists(), "refusing to overwrite frozen evidence")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
