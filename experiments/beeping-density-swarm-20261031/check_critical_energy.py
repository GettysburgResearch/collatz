#!/usr/bin/env python3
"""Two exact constructions and finite overlap checks; no asymptotic proof by testing."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def geometric_law(nums: list[int], den: int, q: int) -> tuple[list[int], int]:
    """Sum the entire geometric exponent law by its modular period."""
    modulus = 3 ** q
    period = 2 * 3 ** (q - 1)
    inverse_two = pow(2, -1, modulus)
    output = [0] * modulus
    power = 1
    for a in range(1, period + 1):
        power = power * inverse_two % modulus
        numerator_weight = 1 << (period - a)
        for r, numerator in enumerate(nums):
            output[((3 * r + 1) * power) % modulus] += numerator * numerator_weight
    denominator = den * ((1 << period) - 1)
    require(sum(output) == denominator, "geometric-law mass")
    return output, denominator


def doubling_solution(previous: list[F], q: int) -> list[F]:
    """Solve the full cyclic doubling recursion, independently of exponent convolution."""
    modulus = 3 ** q
    period = 2 * 3 ** (q - 1)
    cycle = []
    r = 1
    for _ in range(period):
        cycle.append(r)
        r = 2 * r % modulus
    require(r == 1 and len(set(cycle)) == period, "unit doubling cycle")
    forcing = [previous[((2 * r - 1) // 3) % len(previous)]
               if r % 3 == 2 else F(0) for r in cycle]
    numerator = sum((F(1 << (period - 1 - j)) * value
                     for j, value in enumerate(forcing)), F(0))
    start = 3 * numerator / ((1 << period) - 1)
    current = start
    result = [F(0)] * modulus
    for r, value in zip(cycle, forcing):
        result[r] = current
        current = 2 * current - 3 * value
    require(current == start, "cyclic recurrence closure")
    return result


def canonical_hash(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def run(max_level: int) -> dict:
    nums, den = [1], 1
    previous = [F(1)]
    previous_energy = F(1)
    rows = []
    residue_checks = 0
    projective_checks = 0
    for q in range(1, max_level + 1):
        nums, den = geometric_law(nums, den, q)
        modulus = 3 ** q
        rho = [F(modulus * n, den) for n in nums]
        alternative = doubling_solution(previous, q)
        require(rho == alternative, f"whole-law independent agreement at q={q}")
        require(all(v >= 0 for v in rho), "nonnegative density")
        require(sum(rho) == modulus, "mean-one density")
        cross = F(0)
        alternate_cross = F(0)
        for r in range(modulus):
            branch = previous[((2 * r - 1) // 3) % len(previous)] if r % 3 == 2 else F(0)
            a = rho[(2 * r) % modulus] / 2
            b = 3 * branch / 2
            require(rho[r] == a + b, "full finite recursion")
            require(r % 3 != 0 or rho[r] == 0, "unit support")
            cross += a * b / modulus
            alternate_cross += 2 * rho[(2 * r) % modulus] * branch / modulus
            residue_checks += 1
        for r in range(len(previous)):
            require(sum(rho[r + j * len(previous)] for j in range(3)) / 3 == previous[r],
                    "projective martingale relation")
            projective_checks += 1
        energy = sum((v * v for v in rho), F(0)) / modulus
        require(energy - previous_energy == F(8, 3) * cross, "energy overlap coefficient")
        require(energy - previous_energy == alternate_cross, "second energy expression")
        require(cross > 0, "finite positive overlap")
        rows.append({"level": q, "residues": modulus, "second_moment": str(energy),
                     "increment": str(energy - previous_energy), "overlap_integral": str(cross),
                     "whole_density_sha256": canonical_hash([str(v) for v in rho])})
        previous = rho
        previous_energy = energy
    payload = {"status": "PASS", "max_level": max_level,
               "scope": "exact bounded recursion, projectivity and energy checks; unbounded second moment follows from the written proof",
               "infinite_geometric_tails_summed_exactly": True,
               "complete_density_comparisons": max_level,
               "residue_checks": residue_checks, "projective_checks": projective_checks,
               "rows": rows, "external_Lean_replayed": False, "Collatz_proved": False}
    return {"payload": payload, "semantic_sha256": canonical_hash(payload)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-level", type=int, default=6)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not 1 <= args.max_level <= 7:
        parser.error("the bounded replay supports levels 1 through 7")
    report = run(args.max_level)
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "semantic_sha256": report["semantic_sha256"],
                      "residue_checks": report["payload"]["residue_checks"],
                      "projective_checks": report["payload"]["projective_checks"]}))


if __name__ == "__main__":
    main()
