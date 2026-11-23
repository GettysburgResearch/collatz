#!/usr/bin/env python3
"""Exact finite controls for the sparse automatic carry exclusions.

The 2-adic irrationality proof is written in ARITHMETIC_TOWER.md.
No actual infinite scalar is computed and no orbit is assumed to
terminate. Every check stays active with python -O.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import gcd
import json


class Checks:
    def __init__(self):
        self.counts = Counter()

    def need(self, condition, label):
        if not condition:
            raise RuntimeError(label)
        self.counts[label] += 1


def v2_int(n):
    if not n:
        raise ValueError("finite valuation required")
    n = abs(n)
    return (n & -n).bit_length() - 1


def v2_rat(x):
    x = F(x)
    return v2_int(x.numerator) - v2_int(x.denominator)


def odd_step(q):
    if q <= 0 or not q % 2:
        raise ValueError("positive odd ordinary source required")
    value = 3 * q + 1
    gap = v2_int(value)
    return value // 2**gap, gap


def symbol(j, k):
    if j < 0 or k < 1:
        raise ValueError("nonnegative index and positive bit cap required")
    return int(j > 0 and j.bit_count() <= k)


def gaps(script):
    return [g for s in script for g in (2 - s, 1 + 3 * s)]


def cylinder_source(script, lift=0):
    word = gaps(script)
    if not word or lift < 0:
        raise ValueError("nonempty word and nonnegative lift required")
    coefficient, constant, clock = 1, 0, 0
    for gap in word:
        constant = 3 * constant + 2**clock
        coefficient *= 3
        clock += gap
    modulus = 2**(clock + 1)
    source = ((2**clock - constant) * pow(coefficient, -1, modulus)) % modulus
    return source + lift * modulus, clock


def replay(script, source, checks):
    q = source
    boundary = [q + 7]
    partial, clock = F(), 0
    paid_count, paid_series = 0, F()
    for j, s in enumerate(script):
        old_q = q
        for offset, expected in enumerate((2 - s, 1 + 3 * s)):
            successor, gap = odd_step(q)
            checks.need(gap == expected, "every prescribed odd gap is actual")
            checks.need(2**gap * successor == 3 * q + 1,
                        "complete positive ordinary edge")
            partial += F(gap, 3**(2*j + offset + 1))
            clock += gap
            q = successor
        x, y = old_q + 7, q + 7
        checks.need(8 * 4**s * y == 9 * x + 166 * s,
                    "shifted block retains additive constant166")
        checks.need(8 * y <= 9 * x,
                    "positive ordinary block height growth")
        boundary.append(y)
        checks.need(8**(j + 1) * y <= 9**(j + 1) * (source + 7),
                    "unchanged-source full prefix height")
        if s:
            paid_series += F(8, 9)**j * 4**paid_count
            paid_count += 1
        coefficient = F(8, 9)**(j + 1) * 4**paid_count
        checks.need(F(source + 7) == coefficient * y - F(166, 9) * paid_series,
                    "finite inverse identity with actual endpoint")
        checks.need(partial + F(7, 8 * 3**(2*j + 2)) == F(7, 8),
                    "symbolic scalar retained as candidate tail only")
    for j in range(len(script) + 1):
        run = 0
        while j + run < len(script) and not script[j + run]:
            run += 1
        for m in range(run + 1):
            x = boundary[j]
            checks.need(8**m * boundary[j + m] == 9**m * x,
                        "literal unpaid-run shifted identity")
            checks.need(x % 2**(3*m + 1) == 0,
                        "terminal oddness funds full binary divisor")
            checks.need(2**(3*m + 1) * 8**j <= 9**j * (source + 7),
                        "exact same-source unpaid-run window")
    checks.need(clock == 3 * len(script) + 2 * sum(script),
                "complete block clock")
    return {"source": source, "endpoint": q, "clock": clock,
            "source_bits": source.bit_length(), "blocks": len(script)}


def mismatch_budget(q, k):
    if q <= 0 or not q % 2 or not 1 <= k <= 4:
        raise ValueError("positive odd source and bit cap1 through4 required")
    bits = (q + 7).bit_length()
    coefficient = 35 - 2**(k + 1)
    h = 1
    while coefficient * h < 11 * bits + 24:
        h *= 2
    return 2**(k + 1) * h, h, bits, coefficient


def first_mismatch(q, k, budget):
    for i in range(budget):
        s = symbol(i // 2, k)
        expected = 2 - s if i % 2 == 0 else 1 + 3 * s
        q, actual = odd_step(q)
        if actual != expected:
            return i + 1
    return None


def truncation(positions, r):
    last = positions[r]
    denominator = 9**last
    numerator = sum(4**i * 8**positions[i] * 9**(last - positions[i])
                    for i in range(r + 1))
    return numerator, denominator


def run_checks():
    checks = Checks()
    checks.need(9**11 < 2**35, "exact eleventh-power height comparison")
    checks.need(8**16 > 9**15, "largest admitted automatic family is lacunary")
    checks.need(8**32 < 9**31, "displayed fifth-family gap is not admitted")

    word_count = cylinder_count = 0
    cylinder_rows = []
    for length in range(1, 7):
        for word in product((0, 1), repeat=length):
            script = list(word)
            word_count += 1
            for lift in (0, 1):
                source, clock = cylinder_source(script, lift)
                checks.need(source > 0 and source % 2 == 1,
                            "complete cylinder is positive and odd")
                row = replay(script, source, checks)
                checks.need(row["clock"] == clock, "cylinder clock replay")
                cylinder_count += 1

    for k in range(1, 5):
        for h in (1, 2, 4, 8):
            left, right = (2**k - 1) * h, 2**k * h
            checks.need(symbol(left, k) == symbol(right, k) == 1,
                        "two specified endpoints are paid")
            checks.need(all(symbol(j, k) == 0 for j in range(left + 1, right)),
                        "specified paid endpoints are consecutive")
            checks.need(8**right > 9**left,
                        "exact automatic-family lacunary height gain")
            script = [symbol(j, k) for j in range(right)]
            source, _ = cylinder_source(script)
            row = replay(script, source, checks)
            cylinder_rows.append({"k": k, "h": h, "blocks": right,
                                  "source": str(source),
                                  "source_bits": row["source_bits"]})

    budgets_checked = 0
    maximum_match = {k: 0 for k in range(1, 5)}
    sources = list(range(1, 4096, 2))
    sources.extend(int(row["source"]) for row in cylinder_rows)
    for k in range(1, 5):
        for source in sources:
            budget, h, bits, coefficient = mismatch_budget(source, k)
            checks.need(h > 1 and h & (h - 1) == 0,
                        "budget uses a positive power of two")
            checks.need(coefficient * h >= 11 * bits + 24 and
                        coefficient * (h // 2) < 11 * bits + 24,
                        "budget power is least admissible")
            checks.need(budget * coefficient < 2**(k + 2) * (11 * bits + 24),
                        "linear bit-length budget comparison")
            mismatch = first_mismatch(source, k, budget)
            checks.need(mismatch is not None and mismatch <= budget,
                        "fixed positive source mismatches within proved budget")
            maximum_match[k] = max(maximum_match[k], mismatch - 1)
            budgets_checked += 1

    position_families = [list(range(26)), [2**r for r in range(10)],
                         [r*r + r + 1 for r in range(26)]]
    position_families.extend([[j for j in range(1, 200) if symbol(j, k)]
                             for k in range(1, 5)])
    height_rows = []
    valuation_count = rational_checks = 0
    for positions in position_families:
        for r in range(min(8, len(positions) - 3)):
            numerator, denominator = truncation(positions, r)
            checks.need(0 < numerator < 4**(r + 1) * denominator,
                        "ordinary partial numerator height")
            checks.need(gcd(numerator, denominator) == 1,
                        "complete ternary denominator retained")
            next_num, next_den = truncation(positions, r + 2)
            tail = F(next_num, next_den) - F(numerator, denominator)
            expected_v = 2*(r + 1) + 3*positions[r + 1]
            checks.need(v2_rat(tail) == expected_v,
                        "unique first omitted valuation cannot cancel")
            valuation_count += 1
            for a in range(-12, 13):
                for b in range(1, 16, 2):
                    height = abs(a) + b
                    defect = a * denominator - b * numerator
                    checks.need(abs(defect) < height * 4**(r + 1) * denominator,
                                "fixed rational candidate ordinary height")
                    if 8**positions[r + 1] >= height * 9**positions[r]:
                        if defect:
                            checks.need(v2_int(defect) < expected_v,
                                        "rational height cannot fund required tail valuation")
                        else:
                            checks.need(tail != 0,
                                        "truncation equality is not infinite equality")
                    rational_checks += 1
            height_rows.append({"r": r, "last_paid": positions[r],
                                "next_paid": positions[r + 1],
                                "next_tail_valuation": expected_v})

    for r in range(8):
        z = F(8, 9)
        partial = sum((4**i * z**(2**i) for i in range(r + 1)), F())
        scaled = z + 4 * sum((4**i * (z*z)**(2**i) for i in range(r)), F())
        checks.need(partial == scaled, "finite Mahler functional equation")

    return {"status": "PASS", "exact_checks": sum(checks.counts.values()),
            "checks_by_category": dict(sorted(checks.counts.items())),
            "arbitrary_binary_words": word_count,
            "arbitrary_positive_cylinders": cylinder_count,
            "automatic_positive_cylinders": cylinder_rows,
            "fixed_source_budget_cases": budgets_checked,
            "longest_matching_odd_prefix_in_controls": maximum_match,
            "finite_tail_valuation_cases": valuation_count,
            "fixed_rational_height_cases": rational_checks,
            "height_samples": height_rows,
            "scope": "finite exact ordinary realizations, mismatch budgets and arithmetic controls for the written 2-adic irrationality proof",
            "unproved": "arbitrary bounded-carry or automatic-script exclusion and full denominator-eight rigidity"}


if __name__ == "__main__":
    print(json.dumps(run_checks(), sort_keys=True, indent=2))
