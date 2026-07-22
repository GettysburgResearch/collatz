#!/usr/bin/env python3
"""X-9304: exact finite-prefix audit of the centered-power equivalence."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path
from typing import Sequence

M = 64
N = 81
ROOT_M = 8
ROOT_N = 9
BETA = Fraction(N, M)
ROOT_BETA = Fraction(ROOT_N, ROOT_M)
REAL_TAIL = Fraction(1, 3)
DEFAULT_DEPTHS = tuple(range(1, 9))


def parse_depths(text: str) -> tuple[int, ...]:
    try:
        depths = tuple(int(part.strip()) for part in text.split(",") if part.strip())
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc
    if not depths or any(depth < 1 for depth in depths):
        raise argparse.ArgumentTypeError(
            "depths must be comma-separated positive integers"
        )
    return depths


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def nearest_integer(value: Fraction) -> int:
    """Return floor(value+1/2); audited values are never half-integral."""
    return (2 * value.numerator + value.denominator) // (
        2 * value.denominator
    )


def standard_survivor_residue(word: Sequence[int]) -> int:
    depth = len(word)
    modulus = M**depth
    return sum(
        (N - M)
        * digit
        * M**position
        * pow(N, -(position + 1), modulus)
        for position, digit in enumerate(word)
    ) % modulus


def replay_survivor(start: int, word: Sequence[int]) -> list[int]:
    states = [start]
    for digit in word:
        current = states[-1]
        if current % M != digit:
            raise AssertionError("survivor digit does not match the current residue")
        numerator = N * current - (N - M) * digit
        if numerator % M:
            raise AssertionError("survivor update is not integral")
        states.append(numerator // M)
    return states


def real_companion(word: Sequence[int]) -> list[Fraction]:
    states: list[Fraction] = [Fraction(0)] * (len(word) + 1)
    states[-1] = REAL_TAIL
    for position in range(len(word) - 1, -1, -1):
        states[position] = (
            Fraction(N - M, N) * word[position]
            + Fraction(M, N) * states[position + 1]
        )
    return states


def audit_word(word: Sequence[int]) -> int | None:
    start = standard_survivor_residue(word)
    ordinary = replay_survivor(start, word)
    real = real_companion(word)

    # The two trivial finite residues are not part of the nontrivial theorem.
    if start <= 1:
        return None

    xi = (Fraction(start) - real[0]) / M
    if xi <= 0:
        raise AssertionError("centered parameter is not positive")

    # Correct square-root parameter: 81/64=(9/8)^2 and zeta=8*xi.
    zeta = ROOT_M * xi
    errors: list[Fraction] = []
    nearest: list[int] = []

    for position, digit in enumerate(word):
        power = xi * BETA**position
        quotient = (ordinary[position] - digit) // M
        error = power - quotient

        if not abs(error) < Fraction(1, N):
            raise AssertionError("centered error left the critical interval")
        if (error > 0) != bool(digit):
            raise AssertionError("centered error sign does not recover the digit")
        if real[position] != digit - M * error:
            raise AssertionError("real companion reconstruction failed")
        if ordinary[position] != ceil_fraction(M * power):
            raise AssertionError("ceiling reconstruction failed")
        if nearest_integer(power) != quotient:
            raise AssertionError("nearest-integer reconstruction failed")

        # Exact centered square-root phases.
        even_power = zeta * ROOT_BETA ** (2 * position)
        odd_power = zeta * ROOT_BETA ** (2 * position + 1)
        if even_power != ROOT_M * power:
            raise AssertionError("even square-root phase identity failed")
        if odd_power != ROOT_N * power:
            raise AssertionError("odd square-root phase identity failed")
        if nearest_integer(even_power) != ROOT_M * quotient:
            raise AssertionError("even square-root nearest integer failed")
        if nearest_integer(odd_power) != ROOT_N * quotient:
            raise AssertionError("odd square-root nearest integer failed")
        if not abs(even_power - ROOT_M * quotient) < Fraction(8, 81):
            raise AssertionError("even square-root error bound failed")
        if not abs(odd_power - ROOT_N * quotient) < Fraction(1, 9):
            raise AssertionError("odd square-root error bound failed")

        # Exact two-step 8 -> 9 factorization with the digit repeated twice.
        current = ordinary[position]
        first_numerator = ROOT_N * current - digit
        if first_numerator % ROOT_M:
            raise AssertionError("first 8 -> 9 half-step is not integral")
        middle = first_numerator // ROOT_M
        if middle % ROOT_M != digit:
            raise AssertionError("duplicated digit fails at the middle state")
        second_numerator = ROOT_N * middle - digit
        if second_numerator % ROOT_M:
            raise AssertionError("second 8 -> 9 half-step is not integral")
        if second_numerator // ROOT_M != ordinary[position + 1]:
            raise AssertionError("two 8 -> 9 steps do not recover 64 -> 81")

        errors.append(error)
        nearest.append(quotient)

    for position in range(len(word) - 1):
        carry = N * errors[position] - M * errors[position + 1]
        if carry.denominator != 1:
            raise AssertionError("centered carry is not integral")
        if int(carry) != word[position] - word[position + 1]:
            raise AssertionError("centered carry does not equal the digit difference")
        if nearest[position] % M not in {0, 15, 49}:
            raise AssertionError(
                "nearest integer has an impossible residue modulo 64"
            )

    return start


def record_for_depth(depth: int) -> dict[str, int | None]:
    starts: list[int] = []
    for mask in range(1 << depth):
        word = tuple((mask >> position) & 1 for position in range(depth))
        start = audit_word(word)
        if start is not None:
            starts.append(start)

    return {
        "depth": depth,
        "nontrivial_words_checked": len(starts),
        "minimum_start": min(starts) if starts else None,
        "maximum_start": max(starts) if starts else None,
    }


def canonical_payload(depths: Sequence[int]) -> dict[str, object]:
    records = [record_for_depth(depth) for depth in depths]
    total_words = sum(int(record["nontrivial_words_checked"]) for record in records)
    centered_checks = sum(
        int(record["nontrivial_words_checked"]) * int(record["depth"])
        for record in records
    )
    transition_checks = sum(
        int(record["nontrivial_words_checked"])
        * max(0, int(record["depth"]) - 1)
        for record in records
    )
    return {
        "experiment_id": "X-9304",
        "schema_version": 2,
        "arithmetic": "exact fractions and integers",
        "tail_real_coordinate": "1/3",
        "depths": list(depths),
        "records": records,
        "totals": {
            "nontrivial_words_checked": total_words,
            "centered_trace_checks": centered_checks,
            "paired_8_to_9_steps_checked": 2 * centered_checks,
            "centered_carry_checks": transition_checks,
        },
        "checks": [
            "finite survivor replay",
            "forward centered-power formula",
            "nearest-integer reconstruction",
            "sign-to-digit reconstruction",
            "integer carry sign table",
            "exact 64-to-81 factorization through two 8-to-9 steps",
            "duplicated-digit 8-to-9 chart replay",
            "centered 9/8 square-root lift",
        ],
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
        "--depths",
        type=parse_depths,
        default=DEFAULT_DEPTHS,
        help="comma-separated positive depths",
    )
    parser.add_argument(
        "--check-results",
        type=Path,
        help="compare with a frozen canonical JSON payload",
    )
    args = parser.parse_args()

    payload = canonical_payload(args.depths)
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
