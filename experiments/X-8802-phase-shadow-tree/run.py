#!/usr/bin/env python3
"""Exact connector and rational-base controls for the 5x+1 drift-isolation chart.

This experiment validates finite interfaces only:
- the signed phase-shadow identity;
- the complete {-1,-2} connector skeleton and its coboundary;
- signed cycle reconstruction in a frozen parity-word range;
- the exact rational-base 5/4 low-digit-tree conjugacy;
- a bounded survivor-depth census.

No finite result proves or disproves an infinite positive survivor.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path
from typing import Iterable, Sequence


def shortcut_step(a: int, n: int) -> int:
    if a < 3 or a % 2 == 0:
        raise ValueError("a must be odd and >= 3")
    return n // 2 if n % 2 == 0 else (a * n + 1) // 2


def iterate(a: int, n: int, length: int) -> tuple[tuple[int, ...], int]:
    word: list[int] = []
    for _ in range(length):
        word.append(n & 1)
        n = shortcut_step(a, n)
    return tuple(word), n


def affine_correction(a: int, word: Sequence[int]) -> tuple[int, int]:
    correction = 0
    weight = 0
    for k, bit in enumerate(word):
        if bit not in (0, 1):
            raise ValueError("word must be binary")
        if bit:
            correction = a * correction + (1 << k)
            weight += 1
    return correction, weight


def primitive_period(a: int, seed: int, candidate_length: int) -> int:
    for period in range(1, candidate_length + 1):
        if candidate_length % period == 0 and iterate(a, seed, period)[1] == seed:
            return period
    return candidate_length


def canonical_rotation(values: Sequence[int]) -> tuple[int, ...]:
    values = tuple(values)
    return min(values[i:] + values[:i] for i in range(len(values)))


def enumerate_signed_cycles(a: int, max_word_length: int) -> list[dict[str, object]]:
    """Reconstruct every nonzero signed cycle represented in the frozen word range."""
    cycles: dict[tuple[int, ...], dict[str, object]] = {}
    for length in range(1, max_word_length + 1):
        for word in product((0, 1), repeat=length):
            if not any(word):
                continue
            correction, weight = affine_correction(a, word)
            denominator = (1 << length) - a**weight
            if denominator == 0 or correction % denominator != 0:
                continue
            seed = correction // denominator
            if seed == 0:
                continue
            replay_word, endpoint = iterate(a, seed, length)
            if replay_word != word or endpoint != seed:
                continue

            period = primitive_period(a, seed, length)
            orbit: list[int] = []
            n = seed
            for _ in range(period):
                orbit.append(n)
                n = shortcut_step(a, n)
            canonical_orbit = canonical_rotation(orbit)
            canonical_seed = canonical_orbit[0]
            canonical_word, endpoint = iterate(a, canonical_seed, period)
            if endpoint != canonical_seed:
                raise AssertionError("canonical signed cycle did not close")
            primitive_correction, primitive_weight = affine_correction(
                a, canonical_word
            )
            primitive_denominator = (1 << period) - a**primitive_weight
            sign_class = "positive_contracting" if canonical_seed > 0 else "negative_expanding"
            if canonical_seed > 0 and primitive_denominator <= 0:
                raise AssertionError("positive cycle violated sign duality")
            if canonical_seed < 0 and primitive_denominator >= 0:
                raise AssertionError("negative cycle violated sign duality")

            cycles[canonical_orbit] = {
                "seed": canonical_seed,
                "sign_class": sign_class,
                "period": period,
                "parity_word": "".join(str(bit) for bit in canonical_word),
                "weight": primitive_weight,
                "correction": primitive_correction,
                "cycle_denominator_2L_minus_aS": primitive_denominator,
                "orbit": list(canonical_orbit),
            }
    return sorted(
        cycles.values(),
        key=lambda item: (item["sign_class"], item["period"], item["seed"]),
    )


def phase_indicator(phase: int) -> int:
    if phase == -1:
        return 1
    if phase == -2:
        return 0
    raise ValueError("phase must be -1 or -2")


def expected_phase_after(phase: int, length: int) -> int:
    return phase if length % 2 == 0 else (-3 - phase)


def connector_weight(phase: int, length: int) -> int:
    endpoint = expected_phase_after(phase, length)
    numerator = length + phase_indicator(phase) - phase_indicator(endpoint)
    if numerator % 2:
        raise AssertionError("connector coboundary was not integral")
    return numerator // 2


def check_phase_shadow(max_length: int, q_max: int) -> dict[str, object]:
    checks = 0
    connector_rows: list[dict[str, object]] = []
    sample_lengths = {1, 2, 3, max_length}
    for phase in (-2, -1):
        for length in range(1, max_length + 1):
            expected_endpoint = expected_phase_after(phase, length)
            expected_weight = connector_weight(phase, length)
            expected_word, phase_endpoint = iterate(5, phase, length)
            if phase_endpoint != expected_endpoint:
                raise AssertionError("negative phase skeleton did not alternate")
            if sum(expected_word) != expected_weight:
                raise AssertionError("connector weight formula failed")

            for q in range(1, q_max + 1):
                seed = (1 << length) * q + phase
                if seed <= 0:
                    continue
                replay_word, endpoint = iterate(5, seed, length)
                expected = 5**expected_weight * q + expected_endpoint
                if replay_word != expected_word or endpoint != expected:
                    raise AssertionError(
                        f"phase-shadow failure: phase={phase}, L={length}, q={q}"
                    )
                checks += 1

            if length in sample_lengths:
                connector_rows.append(
                    {
                        "start_phase": phase,
                        "length": length,
                        "end_phase": expected_endpoint,
                        "parity_word": "".join(str(bit) for bit in expected_word),
                        "weight": expected_weight,
                        "coboundary_twice_weight_minus_length": (
                            2 * expected_weight - length
                        ),
                        "identity": (
                            f"T_5^{length}(2^{length}*q{phase:+d})="
                            f"5^{expected_weight}*q{expected_endpoint:+d}"
                        ),
                    }
                )

    closed_circuit_checks = 0
    for total_length in range(2, 2 * max_length + 1, 2):
        for phase in (-2, -1):
            endpoint = expected_phase_after(phase, total_length)
            weight = connector_weight(phase, total_length)
            if endpoint != phase or 2 * weight != total_length:
                raise AssertionError("closed connector circuit failed")
            closed_circuit_checks += 1

    return {
        "max_length": max_length,
        "q_max": q_max,
        "physical_replay_checks": checks,
        "closed_circuit_checks": closed_circuit_checks,
        "connector_rows": connector_rows,
        "interpretation": (
            "The odd-step excess is the phase coboundary "
            "chi(start)-chi(end); it vanishes on every closed phase circuit."
        ),
    }


def chart_macro_step_from_A(A: int) -> int:
    if A <= 0 or A % 4 not in (2, 3):
        raise ValueError("A must be positive and in a chart phase")
    return shortcut_step(5, shortcut_step(5, A))


def low_digit_child(x: int) -> tuple[int, int] | None:
    residue = x % 4
    if residue == 0:
        digit = 0
    elif residue == 3:
        digit = 1
    else:
        return None
    numerator = 5 * x + digit
    if numerator % 4:
        raise AssertionError("low-digit child was not integral")
    return numerator // 4, digit


def chart_survival_depth(A: int, cap: int) -> tuple[int, int, str]:
    depth = 0
    phase_bits: list[str] = []
    while depth < cap and A % 4 in (2, 3):
        phase_bits.append(str((A + 2) % 4))
        A = chart_macro_step_from_A(A)
        depth += 1
    return depth, A, "".join(phase_bits)


def check_rational_base_conjugacy(max_A: int, depth_cap: int) -> dict[str, object]:
    checks = 0
    survivors_by_depth = [0] * (depth_cap + 1)
    records: list[dict[str, object]] = []
    record_depth = -1

    for A0 in range(1, max_A + 1):
        A = A0
        M = A + 2
        X = A + 1
        depth = 0
        digits: list[str] = []

        while depth < depth_cap and A % 4 in (2, 3):
            eps = M % 4
            if eps not in (0, 1):
                raise AssertionError("shifted chart residue mismatch")
            M_next = (5 * M - eps) // 4
            if M_next != (5 * M) // 4:
                raise AssertionError("floor-map conjugacy failed")
            A_next = chart_macro_step_from_A(A)
            if M_next != A_next + 2:
                raise AssertionError("A/M conjugacy failed")

            delta = 1 - eps
            child = low_digit_child(X)
            if child is None:
                raise AssertionError("chart state had no low-digit tree child")
            X_next, tree_digit = child
            if tree_digit != delta or X_next != M_next - 1:
                raise AssertionError("rational-base low-digit conjugacy failed")
            if 4 * X_next != 5 * X + delta:
                raise AssertionError("rational-base edge equation failed")

            checks += 1
            digits.append(str(delta))
            A, M, X = A_next, M_next, X_next
            depth += 1

        for d in range(depth + 1):
            survivors_by_depth[d] += 1

        if depth > record_depth:
            record_depth = depth
            records.append(
                {
                    "seed_A": A0,
                    "root_X_equals_A_plus_1": A0 + 1,
                    "survival_depth": depth,
                    "low_digit_path": "".join(digits),
                    "first_exit_A": A,
                }
            )

    return {
        "max_A": max_A,
        "depth_cap": depth_cap,
        "edge_checks": checks,
        "survivors_by_at_least_depth": survivors_by_depth,
        "record_holders": records,
        "maximum_depth_observed": record_depth,
        "interpretation": (
            "A positive infinite 4->5 chart survivor is exactly an infinite path "
            "from X=A+1 in the base-5/4 representation tree using only edge labels "
            "0 and 1. The finite census is not an existence or nonexistence proof."
        ),
    }


def digest_json(value: object) -> str:
    rendered = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(rendered).hexdigest()


def build_results(args: argparse.Namespace) -> dict[str, object]:
    phase_shadow = check_phase_shadow(args.connector_max_length, args.connector_q_max)
    cycles = enumerate_signed_cycles(5, args.signed_cycle_max_length)
    rational_tree = check_rational_base_conjugacy(
        args.max_A, args.survival_depth_cap
    )

    negative_cycles = [c for c in cycles if c["seed"] < 0]
    positive_cycles = [c for c in cycles if c["seed"] > 0]
    if [c["orbit"] for c in negative_cycles] != [[-2, -1]]:
        raise AssertionError("frozen signed census did not isolate the mandatory negative 2-cycle")
    required_positive = {
        (1, 3, 8, 4, 2),
        (13, 33, 83, 208, 104, 52, 26),
        (17, 43, 108, 54, 27, 68, 34),
    }
    found_positive = {tuple(c["orbit"]) for c in positive_cycles}
    if not required_positive.issubset(found_positive):
        raise AssertionError("mandatory positive control cycles were not recovered")

    core = {
        "experiment_id": "X-8802",
        "classification": "EXACT_FINITE_COMPUTATION",
        "signed_phase_shadow": phase_shadow,
        "signed_cycle_census": {
            "multiplier": 5,
            "max_word_length": args.signed_cycle_max_length,
            "cycles": cycles,
            "negative_cycle_count": len(negative_cycles),
            "positive_cycle_count": len(positive_cycles),
            "boundary": (
                "Absence of additional cycles in this finite parity-word range "
                "is not a proof of global uniqueness."
            ),
        },
        "rational_base_low_digit_tree": rational_tree,
        "claim_boundary": (
            "The algebraic identities are exact. The cycle and seed censuses are "
            "finite and do not prove or refute an infinite positive chart survivor."
        ),
    }
    core["content_sha256"] = digest_json(core)
    return core


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--connector-max-length", type=int, default=20)
    parser.add_argument("--connector-q-max", type=int, default=1000)
    parser.add_argument("--signed-cycle-max-length", type=int, default=18)
    parser.add_argument("--max-A", type=int, default=1_000_000)
    parser.add_argument("--survival-depth-cap", type=int, default=64)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-results", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = build_results(args)
    rendered = json.dumps(results, indent=2, sort_keys=True) + "\n"

    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")

    if args.check_results is not None:
        expected = args.check_results.read_text(encoding="utf-8")
        if expected != rendered:
            raise SystemExit("canonical result mismatch")

    if args.output is None and args.check_results is None:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
