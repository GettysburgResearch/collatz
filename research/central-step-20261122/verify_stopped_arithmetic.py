#!/usr/bin/env python3
"""Check the finite sibling arithmetic quoted in STOPPED_MIXING.md.

The imported density generator sums each complete periodic valuation family
with its exact geometric denominator. This checks finite rational statements,
not a comparison of the infinite canonical profile G.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


def decimal_string(value: Fraction) -> str:
    with localcontext() as context:
        context.prec = 25
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def certificate() -> dict:
    repo = Path(__file__).resolve().parents[2]
    source = repo / "research/lean-joint-20261122/finite_density_certificate.py"
    spec = importlib.util.spec_from_file_location("pinned_finite_density", source)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load the existing exact density generator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    levels = module.density_levels(6)

    averages = []
    for depth in range(1, 7):
        values, denominator = levels[depth]
        modulus = 3**depth
        period = 3 ** (depth - 1)
        for root in (1, 5):
            current = root % modulus
            orbit = []
            for _ in range(period):
                orbit.append(current)
                current = (64 * current + 21) % modulus
            expected = {q for q in range(modulus) if q % 3 == root % 3}
            if current != root % modulus or set(orbit) != expected:
                raise ValueError("the B orbit does not exhaust its residue class")
            if len(set(orbit)) != period:
                raise ValueError("a B residue orbit repeats too soon")
            average = Fraction(sum(values[q] for q in orbit), period * denominator)
            coarse = module.as_fraction(levels[1], root)
            if average != coarse:
                raise ValueError("exact ternary sibling average failed")
            averages.append({
                "depth": depth,
                "root": root,
                "modulus": modulus,
                "orbit_length": period,
                "exact_average": str(average),
                "D_1": str(coarse),
            })

    n = 2 * 3**6 - 1
    sibling = 64 * n + 21
    original_density = module.as_fraction(levels[6], n)
    sibling_density = module.as_fraction(levels[6], sibling)
    ratio = sibling_density / original_density
    if not (original_density > 16 and sibling_density < 1 and ratio < Fraction(1, 16)):
        raise ValueError("the quoted exact depth-six inequalities failed")
    return {
        "schema": "collatz-stopped-sibling-arithmetic/v1",
        "scope": "finite rational densities; no canonical G comparison or Collatz conclusion",
        "generator": str(source.relative_to(repo)),
        "generator_sha256": sha256(source.read_bytes()).hexdigest(),
        "valuation_tail": "complete periodic geometric sums; no exponent cutoff",
        "residue_averages": averages,
        "diagnostic": {
            "depth": 6,
            "n": n,
            "B_n": sibling,
            "D_6_n": str(original_density),
            "D_6_B_n": str(sibling_density),
            "ratio": str(ratio),
            "D_6_n_decimal": decimal_string(original_density),
            "D_6_B_n_decimal": decimal_string(sibling_density),
            "ratio_decimal": decimal_string(ratio),
            "D_6_n_gt_16": True,
            "D_6_B_n_lt_1": True,
            "ratio_lt_one_sixteenth": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    result = certificate()
    if args.check and json.loads(args.check.read_text(encoding="utf-8")) != result:
        raise SystemExit("stored certificate differs from exact regeneration")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "passed",
        "exact_residue_averages": len(result["residue_averages"]),
        "n": result["diagnostic"]["n"],
        "B_n": result["diagnostic"]["B_n"],
        "ratio_decimal": result["diagnostic"]["ratio_decimal"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
