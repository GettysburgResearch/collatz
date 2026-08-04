#!/usr/bin/env python3
"""X-9302: exact adversarial audit of completion-height phase carries."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from fractions import Fraction
from typing import Iterable


DEFAULT_DEPTHS = (8, 12, 16, 20, 24, 32, 40, 48, 56, 64, 72, 80)


def parse_depths(text: str) -> tuple[int, ...]:
    values = tuple(int(part.strip()) for part in text.split(",") if part.strip())
    if not values or any(value < 2 for value in values):
        raise argparse.ArgumentTypeError(
            "depths must be comma-separated integers at least 2"
        )
    return values


def signed_residue(value: int, modulus: int) -> int:
    """Return the representative in (-modulus/2, modulus/2]."""
    residue = value % modulus
    if 2 * residue > modulus:
        residue -= modulus
    return residue


def phase_data(depth: int, numerator: int) -> tuple[list[int], list[int], Fraction]:
    signed: list[int] = []
    energy = Fraction(0, 1)

    for ell in range(depth):
        modulus = 81 ** (ell + 1)
        inverse = pow(64, -(depth - ell), modulus)
        value = signed_residue(-17 * numerator * inverse, modulus)
        signed.append(value)
        energy += Fraction(value * value, modulus * modulus)

    carries: list[int] = []
    for ell in range(depth - 1):
        denominator = 81 ** (ell + 1)
        carry_numerator = 64 * signed[ell] - signed[ell + 1]
        if carry_numerator % denominator:
            raise AssertionError(
                f"nonintegral carry at K={depth}, h={numerator}, ell={ell}"
            )
        carries.append(carry_numerator // denominator)

    return signed, carries, energy


def zero_runs(carries: Iterable[int]) -> list[tuple[int, int]]:
    values = list(carries)
    runs: list[tuple[int, int]] = []
    index = 0

    while index < len(values):
        if values[index] != 0:
            index += 1
            continue
        end = index
        while end < len(values) and values[end] == 0:
            end += 1
        runs.append((index, end - index))
        index = end

    return runs


def audit_numerator(depth: int, numerator: int) -> tuple[int, tuple[int, int, int]]:
    if numerator <= 0 or numerator % 64 == 0:
        raise ValueError("the audit expects a positive primitive numerator")

    signed, carries, energy = phase_data(depth, numerator)
    nonzero_carries = sum(carry != 0 for carry in carries)

    if 21314 * energy < nonzero_carries:
        raise AssertionError(
            f"carry-energy failure at K={depth}, h={numerator}"
        )

    longest = (0, 0, 0)
    for start, run_length in zero_runs(carries):
        terminal_length = depth - start - run_length
        if terminal_length < 1:
            raise AssertionError("invalid terminal-length convention")

        ordinary_numerator = (
            64 ** (depth - start) * signed[start] + 17 * numerator
        )
        modulus = 81 ** (start + run_length + 1)

        if ordinary_numerator == 0:
            raise AssertionError(
                f"zero height numerator at K={depth}, h={numerator}, start={start}"
            )
        if ordinary_numerator % modulus:
            raise AssertionError(
                f"zero-run divisibility failure at K={depth}, h={numerator}, "
                f"start={start}, length={run_length}"
            )

        # Exact integer form of 81^r <= 64^(r+t)/2 + 17h.
        if 2 * 81 ** run_length > (
            64 ** (run_length + terminal_length) + 34 * numerator
        ):
            raise AssertionError(
                f"height-squeeze failure at K={depth}, h={numerator}, "
                f"start={start}, length={run_length}"
            )

        # Exact branch used to derive r < kappa*t.
        if 81 ** run_length > 34 * numerator:
            if 81 ** run_length >= 64 ** (run_length + terminal_length):
                raise AssertionError(
                    f"criticality failure at K={depth}, h={numerator}, "
                    f"start={start}, length={run_length}"
                )

        if run_length > longest[0]:
            longest = (run_length, numerator, start)

    return nonzero_carries, longest


def scan_depth(depth: int, numerator_exponent: int) -> dict[str, int]:
    numerator_max = depth ** numerator_exponent
    minimum_nonzero = depth
    first_argmin = 0
    longest = (0, 0, 0)
    checked = 0

    for numerator in range(1, numerator_max + 1):
        if numerator % 64 == 0:
            continue
        nonzero_carries, local_longest = audit_numerator(depth, numerator)
        checked += 1

        if nonzero_carries < minimum_nonzero:
            minimum_nonzero = nonzero_carries
            first_argmin = numerator
        if local_longest[0] > longest[0]:
            longest = local_longest

    return {
        "K": depth,
        "primitive_h_max": numerator_max,
        "primitive_h_checked": checked,
        "min_nonzero_carries": minimum_nonzero,
        "first_argmin": first_argmin,
        "max_zero_run": longest[0],
        "max_zero_run_h": longest[1],
        "max_zero_run_start": longest[2],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--depths",
        type=parse_depths,
        default=DEFAULT_DEPTHS,
        help="comma-separated depths",
    )
    parser.add_argument(
        "--numerator-exponent",
        type=int,
        default=2,
        help="audit primitive 1 <= h <= K**exponent",
    )
    args = parser.parse_args()

    if args.numerator_exponent < 1:
        parser.error("--numerator-exponent must be positive")

    results = [
        scan_depth(depth, args.numerator_exponent)
        for depth in args.depths
    ]
    payload = json.dumps(results, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(payload).hexdigest()

    print("X-9302 completion-height carry audit")
    print(f"python={platform.python_version()}")
    print("arithmetic=exact modular integers and fractions")
    print("primitive_condition=64 does not divide h")
    print(
        "checks=carry integrality; carry-energy inequality; "
        "zero-run nonzero numerator; divisibility; exact height squeeze"
    )
    print(f"bound=h<=K^{args.numerator_exponent}")

    for result in results:
        print(
            "K={K} h_max={primitive_h_max} checked={primitive_h_checked} "
            "min_nonzero={min_nonzero_carries} argmin={first_argmin} "
            "max_zero_run={max_zero_run} zero_h={max_zero_run_h} "
            "zero_start={max_zero_run_start}".format(**result)
        )

    print(f"results_sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
