#!/usr/bin/env python3
"""X-9305: exact appended-cylinder replay for the Thue--Morse itinerary."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path
from typing import Sequence

M = 64
N = 81
DEFAULT_MAX_TRANSITION = 1024
DIRECT_CHECKPOINTS = frozenset({64, 128, 256, 512, 1024})


def thue_morse(index: int) -> int:
    return index.bit_count() & 1


def direct_residue(digits: Sequence[int], depth: int) -> int:
    modulus = M**depth
    return (
        -sum(
            (digits[i] - digits[i + 1])
            * M**i
            * pow(N, -(i + 1), modulus)
            for i in range(depth)
        )
    ) % modulus


def longest_zero_run(values: Sequence[int]) -> int:
    longest = 0
    current = 0
    for value in values:
        if value == 0:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest


def square_witnesses(digits: Sequence[int]) -> list[dict[str, int]]:
    witnesses: list[dict[str, int]] = []
    exponent = 0
    while 7 * 2**exponent <= len(digits):
        length = 2**exponent
        first = 5 * length
        second = 6 * length
        if digits[first : first + length] != digits[second : second + length]:
            raise AssertionError("Thue--Morse square witness failed")
        witnesses.append(
            {
                "m": exponent,
                "length": length,
                "first_start": first,
                "second_start": second,
            }
        )
        exponent += 1
    return witnesses


def canonical_payload(max_transition: int) -> dict[str, object]:
    if max_transition < 1:
        raise ValueError("max_transition must be positive")

    digits = [thue_morse(i) for i in range(max_transition + 2)]

    # The length-one cylinder uses d_0=e_0-e_1.
    first_difference = digits[0] - digits[1]
    representative = (-first_difference * pow(N, -1, M)) % M
    terminal = (N * representative + first_difference) // M

    blocks: list[int] = []

    for depth in range(1, max_transition + 1):
        difference = digits[depth] - digits[depth + 1]
        block = (
            -pow(N, -(depth + 1), M) * (N * terminal + difference)
        ) % M

        if (N * (terminal + block * N**depth) + difference) % M:
            raise AssertionError("appended block does not make the next step integral")

        next_terminal = (
            N * (terminal + block * N**depth) + difference
        ) // M
        next_representative = representative + block * M**depth

        if depth <= 32 or depth in DIRECT_CHECKPOINTS:
            if next_representative != direct_residue(digits, depth + 1):
                raise AssertionError("recursive and direct cylinder residues disagree")

        blocks.append(block)
        representative = next_representative
        terminal = next_terminal

    zero_positions = [
        depth for depth, block in enumerate(blocks, start=1) if block == 0
    ]

    return {
        "experiment_id": "X-9305",
        "schema_version": 1,
        "arithmetic": "exact integers",
        "itinerary": "Thue-Morse t(n)=popcount(n) mod 2",
        "max_transition": max_transition,
        "checks": [
            "exact nearest-integer cylinder recurrence at every transition",
            "exact appended block formula at every transition",
            "direct residue reconstruction through depth 32 and at powers of two",
            "Thue-Morse square witnesses at starts 5*2^m and 6*2^m",
        ],
        "summary": {
            "blocks_checked": len(blocks),
            "nonzero_blocks": sum(block != 0 for block in blocks),
            "zero_blocks": len(zero_positions),
            "longest_zero_run": longest_zero_run(blocks),
            "first_32_blocks": blocks[:32],
            "zero_positions": zero_positions,
            "final_representative_bit_length": representative.bit_length(),
            "final_terminal_bit_length": terminal.bit_length(),
        },
        "square_witnesses": square_witnesses(digits),
    }


def payload_digest(payload: dict[str, object]) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def check_frozen(path: Path, payload: dict[str, object], digest: str) -> None:
    frozen = json.loads(path.read_text(encoding="utf-8"))
    expected_digest = frozen.pop("results_sha256", None)
    if expected_digest != digest:
        raise SystemExit(
            f"digest mismatch: computed {digest}, frozen {expected_digest}"
        )
    if frozen != payload:
        raise SystemExit("computed payload differs from frozen canonical JSON")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--max-transition",
        type=int,
        default=DEFAULT_MAX_TRANSITION,
        help="largest appended block index to audit",
    )
    parser.add_argument(
        "--check-results",
        type=Path,
        help="compare with a frozen canonical JSON payload",
    )
    args = parser.parse_args()

    payload = canonical_payload(args.max_transition)
    digest = payload_digest(payload)
    output = dict(payload)
    output["results_sha256"] = digest

    print(f"python={platform.python_version()}")
    print(json.dumps(output, sort_keys=True, indent=2))

    if args.check_results is not None:
        check_frozen(args.check_results, payload, digest)
        print("frozen result check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
