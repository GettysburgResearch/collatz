#!/usr/bin/env python3
"""X-9408: exact finite checks for block Gaussian-binomial Padé systems.

The universal statements live in L-9410, T-9414, and T-9415. This program uses
only exact standard-library arithmetic. It verifies a frozen set of period-two
and period-three examples and records reduced rational height by bit length.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

T = Fraction(64, 81)


def v2_int(value: int) -> int:
    if value == 0:
        raise ValueError("v2(0) is undefined")
    value = abs(value)
    return (value & -value).bit_length() - 1


def v2_fraction(value: Fraction) -> int:
    return v2_int(value.numerator) - v2_int(value.denominator)


def gaussian_row(n: int, q: Fraction) -> list[Fraction]:
    """Return ([n choose k]_q)_(0<=k<=n) by the polynomial recurrence."""

    row = [Fraction(1)]
    for a in range(1, n + 1):
        nxt = [Fraction(1)] + [Fraction(0)] * (a - 1) + [Fraction(1)]
        for k in range(1, a):
            nxt[k] = row[k] + q ** (a - k) * row[k - 1]
        row = nxt
    return row


def transfer_data(word: tuple[int, ...], m: int) -> dict[str, Any]:
    r = len(word)
    total = sum(word)
    cumulative = 0
    cumulative_sum = 0
    phase_exponents = [0]

    for index, digit in enumerate(word, start=1):
        cumulative += digit
        cumulative_sum += cumulative
        if index < r:
            phase_exponents.append(index + 9 * cumulative_sum + 9 * m * index)

    e = r + 9 * cumulative_sum
    lam = T ** (9 * total)
    return {
        "r": r,
        "S": total,
        "e": e,
        "lambda": lam,
        "R": lam**r,
        "Z": T ** (e + 9 * m * r),
        "phase_values": [T**exponent for exponent in phase_exponents],
    }


def verify_case(word: tuple[int, ...], n: int, m: int = 1) -> dict[str, Any]:
    data = transfer_data(word, m)
    r = data["r"]
    total = data["S"]
    e = data["e"]
    lam = data["lambda"]
    R = data["R"]
    Z = data["Z"]
    phase_values = data["phase_values"]

    degree = r * n
    gaussian = gaussian_row(degree, lam)
    denominator_coefficients: list[Fraction] = []

    for k in range(degree + 1):
        numerator = (1 - r) * k * k + (2 * r * r * n - r - 1) * k
        assert numerator % 2 == 0
        beta = numerator // 2
        assert beta >= 0
        denominator_coefficients.append(
            (-1) ** k * Z**k * lam**beta * gaussian[k]
        )

    denominator = sum(denominator_coefficients, Fraction(0))
    assert v2_fraction(denominator) == 0

    first_error_block = degree + n
    maximum_block = first_error_block + 2
    phase_convolutions: list[list[Fraction]] = []

    for j in range(r):
        shifted_argument = Z * lam**j
        coefficients = [
            phase_values[j]
            * R ** (block * (block - 1) // 2)
            * shifted_argument**block
            for block in range(maximum_block + 1)
        ]

        convolution: list[Fraction] = []
        for block in range(maximum_block + 1):
            convolution.append(
                sum(
                    (
                        denominator_coefficients[k] * coefficients[block - k]
                        for k in range(min(degree, block) + 1)
                    ),
                    Fraction(0),
                )
            )
        phase_convolutions.append(convolution)

    # Every phase separately has n exact cancelled block coefficients.
    for block in range(degree, degree + n):
        assert all(
            phase_convolutions[j][block] == 0 for j in range(r)
        )

    numerator = sum(
        (
            phase_convolutions[j][block]
            for j in range(r)
            for block in range(degree)
        ),
        Fraction(0),
    )

    approximant = numerator / denominator

    first_errors = [
        sum(phase_convolutions[j][block] for j in range(r))
        for block in range(first_error_block, maximum_block + 1)
    ]
    valuations = [v2_fraction(value) for value in first_errors]
    assert valuations[0] < min(valuations[1:])

    l_numerator = n * (
        n * r**3 + n * r**2 + n * r - r**2 - 2 * r
    )
    assert l_numerator % 2 == 0
    first_lambda_exponent = l_numerator // 2
    expected_error = 6 * (
        9 * total * first_lambda_exponent
        + first_error_block * (e + 9 * m * r)
    )
    assert valuations[0] == expected_error

    height = max(abs(approximant.numerator), abs(approximant.denominator))
    height_bits = height.bit_length()
    ratio = Fraction(expected_error, height_bits)

    return {
        "word": list(word),
        "period_length": r,
        "pade_order": n,
        "error_v2": expected_error,
        "reduced_height_bits": height_bits,
        "bitlength_exponent_fraction": f"{ratio.numerator}/{ratio.denominator}",
        "bitlength_exponent_decimal": f"{expected_error / height_bits:.12f}",
    }


def generate() -> dict[str, Any]:
    cases = [
        ((17, 18), 1),
        ((17, 18), 2),
        ((17, 18), 3),
        ((17, 17, 18), 1),
        ((17, 17, 18), 2),
    ]

    return {
        "schema_version": 1,
        "experiment_id": "X-9408",
        "research_question": (
            "Do block Gaussian-binomial common denominators cross the "
            "rationality threshold for periodic stack words of period two "
            "and three?"
        ),
        "theoretical_limiting_exponents": {
            "1": "1.419591945535779",
            "2": "1.104127068750050",
            "3": "1.025260849553618",
            "4": "0.993714361875045",
            "5": "0.977941118035759",
            "6": "0.968927835841881",
        },
        "threshold_classification": {
            "certified_above_one_period_lengths": [1, 2, 3],
            "universal_bound_below_one_from_period_length": 4,
        },
        "exact_records": [verify_case(word, n) for word, n in cases],
        "interpretation": {
            "proved_by_finite_computation": [
                "frozen common-denominator cancellations",
                "frozen first-error valuation identities",
                "frozen denominator-unit checks",
                "frozen reduced rational heights",
            ],
            "not_proved_by_finite_computation": [
                "universal block Pade theorem",
                "irrationality for all period-two or period-three words",
                "irrationality or rationality for period length at least four",
                "balanced nonperiodic stack frontier",
                "Collatz conjecture",
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

    if args.check_results:
        expected = args.check_results.read_bytes()
        if expected != data:
            raise SystemExit("canonical result mismatch")

    print(data.decode("utf-8"), end="")
    print(f"SHA256 {digest}")


if __name__ == "__main__":
    main()
