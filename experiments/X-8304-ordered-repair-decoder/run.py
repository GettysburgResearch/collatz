#!/usr/bin/env python3
"""X-8304: decide the complete 80-site critical run-repair grammar."""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from pathlib import Path
from typing import Callable

K = 3_149_971_404_836
A = 4_992_586_555_009
CHART_BLOCKS = K // 2
EXPANDING = 2 * K - A
RUN_LENGTH = CHART_BLOCKS - EXPANDING
RUN_WEIGHT = EXPANDING - 4 * RUN_LENGTH
OMEGA = 7 * (2**16) * (3**9)
SITE_COUNT = 80
PRECISION = 180
ZERO = Decimal(0)


class Interval:
    __slots__ = ("lo", "hi")

    def __init__(self, lo: object, hi: object | None = None) -> None:
        self.lo = Decimal(lo)
        self.hi = Decimal(lo if hi is None else hi)


def directed(a: Decimal, b: Decimal, operation: Callable, rounding: str) -> Decimal:
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = rounding
        return operation(a, b)


def add(x: Interval, y: Interval) -> Interval:
    return Interval(
        directed(x.lo, y.lo, lambda a, b: a + b, ROUND_FLOOR),
        directed(x.hi, y.hi, lambda a, b: a + b, ROUND_CEILING),
    )


def negate(x: Interval) -> Interval:
    return Interval(x.hi.copy_negate(), x.lo.copy_negate())


def subtract(x: Interval, y: Interval) -> Interval:
    return add(x, negate(y))


def multiply(x: Interval, y: Interval) -> Interval:
    lowers: list[Decimal] = []
    uppers: list[Decimal] = []
    for a in (x.lo, x.hi):
        for b in (y.lo, y.hi):
            lowers.append(directed(a, b, lambda c, d: c * d, ROUND_FLOOR))
            uppers.append(directed(a, b, lambda c, d: c * d, ROUND_CEILING))
    return Interval(min(lowers), max(uppers))


def divide_positive(x: Interval, y: Interval) -> Interval:
    if y.lo <= 0:
        raise ValueError("positive denominator interval required")
    lowers: list[Decimal] = []
    uppers: list[Decimal] = []
    for a in (x.lo, x.hi):
        for b in (y.lo, y.hi):
            lowers.append(directed(a, b, lambda c, d: c / d, ROUND_FLOOR))
            uppers.append(directed(a, b, lambda c, d: c / d, ROUND_CEILING))
    return Interval(min(lowers), max(uppers))


def exact_fraction(numerator: int, denominator: int) -> Interval:
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_FLOOR
        lo = Decimal(numerator) / Decimal(denominator)
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        hi = Decimal(numerator) / Decimal(denominator)
    return Interval(lo, hi)


@dataclass(frozen=True)
class AffineInterval:
    ratio: Interval
    translation: Interval


def affine_identity() -> AffineInterval:
    return AffineInterval(Interval(1), Interval(0))


def affine_multiply(left: AffineInterval, right: AffineInterval) -> AffineInterval:
    return AffineInterval(
        multiply(left.ratio, right.ratio),
        add(multiply(right.ratio, left.translation), right.translation),
    )


def run_affine(bit: int) -> AffineInterval:
    run = 4 + bit
    denominator = 2 ** (16 + 3 * bit)
    return AffineInterval(
        exact_fraction(9 ** (5 + bit), denominator),
        exact_fraction(48 * (9**run - 8**run), denominator),
    )


def monoid_power(value, exponent: int, identity, operation: Callable):
    result = identity
    base = value
    while exponent:
        if exponent & 1:
            result = operation(result, base)
        base = operation(base, base)
        exponent >>= 1
    return result


def mechanical_product(
    ones: int,
    length: int,
    upper: bool,
    zero,
    one,
    identity,
    operation: Callable,
):
    if ones == 0:
        return monoid_power(zero, length, identity, operation)
    if ones == length:
        return monoid_power(one, length, identity, operation)
    quotient, remainder = divmod(length, ones)
    if upper:
        image_zero = operation(
            one, monoid_power(zero, quotient - 1, identity, operation)
        )
        image_one = operation(one, monoid_power(zero, quotient, identity, operation))
        return mechanical_product(
            remainder,
            ones,
            False,
            image_zero,
            image_one,
            identity,
            operation,
        )
    image_zero = operation(
        monoid_power(zero, quotient - 1, identity, operation), one
    )
    image_one = operation(monoid_power(zero, quotient, identity, operation), one)
    return mechanical_product(
        remainder,
        ones,
        True,
        image_zero,
        image_one,
        identity,
        operation,
    )


def prefix_weight(length: int) -> int:
    return (length * RUN_WEIGHT) // RUN_LENGTH


def mechanical_bit(position: int) -> int:
    return prefix_weight(position + 1) - prefix_weight(position)


def disjoint_sites(count: int) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []
    previous = -2
    position = 0
    while len(result) < count:
        left = mechanical_bit(position)
        right = mechanical_bit(position + 1)
        if left != right and position > previous + 1:
            result.append((position, left, right))
            previous = position
        position += 1
    return result


@dataclass(frozen=True)
class ModSummary:
    length: int
    valuation: int
    odd: int
    dyadic: int
    constant: int
    modulus: int

    def __mul__(self, other: "ModSummary") -> "ModSummary":
        if self.modulus != other.modulus:
            raise ValueError("modulus mismatch")
        modulus = self.modulus
        return ModSummary(
            self.length + other.length,
            self.valuation + other.valuation,
            self.odd * other.odd % modulus,
            self.dyadic * other.dyadic % modulus,
            (other.odd * self.constant + self.dyadic * other.constant) % modulus,
            modulus,
        )


def mod_identity(modulus: int) -> ModSummary:
    return ModSummary(0, 0, 1 % modulus, 1 % modulus, 0, modulus)


def run_mod(bit: int, modulus: int) -> ModSummary:
    return ModSummary(
        2 * (5 + bit),
        16 + 3 * bit,
        pow(9, 5 + bit, modulus),
        pow(2, 16 + 3 * bit, modulus),
        48 * (9 ** (4 + bit) - 8 ** (4 + bit)) % modulus,
        modulus,
    )


def site_data(site: tuple[int, int, int]) -> tuple[int, int, int, int]:
    position, left, right = site
    sign = -1 if (left, right) == (0, 1) else 1
    prefix_dyadic = 16 * position + 3 * prefix_weight(position)
    prefix_odd_pairs = 5 * position + prefix_weight(position)
    valuation = 16 + prefix_dyadic
    return sign, prefix_dyadic, prefix_odd_pairs, valuation


def delta_mod(site: tuple[int, int, int], modulus: int) -> int:
    sign, prefix_dyadic, prefix_odd_pairs, _valuation = site_data(site)
    odd_exponent = K - 2 * (prefix_odd_pairs + 11)
    return (
        sign
        * OMEGA
        * pow(2, prefix_dyadic, modulus)
        * pow(3, odd_exponent, modulus)
    ) % modulus


def integers_in_residue_interval(
    residue: int, modulus: int, lower: int, upper: int
) -> list[int]:
    first_multiplier = (lower - residue + modulus - 1) // modulus
    first = residue + first_multiplier * modulus
    if first > upper:
        return []
    count = (upper - first) // modulus + 1
    return [first + index * modulus for index in range(count)]


def generate() -> dict[str, object]:
    sites = disjoint_sites(SITE_COUNT)
    assert [position for position, _left, _right in sites[:3]] == [0, 7, 15]
    valuations = [site_data(site)[3] for site in sites]
    assert all(a < b for a, b in zip(valuations, valuations[1:]))
    assert valuations[2] == 295

    base = mechanical_product(
        RUN_WEIGHT,
        RUN_LENGTH,
        False,
        run_affine(0),
        run_affine(1),
        affine_identity(),
        affine_multiply,
    )
    denominator = subtract(Interval(1), base.ratio)
    assert denominator.lo > 0

    lower_numerator = base.translation
    upper_numerator = base.translation
    for site in sites:
        sign, prefix_dyadic, prefix_odd_pairs, _valuation = site_data(site)
        contribution = multiply(
            base.ratio,
            exact_fraction(
                OMEGA * (2**prefix_dyadic), 9 ** (prefix_odd_pairs + 11)
            ),
        )
        if sign < 0:
            contribution = negate(contribution)
        lower_numerator = add(
            lower_numerator,
            Interval(min(ZERO, contribution.lo), min(ZERO, contribution.hi)),
        )
        upper_numerator = add(
            upper_numerator,
            Interval(max(ZERO, contribution.lo), max(ZERO, contribution.hi)),
        )

    fixed_lower = divide_positive(lower_numerator, denominator).lo
    fixed_upper = divide_positive(upper_numerator, denominator).hi
    integer_lower = math.ceil(fixed_lower)
    integer_upper = math.floor(fixed_upper)
    assert integer_lower <= integer_upper

    modulus_bits = valuations[2]
    modulus = 1 << modulus_bits
    assert fixed_upper < Decimal(modulus)

    zero = run_mod(0, modulus)
    one = run_mod(1, modulus)
    base_mod = mechanical_product(
        RUN_WEIGHT,
        RUN_LENGTH,
        False,
        zero,
        one,
        mod_identity(modulus),
        lambda x, y: x * y,
    )
    denominator_mod = (-pow(3, K, modulus)) % modulus
    denominator_inverse = pow(denominator_mod, -1, modulus)

    viable: list[tuple[int, int]] = []
    prefix_residues: list[int] = []
    for mask in range(4):
        numerator = base_mod.constant
        for index in range(2):
            if mask >> index & 1:
                numerator = (numerator + delta_mod(sites[index], modulus)) % modulus
        quotient_residue = numerator * denominator_inverse % modulus
        prefix_residues.append(quotient_residue)
        for candidate in integers_in_residue_interval(
            quotient_residue, modulus, integer_lower, integer_upper
        ):
            viable.append((mask, candidate))

    assert len(set(prefix_residues)) == 4
    assert viable == []

    return {
        "schema_version": 1,
        "experiment_id": "X-8304",
        "critical_shape": {
            "accelerated_length": K,
            "total_valuation": A,
            "run_length": RUN_LENGTH,
            "run_weight": RUN_WEIGHT,
        },
        "grammar": {
            "disjoint_sites": SITE_COUNT,
            "subset_count": str(1 << SITE_COUNT),
            "first_site_positions": [0, 7, 15],
        },
        "certificate": {
            "first_bits_enumerated": 2,
            "prefix_masks_checked": 4,
            "future_delta_divisibility_bits": modulus_bits,
            "distinct_quotient_residues": len(set(prefix_residues)),
            "real_integer_window_nonempty": True,
            "real_window_below_modulus": True,
            "viable_prefixes": len(viable),
        },
        "conclusion": (
            "no subset of the complete frozen 80-site disjoint run-transposition "
            "grammar has an integral fixed point"
        ),
        "not_proved": [
            "the same conclusion for later or overlapping repair sites",
            "the absence of a positive accelerated cycle in general",
            "the absence of an infinite negative-cycle chart path",
            "the Collatz conjecture",
        ],
    }


def canonical_bytes(payload: dict[str, object]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    data = canonical_bytes(generate())
    if args.write_results:
        args.write_results.parent.mkdir(parents=True, exist_ok=True)
        args.write_results.write_bytes(data)
    if args.check_results and args.check_results.read_bytes() != data:
        raise SystemExit("canonical result mismatch")
    print(data.decode("utf-8"), end="")


if __name__ == "__main__":
    main()
