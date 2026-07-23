#!/usr/bin/env python3
"""Independent X-8305 verifier.  It imports no X-8305 author code."""
from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from pathlib import Path

K = 3_149_971_404_836
A = 4_992_586_555_009
BLOCKS = K // 2
EXPANDING = 2 * K - A
N = BLOCKS - EXPANDING
W = EXPANDING - 4 * N
OMEGA = 7 * 2**16 * 3**9
PREC = 230


class I:
    def __init__(self, lo, hi=None):
        self.lo = Decimal(lo)
        self.hi = Decimal(lo if hi is None else hi)


def rounded(a, b, fn, mode):
    with localcontext() as context:
        context.prec = PREC
        context.rounding = mode
        return fn(a, b)


def add(x, y):
    return I(
        rounded(x.lo, y.lo, lambda a, b: a + b, ROUND_FLOOR),
        rounded(x.hi, y.hi, lambda a, b: a + b, ROUND_CEILING),
    )


def neg(x):
    return I(-x.hi, -x.lo)


def mul(x, y):
    lows = []
    highs = []
    for a in (x.lo, x.hi):
        for b in (y.lo, y.hi):
            lows.append(rounded(a, b, lambda c, d: c * d, ROUND_FLOOR))
            highs.append(rounded(a, b, lambda c, d: c * d, ROUND_CEILING))
    return I(min(lows), max(highs))


def div(x, y):
    assert y.lo > 0
    lows = []
    highs = []
    for a in (x.lo, x.hi):
        for b in (y.lo, y.hi):
            lows.append(rounded(a, b, lambda c, d: c / d, ROUND_FLOOR))
            highs.append(rounded(a, b, lambda c, d: c / d, ROUND_CEILING))
    return I(min(lows), max(highs))


def fraction(a, b):
    with localcontext() as context:
        context.prec = PREC
        context.rounding = ROUND_FLOOR
        lo = Decimal(a) / Decimal(b)
    with localcontext() as context:
        context.prec = PREC
        context.rounding = ROUND_CEILING
        hi = Decimal(a) / Decimal(b)
    return I(lo, hi)


def monoid_power(value, exponent, identity, compose):
    out = identity
    while exponent:
        if exponent & 1:
            out = compose(out, value)
        value = compose(value, value)
        exponent //= 2
    return out


def lower_mechanical(ones, length, upper, zero, one, identity, compose):
    if ones == 0:
        return monoid_power(zero, length, identity, compose)
    if ones == length:
        return monoid_power(one, length, identity, compose)
    quotient, remainder = divmod(length, ones)
    if upper:
        z = compose(one, monoid_power(zero, quotient - 1, identity, compose))
        o = compose(one, monoid_power(zero, quotient, identity, compose))
        return lower_mechanical(remainder, ones, False, z, o, identity, compose)
    z = compose(monoid_power(zero, quotient - 1, identity, compose), one)
    o = compose(monoid_power(zero, quotient, identity, compose), one)
    return lower_mechanical(remainder, ones, True, z, o, identity, compose)


@dataclass(frozen=True)
class Aff:
    r: I
    t: I


def aff_id():
    return Aff(I(1), I(0))


def aff_mul(x, y):
    return Aff(mul(x.r, y.r), add(mul(y.r, x.t), y.t))


def aff_bit(bit):
    run = 4 + bit
    denominator = 2 ** (16 + 3 * bit)
    return Aff(
        fraction(9 ** (5 + bit), denominator),
        fraction(48 * (9**run - 8**run), denominator),
    )


@dataclass(frozen=True)
class Weighted:
    g: I
    end: tuple
    pos: tuple
    neg: tuple
    count: tuple


def weighted_id():
    z = (I(0), I(0), I(0))
    return Weighted(I(1), (0, 1, 2), z, z, (0, 0, 0))


def weighted_bit(bit):
    g = fraction(2 ** (16 + 3 * bit), 9 ** (5 + bit))
    end = []
    positive = []
    negative = []
    count = []
    for state in range(3):
        if state == 0:
            end.append(1 + bit)
            positive.append(I(0))
            negative.append(I(0))
            count.append(0)
        elif state == 1 and bit == 1:
            end.append(0)
            positive.append(I(0))
            negative.append(fraction(9**5, 2**16))
            count.append(1)
        elif state == 2 and bit == 0:
            end.append(0)
            positive.append(fraction(9**6, 2**19))
            negative.append(I(0))
            count.append(1)
        else:
            end.append(1 + bit)
            positive.append(I(0))
            negative.append(I(0))
            count.append(0)
    return Weighted(g, tuple(end), tuple(positive), tuple(negative), tuple(count))


def weighted_mul(x, y):
    end = []
    pos = []
    negs = []
    counts = []
    for state in range(3):
        middle = x.end[state]
        end.append(y.end[middle])
        pos.append(add(x.pos[state], mul(x.g, y.pos[middle])))
        negs.append(add(x.neg[state], mul(x.g, y.neg[middle])))
        counts.append(x.count[state] + y.count[middle])
    return Weighted(
        mul(x.g, y.g), tuple(end), tuple(pos), tuple(negs), tuple(counts)
    )


def prefix(length):
    return length * W // N


def mechanical_bit(index):
    return prefix(index + 1) - prefix(index)


def first_sites(count):
    result = []
    previous = -2
    index = 0
    while len(result) < count:
        left = mechanical_bit(index)
        right = mechanical_bit(index + 1)
        if left != right and index > previous + 1:
            result.append((index, left, right))
            previous = index
        index += 1
    return result


def fields(site):
    index, left, right = site
    sign = -1 if (left, right) == (0, 1) else 1
    dyadic = 16 * index + 3 * prefix(index)
    odd = 5 * index + prefix(index)
    return sign, dyadic, odd, 16 + dyadic


@dataclass(frozen=True)
class Mod:
    p: int
    q: int
    c: int
    modulus: int


def mod_id(modulus):
    return Mod(1, 1, 0, modulus)


def mod_bit(bit, modulus):
    return Mod(
        pow(9, 5 + bit, modulus),
        pow(2, 16 + 3 * bit, modulus),
        48 * (9 ** (4 + bit) - 8 ** (4 + bit)) % modulus,
        modulus,
    )


def mod_mul(x, y):
    m = x.modulus
    assert m == y.modulus
    return Mod(
        x.p * y.p % m,
        x.q * y.q % m,
        (y.p * x.c + x.q * y.c) % m,
        m,
    )


def repair_mod(site, modulus):
    sign, dyadic, odd, _ = fields(site)
    return (
        sign
        * OMEGA
        * pow(2, dyadic, modulus)
        * pow(3, K - 2 * (odd + 11), modulus)
    ) % modulus


def verify(path):
    frozen = json.loads(Path(path).read_text())
    assert frozen["experiment_id"] == "X-8305"
    assert frozen["certificate"]["viable_prefixes"] == 0

    base = lower_mechanical(
        W, N, False, aff_bit(0), aff_bit(1), aff_id(), aff_mul
    )
    scan = lower_mechanical(
        W,
        N,
        False,
        weighted_bit(0),
        weighted_bit(1),
        weighted_id(),
        weighted_mul,
    )
    assert scan.count[0] == 30_790_984_112
    assert scan.count[0] == frozen["full_greedy_grammar"]["site_count"]

    factor = mul(base.r, fraction(OMEGA, 9**11))
    lower_numerator = add(base.t, neg(mul(factor, scan.neg[0])))
    upper_numerator = add(base.t, mul(factor, scan.pos[0]))
    denominator = add(I(1), neg(base.r))
    lo = div(lower_numerator, denominator).lo
    hi = div(upper_numerator, denominator).hi
    lower_integer = math.ceil(lo)
    upper_integer = math.floor(hi)
    assert 0 < lower_integer <= upper_integer

    sites = first_sites(3)
    assert [x[0] for x in sites] == [0, 7, 15]
    assert [fields(x)[3] for x in sites] == [16, 146, 295]

    modulus = 1 << 295
    assert hi < Decimal(modulus)
    base_mod = lower_mechanical(
        W,
        N,
        False,
        mod_bit(0, modulus),
        mod_bit(1, modulus),
        mod_id(modulus),
        mod_mul,
    )
    denominator_mod = (-pow(3, K, modulus)) % modulus
    inverse = pow(denominator_mod, -1, modulus)
    residues = []
    for mask in range(4):
        constant = base_mod.c
        for index in range(2):
            if mask >> index & 1:
                constant = (constant + repair_mod(sites[index], modulus)) % modulus
        residue = constant * inverse % modulus
        residues.append(residue)
        assert not (lower_integer <= residue <= upper_integer)
    assert len(set(residues)) == 4
    assert frozen["full_greedy_grammar"]["subset_count"] == "2^30790984112"
    print("independent X-8305 verification passed")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py results/canonical.json")
    verify(sys.argv[1])
