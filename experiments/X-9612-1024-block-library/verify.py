#!/usr/bin/env python3
"""Independent verifier for the frozen X-9612 payload."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

POSITIONS = (0, 2, 4, 7, 9, 12, 15, 18, 20, 23)


def direct_word() -> list[int]:
    p, q = 19, 30
    return [1 + ((j + 1) * p // q) - (j * p // q) for j in range(q)]


def direct_constant(word: list[int]) -> int:
    answer = 0
    prefix = 0
    for j in range(len(word)):
        answer += (3 ** (len(word) - 1 - j)) * (2 ** prefix)
        prefix += word[j]
    return answer


def apply_mask(word: list[int], mask: int) -> list[int]:
    result = list(word)
    for bit in range(10):
        if (mask >> bit) & 1:
            j = POSITIONS[bit]
            result[j : j + 2] = [result[j + 1], result[j]]
    return result


def verify(path: Path) -> None:
    supplied = json.loads(path.read_text(encoding="utf-8"))
    base = direct_word()
    if supplied["base_word"] != base:
        raise AssertionError("base mechanical word mismatch")

    total_valuation = sum(base)
    dyadic_multiplier = 2 ** total_valuation
    odd_multiplier = 3 ** len(base)
    denominator = dyadic_multiplier - odd_multiplier
    if supplied["summary"] != {
        "D": denominator,
        "P": odd_multiplier,
        "Q": dyadic_multiplier,
        "odd_state_length": 30,
        "total_valuation": 49,
    }:
        raise AssertionError("summary mismatch")

    constants: list[int] = []
    transcript: list[str] = []
    hits: list[dict[str, int]] = []
    for mask in range(1024):
        word = apply_mask(base, mask)
        if len(word) != 30 or sum(word) != 49:
            raise AssertionError("a replacement changed the block summary")
        constant = direct_constant(word)
        constants.append(constant)
        residue = constant % denominator
        transcript.append(f"{mask}:{constant}:{residue}")
        if residue == 0:
            hits.append({"mask": mask, "constant": constant})

    if len(set(constants)) != 1024:
        raise AssertionError("block constants are not pairwise distinct")
    if hits:
        raise AssertionError(f"unexpected single-block divisor hits: {hits}")

    prefix = [0]
    for value in base:
        prefix.append(prefix[-1] + value)
    deltas = [
        3 ** (30 - j - 2)
        * 2 ** prefix[j]
        * (2 ** base[j + 1] - 2 ** base[j])
        for j in POSITIONS
    ]

    expected_digest = hashlib.sha256(
        "\n".join(transcript).encode("utf-8")
    ).hexdigest()
    checks = {
        "swap_positions": list(POSITIONS),
        "signed_deltas": deltas,
        "sum_absolute_deltas": sum(abs(x) for x in deltas),
        "base_constant": direct_constant(base),
        "variant_count": 1024,
        "distinct_constant_count": 1024,
        "minimum_constant": min(constants),
        "maximum_constant": max(constants),
        "constant_span": max(constants) - min(constants),
        "minimum_residue": min(x % denominator for x in constants),
        "maximum_residue": max(x % denominator for x in constants),
        "single_block_divisor_hits": [],
        "variant_residue_transcript_sha256": expected_digest,
    }
    for key, expected in checks.items():
        if supplied[key] != expected:
            raise AssertionError(f"{key} mismatch: {supplied[key]!r} != {expected!r}")

    if supplied["constant_span"] >= dyadic_multiplier:
        raise AssertionError("the narrow-library hypothesis fails")

    print("all independent X-9612 checks passed")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} CANONICAL_JSON")
    verify(Path(sys.argv[1]))
