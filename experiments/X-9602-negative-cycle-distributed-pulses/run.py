#!/usr/bin/env python3
"""X-9602: exact distributed unit-pulse scan on the negative 3-cycle."""
from __future__ import annotations

import argparse
import hashlib
import json
from itertools import combinations
from math import comb
from pathlib import Path

R_MAX = 45


def setup(repeats: int, rotation: int) -> tuple[int, list[int], int, int]:
    word = ([1, 2] if rotation == 0 else [2, 1]) * repeats
    state = -5 if rotation == 0 else -7
    odd_steps = 2 * repeats
    states = [state]
    prefix = 0
    weights: list[int] = []
    for position, valuation in enumerate(word):
        numerator = 3 * states[-1] + 1
        assert numerator % (1 << valuation) == 0
        states.append(numerator >> valuation)
        prefix += valuation
        weights.append(
            (-states[-1])
            * 3 ** (odd_steps - 1 - position)
            * (1 << prefix)
        )
    assert states[-1] == state

    pulse_count = 0
    while (1 << (prefix + pulse_count)) <= 3**odd_steps:
        pulse_count += 1
    denominator = (1 << (prefix + pulse_count)) - 3**odd_steps
    return state, weights, pulse_count, denominator


def local_sum(
    combo: tuple[int, ...], weights: list[int], modulus: int
) -> int:
    total = 0
    for rank, position in enumerate(combo):
        total = (
            total + (1 << rank) * (weights[position] % modulus)
        ) % modulus
    return total


def search_rotation(repeats: int, rotation: int) -> dict[str, object]:
    state, weights, pulse_count, denominator = setup(repeats, rotation)
    left_positions = range(repeats)
    right_positions = range(repeats, 2 * repeats)
    left_counts = sorted({pulse_count // 2, (pulse_count + 1) // 2})
    representatives = 0
    outer_lookups = 0
    hit: dict[str, object] | None = None

    for left_count in left_counts:
        right_count = pulse_count - left_count
        left_size = comb(repeats, left_count)
        right_size = comb(repeats, right_count)
        representatives += left_size * right_size
        right_factor = pow(2, left_count, denominator)

        if left_size <= right_size:
            table: dict[int, tuple[int, ...]] = {}
            for combo in combinations(left_positions, left_count):
                table.setdefault(local_sum(combo, weights, denominator), combo)
            for right_combo in combinations(right_positions, right_count):
                outer_lookups += 1
                needed = (
                    -right_factor
                    * local_sum(right_combo, weights, denominator)
                ) % denominator
                left_combo = table.get(needed)
                if left_combo is None:
                    continue
                pulse_positions = left_combo + right_combo
                correction = sum(
                    (1 << rank) * weights[position]
                    for rank, position in enumerate(pulse_positions)
                )
                assert correction % denominator == 0
                start = state + correction // denominator
                hit = {
                    "pulse_positions": list(pulse_positions),
                    "start": str(start),
                    "trivial": start == 1,
                }
                break
        else:
            table = {}
            for right_combo in combinations(right_positions, right_count):
                table.setdefault(
                    (
                        right_factor
                        * local_sum(right_combo, weights, denominator)
                    )
                    % denominator,
                    right_combo,
                )
            for left_combo in combinations(left_positions, left_count):
                outer_lookups += 1
                needed = (-local_sum(left_combo, weights, denominator)) % denominator
                right_combo = table.get(needed)
                if right_combo is None:
                    continue
                pulse_positions = left_combo + right_combo
                correction = sum(
                    (1 << rank) * weights[position]
                    for rank, position in enumerate(pulse_positions)
                )
                assert correction % denominator == 0
                start = state + correction // denominator
                hit = {
                    "pulse_positions": list(pulse_positions),
                    "start": str(start),
                    "trivial": start == 1,
                }
                break
        if hit is not None:
            break

    return {
        "repeats": repeats,
        "rotation": rotation,
        "pulse_count": pulse_count,
        "denominator_bits": denominator.bit_length(),
        "balanced_representatives": representatives,
        "outer_lookups": outer_lookups,
        "hit": hit,
    }


def canonical_payload() -> dict[str, object]:
    records: list[dict[str, object]] = []
    raw_labeled_words = 0
    for repeats in range(1, R_MAX + 1):
        _, _, pulse_count, _ = setup(repeats, 0)
        raw_labeled_words += 2 * comb(2 * repeats, pulse_count)
        records.extend(
            (search_rotation(repeats, 0), search_rotation(repeats, 1))
        )

    semantic_rows = [
        {
            key: record[key]
            for key in (
                "repeats",
                "rotation",
                "pulse_count",
                "denominator_bits",
                "hit",
            )
        }
        for record in records
    ]
    audit = hashlib.sha256(
        json.dumps(
            semantic_rows, sort_keys=True, separators=(",", ":")
        ).encode()
    ).hexdigest()
    hits = [
        record["hit"]
        | {
            "repeats": record["repeats"],
            "rotation": record["rotation"],
        }
        for record in records
        if isinstance(record["hit"], dict)
    ]
    return {
        "experiment_id": "X-9602",
        "arithmetic": "exact Python integers",
        "r_max": R_MAX,
        "family": (
            "negative 3-cycle repeated word with distinct minimum unit pulses"
        ),
        "coverage": (
            "all pulse sets via cyclic half-balance and both primitive rotations"
        ),
        "raw_labeled_words": raw_labeled_words,
        "semantic_audit_sha256": audit,
        "hits": hits,
        "totals": {
            "nontrivial_hit_count": sum(
                isinstance(record["hit"], dict)
                and not bool(record["hit"]["trivial"])
                for record in records
            ),
            "trivial_hit_count": sum(
                isinstance(record["hit"], dict)
                and bool(record["hit"]["trivial"])
                for record in records
            ),
            "balanced_representatives": sum(
                int(record["balanced_representatives"])
                for record in records
            ),
            "outer_lookups": sum(
                int(record["outer_lookups"]) for record in records
            ),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = canonical_payload()
    payload["results_sha256"] = hashlib.sha256(
        json.dumps(
            payload, sort_keys=True, separators=(",", ":")
        ).encode()
    ).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))

    if args.check_results:
        frozen = json.loads(args.check_results.read_text(encoding="utf-8"))
        if frozen != payload:
            raise SystemExit("frozen result mismatch")
        print("frozen result check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
