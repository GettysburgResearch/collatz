#!/usr/bin/env python3
"""X-9406: exact checks for T-9411 and L-9408."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path
from typing import Any


def v2(n: int) -> int:
    if n == 0:
        raise ValueError("v2(0) is undefined")
    n = abs(n)
    return (n & -n).bit_length() - 1


def fibonacci_bits(length: int) -> tuple[int, ...]:
    word = "0"
    while len(word) < length:
        word = "".join("01" if symbol == "0" else "0" for symbol in word)
    return tuple(int(symbol) for symbol in word[:length])


def balanced_increments(length: int) -> tuple[int, ...]:
    return tuple(17 if bit == 0 else 18 for bit in fibonacci_bits(length))


def heights_and_exponents(
    initial_height: int, increments: tuple[int, ...]
) -> tuple[list[int], list[int], list[int]]:
    heights = [initial_height]
    for increment in increments:
        heights.append(heights[-1] + increment)
    lengths = [9 * height + 1 for height in heights]
    exponents = [0]
    total = 0
    for length in lengths[1:]:
        total += length
        exponents.append(total)
    return heights, lengths, exponents


def truncation_checks() -> dict[str, Any]:
    _, _, exponents = heights_and_exponents(1, balanced_increments(32))
    rows: dict[str, Any] = {}

    for K in (1, 2, 3, 4, 6, 8, 12, 16, 24):
        denominator = 81 ** exponents[K]
        numerator = sum(
            64 ** exponents[j] * 81 ** (exponents[K] - exponents[j])
            for j in range(K + 1)
        )
        assert gcd(numerator, denominator) == 1
        truncation = Fraction(numerator, denominator)
        assert truncation.denominator == denominator

        finite_tail = sum(
            (
                Fraction(64, 81) ** exponents[j]
                for j in range(K + 1, min(len(exponents), K + 6))
            ),
            Fraction(0),
        )
        assert finite_tail.denominator % 2 == 1
        exact_error_v2 = 6 * exponents[K + 1]
        assert v2(finite_tail.numerator) == exact_error_v2

        height = max(abs(truncation.numerator), truncation.denominator)
        tau = exact_error_v2 / math.log2(height)
        rows[str(K)] = {
            "H_K": exponents[K],
            "H_next": exponents[K + 1],
            "denominator_bits": denominator.bit_length(),
            "height_bits": height.bit_length(),
            "exact_error_v2": exact_error_v2,
            "tau": f"{tau:.12f}",
        }

    return {
        "limit": f"{6 / math.log2(81):.15f}",
        "rows": rows,
    }


def word_data(word: tuple[int, ...]) -> dict[str, Any]:
    length = len(word)
    cumulative = 0
    cumulative_sum = 0
    polynomial: dict[tuple[int, int], int] = defaultdict(int)
    polynomial[(0, 0)] += 1

    for j, increment in enumerate(word, start=1):
        cumulative += increment
        cumulative_sum += cumulative
        if j < length:
            polynomial[(j, j + 9 * cumulative_sum)] += 1

    return {
        "r": length,
        "S": cumulative,
        "e": length + 9 * cumulative_sum,
        "P": dict(polynomial),
    }


def concatenate(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    polynomial: dict[tuple[int, int], int] = defaultdict(int)
    for key, coefficient in left["P"].items():
        polynomial[key] += coefficient

    for (degree, exponent), coefficient in right["P"].items():
        polynomial[
            (
                left["r"] + degree,
                left["e"] + exponent + 9 * left["S"] * degree,
            )
        ] += coefficient

    return {
        "r": left["r"] + right["r"],
        "S": left["S"] + right["S"],
        "e": left["e"] + right["e"] + 9 * right["r"] * left["S"],
        "P": dict(polynomial),
    }


def evaluate_polynomial(
    data: dict[str, Any], T: Fraction, X: Fraction
) -> Fraction:
    return sum(
        (
            Fraction(coefficient) * T**exponent * X**degree
            for (degree, exponent), coefficient in data["P"].items()
        ),
        Fraction(0),
    )


def finite_theta(
    initial_height: int, word: tuple[int, ...], T: Fraction
) -> Fraction:
    exponent = 0
    height = initial_height
    value = Fraction(1)
    for increment in word:
        height += increment
        exponent += 9 * height + 1
        value += T**exponent
    return value


def repeated_formula(word: tuple[int, ...], copies: int) -> dict[str, Any]:
    data = word_data(word)
    length = data["r"]
    height_sum = data["S"]
    exponent = data["e"]
    polynomial: dict[tuple[int, int], int] = defaultdict(int)

    for q in range(copies):
        preceding_exponent = (
            q * exponent + 9 * length * height_sum * q * (q - 1) // 2
        )
        for (degree, term_exponent), coefficient in data["P"].items():
            polynomial[
                (
                    q * length + degree,
                    preceding_exponent
                    + term_exponent
                    + 9 * q * height_sum * degree,
                )
            ] += coefficient

    return {
        "r": copies * length,
        "S": copies * height_sum,
        "e": copies * exponent
        + 9 * length * height_sum * copies * (copies - 1) // 2,
        "P": dict(polynomial),
    }


def transfer_checks() -> dict[str, Any]:
    concatenation_checks = 0
    transfer_value_checks = 0
    repeated_block_checks = 0
    maximum_polynomial_terms = 0
    T = Fraction(2, 3)

    for length in range(1, 7):
        for word in product((17, 18), repeat=length):
            data = word_data(word)
            maximum_polynomial_terms = max(
                maximum_polynomial_terms, len(data["P"])
            )
            for cut in range(1, length):
                left_word = word[:cut]
                right_word = word[cut:]
                left = word_data(left_word)
                right = word_data(right_word)
                assert concatenate(left, right) == data
                concatenation_checks += 1

                for initial_height in (0, 1, 7):
                    X = T ** (9 * initial_height)
                    direct = finite_theta(initial_height, word, T)
                    transferred = evaluate_polynomial(left, T, X) + (
                        T ** left["e"]
                        * X ** left["r"]
                        * finite_theta(
                            initial_height + left["S"], right_word, T
                        )
                    )
                    assert direct == transferred
                    transfer_value_checks += 1

    for length in range(1, 5):
        for word in product((17, 18), repeat=length):
            for copies in range(1, 6):
                assert repeated_formula(word, copies) == word_data(word * copies)
                repeated_block_checks += 1

    standard_words: list[tuple[int, ...]] = [(17,), (17, 18)]
    for _ in range(2, 10):
        standard_words.append(standard_words[-1] + standard_words[-2])

    standard_records: list[dict[str, int]] = []
    for index, word in enumerate(standard_words):
        data = word_data(word)
        if index >= 2:
            assert data == concatenate(
                word_data(standard_words[index - 1]),
                word_data(standard_words[index - 2]),
            )
        standard_records.append(
            {
                "index": index,
                "length": data["r"],
                "sum": data["S"],
                "e": data["e"],
                "polynomial_terms": len(data["P"]),
            }
        )

    return {
        "concatenation_checks": concatenation_checks,
        "transfer_value_checks": transfer_value_checks,
        "repeated_block_checks": repeated_block_checks,
        "maximum_polynomial_terms": maximum_polynomial_terms,
        "standard_words": standard_records,
    }


def generate() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "experiment_id": "X-9406",
        "research_question": (
            "Do direct sparse truncations stay below the p-adic approximation "
            "threshold, and do the exact S-adic transfer-polynomial identities hold?"
        ),
        "direct_truncation_barrier": truncation_checks(),
        "s_adic_transfer": transfer_checks(),
        "interpretation": {
            "proved_by_finite_computation": [
                "frozen reduced-denominator and exact first-omitted-valuation cases",
                "frozen finite approximation exponents",
                "frozen transfer, concatenation, repeated-block, and standard-word identities",
            ],
            "not_proved_by_finite_computation": [
                "the universal direct-truncation theorem",
                "the universal S-adic transfer lemma",
                "existence of a determinant or Pade approximant crossing the barrier",
                "p-adic irrationality or transcendence of the stack value",
                "nonexistence of an ordinary stack context or Collatz counterexample",
            ],
        },
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = generate()
    data = canonical_bytes(payload)
    digest = hashlib.sha256(data).hexdigest()

    if args.write_results:
        args.write_results.parent.mkdir(parents=True, exist_ok=True)
        args.write_results.write_bytes(data)
    if args.check_results and args.check_results.read_bytes() != data:
        raise SystemExit("canonical result mismatch")

    print(data.decode("utf-8"), end="")
    print(f"SHA256 {digest}")


if __name__ == "__main__":
    main()
