#!/usr/bin/env python3
"""X-9409: exact reduced-height census for primitive period-four words.

The program evaluates the L-9410 approximants through Padé order three for the
three primitive cyclic binary length-four classes over {17,18}. It uses sparse
integer polynomials in T=64/81, avoiding repeated Fraction normalization.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from math import gcd
from pathlib import Path
from typing import Any


def add_shifted(
    left: dict[int, int], right: dict[int, int], shift: int
) -> dict[int, int]:
    out = dict(left)
    for exponent, coefficient in right.items():
        target = exponent + shift
        out[target] = out.get(target, 0) + coefficient
        if out[target] == 0:
            del out[target]
    return out


def gaussian_polynomials(degree: int) -> list[dict[int, int]]:
    """Return [degree choose k]_q as sparse integer polynomials in q."""

    row: list[dict[int, int]] = [{0: 1}]
    for a in range(1, degree + 1):
        nxt: list[dict[int, int]] = (
            [{0: 1}] + [{} for _ in range(a - 1)] + [{0: 1}]
        )
        for k in range(1, a):
            nxt[k] = add_shifted(row[k], row[k - 1], a - k)
        row = nxt
    return row


def transfer_data(word: tuple[int, ...], m: int = 1) -> dict[str, Any]:
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
    return {
        "r": r,
        "S": total,
        "e": e,
        "zeta": e + 9 * m * r,
        "phase_exponents": phase_exponents,
    }


def evaluate_cleared(poly: dict[int, int], height: int) -> int:
    """Evaluate sum c_e 64^e 81^(height-e) using adjacent sparse exponents."""

    exponents = sorted(poly)
    first = exponents[0]
    term = 64**first * 81 ** (height - first)
    total = poly[first] * term
    previous = first
    power_cache: dict[int, tuple[int, int]] = {}

    for exponent in exponents[1:]:
        gap = exponent - previous
        if gap not in power_cache:
            power_cache[gap] = (64**gap, 81**gap)
        power_64, power_81 = power_cache[gap]
        term = term // power_81 * power_64
        total += poly[exponent] * term
        previous = exponent

    return total


def verify_case(word: tuple[int, ...], n: int, m: int = 1) -> dict[str, Any]:
    data = transfer_data(word, m)
    r = data["r"]
    total = data["S"]
    e = data["e"]
    zeta = data["zeta"]
    phase_exponents = data["phase_exponents"]
    lambda_exponent = 9 * total
    degree = r * n

    gaussian = gaussian_polynomials(degree)
    denominator_poly: defaultdict[int, int] = defaultdict(int)
    numerator_poly: defaultdict[int, int] = defaultdict(int)

    for k in range(degree + 1):
        beta_numerator = (
            (1 - r) * k * k + (2 * r * r * n - r - 1) * k
        )
        assert beta_numerator % 2 == 0
        beta = beta_numerator // 2
        assert beta >= 0
        sign = -1 if k % 2 else 1
        for gaussian_degree, coefficient in gaussian[k].items():
            exponent = zeta * k + lambda_exponent * (beta + gaussian_degree)
            denominator_poly[exponent] += sign * coefficient

    for j in range(r):
        for block in range(degree):
            for k in range(block + 1):
                tail = block - k
                beta_numerator = (
                    (1 - r) * k * k
                    + (2 * r * r * n - r - 1) * k
                )
                assert beta_numerator % 2 == 0
                beta = beta_numerator // 2
                sign = -1 if k % 2 else 1
                for gaussian_degree, coefficient in gaussian[k].items():
                    exponent = (
                        phase_exponents[j]
                        + zeta * block
                        + lambda_exponent
                        * (
                            beta
                            + gaussian_degree
                            + r * tail * (tail - 1) // 2
                            + j * tail
                        )
                    )
                    numerator_poly[exponent] += sign * coefficient

    denominator = {
        exponent: coefficient
        for exponent, coefficient in denominator_poly.items()
        if coefficient
    }
    numerator = {
        exponent: coefficient
        for exponent, coefficient in numerator_poly.items()
        if coefficient
    }

    common_height = max(max(denominator), max(numerator))
    denominator_integer = evaluate_cleared(denominator, common_height)
    numerator_integer = evaluate_cleared(numerator, common_height)
    common_factor = gcd(abs(numerator_integer), abs(denominator_integer))
    reduced_numerator = numerator_integer // common_factor
    reduced_denominator = denominator_integer // common_factor
    reduced_height_bits = max(
        abs(reduced_numerator), abs(reduced_denominator)
    ).bit_length()

    first_block = (r + 1) * n
    l_numerator = n * (
        n * r**3 + n * r**2 + n * r - r**2 - 2 * r
    )
    assert l_numerator % 2 == 0
    error_v2 = 6 * (
        9 * total * (l_numerator // 2) + first_block * zeta
    )
    ratio = Fraction(error_v2, reduced_height_bits)

    return {
        "word": list(word),
        "pade_order": n,
        "gcd_bits": common_factor.bit_length(),
        "reduced_height_bits": reduced_height_bits,
        "error_v2": error_v2,
        "bitlength_exponent_fraction": f"{ratio.numerator}/{ratio.denominator}",
        "bitlength_exponent_decimal": f"{error_v2 / reduced_height_bits:.12f}",
    }


def generate() -> dict[str, Any]:
    representatives = [
        (17, 17, 17, 18),
        (17, 17, 18, 18),
        (17, 18, 18, 18),
    ]

    records = [
        verify_case(word, order)
        for word in representatives
        for order in (1, 2, 3)
    ]

    return {
        "schema_version": 1,
        "experiment_id": "X-9409",
        "research_question": (
            "Do primitive period-four stack words show enough exact "
            "common-factor or reduced-height saving to rescue the L-9410 "
            "Pade family at small orders?"
        ),
        "primitive_cyclic_representatives": [list(word) for word in representatives],
        "universal_limiting_exponent": "0.993714361875045",
        "required_logarithmic_saving_fraction": "0.006285638124955",
        "exact_records": records,
        "interpretation": {
            "proved_by_finite_computation": [
                "frozen sparse-polynomial common denominators",
                "frozen exact cleared gcd bit lengths",
                "frozen reduced rational heights",
                "frozen first-error valuations",
            ],
            "not_proved_by_finite_computation": [
                "absence of an asymptotic period-four gcd saving",
                "irrationality or rationality of a period-four value",
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
