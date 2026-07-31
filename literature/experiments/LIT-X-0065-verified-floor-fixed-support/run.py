#!/usr/bin/env python3
"""Exact certificate for the verified-floor fixed-support pulse exclusion.

This program certifies the arithmetic inequalities used in LIT-KTHM-0065.
The sole imported inputs are:
  * the branch-qualified verified floor N_* from PR #76;
  * Matveev 2000, Corollary 2.3, specialized in LIT-KTHM-0060;
  * the native distributed-pulse identity / resultant caps from PR #53/PR #70.

Everything after those interfaces uses exact integers and Fraction intervals.
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

EXPERIMENT_ID = "LIT-X-0065"
CLAIM_ID = "LIT-KTHM-0065"
LOG_TERMS = 240
MATVEEV_C = 748_000_000
SMALL_R = 1_000_000
N_STAR = 4 * 3**44 + 2


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if not self.lo < self.hi:
            raise ValueError("invalid interval")


@dataclass(frozen=True)
class Family:
    name: str
    base: tuple[int, ...]
    A: int
    k: int
    cmax: int
    max_support: int
    next_support: int
    cutoff: int


FAMILIES = (
    Family(
        name="P3",
        base=(1, 2),
        A=3,
        k=2,
        cmax=7,
        max_support=18,
        next_support=19,
        cutoff=5_000_000_000_000,
    ),
    Family(
        name="P11",
        base=(1, 1, 1, 2, 1, 1, 4),
        A=11,
        k=7,
        cmax=91,
        max_support=117,
        next_support=118,
        cutoff=400_000_000_000_000,
    ),
)


def fraction_text(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def fraction_sha(x: Fraction) -> str:
    return hashlib.sha256(fraction_text(x).encode("ascii")).hexdigest()


def decimal_floor(x: Fraction, digits: int = 18) -> str:
    sign = "-" if x < 0 else ""
    x = abs(x)
    scale = 10**digits
    z = x.numerator * scale // x.denominator
    whole, rem = divmod(z, scale)
    return f"{sign}{whole}.{rem:0{digits}d}"


def atanh_log_interval(z: Fraction, terms: int = LOG_TERMS) -> Interval:
    """Certified interval for log((1+z)/(1-z)), 0 <= z < 1."""
    if not Fraction(0) <= z < 1:
        raise ValueError("atanh argument")
    total = Fraction(0)
    power = z
    square = z * z
    for n in range(terms):
        total += 2 * power / (2 * n + 1)
        power *= square
    tail = 2 * power / ((2 * terms + 1) * (1 - square))
    return Interval(total, total + tail)


def log_interval(x: Fraction, terms: int = LOG_TERMS) -> Interval:
    """Certified natural-log interval for positive rational x."""
    if x <= 0:
        raise ValueError("log argument")
    log2 = atanh_log_interval(Fraction(1, 3), terms)
    if x == 2:
        return log2
    shift = x.numerator.bit_length() - x.denominator.bit_length()
    mantissa = x / (2**shift) if shift >= 0 else x * 2 ** (-shift)
    while mantissa < 1:
        shift -= 1
        mantissa *= 2
    while mantissa >= 2:
        shift += 1
        mantissa /= 2
    core = atanh_log_interval((mantissa - 1) / (mantissa + 1), terms)
    if shift >= 0:
        return Interval(shift * log2.lo + core.lo, shift * log2.hi + core.hi)
    return Interval(shift * log2.hi + core.lo, shift * log2.lo + core.hi)


LOG2 = log_interval(Fraction(2))
LOG3 = log_interval(Fraction(3))


def log_integer(n: int) -> Interval:
    return log_interval(Fraction(n))


def eta_interval(spec: Family) -> Interval:
    numerator_lo = spec.k * LOG3.lo - spec.A * LOG2.hi
    numerator_hi = spec.k * LOG3.hi - spec.A * LOG2.lo
    if numerator_lo <= 0:
        raise AssertionError("eta numerator not positive")
    return Interval(numerator_lo / LOG2.hi, numerator_hi / LOG2.lo)


def continued_fraction_rows(interval: Interval, stop_q: int) -> list[dict[str, Any]]:
    """Resolve all convergents through the first denominator above stop_q."""
    original = interval
    lo, hi = interval.lo, interval.hi
    p_nm2, p_nm1 = 0, 1
    q_nm2, q_nm1 = 1, 0
    rows: list[dict[str, Any]] = []
    for index in range(512):
        a_lo = lo.numerator // lo.denominator
        a_hi = hi.numerator // hi.denominator
        if a_lo != a_hi:
            raise AssertionError(f"continued fraction unresolved at row {index}")
        a = a_lo
        p = a * p_nm1 + p_nm2
        q = a * q_nm1 + q_nm2
        value = Fraction(p, q)
        if value < original.lo:
            side = "below"
        elif value > original.hi:
            side = "above"
        else:
            raise AssertionError("convergent intersects unresolved eta interval")
        rows.append(
            {
                "index": index,
                "partial_quotient": a,
                "p": p,
                "q": q,
                "side": side,
            }
        )
        if q > stop_q:
            return rows
        lo, hi = 1 / (hi - a), 1 / (lo - a)
        p_nm2, p_nm1 = p_nm1, p
        q_nm2, q_nm1 = q_nm1, q
    raise AssertionError("continued fraction did not pass cutoff")


def positive_record(x: Fraction, digits: int = 18) -> dict[str, str]:
    if x <= 0:
        raise AssertionError("nonpositive certified margin")
    return {
        "decimal_lower": decimal_floor(x, digits),
        "fraction_sha256": fraction_sha(x),
    }


def rate_interval(spec: Family) -> Interval:
    s = spec.max_support
    rho = Fraction(s - 1, s)
    return Interval(
        spec.A * LOG2.lo - rho * spec.k * LOG3.hi,
        spec.A * LOG2.hi - rho * spec.k * LOG3.lo,
    )


def support_threshold_certificate(spec: Family) -> dict[str, Any]:
    s = spec.max_support
    good = 2 ** (spec.A * s) - 3 ** ((s - 1) * spec.k)
    bad = 3 ** ((spec.next_support - 1) * spec.k) - 2 ** (
        spec.A * spec.next_support
    )
    if good <= 0 or bad <= 0:
        raise AssertionError("support threshold is not sharp")
    return {
        "last_positive_rate_support": s,
        "positive_rate_integer_margin": good,
        "first_nonpositive_rate_support": spec.next_support,
        "nonpositive_rate_integer_margin": bad,
    }


def all_r_legendre_certificate(spec: Family) -> dict[str, Any]:
    """Cover r<=SMALL_R by the verified floor, and r>=SMALL_R by pulse decay."""
    # For a nontrivial positive cycle:
    # t/r - eta < k/(3*N_STAR*log 2) < k/(2*N_STAR).
    # Thus Legendre holds at r<=SMALL_R if k*r^2 < N_STAR.
    small_margin = N_STAR - spec.k * SMALL_R**2
    if small_margin <= 0:
        raise AssertionError("verified-floor Legendre range too large")

    s = spec.max_support
    # Sufficient pulse condition:
    # 6*c*r*3^floor((s-1)kr/s) < 2^(Ar).
    # Check one representative of every residue class mod s.
    base_rows = []
    for offset in range(s):
        r = SMALL_R + offset
        exponent = ((s - 1) * spec.k * r) // s
        margin = (
            spec.A * r * LOG2.lo
            - exponent * LOG3.hi
            - log_integer(6 * spec.cmax * r).hi
        )
        base_rows.append(
            {
                "r": r,
                "exponent": exponent,
                "log_margin": positive_record(margin, 12),
            }
        )

    # Over one full residue period the pulse ratio decreases.
    period_left = SMALL_R * 2 ** (spec.A * s)
    period_right = (SMALL_R + s) * 3 ** ((s - 1) * spec.k)
    period_margin = period_left - period_right
    if period_margin <= 0:
        raise AssertionError("pulse Legendre period ratio not decreasing")

    return {
        "split_repetition": SMALL_R,
        "small_range_integer_margin_Nstar_minus_kR2": small_margin,
        "pulse_base_rows": base_rows,
        "pulse_period_integer_margin": period_margin,
        "conclusion": "every repetition yields an upper continued-fraction convergent",
    }


def matveev_cutoff_certificate(spec: Family) -> dict[str, Any]:
    rate = rate_interval(spec)
    if rate.lo <= 0:
        raise AssertionError("nonpositive max-support decay rate")
    K_hi = MATVEEV_C * LOG2.hi * LOG3.hi
    M = spec.cutoff
    margin = (
        M * rate.lo
        - log_integer(2 * spec.cmax).hi
        - K_hi * (1 + log_integer(spec.k * M + 1).hi)
    )
    derivative = rate.lo - K_hi * Fraction(spec.k, spec.k * M + 1)
    if margin <= 0 or derivative <= 0:
        raise AssertionError("Matveev cutoff not certified")
    return {
        "cutoff": M,
        "source_constant": MATVEEV_C,
        "max_support_rate_lower": positive_record(rate.lo, 18),
        "cutoff_margin": positive_record(margin, 12),
        "derivative_margin": positive_record(derivative, 18),
    }


def convergent_exclusion_certificate(spec: Family) -> dict[str, Any]:
    rows = continued_fraction_rows(eta_interval(spec), spec.cutoff)
    covered: list[dict[str, Any]] = []
    floor_count = 0
    pulse_count = 0
    both_count = 0

    for index, row in enumerate(rows[:-1]):
        if row["side"] != "above":
            continue
        p = int(row["p"])
        q = int(row["q"])
        if q >= spec.cutoff:
            continue
        q_next = int(rows[index + 1]["q"])

        # Verified-floor exclusion. A candidate multiple would imply
        # lambda_0 < k*q/(3*N_STAR).
        lambda_lower = (
            (spec.A * q + p) * LOG2.lo - spec.k * q * LOG3.hi
        )
        floor_margin = lambda_lower - Fraction(spec.k * q, 3 * N_STAR)
        floor_ok = floor_margin > 0

        # Pulse comparison at the worst (largest allowed) support.
        s = spec.max_support
        exponent = ((s - 1) * spec.k * q) // s
        exponent_step = ((s - 1) * spec.k * q + s - 1) // s
        comparison_margin = (
            spec.A * q * LOG2.lo
            - exponent * LOG3.hi
            - log_integer(4 * spec.cmax * (q + q_next)).hi
        )
        step_margin = spec.A * q * LOG2.lo - exponent_step * LOG3.hi
        pulse_ok = comparison_margin > 0 and step_margin > 0

        if not (floor_ok or pulse_ok):
            raise AssertionError(
                f"uncovered convergent {spec.name}: p/q={p}/{q}"
            )

        if floor_ok and pulse_ok:
            method = "both"
            both_count += 1
        elif floor_ok:
            method = "verified_floor"
            floor_count += 1
        else:
            method = "pulse_comparison"
            pulse_count += 1

        covered.append(
            {
                "index": int(row["index"]),
                "p": p,
                "q": q,
                "q_next": q_next,
                "method": method,
                "verified_floor_margin": (
                    positive_record(floor_margin, 18) if floor_ok else None
                ),
                "pulse_comparison_margin": (
                    positive_record(comparison_margin, 18) if pulse_ok else None
                ),
                "pulse_step_margin": (
                    positive_record(step_margin, 18) if pulse_ok else None
                ),
            }
        )

    if not covered:
        raise AssertionError("no upper convergents certified")

    return {
        "eta_interval": {
            "lo_sha256": fraction_sha(eta_interval(spec).lo),
            "hi_sha256": fraction_sha(eta_interval(spec).hi),
        },
        "continued_fraction_rows": rows,
        "upper_convergents_below_cutoff": covered,
        "coverage_counts": {
            "verified_floor_only": floor_count,
            "pulse_comparison_only": pulse_count,
            "both": both_count,
            "total": len(covered),
        },
    }


def trivial_hit_classification(spec: Family) -> dict[str, Any]:
    if spec.name == "P3":
        return {
            "exists": True,
            "description": (
                "For each support s, take r=s and add one at every valuation-one "
                "position of (1,2)^s; the word becomes (2)^(2s) and replays n=1."
            ),
        }
    return {
        "exists": False,
        "description": (
            "The primitive word contains valuation 4, and upward pulses cannot "
            "turn it into the all-2 itinerary of the trivial cycle."
        ),
    }


def semantic_digest(payload: dict[str, Any]) -> str:
    frozen = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(frozen).hexdigest()


def build_payload() -> dict[str, Any]:
    families = []
    for spec in FAMILIES:
        families.append(
            {
                "name": spec.name,
                "base": list(spec.base),
                "A": spec.A,
                "k": spec.k,
                "cmax": spec.cmax,
                "support_threshold": support_threshold_certificate(spec),
                "all_repetition_legendre": all_r_legendre_certificate(spec),
                "matveev": matveev_cutoff_certificate(spec),
                "convergents": convergent_exclusion_certificate(spec),
                "trivial_cycle": trivial_hit_classification(spec),
            }
        )
    payload: dict[str, Any] = {
        "experiment_id": EXPERIMENT_ID,
        "claim_id": CLAIM_ID,
        "verified_floor": N_STAR,
        "small_repetition_split": SMALL_R,
        "families": families,
        "conclusion": {
            "P3": "all nontrivial positive cycle lifts with fixed support 1..18 excluded",
            "P11": "all positive cycle lifts with fixed support 1..117 excluded",
            "first_uncovered_supports": {"P3": 19, "P11": 118},
        },
    }
    payload["semantic_sha256"] = semantic_digest(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"

    if args.output:
        args.output.write_text(text)
    if args.check_results:
        expected = json.loads(args.check_results.read_text())
        if expected != payload:
            raise SystemExit("frozen result mismatch")
    if not args.output:
        print(text, end="")


if __name__ == "__main__":
    main()
