#!/usr/bin/env python3
"""Small exact audit for PRs #61, #62, and #63.

This is not a Collatz search. It exhaustively checks every nonempty binary
word through length 10 against the affine block formula, finite parity
cylinder, periodic 2-adic rational, and the canonical residue formula used
in PR #63/L-7501. Standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Any


def block_constant(word: tuple[int, ...]) -> int:
    total_ones = sum(word)
    running = 0
    constant = 0
    for j, bit in enumerate(word):
        running += bit
        if bit:
            constant += (1 << j) * 3 ** (total_ones - running)
    return constant


def integer_prefix(x: int, length: int) -> tuple[tuple[int, ...], int]:
    bits: list[int] = []
    y = x
    for _ in range(length):
        bit = y & 1
        bits.append(bit)
        y = y // 2 if bit == 0 else (3 * y + 1) // 2
    return tuple(bits), y


def parity_bit_2adic_rational(x: Fraction) -> int:
    if x.denominator % 2 == 0:
        raise AssertionError("denominator must be odd")
    return x.numerator & 1


def shortcut_2adic_rational(x: Fraction) -> Fraction:
    return x / 2 if parity_bit_2adic_rational(x) == 0 else (3 * x + 1) / 2


def residue_mod_power_two(x: Fraction, exponent: int) -> int:
    modulus = 1 << exponent
    return (
        (x.numerator % modulus)
        * pow(x.denominator % modulus, -1, modulus)
        % modulus
    )


def run(max_length: int = 10, repetitions: int = 5, residue_depth: int = 10) -> dict[str, Any]:
    counts = {
        "words": 0,
        "finite_cylinder_unique": 0,
        "affine_instances": 0,
        "periodic_rational_replays": 0,
        "canonical_residue_instances": 0,
    }

    all_zero_endpoint = {
        "word": "0",
        "divisibility_holds": True,
        "completion": "0",
        "positive_realization": False,
    }

    for length in range(1, max_length + 1):
        modulus = 1 << length
        for word in product((0, 1), repeat=length):
            counts["words"] += 1
            ones = sum(word)
            multiplier = 3**ones
            constant = block_constant(word)

            roots = [
                x
                for x in range(modulus)
                if integer_prefix(x, length)[0] == word
            ]
            if len(roots) != 1:
                raise AssertionError(("finite cylinder", length, word, roots))
            counts["finite_cylinder_unique"] += 1

            root = roots[0]
            for lift in (0, 1, 2):
                x = root + lift * modulus
                bits, y = integer_prefix(x, length)
                if bits != word:
                    raise AssertionError(("lift parity", length, word, x, bits))
                if modulus * y != multiplier * x + constant:
                    raise AssertionError(("affine formula", length, word, x))
                counts["affine_instances"] += 1

            completion = Fraction(constant, modulus - multiplier)
            y = completion
            observed: list[int] = []
            for _ in range(repetitions * length):
                observed.append(parity_bit_2adic_rational(y))
                y = shortcut_2adic_rational(y)
            if tuple(observed) != word * repetitions or y != completion:
                raise AssertionError(("periodic replay", length, word, completion))
            counts["periodic_rational_replays"] += 1

            for depth in range(1, residue_depth + 1):
                if modulus**depth <= constant:
                    continue
                residue = residue_mod_power_two(completion, depth * length)
                if multiplier < modulus:
                    denominator = modulus - multiplier
                    numerator = denominator * residue - constant
                    if numerator % (modulus**depth):
                        raise AssertionError(("subcritical congruence", length, word, depth))
                    coefficient = numerator // (modulus**depth)
                    if not 0 <= coefficient < denominator:
                        raise AssertionError(("subcritical coefficient", length, word, depth, coefficient))
                else:
                    denominator = multiplier - modulus
                    numerator = denominator * residue + constant
                    if numerator % (modulus**depth):
                        raise AssertionError(("supercritical congruence", length, word, depth))
                    coefficient = numerator // (modulus**depth)
                    if not 1 <= coefficient <= denominator:
                        raise AssertionError(("supercritical coefficient", length, word, depth, coefficient))
                counts["canonical_residue_instances"] += 1

    result: dict[str, Any] = {
        "experiment": "X-7710",
        "scope": {
            "maximum_word_length": max_length,
            "period_repetitions": repetitions,
            "maximum_residue_depth": residue_depth,
        },
        "counts": counts,
        "all_zero_endpoint": all_zero_endpoint,
        "verdict": "PASS",
    }
    semantic = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["semantic_digest"] = hashlib.sha256(semantic).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"

    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")

    if args.check_results:
        expected = json.loads(args.check_results.read_text(encoding="utf-8"))
        if result != expected:
            raise SystemExit("result mismatch")


if __name__ == "__main__":
    main()
