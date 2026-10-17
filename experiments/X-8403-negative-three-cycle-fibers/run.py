#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from itertools import combinations
from pathlib import Path


def chart_rows(length: int, pulses: int):
    exponent = 3 * length + pulses
    modulus = 1 << exponent
    multiplier = 9**length
    inverse = pow(multiplier, -1, modulus)
    rows = []

    for pulse_positions in combinations(range(length), pulses):
        pulse_set = set(pulse_positions)
        correction = 0
        used_exponent = 0
        letters = []

        for index in range(length):
            if index in pulse_set:
                letters.append("B")
                correction = 9 * correction + 21 * (1 << used_exponent)
                used_exponent += 4
            else:
                letters.append("A")
                correction *= 9
                used_exponent += 3

        assert used_exponent == exponent
        domain = (-correction * inverse) % modulus
        output = (multiplier * domain + correction) // modulus
        rows.append(("".join(letters), domain, output, correction))

    assert len({domain for _, domain, _, _ in rows}) == len(rows)
    return modulus, multiplier, rows


def replay_h(h: int, word: str) -> int:
    for letter in word:
        if letter == "A":
            assert h % 8 == 0
            h = 9 * (h // 8)
        else:
            assert h % 16 == 3
            h = 3 + 9 * ((h - 3) // 16)
    return h


def replay_physical(h: int, word: str) -> int:
    n = -5 + 2 * h
    for letter in word:
        advertised = (1, 2) if letter == "A" else (2, 2)
        for valuation in advertised:
            value = 3 * n + 1
            actual = (value & -value).bit_length() - 1
            assert actual == valuation
            n = value >> valuation
    assert n == -5 + 2 * replay_h(h, word)
    return n


def finite_minima(modulus: int, multiplier: int, rows, depth: int):
    residues = [0]
    current_modulus = 1
    records = []

    for level in range(1, depth + 1):
        inverse = (
            pow(multiplier, -1, current_modulus)
            if current_modulus > 1
            else 0
        )
        next_residues = []
        for tail in residues:
            for _word, domain, output, _correction in rows:
                quotient = (
                    0
                    if current_modulus == 1
                    else ((tail - output) * inverse) % current_modulus
                )
                next_residues.append(domain + modulus * quotient)

        current_modulus *= modulus
        residues = next_residues
        minimum = min(value for value in residues if value > 0)
        records.append(
            {
                "depth": level,
                "class_count": len(residues),
                "minimum_positive_h": minimum,
                "minimum_bits": minimum.bit_length(),
            }
        )

    return records


def canonical_payload():
    small = []
    rows_by_shape = {}

    for length, pulses in ((6, 1), (12, 2), (18, 3)):
        modulus, multiplier, rows = chart_rows(length, pulses)
        for word, domain, output, correction in rows:
            assert multiplier * domain + correction == modulus * output
            for quotient in (0, 1, 17):
                h = modulus * quotient + domain
                assert replay_h(h, word) == multiplier * quotient + output
                replay_physical(h, word)

        rows_by_shape[(length, pulses)] = (modulus, multiplier, rows)
        small.append(
            {
                "length": length,
                "pulses": pulses,
                "input_exponent": 3 * length + pulses,
                "branches": len(rows),
                "multiplier_minus_radix": multiplier - modulus,
                "supercritical": multiplier > modulus,
                "domain_digits_distinct": True,
                "minimum_domain_digit": min(row[1] for row in rows),
                "maximum_domain_digit": max(row[1] for row in rows),
            }
        )

    modulus, multiplier, rows = rows_by_shape[(6, 1)]
    row_table = [
        {
            "word": word,
            "domain_digit": domain,
            "output_digit": output,
            "digit_displacement": output - domain,
        }
        for word, domain, output, _ in rows
    ]
    minima = finite_minima(modulus, multiplier, rows, 8)

    near_critical = []
    for length, pulses in ((6, 1), (53, 9), (665, 113)):
        modulus = 1 << (3 * length + pulses)
        multiplier = 9**length
        assert modulus < multiplier < 2 * modulus
        near_critical.append(
            {
                "length": length,
                "pulses": pulses,
                "input_exponent": 3 * length + pulses,
                "branch_count": math.comb(length, pulses),
                "multiplier_bits": multiplier.bit_length(),
                "radix_bits": modulus.bit_length(),
                "difference_bits": (multiplier - modulus).bit_length(),
            }
        )

    return {
        "schema_version": 1,
        "experiment_id": "X-8403",
        "status": "EMPIRICAL / EXACT FINITE INTERFACE AUDIT",
        "letter_maps": {
            "A": "h=8q -> 9q; physical valuations (1,2)",
            "B": "h=3+16q -> 3+9q; physical valuations (2,2)",
        },
        "small_shape_audits": small,
        "six_one_chart_rows": row_table,
        "six_one_finite_minima": minima,
        "near_critical_examples": near_critical,
        "interpretation": {
            "proved_by_finite_replay": [
                "all branch digits and exact physical replays for (6,1), (12,2), and (18,3)",
                "the complete six-branch (6,1) digit table",
                "the exact depth-1-through-8 least positive cylinders for the six-branch chart",
                "the displayed exact integer comparisons and branch counts for three near-critical shapes",
            ],
            "not_proved": [
                "an ordinary infinite path in any chart",
                "a divergent Collatz seed",
                "a nontrivial positive cycle",
                "the Collatz conjecture or its negation",
            ],
        },
    }


def digest(payload):
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = canonical_payload()
    payload["payload_sha256"] = digest(payload)
    text = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    print(text, end="")

    if args.check_results:
        frozen = json.loads(args.check_results.read_text(encoding="utf-8"))
        assert frozen == payload
        print("frozen result check passed")


if __name__ == "__main__":
    main()
