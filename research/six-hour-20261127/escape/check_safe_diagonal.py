"""Audit the positive ordinary compression, principal cells and finite joint hits."""

import argparse
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
import subprocess
import tempfile


def require(test, label):
    if not test:
        raise RuntimeError(label)


def future_edge(t):
    if t % 2 == 0:
        return 3 * t // 2, 1, 1
    if t % 8 == 7:
        return (9 * t + 1) // 8, 3, 2
    return None


def past_edge(t):
    if t % 3 == 0:
        return 2 * t // 3, 1, 1
    if t % 9 == 8:
        return (8 * t - 1) // 9, 3, 2
    return None


def odd_edge(x):
    v = 3 * x + 1
    low = v & -v
    return v // low, low.bit_length() - 1


def clears(t, future):
    state, precision = t, 1
    while precision < t:
        edge = (future_edge if future else past_edge)(state)
        if edge is None:
            return False
        state, h, v = edge
        precision *= 2**h if future else 3**v
    return True


def exit_record(t):
    state, h, v, n = t, 0, 0, 0
    while (edge := future_edge(state)) is not None:
        state, dh, dv = edge
        h += dh
        v += dv
        n += 1
        require(n <= 1000, "finite control horizon exhausted")
    return {"state": t, "tokens": n, "odd_departures": v, "dyadic_clock": h,
            "first_rejected_token_entrance": state}


def principal_controls(depth):
    # Lift the low input bits forward here, independently of the backwards
    # terminal formula in check_geodesic.py.
    parents = [((), 1, 1, 0, 0)]
    rows = []
    for n in range(1, depth + 1):
        q = 3**n
        current, cells = [], set()
        for word, source, terminal, h, carry in parents:
            for e in (1, 2):
                if e == 2 and word[-1:] == (2,):
                    continue
                lifts = []
                for j in range(2**e):
                    seed = source + j * 2**(h+1)
                    old_terminal = terminal + 2*3**(n-1)*j
                    new_terminal, paid = odd_edge(old_terminal)
                    if paid == e:
                        lifts.append((seed, new_terminal))
                require(len(lifts) == 1, "unique low-bit lift")
                m, y = lifts[0]
                h1 = h + e
                c1 = 3*carry + 2**h
                require(0 < y < 2*q and y % 2 == 1, "principal terminal")
                require(q*m + c1 == 2**h1*y, "affine reconstruction")
                require(y % q not in cells, "ternary decoding")
                cells.add(y % q)
                require(Fraction(c1, q) <= 7, "uniform additive correction")
                if m != source:
                    require(2*y >= q and m >= source + 2**(h+1), "jump floor")
                current.append((word+(e,), m, y, h1, c1))
        rows.append({"depth": n, "distinct_principal_cells": len(cells),
                     "least_seed": min(m for _, m, _, _, _ in current)})
        parents = current
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ternary-depth", type=int, default=20)
    args = parser.parse_args()
    require(1 <= args.ternary_depth <= 45, "unsupported search depth")
    cpp = Path(__file__).with_name("safe_diagonal.cpp")
    with tempfile.TemporaryDirectory() as tmp:
        exe = Path(tmp, "diagonal")
        subprocess.run(["c++", "-std=c++17", "-O3", "-Wall", "-Wextra", "-Werror",
                        str(cpp), "-o", str(exe)], check=True)
        lines = subprocess.check_output([str(exe), str(args.ternary_depth)], text=True)
    hits, shells = [], []
    for line in lines.splitlines():
        op, *values = line.split()
        if op == "hit":
            _, y = map(int, values)
            require(clears(y, False) and clears(y, True), "positive joint hit replay")
            hits.append(y)
        elif op == "shell":
            m, candidates, count = map(int, values)
            shells.append([m, candidates, count])
        else:
            raise RuntimeError("unexpected C++ control row")
    require(len(hits) == len(set(hits)), "duplicate joint hit")
    check_m = min(10, args.ternary_depth)
    observed = Counter()
    brute_hits = []
    for t in range(1, 3**check_m + 1):
        if clears(t, False):
            shell, power = 0, 1
            while power < t:
                power *= 3
                shell += 1
            observed[shell] += 1
            if clears(t, True):
                brute_hits.append(t)
        edge = future_edge(t)
        y, e = odd_edge(6*t-1)
        if e == 2:
            y, e1 = odd_edge(y)
            valid = e1 == 1
        else:
            valid = e == 1
        require(valid == (edge is not None), "exact token domain")
        if valid:
            require(6*edge[0]-1 == y, "compressed positive endpoint")
            require(past_edge(edge[0]) == (t, edge[1], edge[2]), "positive inverse")
    require(sorted(y for y in hits if y <= 3**check_m) == brute_hits,
            "complete direct integer scan")
    for m, candidates, count in shells:
        if m <= check_m:
            require(candidates == observed[m], "complete direct reverse candidate count")
        require(count == sum(3**(m-1) < y <= 3**m for y in hits), "shell hit count")
    require(22**3 > 22**2*15 + 15**3 and 22**9 < 32*15**9, "dyadic dimension")
    require(13**2 > 13*8+8**2 and 13**9 < 81*8**9, "ternary dimension")
    print(json.dumps({"scope": "finite unshifted double height test; future exit for listed hits",
                      "ternary_depth": args.ternary_depth,
                      "height_inclusive": 3**args.ternary_depth,
                      "direct_all_integer_crosscheck_through": 3**check_m,
                      "principal_controls": principal_controls(15),
                      "shells_depth_candidates_hits": shells,
                      "hits": [exit_record(t) for t in sorted(hits)]}, indent=2))


if __name__ == "__main__":
    main()
