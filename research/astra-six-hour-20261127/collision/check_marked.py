#!/usr/bin/env python3
"""Exact bounded checks for the marked original-law identities."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from functools import cache
from itertools import combinations
from math import comb
from pathlib import Path


def compositions(total: int, length: int):
    for cuts in combinations(range(1, total), length - 1):
        positions = (0, *cuts, total)
        yield tuple(b - a for a, b in zip(positions, positions[1:]))


def offset_numerator(word: tuple[int, ...]) -> int:
    total = 0
    numerator = 0
    for gap in word:
        numerator = 3 * numerator + (1 << total)
        total += gap
    return numerator


def orbit_data(start: int, depth: int) -> tuple[int, int]:
    value = start
    total = 0
    for _ in range(depth):
        numerator = 3 * value + 1
        gap = (numerator & -numerator).bit_length() - 1
        value = numerator >> gap
        total += gap
    return value, total


def marked_law(depth: int, max_total: int) -> dict:
    q = 3 ** depth
    counts = Counter()
    for start in range(1, 6 * (1 << max_total), 2):
        target, total = orbit_data(start, depth)
        if total <= max_total and target < 6 * q:
            counts[total, target, start % 3] += 1

    trit_cells = words = 0
    for total in range(depth, max_total + 1):
        histogram = Counter()
        inv_scale = pow(2, -total, 3 * q)
        for word in compositions(total, depth):
            offset = offset_numerator(word) * inv_scale % (3 * q)
            histogram[offset] += 1
            words += 1
        for target in range(1, 6 * q, 2):
            for digit in range(3):
                residue = (pow(2, total, 3) * digit) % 3
                predicted = histogram[(target - digit * q) % (3 * q)]
                assert predicted == counts[total, target, residue]
                trit_cells += 1
    return dict(depth=depth, total_at_most=max_total, words=words,
                exact_cells=trit_cells, observed_preimages=sum(counts.values()))


@cache
def geometric_sum(count: int, total: int) -> Fraction:
    if count == 0:
        return Fraction(int(total == 0))
    if total < count:
        return Fraction()
    return Fraction(comb(total - 1, count - 1), 1 << total)


def inverse_tree(root: int, max_depth: int, max_total: int) -> dict:
    # Every node here reaches this single positive target at the specified
    # depth. The branch truncation discards only gaps beyond the tested total.
    layers = [{(root, 0)}]
    counted = [Counter({(0, root % 3): 1})]
    for _ in range(max_depth):
        children = set()
        for target, total in layers[-1]:
            for gap in range(1, max_total - total + 1):
                numerator = (1 << gap) * target - 1
                if numerator % 3 == 0:
                    child = numerator // 3
                    assert child > 0 and child % 2 == 1
                    assert (child, total + gap) not in children
                    children.add((child, total + gap))
        layers.append(children)
        counted.append(Counter((total, child % 3) for child, total in children))

    mass: list[list[Fraction]] = []
    forcing: list[list[Fraction]] = []
    equalities = 0
    for depth, indexed in enumerate(counted):
        level = []
        for total in range(max_total + 1):
            cardinality = sum(indexed[total, digit] for digit in range(3))
            level.append(Fraction(cardinality * 3**depth, root * (1 << total)))
        mass.append(level)
        if depth == 0:
            continue
        previous = counted[depth-1]
        residual = []
        for total in range(max_total + 1):
            digit_prediction = Fraction()
            mixed_prediction = Fraction()
            for gap in range(1, total + 1):
                earlier_total = total - gap
                digit = pow(2, -gap, 3)
                weight = Fraction(3**depth, root * (1 << total))
                digit_prediction += weight * previous[earlier_total, digit]
                mixed_prediction += geometric_sum(1, gap) * mass[depth-1][earlier_total]
            assert digit_prediction == level[total]
            residual.append(digit_prediction - mixed_prediction)
            equalities += 1
        forcing.append(residual)
        for total in range(max_total + 1):
            propagated = geometric_sum(depth, total) * mass[0][0]
            for time in range(1, depth + 1):
                for earlier_total in range(total + 1):
                    propagated += (geometric_sum(depth-time, total-earlier_total)
                                   * forcing[time-1][earlier_total])
            assert propagated == level[total]
            equalities += 1

    example = None
    for depth, layer in enumerate(layers):
        by_total: dict[int, list[int]] = {}
        for child, total in sorted(layer):
            by_total.setdefault(total, []).append(child)
        for total, starts in sorted(by_total.items()):
            if len(starts) >= 2:
                example = dict(root=root, depth=depth, total=total, starts=starts[:2])
                assert all(orbit_data(x, depth) == (root, total) for x in starts[:2])
                break
        if example is not None:
            break
    return dict(root=root, max_depth=max_depth, max_total=max_total,
                nodes_by_depth=[len(layer) for layer in layers],
                tested_equalities=equalities, exact_same_clock_pair=example)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {
        "scope": "Finite exact checks of the retained-clock trit formula, inverse "
                 "recursion and geometric forcing expansion. No escape or "
                 "unbounded-depth inference.",
        "marked_original_law": [marked_law(k, k+8) for k in range(1, 6)],
        "single_target_trees": [inverse_tree(y, 6, 18) for y in (5, 7, 11)],
    }
    text = json.dumps(report, indent=2) + "\n"
    if args.output is None:
        print(text, end="")
    else:
        args.output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
