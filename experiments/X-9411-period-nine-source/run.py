#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

sys.set_int_max_str_digits(0)


def transfer_data(word: tuple[int, ...]) -> tuple[int, int, tuple[int, ...]]:
    """Return S(W), e(W), and the exponents in P_W(X)."""
    r = len(word)
    cumulative = 0
    cumulative_sum = 0
    prefix_exponents = [0]
    for j in range(1, r):
        cumulative += word[j - 1]
        cumulative_sum += cumulative
        prefix_exponents.append(j + 9 * cumulative_sum)

    cumulative = 0
    total_cumulative_sum = 0
    for letter in word:
        cumulative += letter
        total_cumulative_sum += cumulative
    e = r + 9 * total_cumulative_sum
    return sum(word), e, tuple(prefix_exponents)


def direct_block_sum(
    word: tuple[int, ...], starting_height: int, blocks: int
) -> Fraction:
    """Finite direct sum for the first ``blocks * len(word)`` stage terms."""
    T = Fraction(64, 81)
    increments = word * blocks
    exponent = 0
    height = starting_height
    total = Fraction(1)
    for increment in increments[:-1]:
        height += increment
        exponent += 9 * height + 1
        total += T**exponent
    return total


def phase_block_sum(
    word: tuple[int, ...], starting_height: int, blocks: int
) -> Fraction:
    """The same finite sum, grouped into periodic Tschakaloff phases."""
    T = Fraction(64, 81)
    r = len(word)
    total_height, e, prefix_exponents = transfer_data(word)
    X = T ** (9 * starting_height)
    lam = T ** (9 * total_height)
    R = lam**r
    Z = T**e * X**r

    total = Fraction(0)
    for j in range(r):
        coefficient = T ** prefix_exponents[j] * X**j
        point = Z * lam**j
        for n in range(blocks):
            total += coefficient * R ** (n * (n - 1) // 2) * point**n
    return total


def decimal_text(value: Decimal, places: int = 18) -> str:
    quantum = Decimal(1).scaleb(-places)
    return format(value.quantize(quantum), "f")


def gamma_table() -> dict[str, Any]:
    getcontext().prec = 80
    one = Decimal(1)
    gamma = one - Decimal(64).ln() / Decimal(81).ln()
    rows: dict[str, Any] = {}
    for dimension in range(1, 13):
        D = Decimal(dimension)
        threshold = (
            Decimal(2 * dimension + 1)
            - (one + Decimal(4 * dimension * dimension)).sqrt()
        ) / Decimal(2 * dimension)
        rows[str(dimension)] = {
            "Gamma_D": decimal_text(threshold),
            "gamma_less_than_Gamma_D": gamma < threshold,
        }
    return {
        "gamma": decimal_text(gamma),
        "rows": rows,
        "last_dimension_passing": max(
            int(d) for d, row in rows.items() if row["gamma_less_than_Gamma_D"]
        ),
    }


def source_endpoint_checks() -> dict[str, Any]:
    return {
        "dimension_9": {
            "64_pow_93_gt_81_pow_88": 64**93 > 81**88,
            "difference_64_pow_93_minus_81_pow_88": str(64**93 - 81**88),
            "559_sq_minus_325_times_31_sq": 559**2 - 325 * 31**2,
            "condition_certified": (64**93 > 81**88)
            and (559**2 - 325 * 31**2 > 0),
        },
        "dimension_10": {
            "64_pow_20_lt_81_pow_19": 64**20 < 81**19,
            "difference_81_pow_19_minus_64_pow_20": str(81**19 - 64**20),
            "401_minus_20_sq": 401 - 20**2,
            "condition_fails": (64**20 < 81**19) and (401 > 20**2),
        },
    }


def orbit_separation_checks() -> dict[str, Any]:
    pairs = 0
    for r in range(1, 11):
        for i in range(r):
            for j in range(i + 1, r):
                pairs += 1
                difference = i - j
                assert difference % r != 0
    return {
        "period_lengths": [1, 10],
        "phase_pairs_checked": pairs,
        "all_distinct_mod_period": True,
    }


def decomposition_checks() -> dict[str, Any]:
    words = (
        (1,),
        (1, 2),
        (1, 1, 2),
        (1, 1, 1, 1, 1, 1, 1, 1, 2),
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
    )
    records: list[dict[str, Any]] = []
    checks = 0
    for word in words:
        for starting_height in (0, 1):
            for blocks in (1, 2, 3):
                direct = direct_block_sum(word, starting_height, blocks)
                phased = phase_block_sum(word, starting_height, blocks)
                assert direct == phased
                checks += 1
                if blocks == 3:
                    records.append(
                        {
                            "word": list(word),
                            "starting_height": starting_height,
                            "blocks": blocks,
                            "fraction_sha256": hashlib.sha256(
                                f"{direct.numerator}/{direct.denominator}".encode()
                            ).hexdigest(),
                            "numerator_bits": direct.numerator.bit_length(),
                            "denominator_bits": direct.denominator.bit_length(),
                        }
                    )
    return {
        "exact_identities_checked": checks,
        "selected_records": records,
    }


def adjacent_optimistic_ceiling() -> dict[str, Any]:
    getcontext().prec = 80
    base = Decimal(64).ln() / Decimal(81).ln()
    rows: dict[str, Any] = {}
    for r in range(1, 16):
        factor = Decimal(r * r + r + 3) / Decimal(r * (r + 1))
        value = base * factor
        rows[str(r)] = {
            "max_zero_height_cost_exponent": decimal_text(value),
            "above_one": value > 1,
        }
    assert 64**45 > 81**42
    assert 64**59 < 81**56
    assert 64**113 < 81**110
    return {
        "formula": "log_81(64)*(r^2+r+3)/(r*(r+1))",
        "rows": rows,
        "last_period_above_one": 6,
        "first_period_below_one": 7,
        "exact_boundary_checks": {
            "r_6": "64^45 > 81^42",
            "r_7": "64^59 < 81^56",
            "r_10": "64^113 < 81^110",
        },
    }


def scalar_phase_exponents() -> dict[str, Any]:
    getcontext().prec = 80
    exponent = Decimal(9) / (Decimal(81).ln() / Decimal(2).ln())
    return {
        "generic_scalar_tschakaloff_pade_exponent": decimal_text(exponent),
        "greater_than_one": exponent > 1,
    }


def generate() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "experiment_id": "X-9411",
        "research_question": (
            "Does the Vaananen-Wallisser source condition close exactly periods "
            "through nine, and what exact period-ten interfaces remain after "
            "scalar-phase and adjacent-order audits?"
        ),
        "source_endpoint_checks": source_endpoint_checks(),
        "numerical_source_table": gamma_table(),
        "orbit_separation": orbit_separation_checks(),
        "periodic_phase_decomposition": decomposition_checks(),
        "generic_scalar_phase": scalar_phase_exponents(),
        "adjacent_order_optimistic_ceiling": adjacent_optimistic_ceiling(),
        "interpretation": {
            "proved_by_finite_computation": [
                "the displayed exact integer endpoint inequalities",
                "the frozen finite periodic phase decompositions",
                "the frozen orbit-separation and numerical threshold table",
                "the exact arithmetic in the optimistic adjacent-order ceiling table",
            ],
            "not_proved_by_finite_computation": [
                "the Vaananen-Wallisser source theorem",
                "the universal native period-nine corollary",
                "the generic scalar Pade proof",
                "period-ten special-vector irrationality",
                "the Collatz conjecture",
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

    data = canonical_bytes(generate())
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
