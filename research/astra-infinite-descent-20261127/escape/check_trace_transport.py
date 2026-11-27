"""Exact bounded forward and inverse checks for the stopped-trace variation proof."""

import argparse
import json
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def selector(x):
    return x % 3 if x % 2 else 0


def oddpart(x):
    r = (x & -x).bit_length() - 1
    return x >> r, r


def physical_rows(x, depth):
    y, clock = oddpart(x)
    for d in range(depth+1):
        h = F(3**d, 2**clock*y)
        yield d, y, clock, h*x, h/(3*y+1)
        y, e = oddpart(3*y+1)
        clock += e


def inverse_paths(y, d, X):
    if d == 0:
        if y < X and y % 3:
            yield y, 0
        return
    # In the remaining d-1 forward odd moves a source < X cannot exceed 2^(d-1) X.
    cap = 2**(d-1)*X
    lift = 2*y
    e = 1
    while lift <= 3*cap+1:
        if lift % 9 in (4, 7):
            for x, clock in inverse_paths((lift-1)//3, d-1, X):
                yield x, clock+e
        lift *= 2
        e += 1


def direct_inverse(X, Y, depth):
    rows = defaultdict(dict)
    total_laps = 0
    for x in range(1, X, 2):
        if not selector(x):
            continue
        seen = set()
        for d, y, clock, _, _ in physical_rows(x, depth):
            if y < Y:
                rows[d, y][x] = clock
                total_laps += y in seen
            seen.add(y)
    keys = paths = marked = 0
    for y in range(1, Y, 2):
        for d in range(depth+1):
            actual = rows[d, y]
            inv = list(inverse_paths(y, d, X)) if y % 3 else []
            require(len(inv) == len(set(x for x, _ in inv)), "duplicate inverse source at fixed grade")
            require(dict(inv) == actual, "all-visit ordinary/inverse path mismatch")
            raw = sum((F(selector(x)*3**d, 2**m) for x, m in inv), F(0))
            physical = sum((F(selector(x)*3**d, 2**m*y*(3*y+1)) for x, m in actual.items()), F(0))
            require(raw/(y*(3*y+1)) == physical, "PR193 original row normalization")
            for x, m in inv:
                if d > 0 and F(x*3**d, 2**m*y) <= F(1, d):
                    marked += 1
            keys += 1
            paths += len(inv)
    return {"sources_below": X, "targets_below": Y, "max_grade": depth,
            "complete_compared_rows": keys, "path_matches": paths,
            "return_visits_included": total_laps, "endpoint_band_matches": marked}


def loss_checks(seeds, D):
    threshold_tests = degree_tests = 0
    for x in seeds:
        rows = list(physical_rows(x, D+1))
        for a, b in zip(rows, rows[1:]):
            require(x*a[4] == a[3]-b[3], "actual odd loss telescope")
            degree_tests += 1
        for h in (F(1), F(1, 2), F(1, D), F(1, 2**20)):
            s = sum((k[4]*x for k in rows[:-1] if k[3] <= h), F(0))
            require(s <= h, "actual endpoint-band charge")
            threshold_tests += 1
    return {"seeds": seeds, "max_grade": D, "step_identities": degree_tests,
            "band_tests": threshold_tests}


def run(x, h):
    g = 0
    for _ in range(h):
        odd = x % 2
        g += odd
        x = (3*x+1)//2 if odd else x//2
    return x, g


def octave(N, L, D):
    rows = defaultdict(lambda: F(0))
    for x in range(N, 2*N):
        for d, y, _, _, loss in physical_rows(x, D):
            rows[d, y] += loss
    keys = set(rows) | {(d+1, y) for d, y in rows if d < D}
    variation = sum((abs(rows[d, y]-rows[d-1, y]) for d, y in keys), F(0))
    bad = 0
    for cell in range(3*N, 6*N):
        s = 1 if cell < 4*N else 2
        low, grade = run(cell//3, L+s)
        high, other = run(cell//2**s, L)
        bad += (low, grade) != (high, other+1)
    # Integral of dt/t on an octave is log(2) < 1. A complete bad cell costs <=1/(3N).
    bound = 2*F(N+1, N)*(F(bad, 3*N)+F((L+3)*2**(L+2), 3*N))
    require(variation <= bound, "complete truncated grade-target variation bound")
    return {"N": N, "comparison_clock": L, "tested_grades_0_through": D,
            "bad_cells": bad, "cells": 3*N, "variation_floor_scaled_1e8": int(10**8*variation),
            "rational_majorant": str(bound)}


def signed_cones():
    numerators = (0, 1, 2, 0, 4, -10, 0, -5, 8)
    def delta(x):
        return F(numerators[x % 9], 7)
    def signed(x):
        return F(3, 2)*((x % 9 == 8)-(x % 9 == 5))
    table = cones = coordinates = 0
    for u in range(1, 36, 2):
        first = sum((F(3, 2**e) * (((2**e*u-1)//3) % 3)
                     for e in range(1, 7) if (2**e*u-1) % 3 == 0), F(0))*F(64, 63)
        require(first-(u % 3) == delta(u), "single exact six-exponent period")
        table += 1
    for u in range(1, 85, 2):
        base = list(physical_rows(u, 9))
        total = F(0)
        for r in range(12):
            x = 2**r*u
            require(signed(x) == delta(x)-delta(2*x)/2, "all-parity signed density")
            total += signed(x)/2**r
            require(total == delta(u)-delta(2*x)/2**(r+1), "finite cone boundary")
            cones += 1
            for (d,y,m,b,v), (j,z,n,a,w) in zip(base, physical_rows(x, 9)):
                require((d,y,m+r,b,v/2**r) == (j,z,n,a,w), "physical dyadic lift")
                coordinates += 1
    return {"exact_period_rows": table, "finite_cone_boundaries": cones,
            "ordinary_lift_coordinates": coordinates}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    results = {"scope": "bounded all-visit normalization and complete finite octave identities",
               "forward_inverse": direct_inverse(257, 129, 8),
               "signed_gap_three": signed_cones(),
               "loss": loss_checks([1, 2, 3, 5, 7, 11, 27, 54, 55, 97, 871], 140),
               "octaves": [octave(N, L, 30) for N, L in ((32, 2), (128, 3), (512, 4))]}
    data = json.dumps(results, indent=2)+"\n"
    if args.output:
        args.output.write_text(data)
    else:
        print(data, end="")


if __name__ == "__main__":
    main()
