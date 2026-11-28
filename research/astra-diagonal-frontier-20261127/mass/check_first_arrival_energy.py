"""Compare original-word canonical rows with ordinary first-hit and all-visit counts."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import argparse
import json
from pathlib import Path


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


def odd_step(value):
    numerator = 3 * value + 1
    gap = (numerator & -numerator).bit_length() - 1
    return numerator >> gap, gap


def word_rows(depth, maximum_clock):
    """Count genuine original words by native total and ternary affine endpoint."""
    if depth == 0:
        return Counter({(0, 0): 1})
    modulus = 3**depth
    counts = Counter()
    for clock in range(depth, maximum_clock + 1):
        inverse_two = pow(2, -clock, modulus)
        for breaks in combinations(range(1, clock), depth - 1):
            prefix_totals = (0, *breaks)
            numerator = sum(
                3 ** (depth - index - 1) * 2**total
                for index, total in enumerate(prefix_totals)
            )
            counts[clock, (inverse_two * numerator) % modulus] += 1
    return counts


def source_rows(depth, maximum_clock):
    modulus = 3**depth
    all_visits = Counter()
    first_visits = Counter()
    # Every possible input is ≤p and the largest retained y is below 2q.
    for source in range(1, 2 ** (maximum_clock + 1), 2):
        value = source
        visited = set()
        clock = 0
        for _ in range(depth):
            visited.add(value)
            value, gap = odd_step(value)
            clock += gap
            if clock > maximum_clock:
                break
        if clock <= maximum_clock and value < 2 * modulus:
            all_visits[clock, value] += 1
            if value not in visited:
                first_visits[clock, value] += 1
    return all_visits, first_visits


def primitive_lap(target, maximum_depth):
    value = target
    clock = 0
    for depth in range(1, maximum_depth + 1):
        value, gap = odd_step(value)
        clock += gap
        if value == target:
            return depth, clock
    return None


def compare(maximum_depth, maximum_clock):
    tables = [word_rows(d, maximum_clock) for d in range(maximum_depth + 1)]
    output = []
    for depth, words in enumerate(tables):
        all_visits, first_visits = source_rows(depth, maximum_clock)
        modulus = 3**depth
        predicted_all = Counter()
        predicted_first = Counter()
        cyclic_rows = 0
        energy = Fraction()
        for (clock, residue), count in words.items():
            target = residue if residue % 2 else residue + modulus
            predicted_all[clock, target] = count
            lap = primitive_lap(target, depth)
            rejected = 0
            if lap:
                lap_depth, lap_clock = lap
                shorter = depth - lap_depth
                rejected = tables[shorter][clock - lap_clock, target % (3**shorter)]
            survivors = count - rejected
            check(survivors >= 0, f"Negative first-hit count at {(depth, clock, target)}")
            if survivors:
                predicted_first[clock, target] = survivors
                energy += Fraction(modulus * survivors, 2**clock * target) ** 3
            cyclic_rows += bool(rejected)
        check(all_visits == predicted_all, f"Unrestricted rows disagree at depth {depth}")
        check(first_visits == predicted_first, f"First visits disagree at depth {depth}")
        direct_energy = sum(
            Fraction(modulus * count, 2**clock * target) ** 3
            for (clock, target), count in first_visits.items()
        )
        check(energy == direct_energy, f"Cubic energy disagrees at depth {depth}")
        output.append({
            "odd_depth": depth,
            "native_clock_at_most": maximum_clock,
            "canonical_odd_targets_below": 2 * modulus,
            "unrestricted_rows": len(all_visits),
            "first_arrival_rows": len(first_visits),
            "rows_with_positive_lap_subtraction": cyclic_rows,
            "exact_first_sources": sum(first_visits.values()),
            "cubic_numerator": str(energy.numerator),
            "cubic_denominator": str(energy.denominator),
        })
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    results = compare(maximum_depth=5, maximum_clock=13)
    rendered = json.dumps(results, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end="")
