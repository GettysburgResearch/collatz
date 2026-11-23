#!/usr/bin/env python3
"""Generate exact arithmetic data for all independent P^a Q^b cycles.

The mathematical coverage theorem is in ARITHMETIC_CLOSURE.md.  This script
does not claim to prove Matveev's theorem or the analytic coverage argument.
No floating point arithmetic, Collatz census, or external package is used.
"""

from fractions import Fraction
from pathlib import Path
import json


def log_bounds(z: int, terms: int) -> tuple[Fraction, Fraction]:
    t = Fraction(z - 1, z + 1)
    lower = 2 * sum((t ** (2 * j + 1) / (2 * j + 1)
                     for j in range(terms)), Fraction(0))
    remainder = 2 * t ** (2 * terms + 1) / ((2 * terms + 1) * (1 - t * t))
    return lower, lower + remainder


def affine(bits: str) -> tuple[int, int, int]:
    length, odd, correction = 0, 0, 0
    for bit in bits:
        if bit == "1":
            correction = 3 * correction + 2 ** length
            odd += 1
        elif bit != "0":
            raise ValueError("Not a binary word")
        length += 1
    return length, odd, correction


def main() -> None:
    p_word, q_word = "11100011110", "10"
    blocks = [affine(p_word), affine(q_word)]
    constant = 2 ** 32
    coefficient = max(abs(2 ** length - 3 ** odd) + correction
                      for length, odd, correction in blocks)
    translation = 2 * sum(correction for _, _, correction in blocks)
    cutoff = (2 ** 3 * (coefficient + 2 * translation + 2 * constant)) ** 2
    terms, threshold = 128, 16
    l2, u2 = log_bounds(2, terms)
    l3, u3 = log_bounds(3, terms)
    alpha_lo, alpha_hi = l3 / u2, u3 / l2
    left_n, left_d, right_n, right_d = 1, 1, 2, 1
    iterations = 0
    while left_d + right_d <= cutoff:
        mid_n, mid_d = left_n + right_n, left_d + right_d
        mid = Fraction(mid_n, mid_d)
        if mid <= alpha_lo:
            left_n, left_d = mid_n, mid_d
        elif mid >= alpha_hi:
            right_n, right_d = mid_n, mid_d
        else:
            raise ValueError("Increase logarithm precision")
        iterations += 1
    if Fraction(right_n, right_d) - alpha_hi <= Fraction(168, 2048 ** threshold):
        raise ValueError("Tail gap does not close")
    rows = []
    for a in range(1, threshold):
        for b in range(1, a):
            denominator = 2048 ** a * 4 ** b - 2187 ** a * 3 ** b
            numerator = (2048 ** a * 4 ** b - 42 * 2048 ** a * 3 ** b
                         + 41 * 2187 ** a * 3 ** b)
            if denominator <= 0:
                rows.append({"a": a, "b": b, "outcome": "nonpositive_denominator"})
            else:
                remainder = numerator % denominator
                if remainder == 0:
                    raise ValueError(f"Unexcluded ordinary candidate: {(a, b)}")
                rows.append({"a": a, "b": b, "outcome": "nonzero_remainder",
                             "remainder": str(remainder)})
    output = {
        "schema": "collatz-independent-pq-v1",
        "scope": "All independent integers a,b >= 1; no positive ordinary cycle P^a Q^b",
        "p_word": p_word,
        "q_word": q_word,
        "logarithm_terms": terms,
        "tail_threshold_a": threshold,
        "matveev_constant": str(constant),
        "block_coefficient_K": str(coefficient),
        "translation_bound_B": str(translation),
        "total_clock_cutoff_H": str(cutoff),
        "farey_left": [str(left_n), str(left_d)],
        "farey_right": [str(right_n), str(right_d)],
        "generator_iterations": iterations,
        "finite_rows": rows,
    }
    path = Path(__file__).with_name("independent_pq_certificate.json")
    path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"written": path.name, "cutoff_H": str(cutoff),
                      "farey_left": output["farey_left"],
                      "farey_right": output["farey_right"],
                      "tail_a_ge": threshold, "finite_rows": len(rows)}, indent=2))


if __name__ == "__main__":
    main()
