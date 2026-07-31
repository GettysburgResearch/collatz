#!/usr/bin/env python3
"""Independent verifier for LIT-X-0065.

This file imports no author-side module. It reconstructs logarithm intervals
with a separate implementation and checks every structural and inequality
certificate in the frozen JSON.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

sys.set_int_max_str_digits(0)

TERMS = 300
MATVEEV_C = 748_000_000
N_STAR = 4 * 3**44 + 2


@dataclass(frozen=True)
class I:
    a: Fraction
    b: Fraction

    def __post_init__(self) -> None:
        if self.a >= self.b:
            raise ValueError("bad interval")


def log_unit_interval(x: Fraction) -> I:
    """Log interval after reducing x to [1,2), via y=(x-1)/(x+1)."""
    if not 1 <= x < 2:
        raise ValueError("not a unit mantissa")
    y = (x - 1) / (x + 1)
    y2 = y * y
    term = y
    total = Fraction(0)
    for j in range(TERMS):
        total += term / (2 * j + 1)
        term *= y2
    lower = 2 * total
    upper = lower + 2 * term / ((2 * TERMS + 1) * (1 - y2))
    return I(lower, upper)


def log2_interval() -> I:
    y = Fraction(1, 3)
    y2 = y * y
    term = y
    total = Fraction(0)
    for j in range(TERMS):
        total += term / (2 * j + 1)
        term *= y2
    return I(
        2 * total,
        2 * total + 2 * term / ((2 * TERMS + 1) * (1 - y2)),
    )


L2 = log2_interval()


def logq(x: Fraction) -> I:
    if x <= 0:
        raise ValueError("nonpositive")
    shift = 0
    while x >= 2:
        x /= 2
        shift += 1
    while x < 1:
        x *= 2
        shift -= 1
    core = log_unit_interval(x)
    if shift >= 0:
        return I(core.a + shift * L2.a, core.b + shift * L2.b)
    return I(core.a + shift * L2.b, core.b + shift * L2.a)


L3 = logq(Fraction(3))


def digest_without_digest(data: dict[str, Any]) -> str:
    copy = dict(data)
    copy.pop("semantic_sha256", None)
    frozen = json.dumps(copy, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(frozen).hexdigest()


def eta(A: int, k: int) -> I:
    nlo = k * L3.a - A * L2.b
    nhi = k * L3.b - A * L2.a
    return I(nlo / L2.b, nhi / L2.a)


def verify_cf(rows: list[dict[str, Any]], A: int, k: int, cutoff: int) -> None:
    e = eta(A, k)
    lo, hi = e.a, e.b
    pm2, pm1, qm2, qm1 = 0, 1, 1, 0
    passed = False
    for idx, row in enumerate(rows):
        a0 = lo.numerator // lo.denominator
        a1 = hi.numerator // hi.denominator
        assert a0 == a1 == row["partial_quotient"]
        p = a0 * pm1 + pm2
        q = a0 * qm1 + qm2
        assert p == row["p"] and q == row["q"] and idx == row["index"]
        value = Fraction(p, q)
        side = "below" if value < e.a else "above" if value > e.b else "inside"
        assert side == row["side"] and side != "inside"
        if q > cutoff:
            passed = True
            assert idx == len(rows) - 1
            break
        lo, hi = 1 / (hi - a0), 1 / (lo - a0)
        pm2, pm1, qm2, qm1 = pm1, p, qm1, q
    assert passed


def family_parameters(name: str) -> tuple[int, int, int, int, int, int]:
    if name == "P3":
        return 3, 2, 7, 18, 19, 5_000_000_000_000
    if name == "P11":
        return 11, 7, 91, 117, 118, 400_000_000_000_000
    raise AssertionError(name)


def verify_family(f: dict[str, Any], split: int) -> None:
    A, k, c, s, snext, cutoff = family_parameters(f["name"])
    assert f["A"] == A and f["k"] == k and f["cmax"] == c
    assert f["matveev"]["cutoff"] == cutoff

    threshold = f["support_threshold"]
    assert threshold["last_positive_rate_support"] == s
    assert threshold["first_nonpositive_rate_support"] == snext
    good = 2 ** (A * s) - 3 ** ((s - 1) * k)
    bad = 3 ** ((snext - 1) * k) - 2 ** (A * snext)
    assert good > 0 and bad > 0
    assert threshold["positive_rate_margin_sha256"] == hashlib.sha256(
        f"{good}/1".encode()
    ).hexdigest()
    assert threshold["nonpositive_rate_margin_sha256"] == hashlib.sha256(
        f"{bad}/1".encode()
    ).hexdigest()

    leg = f["all_repetition_legendre"]
    assert leg["split_repetition"] == split
    assert N_STAR - k * split**2 == leg[
        "small_range_integer_margin_Nstar_minus_kR2"
    ] > 0

    assert leg["pulse_base_row_count"] == s
    minimum = None
    for offset in range(s):
        r = split + offset
        exponent = ((s - 1) * k * r) // s
        margin = A * r * L2.a - exponent * L3.b - logq(Fraction(6 * c * r)).b
        assert margin > 0
        if minimum is None or margin < minimum[0]:
            minimum = (margin, r, exponent)
    assert minimum is not None
    frozen_min = leg["minimum_pulse_log_margin"]
    assert frozen_min["r"] == minimum[1]
    assert frozen_min["exponent"] == minimum[2]

    period_margin = split * 2 ** (A * s) - (split + s) * 3 ** ((s - 1) * k)
    assert period_margin > 0
    assert leg["pulse_period_margin_sha256"] == hashlib.sha256(
        f"{period_margin}/1".encode()
    ).hexdigest()

    rho = Fraction(s - 1, s)
    rate_lo = A * L2.a - rho * k * L3.b
    assert rate_lo > 0
    K_hi = MATVEEV_C * L2.b * L3.b
    M = cutoff
    margin = (
        M * rate_lo
        - logq(Fraction(2 * c)).b
        - K_hi * (1 + logq(Fraction(k * M + 1)).b)
    )
    derivative = rate_lo - K_hi * Fraction(k, k * M + 1)
    assert margin > 0 and derivative > 0

    cf = f["convergents"]
    all_rows = cf["continued_fraction_rows"]
    verify_cf(all_rows, A, k, cutoff)
    row_by_index = {row["index"]: row for row in all_rows}
    covered = cf["upper_convergents_below_cutoff"]
    actual_upper = [
        row for row in all_rows
        if row["side"] == "above" and row["q"] < cutoff
    ]
    assert len(covered) == len(actual_upper)

    counts = {"verified_floor_only": 0, "pulse_comparison_only": 0, "both": 0}
    for record, source in zip(covered, actual_upper):
        assert record["index"] == source["index"]
        assert record["p"] == source["p"] and record["q"] == source["q"]
        nxt = row_by_index[source["index"] + 1]
        assert record["q_next"] == nxt["q"]
        p, q, qn = record["p"], record["q"], record["q_next"]

        lam_lo = (A * q + p) * L2.a - k * q * L3.b
        floor_ok = lam_lo > Fraction(k * q, 3 * N_STAR)

        exponent = ((s - 1) * k * q) // s
        exponent_step = ((s - 1) * k * q + s - 1) // s
        comp = (
            A * q * L2.a
            - exponent * L3.b
            - logq(Fraction(4 * c * (q + qn))).b
        )
        step = A * q * L2.a - exponent_step * L3.b
        pulse_ok = comp > 0 and step > 0
        assert floor_ok or pulse_ok

        expected = (
            "both" if floor_ok and pulse_ok
            else "verified_floor" if floor_ok
            else "pulse_comparison"
        )
        assert record["method"] == expected
        counts[
            "both" if expected == "both"
            else "verified_floor_only" if expected == "verified_floor"
            else "pulse_comparison_only"
        ] += 1

    counts["total"] = len(covered)
    assert counts == cf["coverage_counts"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    data = json.loads(args.result.read_text())
    assert data["experiment_id"] == "LIT-X-0065"
    assert data["claim_id"] == "LIT-KTHM-0065"
    assert data["verified_floor"] == N_STAR
    assert digest_without_digest(data) == data["semantic_sha256"]
    for family in data["families"]:
        verify_family(family, data["small_repetition_split"])
    print("LIT-X-0065 INDEPENDENT VERIFICATION PASSED")
    print(data["semantic_sha256"])


if __name__ == "__main__":
    main()
