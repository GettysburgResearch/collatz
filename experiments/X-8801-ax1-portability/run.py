#!/usr/bin/env python3
"""Exact portability controls for the generalized shortcut map T_a.

This experiment deliberately separates:
- universal algebraic facts that hold for every odd multiplier a;
- multiplier-sensitive constants in a generic expanding digit chart;
- finite observations on the 5x+1 orbit of 7.

Nothing in this file proves that any 5x+1 orbit diverges.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from decimal import Decimal, localcontext
from itertools import combinations, product
from pathlib import Path
from typing import Iterable, Sequence


def shortcut_step(a: int, n: int) -> int:
    """One shortcut ax+1 step on positive integers."""
    if a < 3 or a % 2 == 0:
        raise ValueError("a must be an odd integer >= 3")
    if n <= 0:
        raise ValueError("n must be positive")
    return n // 2 if n % 2 == 0 else (a * n + 1) // 2


def v2(n: int) -> int:
    """2-adic valuation of a nonzero integer."""
    if n == 0:
        raise ValueError("v2(0) is not finite")
    n = abs(n)
    return (n & -n).bit_length() - 1


def affine_correction(a: int, word: Sequence[int]) -> tuple[int, int]:
    """Return (B_a(word), weight(word)).

    For an admissible parity word eps_0,...,eps_{L-1},

        2^L T_a^L(n) = a^s n + B_a(word).
    """
    correction = 0
    weight = 0
    for k, bit in enumerate(word):
        if bit not in (0, 1):
            raise ValueError("parity words must be binary")
        if bit:
            correction = a * correction + (1 << k)
            weight += 1
    return correction, weight


def orbit_prefix(a: int, seed: int, length: int) -> tuple[tuple[int, ...], int]:
    """Return the parity word and endpoint after length shortcut steps."""
    n = seed
    word: list[int] = []
    for _ in range(length):
        word.append(n & 1)
        n = shortcut_step(a, n)
    return tuple(word), n


def primitive_word_period(word: Sequence[int]) -> int:
    length = len(word)
    for period in range(1, length + 1):
        if length % period == 0 and all(
            word[i] == word[i % period] for i in range(length)
        ):
            return period
    return length


def canonical_rotation(values: Sequence[int]) -> tuple[int, ...]:
    values = tuple(values)
    return min(values[i:] + values[:i] for i in range(len(values)))


def enumerate_positive_cycles(a: int, max_word_length: int) -> list[dict[str, object]]:
    """Exhaust parity words and reconstruct all positive cycles in scope.

    A word is accepted only after divisibility, positivity, full parity replay,
    and exact return are checked. Repeated words and rotations are deduplicated.
    """
    cycles: dict[tuple[int, ...], dict[str, object]] = {}
    for length in range(1, max_word_length + 1):
        for word in product((0, 1), repeat=length):
            if not any(word):
                continue
            correction, weight = affine_correction(a, word)
            denominator = (1 << length) - a**weight
            if denominator <= 0 or correction % denominator != 0:
                continue
            seed = correction // denominator
            if seed <= 0:
                continue
            replay_word, endpoint = orbit_prefix(a, seed, length)
            if replay_word != word or endpoint != seed:
                continue

            period = primitive_word_period(word)
            _, period_endpoint = orbit_prefix(a, seed, period)
            if period_endpoint != seed:
                period = length

            orbit: list[int] = []
            n = seed
            for _ in range(period):
                orbit.append(n)
                n = shortcut_step(a, n)
            canonical_orbit = canonical_rotation(orbit)
            canonical_seed = canonical_orbit[0]
            canonical_word, endpoint = orbit_prefix(a, canonical_seed, period)
            if endpoint != canonical_seed:
                raise AssertionError("canonicalized orbit did not close")

            cycles[canonical_orbit] = {
                "seed": canonical_seed,
                "period": period,
                "parity_word": "".join(str(bit) for bit in canonical_word),
                "orbit": list(canonical_orbit),
                "weight": sum(canonical_word),
                "correction": affine_correction(a, canonical_word)[0],
                "cycle_denominator": (1 << period) - a ** sum(canonical_word),
            }

    return sorted(cycles.values(), key=lambda item: (item["period"], item["seed"]))



def enumerate_fixed_phase_blocks(a: int, length: int, weight: int) -> list[dict[str, object]]:
    """Find same-phase blocks T_a^L(2^L q+d)=a^s q+d.

    The affine formula forces d=-B_a(w)/(a^s-2^L). Every returned phase is
    integral and is replay-checked on a positive representative.
    """
    u = 1 << length
    v = a**weight
    denominator = v - u
    if denominator <= 0:
        return []

    blocks: list[dict[str, object]] = []
    for odd_positions in combinations(range(length), weight):
        odd_set = set(odd_positions)
        word = tuple(1 if k in odd_set else 0 for k in range(length))
        correction, _ = affine_correction(a, word)
        if correction % denominator != 0:
            continue

        phase = -(correction // denominator)
        q = max(1, (-phase) // u + 2)
        seed = u * q + phase
        replay_word, endpoint = orbit_prefix(a, seed, length)
        expected = v * q + phase
        if replay_word != word or endpoint != expected:
            raise AssertionError(
                f"fixed-phase replay failed: a={a}, word={word}, phase={phase}"
            )
        blocks.append(
            {
                "parity_word": "".join(str(bit) for bit in word),
                "weight": weight,
                "correction": correction,
                "phase": phase,
                "phase_mod_2L": phase % u,
                "identity": f"T_{a}^{length}({u}*q{phase:+d})={v}*q{phase:+d}",
            }
        )
    return blocks


def check_5x1_four_to_five_chart(max_q: int) -> dict[str, object]:
    """Exhaustively verify the two exact T_5^2 phase identities."""
    checks = 0
    for q in range(1, max_q + 1):
        for phase, expected_word in ((-1, (1, 0)), (-2, (0, 1))):
            seed = 4 * q + phase
            word, endpoint = orbit_prefix(5, seed, 2)
            if word != expected_word or endpoint != 5 * q + phase:
                raise AssertionError(
                    f"4->5 chart failed: q={q}, phase={phase}, "
                    f"word={word}, endpoint={endpoint}"
                )
            checks += 1
    return {
        "q_max": max_q,
        "checks": checks,
        "phases": [-2, -1],
        "identities": [
            "T_5^2(4q-1)=5q-1 with parity word 10",
            "T_5^2(4q-2)=5q-2 with parity word 01",
        ],
    }


def check_affine_formula(
    multipliers: Iterable[int], max_seed: int, max_length: int
) -> dict[str, int]:
    checks = 0
    for a in multipliers:
        for seed in range(1, max_seed + 1):
            n = seed
            word: list[int] = []
            for length in range(1, max_length + 1):
                word.append(n & 1)
                n = shortcut_step(a, n)
                correction, weight = affine_correction(a, word)
                if (1 << length) * n != a**weight * seed + correction:
                    raise AssertionError(
                        f"affine formula failed: a={a}, seed={seed}, length={length}"
                    )
                checks += 1
    return {
        "multipliers": len(tuple(multipliers)),
        "max_seed": max_seed,
        "max_length": max_length,
        "checks": checks,
    }


def check_fuel_loss(multipliers: Sequence[int], max_value: int) -> dict[str, int]:
    checks = 0
    for a in multipliers:
        for x in range(1, max_value + 1):
            for y in range(x + 1, max_value + 1):
                if (x & 1) != (y & 1):
                    continue
                before = v2(y - x)
                after = v2(shortcut_step(a, y) - shortcut_step(a, x))
                if after != before - 1:
                    raise AssertionError(
                        f"fuel loss failed: a={a}, x={x}, y={y}, "
                        f"before={before}, after={after}"
                    )
                checks += 1
    return {
        "multipliers": len(multipliers),
        "max_value": max_value,
        "checks": checks,
    }


def decimal_text(value: Decimal, places: int = 36) -> str:
    return format(value, f".{places}f")


def chart_constants(a: int, macro_length: int = 6, macro_weight: int = 4) -> dict[str, object]:
    u = Decimal(2) ** macro_length
    v = Decimal(a) ** macro_weight
    if v <= u:
        raise ValueError("the chart must be supercritical: a^s > 2^L")
    with localcontext() as context:
        context.prec = 80
        delta = v.ln() / u.ln() - Decimal(1)
        kappa = Decimal(1) / delta
        fair_drift_log2 = Decimal(a).ln() / Decimal(2).ln() / Decimal(2) - Decimal(1)
    return {
        "a": a,
        "macro_length": macro_length,
        "macro_weight": macro_weight,
        "U": int(u),
        "V": int(v),
        "forward_multiplier": f"{int(v)}/{int(u)}",
        "inverse_ratio": f"{int(u)}/{int(v)}",
        "delta_log_U_V_minus_1": decimal_text(delta),
        "factor_complexity_slope_kappa": decimal_text(kappa),
        "fair_parity_log2_drift_model": decimal_text(fair_drift_log2),
    }


def exact_orbit_ledger(
    a: int,
    seed: int,
    steps: int,
    checkpoint_interval: int,
) -> dict[str, object]:
    """Stream an exact finite orbit ledger without storing the trajectory.

    The parity digest hashes ASCII 0/1 for every source-state parity.
    The checkpoint digest hashes, at each checkpoint, the 8-byte step number,
    8-byte byte-length, and the unsigned big-endian value.
    """
    n = seed
    odd_steps = 0
    maximum_bit_length = n.bit_length()
    maximum_step = 0
    minimum_value = n
    last_step_at_or_below_seed = 0
    record_high_count = 1
    last_record_high_step = 0

    parity_digest = hashlib.sha256()
    parity_buffer = bytearray()
    checkpoint_digest = hashlib.sha256()

    for step_index in range(steps):
        parity = n & 1
        odd_steps += parity
        parity_buffer.append(48 + parity)
        if len(parity_buffer) >= 8192:
            parity_digest.update(parity_buffer)
            parity_buffer.clear()

        n = shortcut_step(a, n)
        bit_length = n.bit_length()

        if bit_length > maximum_bit_length:
            maximum_bit_length = bit_length
            maximum_step = step_index + 1
            record_high_count += 1
            last_record_high_step = step_index + 1

        minimum_value = min(minimum_value, n)
        if n <= seed:
            last_step_at_or_below_seed = step_index + 1

        if (step_index + 1) % checkpoint_interval == 0:
            raw = n.to_bytes((bit_length + 7) // 8, "big")
            checkpoint_digest.update((step_index + 1).to_bytes(8, "big"))
            checkpoint_digest.update(len(raw).to_bytes(8, "big"))
            checkpoint_digest.update(raw)

    if parity_buffer:
        parity_digest.update(parity_buffer)

    final_raw = n.to_bytes((n.bit_length() + 7) // 8, "big")
    sys.set_int_max_str_digits(0)

    return {
        "a": a,
        "seed": seed,
        "steps": steps,
        "checkpoint_interval": checkpoint_interval,
        "odd_steps": odd_steps,
        "even_steps": steps - odd_steps,
        "minimum_value": minimum_value,
        "last_step_at_or_below_seed": last_step_at_or_below_seed,
        "final_bit_length": n.bit_length(),
        "final_decimal_digits": len(str(n)),
        "maximum_bit_length": maximum_bit_length,
        "maximum_bit_length_step": maximum_step,
        "record_high_count": record_high_count,
        "last_record_high_step": last_record_high_step,
        "final_value_sha256": hashlib.sha256(final_raw).hexdigest(),
        "parity_ascii_sha256": parity_digest.hexdigest(),
        "checkpoint_values_sha256": checkpoint_digest.hexdigest(),
        "interpretation": (
            "Exact finite observation only. It does not prove that the orbit diverges "
            "or avoids a later cycle."
        ),
    }


def build_results(args: argparse.Namespace) -> dict[str, object]:
    multipliers = (3, 5, 7, 9)
    affine = check_affine_formula(
        multipliers=multipliers,
        max_seed=args.affine_max_seed,
        max_length=args.affine_max_length,
    )
    fuel = check_fuel_loss(multipliers, args.fuel_max_value)

    constants_3_64_to_81 = chart_constants(3, macro_length=6, macro_weight=4)
    constants_5_4_to_5 = chart_constants(5, macro_length=2, macro_weight=1)
    constants_5_same_shape = chart_constants(5, macro_length=6, macro_weight=4)
    with localcontext() as context:
        context.prec = 80
        kappa_3 = Decimal(
            constants_3_64_to_81["factor_complexity_slope_kappa"]
        )
        kappa_5_actual = Decimal(
            constants_5_4_to_5["factor_complexity_slope_kappa"]
        )
        kappa_5_same_shape = Decimal(
            constants_5_same_shape["factor_complexity_slope_kappa"]
        )
        actual_slope_difference = kappa_3 - kappa_5_actual
        actual_slope_ratio = kappa_3 / kappa_5_actual
        same_shape_slope_difference = kappa_3 - kappa_5_same_shape
        same_shape_slope_ratio = kappa_3 / kappa_5_same_shape

    cycles = {
        str(a): enumerate_positive_cycles(a, args.max_cycle_length)
        for a in (3, 5)
    }

    expected_5x1_controls = {
        (1, 3, 8, 4, 2),
        (13, 33, 83, 208, 104, 52, 26),
        (17, 43, 108, 54, 27, 68, 34),
    }
    found_5x1_controls = {tuple(item["orbit"]) for item in cycles["5"]}
    if not expected_5x1_controls.issubset(found_5x1_controls):
        raise AssertionError("mandatory 5x+1 cycle controls were not recovered")

    fixed_phase_census = {
        "a3_length6_weight4": enumerate_fixed_phase_blocks(3, 6, 4),
        "a5_length6_weight4": enumerate_fixed_phase_blocks(5, 6, 4),
        "a5_length2_weight1": enumerate_fixed_phase_blocks(5, 2, 1),
    }
    chart_check = check_5x1_four_to_five_chart(args.chart_max_q)

    return {
        "experiment_id": "X-8801",
        "classification": "EXACT_FINITE_COMPUTATION",
        "map": "T_a(n)=n/2 for even n; (a*n+1)/2 for odd n",
        "scope": {
            "cycle_word_length_max": args.max_cycle_length,
            "affine_max_seed": args.affine_max_seed,
            "affine_max_length": args.affine_max_length,
            "fuel_max_value": args.fuel_max_value,
            "chart_max_q": args.chart_max_q,
            "orbit_steps": args.orbit_steps,
        },
        "universal_affine_formula_checks": affine,
        "universal_one_step_fuel_loss_checks": fuel,
        "positive_cycle_census": cycles,
        "fixed_phase_block_census": fixed_phase_census,
        "exact_5x1_four_to_five_chart": chart_check,
        "expanding_chart_portability": {
            "original_3x1_chart": constants_3_64_to_81,
            "actual_5x1_chart": constants_5_4_to_5,
            "same_length_weight_5x1_diagnostic": constants_5_same_shape,
            "actual_chart_kappa_3_minus_kappa_5": decimal_text(
                actual_slope_difference
            ),
            "actual_chart_kappa_3_over_kappa_5": decimal_text(
                actual_slope_ratio
            ),
            "same_shape_kappa_3_minus_kappa_5": decimal_text(
                same_shape_slope_difference
            ),
            "same_shape_kappa_3_over_kappa_5": decimal_text(
                same_shape_slope_ratio
            ),
            "interpretation": (
                "The height/repetition proof is format-driven, but its strength is "
                "controlled by delta=log_U(V)-1. The genuine T_5 4->5 chart still "
                "has a strong complexity obstruction, while the literal length-6, "
                "weight-4 phase chart fails earlier because 5^4-2^6=561 divides "
                "none of the relevant affine corrections."
            ),
        },
        "orbit_5x1_seed_7": exact_orbit_ledger(
            a=5,
            seed=7,
            steps=args.orbit_steps,
            checkpoint_interval=args.checkpoint_interval,
        ),
        "claim_boundary": (
            "No finite computation here establishes an infinite divergent orbit "
            "for 5x+1 or a counterexample to the Collatz conjecture."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-cycle-length", type=int, default=14)
    parser.add_argument("--affine-max-seed", type=int, default=256)
    parser.add_argument("--affine-max-length", type=int, default=12)
    parser.add_argument("--fuel-max-value", type=int, default=256)
    parser.add_argument("--chart-max-q", type=int, default=100_000)
    parser.add_argument("--orbit-steps", type=int, default=1_000_000)
    parser.add_argument("--checkpoint-interval", type=int, default=1_000)
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
            print("canonical result mismatch", file=sys.stderr)
            return 1

    if args.output is None and args.check_results is None:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
