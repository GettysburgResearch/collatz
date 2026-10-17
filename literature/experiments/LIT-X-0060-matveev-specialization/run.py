#!/usr/bin/env python3
"""Exact source specialization of Matveev Corollary 2.3 to log 2/log 3.

The script certifies a safe n=2 constant, strengthened repetition cutoffs for
T-8255/T-8260, and the fixed-support exponential-rate thresholds.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

sys.set_int_max_str_digits(0)

TERMS = 200
SAFE_C2 = 748_000_000


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("bad interval")


def atanh_interval(z: Fraction, terms: int = TERMS) -> Interval:
    if not Fraction(0) <= z < 1:
        raise ValueError("atanh domain")
    s = Fraction(0)
    zpow = z
    z2 = z * z
    for j in range(terms):
        s += 2 * zpow / (2 * j + 1)
        zpow *= z2
    tail = 2 * zpow / ((2 * terms + 1) * (1 - z2))
    return Interval(s, s + tail)


def log_interval(x: Fraction, terms: int = TERMS) -> Interval:
    if x <= 0:
        raise ValueError("log domain")
    if x == 2:
        return atanh_interval(Fraction(1, 3), terms)
    m = x.numerator.bit_length() - x.denominator.bit_length()
    y = x / (2**m) if m >= 0 else x * (2 ** (-m))
    while y < 1:
        m -= 1
        y *= 2
    while y >= 2:
        m += 1
        y /= 2
    z = (y - 1) / (y + 1)
    core = atanh_interval(z, terms)
    l2 = atanh_interval(Fraction(1, 3), terms)
    if m >= 0:
        return Interval(m * l2.lo + core.lo, m * l2.hi + core.hi)
    return Interval(m * l2.hi + core.lo, m * l2.lo + core.hi)


LOG2 = log_interval(Fraction(2))
LOG3 = log_interval(Fraction(3))


def e_upper(terms: int = 30) -> Fraction:
    fact = 1
    s = Fraction(1)
    for n in range(1, terms + 1):
        fact *= n
        s += Fraction(1, fact)
    first = Fraction(1, fact * (terms + 1))
    tail = first / (1 - Fraction(1, terms + 2))
    return s + tail


def decimal_floor(x: Fraction, digits: int = 18) -> str:
    sign = "-" if x < 0 else ""
    x = abs(x)
    scale = 10**digits
    n = x.numerator * scale // x.denominator
    q, r = divmod(n, scale)
    return f"{sign}{q}.{r:0{digits}d}"


def certify_safe_constant() -> dict[str, object]:
    sqrt2_hi = Fraction(1_414_214, 1_000_000)
    if sqrt2_hi * sqrt2_hi <= 2:
        raise AssertionError("sqrt(2) upper bound failed")
    upper = e_upper() * 30**5 * 8 * sqrt2_hi
    if not upper < SAFE_C2:
        raise AssertionError("safe Matveev constant failed")
    return {
        "source_expression": "e*30^5*2^(7/2)",
        "safe_integer_upper_bound": SAFE_C2,
        "upper_bound_decimal": decimal_floor(upper, 12),
        "second_source_branch": 2**32,
        "improvement_factor_over_2^32_lower": decimal_floor(Fraction(2**32, SAFE_C2), 9),
    }


def sha_fraction(x: Fraction) -> str:
    return hashlib.sha256(f"{x.numerator}/{x.denominator}".encode()).hexdigest()


def effective_rate(A: int, k: int, support_fraction: Fraction) -> Interval:
    return Interval(
        A * LOG2.lo - support_fraction * k * LOG3.hi,
        A * LOG2.hi - support_fraction * k * LOG3.lo,
    )


def cutoff_certificate(A: int, k: int, cmax: int, support_fraction: Fraction, M: int) -> dict[str, object]:
    rate = effective_rate(A, k, support_fraction)
    if rate.lo <= 0:
        raise AssertionError("nonpositive effective rate")
    K = Interval(SAFE_C2 * LOG2.lo * LOG3.lo, SAFE_C2 * LOG2.hi * LOG3.hi)
    logc = log_interval(Fraction(2 * cmax))
    logB = log_interval(Fraction(k * M + 1))
    margin = M * rate.lo - logc.hi - K.hi * (1 + logB.hi)
    derivative = rate.lo - K.hi * Fraction(k, k * M + 1)
    if margin <= 0 or derivative <= 0:
        raise AssertionError("cutoff not certified")
    return {
        "cutoff": M,
        "support_fraction": f"{support_fraction.numerator}/{support_fraction.denominator}",
        "effective_rate_decimal_lower": decimal_floor(rate.lo, 18),
        "margin_decimal_lower": decimal_floor(margin, 12),
        "margin_sha256": sha_fraction(margin),
        "derivative_decimal_lower": decimal_floor(derivative, 18),
        "derivative_sha256": sha_fraction(derivative),
    }


def support_threshold(A: int, k: int, expected: int) -> dict[str, object]:
    good = effective_rate(A, k, Fraction(expected - 1, expected))
    bad = effective_rate(A, k, Fraction(expected, expected + 1))
    if good.lo <= 0:
        raise AssertionError("expected fixed-support threshold is not good")
    if bad.hi >= 0:
        raise AssertionError("next fixed-support threshold is not bad")
    return {
        "maximum_support_with_positive_rate": expected,
        "rate_at_max_decimal_lower": decimal_floor(good.lo, 18),
        "rate_at_next_decimal_upper": decimal_floor(bad.hi, 18),
        "criterion": "A*log(2)-((s-1)/s)*k*log(3)>0",
    }


def build() -> dict[str, object]:
    return {
        "description": "Exact Matveev n=2 source specialization and pulse cutoffs",
        "matveev_constant": certify_safe_constant(),
        "strengthened_cutoffs": {
            "T-8255-two-pulse-P3": cutoff_certificate(3, 2, 7, Fraction(1, 2), 14_600_000_000),
            "T-8255-two-pulse-P11": cutoff_certificate(11, 7, 91, Fraction(1, 2), 3_800_000_000),
            "T-8260-three-pulse-P3": cutoff_certificate(3, 2, 7, Fraction(2, 3), 23_800_000_000),
            "T-8260-three-pulse-P11": cutoff_certificate(11, 7, 91, Fraction(2, 3), 5_800_000_000),
        },
        "fixed_support_thresholds": {
            "P3-(1,2)": support_threshold(3, 2, 18),
            "P11-(1,1,1,2,1,1,4)": support_threshold(11, 7, 117),
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    ap.add_argument("--check-results", type=Path)
    args = ap.parse_args()
    obj = build()
    payload = json.dumps(obj, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    if args.check_results:
        expected = args.check_results.read_text(encoding="utf-8")
        if payload != expected:
            raise SystemExit("Matveev specialization result mismatch")
    print(payload, end="")


if __name__ == "__main__":
    main()
