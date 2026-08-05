#!/usr/bin/env python3
"""X-9604: two compressed block families around the negative 3-cycle."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from itertools import product
from pathlib import Path

M_MAX = 1000
V_LENGTH_MAX = 5
V_LETTER_MAX = 6


def summary(word: tuple[int, ...]) -> tuple[int, int, int]:
    length = len(word)
    exponent = sum(word)
    constant = 0
    prefix = 0
    for position, valuation in enumerate(word):
        constant += 3 ** (length - 1 - position) * 2**prefix
        prefix += valuation
    return length, exponent, constant


def primitive(word: tuple[int, ...]) -> bool:
    length = len(word)
    return all(
        not (
            length % divisor == 0
            and word == word[:divisor] * (length // divisor)
        )
        for divisor in range(1, length)
    )


def contracting_blocks() -> list[tuple[tuple[int, ...], int, int, int, int, float]]:
    blocks = []
    for length in range(1, V_LENGTH_MAX + 1):
        for word in product(range(1, V_LETTER_MAX + 1), repeat=length):
            if not primitive(word):
                continue
            odd_steps, exponent, constant = summary(word)
            odd_multiplier = 3**odd_steps
            dyadic_radix = 2**exponent
            if dyadic_radix <= odd_multiplier or word == (2,):
                continue
            commutator = -(constant + 5 * (dyadic_radix - odd_multiplier))
            assert commutator != 0
            blocks.append(
                (
                    word,
                    odd_multiplier,
                    dyadic_radix,
                    constant,
                    abs(commutator),
                    math.log(dyadic_radix / odd_multiplier),
                )
            )
    return blocks


def canonical_payload() -> dict[str, object]:
    library = contracting_blocks()
    odd_power = 1
    dyadic_power = 1
    hits: list[dict[str, object]] = []
    reduced_rows = 0
    terminal_size_eliminations = 0
    audit = hashlib.sha256()

    for negative_repeats in range(1, M_MAX + 1):
        odd_power *= 9
        dyadic_power *= 8
        negative_geometric = odd_power - dyadic_power

        for (
            word,
            block_odd,
            block_dyadic,
            block_constant,
            commutator,
            log_ratio,
        ) in library:
            block_repeats = max(
                1,
                int(
                    negative_repeats * math.log(9 / 8) / log_ratio
                ),
            )
            repeated_odd = block_odd**block_repeats
            repeated_dyadic = block_dyadic**block_repeats
            while (
                dyadic_power * repeated_dyadic
                <= odd_power * repeated_odd
            ):
                repeated_odd *= block_odd
                repeated_dyadic *= block_dyadic
                block_repeats += 1

            reduced_bound = negative_geometric * commutator
            while True:
                denominator = (
                    dyadic_power * repeated_dyadic
                    - odd_power * repeated_odd
                )
                if denominator > reduced_bound:
                    terminal_size_eliminations += 1
                    break

                reduced_rows += 1
                if reduced_bound % denominator == 0:
                    block_geometric = (
                        repeated_dyadic - repeated_odd
                    ) // (block_dyadic - block_odd)
                    repeated_constant = block_constant * block_geometric
                    negative_constant = 5 * negative_geometric
                    total_constant = (
                        repeated_odd * negative_constant
                        + dyadic_power * repeated_constant
                    )
                    if total_constant % denominator == 0:
                        start = total_constant // denominator
                        hits.append(
                            {
                                "negative_block_repeats": negative_repeats,
                                "contracting_word": list(word),
                                "contracting_repeats": block_repeats,
                                "start": str(start),
                                "trivial": start == 1,
                            }
                        )

                repeated_odd *= block_odd
                repeated_dyadic *= block_dyadic
                block_repeats += 1

            audit.update(negative_repeats.to_bytes(4, "big"))
            audit.update(len(word).to_bytes(2, "big"))
            audit.update(bytes(word))
            audit.update(block_repeats.to_bytes(4, "big"))

    return {
        "experiment_id": "X-9604",
        "arithmetic": "exact Python integers",
        "negative_block": "(1,2)^m",
        "m_max": M_MAX,
        "contracting_word_length_max": V_LENGTH_MAX,
        "contracting_letter_max": V_LETTER_MAX,
        "primitive_contracting_block_count": len(library),
        "reduced_divisibility_rows": reduced_rows,
        "terminal_size_eliminations": terminal_size_eliminations,
        "hits": hits,
        "nontrivial_hit_count": sum(not bool(hit["trivial"]) for hit in hits),
        "semantic_audit_sha256": audit.hexdigest(),
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
