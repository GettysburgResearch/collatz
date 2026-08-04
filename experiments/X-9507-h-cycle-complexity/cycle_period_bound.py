#!/usr/bin/env python3
"""Exact certificate extending the finite H cycle exclusion.

Uses rational interval bounds for log(4/3) and log(9/8), Legendre's theorem,
and the ordinary-state sweep bound from X-9506. Standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

B0 = 3 * 2**65
L0 = 2_479_700_524
EXPECTED_CF = [2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3, 1, 1, 15, 1, 9]


def log_bounds(z: Fraction, terms: int = 120) -> tuple[Fraction, Fraction]:
    """Bound log((1+z)/(1-z)) by truncating its positive atanh series."""
    z2 = z * z
    power = z
    partial = Fraction(0)
    for k in range(terms):
        partial += power / (2 * k + 1)
        power *= z2
    lo = 2 * partial
    # Every denominator in the remaining tail is at least 2*terms+1.
    rem = 2 * power / ((2 * terms + 1) * (1 - z2))
    return lo, lo + rem


def cf_interval(lo: Fraction, hi: Fraction, count: int) -> list[int]:
    """Recover a continued-fraction prefix common to an exact rational interval."""
    out: list[int] = []
    for _ in range(count):
        a = lo.numerator // lo.denominator
        b = hi.numerator // hi.denominator
        if a != b:
            raise AssertionError(("continued-fraction interval split", a, b))
        out.append(a)
        lo -= a
        hi -= a
        if lo <= 0:
            raise AssertionError("interval reached integer boundary")
        lo, hi = 1 / hi, 1 / lo
    return out


def convergents(cf: list[int]) -> list[tuple[int, int, int]]:
    p2, p1 = 0, 1
    q2, q1 = 1, 0
    out: list[tuple[int, int, int]] = []
    for i, a in enumerate(cf):
        p = a * p1 + p2
        q = a * q1 + q2
        out.append((i, p, q))
        p2, p1 = p1, p
        q2, q1 = q1, q
    return out


def audit() -> dict[str, object]:
    # log(4/3) = 2*atanh(1/7), log(9/8) = 2*atanh(1/17).
    A_lo, A_hi = log_bounds(Fraction(1, 7))
    b_lo, b_hi = log_bounds(Fraction(1, 17))
    k_lo = A_lo / b_hi
    k_hi = A_hi / b_lo

    cf = cf_interval(k_lo, k_hi, len(EXPECTED_CF))
    if cf != EXPECTED_CF:
        raise AssertionError((cf, EXPECTED_CF))
    conv = convergents(cf)

    if not (18 * L0 * L0 + L0 < B0 <= 18 * (L0 + 1) * (L0 + 1) + (L0 + 1)):
        raise AssertionError("Legendre range endpoint mismatch")

    certs: list[dict[str, int]] = []
    for i, p, q in conv:
        if q > L0:
            break
        # Certify that p/q is strictly below kappa.
        if Fraction(p, q) < k_lo:
            max_multiple = L0 // q
            # x = q*log(4/3)-p*log(9/8) has this positive lower bound.
            x_lo = q * A_lo - p * b_hi
            if x_lo <= 0:
                raise AssertionError("nonpositive logarithmic gap")
            # For every m <= max_multiple,
            # mq/(1-exp(-m*x)) <= q/x + mq.
            upper = Fraction(q, 1) / x_lo + max_multiple * q
            if not upper < B0:
                raise AssertionError(("cycle cap not certified", i, p, q, max_multiple))
            certs.append(
                {
                    "index": i,
                    "R": p,
                    "L": q,
                    "max_multiple": max_multiple,
                    "upper_floor": upper.numerator // upper.denominator,
                }
            )

    payload: dict[str, object] = {
        "ordinary_sweep_bound_exclusive": B0,
        "cycle_length_limit": L0,
        "continued_fraction_prefix": cf,
        "convergents": [{"index": i, "R": p, "L": q} for i, p, q in conv],
        "lower_convergent_certificates": certs,
        "last_lower_convergent": {"R": 2_733_776_749, "L": 1_119_265_172},
        "next_convergent": {"R": 27_172_759_629, "L": 11_125_094_063, "side": "upper"},
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["digest_sha256"] = hashlib.sha256(raw).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = audit()
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
