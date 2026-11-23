"""Exact small certificates for the all-depth optimizer diagnostic.

All-depth coverage is the written bound gamma(n,q) <= q/n. This program
checks the finite low-source certificate and its exact cutoff arithmetic;
it does not search an unbounded ancestor tree or verify Collatz globally.
"""

from fractions import Fraction
from itertools import product
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def odd_step(n):
    require(isinstance(n, int) and n > 0 and n % 2 == 1, "positive odd input")
    value = 3 * n + 1
    gap = 0
    while value % 2 == 0:
        value //= 2
        gap += 1
    return value, gap


def to_one(n):
    values, gaps = [n], []
    seen = set()
    while n != 1:
        require(n not in seen, "unexpected nontrivial repeated state")
        require(len(values) < 1000, "control horizon exceeded")
        seen.add(n)
        n, gap = odd_step(n)
        values.append(n)
        gaps.append(gap)
    return {"states": values, "gaps": gaps}


def carry(gaps):
    total = 0
    prefix = 0
    for i, gap in enumerate(gaps):
        total += 3 ** (len(gaps) - 1 - i) * 2 ** prefix
        prefix += gap
    return total


def check():
    targets = [31, 47, 71, 107, 161, 121, 91]
    gaps = [1, 1, 1, 1, 2, 2]
    for source, target, gap in zip(targets, targets[1:], gaps):
        require(odd_step(source) == (target, gap), "displayed edge mismatch")
        require(source % 3 != 0 and target % 3 != 0, "unit-domain mismatch")

    low_sources = [n for n in range(1, 31, 2) if n % 3 != 0]
    require(low_sources == [1, 5, 7, 11, 13, 17, 19, 23, 25, 29], "low source inventory")
    low_paths = {str(n): to_one(n) for n in low_sources}
    for n, record in low_paths.items():
        require(set(record["states"]).isdisjoint(targets), "low source reaches a target: " + n)

    original_path = to_one(31)
    require(original_path["states"][:7] == targets, "original prefix mismatch")
    require(len(original_path["states"]) == len(set(original_path["states"])), "original nontrivial revisit")

    clock = 0
    comparisons = []
    for j, q in enumerate(targets):
        if j:
            clock += gaps[j - 1]
        lhs = q * 2 ** clock
        rhs = 32 * 3 ** j
        require(lhs < rhs, "unbounded-source cutoff failed")
        comparisons.append({"odd_clock": j, "target": q, "total_gap": clock,
                            "target_times_two_power": lhs, "cutoff_times_three_power": rhs})
    require(Fraction(91, 32) == Fraction(728, 256), "one-unit comparison")
    require(Fraction(91, 32) < Fraction(729, 256), "final strict cutoff")

    bits = "".join("1" + "0" * (a - 1) for a in gaps)
    require(bits == "11111010", "shortcut encoding")
    doubled = bits + bits
    windows = [doubled[i:i + 4] for i in range(len(bits))]
    counts = [word.count("1") for word in windows]
    require(max(counts) - min(counts) == 2, "unbalanced certificate")

    fixed_fibre = []
    for candidate in product(range(1, 5), repeat=3):
        if sum(candidate) != 6:
            continue
        c = carry(candidate)
        n = Fraction(2 ** 6 * 5 - c, 3 ** 3)
        ordinary = n.denominator == 1 and n > 0 and n.numerator % 2 == 1 and n.numerator % 3 != 0
        if ordinary:
            state = n.numerator
            for gap in candidate:
                next_state, actual_gap = odd_step(state)
                require(actual_gap == gap and next_state % 3 != 0, "admissible fibre edge")
                state = next_state
            require(state == 5, "admissible fibre endpoint")
        fixed_fibre.append({"gaps": list(candidate), "carry": c,
                            "input": str(n), "ordinary_unit_ancestor": ordinary})
    require(len(fixed_fibre) == 10, "composition coverage")
    valid = [entry for entry in fixed_fibre if entry["ordinary_unit_ancestor"]]
    require(valid == [{"gaps": [1, 2, 3], "carry": 23, "input": "11", "ordinary_unit_ancestor": True}], "singleton fibre")
    require(carry((2, 2, 2)) == 37, "balanced carry")
    require(Fraction(320 - 37, 27) == Fraction(283, 27), "balanced rational input")

    return {"schema": "collatz-optimal-ancestor-control/v1", "success": True,
            "scope": "finite certificates for an all-depth written bound; not Collatz closure",
            "low_source_count": len(low_sources), "low_source_paths": low_paths,
            "original_path_to_one": original_path, "all_depth_cutoffs": comparisons,
            "unbalanced_word": bits, "length_four_windows": windows,
            "window_ones_counts": counts, "fixed_target_fibre": fixed_fibre}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2, sort_keys=True))
