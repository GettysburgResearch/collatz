#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any

Poly = dict[int, int]


def poly_add(left: Poly, right: Poly) -> Poly:
    out = dict(left)
    for exponent, coefficient in right.items():
        out[exponent] = out.get(exponent, 0) + coefficient
        if out[exponent] == 0:
            del out[exponent]
    return out


def poly_shift_scale(poly: Poly, shift: int, scale: int = 1) -> Poly:
    return {
        exponent + shift: scale * coefficient
        for exponent, coefficient in poly.items()
        if scale * coefficient
    }


def poly_multiply(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = left_exponent + right_exponent
            out[exponent] = (
                out.get(exponent, 0)
                + left_coefficient * right_coefficient
            )
    return {
        exponent: coefficient
        for exponent, coefficient in out.items()
        if coefficient
    }


@lru_cache(maxsize=None)
def gaussian_binomial_items(n: int, k: int) -> tuple[tuple[int, int], ...]:
    if k < 0 or k > n:
        return ()
    if k == 0 or k == n:
        return ((0, 1),)
    left = dict(gaussian_binomial_items(n - 1, k))
    right = poly_shift_scale(
        dict(gaussian_binomial_items(n - 1, k - 1)),
        n - k,
    )
    return tuple(sorted(poly_add(left, right).items()))


def gaussian_binomial(n: int, k: int) -> Poly:
    return dict(gaussian_binomial_items(n, k))


def beta(period: int, order: int, delay: int, k: int) -> int:
    numerator = (
        (1 - period) * k * k
        + (2 * period * delay - period - 1) * k
    )
    assert numerator % 2 == 0
    value = numerator // 2
    assert value >= 0
    return value


def normalized_convolution(
    period: int,
    order: int,
    delay: int,
    phase: int,
    block: int,
) -> Poly:
    degree = period * order
    total: Poly = {}
    for k in range(degree + 1):
        shift = (
            beta(period, order, delay, k)
            - period * block * k
            + period * k * (k + 1) // 2
            - phase * k
        )
        term = poly_shift_scale(
            gaussian_binomial(degree, k),
            shift,
            -1 if k % 2 else 1,
        )
        total = poly_add(total, term)
    return total


def root_product(
    period: int,
    order: int,
    delay: int,
    phase: int,
    block: int,
) -> Poly:
    degree = period * order
    product: Poly = {0: 1}
    for h in range(degree):
        exponent = h + period * delay - period * block - phase
        factor = poly_add({0: 1}, {exponent: -1})
        product = poly_multiply(product, factor)
    return product


def first_lambda_exponent(period: int, order: int, delay: int) -> int:
    degree = period * order
    first_block = delay + order
    numerator = (
        period * first_block * (first_block - 1)
        - degree * (degree + 1)
    )
    assert numerator % 2 == 0
    return numerator // 2


def height_lambda_exponent(
    period: int,
    order: int,
    delay: int,
) -> int:
    degree = period * order
    numerator = (
        degree * degree
        + degree
        + period * delay * delay
        - period * delay
        - 2 * delay
        + 2
    )
    assert numerator % 2 == 0
    return numerator // 2


def product_identity_audit() -> dict[str, Any]:
    identities = 0
    zero_windows = 0
    first_errors = 0
    selected: list[dict[str, Any]] = []

    for period in range(1, 5):
        for order in range(1, 4):
            degree = period * order
            for delay in range(degree + 1, degree + 4):
                for phase in range(period):
                    for block in range(
                        degree,
                        delay + order + 3,
                    ):
                        left = normalized_convolution(
                            period, order, delay, phase, block
                        )
                        right = root_product(
                            period, order, delay, phase, block
                        )
                        assert left == right
                        identities += 1

                    for offset in range(order):
                        block = delay + offset
                        value = root_product(
                            period, order, delay, phase, block
                        )
                        assert value == {}
                        zero_windows += 1

                first_block = delay + order
                expected = first_lambda_exponent(
                    period, order, delay
                )
                phase_minima: list[int] = []
                for phase in range(period):
                    product = root_product(
                        period, order, delay, phase, first_block
                    )
                    assert product
                    base = (
                        period * first_block * (first_block - 1) // 2
                        + phase * first_block
                    )
                    minimum = base + min(product)
                    phase_minima.append(minimum)
                assert phase_minima[0] == expected
                assert all(
                    phase_minima[phase] > expected
                    for phase in range(1, period)
                )
                first_errors += 1

                if (
                    period in (1, 4)
                    and order in (1, 3)
                    and delay == degree + 2
                ):
                    selected.append(
                        {
                            "period": period,
                            "order": order,
                            "delay": delay,
                            "degree": degree,
                            "first_block": first_block,
                            "first_lambda_exponent": expected,
                            "phase_minima": phase_minima,
                        }
                    )

    return {
        "laurent_product_identities": identities,
        "zero_window_checks": zero_windows,
        "first_error_checks": first_errors,
        "selected_records": selected,
    }


def height_audit() -> dict[str, Any]:
    denominator_terms = 0
    numerator_terms = 0
    selected: list[dict[str, Any]] = []

    for period in range(1, 5):
        for order in range(1, 4):
            degree = period * order
            for delay in range(degree + 1, degree + 4):
                bound = height_lambda_exponent(
                    period, order, delay
                )
                denominator_max = -1
                denominator_arg = None
                numerator_max = -1
                numerator_arg = None

                for k in range(degree + 1):
                    beta_value = beta(
                        period, order, delay, k
                    )
                    for gaussian_degree in gaussian_binomial(
                        degree, k
                    ):
                        denominator_value = (
                            beta_value + gaussian_degree
                        )
                        assert denominator_value <= bound
                        denominator_terms += 1
                        if denominator_value > denominator_max:
                            denominator_max = denominator_value
                            denominator_arg = [k, gaussian_degree]

                        for phase in range(period):
                            for series_index in range(delay - k):
                                block = k + series_index
                                assert block < delay
                                numerator_value = (
                                    beta_value
                                    + gaussian_degree
                                    + period
                                    * series_index
                                    * (series_index - 1)
                                    // 2
                                    + phase * series_index
                                )
                                assert numerator_value <= bound
                                numerator_terms += 1
                                if numerator_value > numerator_max:
                                    numerator_max = numerator_value
                                    numerator_arg = [
                                        k,
                                        gaussian_degree,
                                        phase,
                                        series_index,
                                    ]

                assert numerator_max == bound
                if period in (1, 4) and order in (1, 3):
                    selected.append(
                        {
                            "period": period,
                            "order": order,
                            "delay": delay,
                            "height_lambda_bound": bound,
                            "denominator_max": denominator_max,
                            "denominator_arg": denominator_arg,
                            "numerator_max": numerator_max,
                            "numerator_arg": numerator_arg,
                        }
                    )

    return {
        "denominator_monomials_checked": denominator_terms,
        "numerator_monomials_checked": numerator_terms,
        "selected_records": selected,
    }


def decimal_text(value: Decimal, places: int = 18) -> str:
    quantum = Decimal(1).scaleb(-places)
    return format(value.quantize(quantum), "f")


def optimized_delay_records() -> dict[str, Any]:
    getcontext().prec = 80
    log_ratio = Decimal(64).ln() / Decimal(81).ln()
    rows: dict[str, Any] = {}

    for period in range(1, 16):
        r = Decimal(period)
        alpha = (
            Decimal(2 * period - 1)
            + Decimal(4 * period * period + 1).sqrt()
        ) / Decimal(2)
        shape = (
            (alpha + 1) * (alpha + 1) - r
        ) / (alpha * alpha + r)
        exponent = log_ratio * shape
        rows[str(period)] = {
            "optimal_delay_ratio": decimal_text(alpha),
            "optimal_shape": decimal_text(shape),
            "optimized_exponent": decimal_text(exponent),
            "above_one": exponent > 1,
        }

    return {
        "formula": (
            "log_81(64)*[((alpha+1)^2-r)/(alpha^2+r)]"
        ),
        "optimizer": "(2*r-1+sqrt(4*r^2+1))/2",
        "rows": rows,
        "last_period_above_one": max(
            int(period)
            for period, row in rows.items()
            if row["above_one"]
        ),
    }


def exact_threshold_certificates() -> dict[str, Any]:
    alpha = Fraction(37, 2)
    period_shapes: dict[str, str] = {}
    for period in range(1, 10):
        shape = (
            (alpha + 1) * (alpha + 1) - period
        ) / (alpha * alpha + period)
        period_shapes[str(period)] = (
            f"{shape.numerator}/{shape.denominator}"
        )
        assert shape >= Fraction(297, 281)

    native_nine_margin = 88 * 297 - 93 * 281
    assert 64**93 > 81**88
    assert native_nine_margin == 3

    discriminant = 500**2 - 4 * 13 * 4880
    assert discriminant == -3760
    assert 64**20 < 81**19
    period_ten_ceiling = Fraction(19, 20) * Fraction(
        263, 250
    )
    assert period_ten_ceiling == Fraction(4997, 5000)
    assert period_ten_ceiling < 1

    return {
        "uniform_period_1_to_9": {
            "delay_ratio": "37/2",
            "shape_at_period_9": "297/281",
            "period_shapes": period_shapes,
            "log_ratio_lower_certificate": "64^93 > 81^88",
            "integer_margin": native_nine_margin,
            "conclusion": (
                "log_81(64)*(297/281)>1"
            ),
        },
        "period_10_ceiling": {
            "shape_upper_bound": "263/250",
            "positive_quadratic": (
                "13*alpha^2-500*alpha+4880"
            ),
            "quadratic_discriminant": discriminant,
            "log_ratio_upper_certificate": "64^20 < 81^19",
            "final_upper_bound": (
                f"{period_ten_ceiling.numerator}/"
                f"{period_ten_ceiling.denominator}"
            ),
            "strictly_below_one": True,
        },
    }


def generate() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "experiment_id": "X-9413",
        "research_question": (
            "Does an independently delayed Gaussian-binomial "
            "block-Pade window produce a source-independent "
            "period-nine theorem, and where does that family stop?"
        ),
        "ranges": {
            "product_periods": [1, 4],
            "product_orders": [1, 3],
            "delay_offset_from_degree": [1, 3],
            "optimized_periods": [1, 15],
        },
        "product_identity": product_identity_audit(),
        "height": height_audit(),
        "optimized_delay": optimized_delay_records(),
        "exact_thresholds": exact_threshold_certificates(),
        "interpretation": {
            "proved_by_finite_computation": [
                "the frozen Laurent-polynomial identities",
                "the frozen cancellation windows",
                "the frozen first-error and monomial-height formulas",
                "the displayed exact period-nine and period-ten certificates",
            ],
            "not_proved_by_finite_computation": [
                "the universal delayed-window lemma",
                "the universal height estimate",
                "the source-independent period-nine irrationality theorem",
                "irrationality at period ten",
                "the balanced nonperiodic stack value",
                "the Collatz conjecture",
            ],
        },
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    data = canonical_bytes(generate())
    digest = hashlib.sha256(data).hexdigest()

    if args.write_results:
        args.write_results.parent.mkdir(
            parents=True, exist_ok=True
        )
        args.write_results.write_bytes(data)
    if (
        args.check_results
        and args.check_results.read_bytes() != data
    ):
        raise SystemExit("canonical result mismatch")

    print(data.decode("utf-8"), end="")
    print(f"SHA256 {digest}")


if __name__ == "__main__":
    main()
