#!/usr/bin/env python3
"""X-9301: exact modular probe for logarithmic cusp scattering."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


DEFAULT_DEPTHS = (8, 12, 16, 20, 24, 32, 40, 48, 56, 64, 72, 80)
DEFAULT_THRESHOLDS = (
    Fraction(1, 146),
    Fraction(1, 64),
    Fraction(1, 32),
    Fraction(1, 16),
    Fraction(1, 8),
)


@dataclass(frozen=True)
class ThresholdMinimum:
    threshold: Fraction
    minimum: int
    first_argmin: int


def parse_depths(text: str) -> tuple[int, ...]:
    values = tuple(int(part.strip()) for part in text.split(",") if part.strip())
    if not values or any(value < 1 for value in values):
        raise argparse.ArgumentTypeError("depths must be positive comma-separated integers")
    return values


def parse_thresholds(text: str) -> tuple[Fraction, ...]:
    try:
        values = tuple(Fraction(part.strip()) for part in text.split(",") if part.strip())
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError(f"invalid threshold: {exc}") from exc
    if not values or any(value <= 0 or value >= Fraction(1, 2) for value in values):
        raise argparse.ArgumentTypeError("thresholds must lie strictly between 0 and 1/2")
    return values


def level_data(depth: int) -> tuple[tuple[int, int], ...]:
    data: list[tuple[int, int]] = []
    for t in range(depth):
        modulus = 64 ** (depth - t)
        inverse = pow(81, -(t + 1), modulus)
        coefficient = (17 * inverse) % modulus
        data.append((modulus, coefficient))
    return tuple(data)


def scattered_counts(
    theta: int,
    data: Iterable[tuple[int, int]],
    thresholds: tuple[Fraction, ...],
) -> list[int]:
    counts = [0] * len(thresholds)
    for modulus, coefficient in data:
        residue = (theta * coefficient) % modulus
        if residue > modulus // 2:
            residue -= modulus
        absolute = abs(residue)
        for index, threshold in enumerate(thresholds):
            if absolute * threshold.denominator >= threshold.numerator * modulus:
                counts[index] += 1
    return counts


def scan_depth(
    depth: int,
    theta_exponent: int,
    thresholds: tuple[Fraction, ...],
) -> dict[str, object]:
    theta_max = depth ** theta_exponent
    data = level_data(depth)
    minima = [depth + 1] * len(thresholds)
    first_argmins = [0] * len(thresholds)

    for theta in range(1, theta_max + 1):
        counts = scattered_counts(theta, data, thresholds)
        for index, count in enumerate(counts):
            if count < minima[index]:
                minima[index] = count
                first_argmins[index] = theta

    records = [
        ThresholdMinimum(threshold, minimum, argmin)
        for threshold, minimum, argmin in zip(thresholds, minima, first_argmins)
    ]
    return {
        "depth": depth,
        "theta_max": theta_max,
        "minima": [
            {
                "threshold": f"{record.threshold.numerator}/{record.threshold.denominator}",
                "min_scattered": record.minimum,
                "first_argmin": record.first_argmin,
            }
            for record in records
        ],
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
        "--theta-exponent",
        type=int,
        default=2,
        help="scan 1 <= theta <= K**exponent",
    )
    parser.add_argument(
        "--thresholds",
        type=parse_thresholds,
        default=DEFAULT_THRESHOLDS,
        help="comma-separated rational thresholds",
    )
    args = parser.parse_args()

    if args.theta_exponent < 1:
        parser.error("--theta-exponent must be positive")

    results = [
        scan_depth(depth, args.theta_exponent, args.thresholds)
        for depth in args.depths
    ]
    digest_payload = json.dumps(results, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(digest_payload).hexdigest()

    print("X-9301 exact cusp-scattering probe")
    print(f"python={platform.python_version()}")
    print("arithmetic=exact modular integers; no floating-point Fourier values")
    print(f"theta_bound=K^{args.theta_exponent}")
    print(
        "thresholds="
        + ",".join(f"{value.numerator}/{value.denominator}" for value in args.thresholds)
    )
    for result in results:
        fields = [
            f"K={result['depth']}",
            f"theta_max={result['theta_max']}",
        ]
        for item in result["minima"]:
            fields.append(
                "delta={threshold}:min={min_scattered}:argmin={first_argmin}".format(**item)
            )
        print(" ".join(fields))
    print(f"results_sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
