#!/usr/bin/env python3
"""Build the exact X-9612 1,024-block mechanical library certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


P_NUM = 19
Q_DEN = 30
SWAP_POSITIONS = (0, 2, 4, 7, 9, 12, 15, 18, 20, 23)


def mechanical_word(p: int, q: int) -> list[int]:
    return [
        1 + ((j + 1) * p // q) - (j * p // q)
        for j in range(q)
    ]


def affine_constant(word: list[int]) -> int:
    k = len(word)
    prefix = 0
    total = 0
    for j, valuation in enumerate(word):
        total += pow(3, k - 1 - j) * pow(2, prefix)
        prefix += valuation
    return total


def variant(base: list[int], mask: int) -> list[int]:
    out = base.copy()
    for bit, position in enumerate(SWAP_POSITIONS):
        if mask & (1 << bit):
            out[position], out[position + 1] = out[position + 1], out[position]
    return out


def build_payload() -> dict[str, Any]:
    base = mechanical_word(P_NUM, Q_DEN)
    if any(base[p] == base[p + 1] for p in SWAP_POSITIONS):
        raise AssertionError("a selected swap does not exchange unequal letters")
    if any(b <= a + 1 for a, b in zip(SWAP_POSITIONS, SWAP_POSITIONS[1:])):
        raise AssertionError("selected swaps overlap")

    length = len(base)
    total_valuation = sum(base)
    odd_multiplier = pow(3, length)
    dyadic_multiplier = pow(2, total_valuation)
    denominator = dyadic_multiplier - odd_multiplier
    if denominator <= 0:
        raise AssertionError("base block is not positive drift")

    prefix = [0]
    for valuation in base:
        prefix.append(prefix[-1] + valuation)

    signed_deltas: list[int] = []
    for position in SWAP_POSITIONS:
        delta = (
            pow(3, length - position - 2)
            * pow(2, prefix[position])
            * (pow(2, base[position + 1]) - pow(2, base[position]))
        )
        signed_deltas.append(delta)

    base_constant = affine_constant(base)
    constants: list[int] = []
    transcript: list[str] = []
    divisor_hits: list[dict[str, int]] = []

    for mask in range(1 << len(SWAP_POSITIONS)):
        word = variant(base, mask)
        constant = affine_constant(word)
        expected = base_constant + sum(
            signed_deltas[bit]
            for bit in range(len(SWAP_POSITIONS))
            if mask & (1 << bit)
        )
        if constant != expected:
            raise AssertionError(f"additive swap identity failed at mask {mask}")
        constants.append(constant)
        residue = constant % denominator
        transcript.append(f"{mask}:{constant}:{residue}")
        if residue == 0:
            divisor_hits.append({"mask": mask, "constant": constant})

    digest = hashlib.sha256("\n".join(transcript).encode("utf-8")).hexdigest()
    span = max(constants) - min(constants)
    sum_absolute_deltas = sum(abs(value) for value in signed_deltas)

    if span != sum_absolute_deltas:
        raise AssertionError("library span does not equal the independent correction width")
    if span >= dyadic_multiplier:
        raise AssertionError("library is not on the narrow side of L-9608")

    return {
        "experiment_id": "X-9612",
        "status": "EXACT FINITE BASE-LIBRARY AUDIT",
        "mechanical_slope": {"p": P_NUM, "q": Q_DEN},
        "base_word": base,
        "summary": {
            "odd_state_length": length,
            "total_valuation": total_valuation,
            "P": odd_multiplier,
            "Q": dyadic_multiplier,
            "D": denominator,
        },
        "swap_positions": list(SWAP_POSITIONS),
        "signed_deltas": signed_deltas,
        "sum_absolute_deltas": sum_absolute_deltas,
        "base_constant": base_constant,
        "variant_count": len(constants),
        "distinct_constant_count": len(set(constants)),
        "minimum_constant": min(constants),
        "maximum_constant": max(constants),
        "constant_span": span,
        "minimum_residue": min(value % denominator for value in constants),
        "maximum_residue": max(value % denominator for value in constants),
        "single_block_divisor_hits": divisor_hits,
        "variant_residue_transcript_sha256": digest,
        "theorem_interface": {
            "narrow_library_hypothesis": span < dyadic_multiplier,
            "all_repetition_conclusion": (
                "L-9608 reduces every full-denominator hit over this library "
                "to a pure power of one base variant"
            ),
            "not_proved": [
                "a positive cycle outside this library",
                "a divergent orbit",
                "the Collatz conjecture or its negation",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"

    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")

    if args.check_results:
        expected = args.check_results.read_text(encoding="utf-8")
        if text != expected:
            raise SystemExit("X-9612 payload differs from the frozen canonical JSON")


if __name__ == "__main__":
    main()
