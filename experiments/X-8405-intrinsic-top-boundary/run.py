#!/usr/bin/env python3
"""X-8405: exact intrinsic-cell and nineteen-bit top-boundary audit."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

M = 2**19
N = 3**12
DELTA = N - M
WORDS = ("AAAAAB", "AAAABA", "AAABAA", "AABAAA", "ABAAAA", "BAAAAA")
DOMAIN = (360448, 471040, 267776, 366784, 19416, 349523)
OUTPUT = (365367, 477468, 271431, 371790, 19683, 354294)
S = (11, 115, 523, 5731, 2427, 349523)

REFUND_Q0 = (
    16034515502580063307301771541219136736699152614293326570421852507777970140
)
REFUND_TYPES = (0, 5, 3, 0, 3, 5, 0, 5, 2, 4, 3, 2, 5, 4, 0, 5)
REFUND_DIGITS = (
    438236,
    105059,
    71880,
    265736,
    387279,
    114075,
    148402,
    297241,
    57544,
    330113,
    431826,
    40476,
    37172,
)


def v2(value: int) -> int:
    if value == 0:
        raise ValueError("v2(0)")
    return (value & -value).bit_length() - 1


def v3(value: int) -> int:
    result = 0
    while value % 3 == 0:
        value //= 3
        result += 1
    return result


def hash_int(digest: "hashlib._Hash", value: int) -> None:
    sign = 1 if value < 0 else 0
    raw_value = abs(value)
    raw = raw_value.to_bytes(max(1, (raw_value.bit_length() + 7) // 8), "big")
    digest.update(bytes((sign,)))
    digest.update(len(raw).to_bytes(4, "big"))
    digest.update(raw)


def cells(previous_type: int, current_type: int, section: int) -> tuple[int, list[int]]:
    binary_modulus = 1 << (4 + 3 * current_type)
    modulus = (21 // section) * binary_modulus
    base = (
        S[current_type]
        * pow(
            (pow(3, 2 * previous_type + 1, binary_modulus) * section)
            % binary_modulus,
            -1,
            binary_modulus,
        )
    ) % binary_modulus

    result: list[int] = []
    for lift in range(21 // section):
        value = base + binary_modulus * lift
        if math.gcd(value, 6) != 1:
            continue
        if section == 1 and value % 7 == 0:
            continue
        result.append(value)
    return modulus, result


def payload_digest(payload: dict[str, Any]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def build_payload() -> dict[str, Any]:
    constants = tuple(M * OUTPUT[i] - N * DOMAIN[i] for i in range(6))
    assert tuple(v2(DOMAIN[i]) for i in range(6)) == tuple(15 - 3 * i for i in range(6))
    assert tuple(v3(OUTPUT[i]) for i in range(6)) == tuple(2 * i + 1 for i in range(6))
    assert constants == tuple(21 * (1 << (15 - 3 * i)) * 3 ** (2 * i) for i in range(6))

    state_count = 0
    transition_count = 0
    rho_zero_count = 0
    sigma_zero_count = 0
    section_state_counts = {"1": 0, "7": 0}
    minimum_rho = M
    maximum_rho = 0
    minimum_sigma = 10**100
    maximum_sigma = -(10**100)
    minimum_k = {1: 10**100, 7: 10**100}
    maximum_k = {1: -(10**100), 7: -(10**100)}
    growth_threshold = {1: 0, 7: 0}
    transition_digest = hashlib.sha256()

    for section in (1, 7):
        additive_toll = 7 if section == 1 else 1
        for previous_type in range(6):
            for current_type in range(6):
                current_modulus, current_cells = cells(
                    previous_type, current_type, section
                )
                state_count += len(current_cells)
                section_state_counts[str(section)] += len(current_cells)

                for current_cell_index, current_cell in enumerate(current_cells):
                    for next_type in range(6):
                        next_modulus, next_cells = cells(
                            current_type, next_type, section
                        )
                        odd_exponent = 12 + 2 * (previous_type - current_type)
                        binary_exponent = 19 + 3 * (current_type - next_type)
                        matches: list[tuple[int, int, int, int, int]] = []

                        for next_cell_index, next_cell in enumerate(next_cells):
                            numerator = (
                                3**odd_exponent * current_cell
                                + additive_toll
                                - (1 << binary_exponent) * next_cell
                            )
                            if numerator % current_modulus:
                                continue

                            kappa = numerator // current_modulus
                            rho = (
                                -kappa * pow(3**odd_exponent, -1, M)
                            ) % M
                            sigma = (3**odd_exponent * rho + kappa) // M

                            core = current_cell + current_modulus * rho
                            next_core_numerator = 3**odd_exponent * core + additive_toll
                            assert next_core_numerator % (1 << binary_exponent) == 0
                            next_core = next_core_numerator >> binary_exponent
                            assert next_core == next_cell + next_modulus * sigma

                            matches.append(
                                (next_cell_index, next_cell, kappa, rho, sigma)
                            )

                        assert len(matches) == 1
                        next_cell_index, next_cell, kappa, rho, sigma = matches[0]
                        transition_count += 1
                        rho_zero_count += int(rho == 0)
                        sigma_zero_count += int(sigma == 0)
                        minimum_rho = min(minimum_rho, rho)
                        maximum_rho = max(maximum_rho, rho)
                        minimum_sigma = min(minimum_sigma, sigma)
                        maximum_sigma = max(maximum_sigma, sigma)

                        fixed_slope_constant = 3 ** (2 * current_type) * kappa
                        minimum_k[section] = min(
                            minimum_k[section], fixed_slope_constant
                        )
                        maximum_k[section] = max(
                            maximum_k[section], fixed_slope_constant
                        )
                        if fixed_slope_constant < 0:
                            threshold = (-fixed_slope_constant) // DELTA + 1
                            growth_threshold[section] = max(
                                growth_threshold[section], threshold
                            )

                        for value in (
                            section,
                            previous_type,
                            current_type,
                            current_cell_index,
                            next_type,
                            next_cell_index,
                            current_cell,
                            next_cell,
                            current_modulus,
                            next_modulus,
                            odd_exponent,
                            binary_exponent,
                            kappa,
                            rho,
                            sigma,
                            fixed_slope_constant,
                        ):
                            hash_int(transition_digest, value)

    assert state_count == 504
    assert section_state_counts == {"1": 432, "7": 72}
    assert transition_count == 3024
    assert rho_zero_count == 0
    assert sigma_zero_count == 11
    assert growth_threshold == {1: 4_271_324, 7: 3_212_050}

    inverse_delta = pow(DELTA, -1, M)
    coarse_digest = hashlib.sha256()
    coarse_growth: list[int] = []
    for source in range(6):
        for target in range(6):
            rho = ((DOMAIN[target] - OUTPUT[source]) * inverse_delta) % M
            sigma = (N * rho + OUTPUT[source] - DOMAIN[target]) // M
            assert sigma > rho
            coarse_growth.append(sigma - rho)
            for value in (source, target, rho, sigma, sigma - rho):
                hash_int(coarse_digest, value)

    quotient = REFUND_Q0
    for source, target in zip(REFUND_TYPES[:-1], REFUND_TYPES[1:]):
        remainder = (DELTA * quotient + OUTPUT[source]) % M
        assert remainder == DOMAIN[target]
        quotient = (N * quotient + OUTPUT[source] - DOMAIN[target]) // M

    exit_remainder = (DELTA * quotient + OUTPUT[REFUND_TYPES[-1]]) % M
    assert exit_remainder not in DOMAIN

    digits: list[int] = []
    temporary = REFUND_Q0
    while temporary:
        digits.append(temporary % M)
        temporary //= M
    assert tuple(digits) == REFUND_DIGITS

    payload: dict[str, Any] = {
        "schema_version": 1,
        "experiment_id": "X-8405",
        "status": "EMPIRICAL / EXACT FINITE INTERFACE AUDIT",
        "chart": {"M": M, "N": N, "N_minus_M": DELTA},
        "intrinsic_states": state_count,
        "section_state_counts": section_state_counts,
        "top_transitions": transition_count,
        "rho_zero_count": rho_zero_count,
        "sigma_zero_count": sigma_zero_count,
        "rho_range": [minimum_rho, maximum_rho],
        "sigma_range": [minimum_sigma, maximum_sigma],
        "fixed_slope_K_range": {
            "g=1": [minimum_k[1], maximum_k[1]],
            "g=7": [minimum_k[7], maximum_k[7]],
        },
        "uniform_scaled_growth_threshold": {
            "g=1": growth_threshold[1],
            "g=7": growth_threshold[7],
        },
        "transition_digest": transition_digest.hexdigest(),
        "coarse_ordered_pairs": 36,
        "coarse_min_growth": min(coarse_growth),
        "coarse_max_growth": max(coarse_growth),
        "coarse_digest": coarse_digest.hexdigest(),
        "refund_prefix": {
            "initial_quotient": REFUND_Q0,
            "initial_base_M_digits": digits,
            "initial_digit_count": len(digits),
            "transitions": len(REFUND_TYPES) - 1,
            "types": list(REFUND_TYPES),
            "final_quotient": quotient,
            "exit_remainder": exit_remainder,
            "conclusion": "finite two-cell refund; exits after the frozen prefix",
        },
        "interpretation": {
            "proved_by_finite_replay": [
                "all intrinsic cells and all 3024 proposed target transitions",
                "unique next cell, exact kappa, rho, sigma, and ordinary lift identity",
                "nonzero input top block on every transition",
                "the exact fixed-slope growth thresholds",
                "the frozen 15-transition ordinary refund prefix",
            ],
            "not_proved": [
                "a forever-defined ordinary state",
                "the full existence lemma",
                "a divergent Collatz seed",
                "the Collatz conjecture or its negation",
            ],
        },
    }
    payload["payload_sha256"] = payload_digest(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    print(json.dumps(payload, sort_keys=True, indent=2))
    if args.check_results:
        frozen = json.loads(args.check_results.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("frozen result mismatch")
        print("frozen result check passed")


if __name__ == "__main__":
    main()
