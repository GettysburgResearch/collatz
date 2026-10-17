#!/usr/bin/env python3
"""X-9405: exact checks for the sparse stack partial-theta packet."""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path
from typing import Any


def stage_length(m: int) -> int:
    return 9 * m + 1


def params(m: int) -> tuple[int, int, int, int]:
    ell = stage_length(m)
    modulus = 64**ell
    multiplier = 81**ell
    constant = (modulus + 17) // 81
    return ell, modulus, multiplier, constant


def edge(m: int, n: int) -> tuple[int, int, int, int]:
    _, _, multiplier, _ = params(m)
    _, modulus, _, constant = params(n)
    base = 81 ** (9 * m)
    residue = pow(multiplier, -1, modulus) * (constant - base) % modulus
    carry = (multiplier * residue + base - constant) // modulus
    return residue, carry, modulus, multiplier


def cylinder(schedule: tuple[int, ...]) -> tuple[int, int]:
    residue, modulus = 0, 1
    for i in range(len(schedule) - 2, -1, -1):
        m, n = schedule[i], schedule[i + 1]
        edge_residue, carry, edge_modulus, multiplier = edge(m, n)
        quotient_residue = (
            pow(multiplier, -1, modulus) * (residue - carry)
        ) % modulus if modulus > 1 else 0
        residue = edge_residue + edge_modulus * quotient_residue
        modulus *= edge_modulus
    return residue, modulus


def boundaries(schedule: tuple[int, ...]) -> list[int]:
    result: list[int] = []
    position = 0
    for m in schedule:
        result.append(position)
        position += stage_length(m)
    return result


def phi_residue(schedule: tuple[int, ...]) -> tuple[int, int]:
    positions = boundaries(schedule)
    total = sum(stage_length(m) for m in schedule)
    modulus = 64**total
    value = 0
    for position in positions:
        denominator = pow(81, position + 1, modulus)
        term = 17 * pow(64, position, modulus) * pow(denominator, -1, modulus)
        value = (value + term) % modulus
    return value, modulus


def context_series_residue(schedule: tuple[int, ...]) -> tuple[int, int]:
    m0 = schedule[0]
    target_lengths = [stage_length(m) for m in schedule[1:]]
    exponent = 0
    modulus = 64 ** sum(target_lengths)
    value = 0
    for ell in [0] + target_lengths[:-1]:
        if ell:
            exponent += ell
        denominator = pow(81, stage_length(m0) + exponent, modulus)
        term = 17 * pow(64, exponent, modulus) * pow(denominator, -1, modulus)
        value = (value + term) % modulus
    return value, modulus


def series_cylinder_checks() -> dict[str, Any]:
    schedules: list[tuple[int, ...]] = []
    for edges in range(1, 4):
        schedules.extend(
            tuple(schedule)
            for schedule in product(range(4), repeat=edges + 1)
        )

    checked = 0
    maximum_bits = 0
    for schedule in schedules:
        context, context_modulus = cylinder(schedule)
        _, first_modulus, _, first_constant = params(schedule[0])
        initial_state = first_modulus * context + first_constant

        sparse_value, state_modulus = phi_residue(schedule)
        assert state_modulus == first_modulus * context_modulus
        assert initial_state % state_modulus == sparse_value

        context_value, context_series_modulus = context_series_residue(schedule)
        assert context_series_modulus == context_modulus
        assert (81 * context + 1) % context_modulus == context_value

        maximum_bits = max(maximum_bits, state_modulus.bit_length() - 1)
        checked += 1

    return {
        "schedules": checked,
        "maximum_prefix_bits": maximum_bits,
    }


def fibonacci_bits(length: int) -> tuple[int, ...]:
    word = "0"
    while len(word) < length:
        word = "".join("01" if symbol == "0" else "0" for symbol in word)
    return tuple(int(symbol) for symbol in word[:length])


def stack_positions(count: int) -> tuple[list[int], list[int]]:
    directive = fibonacci_bits(count + 2)
    heights = [1]
    for bit in directive:
        heights.append(heights[-1] + (17 if bit == 0 else 18))

    positions = [0]
    for j in range(count):
        positions.append(positions[-1] + stage_length(heights[j]))
    return positions, heights


def exact_factor_complexity(n: int) -> int:
    # Once all later gaps exceed n, every later factor contains at most one 1.
    positions, _ = stack_positions(max(20, n // 150 + 20))
    while positions[-1] - positions[-2] <= n or positions[-2] - positions[-3] <= n:
        positions, _ = stack_positions(len(positions) + 20)

    last_pair = max(
        i
        for i in range(len(positions) - 1)
        if positions[i + 1] - positions[i] < n
    )
    maximum_start = positions[last_pair + 1]

    factors: set[tuple[int, ...]] = set()
    left = 0
    right = 0
    for start in range(maximum_start + 1):
        while left < len(positions) and positions[left] < start:
            left += 1
        if right < left:
            right = left
        while right < len(positions) and positions[right] < start + n:
            right += 1
        factors.add(tuple(position - start for position in positions[left:right]))

    factors.add(())
    for offset in range(n):
        factors.add((offset,))
    return len(factors)


def complexity_checks() -> dict[str, Any]:
    increment_bound = 162
    profiles: dict[str, Any] = {}
    for n in (512, 1024, 2048, 4096):
        complexity = exact_factor_complexity(n)
        upper = n * n + n + 1
        lower = max(
            0,
            (n // (10 * increment_bound) - 1) * (2 * n // 5 - 1),
        )
        assert lower <= complexity <= upper
        profiles[str(n)] = {
            "exact_factor_complexity": complexity,
            "ratio_over_n2": f"{complexity / (n * n):.12f}",
            "universal_upper": upper,
            "T9406_lower": lower,
        }
    return {
        "gap_increment_bound": increment_bound,
        "profiles": profiles,
    }


def exponent_bounds() -> dict[str, Any]:
    positions, heights = stack_positions(200)
    m0 = heights[0]
    rows: dict[str, Any] = {}
    for j in (1, 2, 4, 8, 16, 32, 64, 128, 200):
        boundary = positions[j]
        lower = j * (9 * m0 + 1) + 153 * j * (j - 1) // 2
        upper = j * (9 * m0 + 1) + 162 * j * (j - 1) // 2
        assert lower <= boundary <= upper
        rows[str(j)] = {
            "boundary": boundary,
            "lower": lower,
            "upper": upper,
        }
    return rows


def balanced_series_checks() -> dict[str, Any]:
    directive = fibonacci_bits(24)
    heights = [1]
    for bit in directive:
        heights.append(heights[-1] + (17 if bit == 0 else 18))

    rows: dict[str, Any] = {}
    for stages in (1, 2, 3, 4, 6, 8, 12):
        schedule = tuple(heights[: stages + 1])
        context, context_modulus = cylinder(schedule)
        _, first_modulus, _, first_constant = params(schedule[0])
        initial_state = first_modulus * context + first_constant
        sparse_value, state_modulus = phi_residue(schedule)
        assert initial_state % state_modulus == sparse_value
        rows[str(stages)] = {
            "last_height": heights[stages],
            "code_prefix_bits": state_modulus.bit_length() - 1,
            "context_bits": context_modulus.bit_length() - 1,
            "context_least_rep_bits": context.bit_length(),
        }
    return rows


def generate() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "experiment_id": "X-9405",
        "research_question": (
            "Does the active stack cylinder equal a sparse p-adic partial-theta "
            "series, and what is the exact factor-complexity class of its support word?"
        ),
        "series_cylinder_equivalence": series_cylinder_checks(),
        "balanced_prefixes": balanced_series_checks(),
        "support_exponent_bounds": exponent_bounds(),
        "support_factor_complexity": complexity_checks(),
        "interpretation": {
            "proved_by_finite_computation": [
                "the frozen sparse-series/cylinder congruences",
                "the frozen balanced-prefix congruences",
                "the frozen support-position bounds",
                "the frozen exact finite factor-complexity profiles",
            ],
            "not_proved_by_finite_computation": [
                "the universal sparse-series normal form",
                "the universal Theta(n^2) theorem",
                "p-adic irrationality or transcendence of the partial-theta value",
                "nonexistence of an ordinary stack context or Collatz counterexample",
            ],
        },
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = generate()
    data = canonical_bytes(payload)
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
