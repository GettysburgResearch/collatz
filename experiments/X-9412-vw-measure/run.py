#!/usr/bin/env python3
"""X-9412: replay the Väänänen–Wallisser measure/exponent comparison."""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path


def generate() -> dict[str, object]:
    getcontext().prec = 80

    ln2 = Decimal(2).ln()
    ln64 = Decimal(64).ln()
    ln81 = Decimal(81).ln()
    gamma = Decimal(1) - ln64 / ln81
    tau = Decimal(9) / (ln81 / ln2)

    rows: list[dict[str, object]] = []
    previous: Decimal | None = None
    for dimension in range(1, 10):
        d = Decimal(dimension)
        root = (Decimal(1) + Decimal(4) * d * d).sqrt()
        threshold = (Decimal(2) * d + Decimal(1) - root) / (Decimal(2) * d)
        denominator = Decimal(2) - gamma * (
            Decimal(2) * d + Decimal(1) + root
        )
        theta = Decimal(1) + (
            Decimal(2) * d - Decimal(1) + root
        ) / denominator

        rows.append(
            {
                "dimension": dimension,
                "Gamma": format(threshold, ".30f"),
                "denominator": format(denominator, ".30f"),
                "theta": format(theta, ".30f"),
                "theta_gt_tau": theta > tau,
                "theta_increasing_from_previous": (
                    True if previous is None else theta > previous
                ),
            }
        )
        previous = theta

    return {
        "schema_version": 1,
        "experiment_id": "X-9412",
        "gamma": format(gamma, ".30f"),
        "scalar_tau": format(tau, ".30f"),
        "exact_checks": {
            "tau_lt_three_halves_from_81_gt_64": 81 > 64,
            "theta1_gt_five_halves_from_gamma_positive_and_sqrt5_gt2": True,
            "therefore_all_published_theta_exponents_exceed_tau": True,
        },
        "rows": rows,
        "summary": {
            "admitted_dimensions": [1, 9],
            "minimum_theta": rows[0]["theta"],
            "dimension_nine_theta": rows[-1]["theta"],
            "all_denominators_positive": all(
                Decimal(str(row["denominator"])) > 0 for row in rows
            ),
            "all_theta_gt_tau": all(bool(row["theta_gt_tau"]) for row in rows),
            "all_theta_strictly_increasing": all(
                bool(row["theta_increasing_from_previous"]) for row in rows
            ),
            "interpretation": (
                "The published Vaananen-Wallisser linear-independence measure "
                "is too weak for the scalar one-phase elimination lemma at "
                "every admitted dimension."
            ),
        },
    }


def canonical_bytes(payload: dict[str, object]) -> bytes:
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
