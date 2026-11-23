#!/usr/bin/env python3
"""Emit exact finite length-bound certificates, not a claimed full census.

The theorem and the external Matveev input are in BOUNDED_POWER_LANGUAGES.md.
Only Python integers and fractions are used. No exponent samples are used
to infer a statement about an infinite language.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path

MATVEEV_K = 1 << 33


def affine(word: str) -> dict:
    if not word or any(bit not in "01" for bit in word):
        raise ValueError("a base block must be a nonempty binary word")
    a, c, denominator = 1, 0, 1
    for bit in word:
        if bit == "1":
            a, c = 3 * a, 3 * c + denominator
        denominator *= 2
    return {
        "word": word,
        "length": len(word),
        "odd_count": word.count("1"),
        "a": a,
        "C": c,
        "D": denominator - a,
    }


def positive_fixed_cycle(data: dict) -> dict | None:
    c, d = data["C"], data["D"]
    if d <= 0 or c <= 0 or c % d:
        return None
    start = c // d
    n = start
    visited = []
    for bit in data["word"]:
        if n % 2 != int(bit):
            raise ArithmeticError("integral fixed point failed physical replay")
        visited.append(n)
        n = (3 * n + 1) // 2 if n % 2 else n // 2
    if n != start:
        raise ArithmeticError("fixed block failed its closing edge")
    period = next((i for i in range(1, len(visited)) if visited[i] == start), len(visited))
    cycle = visited[:period]
    pivot = cycle.index(min(cycle))
    cycle = cycle[pivot:] + cycle[:pivot]
    return {"entry": start, "primitive_cycle": cycle}


def binary_ceiling(value: Fraction | int) -> int:
    value = Fraction(value)
    if value <= 0:
        raise ValueError("binary ceiling requires a positive value")
    b = 0
    while value.numerator > value.denominator << b:
        b += 1
    return b


def threshold(r: int, b: int, d: int) -> dict:
    a = (1 << r) - 1
    c = b + 3 * MATVEEV_K + 1 + d
    j = a * c
    q = 0
    while (1 << q) < j * (q + 2):
        q += 1
    return {
        "r": r,
        "b": b,
        "d": d,
        "A": a,
        "C_budget": c,
        "J": j,
        "q": q,
        "threshold_rhs": j * (q + 2),
        "strict_length_upper_bound": 1 << q,
    }


def schema_certificate(name: str, blocks: list[str]) -> dict:
    if not blocks:
        raise ValueError("the block list must be nonempty")
    data = [affine(word) for word in blocks]
    b_value = 2 * sum((abs(Fraction(row["C"], row["D"])) for row in data), Fraction())
    coeff = max(abs(row["D"]) + row["C"] for row in data)
    bound = threshold(len(data), binary_ceiling(b_value + 1), binary_ceiling(coeff))
    fixed = []
    for index, row in enumerate(data):
        cycle = positive_fixed_cycle(row)
        if cycle is not None:
            fixed.append({"block_index": index, **cycle})
    return {
        "name": name,
        "affine_blocks": data,
        "B": [b_value.numerator, b_value.denominator],
        "max_divisibility_coefficient": coeff,
        "fixed_block_cycles": fixed,
        **bound,
    }


def uniform_certificate(r: int, h: int) -> dict:
    if r < 1 or h < 1:
        raise ValueError("uniform block count and maximum length must be positive")
    b_value = 2 * r * 3**h
    return {
        "maximum_base_length": h,
        "B": b_value,
        **threshold(r, binary_ceiling(b_value + 1), 2 * h + 1),
    }


def gap_word(gaps: list[int]) -> str:
    if any(gap < 1 for gap in gaps):
        raise ValueError("odd gaps must be positive")
    return "".join("1" + "0" * (gap - 1) for gap in gaps)


def certificate() -> dict:
    return {
        "format": "collatz-bounded-power-bound-v1",
        "matveev_K": MATVEEV_K,
        "scope": {
            "independent_nonnegative_exponents": True,
            "positive_integer_cycles_only": True,
            "full_cycle_enumeration_executed": False,
            "external_logarithm_theorem": "Matveev 2000 II, Corollary 2.3",
        },
        "schemas": [
            schema_certificate("separate_odd_even_runs", ["1", "0"]),
            schema_certificate("mixed_pin_independent_exponents", [gap_word([1, 1, 4, 1, 1, 1, 2]), "10"]),
            schema_certificate("single_fixed_cycle_block", ["10"]),
            schema_certificate("rotated_and_repeated_fixed_blocks", ["01", "1010"]),
            schema_certificate("zero_odd_blocks", ["00", "0"]),
            schema_certificate("negative_fixed_points_only", ["1", "111"]),
        ],
        "uniform_bounds": [uniform_certificate(r, h) for r, h in [(1, 1), (2, 11), (4, 12), (8, 64)]],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("bounded_power_certificates.json"))
    args = parser.parse_args()
    result = certificate()
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "schemas": len(result["schemas"]), "uniform_bounds": len(result["uniform_bounds"])}))


if __name__ == "__main__":
    main()
