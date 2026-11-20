#!/usr/bin/env python3
"""Independent small exact certificates for the symbolic-order review.

This program imports no author checker. Universal exclusions are deductions
in the written review; the finite moments are adversarial replay controls.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import comb
from pathlib import Path


def check(condition, message):
    if not condition:
        raise ValueError(message)


# (first row, second row, offset), transcribed from AYH Example 4.3.
LETTERS = {
    "a": ((1, 1), (1, 0), (0, 0)),
    "b": ((1, 3), (3, 4), (1, 1)),
    "c": ((1, 5), (0, 0), (0, 0)),
    "d": ((1, 0), (1, 0), (1, 1)),
    "e": ((7, 2), (2, 5), (2, 1)),
    "f": ((2, 1), (1, 1), (1, 0)),
    "g": ((2, 2), (2, 4), (0, 2)),
}
RULES = ("ad:d", "bd:gd", "ae:ea", "af:eb", "ag:fa", "be:fb",
         "bf:ga", "bg:gb", "ce:cb", "cf:caa", "cg:cab")


def evaluate(word, x, y):
    for letter in word[::-1]:
        row1, row2, offset = LETTERS[letter]
        x, y = row1[0] * x + row1[1] * y + offset[0], row2[0] * x + row2[1] * y + offset[1]
    return x, y


def coefficients(word):
    # An affine function is determined by zero and the two coordinate units.
    zero = evaluate(word, 0, 0)
    unit1, unit2 = evaluate(word, 1, 0), evaluate(word, 0, 1)
    return [[unit1[i] - zero[i], unit2[i] - zero[i], zero[i]] for i in range(2)]


def moments(n, digit, power):
    text = bin(n)[2:]
    # Splitting at the other digit is independent of the author's run parser.
    return sum(len(run) ** power for run in text.split(str(1 - digit)) if run)


def odd_map(n):
    result, steps = 3 * n + 1, 0
    while result % 2 == 0:
        result //= 2
        steps += 1
    return result, steps


def run():
    certificates = {}
    for rule in RULES:
        left, right = rule.split(":")
        a, b = coefficients(left), coefficients(right)
        delta = [[a[i][j] - b[i][j] for j in range(3)] for i in range(2)]
        certificates[rule] = delta
        if left != "af":
            check(all(entry >= 0 for row in delta for entry in row), "weak rule inequality")
            check(delta[0][2] >= 1, "strict constant")
    a, b = coefficients("af"), coefficients("eb")
    factor = max(Fraction(b[i][j], a[i][j]) for i in range(2) for j in range(3))
    check(factor == 26, "carry coefficient majorant")
    # Factor 25 fails on the second coordinate as its second input grows.
    check(evaluate("eb", 0, 100)[1] > 25 * evaluate("af", 0, 100)[1], "factor-25 rejection")

    # Leading-term cancellation of the universal degree argument uses only
    # nonnegative slacks; the final two inequalities force degree one.
    degree_rows = ((0, 0, -1, 1, 0), (0, 0, 0, 1, -1),
                   (-1, 1, 1, -1, 0), (1, -1, 0, -1, 1))
    check(all(sum(row[j] for row in degree_rows) == 0 for j in range(5)), "degree product identity")
    # -beta >= 0, beta-alpha >= 0, alpha+beta >= 0 have a
    # nonnegative combination identically zero, forcing each to vanish.
    run_rows = ((0, -1), (-1, 1), (1, 1))
    check(all(2 * run_rows[0][j] + run_rows[1][j] + run_rows[2][j] == 0 for j in range(2)), "energy cone identity")

    # Direct exact carry edges at parameters beyond the author's low-degree
    # moment menu, with moments 9, 12, and 17.
    moment_checks = edge_checks = 0
    for m in (3, 7, 19, 65, 131, 259, 1031):
        n, image = ((1 << (m + 2)) - 5) // 3, (1 << m) - 1
        check(odd_map(n) == (image, 2), "one-run physical edge")
        check(n.bit_length() == m + 1 and image.bit_length() == m, "one-run heights")
        edge_checks += 1
        for degree in (9, 12, 17):
            check(moments(n, 1, degree) == (m + 1) // 2, "one-run source moment")
            check(moments(n, 0, degree) == (m - 3) // 2 + 2 ** degree, "one-run source zero moment")
            check(moments(image, 1, degree) == m ** degree, "one-run target moment")
            moment_checks += 3
    for m in (4, 8, 20, 66, 132, 260, 1032):
        n, image = ((1 << (m + 1)) + 1) // 3, (1 << m) + 1
        check(odd_map(n) == (image, 1), "zero-run physical edge")
        check(n.bit_length() == m and image.bit_length() == m + 1, "zero-run heights")
        edge_checks += 1
        for degree in (9, 12, 17):
            check(moments(n, 1, degree) == m // 2 - 1 + 2 ** degree, "zero-run source moment")
            check(moments(n, 0, degree) == m // 2 - 1, "zero-run source zero moment")
            check(moments(image, 0, degree) == (m - 1) ** degree, "zero-run target moment")
            moment_checks += 3
    mersenne_leading = []
    for degree in range(2, 33):
        # Coefficients of m^(d-1) in (m+1)^d-m^d and
        # (m-1)^d+1-m^d. This tests the exact binomial identities.
        positive, negative = comb(degree, degree - 1), -comb(degree, degree - 1)
        check((positive, negative) == (degree, -degree), "leading Mersenne difference")
        mersenne_leading.append([degree, positive, negative])
    return {
        "schema": "collatz-creative-symbolic-independent/v1", "status": "PASS",
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "independent local affine certificates, two exact cone identities, and bounded high-degree run controls; universal theorems use written review",
        "rule_differences": certificates, "carry_majorant": str(factor),
        "factor_25_rejected": True, "ordinary_edges": edge_checks,
        "moment_checks": moment_checks, "moment_degrees": [9, 12, 17],
        "mersenne_leading_coefficients": mersenne_leading,
        "imports_author_checker": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--output", type=Path)
    modes.add_argument("--compare", type=Path)
    args = parser.parse_args()
    result = run()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        with args.output.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(rendered)
    if args.compare:
        check(args.compare.read_text(encoding="utf-8") == rendered, "frozen report mismatch")
    print(json.dumps({"status": "PASS", "ordinary_edges": result["ordinary_edges"],
                      "moment_checks": result["moment_checks"], "report_sha256": sha256(rendered.encode()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
