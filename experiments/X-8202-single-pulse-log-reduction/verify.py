#!/usr/bin/env python3
"""Independent exact reconstruction of X-8202.

This verifier intentionally imports no code from run.py. It rebuilds the certified
logarithm intervals, continued fractions, Matveev cutoffs, convergent reductions,
and exact small cases, then compares the complete payload with canonical.json.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Iterable

sys.set_int_max_str_digits(0)
NTERMS = 180
C_MAT = 1 << 32


class Pair:
    __slots__ = ("lower", "upper")

    def __init__(self, lower: Fraction, upper: Fraction) -> None:
        assert lower < upper
        self.lower = lower
        self.upper = upper


def digest(q: Fraction) -> str:
    return hashlib.sha256(f"{q.numerator}/{q.denominator}".encode("ascii")).hexdigest()


def down(q: Fraction, places: int) -> str:
    scale = 10**places
    neg = q < 0
    q = abs(q)
    n = q.numerator * scale // q.denominator
    a, b = divmod(n, scale)
    return ("-" if neg else "") + f"{a}.{b:0{places}d}"


def up(q: Fraction, places: int) -> str:
    scale = 10**places
    neg = q < 0
    q = abs(q)
    n = (q.numerator * scale + q.denominator - 1) // q.denominator
    a, b = divmod(n, scale)
    return ("-" if neg else "") + f"{a}.{b:0{places}d}"


def log_core(z: Fraction) -> Pair:
    assert 0 <= z < 1
    zz = z * z
    term = z
    total = Fraction(0)
    for j in range(NTERMS):
        total += 2 * term / (2 * j + 1)
        term *= zz
    remainder = 2 * term / ((2 * NTERMS + 1) * (1 - zz))
    return Pair(total, total + remainder)


def rational_log(x: Fraction) -> Pair:
    assert x > 0
    if x == 2:
        return log_core(Fraction(1, 3))
    shift = x.numerator.bit_length() - x.denominator.bit_length()
    y = x / (2**shift) if shift >= 0 else x * (2 ** (-shift))
    while y < 1:
        shift -= 1
        y *= 2
    while y >= 2:
        shift += 1
        y /= 2
    middle = log_core((y - 1) / (y + 1))
    two = log_core(Fraction(1, 3))
    if shift >= 0:
        return Pair(middle.lower + shift * two.lower, middle.upper + shift * two.upper)
    return Pair(middle.lower + shift * two.upper, middle.upper + shift * two.lower)


LN2 = rational_log(Fraction(2))
LN3 = rational_log(Fraction(3))


def alpha_bounds(A: int, k: int) -> Pair:
    low_num = k * LN3.lower - A * LN2.upper
    high_num = k * LN3.upper - A * LN2.lower
    assert low_num > 0
    return Pair(low_num / LN2.upper, high_num / LN2.lower)


def pair_product(a: Pair, b: Pair) -> Pair:
    assert a.lower > 0 and b.lower > 0
    return Pair(a.lower * b.lower, a.upper * b.upper)


def alpha_record(x: Pair) -> dict[str, object]:
    width = x.upper - x.lower
    exponent = 0
    while width < Fraction(1, 2 ** (exponent + 1)):
        exponent += 1
    return {
        "decimal_lo": down(x.lower, 30),
        "decimal_hi": up(x.upper, 30),
        "lo_sha256": digest(x.lower),
        "hi_sha256": digest(x.upper),
        "width_less_than_2_pow_minus": exponent,
    }


def continued_fraction(x: Pair, limit: int) -> list[dict[str, int | str]]:
    a, b = x.lower, x.upper
    p0, p1, q0, q1 = 0, 1, 1, 0
    rows: list[dict[str, int | str]] = []
    for idx in range(256):
        digit_a = a.numerator // a.denominator
        digit_b = b.numerator // b.denominator
        assert digit_a == digit_b
        digit = digit_a
        p = digit * p1 + p0
        q = digit * q1 + q0
        frac = Fraction(p, q)
        assert frac < x.lower or frac > x.upper
        side = "below" if frac < x.lower else "above"
        rows.append(
            {"index": idx, "partial_quotient": digit, "p": p, "q": q, "side": side}
        )
        if q > limit:
            return rows
        a, b = 1 / (b - digit), 1 / (a - digit)
        p0, p1, q0, q1 = p1, p, q1, q
    raise AssertionError("continued fraction cutoff not reached")


def matveev(A: int, k: int, c: int, threshold: int) -> dict[str, object]:
    assert A * threshold >= (2 * c).bit_length() and LN3.lower > 1
    product = pair_product(LN2, LN3)
    Klo, Khi = C_MAT * product.lower, C_MAT * product.upper
    lhs = threshold * A * LN2.lower
    rhs = rational_log(Fraction(2 * c)).upper + Khi * (
        1 + rational_log(Fraction(k * threshold + 1)).upper
    )
    margin = lhs - rhs
    derivative = A * LN2.lower - Khi * Fraction(k, k * threshold + 1)
    assert margin > 0 and derivative > 0
    return {
        "cutoff_verified": True,
        "margin_decimal_lower": down(margin, 12),
        "margin_sha256": digest(margin),
        "derivative_decimal_lower": down(derivative, 18),
        "derivative_sha256": digest(derivative),
    }


def small_divisors(A: int, k: int, coeffs: Iterable[int], upto: int) -> list[dict[str, int]]:
    coeffs = tuple(coeffs)
    U, Q = 2**A, 3**k
    ur = qr = 1
    result: list[dict[str, int]] = []
    for r in range(1, upto + 1):
        ur *= U
        qr *= Q
        delta = 1
        while ur * (2**delta) <= qr:
            delta += 1
        while True:
            denominator = ur * (2**delta) - qr
            active = False
            for c in coeffs:
                target = c * (2**delta - 1)
                if denominator <= target:
                    active = True
                    if target % denominator == 0:
                        result.append(
                            {
                                "r": r,
                                "delta": delta,
                                "c": c,
                                "D": denominator,
                                "quotient": target // denominator,
                            }
                        )
            if not active:
                break
            delta += 1
    return result


def reject_primitives(
    A: int, cmax: int, rows: list[dict[str, int | str]], cutoff: int, rmin: int
) -> list[dict[str, object]]:
    rejected: list[dict[str, object]] = []
    for j in range(len(rows) - 1):
        row = rows[j]
        q, p = int(row["q"]), int(row["p"])
        if row["side"] != "above" or q < rmin or q >= cutoff:
            continue
        q2 = int(rows[j + 1]["q"])
        rhs = 4 * cmax * (q + q2)
        assert A * q >= rhs.bit_length()
        rejected.append(
            {
                "primitive_denominator_q": q,
                "primitive_numerator_p": p,
                "next_denominator": q2,
                "power_two_exponent_at_m1": A * q,
                "comparison_rhs_at_m1": rhs,
                "all_positive_multiples_rejected": True,
            }
        )
    return rejected


DATA = (
    {
        "name": "negative-three-cycle",
        "A": 3,
        "k": 2,
        "coeffs": (5, 7),
        "cmax": 7,
        "limit": 50_000_000_000,
        "rmin": 3,
        "small": 4,
    },
    {
        "name": "negative-eleven-cycle",
        "A": 11,
        "k": 7,
        "coeffs": (17, 25, 37, 41, 55, 61, 91),
        "cmax": 91,
        "limit": 12_000_000_000,
        "rmin": 1,
        "small": 1,
    },
)


def rebuild() -> dict[str, object]:
    all_cases: list[dict[str, object]] = []
    transcript = hashlib.sha256()
    nrows = ncandidates = 0

    for spec in DATA:
        A, k = int(spec["A"]), int(spec["k"])
        limit, rmin = int(spec["limit"]), int(spec["rmin"])
        interval = alpha_bounds(A, k)
        rows = continued_fraction(interval, limit)
        cutoff_record = matveev(A, k, int(spec["cmax"]), limit)

        legendre_margin = LN2.lower * 2 ** (A * rmin) - 4 * int(spec["cmax"]) * rmin
        assert legendre_margin > 0

        hits = small_divisors(A, k, spec["coeffs"], int(spec["small"]))
        if spec["name"] == "negative-three-cycle":
            assert hits == [{"r": 1, "delta": 1, "c": 7, "D": 7, "quotient": 1}]
        else:
            assert hits == []

        primitive_rows = [
            {
                "primitive_denominator_q": int(row["q"]),
                "primitive_numerator_p": int(row["p"]),
                "next_q": int(rows[j + 1]["q"]),
            }
            for j, row in enumerate(rows[:-1])
            if row["side"] == "above" and rmin <= int(row["q"]) < limit
        ]
        rejected = reject_primitives(A, int(spec["cmax"]), rows, limit, rmin)
        assert len(primitive_rows) == len(rejected)

        for row in rows:
            transcript.update(
                f"{spec['name']}|{row['index']}|{row['partial_quotient']}|{row['p']}|{row['q']}|{row['side']}\n".encode(
                    "ascii"
                )
            )
        nrows += len(rows)
        ncandidates += len(rejected)
        all_cases.append(
            {
                "name": spec["name"],
                "A": A,
                "k": k,
                "odd_coefficients": list(spec["coeffs"]),
                "cutoff": limit,
                "alpha_interval": alpha_record(interval),
                "continued_fraction": rows,
                "upper_convergents_below_cutoff": primitive_rows,
                "candidate_rejections": rejected,
                "small_hits": hits,
                "matveev_certificate": cutoff_record,
                "legendre_margin_decimal_lower": down(legendre_margin, 18),
                "legendre_margin_sha256": digest(legendre_margin),
            }
        )

    return {
        "claim": "T-8202",
        "status": "SOURCE-DEPENDENT PROPOSED; exact reduction/checker, external Matveev theorem pending independent source reconstruction",
        "matveev_form_used": {
            "n": 2,
            "degree": 1,
            "constant": "2^(6n+20)=2^32",
            "A1": "log(2)",
            "A2": "log(3)",
            "bound": "log|Lambda| >= -2^32*log(2)*log(3)*(1+log B)",
        },
        "log_interval_terms": NTERMS,
        "cases": all_cases,
        "summary": {
            "certified_continued_fraction_rows": nrows,
            "upper_convergent_candidates_rejected": ncandidates,
            "nontrivial_divisibility_hits": 0,
            "trivial_hits": 1,
        },
        "transcript_sha256": transcript.hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path)
    args = parser.parse_args()
    frozen = json.loads(args.artifact.read_text(encoding="utf-8"))
    fresh = rebuild()
    if fresh != frozen:
        raise SystemExit("independent reconstruction differs from frozen X-8202 artifact")
    print("independent reconstruction matches")
    print(json.dumps(fresh["summary"], sort_keys=True))
    print(f"transcript_sha256={fresh['transcript_sha256']}")


if __name__ == "__main__":
    main()
