#!/usr/bin/env python3
"""X-8401: compressed critical-cycle and mechanical-block audit."""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from pathlib import Path
from typing import Callable

A = 4_992_586_555_009
K = 3_149_971_404_836
ONES = A - K
FACTORS = (7, 191, 281, 28_591, 136_398_329)
MODULUS = 1
for _p in FACTORS:
    MODULUS *= _p

MASK_FIRST_40 = 679_923_852_302
MASK_LAST_40 = 1_092_615_932_587
EXPECTED_SWAP_POSITIONS = (
    2, 4, 6, 23, 30, 35, 39, 42, 44, 47, 54, 59, 61, 64, 71,
    78, 80, 83, 85, 92, 95, 97, 102, 107, 112, 117, 121, 138,
    141, 143, 145, 148, 150, 158, 165, 167, 174, 177, 179,
    182, 184, 186, 189,
)
PREC = 120


@dataclass(frozen=True)
class Summary:
    length: int
    valuation: int
    odd_multiplier: int
    dyadic_multiplier: int
    constant: int
    modulus: int

    def __mul__(self, other: "Summary") -> "Summary":
        if self.modulus != other.modulus:
            raise ValueError("modulus mismatch")
        m = self.modulus
        return Summary(
            self.length + other.length,
            self.valuation + other.valuation,
            self.odd_multiplier * other.odd_multiplier % m,
            self.dyadic_multiplier * other.dyadic_multiplier % m,
            (
                other.odd_multiplier * self.constant
                + self.dyadic_multiplier * other.constant
            )
            % m,
            m,
        )


def identity(modulus: int) -> Summary:
    return Summary(0, 0, 1 % modulus, 1 % modulus, 0, modulus)


def letter(bit: int, modulus: int) -> Summary:
    valuation = 1 + bit
    return Summary(1, valuation, 3 % modulus, pow(2, valuation, modulus), 1, modulus)


def monoid_power(value, exponent: int, identity_value, multiply: Callable):
    result = identity_value
    base = value
    while exponent:
        if exponent & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent >>= 1
    return result


def mechanical_product(
    ones: int,
    length: int,
    upper: bool,
    zero,
    one,
    identity_value,
    multiply: Callable,
):
    """Product of a lower/upper mechanical word in an arbitrary monoid."""
    if ones == 0:
        return monoid_power(zero, length, identity_value, multiply)
    if ones == length:
        return monoid_power(one, length, identity_value, multiply)
    quotient, remainder = divmod(length, ones)
    if upper:
        image_zero = multiply(one, monoid_power(zero, quotient - 1, identity_value, multiply))
        image_one = multiply(one, monoid_power(zero, quotient, identity_value, multiply))
        return mechanical_product(
            remainder,
            ones,
            False,
            image_zero,
            image_one,
            identity_value,
            multiply,
        )
    image_zero = multiply(monoid_power(zero, quotient - 1, identity_value, multiply), one)
    image_one = multiply(monoid_power(zero, quotient, identity_value, multiply), one)
    return mechanical_product(
        remainder,
        ones,
        True,
        image_zero,
        image_one,
        identity_value,
        multiply,
    )


def mechanical_bit(position: int) -> int:
    return ((position + 1) * ONES) // K - (position * ONES) // K


def prefix_valuation(prefix_length: int) -> int:
    return prefix_length + (prefix_length * ONES) // K


def legal_swap_sites(count: int) -> list[tuple[int, int, int, int]]:
    result: list[tuple[int, int, int, int]] = []
    previous = -2
    position = 0
    while len(result) < count:
        left = mechanical_bit(position)
        right = mechanical_bit(position + 1)
        if left != right and position > previous + 1:
            result.append((position, left, right, prefix_valuation(position + 1)))
            previous = position
        position += 1
    return result


def swap_delta(position: int, left: int, right: int, prefix: int, modulus: int) -> int:
    coefficient = pow(3, K - 2 - position, modulus)
    if (left, right) == (0, 1):
        return coefficient * pow(2, prefix, modulus) % modulus
    if (left, right) == (1, 0):
        return -coefficient * pow(2, prefix - 1, modulus) % modulus
    raise ValueError("not a legal adjacent swap")


class Interval:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = Decimal(lo)
        self.hi = Decimal(lo if hi is None else hi)


def directed_binary(a: Decimal, b: Decimal, operation, rounding: str) -> Decimal:
    with localcontext() as context:
        context.prec = PREC
        context.rounding = rounding
        return operation(a, b)


def interval_add(x: Interval, y: Interval) -> Interval:
    return Interval(
        directed_binary(x.lo, y.lo, lambda a, b: a + b, ROUND_FLOOR),
        directed_binary(x.hi, y.hi, lambda a, b: a + b, ROUND_CEILING),
    )


def interval_negate(x: Interval) -> Interval:
    return Interval(x.hi.copy_negate(), x.lo.copy_negate())


def interval_subtract(x: Interval, y: Interval) -> Interval:
    return interval_add(x, interval_negate(y))


def interval_multiply(x: Interval, y: Interval) -> Interval:
    lower = []
    upper = []
    for a in (x.lo, x.hi):
        for b in (y.lo, y.hi):
            lower.append(directed_binary(a, b, lambda c, d: c * d, ROUND_FLOOR))
            upper.append(directed_binary(a, b, lambda c, d: c * d, ROUND_CEILING))
    return Interval(min(lower), max(upper))


def interval_divide_positive(x: Interval, y: Interval) -> Interval:
    if y.lo <= 0:
        raise ValueError("positive denominator interval required")
    lower = []
    upper = []
    for a in (x.lo, x.hi):
        for b in (y.lo, y.hi):
            lower.append(directed_binary(a, b, lambda c, d: c / d, ROUND_FLOOR))
            upper.append(directed_binary(a, b, lambda c, d: c / d, ROUND_CEILING))
    return Interval(min(lower), max(upper))


def exact_fraction_interval(numerator: int, denominator: int) -> Interval:
    with localcontext() as context:
        context.prec = PREC
        context.rounding = ROUND_FLOOR
        lo = Decimal(numerator) / Decimal(denominator)
    with localcontext() as context:
        context.prec = PREC
        context.rounding = ROUND_CEILING
        hi = Decimal(numerator) / Decimal(denominator)
    return Interval(lo, hi)


@dataclass(frozen=True)
class AffineInterval:
    ratio: Interval
    translation: Interval


def affine_multiply(left: AffineInterval, right: AffineInterval) -> AffineInterval:
    return AffineInterval(
        interval_multiply(left.ratio, right.ratio),
        interval_add(
            interval_multiply(right.ratio, left.translation),
            right.translation,
        ),
    )


def affine_identity() -> AffineInterval:
    return AffineInterval(Interval(1), Interval(0))


def affine_letter(bit: int) -> AffineInterval:
    denominator = 1 << (1 + bit)
    return AffineInterval(
        exact_fraction_interval(3, denominator),
        exact_fraction_interval(1, denominator),
    )


def selected_indices() -> list[int]:
    return [i for i in range(40) if MASK_FIRST_40 >> i & 1] + [
        40 + i for i in range(40) if MASK_LAST_40 >> i & 1
    ]


def local_minima_count(sites, selected) -> int:
    base_count = K - ONES
    changed: dict[int, int] = {}
    for index in selected:
        position, left, right, _prefix = sites[index]
        changed[position] = right
        changed[position + 1] = left
    affected = set()
    for position in changed:
        affected.add(position)
        affected.add(position + 1)

    def base_bit(position: int) -> int:
        return mechanical_bit(position % K)

    def final_bit(position: int) -> int:
        position %= K
        return changed.get(position, base_bit(position))

    before = sum(base_bit(j - 1) == 1 and base_bit(j) == 0 for j in affected)
    after = sum(final_bit(j - 1) == 1 and final_bit(j) == 0 for j in affected)
    return base_count + after - before


def interval_fixed_point(sites, selected) -> Interval:
    base = mechanical_product(
        ONES,
        K,
        False,
        affine_letter(0),
        affine_letter(1),
        affine_identity(),
        affine_multiply,
    )
    delta = Interval(0)
    for index in selected:
        position, left, right, prefix = sites[index]
        if (left, right) == (0, 1):
            factor = exact_fraction_interval(1 << prefix, 3 ** (position + 2))
            contribution = interval_multiply(base.ratio, factor)
        else:
            factor = exact_fraction_interval(1 << (prefix - 1), 3 ** (position + 2))
            contribution = interval_negate(interval_multiply(base.ratio, factor))
        delta = interval_add(delta, contribution)
    numerator = interval_add(base.translation, delta)
    denominator = interval_subtract(Interval(1), base.ratio)
    return interval_divide_positive(numerator, denominator)


def generate() -> dict[str, object]:
    for factor in FACTORS:
        assert pow(2, A, factor) == pow(3, K, factor)

    base = mechanical_product(
        ONES,
        K,
        False,
        letter(0, MODULUS),
        letter(1, MODULUS),
        identity(MODULUS),
        lambda x, y: x * y,
    )
    assert base.length == K and base.valuation == A

    sites = legal_swap_sites(80)
    selected = selected_indices()
    positions = tuple(sites[index][0] for index in selected)
    assert positions == EXPECTED_SWAP_POSITIONS

    residue = base.constant
    for index in selected:
        residue = (residue + swap_delta(*sites[index], MODULUS)) % MODULUS
    assert residue == 0

    fixed = interval_fixed_point(sites, selected)
    floor_lo = int(fixed.lo)
    floor_hi = int(fixed.hi)
    assert floor_lo == floor_hi
    assert fixed.hi < Decimal(floor_lo + 1)
    assert fixed.lo > Decimal(floor_lo)

    minima = local_minima_count(sites, selected)
    assert minima > 95

    def exact_constant(word):
        prefix = 0
        total = 0
        for j, value in enumerate(word):
            total += 3 ** (len(word) - 1 - j) * 2 ** prefix
            prefix += value
        return total

    control = (1, 2, 1, 3)
    swapped = (1, 1, 2, 3)
    delta_control = exact_constant(swapped) - exact_constant(control)
    expected_delta = 3 ** (len(control) - 3) * 2 * (2 - 4)
    assert delta_control == expected_delta

    return {
        "schema_version": 1,
        "experiment_id": "X-8401",
        "target": {
            "accelerated_length": K,
            "total_valuation": A,
            "extra_binary_digits": ONES,
            "local_minima_after_swaps": minima,
        },
        "certified_divisor_component": {
            "factors": list(FACTORS),
            "product": MODULUS,
            "each_factor_divides_2A_minus_3K": True,
            "base_mechanical_constant_mod_product": base.constant,
            "modified_constant_mod_product": residue,
        },
        "mechanical_compiler": {
            "lower_word": True,
            "euclidean_recursion_depth_bound": "O(log k)",
            "summary_length": base.length,
            "summary_valuation": base.valuation,
        },
        "block_replacement": {
            "legal_sites_generated": len(sites),
            "selected_swap_count": len(selected),
            "mask_first_40": MASK_FIRST_40,
            "mask_last_40": MASK_LAST_40,
            "selected_positions": list(positions),
            "small_control_delta": delta_control,
        },
        "completion_safe_real_filter": {
            "fixed_point_lower": str(fixed.lo),
            "fixed_point_upper": str(fixed.hi),
            "interval_width": str(fixed.hi - fixed.lo),
            "unique_floor": floor_lo,
            "distance_to_next_integer_lower_bound": str(Decimal(floor_lo + 1) - fixed.hi),
            "conclusion": "the frozen modified word is not an integral cycle",
        },
        "interpretation": {
            "proved_by_exact_replay": [
                "the Euclidean monoid summary at the frozen modulus",
                "divisibility by the five listed denominator factors",
                "the 43 disjoint block replacements",
                "the directed real interval excluding integrality",
                "the exact cyclic local-minimum count",
            ],
            "not_proved": [
                "complete factorization of the cycle denominator",
                "a positive nontrivial cycle",
                "a divergent Collatz orbit",
                "the Collatz conjecture or its negation",
            ],
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
