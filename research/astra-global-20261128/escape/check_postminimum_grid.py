#!/usr/bin/env python3
"""Exact finite floor, affine-strip, donor-split and critical grid controls."""

from bisect import bisect_left
from fractions import Fraction as F
from functools import lru_cache
import json


def require(truth, message):
    if not truth:
        raise RuntimeError(message)


def next_edge(x):
    lift = 3 * x + 1
    power = lift & -lift
    return lift // power, power.bit_length() - 1


def first_repeat(x):
    seen = set()
    path = []
    while x not in seen:
        seen.add(x)
        path.append(x)
        x, _ = next_edge(x)
    return path + [x]


def count_interval(grid, lo, hi):
    return bisect_left(grid, hi) - bisect_left(grid, lo)


@lru_cache(maxsize=None)
def grid_powers(base, p, q, cap):
    """q-th powers of all relevant base^(n+p/q), keeping endpoint equality."""
    points = []
    index = -2
    while True:
        point = base ** (q * index + p)
        points.append(point)
        if point > cap ** q:
            return points
        index += 1


def critical_grid_checks():
    phases = [(0, 1), (1, 2), (1, 3), (2, 3), (3, 5), (4, 7)]
    counters = dict(grid_tests=0, ideal_one=0, doubled=0, missed=0, exact_one=0)
    for y in range(1, 8192, 2):
        z, e = next_edge(y)
        if e == 1:
            base = F(3, 2)
        else:
            base = F(2 ** e, 3)
        ideal = F(3 * y, 2 ** e)
        for p, q in phases:
            grid = grid_powers(base, p, q, 13000)
            ci = count_interval(grid, min(y, ideal) ** q, max(y, ideal) ** q)
            ca = count_interval(grid, min(y, z) ** q, max(y, z) ** q)
            strip = count_interval(grid, y ** q, (y + F(1, 3)) ** q)
            require(ci == 1, (y, str(F(p, q)), ci))
            require(abs(ca - ci) == strip, (y, e, p, q, ca, strip))
            require(ca == 1 + (strip if e == 1 else -strip), (y, e, p, q))
            counters["grid_tests"] += 1
            counters["ideal_one"] += ci
            counters[{0: "missed", 1: "exact_one", 2: "doubled"}[ca]] += 1
    require(counters["doubled"] and counters["missed"], "both error directions")
    return counters


def rewards(path, B):
    survival = F(1)
    up, down, high_kill = F(0), F(0), F(0)
    for x, y in zip(path, path[1:]):
        w = F(3 * x, 3 * x + 1)
        if x > B:
            high_kill += survival * (1 - w)
        survival *= w
        if x <= B < y:
            up += survival
        if y <= B < x:
            down += survival
    return up, down, high_kill, survival


def true_postminimum_checks():
    counters = dict(trajectory_floor_tests=0, minimum_splits=0,
                    native_offset_segments=0, repeated_lap_tests=0)
    for m in range(1, 512, 2):
        path = first_repeat(m)
        # Follow three further actual odd steps, including laps at the fixed point.
        for _ in range(3):
            path.append(next_edge(path[-1])[0])
        tau = path.index(min(path))
        for B in sorted({1, 3, min(path), m, m // 2, max(path) // 2}):
            up, down, high_kill, survival = rewards(path, B)
            expected = survival * int(path[-1] > B) - int(path[0] > B) + high_kill
            require(up - down == expected, (m, B, "signed flux"))
            early = rewards(path[:tau + 1], B)
            late = rewards(path[tau:], B)
            for j in range(3):
                require((up, down, high_kill)[j] == early[j] + early[3] * late[j],
                        (m, B, "minimum split", j))
            counters["trajectory_floor_tests"] += 1
            counters["minimum_splits"] += 1
            if len(path) > len(set(path)):
                counters["repeated_lap_tests"] += 1
        for i in range(len(path) - 1):
            A = F(1)
            offset = F(0)
            for j in range(i, min(i + 7, len(path) - 1)):
                y, e = next_edge(path[j])
                offset += 1 / (3 * A)
                A *= F(3, 2 ** e)
                t = j + 1 - i
                require(A * (path[i] + offset) == y, (m, i, j, "affine"))
                require(offset >= 1 - F(2, 3) ** t, (m, i, j, "strip"))
                counters["native_offset_segments"] += 1
    return counters


if __name__ == "__main__":
    print(json.dumps({**critical_grid_checks(), **true_postminimum_checks()},
                     sort_keys=True, indent=2))
