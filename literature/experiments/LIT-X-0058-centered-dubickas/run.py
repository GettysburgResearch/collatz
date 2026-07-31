#!/usr/bin/env python3
"""Exact rational constants for the Dubickas centered-power specialization.

This script does not prove the external theorems. It certifies all numerical
specializations and comparisons used by LIT-KTHM-0058.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

sys.set_int_max_str_digits(0)


def product_interval(r: Fraction, factors: int = 16) -> tuple[Fraction, Fraction]:
    """Return rigorous lower/upper bounds for prod_{m>=0}(1-r^(2^m))."""
    p = Fraction(1)
    for m in range(factors):
        p *= 1 - r ** (2**m)
    a = r ** (2**factors)
    tail_sum_upper = a / (1 - a)
    if tail_sum_upper >= 1:
        raise AssertionError("tail bound too coarse")
    return p * (1 - tail_sum_upper), p


def E_interval(r: Fraction, factors: int = 16) -> tuple[Fraction, Fraction]:
    t_lo, t_hi = product_interval(r, factors)
    return (
        (1 - (1 - r) * t_hi) / (2 * r),
        (1 - (1 - r) * t_lo) / (2 * r),
    )


def decimal_bounds(lo: Fraction, hi: Fraction, digits: int = 24) -> dict[str, str]:
    scale = 10**digits
    lo_n = lo.numerator * scale // lo.denominator
    hi_n = (hi.numerator * scale + hi.denominator - 1) // hi.denominator

    def fmt(n: int) -> str:
        q, rem = divmod(n, scale)
        return f"{q}.{rem:0{digits}d}"

    return {"lo": fmt(lo_n), "hi": fmt(hi_n)}


def frac_sha(x: Fraction) -> str:
    return hashlib.sha256(f"{x.numerator}/{x.denominator}".encode()).hexdigest()


def build() -> dict[str, object]:
    r_direct = Fraction(64, 81)
    e_lo, e_hi = E_interval(r_direct)
    rho_direct = (e_lo / 81, e_hi / 81)

    t23_lo, t23_hi = product_interval(Fraction(2, 3))
    rho32 = ((3 - t23_hi) / 12, (3 - t23_lo) / 12)
    rho_lift = (rho32[0] / 27, rho32[1] / 27)

    threshold = Fraction(1, 81)
    phase2_max = Fraction(2, 9)
    if not rho32[0] > phase2_max:
        raise AssertionError("large 3/2 limit point not forced into phase 3")
    if not rho_lift[0] > rho_direct[1]:
        raise AssertionError("four-phase lift does not improve direct bound")
    if not rho_lift[1] < threshold:
        raise AssertionError("lifted source bound would already solve the problem")

    return {
        "description": "Exact source-specialization constants for centered 81/64",
        "product_factors": 16,
        "T_64_over_81": decimal_bounds(*product_interval(r_direct)),
        "E_64_over_81": decimal_bounds(e_lo, e_hi),
        "rho_direct_E_over_81": decimal_bounds(*rho_direct),
        "T_2_over_3": decimal_bounds(t23_lo, t23_hi),
        "rho_3_over_2_large_limit_point": decimal_bounds(*rho32),
        "rho_lifted_to_81_over_64": decimal_bounds(*rho_lift),
        "allowed_radius_1_over_81": decimal_bounds(threshold, threshold),
        "lift_improves_direct_bound": True,
        "lift_still_subcritical": True,
        "phase_0_1_2_distance_maxima": ["8/81", "4/27", "2/9"],
        "phase3_identity": "||8*xi*(3/2)^(4n+3)|| = 27*|u_n|",
        "certificate_sha256": hashlib.sha256(
            "|".join([
                frac_sha(rho_direct[0]),
                frac_sha(rho_direct[1]),
                frac_sha(rho_lift[0]),
                frac_sha(rho_lift[1]),
            ]).encode()
        ).hexdigest(),
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
            raise SystemExit("centered Dubickas result mismatch")
    print(payload, end="")


if __name__ == "__main__":
    main()
