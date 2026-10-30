#!/usr/bin/env python3
"""Exact finite checks of the negative reference-law spike and positive run cap.

All tests use exact integers/Fractions. Infinite geometric exponent sums are
evaluated exactly by their period modulo 3**q, rather than truncated.
This does not prove a source-conditioned transported density estimate.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path


def v3(n: int) -> int:
    if n <= 0:
        raise ValueError("v3 expects a positive integer")
    power = 0
    while n % 3 == 0:
        n //= 3
        power += 1
    return power


def next_law(numerators: list[int], denominator: int,
             q: int) -> tuple[list[int], int]:
    modulus = 3 ** q
    period = 2 * 3 ** (q - 1)
    period_denominator = (1 << period) - 1
    updated = [0] * modulus
    inv_two = pow(2, -1, modulus)
    multiplier = 1
    for a in range(1, period + 1):
        multiplier = multiplier * inv_two % modulus
        weight = 1 << (period - a)
        for residue, mass in enumerate(numerators):
            if mass:
                dest = multiplier * (3 * residue + 1) % modulus
                updated[dest] += mass * weight
    new_denominator = denominator * period_denominator
    if multiplier != 1 or sum(updated) != new_denominator:
        raise AssertionError(("geometric law normalization", q))
    return updated, new_denominator


def compositions(total: int, length: int):
    if length == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - length + 2):
        for rest in compositions(total - first, length - 1):
            yield (first, *rest)


def positive_word_checks() -> dict[str, int]:
    legal_words = 0
    layers = 0
    for target in range(1, 102, 2):
        for q in range(1, 5):
            all_sources: set[int] = set()
            for total in range(q, 13):
                sources: set[int] = set()
                for word in compositions(total, q):
                    current = target
                    for a in word:
                        numerator = (1 << a) * current - 1
                        if numerator % 3:
                            break
                        current = numerator // 3
                    else:
                        if current <= 0 or current % 2 == 0:
                            raise AssertionError(("positive integral fiber", target, word))
                        if current in all_sources:
                            raise AssertionError(("fixed-depth source collision", target, word))
                        if 3 ** q * current >= (1 << total) * target:
                            raise AssertionError(("positive affine offset", target, word))
                        all_sources.add(current)
                        sources.add(current)
                        legal_words += 1
                if 3 ** q * len(sources) > target * (1 << total):
                    raise AssertionError(("single-layer mass bound", target, q, total))
                layers += 1
    return {"targets": 51, "maximum_depth": 4, "maximum_total_valuation": 12,
            "legal_words_checked": legal_words, "layers_checked": layers}


def run(max_level: int = 6, source_limit: int = 10001) -> dict:
    numerators, denominator = [1], 1
    rows = []
    exact_tail_checks = 0
    exact_annulus_checks = 0
    positive_density_bound_checks = 0
    for q in range(1, max_level + 1):
        numerators, denominator = next_law(numerators, denominator, q)
        modulus = 3 ** q
        negative_height = Fraction(modulus * numerators[-1], denominator)
        lower_height = Fraction(3, 2) ** q
        if negative_height < lower_height:
            raise AssertionError(("negative spike", q))
        for target in range(1, 1002, 2):
            actual = Fraction(modulus * numerators[target % modulus], denominator)
            bound = 6 * q * target + Fraction(64, 81) ** q
            if actual > bound:
                raise AssertionError(("positive pointwise density bound", target, q))
            positive_density_bound_checks += 1
        for k in range(1, q + 1):
            uk = Fraction(3, 2) ** k / 2
            tail = Fraction(sum(max(modulus * value * uk.denominator
                                    - uk.numerator * denominator, 0)
                                for value in numerators),
                            modulus * denominator * uk.denominator)
            if tail < Fraction(1, 2 ** (k + 1)):
                raise AssertionError(("clipping lower tail", q, k, tail))
            exact_tail_checks += 1
        for k in range(q):
            annulus_mass = Fraction(sum(
                value for y, value in enumerate(numerators)
                if (y + 1) % (3 ** k) == 0
                and (y + 1) % (3 ** (k + 1)) != 0), denominator)
            if annulus_mass < Fraction(1, 2 ** (k + 2)):
                raise AssertionError(("annulus probability", q, k))
            exact_annulus_checks += 1
        third_moment = Fraction(modulus ** 2 * sum(v ** 3 for v in numerators),
                                denominator ** 3)
        third_lower = Fraction(9, 8) ** q + sum(
            (Fraction(9, 256) * Fraction(9, 8) ** k for k in range(q)),
            Fraction(0))
        if third_moment < third_lower:
            raise AssertionError(("disjoint-annuli moment lower bound", q))
        rows.append({"level": q, "residues": modulus,
                     "exact_denominator_bits": denominator.bit_length(),
                     "negative_height": str(negative_height),
                     "negative_height_decimal": float(negative_height),
                     "proved_height_lower_bound": str(lower_height),
                     "third_moment_decimal": float(third_moment),
                     "third_moment_proved_lower_bound": str(third_lower)})
    source_checks = 0
    for t in range(1, source_limit + 1, 2):
        cap = v3(t + 1)
        current = t
        for r in range(1, cap + 1):
            if (2 * current - 1) % 3:
                raise AssertionError(("prefix legality", t, r))
            current = (2 * current - 1) // 3
            expected = 2 ** r * ((t + 1) // 3 ** r) - 1
            if current != expected or current <= 0 or current % 2 == 0:
                raise AssertionError(("physical inverse formula", t, r))
        if (2 * current - 1) % 3 == 0:
            raise AssertionError(("run cap not exact", t, cap))
        source_checks += 1
    for r in range(1, 513):
        t = 2 * 3 ** r - 1
        if v3(t + 1) != r or (2 ** r * ((t + 1) // 3 ** r) - 1) != 2 ** (r + 1) - 1:
            raise AssertionError(("arbitrarily long positive finite witness", r))
        mod = 3 ** (r + 1)
        annulus_residue = (5 * 3 ** r * pow(2 ** (r + 2), -1, mod) - 1) % mod
        if v3(annulus_residue + 1) != r:
            raise AssertionError(("annulus congruence", r))
    delta = math.log(2) / math.log(1.5)
    return {
        "schema": "collatz-negative-reference-spike-v1",
        "status": "EXACT_BOUNDED_REPLAY_OPEN_TRANSPORT_BUDGET",
        "normalization": "rho_q=3^q*Pr(Y_q=y), full-group mean one",
        "max_reference_level": max_level,
        "reference_laws": rows,
        "exact_tail_checks": exact_tail_checks,
        "exact_annulus_checks": exact_annulus_checks,
        "positive_odd_source_cap_checks": source_checks,
        "positive_pointwise_density_bound_checks": positive_density_bound_checks,
        "positive_fixed_depth_word_checks": positive_word_checks(),
        "arbitrary_length_family_checked_through": 512,
        "critical_tail_exponent_approximation": delta,
        "critical_strong_moment_approximation": 1 + delta,
        "global_clipping_target_exponent_barrier_approximation": math.log2(3),
        "source_conditioned_transport_bound_proved": False,
        "full_Collatz_proved": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-level", type=int, default=6)
    parser.add_argument("--source-limit", type=int, default=10001)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not 1 <= args.max_level <= 7:
        raise ValueError("This bounded verifier supports reference levels 1..7.")
    result = run(args.max_level, args.source_limit)
    body = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(body, encoding="utf-8")
        print(json.dumps({"output": str(args.output),
                          "max_reference_level": result["max_reference_level"],
                          "exact_tail_checks": result["exact_tail_checks"],
                          "positive_odd_source_cap_checks": result["positive_odd_source_cap_checks"],
                          "full_Collatz_proved": False}, sort_keys=True))
    else:
        print(body, end="")


if __name__ == "__main__":
    main()
