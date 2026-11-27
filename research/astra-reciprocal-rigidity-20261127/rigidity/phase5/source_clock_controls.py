"""Replay the ordinary inverse bank, its finite residue census and sample clocks."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def require(test: bool, message: str) -> None:
    if not test:
        raise ValueError(message)


def lift_counts(steps: int, maximum: int, minimum_letter: int) -> dict[tuple[int, int], int]:
    """Prepend odd-to-odd exponents, lifting the parent modulus once per letter."""
    counts = Counter({(0, 1): 1})
    modulus = 3
    for used in range(steps):
        modulus *= 3
        limit = maximum - minimum_letter * (steps - used - 1)
        powers = [pow(2, -exponent, modulus) for exponent in range(limit + 1)]
        expanded = Counter()
        for (total, child), count in counts.items():
            for exponent in range(minimum_letter, limit - total + 1):
                parent = ((3 * child + 1) * powers[exponent]) % modulus
                expanded[total + exponent, parent] += count
        counts = expanded
    return counts


def positive_prefix_counts(steps: int, total_time: int) -> Counter:
    """Count words whose every cumulative inverse multiplier exceeds one."""
    prefix_minimum = [0] + [(3 ** i).bit_length() for i in range(1, steps + 1)]
    counts = Counter({(total_time, 1): 1})
    modulus = 3
    for prefix_length in range(steps, 0, -1):
        modulus *= 3
        inverse = [pow(2, -e, modulus) for e in range(total_time + 1)]
        expanded = Counter()
        for (remaining, child), count in counts.items():
            if remaining < prefix_minimum[prefix_length]:
                continue
            options = (remaining,) if prefix_length == 1 else range(
                1, remaining - prefix_minimum[prefix_length - 1] + 1)
            for exponent in options:
                previous = ((3 * child + 1) * inverse[exponent]) % modulus
                expanded[remaining - exponent, previous] += count
        counts = expanded
    return Counter({residue: count for (remaining, residue), count in counts.items()
                    if remaining == 0})


def physical_child(parent: int, exponent: int) -> int:
    numerator = (parent << exponent) - 1
    require(numerator % 3 == 0, "nonintegral odd ancestor")
    child = numerator // 3
    require(child % 2 == 1 and child > 0, "invalid odd ancestor")
    return child


def shortcut(source: int) -> int:
    return (3 * source + 1) // 2 if source % 2 else source // 2


def prepare(target: int) -> tuple[int, int]:
    exponent = next(e for e in range(10, 16) if (target << e) % 9 == 4)
    return physical_child(target, exponent), exponent


def pair(parent: int, total: int) -> tuple[int, int]:
    candidates = [e for e in range(4, 21, 2) if pow(2, e, 27) == ((parent << total) - 12) % 27]
    require(len(candidates) == 1, "pair steering failed")
    second = candidates[0]
    first = total - second
    middle = physical_child(parent, first)
    end = physical_child(middle, second)
    require(end % 3 == 1 and end > middle > parent, "bad two-step branch")
    return end, total


def dyadic_leaf_fixture(target: int, log_scale: int) -> dict:
    root, initial = prepare(target)
    threshold = root << log_scale
    pending = [(root, initial)]
    leaves = []
    while pending:
        value, clock = pending.pop()
        if value >= threshold:
            leaves.append((value, clock))
            continue
        for total in (24, 26):
            child, length = pair(value, total)
            pending.append((child, clock + length))
    shell = threshold * (1 << 26) // 9 + 1
    answers = {}
    for odd, clock in leaves:
        source = odd
        while source < shell:
            source *= 2
            clock += 1
        require(shell <= source < 2 * shell and source not in answers, "shell injection failed")
        value = source
        for _ in range(clock):
            require(value > target, "early hit or dip")
            value = shortcut(value)
        require(value == target, "physical first arrival did not match")
        answers[source] = clock
    distribution = sorted(Counter(answers.values()).items())
    return {"target": target, "log2_growth_cut": log_scale, "sources": len(answers),
            "distinct_clocks": len(distribution), "maximum_clock_atom": max(v for k, v in distribution),
            "clock_histogram_sha256": hashlib.sha256(repr(distribution).encode()).hexdigest()}


def report() -> dict:
    counts = lift_counts(6, 40, 2)
    modulus = 3 ** 7
    minima = {h: min(counts[h, a] for a in range(1, modulus, 3)) for h in range(27, 41)}
    require(min(minima.values()) > 0, "six-step bank missing a type")
    pressure = sum(Fraction(9 * value, 2 ** ((h + 2) // 3)) for h, value in minima.items())
    require(pressure > 1, "one-third pressure certificate failed")
    # Check the residue-lift combinatorics against an independent physical search.
    small = lift_counts(3, 15, 2)
    physical_comparisons = 0
    for residue in range(1, 3 ** 4, 3):
        parent = residue + (0 if residue % 2 else 3 ** 4)
        observed = Counter()
        def visit(value: int, depth: int, total: int) -> None:
            if depth == 3:
                if value % 3 == 1:
                    observed[total] += 1
                return
            for e in range(2, 16 - total):
                if (value << e) % 3 == 1:
                    visit(physical_child(value, e), depth + 1, total + e)
        visit(parent, 0, 0)
        for h in range(6, 16):
            require(observed[h] == small[h, residue], "residue census disagrees with true vertices")
            physical_comparisons += 1
    full_prefix = {h: positive_prefix_counts(8, h) for h in range(24, 37)}
    prefix_minima = {h: min(row[a] for a in range(1, 3 ** 9, 3))
                     for h, row in full_prefix.items()}
    half_pressure = sum(Fraction(81 * value, 2 ** ((h + 1) // 2))
                        for h, value in prefix_minima.items())
    require(half_pressure > 1, "one-half pressure certificate failed")
    # Walk actual integers independently in the prefix-balanced three-step model.
    prefix_physical = {h: positive_prefix_counts(3, h) for h in range(6, 16)}
    for residue in range(1, 3 ** 4, 3):
        root = residue + (3 ** 4 if residue % 2 == 0 else 0) + 2 * 3 ** 4
        frontier = [(root, 0)]
        for i in range(1, 4):
            frontier = [(physical_child(z, e), h + e)
                        for z, h in frontier for e in range(1, 16 - h)
                        if (1 << (h + e)) > 3 ** i and (z << e) % 3 == 1]
        obs = Counter(h for z, h in frontier if z % 3 == 1)
        for h in range(6, 16):
            require(obs[h] == prefix_physical[h][residue], "physical prefix census mismatch")
    for residue in range(1, 27, 3):
        odd = residue if residue % 2 else residue + 27
        for total in (24, 26):
            pair(odd, total)
    return {"six_odd_steps": {"modulus": modulus, "root_residues": 3 ** 6,
                "minimum_arity_by_total_time": minima, "lower_pressure_at_one_third": str(pressure)},
            "eight_odd_steps": {"modulus": 3 ** 9, "root_residues": 3 ** 8,
                "minimum_arity_by_total_time": prefix_minima, "lower_pressure_at_one_half": str(half_pressure),
                "minimum_ideal_prefix_multiplier": str(min(Fraction(2 ** ((3 ** i).bit_length()), 3 ** i)
                                                          for i in range(1, 9)))},
            "physical_census_comparisons_per_model": physical_comparisons,
            "elementary_pair_residue_time_cases": 18,
            "first_hit_shells": [dyadic_leaf_fixture(y, level) for y in (1, 5, 85, 1000001)
                                 for level in (67, 137)]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = json.dumps(report(), indent=2, sort_keys=True) + "\n"
    if args.check:
        require(result == Path(__file__).with_name("SOURCE_CLOCK_CONTROLS.json").read_text(),
                "source-clock fixture changed")
    print(result, end="")
