#!/usr/bin/env python3
"""Exact finite checks of both transport legs, shared envelopes, and clock-row maxima."""

import argparse
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def labels_through(limit, root_origins):
    labels = {root: (root, origin) for root, origin in root_origins.items()}
    for source in range(1, limit + 1):
        n = source
        path = []
        visited = set()
        while n not in labels:
            require(n not in visited, "a trajectory repeated before reaching a supplied root")
            visited.add(n)
            path.append(n)
            n = shortcut(n)
        root, clock = labels[n]
        for previous in reversed(path):
            clock -= 1
            labels[previous] = (root, clock)
    return labels


def shifted(atom):
    component, clock = atom
    return component, clock - 1


def add_disagreement(measure, first, second):
    if first != second:
        measure[first] += 1
        measure[second] += 1


def common_envelope(cutoff, labels):
    doubled = Counter()
    tripled = Counter()
    for end in range(1, 18 * cutoff + 1):
        # Last endpoint of one half-open sixth-cell in (0, 3X].
        base = labels[(end + 5) // 6]
        add_disagreement(doubled, labels[(end + 2) // 3], shifted(base))
        add_disagreement(tripled, labels[(end + 1) // 2], base)
    return doubled, tripled


def prefix_histograms(cutoff, labels, steps):
    # All cutoffs are rational. Every histogram has the same global label names.
    scales = [Fraction(1)]
    for _ in range(steps):
        scale = 2 * scales[-1]
        if scale >= 3:
            scale /= 3
        scales.append(scale)
    cutoffs = [scale * cutoff for scale in scales]
    requested = sorted(set(cutoffs))
    histograms = {}
    current = Counter()
    floor = 0
    for endpoint in requested:
        new_floor = int(endpoint)
        for n in range(floor + 1, new_floor + 1):
            current[labels[n]] += 1
        floor = new_floor
        weighted = current.copy()
        fraction = endpoint - new_floor
        if fraction:
            weighted[labels[new_floor + 1]] += fraction
        histograms[endpoint] = {key: value / endpoint for key, value in weighted.items()}
    return [histograms[endpoint] for endpoint in cutoffs], scales


def run_case(cutoff, root_origins):
    labels = labels_through(9 * cutoff, root_origins)
    doubled, tripled = common_envelope(cutoff, labels)
    envelope_units = doubled + tripled
    denominator = 6 * cutoff
    common_support = {labels[n] for n in range(1, 3 * cutoff + 1)}
    clock_values = [clock for _, clock in common_support]
    steps = max(clock_values) - min(clock_values) + 2
    histograms, scales = prefix_histograms(cutoff, labels, steps)
    for j in range(1, steps + 1):
        previous = {shifted(key): value for key, value in histograms[j - 1].items()}
        current = histograms[j]
        divided = scales[j] != 2 * scales[j - 1]
        for key in current.keys() | previous.keys():
            error = abs(current.get(key, 0) - previous.get(key, 0))
            budget = envelope_units[key] if divided else doubled[key]
            require(error * denominator <= budget, "one transport leg exceeded the common envelope")
    origin_histogram = histograms[0]
    row_max = {}
    for key, mass in origin_histogram.items():
        root, clock = key
        terminal = root, clock - steps
        require(terminal not in common_support, "terminal value did not leave the finite common support")
        translated = sum(envelope_units[root, clock - j] for j in range(1, steps + 1))
        require(mass * denominator <= translated, "translated telescoping failed")
        row_max[root] = max(row_max.get(root, 0), mass)
    total_max = sum(row_max.values())
    require(total_max * denominator <= sum(envelope_units.values()), "summed row maxima exceeded total error")
    return {
        "cutoff": cutoff,
        "origin_clocks_by_root": dict(sorted(root_origins.items())),
        "balanced_steps": steps,
        "divided_steps": sum(scales[j] != 2 * scales[j - 1] for j in range(1, steps + 1)),
        "summed_row_maximum": str(total_max),
        "dyadic_error_mass": str(Fraction(sum(doubled.values()), denominator)),
        "triadic_error_mass": str(Fraction(sum(tripled.values()), denominator)),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="compare the exact report to the recorded fixture")
    args = parser.parse_args()
    cases = [
        run_case(cutoff, roots)
        for cutoff in (8, 31, 128, 511)
        for roots in ({1: 0}, {1: 0, 5: 17, 85: -27})
    ]
    report = json.dumps({"cases": cases}, indent=2, sort_keys=True) + "\n"
    if args.check:
        expected = Path(__file__).with_name("CLOCK_CONTROLS.json").read_text()
        require(expected == report, "the exact clock report changed")
    print(report, end="")


if __name__ == "__main__":
    main()
