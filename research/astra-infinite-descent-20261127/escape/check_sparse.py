"""Exact bounded checks for unit-valued inverse clock rows and discrete poles."""

import argparse
import json
from math import comb
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def unit_residues(modulus):
    return [v for v in range(1, modulus) if v % 3]


def run_checks(max_grade, extra):
    moduli = [3 ** (d + 1) for d in range(max_grade + 1)]
    units = [unit_residues(n) for n in moduli]
    index = [{v: i for i, v in enumerate(us)} for us in units]
    doubled = [[index[d][2 * y % moduli[d]] for y in us] for d, us in enumerate(units)]
    inverse_one = [[]]
    for d in range(1, max_grade + 1):
        inverse_one.append([
            index[d - 1][((2 * y - 1) // 3) % moduli[d - 1]]
            if 2 * y % 9 in (4, 7) else None for y in units[d]
        ])
    # The full dth row needs d+1 ternary digits because inverse sources must be units.
    rows = [[[int(d == 0) for _ in us]] for d, us in enumerate(units)]
    highest_clock = 2 * 3 ** max_grade + extra + max_grade
    haar_identities = 0
    direct_words = 0
    for m in range(1, highest_clock + 1):
        rows[0].append([0] * len(units[0]))
        for d in range(1, max_grade + 1):
            prev, prev_grade = rows[d][-1], rows[d - 1][m - 1]
            row = [prev[j] + (prev_grade[i] if i is not None else 0)
                   for j, i in zip(doubled[d], inverse_one[d])]
            rows[d].append(row)
            expected = 2 * comb(m - 1, d - 1) if d <= m else 0
            require(sum(row) == expected, "finite Haar path count")
            haar_identities += 1
            if 1 <= d <= m <= 10:
                for i, y in enumerate(units[d]):
                    ordinary = y if y % 2 else y + moduli[d]
                    count = direct_count(ordinary, m, d)
                    require(row[i] == count, "ordinary recursion disagrees with residue count")
                    direct_words += 1

    cases = []
    for d in range(1, max_grade + 1):
        period = 2 * 3 ** d
        tested = 0
        for m in range(1, extra + 1):
            for i in range(len(units[d])):
                delta = sum((-1) ** (d - 1 - j) * comb(d - 1, j)
                            * (rows[d][m + j + period][i] - rows[d][m + j][i])
                            for j in range(d))
                require(delta == 0, "period-shifted (d-1)st difference")
                tested += 1
        example_m = period + extra
        row = rows[d][example_m]
        cases.append({"grade": d, "target_precision": moduli[d], "period": period,
                      "finite_difference_checks": tested, "example_clock": example_m,
                      "min_odd_sources": min(row), "max_odd_sources": max(row)})
    return {"exact_haar_identities": haar_identities, "ordinary_cross_checks": direct_words,
            "highest_clock": highest_clock, "rows": cases}


def direct_count(y, total, depth):
    if depth == 0:
        return int(total == 0)
    count = 0
    for e in range(1, total - depth + 2):
        a = (1 << e) * y
        if a % 9 in (4, 7):
            child = (a - 1) // 3
            require(child > 0 and child % 2 == 1 and child % 3 != 0, "ordinary inverse edge")
            count += direct_count(child, total - e, depth - 1)
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-grade", type=int, default=5)
    parser.add_argument("--extra", type=int, default=19)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not 1 <= args.max_grade <= 6 or args.extra < 1:
        parser.error("use grade 1 through 6 and a positive number of additional clocks")
    data = json.dumps(run_checks(args.max_grade, args.extra), indent=2) + "\n"
    if args.output:
        args.output.write_text(data)
    else:
        print(data, end="")


if __name__ == "__main__":
    main()
