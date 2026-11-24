#!/usr/bin/env python3
"""Exact finite controls for the killed negative-integer inverse kernel."""
from collections import defaultdict
from fractions import Fraction
import json


def require(value, message):
    if not value:
        raise ValueError(message)


def children(h):
    yield 2 * h, Fraction(1, 3)
    if h % 3 == 1:
        yield (2 * h + 1) // 3, Fraction(2, 3)


def advance(distribution):
    result = defaultdict(Fraction)
    for h, mass in distribution.items():
        for child, weight in children(h):
            result[child] += mass * weight
    return dict(result)


def main():
    constant = Fraction(32, 13)
    ratio = Fraction(76, 81)
    bound = Fraction(1539, 13)
    for h in range(1, 10001):
        first = advance({h: Fraction(1)})
        second = advance(first)
        moment1 = sum(mass * (j + constant) for j, mass in first.items())
        moment2 = sum(mass * (j + constant) for j, mass in second.items())
        require(moment1 <= Fraction(10, 9) * (h + constant), "one-step moment")
        require(moment2 <= ratio * (h + constant), "two-step contraction")
        if h % 3 == 0:
            formula = Fraction(4 * h, 9) + constant / 9
        elif h % 3 == 2:
            formula = Fraction(20 * h, 27) + constant / 3 + Fraction(2, 27)
        elif h % 9 == 1:
            formula = Fraction(76 * h, 81) + 7 * constant / 9 + Fraction(32, 81)
        else:
            formula = Fraction(20 * h, 27) + constant / 3 + Fraction(4, 27)
        require(moment2 == formula, "full residue row")

    distribution = {1: Fraction(1)}
    measure = defaultdict(Fraction)
    for _ in range(24):
        for h, mass in distribution.items():
            measure[h] += mass
        distribution = advance(distribution)
    partial = sum(mass * (h + constant) for h, mass in measure.items())
    require(partial <= bound, "finite Green moment bound")
    require(measure[2] >= Fraction(1, 3), "positive pole at magnitude two")
    for k in range(4, 50, 2):
        n = (2 ** (k + 1) - 5) // 3
        require(3 * n == 2 ** (k + 1) - 5 and n % 2 == 1, "ordinary pole lift")
        target = (3 * n + 1) // 2
        require(target + 2 == 2 ** k, "pulled-back pole")
    print(json.dumps({
        "two_step_rows": 10000,
        "green_depths": 24,
        "distinct_negative_centers": len(measure),
        "weighted_moment_partial_sum": str(partial),
        "weighted_moment_upper_bound": str(bound),
        "odd_pole_lifts": 23,
        "scope": "finite operator controls; no universal supersolution",
    }, indent=2))


if __name__ == "__main__":
    main()
