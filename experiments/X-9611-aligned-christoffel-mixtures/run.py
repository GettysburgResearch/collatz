#!/usr/bin/env python3
"""X-9611: exact audit of aligned Christoffel conjugate mixtures."""
from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd
from pathlib import Path

BOUND = 30
REPETITION_MAX = 12


def lower_word(p: int, q: int) -> tuple[int, ...]:
    return tuple(
        1 + ((i + 1) * p // q - i * p // q)
        for i in range(q)
    )


def summary(word: tuple[int, ...]) -> tuple[int, int, int]:
    length = len(word)
    total = 0
    numerator = 0
    for index, valuation in enumerate(word):
        numerator += 3 ** (length - 1 - index) * 2**total
        total += valuation
    return length, total, numerator


def farey_parents(p: int, q: int) -> tuple[int, int, int, int]:
    b = pow(p, -1, q)
    a = (p * b - 1) // q
    return a, b, p - a, q - b


def canonical_payload() -> dict[str, object]:
    rows: list[list[object]] = []
    patterns_checked = 0
    mixed_patterns = 0
    formal_hits: list[list[object]] = []

    for q in range(2, BOUND + 1):
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            a, b, c, d = farey_parents(p, q)
            left = lower_word(a, b)
            right = lower_word(c, d)
            word = left + right
            conjugate = right + left

            length, total, numerator = summary(word)
            assert length == q and total == p + q
            conjugate_numerator = summary(conjugate)[2]
            delta = numerator - conjugate_numerator

            odd_multiplier = 3**length
            dyadic_multiplier = 2**total
            primitive_denominator = dyadic_multiplier - odd_multiplier

            for repetitions in range(1, REPETITION_MAX + 1):
                geometric = (
                    dyadic_multiplier**repetitions
                    - odd_multiplier**repetitions
                ) // primitive_denominator
                assert gcd(delta, geometric) == 1

                for mask in range(1 << repetitions):
                    selected = 0
                    for position in range(repetitions):
                        if (mask >> (repetitions - 1 - position)) & 1:
                            selected += (
                                odd_multiplier
                                ** (repetitions - 1 - position)
                                * dyadic_multiplier**position
                            )

                    full_numerator = numerator * geometric - delta * selected
                    full_denominator = primitive_denominator * geometric

                    if 0 < mask < (1 << repetitions) - 1:
                        mixed_patterns += 1
                        assert full_numerator % geometric != 0

                    if (
                        full_denominator > 0
                        and full_numerator % full_denominator == 0
                    ):
                        formal_hits.append(
                            [
                                p,
                                q,
                                repetitions,
                                mask,
                                str(full_numerator // full_denominator),
                            ]
                        )
                    patterns_checked += 1

                rows.append(
                    [
                        p,
                        q,
                        repetitions,
                        str(delta),
                        str(geometric),
                        gcd(delta, geometric),
                    ]
                )

    semantic_digest = hashlib.sha256(
        json.dumps(rows, separators=(",", ":")).encode()
    ).hexdigest()

    payload: dict[str, object] = {
        "experiment_id": "X-9611",
        "arithmetic": "exact Python integers",
        "denominator_bound": BOUND,
        "repetition_max": REPETITION_MAX,
        "primitive_slope_repetition_rows": len(rows),
        "aligned_patterns_checked": patterns_checked,
        "genuinely_mixed_patterns": mixed_patterns,
        "geometric_coprimality_checks": len(rows),
        "formal_divisor_hits": len(formal_hits),
        "nontrivial_cycle_hits": formal_hits,
        "semantic_sha256": semantic_digest,
    }
    payload["results_sha256"] = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = canonical_payload()
    print(json.dumps(payload, indent=2, sort_keys=True))
    if args.check_results is not None:
        frozen = json.loads(args.check_results.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("frozen result mismatch")
        print("frozen result check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
