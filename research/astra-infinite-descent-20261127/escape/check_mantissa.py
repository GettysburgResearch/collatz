"""Exact finite checks for logarithmic-octave first-hit clock transfer."""

import argparse
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def run(n, steps):
    count = 0
    for _ in range(steps):
        odd = n % 2
        count += odd
        n = (3*n+1)//2 if odd else n//2
    return n, count


def scalar_step(state, bit):
    k, c = state
    p = (bit+c) % 2
    j = k+p-bit
    if j < 0:
        return 1, (1-3*c)//2
    return j, (3**p*c+p-3**j*bit)//2


def canonical(s, r):
    base, grade = run(r//3, s)
    other = r//(2**s)
    if grade <= 1:
        gap = 1-grade
        return gap, other-3**gap*base
    return grade-1, base-3**(grade-1)*other


def survival_table(initial, depth):
    states = Counter(initial)
    states.pop((0, 0), None)
    result = [sum(states.values())]
    for _ in range(depth):
        following = defaultdict(int)
        for state, count in states.items():
            for bit in (0, 1):
                following[scalar_step(state, bit)] += count
        following.pop((0, 0), None)
        states = following
        result.append(sum(states.values()))
    return result


def physical(s, L, cell):
    a, g = run(cell//3, L+s)
    b, h = run(cell//(2**s), L)
    return a == b and g == h+1


def fractions_for_menu(depth, direct):
    tables = []
    for s in (1, 2):
        period = 3*2**s
        table = survival_table([canonical(s, r) for r in range(period)], depth)
        for L in range(direct+1):
            whole = period*2**L
            failures = 0
            for cell in range(whole):
                good = physical(s, L, cell)
                failures += not good
                require(physical(s, L, cell+3*whole) == good, "binary cell lift")
            require(failures == table[L], "canonical counting and direct ordinary menu differ")
        tables.append(table)
    adjacent = survival_table([(0, 1)], depth)
    records = []
    for L in range(depth+1):
        p = [Fraction(t[L], 3*2**(L+s)) for s, t in enumerate(tables, 1)]
        adj = Fraction(adjacent[L], 2**L)
        records.append({"comparison_clock": L, "q_adjacent": str(adj),
                        "p_doubling_exponent_1": str(p[0]),
                        "p_doubling_exponent_2": str(p[1]), "p_max": str(max(p))})
    return records


def trajectory(z, deadline):
    result = [(z, 0)]
    for _ in range(deadline):
        x, g = result[-1]
        odd = x % 2
        result.append(((3*x+1)//2 if odd else x//2, g+odd))
    return result


def actual_octave(N, deadline):
    sources = [trajectory(z, deadline) for z in range(N, 2*N)]
    columns = []
    S_list = ({1}, {5, 7}, {2, 5, 13}, {N//3, N//2-1, N//2+1})
    for S in S_list:
        hits = [next(((m, g) for m, (y, g) in enumerate(row) if y in S), None)
                for row in sources]
        score_max = {}
        for a, b in ((1, 0), (0, 1), (1, 1), (2, 3)):
            counts = Counter(a*m+b*g for hit in hits if hit is not None for m, g in [hit])
            score_max[f"{a}clock+{b}grade"] = max(counts.values(), default=0)
        for L in (2, 6, 10):
            bad = coupling_bad = 0
            for cell in range(3*N, 6*N):
                s = 1 if cell < 4*N else 2
                a, b = cell//3-N, cell//(2**s)-N
                y, g = sources[a][L+s]
                z, h = sources[b][L]
                coupled = (y, g) == (z, h+1)
                coupling_bad += not coupled
                left, right = hits[a], hits[b]
                safe = ((left is None or left[0] > L+s) and
                        (right is None or right[0] > L))
                bad += not (safe and coupled)
                if coupled and safe and left is not None:
                    require(right == (left[0]-s, left[1]-1), "first-hit transfer")
            require(3*max(score_max.values()) <= 2*bad, "finite integer flux inequality")
            columns.append({"target_set": sorted(S), "comparison_clock": L,
                            "all_cells": 3*N, "failed_merger_cells": coupling_bad,
                            "failed_protected_cells": bad, "largest_score_atoms": score_max})
    return {"N": N, "deadline": deadline, "tests": columns}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--depth", type=int, default=16)
    parser.add_argument("--direct", type=int, default=9)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not 0 <= args.direct <= min(args.depth, 14) or not 1 <= args.depth <= 22:
        parser.error("select a scalar depth 1–22 and a direct depth 0–min(depth,14)")
    result = {"scope": "finite physical rows and exact finite scalar kernel only",
              "direct_checked_through": args.direct, "comparators": fractions_for_menu(args.depth, args.direct),
              "octaves": [actual_octave(N, 140) for N in (128, 512, 2048)]}
    data = json.dumps(result, indent=2)+"\n"
    if args.output:
        args.output.write_text(data)
    else:
        print(data, end="")


if __name__ == "__main__":
    main()
