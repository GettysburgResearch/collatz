#!/usr/bin/env python3
"""Independent ordinary-word and rational-series audit of OCC-001/004.

Does not import the production checker. Acceleration is reconstructed by
maximal repetition of its literal parity word, not its affine formula.
Logarithms use rational truncated series, then round once to a binary scale.
Uncomputed original sources are retained through analytic upper tails.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from functools import cache
from hashlib import sha256
import json
from math import lcm
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCALE = 2**128
SERIES_TERMS = 20


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


def ceil_div(a, b):
    return -((-a) // b)


def valuation(n, p):
    check(n != 0, "nonzero valuation input")
    n, v = abs(n), 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def active(n):
    return 0 if n % 2 == 0 else valuation(n + 1, 2)


@cache
def rank(n):
    if n == 1:
        return 0
    h = valuation(2 * n + 1, 3)
    values = {}
    # Extra modes independently check the compact source menu on this scope.
    for a in range(max(8, h + 2) + 1):
        z = (3**a - 2**(a + 1)) * n + 3**a - 2**a
        values[a] = z * z // 3**valuation(z, 3)
    answer = min(values.values())
    compact = (0, 1, 2, h) if h >= 3 else (0, 1, 2)
    check(answer == min(values[a] for a in compact), "finite rank-menu reconstruction")
    check(n - 1 <= answer <= n * n, "rank bounds")
    return answer


@cache
def acceleration(n):
    if n == 1:
        return 1
    a, current = active(n), n
    while current > 1 and active(current) == a:
        for position in range(a + 1):
            check((current % 2 == 1) == (position < a), "literal repeated parity word")
            current = shortcut(current)
    return current


@cache
def unsafe(n):
    return n > 1 and 4 * rank(acceleration(n)) > rank(n)


@cache
def ordinary_return(n):
    if n == 1:
        return 1
    check(unsafe(n), "unsafe return domain")
    y = acceleration(n)
    while y != 1 and not unsafe(y):
        z = acceleration(y)
        check(4 * rank(z) <= rank(y), "quarter-safe strict rank drop")
        y = z
    return y


def rational_log_unit(n, d):
    z = Fraction(n - d, n + d)
    check(0 <= z <= Fraction(1, 3), "rational log range")
    power, partial = z, Fraction(0)
    for j in range(SERIES_TERMS):
        partial += power / (2 * j + 1)
        power *= z * z
    lower = 2 * partial
    remainder = 2 * power / ((2 * SERIES_TERMS + 1) * (1 - z * z))
    return lower, lower + remainder


LN2 = rational_log_unit(2, 1)


@cache
def log_interval(n, d=1):
    check(n > 0 and d > 0, "positive logarithm input")
    k = n.bit_length() - d.bit_length()
    if (n < d * 2**k) if k >= 0 else (n * 2**(-k) < d):
        k -= 1
    nn, dd = (n, d * 2**k) if k >= 0 else (n * 2**(-k), d)
    lo, hi = rational_log_unit(nn, dd)
    if k >= 0:
        lo, hi = lo + k * LN2[0], hi + k * LN2[1]
    else:
        lo, hi = lo + k * LN2[1], hi + k * LN2[0]
    return (SCALE * lo.numerator // lo.denominator,
            ceil_div(SCALE * hi.numerator, hi.denominator))


def entropy_point(x):
    if x == 0:
        return 0, 0
    lo, hi = log_interval(x, SCALE)
    return -x * hi // SCALE, ceil_div(-x * lo, SCALE)


def entropy(mass):
    lo = hi = 0
    for a, b in mass.values():
        check(0 <= a <= b and 3 * b < SCALE, "increasing entropy domain")
        lo += entropy_point(a)[0]
        hi += entropy_point(b)[1]
    return lo, hi


@cache
def psi_interval(r):
    a, b = log_interval(r + 6)
    return SCALE + log_interval(a, SCALE)[0], SCALE + log_interval(b, SCALE)[1]


def push(mass):
    out = defaultdict(lambda: [0, 0])
    for n, (a, b) in mass.items():
        y = ordinary_return(n)
        out[y][0] += a
        out[y][1] += b
    return dict(out)


def as_rational(x, denominator=SCALE):
    value = Fraction(x, denominator)
    return f"{value.numerator}/{value.denominator}"


def entropy_audit():
    cutoff = 65536
    starts = [u for u in range(2, cutoff + 1) if unsafe(u)]
    mass = {u: (SCALE // (u * (u + 1)), ceil_div(SCALE, u * (u + 1))) for u in starts}
    check(3 * (sum(v[1] for v in mass.values()) + ceil_div(SCALE, cutoff + 1)) < SCALE,
          "full original mass below one third")
    for _ in range(8):
        mass = push(mass)
    entropy8 = entropy(mass)
    charge_lo = charge_hi = 0
    for n, (lo, hi) in mass.items():
        if n > 1:
            p, q = psi_interval(rank(n))
            charge_lo += SCALE * lo // q
            charge_hi += ceil_div(SCALE * hi, p)
    entropy9 = entropy(push(mass))
    omitted_entropy = ceil_div(2 * (log_interval(cutoff + 2)[1] + SCALE), cutoff + 1)
    full_j_lo = max(0, entropy8[0] - entropy9[1] - omitted_entropy)
    full_j_hi = entropy8[1] - entropy9[0] + omitted_entropy
    omitted_charge = ceil_div(SCALE * SCALE, (cutoff + 1) * psi_interval(1)[0])
    gap = charge_lo - full_j_hi
    check(Fraction(gap, SCALE) > Fraction(265165623, 10**12), "whole-source j=8 strict gap")
    return {"original_source_cutoff": cutoff, "unsafe_sources": len(starts), "return_index": 8,
            "whole_source_charge_lower": as_rational(charge_lo),
            "whole_source_charge_upper": as_rational(charge_hi + omitted_charge),
            "whole_source_entropy_drop_lower": as_rational(full_j_lo),
            "whole_source_entropy_drop_upper": as_rational(full_j_hi),
            "charge_minus_drop_lower": as_rational(gap),
            "gap_exceeds_0.000265165623": True}


def capacity_audit(production):
    cutoff = 8192
    common = lcm(*range(1, cutoff + 2))
    capacity = defaultdict(int)
    sources = longest = 0
    for u in range(2, cutoff + 1):
        if not unsafe(u):
            continue
        sources += 1
        check(common % (u * (u + 1)) == 0, "exact source denominator")
        weight, n, seen = common // (u * (u + 1)), u, set()
        for _ in range(64):
            if n == 1 or n in seen:
                break
            seen.add(n)
            capacity[n] += weight
            n = ordinary_return(n)
        check(n == 1, "finite source scope resolved at one")
        longest = max(longest, len(seen))
    check(sources == 2941 and longest == 37, "source scope and maximum return count")
    witness = production["capacity"]["witness"]
    for endpoint, key in ((31, "source_capacity"), (121, "endpoint_capacity")):
        lower = Fraction(capacity[endpoint], common)
        upper = lower + Fraction(1, cutoff + 1)
        check(lower == Fraction(witness[key]["lower"]), "independent exact capacity lower")
        check(upper == Fraction(witness[key]["upper"]), "independent exact capacity upper")
    lower_x, upper_y = capacity[31], capacity[121] + common // (cutoff + 1)
    check(lower_x**2 * 121 > upper_y**2 * 31, "all-s compactification obstruction")
    check(lower_x**5 * common**2 > 5000 * upper_y**7, "all-c compactification obstruction")
    path, n = [], 31
    while n != 1:
        check(n not in path, "finite witness remains simple")
        path.append(n)
        n = ordinary_return(n)
    path.append(1)
    check(path == witness["known_convergent_B_path"], "literal-word witness path")
    check(rank(31) == 144 and rank(121) == 1764, "witness ranks")
    patch = {n: 150 for n in path[1:-1]}
    defect = defaultdict(int, patch)
    for n, value in patch.items():
        y = ordinary_return(n)
        if y != 1:
            defect[y] -= value
    check({n: v for n, v in defect.items() if v} == {121: 150}, "finite Poisson repair")
    return {"original_source_cutoff": cutoff, "unsafe_sources": sources,
            "maximum_return_count": longest, "exact_capacity_bounds_match_production": True,
            "all_s_at_least_one_half_failure": True, "all_c_greater_than_one_failure": True,
            "witness_path": path, "repair_support": len(patch), "repair_mass": sum(patch.values())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument("--compare", type=Path)
    args = parser.parse_args()
    source_paths = ["research/creative-closure-20261120/occupation.md",
                    "experiments/creative_occupation.py",
                    "reports/2026-11-20-creative-closure/occupation-report.json"]
    hashes = {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in source_paths}
    production = json.loads((ROOT / source_paths[2]).read_text(encoding="utf-8"))
    entropy_result = entropy_audit()
    capacity_result = capacity_audit(production)
    report = {"schema": "creative-occupation-independent-five-review-v1", "status": "PASS",
              "reviewed_sha256": hashes, "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "arithmetic": {"binary_scale_exponent": 128, "rational_log_terms": SERIES_TERMS},
              "entropy": entropy_result, "capacity": capacity_result,
              "all_time_occupation_upper_claimed": False}
    serialized = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        with args.output.open("x", encoding="utf-8") as stream:
            stream.write(serialized)
    elif args.compare:
        check(json.loads(args.compare.read_text(encoding="utf-8")) == report, "independent frozen report")
    else:
        print(serialized, end="")
    print("PASS: independently reconstructed ordinary words, entropy gap, capacities, and finite repair")


if __name__ == "__main__":
    main()
