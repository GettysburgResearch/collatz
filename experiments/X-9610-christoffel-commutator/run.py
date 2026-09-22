#!/usr/bin/env python3
"""X-9610: exact Christoffel/Farey commutator and gcd audit."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from math import gcd
from pathlib import Path

BOUND = 100


def lower_word(p: int, q: int) -> tuple[int, ...]:
    return tuple(
        1 + ((i + 1) * p // q - i * p // q)
        for i in range(q)
    )


def upper_word(p: int, q: int) -> tuple[int, ...]:
    return tuple(
        1
        + (((i + 1) * p + q - 1) // q)
        - ((i * p + q - 1) // q)
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


def is_rotation(left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    if len(left) != len(right):
        return False
    return any(left == right[shift:] + right[:shift] for shift in range(len(right)))


def farey_parents(p: int, q: int) -> tuple[int, int, int, int]:
    b = pow(p, -1, q)
    a = (p * b - 1) // q
    return a, b, p - a, q - b


def canonical_payload() -> dict[str, object]:
    neighbor_rows: list[list[object]] = []
    primitive_rows: list[list[int]] = []
    formula_checks = 0
    context_checks = 0

    contexts: list[tuple[int, ...]] = [()]
    for length in range(1, 3):
        contexts.extend(itertools.product((1, 2), repeat=length))

    for q in range(1, BOUND + 1):
        for p in range(q + 1):
            if gcd(p, q) != 1:
                continue
            for s in range(1, BOUND + 1):
                for r in range(s + 1):
                    if gcd(r, s) != 1:
                        continue
                    determinant = r * q - p * s
                    if abs(determinant) != 1:
                        continue

                    left = lower_word(p, q)
                    right = lower_word(r, s)
                    omega = summary(left + right)[2] - summary(right + left)[2]
                    if determinant == 1:
                        expected = -(2 ** (r + s - 1)) * 3 ** (q - 1)
                    else:
                        expected = 2 ** (p + q - 1) * 3 ** (s - 1)
                    assert omega == expected
                    formula_checks += 1

                    if q <= 15 and s <= 15:
                        for prefix in contexts:
                            prefix_total = summary(prefix)[1]
                            for suffix in contexts:
                                suffix_length = len(suffix)
                                contextual = (
                                    summary(prefix + left + right + suffix)[2]
                                    - summary(prefix + right + left + suffix)[2]
                                )
                                assert contextual == 3**suffix_length * 2**prefix_total * omega
                                context_checks += 1

                    neighbor_rows.append(
                        [p, q, r, s, determinant, str(omega)]
                    )

    factor_checks = 0
    gcd_checks = 0
    upper_rotation_checks = 0
    for q in range(2, BOUND + 1):
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            a, b, c, d = farey_parents(p, q)
            word = lower_word(p, q)
            assert word == lower_word(a, b) + lower_word(c, d)
            factor_checks += 1

            length, total, numerator = summary(word)
            denominator = 2**total - 3**length
            assert gcd(numerator, abs(denominator)) == 1
            gcd_checks += 1

            assert is_rotation(upper_word(p, q), word)
            upper_rotation_checks += 1
            primitive_rows.append(
                [p, q, a, b, c, d, abs(denominator).bit_length()]
            )

    rational_words = 0
    power_checks = 0
    nontrivial_hits: list[list[object]] = []
    for q in range(1, BOUND + 1):
        for p in range(q + 1):
            word = lower_word(p, q)
            length, total, numerator = summary(word)
            denominator = 2**total - 3**length
            rational_words += 1
            if denominator > 0 and numerator % denominator == 0:
                start = numerator // denominator
                if start != 1:
                    nontrivial_hits.append([p, q, str(start)])

            divisor = gcd(p, q)
            if 0 < p < q and divisor > 1:
                primitive = lower_word(p // divisor, q // divisor)
                assert word == primitive * divisor
                power_checks += 1

    semantic = {
        "neighbor_rows": neighbor_rows,
        "primitive_rows": primitive_rows,
    }
    semantic_digest = hashlib.sha256(
        json.dumps(semantic, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    payload: dict[str, object] = {
        "experiment_id": "X-9610",
        "arithmetic": "exact Python integers",
        "denominator_bound": BOUND,
        "neighbor_formula_checks": formula_checks,
        "contextual_commutator_checks": context_checks,
        "primitive_standard_factorizations": factor_checks,
        "primitive_full_denominator_gcd_checks": gcd_checks,
        "upper_rotation_checks": upper_rotation_checks,
        "rational_mechanical_words_checked": rational_words,
        "nonprimitive_power_checks": power_checks,
        "nontrivial_cycle_hits": nontrivial_hits,
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
