#!/usr/bin/env python3
"""X-8301: exact decoder excluding positive accelerated cycles of length 185.

Standard library only.  The script reconstructs both maximal-local-minimum
skeletons, proves the ordered-jump representation by finite self-tests, scans
all candidate multipliers at the finitely many low excess heights, and checks
the reference-height data used by the stability theorem.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

K = 185
THREE_K = 3**K
REFERENCE_H = 31


@dataclass(frozen=True)
class Skeleton:
    name: str
    base_word: tuple[int, ...]
    variable_positions: tuple[int, ...]
    base_total: int
    base_constant: int
    suffix_weights: tuple[int, ...]
    suffix_valuations: tuple[int, ...]
    minimum_h: int
    direct_max_h: int
    uniform_multiplier_max: int


def affine_constant(word: Iterable[int]) -> int:
    word = tuple(word)
    total = 0
    prefix = 0
    for j, value in enumerate(word):
        total += 3 ** (len(word) - 1 - j) * 2**prefix
        prefix += value
    return total


def build_skeleton(name: str) -> Skeleton:
    if name == "AA":
        # Unique doubled ascent, after cyclic rotation:
        # 1,1,b_0,1,b_1,...,1,b_91.
        word: list[int] = [1]
        variable_positions: list[int] = []
        for _ in range(92):
            word.extend((1, 2))
            variable_positions.append(len(word) - 1)
        minimum_h = 17
        uniform_multiplier_max = 539_801
    elif name == "DD":
        # Unique doubled descent, after cyclic rotation:
        # 1,b_0,b_1,1,b_2,...,1,b_92.
        word = [1, 2, 2]
        variable_positions = [1, 2]
        for _ in range(2, 93):
            word.extend((1, 2))
            variable_positions.append(len(word) - 1)
        minimum_h = 16
        uniform_multiplier_max = 566_791
    else:
        raise ValueError(name)

    if len(word) != K:
        raise AssertionError("wrong skeleton length")

    prefix = 0
    terms: list[int] = []
    for j, value in enumerate(word):
        terms.append(3 ** (K - 1 - j) * 2**prefix)
        prefix += value

    suffix_after = [0] * (K + 1)
    for j in range(K - 1, -1, -1):
        suffix_after[j] = suffix_after[j + 1] + terms[j]

    suffix_weights = tuple(suffix_after[pos + 1] for pos in variable_positions)
    suffix_valuations = tuple(
        ((value & -value).bit_length() - 1) if value else -1
        for value in suffix_weights
    )

    result = Skeleton(
        name=name,
        base_word=tuple(word),
        variable_positions=tuple(variable_positions),
        base_total=sum(word),
        base_constant=sum(terms),
        suffix_weights=suffix_weights,
        suffix_valuations=suffix_valuations,
        minimum_h=minimum_h,
        direct_max_h=30,
        uniform_multiplier_max=uniform_multiplier_max,
    )
    validate_skeleton(result)
    return result


def validate_skeleton(skeleton: Skeleton) -> None:
    if affine_constant(skeleton.base_word) != skeleton.base_constant:
        raise AssertionError("base constant mismatch")
    if skeleton.suffix_weights[-1] != 0:
        raise AssertionError("the final valuation must have zero suffix weight")
    positive_vals = skeleton.suffix_valuations[:-1]
    if len(set(positive_vals)) != len(positive_vals):
        raise AssertionError("suffix valuations must be distinct")
    if tuple(sorted(positive_vals)) != positive_vals:
        raise AssertionError("suffix valuations must increase")

    # Deterministic finite controls for the ordered-jump identity.
    test_assignments = [
        [], [0], [len(skeleton.variable_positions)-1],
        [0, 0], [0, 1], [1, len(skeleton.variable_positions)-1],
        [0, 2, 5], [3, 3, len(skeleton.variable_positions)-1],
    ]
    for expanded in test_assignments:
        word_test = list(skeleton.base_word)
        for index in expanded:
            word_test[skeleton.variable_positions[index]] += 1
        predicted = skeleton.base_constant + sum(
            (1 << r) * skeleton.suffix_weights[index]
            for r, index in enumerate(sorted(expanded))
        )
        if affine_constant(word_test) != predicted:
            raise AssertionError("ordered-jump identity failed")


def denominator(skeleton: Skeleton, h: int) -> int:
    return 2 ** (skeleton.base_total + h) - THREE_K


def multiplier_bounds(skeleton: Skeleton, h: int) -> tuple[int, int]:
    d = denominator(skeleton, h)
    c_min = skeleton.base_constant
    c_max = c_min + ((1 << h) - 1) * skeleton.suffix_weights[0]
    return (c_min + d - 1) // d, c_max // d


def decode(
    skeleton: Skeleton,
    h: int,
    multiplier: int,
    d: int,
    value_to_index: dict[int, int],
) -> tuple[bool, int, int, str]:
    """Run the unique ordered-jump decoder.

    Returns (success, decoded_depth, maximum_valuation_seen, stop_reason).
    A zero remainder before depth h means that every remaining excess unit is
    placed on the final valuation, whose suffix weight is zero.
    """
    remainder = multiplier * d - skeleton.base_constant
    if remainder < 0:
        return False, 0, 0, "initial_negative"

    previous_index = 0
    maximum_valuation = 0

    for r in range(h):
        if remainder == 0:
            return True, r, maximum_valuation, "success_final_tail"
        valuation = (remainder & -remainder).bit_length() - 1
        maximum_valuation = max(maximum_valuation, valuation)
        index = value_to_index.get(valuation - r)
        if index is None:
            return False, r, maximum_valuation, "invalid_valuation"
        if index < previous_index:
            return False, r, maximum_valuation, "decreasing_position"
        term = (1 << r) * skeleton.suffix_weights[index]
        if term > remainder:
            return False, r + 1, maximum_valuation, "negative_remainder"
        remainder -= term
        previous_index = index

    if remainder == 0:
        return True, h, maximum_valuation, "success"
    return False, h, maximum_valuation, "nonzero_terminal_remainder"


def scan(
    skeleton: Skeleton,
    h: int,
    first_multiplier: int,
    last_multiplier: int,
) -> dict[str, object]:
    reasons: dict[str, int] = {}
    d = denominator(skeleton, h)
    value_to_index = {
        value: index
        for index, value in enumerate(skeleton.suffix_valuations[:-1])
    }
    max_depth = 0
    max_valuation = 0
    solutions: list[dict[str, int]] = []

    for multiplier in range(first_multiplier, last_multiplier + 1):
        success, depth, valuation, reason = decode(
            skeleton, h, multiplier, d, value_to_index
        )
        reasons[reason] = reasons.get(reason, 0) + 1
        max_depth = max(max_depth, depth)
        max_valuation = max(max_valuation, valuation)
        if success:
            solutions.append({"multiplier": multiplier, "decoded_depth": depth})

    return {
        "h": h,
        "first_multiplier": first_multiplier,
        "last_multiplier": last_multiplier,
        "multipliers_scanned": last_multiplier - first_multiplier + 1,
        "maximum_decoded_depth": max_depth,
        "maximum_remainder_valuation": max_valuation,
        "stop_reasons": dict(sorted(reasons.items())),
        "solutions": solutions,
    }


def build_results() -> dict[str, object]:
    output: dict[str, object] = {
        "experiment_id": "X-8301",
        "classification": "EXACT_FINITE_COMPUTATION",
        "accelerated_odd_length": K,
        "external_input": (
            "Hercher: every nontrivial positive cycle has at least 92 local minima"
        ),
        "claim_boundary": (
            "The finite scans plus the proved 2-adic stability argument exclude "
            "odd length 185 only; they do not prove the Collatz conjecture."
        ),
        "skeletons": {},
    }

    for name in ("AA", "DD"):
        skeleton = build_skeleton(name)
        direct: list[dict[str, object]] = []
        for h in range(skeleton.minimum_h, skeleton.direct_max_h + 1):
            lo, hi = multiplier_bounds(skeleton, h)
            direct.append(scan(skeleton, h, lo, hi))

        reference = scan(
            skeleton,
            REFERENCE_H,
            1,
            skeleton.uniform_multiplier_max,
        )
        if reference["solutions"]:
            raise AssertionError("unexpected reference solution")
        if set(reference["stop_reasons"]) != {"invalid_valuation"}:
            raise AssertionError("reference failures are not valuation-stable")

        stability_modulus_valuation = skeleton.base_total + REFERENCE_H
        if reference["maximum_remainder_valuation"] >= stability_modulus_valuation:
            raise AssertionError("insufficient stability margin")

        output["skeletons"][name] = {
            "description": (
                "unique doubled ascent" if name == "AA" else "unique doubled descent"
            ),
            "base_total_valuation": skeleton.base_total,
            "variable_count": len(skeleton.variable_positions),
            "minimum_excess_h": skeleton.minimum_h,
            "uniform_multiplier_max": skeleton.uniform_multiplier_max,
            "positive_suffix_valuation_min": skeleton.suffix_valuations[0],
            "positive_suffix_valuation_max": skeleton.suffix_valuations[-2],
            "direct_scans": direct,
            "reference_scan": reference,
            "stability": {
                "reference_h": REFERENCE_H,
                "difference_divisible_by_2_power": stability_modulus_valuation,
                "maximum_reference_valuation": reference[
                    "maximum_remainder_valuation"
                ],
                "conclusion": (
                    "the same valuation choices and the same invalid-valuation "
                    "failure occur for every larger h"
                ),
            },
        }

    return output


def canonical_bytes(data: dict[str, object]) -> bytes:
    return (json.dumps(data, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    data = canonical_bytes(build_results())
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
