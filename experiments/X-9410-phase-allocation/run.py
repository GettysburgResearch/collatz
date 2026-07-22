#!/usr/bin/env python3
"""X-9410: exact finite checks for T-9416 phase-allocation optimality."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterator


def weak_compositions(total: int, parts: int) -> Iterator[tuple[int, ...]]:
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, parts - 1):
            yield (first,) + tail


def shape_ratio(allocation: tuple[int, ...]) -> Fraction:
    """Exact min-phase/height shape from T-9416.

    If D=sum n_j and m=min n_j, the minimizing phase has
      2 D^2 e_min = D^2+2mD+(1-r)m^2,
    while
      2 D^2 h = D^2+sum n_j^2.
    """
    total = sum(allocation)
    period = len(allocation)
    minimum = min(allocation)
    numerator = total * total + 2 * minimum * total + (1 - period) * minimum * minimum
    denominator = total * total + sum(value * value for value in allocation)
    return Fraction(numerator, denominator)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def generate() -> dict[str, object]:
    payload: dict[str, object] = {
        "schema_version": 1,
        "experiment_id": "X-9410",
        "research_question": (
            "Can unequal phasewise Gaussian-binomial root allocations improve "
            "the asymptotic raw Pade exponent beyond equal allocation?"
        ),
        "ranges": {
            "period_lengths": [2, 3, 4, 5, 6, 7],
            "total_root_counts": [1, 18],
        },
        "records": {},
    }

    total_checked = 0
    records: dict[str, object] = {}

    for period in range(2, 8):
        bound = Fraction(period * period + period + 1, period * (period + 1))
        period_checked = 0
        selected: dict[str, object] = {}
        selected_totals = {period, period + 1, 2 * period, 2 * period + 1, 18}

        for total in range(1, 19):
            best = Fraction(-1)
            maximizers: list[tuple[int, ...]] = []
            count = 0

            for allocation in weak_compositions(total, period):
                count += 1
                ratio = shape_ratio(allocation)
                assert ratio <= bound
                if ratio > best:
                    best = ratio
                    maximizers = [allocation]
                elif ratio == best:
                    maximizers.append(allocation)

            period_checked += count
            total_checked += count
            assert all(max(item) - min(item) <= 1 for item in maximizers)

            if total in selected_totals:
                selected[str(total)] = {
                    "weak_compositions": count,
                    "best_shape_ratio": fraction_text(best),
                    "best_shape_decimal": f"{float(best):.15f}",
                    "representative_maximizer": list(maximizers[0]),
                    "maximizer_count": len(maximizers),
                    "attains_continuous_bound": best == bound,
                }

        records[str(period)] = {
            "weak_compositions_checked": period_checked,
            "equal_allocation_shape_bound": fraction_text(bound),
            "equal_allocation_shape_decimal": f"{float(bound):.15f}",
            "all_ratios_within_bound": True,
            "all_finite_maximizers_balanced": True,
            "selected_totals": selected,
        }

    payload["records"] = records
    payload["summary"] = {
        "weak_compositions_checked": total_checked,
        "all_ratios_within_equal_allocation_bound": True,
        "all_finite_maximizers_balanced": True,
        "interpretation": (
            "Finite exact checks validate the phase-functional optimization "
            "interface; T-9416 proves the universal inequality."
        ),
    }
    return payload


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
