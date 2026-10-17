#!/usr/bin/env python3
"""X-8306: exact critical Farey-tree grammar compiler."""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from functools import lru_cache
from pathlib import Path
from typing import Callable

ROOT_P = 236_838_463_643
ROOT_Q = 267_629_447_755
K = 3_149_971_404_836
A = 4_992_586_555_009
BITS = 314
MODULUS = 1 << BITS
PRECISION = 190
sys.setrecursionlimit(1_000_000)


@lru_cache(maxsize=None)
def farey_parents(p: int, q: int):
    if (p, q) in ((0, 1), (1, 1)):
        return None
    b = pow(p, -1, q)
    a = (p * b - 1) // q
    left = (a, b)
    right = (p - a, q - b)
    assert p * b - q * a == 1
    assert left[0] * right[1] < right[0] * left[1]
    return left, right


def lower_word(p: int, q: int) -> tuple[int, ...]:
    return tuple(((j + 1) * p) // q - (j * p) // q for j in range(q))


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


def multiply(x: Interval, y: Interval) -> Interval:
    lower: list[Decimal] = []
    upper: list[Decimal] = []
    for a in (x.lo, x.hi):
        for b in (y.lo, y.hi):
            lower.append(directed(a, b, lambda c, d: c * d, ROUND_FLOOR))
            upper.append(directed(a, b, lambda c, d: c * d, ROUND_CEILING))
    return Interval(min(lower), max(upper))


def divide_positive(x: Interval, y: Interval) -> Interval:
    if y.lo <= 0:
        raise ValueError("positive denominator required")
    lower: list[Decimal] = []
    upper: list[Decimal] = []
    for a in (x.lo, x.hi):
        for b in (y.lo, y.hi):
            lower.append(directed(a, b, lambda c, d: c / d, ROUND_FLOOR))
            upper.append(directed(a, b, lambda c, d: c / d, ROUND_CEILING))
    return Interval(min(lower), max(upper))


def fraction(numerator: int, denominator: int) -> Interval:
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
class RealSummary:
    ratio: Interval
    translation: Interval


@lru_cache(maxsize=None)
def real_summary(node: tuple[int, int]) -> RealSummary:
    if node == (0, 1):
        return RealSummary(
            fraction(9**5, 2**16),
            fraction(48 * (9**4 - 8**4), 2**16),
        )
    if node == (1, 1):
        return RealSummary(
            fraction(9**6, 2**19),
            fraction(48 * (9**5 - 8**5), 2**19),
        )
    children = farey_parents(*node)
    assert children is not None
    left, right = children
    x = real_summary(left)
    y = real_summary(right)
    ratio = multiply(x.ratio, y.ratio)
    xy = add(multiply(y.ratio, x.translation), y.translation)
    yx = add(multiply(x.ratio, y.translation), x.translation)
    translation = Interval(min(xy.lo, yx.lo), max(xy.hi, yx.hi))
    return RealSummary(ratio, translation)


@lru_cache(maxsize=None)
def multipliers(node: tuple[int, int]) -> tuple[int, int]:
    p, q = node
    return (
        pow(9, 5 * q + p, MODULUS),
        pow(2, 16 * q + 3 * p, MODULUS),
    )


@lru_cache(maxsize=None)
def constants(node: tuple[int, int]) -> frozenset[int]:
    if node == (0, 1):
        return frozenset([48 * (9**4 - 8**4) % MODULUS])
    if node == (1, 1):
        return frozenset([48 * (9**5 - 8**5) % MODULUS])
    children = farey_parents(*node)
    assert children is not None
    left, right = children
    left_values = constants(left)
    right_values = constants(right)
    p_left, q_left = multipliers(left)
    p_right, q_right = multipliers(right)
    result: set[int] = set()
    for c_left in left_values:
        for c_right in right_values:
            result.add((p_right * c_left + q_left * c_right) % MODULUS)
            result.add((p_left * c_right + q_right * c_left) % MODULUS)
    return frozenset(result)


def small_orientation_checks() -> None:
    for q in range(2, 40):
        for p in range(1, q):
            if math.gcd(p, q) != 1:
                continue
            children = farey_parents(p, q)
            assert children is not None
            left, right = children
            assert lower_word(p, q) == lower_word(*left) + lower_word(*right)


def generate() -> dict[str, object]:
    small_orientation_checks()

    real = real_summary((ROOT_P, ROOT_Q))
    denominator = Interval(
        directed(Decimal(1), real.ratio.hi, lambda a, b: a - b, ROUND_FLOOR),
        directed(Decimal(1), real.ratio.lo, lambda a, b: a - b, ROUND_CEILING),
    )
    fixed = divide_positive(real.translation, denominator)
    integer_lower = math.ceil(fixed.lo)
    integer_upper = math.floor(fixed.hi)
    assert 0 < integer_lower <= integer_upper
    assert fixed.hi < Decimal(MODULUS)

    root_constants = constants((ROOT_P, ROOT_Q))
    denominator_mod = (-pow(3, K, MODULUS)) % MODULUS
    inverse = pow(denominator_mod, -1, MODULUS)
    viable = 0
    for constant in root_constants:
        residue = constant * inverse % MODULUS
        if integer_lower <= residue <= integer_upper:
            viable += 1
    assert viable == 0

    return {
        "schema_version": 1,
        "experiment_id": "X-8306",
        "critical_shape": {
            "run_fraction": [ROOT_P, ROOT_Q],
            "accelerated_length": K,
            "total_valuation": A,
        },
        "grammar": {
            "type": "recursive Farey sibling swaps",
            "leaf_count": ROOT_Q,
            "internal_occurrences": ROOT_Q - 1,
            "independent_choice_at_each_occurrence": True,
        },
        "certificate": {
            "precision_bits": BITS,
            "small_farey_orientation_checks": True,
            "exact_modular_set_compiled": True,
            "directed_real_envelope_compiled": True,
            "real_integer_window_nonempty": True,
            "real_envelope_positive": True,
            "real_envelope_below_modulus": True,
            "viable_quotient_residues": viable,
        },
        "conclusion": (
            "the full critical hierarchical Farey sibling-swap grammar contains "
            "no integral fixed point"
        ),
        "not_proved": [
            "the same result for arbitrary fixed-weight words",
            "the same result for grammars changing the critical shape",
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
    print(data.decode(), end="")


if __name__ == "__main__":
    main()
