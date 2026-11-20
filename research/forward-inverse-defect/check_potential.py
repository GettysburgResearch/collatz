#!/usr/bin/env python3
"""Exact bounded replay for PROOF.md; no infinite pointwise bound is tested."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def odd_step(n):
    require(n > 0 and n % 2 == 1, "odd positive input required")
    z = 3 * n + 1
    g = (z & -z).bit_length() - 1
    return z >> g, g


def potential_by_paths(root, horizon, require_terminal_unit=True):
    """Enumerate actual inverse paths, with a score-based exact pruning rule."""
    best = 0
    visited = 0
    stack = [(root, 0, 0)]
    while stack:
        n, depth, score = stack.pop()
        visited += 1
        best = max(best, score)
        if depth == horizon:
            continue
        remaining = horizon - depth - 1
        # Every later letter gains at most 3. A branch unable to beat zero
        # cannot improve the potential and may be omitted.
        maximum_gap = (score + 8 + 3 * remaining - 1) // 5
        for g in range(1, maximum_gap + 1):
            numerator = (n << g) - 1
            if numerator % 3:
                continue
            child = numerator // 3
            if require_terminal_unit and child % 3 == 0:
                continue
            stack.append((child, depth + 1, score + 8 - 5 * g))
    return best, visited


def bounded_words(length, total_bound, prefix=()):
    """Independent composition enumeration, without testing any source."""
    if length == 0:
        yield prefix
        return
    for gap in range(1, total_bound - length + 2):
        yield from bounded_words(length - 1, total_bound - gap, prefix + (gap,))


def potential_by_source_domains(horizon):
    """Construct all positive-score source cylinders using affine algebra."""
    modulus = 3 ** (horizon + 1)
    values = [0] * modulus
    word_count = 0
    for length in range(1, horizon + 1):
        bound = (8 * length - 1) // 5
        for word in bounded_words(length, bound):
            total = sum(word)
            score = 8 * length - 5 * total
            require(score > 0, "composition bound failed")
            coefficient = 1
            offset = 0
            for gap in word:
                offset = (offset << gap) + coefficient
                coefficient *= 3
            small_modulus = 3 ** (length + 1)
            inverse_denominator = pow(1 << total, -1, small_modulus)
            residues = {
                ((coefficient * last + offset) * inverse_denominator)
                % small_modulus
                for last in (1, 2)
            }
            require(len(residues) == 2, "unit-terminal domains must be distinct")
            for residue in residues:
                require(residue % 3 != 0, "source domain left the units")
                for r in range(residue, modulus, small_modulus):
                    values[r] = max(values[r], score)
            word_count += 1
    return values, word_count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    weight_sum = Fraction(6**8, 3 * 5**3 * (6**5 - 5**5))
    require(weight_sum == Fraction(1679616, 1744125), "weight sum mismatch")
    require(weight_sum < 1, "letter weights are not a subprobability")
    require(100**5 < 2**8 * 33**5, "ordinary drift threshold failed")
    require(3**41 < 2**65 and 3**7 > 2**11, "critical coefficient bracket failed")
    floor = 56 * 2**43
    small_gap_error = Fraction(7 * 2**43, 2 * (floor + 1))
    require(small_gap_error < Fraction(1, 16), "uniform finite-gap error failed")
    require(Fraction(43, 8) - Fraction(21, 4) > Fraction(1, 16),
            "uniform large-gap gain failed")

    rows = []
    residue_checks = 0
    lift_checks = 0
    node_visits = 0
    for depth in range(1, 8):
        source_values, word_count = potential_by_source_domains(depth)
        modulus = len(source_values)
        histogram = Counter()
        for root in range(modulus):
            if root % 3 == 0:
                continue
            value, nodes = potential_by_paths(root, depth)
            require(value == source_values[root],
                    f"independent source-domain mismatch at depth {depth}, root {root}")
            histogram[value] += 1
            residue_checks += 1
            node_visits += nodes
            if depth <= 4:
                for lift in (1, 2):
                    lifted, _ = potential_by_paths(root + lift * modulus, depth)
                    require(lifted == value, "unobserved-lift value changed")
                    lift_checks += 1
        population = sum(histogram.values())
        for level in range(1, 3 * depth + 1):
            tail = sum(count for value, count in histogram.items() if value >= level)
            require(tail * 6**level <= population * 5**level,
                    f"finite Haar tail failed at depth {depth}, level {level}")
        minus_one, _ = potential_by_paths(-1, depth)
        require(minus_one == 3 * depth, "negative fixed-point score failed")
        rows.append({
            "depth": depth,
            "modulus": modulus,
            "unit_residues": population,
            "positive_score_words": word_count,
            "maximum": max(histogram),
            "histogram": dict(sorted(histogram.items())),
        })

    forward_edges = 0
    for n in range(1, 2002, 2):
        if n % 3 == 0:
            continue
        target, gap = odd_step(n)
        before, _ = potential_by_paths(n, 4)
        after, _ = potential_by_paths(target, 5)
        require(after >= before + 8 - 5 * gap, "finite-horizon forward inequality failed")
        require((target + 1) * 2**gap == 3 * (n + 1) + 2**gap - 2,
                "critical-height affine identity failed")
        forward_edges += 1

    small_sources = []
    for start in range(1, 33):
        n = start
        seen = set()
        steps = 0
        while n != 1:
            require(n not in seen, "small source repeated before reaching 1")
            seen.add(n)
            n = n // 2 if n % 2 == 0 else (3 * n + 1) // 2
            steps += 1
        small_sources.append({"source": start, "shortcut_steps": steps})

    converger_controls = []
    for q in range(1, 9):
        exponent = 3 ** (q + 1) + 1
        n = (2**exponent - 1) // 3
        require(n % 2 == 1 and n % 3 != 0, "control is not an odd unit")
        target, gap = odd_step(n)
        require((target, gap) == (1, exponent), "one-step convergence control failed")
        z = n
        for _ in range(q):
            require((2 * z - 1) % 3 == 0, "control inverse letter not integral")
            z = (2 * z - 1) // 3
            require(z > 0 and z % 2 == 1 and z % 3 != 0,
                    "control inverse letter left positive ordinary odd units")
        require((n + 1) % 3 ** (q + 1) == 0
                and (n + 1) % 3 ** (q + 2) != 0, "control precision mismatch")
        converger_controls.append({
            "inverse_ones": q,
            "certified_score": 3 * q,
            "root_bits": n.bit_length(),
            "forward_odd_steps_to_1": 1,
            "forward_exponent": exponent,
        })

    # These controls catch three mathematically material wrong strengthenings.
    proper, _ = potential_by_paths(5, 1)
    omitted_terminal_guard, _ = potential_by_paths(5, 1, False)
    require(proper == 0 and omitted_terminal_guard == 3,
            "unit-terminal mutation was not detected")
    value_two, _ = potential_by_paths(2, 1)
    value_five, _ = potential_by_paths(5, 1)
    require(2 % 3 == 5 % 3 and value_two != value_five,
            "missing extra ternary digit was not detected")
    before_one, _ = potential_by_paths(1, 1)
    after_one, _ = potential_by_paths(1, 2)
    require(after_one >= before_one + 8 - 5 * 2
            and not after_one >= before_one + 8 + 5 * 2,
            "wrong forward sign mutation was not detected")

    report = {
        "status": "PASS",
        "scope": "Exact finite arithmetic and independent truncation reconstruction; "
                 "does not establish the uniform ordinary potential bound or Collatz",
        "weight_sum": {"numerator": weight_sum.numerator,
                       "denominator": weight_sum.denominator},
        "critical_height_floor": floor,
        "critical_height_gain": "1/16 per exponent greater than one above the floor",
        "independent_residue_comparisons": residue_checks,
        "unseen_lift_comparisons": lift_checks,
        "path_nodes_visited": node_visits,
        "forward_edges_checked": forward_edges,
        "finite_haar_profiles": rows,
        "small_source_replays": small_sources,
        "immediate_converger_controls": converger_controls,
        "rejected_mutations": [
            "omit the final ternary-unit guard",
            "observe only N rather than N+1 ternary digits",
            "reverse the sign of the forward exponent cost",
        ],
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
