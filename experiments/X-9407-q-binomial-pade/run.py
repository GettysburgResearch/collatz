#!/usr/bin/env python3
"""X-9407: exact checks for L-9409 and T-9412."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


def v2(n: int) -> int:
    if n == 0:
        raise ValueError("v2(0) is undefined")
    n = abs(n)
    return (n & -n).bit_length() - 1


def gaussian_q(n: int, k: int, q: Fraction) -> Fraction:
    if k < 0 or k > n:
        return Fraction(0)
    value = Fraction(1)
    for i in range(1, k + 1):
        value *= (1 - q ** (n - k + i)) / (1 - q**i)
    return value


def pade_record(d: int, m: int, n: int) -> dict[str, Any]:
    T = Fraction(64, 81)
    rho = T ** (9 * d)
    X = T ** (9 * m + 1)

    coefficients = [
        (-1) ** k * rho ** (n * k) * gaussian_q(n, k, rho)
        for k in range(n + 1)
    ]

    def u(index: int) -> Fraction:
        return rho ** (index * (index + 1) // 2)

    convolution: list[Fraction] = []
    for N in range(2 * n + 5):
        value = sum(
            (
                coefficients[k] * u(N - k)
                for k in range(min(n, N) + 1)
            ),
            Fraction(0),
        )
        convolution.append(value)

    assert all(value == 0 for value in convolution[n : 2 * n])

    expected_first = u(2 * n)
    for r in range(1, n + 1):
        expected_first *= 1 - rho ** (-r)
    assert convolution[2 * n] == expected_first

    B = sum(
        (coefficient * X**k for k, coefficient in enumerate(coefficients)),
        Fraction(0),
    )
    assert B.denominator % 2 == 1
    assert v2(B.numerator) == 0

    A = sum(
        (convolution[N] * X**N for N in range(n)),
        Fraction(0),
    )

    exact_error_v2 = 27 * d * (3 * n * n + n) + 12 * n * (9 * m + 1)
    first_error = convolution[2 * n] * X ** (2 * n)
    assert v2(first_error.numerator) == exact_error_v2

    for N in range(2 * n + 1, 2 * n + 5):
        term = convolution[N] * X**N
        if term:
            assert v2(term.numerator) > exact_error_v2

    approximant = A / B
    height = max(abs(approximant.numerator), approximant.denominator)
    E_n = 9 * d * n * n + (9 * m + 1) * n
    tau = exact_error_v2 / math.log2(height)

    return {
        "order": n,
        "zero_coefficients": n,
        "error_v2": exact_error_v2,
        "height_bits": height.bit_length(),
        "tau": f"{tau:.12f}",
        "E_n": E_n,
        "B_unit": True,
    }


def generate() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "experiment_id": "X-9407",
        "research_question": (
            "Do the q-binomial Pade approximants cancel exactly and cross the "
            "rational-target exponent one in constant-increment stack models?"
        ),
        "parameters": {
            "T": "64/81",
            "m": 1,
            "increments": [17, 18],
            "orders": [1, 2, 3, 4, 5],
        },
        "asymptotic_exponent": f"{9 / math.log2(81):.15f}",
        "records": {
            str(d): [pade_record(d, 1, n) for n in range(1, 6)]
            for d in (17, 18)
        },
        "interpretation": {
            "proved_by_finite_computation": [
                "the frozen Gaussian-binomial coefficient cancellations",
                "the frozen first-error valuations and denominator-unit checks",
                "the frozen reduced rational heights and approximation exponents",
            ],
            "not_proved_by_finite_computation": [
                "the universal q-binomial Pade lemma",
                "the universal constant-increment irrationality theorem",
                "irrationality for the balanced nonperiodic 17/18 stack",
                "transcendence or a Collatz counterexample",
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
