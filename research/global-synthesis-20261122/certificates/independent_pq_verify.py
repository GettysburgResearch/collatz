#!/usr/bin/env python3
"""Independently check the exact finite and tail-separation data.

This checks the arithmetic certificate used by the written proof.  It is not
a formalization of Matveev or of the written real-logarithm coverage argument.
All failures raise exceptions even with Python optimization enabled.
"""

from copy import deepcopy
from fractions import Fraction
from pathlib import Path
import argparse
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def series_interval(z: int, count: int) -> tuple[Fraction, Fraction]:
    # Evaluate the geometric powers by recurrence, independently of the
    # generator's direct-power sum.
    ratio = Fraction(z - 1, z + 1)
    ratio_squared = ratio * ratio
    power = ratio
    lower = Fraction(0)
    for j in range(count):
        lower += 2 * power / (2 * j + 1)
        power *= ratio_squared
    upper = lower + 2 * power / ((2 * count + 1) * (1 - ratio_squared))
    return lower, upper


def compose_forward(word: str) -> tuple[int, int, int]:
    # Exact affine matrices: after j symbols the map is (A*x+C)/den.
    a, c, denominator = 1, 0, 1
    for bit in word:
        require(bit in "01", "Nonbinary word")
        if bit == "1":
            a, c = 3 * a, 3 * c + denominator
        denominator *= 2
    return a, c, denominator


def verify(data: dict) -> dict:
    require(data["schema"] == "collatz-independent-pq-v1", "Wrong schema")
    require(data["p_word"] == "11100011110" and data["q_word"] == "10", "Wrong blocks")
    p, q = data["p_word"], data["q_word"]
    p_a, p_c, p_d = compose_forward(p)
    q_a, q_c, q_d = compose_forward(q)
    require((p_a, p_c, p_d) == (2187, 5699, 2048), "P affine identity")
    require((q_a, q_c, q_d) == (3, 1, 4), "Q affine identity")
    constant = 4294967296
    coefficient = max(abs(p_d - p_a) + p_c, abs(q_d - q_a) + q_c)
    translation = 2 * (p_c + q_c)
    cutoff = 64 * (coefficient + 2 * translation + 2 * constant) ** 2
    require(int(data["matveev_constant"]) == constant, "Wrong Matveev specialization")
    require(int(data["block_coefficient_K"]) == coefficient, "Wrong K")
    require(int(data["translation_bound_B"]) == translation, "Wrong B")
    require(int(data["total_clock_cutoff_H"]) == cutoff, "Wrong total-clock cutoff")
    terms, threshold = data["logarithm_terms"], data["tail_threshold_a"]
    require(isinstance(terms, int) and 1 <= terms <= 1024, "Invalid logarithm truncation")
    require(isinstance(threshold, int) and 2 <= threshold <= 128, "Invalid finite threshold")
    lo2, hi2 = series_interval(2, terms)
    lo3, hi3 = series_interval(3, terms)
    require(lo2 > Fraction(1, 2), "Required lower bound on log 2")
    require(hi2 < Fraction(7, 10) and hi3 < Fraction(11, 10), "Required log-product bound")
    alpha_lo, alpha_hi = lo3 / hi2, hi3 / lo2
    left_n, left_d = map(int, data["farey_left"])
    right_n, right_d = map(int, data["farey_right"])
    require(min(left_n, left_d, right_n, right_d) > 0, "Nonpositive Farey data")
    require(left_d * right_n - left_n * right_d == 1, "Farey determinant is not one")
    require(left_d + right_d > cutoff, "Farey interval does not cover the clock cutoff")
    left, right = Fraction(left_n, left_d), Fraction(right_n, right_d)
    require(left < alpha_lo < alpha_hi < right, "Logarithm enclosure is not strictly inside Farey neighbors")
    require(right - alpha_hi > Fraction(168, 2048 ** threshold), "Insufficient all-tail gap")
    require(Fraction(6561, 8192) < 1 - Fraction(42, 2048), "b >= a reduction failed")
    require(Fraction(42, 2048) < Fraction(1, 2), "Small-deficit logarithm bound failed")
    expected_pairs = {(a, b) for a in range(1, threshold) for b in range(1, a)}
    actual_pairs = [(row["a"], row["b"]) for row in data["finite_rows"]]
    require(len(actual_pairs) == len(set(actual_pairs)), "Duplicate finite pair")
    require(set(actual_pairs) == expected_pairs, "Incomplete finite-pair coverage")
    positive_denominators = 0
    for row in data["finite_rows"]:
        a, b = row["a"], row["b"]
        slope, numerator, denominator_power = compose_forward(p * a + q * b)
        denominator = denominator_power - slope
        require(slope == 3 ** (7 * a + b), "Odd count mismatch")
        require(denominator_power == 2 ** (11 * a + 2 * b), "Shortcut clock mismatch")
        require(numerator > 0, "Nonpositive formal correction")
        if denominator <= 0:
            require(row["outcome"] == "nonpositive_denominator", "Wrong sign classification")
        else:
            positive_denominators += 1
            remainder = numerator % denominator
            require(row["outcome"] == "nonzero_remainder", "Wrong divisibility classification")
            require(remainder > 0, "Candidate has a positive integer periodic point")
            require(int(row["remainder"]) == remainder, "Incorrect whole-denominator remainder")
    return {"status": "exact arithmetic certificate verified",
            "cutoff_H": str(cutoff), "tail_a_ge": threshold,
            "finite_pairs": len(expected_pairs),
            "positive_denominator_checks": positive_denominators,
            "nonpositive_denominator_checks": len(expected_pairs) - positive_denominators}


def mutation_checks(data: dict) -> list[str]:
    mutations = []
    changed = deepcopy(data)
    changed["farey_right"][0] = str(int(changed["farey_right"][0]) + 1)
    mutations.append(("altered Farey endpoint", changed))
    changed = deepcopy(data)
    changed["total_clock_cutoff_H"] = str(int(changed["total_clock_cutoff_H"]) - 1)
    mutations.append(("altered theorem cutoff", changed))
    changed = deepcopy(data)
    changed["finite_rows"].pop()
    mutations.append(("missing finite pair", changed))
    changed = deepcopy(data)
    row = next(row for row in changed["finite_rows"] if row["outcome"] == "nonzero_remainder")
    row["remainder"] = str(int(row["remainder"]) + 1)
    mutations.append(("altered full-denominator remainder", changed))
    rejected = []
    for name, changed in mutations:
        try:
            verify(changed)
        except (ValueError, KeyError, TypeError):
            rejected.append(name)
        else:
            raise ValueError(f"Corruption was accepted: {name}")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", nargs="?", type=Path,
                        default=Path(__file__).with_name("independent_pq_certificate.json"))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text(encoding="utf-8"))
    result = verify(data)
    if args.self_test:
        result["rejected_corruptions"] = mutation_checks(data)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
