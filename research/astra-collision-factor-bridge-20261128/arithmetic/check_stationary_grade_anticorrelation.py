#!/usr/bin/env python3
"""Exact finite native count plus rational certificate for a stationary gap.

This is a bounded arithmetic replay, not a proof of an asymptotic claim.
The fair stationary transfer and fractional-moment argument remain written
in STATIONARY_GRADE_ANTICORRELATION.md. No floating-point comparison enters
the certificate and all checks remain active under python -O.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from math import comb
from pathlib import Path
import sys


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def direct_count(cutoff: int, clock: int, grade_cut: int) -> int:
    count = 0
    for source in range(1, cutoff + 1):
        value, grade = source, 0
        for _ in range(clock):
            if value % 2:
                grade += 1
                value = (3 * value + 1) // 2
            else:
                value //= 2
        count += grade <= grade_cut
    return count


def aggregate_count(cutoff: int, clock: int, grade_cut: int) -> int:
    population: dict[tuple[int, int], int] = {
        (source, 0): 1 for source in range(1, cutoff + 1)
    }
    for _ in range(clock):
        next_population: dict[tuple[int, int], int] = defaultdict(int)
        for (value, grade), multiplicity in population.items():
            bit = value & 1
            next_value = (3 ** bit * value + bit) // 2
            next_population[(next_value, grade + bit)] += multiplicity
        population = next_population
        require(sum(population.values()) == cutoff, "population mass changed")
    return sum(mass for (_, grade), mass in population.items() if grade <= grade_cut)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    cutoff, clock, grade_cut = 100_000, 80, 35
    count_direct = direct_count(cutoff, clock, grade_cut)
    count_aggregate = aggregate_count(cutoff, clock, grade_cut)
    require(count_direct == count_aggregate == 12_850, "exact counts disagree")

    # h=floor(2 log X/log(4/3)); square the exponential inequalities.
    require(4 ** clock <= cutoff ** 2 * 3 ** clock,
            "critical lower clock inequality failed")
    require(cutoff ** 2 * 3 ** (clock + 1) < 4 ** (clock + 1),
            "critical upper clock inequality failed")
    # floor(40-sqrt(20))=35, with no approximate square root.
    require(4 ** 2 < 20 <= 5 ** 2, "grade threshold failed")

    # 2^(7/4)>84/25 and 3^(3/4)<57/25, so M_(3/4)<25/2.
    require(Fraction(84, 25) ** 4 < 2 ** 7, "power-of-two bound failed")
    require(Fraction(57, 25) ** 4 > 3 ** 3, "power-of-three bound failed")
    require(Fraction(84, 25) - 1 - Fraction(57, 25) == Fraction(2, 25),
            "moment denominator gap failed")
    require(5_000 ** 4 < cutoff ** 3, "source fractional-power bound failed")
    stationary_error_bound = Fraction(25, 2) / 5_000
    ordinary_tail = Fraction(count_direct, cutoff)
    stationary_tail_upper = ordinary_tail + stationary_error_bound
    binomial_tail = Fraction(sum(comb(clock, a) for a in range(grade_cut + 1)),
                             2 ** clock)
    require(stationary_tail_upper == Fraction(131, 1_000),
            "conditional upper bound changed")
    require(binomial_tail > Fraction(157, 1_000), "binomial lower bound failed")
    require(binomial_tail - stationary_tail_upper > Fraction(26, 1_000),
            "strict negative covariance gap failed")

    def rational(value: Fraction) -> dict[str, int]:
        return {"numerator": value.numerator, "denominator": value.denominator}

    receipt = {
        "status": "pass",
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "optimization_level": sys.flags.optimize,
        "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_cutoff": cutoff,
        "native_shortcut_clock": clock,
        "odd_grade_cutoff": grade_cut,
        "direct_native_count": count_direct,
        "independent_population_aggregate_count": count_aggregate,
        "ordinary_tail": rational(ordinary_tail),
        "fair_binomial_tail": rational(binomial_tail),
        "strict_stationary_TV_upper_bound": rational(stationary_error_bound),
        "strict_stationary_conditional_tail_upper_bound": rational(stationary_tail_upper),
        "strict_negative_relative_covariance_gap_lower_bound": rational(Fraction(26, 1_000)),
        "checks": [
            "native counts agree by direct source iteration and population aggregation",
            "clock and grade threshold certified by integer powers",
            "fractional moment bounded using rational fourth powers",
            "binomial probability and final covariance gap compared as exact fractions",
            "no floating-point arithmetic or optimization-sensitive assertions",
        ],
        "scope": "Bounded exact replay plus rational inequalities. The stationary transfer, moment construction, and covariance interpretation are written proofs; this does not certify or refute the asymptotic one-copy lower bound.",
    }
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"status": "pass", "count": count_direct,
                      "receipt": str(args.receipt),
                      "runner_sha256": receipt["runner_sha256"]}))


if __name__ == "__main__":
    main()
