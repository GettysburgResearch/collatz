#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

A = 4_992_586_555_009
K = 3_149_971_404_836
M = 1_465_129_870_107_858_983
N_STAR = 110_340_992_901_879
PUBLISHED_X8302_FLOOR = 1_567_441_266_425_753_353_472_608
REAL_GAP_UPPER = Fraction(2_364_276_307_615, 10**25)
TERMS = 128


def raw_log_bounds(y: Fraction) -> tuple[Fraction, Fraction]:
    assert 1 <= y <= 2
    z = (y - 1) / (y + 1)
    z2 = z * z
    zpower = z
    partial = Fraction(0)
    for j in range(TERMS):
        partial += zpower / (2 * j + 1)
        zpower *= z2
    lower = 2 * partial
    upper = lower + 2 * zpower / ((2 * TERMS + 1) * (1 - z2))
    return lower, upper


LOG2_LOWER, LOG2_UPPER = raw_log_bounds(Fraction(2))


def log_bounds(x: Fraction) -> tuple[Fraction, Fraction]:
    assert x > 0
    exponent = x.numerator.bit_length() - x.denominator.bit_length()
    scale = Fraction(1 << exponent) if exponent >= 0 else Fraction(1, 1 << (-exponent))
    y = x / scale
    while y < 1:
        exponent -= 1
        y *= 2
    while y >= 2:
        exponent += 1
        y /= 2
    lower_y, upper_y = raw_log_bounds(y)
    if exponent >= 0:
        return exponent * LOG2_LOWER + lower_y, exponent * LOG2_UPPER + upper_y
    return exponent * LOG2_UPPER + lower_y, exponent * LOG2_LOWER + upper_y


def shortcut_orbit(n: int) -> dict[str, int | str]:
    current = n
    steps = 0
    odd_steps = 0
    maximum = n
    digest = hashlib.sha256()
    while True:
        digest.update(f"{current}\n".encode("ascii"))
        if current == 1:
            break
        if current & 1:
            current = (3 * current + 1) // 2
            odd_steps += 1
        else:
            current //= 2
        steps += 1
        maximum = max(maximum, current)
    return {
        "shortcut_steps_to_1": steps,
        "odd_shortcut_steps": odd_steps,
        "maximum_shortcut_state": maximum,
        "trajectory_sha256": digest.hexdigest(),
    }


def generate() -> dict[str, object]:
    log3_lower, log3_upper = log_bounds(Fraction(3))
    theta_lower = A * LOG2_LOWER - K * log3_upper
    theta_upper = A * LOG2_UPPER - K * log3_lower
    assert 0 < theta_lower < theta_upper < Fraction(1, 2**41)
    assert REAL_GAP_UPPER < Fraction(1, 2**41)
    assert M > 2**60

    log_m_lower, _log_m_upper = log_bounds(Fraction(M))
    _log_theta_lower, log_theta_upper = log_bounds(theta_upper)
    _log_gap_lower, log_gap_upper = log_bounds(REAL_GAP_UPPER)
    height_upper = A * LOG2_UPPER + log_theta_upper + log_gap_upper
    sharp_exponent = int(height_upper // log_m_lower + 1)
    assert sharp_exponent * log_m_lower > height_upper

    coarse_exponent = (A - 82 + 59) // 60
    orbit = shortcut_orbit(2 * N_STAR + 1)

    return {
        "schema_version": 1,
        "experiment_id": "X-8307",
        "critical_parameters": {"A": A, "K": K, "M": M, "M_gt_2_pow_60": True},
        "height_certificate": {
            "log_gap_positive": True,
            "one_minus_multiplier_lt_2_pow_minus_41": True,
            "real_gap_upper_fraction": [REAL_GAP_UPPER.numerator, REAL_GAP_UPPER.denominator],
            "real_gap_lt_2_pow_minus_41": True,
            "difference_abs_lt_2_power": A - 82,
            "mixed_place_condition": "B+60*J>=A-82",
            "coarse_sufficient_M_exponent": coarse_exponent,
            "range_reduced_log_sufficient_M_exponent": sharp_exponent,
        },
        "nstar_refutation": {
            "N_star": N_STAR,
            "N_star_mod_16": N_STAR % 16,
            "legal_chart_residues_mod_16": [0, 5, 13],
            "chart_domain_compatible": False,
            "physical_seed": 2 * N_STAR + 1,
            **orbit,
        },
        "published_x8302_floor_gate": {
            "integer_floor": PUBLISHED_X8302_FLOOR,
            "floor_mod_16": PUBLISHED_X8302_FLOOR % 16,
            "frozen_first_chart_symbol": 1,
            "required_residues_for_symbol_1_mod_16": [5, 13],
            "compatible": False,
        },
        "ladder_budget": {
            "reported_odd_prime_lift_order": 7,
            "coarse_odd_prime_bits": 7 * 60,
            "nstar_dyadic_branch_bits": 0,
            "required_mixed_bits_at_least": A - 82,
            "coarse_bit_deficit": (A - 82) - 7 * 60,
            "maximum_standard_binary_prouhet_order_in_fixed_chart_word": 40,
            "maximum_coarse_M_bits_from_that_order": 40 * 60,
        },
        "interpretation": {
            "proved": [
                "an exact sufficient height budget for C-ND=0",
                "the reported N_star is outside both first chart domains",
                "the associated physical seed reaches 1 exactly",
                "odd-prime lifting alone is short of the height gate by trillions of bits",
            ],
            "not_proved": [
                "a replacement chart-compatible quotient",
                "a full-denominator positive cycle",
                "a divergent Collatz seed",
                "the Collatz conjecture or its negation",
            ],
        },
    }


def canonical_bytes(payload: dict[str, object]) -> bytes:
    return (json.dumps(payload, sort_keys=True, indent=2) + "\n").encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()
    data = canonical_bytes(generate())
    if args.write_results:
        args.write_results.parent.mkdir(parents=True, exist_ok=True)
        args.write_results.write_bytes(data)
    if args.check_results and args.check_results.read_bytes() != data:
        raise SystemExit("canonical result mismatch")
    print(data.decode("utf-8"), end="")
    print("SHA256", hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
