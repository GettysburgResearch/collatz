#!/usr/bin/env python3
"""Independent bounded replay for the separately reconstructed GCL proofs."""

from fractions import Fraction
from hashlib import sha256
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NOTE = ROOT / "research/global-closure-20261120/closing-attempts.md"
NOTE_SHA256 = "956ffcb0d70edfc9caf94cbddeada8259088cd6c187a068fdd798bbfd0da723a"


def require(value, message):
    if not value:
        raise ValueError(message)


def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def odd_event(n):
    require(n > 0 and n % 2, "odd-map source")
    m, g = 3 * n + 1, 0
    while m % 2 == 0:
        m //= 2
        g += 1
    return m, g


def first_hit(n, cap=10000):
    d = o = 0
    while n != 1 and d < cap:
        o += n % 2
        d += 1
        n = T(n)
    require(n == 1, "bounded replay did not certify a first hit")
    return d, o


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument("--compare", type=Path)
    args = parser.parse_args()
    require(sha256(NOTE.read_bytes()).hexdigest() == NOTE_SHA256, "reviewed note changed")

    shifted_cases = 0
    for a in range(2, 81):
        x = (4 ** a - 1) // 3
        require(3 * x + 1 == 4 ** a and x % 2 == 1, "antecedent identity")
        require((x % 3 == 0) == (a % 3 == 0), "antecedent unit guard")
        require(first_hit(x) == (2 * a, 1), "antecedent first-hit clocks")
        y, exponents = 5 * x, []
        for _ in range(2 * a - 1):
            y, g = odd_event(y)
            exponents.append(g)
        require(exponents == [2] + [1] * (2 * a - 3) + [3], "shifted-power parity word")
        require(sum(exponents) == 2 * a + 2, "shifted-power shortcut clock")
        require(y == (5 * 9 ** (a - 1) - 1) // 4, "shifted-power endpoint")
        if a >= 4:
            require(y > 5 * x, "first-hit-plus-two height obstruction")
        shifted_cases += 1

    inverse_lifts = 0
    for z in range(1, 1000, 2):
        if z % 3 == 0:
            continue
        for g in range(2, 31):
            numerator = 2 ** g * z - 1
            if numerator % 3:
                continue
            x = numerator // 3
            if x % 3 == 0:
                continue
            p, q = x, 5 * x
            for _ in range(g):
                p, q = T(p), T(q)
            require(p == z and q == 5 * 3 ** (g - 2) * z - 1, "general inverse-lift identity")
            inverse_lifts += 1

    commutators = 0
    for x in range(1, 100, 2):
        for a in range(16):
            jx = 4 ** a * x + (4 ** a - 1) // 3
            j5x = 4 ** a * (5 * x) + (4 ** a - 1) // 3
            require(5 * jx - j5x == 4 * (4 ** a - 1) // 3, "J commutator")
            commutators += 1

    for t in range(512):
        x = 5 + 96 * t
        u, g = odd_event(x)
        require(g == 4 and 5 * x == 25 + 480 * t and 5 * u == 5 + 90 * t,
                "uniform propagator input arms")
    counts = {n: first_hit(n) for n in (1, 2, 5, 25)}
    require(counts == {1: (0, 0), 2: (1, 0), 5: (4, 1), 25: (16, 7)}, "stopping grades")
    require(Fraction(480, 90) == Fraction(2 ** 4, 3), "slope ratio")
    require(4 - 2 * 1 == 2, "slope-forced grade")
    require((16 - 2 * 7) - (4 - 2 * 1) == 0, "common-endpoint forced grade")
    paths = []
    for start in (25, 5):
        path, n, o = [], start, 0
        for d in range(97):
            path.append((n, d, o))
            o += n % 2
            n = T(n)
        paths.append(path)
    common_endpoint_pairs = 0
    for n, d, o in paths[0]:
        for m, e, p in paths[1]:
            if n == m:
                require(d - 2 * o == e - 2 * p, "grade telescoping at a common endpoint")
                require(not (d - e == 4 and o - p == 1), "forbidden uniform grade")
                common_endpoint_pairs += 1

    product_cases = padding_cases = 0
    maximum_reciprocal = Fraction(0)
    for source in range(1, 5002, 2):
        if source % 3 == 0:
            continue
        n, h, exponent = source, 0, 0
        product, reciprocal = Fraction(1), Fraction(0)
        seen = set()
        while n != 1 and h < 10000:
            require(n not in seen and n % 3 != 0, "first-hit simplicity or unit domain")
            seen.add(n)
            product *= Fraction(3 * n + 1, 3 * n)
            reciprocal += Fraction(1, n)
            n, g = odd_event(n)
            h += 1
            exponent += g
        require(n == 1, "bounded product source did not hit")
        require(2 ** exponent == 3 ** h * source * product, "exact first-hit product identity")
        require(product >= 1 and reciprocal <= 200, "finite distortion control")
        for repetitions in range(4):
            require(8 * (h + repetitions) - 5 * (exponent + 2 * repetitions)
                    == 8 * h - 5 * exponent - 2 * repetitions, "root-loop score")
            padding_cases += 1
        maximum_reciprocal = max(maximum_reciprocal, reciprocal)
        product_cases += 1

    require(3 ** 5 < 2 ** 8, "positive delta")
    require(8 * 3125 ** 24 < 3456 ** 24, "finite-path exponent certificate")
    report = {
        "status": "PASS: bounded arithmetic replay; all-depth deductions reconstructed separately in CLOSING_REVIEW.md",
        "reviewed_note_sha256": NOTE_SHA256,
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "shifted_power_cases_a_2_through_80": shifted_cases,
        "general_inverse_lifts_z_below_1000_g_2_through_30": inverse_lifts,
        "J_commutators": commutators,
        "propagator_progression_cases": 512,
        "stopping_counts_shortcut_and_odd": {str(n): list(v) for n, v in counts.items()},
        "common_endpoint_pairs_through_shortcut_clock_96": common_endpoint_pairs,
        "first_hit_product_cases_odd_units_through_5001": product_cases,
        "negative_root_cycle_padding_cases": padding_cases,
        "maximum_finite_reciprocal_sum": [maximum_reciprocal.numerator, maximum_reciprocal.denominator],
        "all_depth_closure_claimed": False,
    }
    data = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        with args.output.open("x", encoding="utf-8") as handle:
            handle.write(data)
        print(f"PASS: wrote {args.output}")
    elif args.compare:
        require(json.loads(args.compare.read_text(encoding="utf-8")) == report, "frozen replay differs")
        print(f"PASS: exact comparison {args.compare}")
    else:
        print(data, end="")


if __name__ == "__main__":
    main()
