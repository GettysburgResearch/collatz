#!/usr/bin/env python3
"""Exact finite ternary densities and calibrated inverse horizons.

This computes finite rational quantities.  It does not test Collatz
convergence or promote a finite horizon to an infinite one.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


def density_levels(depth: int) -> list[tuple[list[int], int]]:
    """Return common-denominator arrays for D_r=P^r 1, 0<=r<=depth."""
    levels = [([1], 1)]
    for r in range(depth):
        previous, denominator = levels[-1]
        source_modulus = 3**r
        target_modulus = 3 * source_modulus
        period = 2 * source_modulus
        powers = [pow(2, e, target_modulus) for e in range(1, period + 1)]
        values: list[int] = []
        for q in range(target_modulus):
            numerator = 0
            for e, power in enumerate(powers, start=1):
                residue = power * q % target_modulus
                if residue % 3 == 1:
                    parent = (residue - 1) // 3
                    numerator += 3 * (previous[parent] << (period - e))
            values.append(numerator)
        levels.append((values, denominator * ((1 << period) - 1)))
    return levels


def as_fraction(data: tuple[list[int], int], residue: int) -> Fraction:
    values, denominator = data
    return Fraction(values[residue % len(values)], denominator)


def fourth_root_floor(numerator: int, denominator: int) -> int:
    """Largest H with H^4 * numerator <= denominator, using integers only."""
    if numerator <= 0 or denominator <= 0:
        raise ValueError("positive numerator and denominator required")
    lo, hi = 0, 1
    while hi**4 * numerator <= denominator:
        lo, hi = hi, 2 * hi
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**4 * numerator <= denominator:
            lo = mid
        else:
            hi = mid
    return lo


def audit_levels(levels: list[tuple[list[int], int]]) -> dict[str, int]:
    """Check exact density consistency and literal ordinary inverse rows."""
    consistency_cells = 0
    ordinary_rows = 0
    for r, (values, denominator) in enumerate(levels):
        if min(values) < 0 or sum(values) != len(values) * denominator:
            raise ValueError(f"density normalization failed at depth {r}")
        if max(values) > (2**r) * denominator:
            raise ValueError(f"row norm bound failed at depth {r}")
        if r:
            prior_values, prior_denominator = levels[r - 1]
            modulus = len(prior_values)
            for a in range(modulus):
                coarse_sum = sum(values[a + j * modulus] for j in range(3))
                if coarse_sum * prior_denominator != 3 * prior_values[a] * denominator:
                    raise ValueError(f"ternary consistency failed at {(r, a)}")
                consistency_cells += 1
        if 1 <= r <= 4:
            source_modulus = 3 ** (r - 1)
            period = 2 * source_modulus
            cutoff = 2 * period
            for residue in range(3**r):
                # A positive odd representative; all literal parents are positive odd.
                q = residue if residue > 0 and residue % 2 else residue + 3**r
                partial = Fraction(0)
                for e in range(1, cutoff + 1):
                    top = (1 << e) * q - 1
                    if top % 3 == 0:
                        n = top // 3
                        if n <= 0 or n % 2 != 1:
                            raise ValueError("invalid ordinary parent")
                        partial += Fraction(3, 1 << e) * as_fraction(levels[r - 1], n)
                exact = as_fraction(levels[r], residue)
                tail = exact - partial
                if not (0 <= tail <= Fraction(3 * 2 ** (r - 1), 1 << cutoff)):
                    raise ValueError(f"ordinary inverse row tail failed at {(r, residue)}")
                if tail != exact / (1 << cutoff):
                    raise ValueError(f"periodic geometric remainder failed at {(r, residue)}")
                ordinary_rows += 1
    return {"consistency_cells": consistency_cells, "ordinary_rows": ordinary_rows}


def certificate(max_block: int) -> dict:
    if not 1 <= max_block <= 4:
        raise ValueError("choose a finite block size between 1 and 4")
    levels = density_levels(2 * max_block)
    checks = audit_levels(levels)
    rows = []
    for m in range(1, max_block + 1):
        fine, fine_denominator = levels[2 * m]
        coarse, coarse_denominator = levels[m]
        ratio, remainder = divmod(fine_denominator, coarse_denominator)
        if remainder:
            raise ValueError("common-denominator nesting failed")
        discrepancy = sum(abs(v - coarse[i % len(coarse)] * ratio) for i, v in enumerate(fine))
        epsilon = Fraction(discrepancy, len(fine) * fine_denominator)
        cylinder_floor = 2 * (Fraction(1, 4)**m - Fraction(2, 9)**m)
        simple_floor = Fraction(2, 9) * Fraction(1, 4)**m
        if not (0 < simple_floor <= cylinder_floor <= epsilon):
            raise ValueError("ordinary cylinder error floor failed")
        if Fraction(fine[-1], fine_denominator) < Fraction(9, 4)**m:
            raise ValueError("all-one cylinder contribution failed")
        intrinsic_horizon = fourth_root_floor(epsilon.numerator, epsilon.denominator)
        if intrinsic_horizon**4 * epsilon > 1 or (intrinsic_horizon + 1)**4 * epsilon <= 1:
            raise ValueError("intrinsic quartic horizon maximality failed")
        if 2 * intrinsic_horizon**4 > 9 * 4**m:
            raise ValueError("intrinsic calibration ceiling failed")
        regularized = epsilon + Fraction(1, 9**m)
        horizon = fourth_root_floor(regularized.numerator, regularized.denominator)
        if horizon**4 * regularized > 1 or (horizon + 1)**4 * regularized <= 1:
            raise ValueError("quartic horizon maximality failed")
        if horizon > intrinsic_horizon:
            raise ValueError("regularized horizon exceeded intrinsic horizon")
        rows.append({
            "m": m,
            "epsilon": str(epsilon),
            "regularized_error": str(regularized),
            "H": horizon,
            "intrinsic_H": intrinsic_horizon,
            "cylinder_error_lower_bound": str(cylinder_floor),
            "simple_error_lower_bound": str(simple_floor),
            "minimum_floor": 9**m,
            "uniform_density_bound": str(Fraction(4, 9)**m + Fraction(9, m * horizon**2))
            if horizon else None,
            "fine_density_sha256": sha256(json.dumps(fine, separators=(",", ":")).encode()).hexdigest(),
        })
    return {
        "schema": "collatz-exact-mixing-horizon/v2",
        "scope": "exact finite rational matrices; no infinite-depth or convergence claim",
        "max_block": max_block,
        "checks": checks,
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-block", type=int, default=3)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    result = certificate(args.max_block)
    if args.check:
        existing = json.loads(args.check.read_text(encoding="utf8"))
        if existing != result:
            raise SystemExit("certificate differs from exact regeneration")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf8")
    print(json.dumps({"status": "passed", "max_block": args.max_block,
                      "checks": result["checks"],
                      "horizons": [row["H"] for row in result["rows"]],
                      "intrinsic_horizons": [row["intrinsic_H"] for row in result["rows"]]}, sort_keys=True))


if __name__ == "__main__":
    main()
