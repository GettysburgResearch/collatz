#!/usr/bin/env python3
"""Independent iterative verifier for X-8306."""
from __future__ import annotations

import json
import math
import sys
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from pathlib import Path

ROOT = (236_838_463_643, 267_629_447_755)
K = 3_149_971_404_836
A = 4_992_586_555_009
BITS = 314
MODULUS = 1 << BITS
PRECISION = 220


def parents(node: tuple[int, int]):
    p, q = node
    if node in ((0, 1), (1, 1)):
        return None
    b = pow(p, -1, q)
    a = (p * b - 1) // q
    return (a, b), (p - a, q - b)


def word(p: int, q: int) -> tuple[int, ...]:
    return tuple(((j + 1) * p) // q - (j * p) // q for j in range(q))


class Ball:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = Decimal(lo)
        self.hi = Decimal(lo if hi is None else hi)


def op(a, b, fn, rounding):
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = rounding
        return fn(a, b)


def plus(x, y):
    return Ball(
        op(x.lo, y.lo, lambda a, b: a + b, ROUND_FLOOR),
        op(x.hi, y.hi, lambda a, b: a + b, ROUND_CEILING),
    )


def times(x, y):
    lower = []
    upper = []
    for a in (x.lo, x.hi):
        for b in (y.lo, y.hi):
            lower.append(op(a, b, lambda c, d: c * d, ROUND_FLOOR))
            upper.append(op(a, b, lambda c, d: c * d, ROUND_CEILING))
    return Ball(min(lower), max(upper))


def divide(x, y):
    assert y.lo > 0
    lower = []
    upper = []
    for a in (x.lo, x.hi):
        for b in (y.lo, y.hi):
            lower.append(op(a, b, lambda c, d: c / d, ROUND_FLOOR))
            upper.append(op(a, b, lambda c, d: c / d, ROUND_CEILING))
    return Ball(min(lower), max(upper))


def rational(a, b):
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_FLOOR
        lo = Decimal(a) / Decimal(b)
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        hi = Decimal(a) / Decimal(b)
    return Ball(lo, hi)


def build_nodes() -> list[tuple[int, int]]:
    seen: set[tuple[int, int]] = set()
    stack = [ROOT]
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        children = parents(node)
        if children is not None:
            stack.extend(children)
    return sorted(seen, key=lambda item: (item[1], item[0]))


def verify(path: Path) -> None:
    frozen = json.loads(path.read_text())
    assert frozen["experiment_id"] == "X-8306"
    assert frozen["certificate"]["viable_quotient_residues"] == 0

    for q in range(2, 45):
        for p in range(1, q):
            if math.gcd(p, q) != 1:
                continue
            children = parents((p, q))
            assert children is not None
            left, right = children
            assert word(p, q) == word(*left) + word(*right)

    nodes = build_nodes()
    ratios: dict[tuple[int, int], Ball] = {}
    translations: dict[tuple[int, int], Ball] = {}
    constants: dict[tuple[int, int], frozenset[int]] = {}
    multipliers: dict[tuple[int, int], tuple[int, int]] = {}

    for node in nodes:
        p, q = node
        multipliers[node] = (
            pow(9, 5 * q + p, MODULUS),
            pow(2, 16 * q + 3 * p, MODULUS),
        )
        if node == (0, 1):
            ratios[node] = rational(9**5, 2**16)
            translations[node] = rational(48 * (9**4 - 8**4), 2**16)
            constants[node] = frozenset([48 * (9**4 - 8**4) % MODULUS])
            continue
        if node == (1, 1):
            ratios[node] = rational(9**6, 2**19)
            translations[node] = rational(48 * (9**5 - 8**5), 2**19)
            constants[node] = frozenset([48 * (9**5 - 8**5) % MODULUS])
            continue

        children = parents(node)
        assert children is not None
        left, right = children
        assert left in ratios and right in ratios

        ratios[node] = times(ratios[left], ratios[right])
        lr = plus(times(ratios[right], translations[left]), translations[right])
        rl = plus(times(ratios[left], translations[right]), translations[left])
        translations[node] = Ball(min(lr.lo, rl.lo), max(lr.hi, rl.hi))

        p_left, q_left = multipliers[left]
        p_right, q_right = multipliers[right]
        result: set[int] = set()
        for c_left in constants[left]:
            for c_right in constants[right]:
                result.add((p_right * c_left + q_left * c_right) % MODULUS)
                result.add((p_left * c_right + q_right * c_left) % MODULUS)
        constants[node] = frozenset(result)

    ratio = ratios[ROOT]
    translation = translations[ROOT]
    denominator = Ball(
        op(Decimal(1), ratio.hi, lambda a, b: a - b, ROUND_FLOOR),
        op(Decimal(1), ratio.lo, lambda a, b: a - b, ROUND_CEILING),
    )
    fixed = divide(translation, denominator)
    integer_lower = math.ceil(fixed.lo)
    integer_upper = math.floor(fixed.hi)
    assert 0 < integer_lower <= integer_upper
    assert fixed.hi < Decimal(MODULUS)

    denominator_mod = (-pow(3, K, MODULUS)) % MODULUS
    inverse = pow(denominator_mod, -1, MODULUS)
    for constant in constants[ROOT]:
        residue = constant * inverse % MODULUS
        assert not (integer_lower <= residue <= integer_upper)

    assert frozen["grammar"]["leaf_count"] == ROOT[1]
    assert frozen["grammar"]["internal_occurrences"] == ROOT[1] - 1
    print("independent X-8306 verification passed")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py results/canonical.json")
    verify(Path(sys.argv[1]))
