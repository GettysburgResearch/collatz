"""Check the inverse digits, reflection into a shell, and the finite upper count."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from math import comb
from pathlib import Path

from source_clock_controls import physical_child, prepare, require, shortcut


def exponent(parent, start, index):
    first = [e for e in range(start, start + 6) if (parent << e) % 9 in (4, 7)]
    require(len(first) == 2, "unit alphabet count mismatch")
    return first[index % 2] + 6 * (index // 2)


def shell_fixture(target, depth, digit_budget):
    root, prep_clock = prepare(target)
    maximum_time = 3 * digit_budget + 8 * depth
    # This exact ceiling on the worst ideal origin puts every test leaf below X.
    scale = ((root << maximum_time) + 3 ** depth - 1) // (3 ** depth)
    answers = {}
    clock_histogram = Counter()

    def visit(parent, count, budget, time):
        if count:
            for index in range(budget + 1):
                e = exponent(parent, 2, index)
                child = physical_child(parent, e)
                require(child > parent and child % 3 != 0, "inverse path failed to increase")
                visit(child, count - 1, budget - index, time + e)
            return
        ideal = Fraction(root << time, 3 ** depth)
        require(0 < ideal - parent <= Fraction(1 << time, 3 ** depth), "wrong defect scale")
        require(parent <= scale, "odd source beyond shell base")
        source = parent
        arrival = prep_clock + time
        while source < scale:
            source *= 2
            arrival += 1
        require(source < 2 * scale and source not in answers, "duplicate shell source")
        value = source
        for _ in range(arrival):
            require(value > target, "premature shortcut hit")
            value = shortcut(value)
        require(value == target, "wrong shortcut arrival")
        answers[source] = arrival
        clock_histogram[arrival] += 1

    visit(root, depth, digit_budget, 0)
    require(len(answers) == comb(digit_budget + depth, depth), "composition count mismatch")
    require(max(clock_histogram) - min(clock_histogram) <= 1, "clocks failed to equalize")
    digest = hashlib.sha256(repr(sorted(answers.items())).encode()).hexdigest()
    return {"target": target, "odd_inverse_depth": depth, "digit_budget": digit_budget,
            "origins": len(answers), "distinct_clocks": len(clock_histogram),
            "largest_atom": max(clock_histogram.values()), "origins_and_clocks_sha256": digest}


def upper_fixture(target, cutoff):
    # Enumerate the entire finite first-hit layer, including initially even origins,
    # and compare with the integer encoding in the proof of inequality (4).
    layer = {target}
    seen = {target}
    by_length = []
    for time in range(1, cutoff + 1):
        next_layer = set()
        for vertex in layer:
            next_layer.add(2 * vertex)
            if vertex % 3 == 2:
                next_layer.add((2 * vertex - 1) // 3)
        layer = next_layer - seen
        seen.update(layer)
        by_q = Counter()
        for source in layer:
            vertex = source
            q = 0
            for _ in range(time):
                q += vertex % 2
                vertex = shortcut(vertex)
            require(vertex == target, "upper fixture forward orbit mismatch")
            by_q[q] += 1
        for q, actual in by_q.items():
            upper = time * comb((time + 6 * q) // 3 + q, q) if q else 1
            require(actual <= upper, "unrestricted layer exceeded composition bound")
        by_length.append(len(layer))
    return {"target": target, "depth": cutoff, "total_new_origins": sum(by_length),
            "layer_sizes": by_length}


def report():
    cases = 0
    for parent in (1, 5, 7, 11, 13, 17):
        for start in (1, 2):
            for j in range(40):
                e = exponent(parent, start, j)
                require(3 * j - 6 <= e <= 3 * j + 8, "uniform digit spacing failed")
                require(physical_child(parent, e) % 3 != 0, "digit did not produce a unit")
                cases += 1
    return {"unit_root_start_index_cases": cases,
            "one_clock_shells": [shell_fixture(y, q, b) for y in (1, 5, 85, 1000001)
                                 for q, b in ((3, 9), (5, 5))],
            "all_preimage_upper_cases": [upper_fixture(y, 15) for y in (1, 5, 85)]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = json.dumps(report(), indent=2, sort_keys=True) + "\n"
    if args.check:
        require(result == Path(__file__).with_name("FAST_CLOCK_CONTROLS.json").read_text(),
                "fast-clock fixture changed")
    print(result, end="")
