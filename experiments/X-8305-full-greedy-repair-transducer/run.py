#!/usr/bin/env python3
"""X-8305: exact full-word greedy repair envelope and quotient cylinders."""
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
BLOCKS = K // 2
EXPANDING = 2 * K - A
LENGTH = BLOCKS - EXPANDING
WEIGHT = EXPANDING - 4 * LENGTH
OMEGA = 7 * 2**16 * 3**9
PRECISION = 190
Z = Decimal(0)


class Interval:
    __slots__ = ("lo", "hi")

    def __init__(self, lo: object, hi: object | None = None) -> None:
        self.lo = Decimal(lo)
        self.hi = Decimal(lo if hi is None else hi)


def directed(a: Decimal, b: Decimal, fn: Callable, rounding: str) -> Decimal:
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = rounding
        return fn(a, b)


def add(x: Interval, y: Interval) -> Interval:
    return Interval(
        directed(x.lo, y.lo, lambda a, b: a + b, ROUND_FLOOR),
        directed(x.hi, y.hi, lambda a, b: a + b, ROUND_CEILING),
    )


def neg(x: Interval) -> Interval:
    return Interval(-x.hi, -x.lo)


def sub(x: Interval, y: Interval) -> Interval:
    return add(x, neg(y))


def mul(x: Interval, y: Interval) -> Interval:
    lower: list[Decimal] = []
    upper: list[Decimal] = []
    for a in (x.lo, x.hi):
        for b in (y.lo, y.hi):
            lower.append(directed(a, b, lambda c, d: c * d, ROUND_FLOOR))
            upper.append(directed(a, b, lambda c, d: c * d, ROUND_CEILING))
    return Interval(min(lower), max(upper))


def div_positive(x: Interval, y: Interval) -> Interval:
    if y.lo <= 0:
        raise ValueError("positive denominator required")
    lower: list[Decimal] = []
    upper: list[Decimal] = []
    for a in (x.lo, x.hi):
        for b in (y.lo, y.hi):
            lower.append(directed(a, b, lambda c, d: c / d, ROUND_FLOOR))
            upper.append(directed(a, b, lambda c, d: c / d, ROUND_CEILING))
    return Interval(min(lower), max(upper))


def frac(numerator: int, denominator: int) -> Interval:
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_FLOOR
        lo = Decimal(numerator) / Decimal(denominator)
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        hi = Decimal(numerator) / Decimal(denominator)
    return Interval(lo, hi)


def power(value, exponent: int, identity, compose: Callable):
    result = identity
    while exponent:
        if exponent & 1:
            result = compose(result, value)
        value = compose(value, value)
        exponent >>= 1
    return result


def mechanical_product(
    ones: int,
    length: int,
    upper: bool,
    zero,
    one,
    identity,
    compose: Callable,
):
    if ones == 0:
        return power(zero, length, identity, compose)
    if ones == length:
        return power(one, length, identity, compose)
    quotient, remainder = divmod(length, ones)
    if upper:
        image_zero = compose(one, power(zero, quotient - 1, identity, compose))
        image_one = compose(one, power(zero, quotient, identity, compose))
        return mechanical_product(
            remainder,
            ones,
            False,
            image_zero,
            image_one,
            identity,
            compose,
        )
    image_zero = compose(power(zero, quotient - 1, identity, compose), one)
    image_one = compose(power(zero, quotient, identity, compose), one)
    return mechanical_product(
        remainder,
        ones,
        True,
        image_zero,
        image_one,
        identity,
        compose,
    )


@dataclass(frozen=True)
class Affine:
    ratio: Interval
    translation: Interval


def affine_identity() -> Affine:
    return Affine(Interval(1), Interval(0))


def affine_compose(left: Affine, right: Affine) -> Affine:
    return Affine(
        mul(left.ratio, right.ratio),
        add(mul(right.ratio, left.translation), right.translation),
    )


def run_affine(bit: int) -> Affine:
    run = 4 + bit
    denominator = 2 ** (16 + 3 * bit)
    return Affine(
        frac(9 ** (5 + bit), denominator),
        frac(48 * (9**run - 8**run), denominator),
    )


# States: 0=empty, 1=pending zero, 2=pending one.
@dataclass(frozen=True)
class Scan:
    multiplier: Interval
    end: tuple[int, int, int]
    positive: tuple[Interval, Interval, Interval]
    negative: tuple[Interval, Interval, Interval]
    count: tuple[int, int, int]


def scan_identity() -> Scan:
    zeros = (Interval(0), Interval(0), Interval(0))
    return Scan(Interval(1), (0, 1, 2), zeros, zeros, (0, 0, 0))


def scan_letter(bit: int) -> Scan:
    multiplier = frac(2 ** (16 + 3 * bit), 9 ** (5 + bit))
    ends: list[int] = []
    positive: list[Interval] = []
    negative: list[Interval] = []
    counts: list[int] = []
    for state in range(3):
        if state == 0:
            ends.append(1 + bit)
            positive.append(Interval(0))
            negative.append(Interval(0))
            counts.append(0)
        elif state == 1:
            if bit == 0:
                ends.append(1)
                positive.append(Interval(0))
                negative.append(Interval(0))
                counts.append(0)
            else:
                ends.append(0)
                positive.append(Interval(0))
                negative.append(frac(9**5, 2**16))
                counts.append(1)
        else:
            if bit == 1:
                ends.append(2)
                positive.append(Interval(0))
                negative.append(Interval(0))
                counts.append(0)
            else:
                ends.append(0)
                positive.append(frac(9**6, 2**19))
                negative.append(Interval(0))
                counts.append(1)
    return Scan(
        multiplier,
        tuple(ends),
        tuple(positive),
        tuple(negative),
        tuple(counts),
    )


def scan_compose(left: Scan, right: Scan) -> Scan:
    ends: list[int] = []
    positive: list[Interval] = []
    negative: list[Interval] = []
    counts: list[int] = []
    for state in range(3):
        middle = left.end[state]
        ends.append(right.end[middle])
        positive.append(
            add(left.positive[state], mul(left.multiplier, right.positive[middle]))
        )
        negative.append(
            add(left.negative[state], mul(left.multiplier, right.negative[middle]))
        )
        counts.append(left.count[state] + right.count[middle])
    return Scan(
        mul(left.multiplier, right.multiplier),
        tuple(ends),
        tuple(positive),
        tuple(negative),
        tuple(counts),
    )


def prefix_weight(length: int) -> int:
    return length * WEIGHT // LENGTH


def bit(position: int) -> int:
    return prefix_weight(position + 1) - prefix_weight(position)


def first_sites(count: int) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []
    previous = -2
    position = 0
    while len(result) < count:
        left, right = bit(position), bit(position + 1)
        if left != right and position > previous + 1:
            result.append((position, left, right))
            previous = position
        position += 1
    return result


@dataclass(frozen=True)
class ModSummary:
    odd: int
    dyadic: int
    constant: int
    modulus: int


def mod_identity(modulus: int) -> ModSummary:
    return ModSummary(1 % modulus, 1 % modulus, 0, modulus)


def mod_run(bit: int, modulus: int) -> ModSummary:
    return ModSummary(
        pow(9, 5 + bit, modulus),
        pow(2, 16 + 3 * bit, modulus),
        48 * (9 ** (4 + bit) - 8 ** (4 + bit)) % modulus,
        modulus,
    )


def mod_compose(left: ModSummary, right: ModSummary) -> ModSummary:
    modulus = left.modulus
    if modulus != right.modulus:
        raise ValueError("modulus mismatch")
    return ModSummary(
        left.odd * right.odd % modulus,
        left.dyadic * right.dyadic % modulus,
        (right.odd * left.constant + left.dyadic * right.constant) % modulus,
        modulus,
    )


def site_fields(site: tuple[int, int, int]) -> tuple[int, int, int, int]:
    position, left, right = site
    sign = -1 if (left, right) == (0, 1) else 1
    dyadic = 16 * position + 3 * prefix_weight(position)
    odd_pairs = 5 * position + prefix_weight(position)
    return sign, dyadic, odd_pairs, 16 + dyadic


def delta_mod(site: tuple[int, int, int], modulus: int) -> int:
    sign, dyadic, odd_pairs, _valuation = site_fields(site)
    return (
        sign
        * OMEGA
        * pow(2, dyadic, modulus)
        * pow(3, K - 2 * (odd_pairs + 11), modulus)
    ) % modulus


def generate() -> dict[str, object]:
    base = mechanical_product(
        WEIGHT,
        LENGTH,
        False,
        run_affine(0),
        run_affine(1),
        affine_identity(),
        affine_compose,
    )
    scan = mechanical_product(
        WEIGHT,
        LENGTH,
        False,
        scan_letter(0),
        scan_letter(1),
        scan_identity(),
        scan_compose,
    )
    assert scan.count[0] == 30_790_984_112

    common = mul(base.ratio, frac(OMEGA, 9**11))
    lower_numerator = add(base.translation, neg(mul(common, scan.negative[0])))
    upper_numerator = add(base.translation, mul(common, scan.positive[0]))
    denominator = sub(Interval(1), base.ratio)
    fixed_lower = div_positive(lower_numerator, denominator).lo
    fixed_upper = div_positive(upper_numerator, denominator).hi
    integer_lower = math.ceil(fixed_lower)
    integer_upper = math.floor(fixed_upper)
    assert 0 < integer_lower <= integer_upper

    sites = first_sites(3)
    assert [site[0] for site in sites] == [0, 7, 15]
    valuations = [site_fields(site)[3] for site in sites]
    assert valuations == [16, 146, 295]

    modulus_bits = 295
    modulus = 1 << modulus_bits
    assert fixed_upper < Decimal(modulus)
    base_mod = mechanical_product(
        WEIGHT,
        LENGTH,
        False,
        mod_run(0, modulus),
        mod_run(1, modulus),
        mod_identity(modulus),
        mod_compose,
    )
    denominator_mod = (-pow(3, K, modulus)) % modulus
    inverse = pow(denominator_mod, -1, modulus)

    quotient_residues: list[int] = []
    for mask in range(4):
        constant = base_mod.constant
        for index in range(2):
            if mask >> index & 1:
                constant = (constant + delta_mod(sites[index], modulus)) % modulus
        quotient_residues.append(constant * inverse % modulus)

    assert len(set(quotient_residues)) == 4
    viable = [
        residue
        for residue in quotient_residues
        if integer_lower <= residue <= integer_upper
    ]
    assert viable == []

    return {
        "schema_version": 1,
        "experiment_id": "X-8305",
        "critical_shape": {
            "accelerated_length": K,
            "total_valuation": A,
            "run_length": LENGTH,
            "run_weight": WEIGHT,
        },
        "full_greedy_grammar": {
            "site_count": scan.count[0],
            "subset_count": "2^30790984112",
            "first_site_positions": [0, 7, 15],
            "first_delta_valuations": [16, 146, 295],
        },
        "certificate": {
            "first_bits_enumerated": 2,
            "prefix_masks_checked": 4,
            "future_delta_divisibility_bits": modulus_bits,
            "distinct_quotient_residues": len(set(quotient_residues)),
            "full_real_integer_window_nonempty": True,
            "full_real_window_positive": True,
            "full_real_window_below_modulus": True,
            "viable_prefixes": len(viable),
        },
        "conclusion": (
            "the complete canonical full-word greedy disjoint run-repair grammar "
            "contains no integral fixed point"
        ),
        "not_proved": [
            "the same result for overlapping or noncanonical matchings",
            "the same result for hierarchical Farey block repairs",
            "the absence of positive accelerated cycles in general",
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
