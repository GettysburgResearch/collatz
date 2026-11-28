"""Compute exact extrema of normalized ordinary first-arrival rows at bounded grades."""

import argparse
import json
from fractions import Fraction
from functools import lru_cache
from math import comb


def step(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def ladder_clocks(max_grade):
    y, m = 1, 0
    clocks = [0]
    for _ in range(max_grade):
        e = next(j for j in range(3, 7) if (2 ** j * y) % 9 in (4, 7))
        y = (2 ** e * y - 1) // 3
        m += e
        clocks.append(m)
    return clocks


def first_sources(y, m, d):
    values = [(y, 0)]
    for _ in range(m):
        nxt = []
        for z, grade in values:
            if 2 * z != y:
                nxt.append((2 * z, grade))
            if z % 3 == 2 and grade < d:
                parent = (2 * z - 1) // 3
                if parent != y:
                    nxt.append((parent, grade + 1))
        values = nxt
    sources = sorted(z for z, grade in values if grade == d)
    for z in sources:
        n, grade = z, 0
        for _ in range(m):
            if n == y:
                raise ArithmeticError("early forward visit")
            grade += n % 2
            n = step(n)
        if (n, grade) != (y, d):
            raise ArithmeticError("wrong forward row")
    return sources


def audit(max_grade):
    @lru_cache(maxsize=None)
    def lap(y):
        x, grade = y, 0
        for m in range(1, 2 * max_grade + 1):
            grade += x % 2
            x = step(x)
            if x == y:
                return grade, m
        return None

    power3 = [3 ** d for d in range(max_grade + 1)]
    clocks = ladder_clocks(max_grade)
    best = [Fraction(power3[d], 2 ** clocks[d]) for d in range(max_grade + 1)]
    winners = [[] for _ in best]
    last_test = [None for _ in best]
    rows = [[] for _ in best]
    m = 0
    while any(v is None for v in last_test):
        denom = 1 << m
        rows[0].append([1])
        for d in range(1, max_grade + 1):
            mod = power3[d]
            if m < d:
                rows[d].append([0] * mod)
            else:
                same = rows[d][m - 1]
                lower = rows[d - 1][m - 1]
                rows[d].append([same[2 * a % mod] +
                                (lower[((2 * a - 1) // 3) % (mod // 3)] if a % 3 == 2 else 0)
                                for a in range(mod)])
        for d in range(max_grade + 1):
            if m < d or last_test[d] is not None:
                continue
            majorant = Fraction(power3[d] * comb(m, d), denom)
            if m >= 2 * d and majorant < best[d]:
                last_test[d] = m - 1
                continue
            mod = power3[d]
            for a, total in enumerate(rows[d][m]):
                if total == 0:
                    continue
                y = a if a % 2 else a + mod
                weighted_total = mod * total
                while weighted_total * best[d].denominator >= denom * y * best[d].numerator:
                    first = total
                    cycle = lap(y)
                    if cycle:
                        c, h = cycle
                        if c <= d and h <= m:
                            first -= rows[d - c][m - h][y % power3[d - c]]
                    wt = Fraction(mod * first, denom * y)
                    if wt > best[d]:
                        best[d], winners[d] = wt, []
                    if wt == best[d]:
                        winners[d].append((y, m, first))
                    y += 2 * mod
        m += 1
    result = []
    for d, (weight, rows_winning, final_m) in enumerate(zip(best, winners, last_test)):
        if not rows_winning:
            raise ArithmeticError("missing maximizer")
        witnesses = []
        for y, m, expected in rows_winning:
            starts = first_sources(y, m, d)
            if len(starts) != expected:
                raise ArithmeticError("wrong exact first count")
            witnesses.append({"target": y, "clock": m, "sources": starts})
        # A strict grade/H threshold forces every maximizing label onto these actual paths.
        cutoff = int(Fraction(d + 3, 3) / weight) + 1
        menu = set()
        for q in range(1, cutoff + 1, 2):
            u = q
            for _ in range(d + 1):
                menu.add(u)
                a = 3 * u + 1
                u = a // (a & -a)
        if not all(w["target"] in menu for w in witnesses):
            raise ArithmeticError("maximizer outside the elementary target menu")
        result.append({"grade": d, "extreme": str(weight), "last_clock_tested": final_m,
                       "small_odd_cutoff": cutoff, "target_menu_size": len(menu),
                       "maximizers": witnesses})
    return {"maximum_grade": max_grade, "rows": result}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-grade", type=int, default=11)
    args = parser.parse_args()
    if not 0 <= args.max_grade <= 11:
        parser.error("choose a maximum grade from zero through eleven")
    print(json.dumps(audit(args.max_grade), indent=2))

