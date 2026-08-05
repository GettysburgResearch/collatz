#!/usr/bin/env python3
"""Independent verifier for X-8304; imports no author module."""
from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from pathlib import Path

K = 3_149_971_404_836
A = 4_992_586_555_009
B = K // 2
S = 2 * K - A
L = B - S
R = S - 4 * L
OMEGA = 7 * 2**16 * 3**9
PREC = 220


class Ball:
    def __init__(self, lo, hi=None):
        self.lo = Decimal(lo)
        self.hi = Decimal(lo if hi is None else hi)


def op(a, b, fn, rounding):
    with localcontext() as context:
        context.prec = PREC
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


def minus(x, y):
    return plus(x, Ball(-y.hi, -y.lo))


def quotient(x, y):
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
        context.prec = PREC
        context.rounding = ROUND_FLOOR
        lo = Decimal(a) / Decimal(b)
    with localcontext() as context:
        context.prec = PREC
        context.rounding = ROUND_CEILING
        hi = Decimal(a) / Decimal(b)
    return Ball(lo, hi)


@dataclass(frozen=True)
class Aff:
    r: Ball
    t: Ball


def aff_compose(a, b):
    # a acts first, b second
    return Aff(times(a.r, b.r), plus(times(b.r, a.t), b.t))


def aff_power(a, n):
    out = Aff(Ball(1), Ball(0))
    while n:
        if n & 1:
            out = aff_compose(out, a)
        a = aff_compose(a, a)
        n //= 2
    return out


def aff_letter(bit):
    run = 4 + bit
    den = 2 ** (16 + 3 * bit)
    return Aff(
        rational(9 ** (5 + bit), den),
        rational(48 * (9**run - 8**run), den),
    )


@dataclass(frozen=True)
class Mod:
    k: int
    a: int
    p: int
    q: int
    c: int
    modulus: int


def mod_compose(x, y):
    modulus = x.modulus
    assert modulus == y.modulus
    return Mod(
        x.k + y.k,
        x.a + y.a,
        x.p * y.p % modulus,
        x.q * y.q % modulus,
        (y.p * x.c + x.q * y.c) % modulus,
        modulus,
    )


def mod_power(x, n):
    out = Mod(0, 0, 1 % x.modulus, 1 % x.modulus, 0, x.modulus)
    while n:
        if n & 1:
            out = mod_compose(out, x)
        x = mod_compose(x, x)
        n //= 2
    return out


def mod_letter(bit, modulus):
    return Mod(
        2 * (5 + bit),
        16 + 3 * bit,
        pow(9, 5 + bit, modulus),
        pow(2, 16 + 3 * bit, modulus),
        48 * (9 ** (4 + bit) - 8 ** (4 + bit)) % modulus,
        modulus,
    )


def product(word_ones, word_length, upper, zero, one, identity, compose, power):
    if word_ones == 0:
        return power(zero, word_length)
    if word_ones == word_length:
        return power(one, word_length)
    quotient_value, remainder = divmod(word_length, word_ones)
    if upper:
        image_zero = compose(one, power(zero, quotient_value - 1))
        image_one = compose(one, power(zero, quotient_value))
        return product(
            remainder,
            word_ones,
            False,
            image_zero,
            image_one,
            identity,
            compose,
            power,
        )
    image_zero = compose(power(zero, quotient_value - 1), one)
    image_one = compose(power(zero, quotient_value), one)
    return product(
        remainder,
        word_ones,
        True,
        image_zero,
        image_one,
        identity,
        compose,
        power,
    )


def prefix(n):
    return n * R // L


def bit(n):
    return prefix(n + 1) - prefix(n)


def sites(count):
    result = []
    previous = -2
    n = 0
    while len(result) < count:
        x, y = bit(n), bit(n + 1)
        if x != y and n > previous + 1:
            result.append((n, x, y))
            previous = n
        n += 1
    return result


def site_fields(site):
    n, x, y = site
    sign = -1 if (x, y) == (0, 1) else 1
    dyadic = 16 * n + 3 * prefix(n)
    odd_pairs = 5 * n + prefix(n)
    return sign, dyadic, odd_pairs, 16 + dyadic


def verify(path: Path):
    frozen = json.loads(path.read_text())
    assert frozen["experiment_id"] == "X-8304"
    assert frozen["certificate"]["viable_prefixes"] == 0

    repair_sites = sites(80)
    assert [x[0] for x in repair_sites[:3]] == [0, 7, 15]
    valuations = [site_fields(x)[3] for x in repair_sites]
    assert valuations == sorted(set(valuations))
    assert valuations[2] == 295

    base = product(
        R,
        L,
        False,
        aff_letter(0),
        aff_letter(1),
        Aff(Ball(1), Ball(0)),
        aff_compose,
        aff_power,
    )
    den = minus(Ball(1), base.r)
    lower = base.t
    upper = base.t
    for repair in repair_sites:
        sign, dyadic, odd_pairs, _ = site_fields(repair)
        change = times(
            base.r,
            rational(OMEGA * 2**dyadic, 9 ** (odd_pairs + 11)),
        )
        if sign < 0:
            change = Ball(-change.hi, -change.lo)
        lower = plus(lower, Ball(min(Decimal(0), change.lo), min(Decimal(0), change.hi)))
        upper = plus(upper, Ball(max(Decimal(0), change.lo), max(Decimal(0), change.hi)))

    lo = quotient(lower, den).lo
    hi = quotient(upper, den).hi
    first_integer = math.ceil(lo)
    last_integer = math.floor(hi)
    assert first_integer <= last_integer

    modulus = 1 << 295
    assert hi < Decimal(modulus)
    base_mod = product(
        R,
        L,
        False,
        mod_letter(0, modulus),
        mod_letter(1, modulus),
        Mod(0, 0, 1, 1, 0, modulus),
        mod_compose,
        mod_power,
    )
    denominator = (-pow(3, K, modulus)) % modulus
    inverse = pow(denominator, -1, modulus)

    residues = []
    for mask in range(4):
        constant = base_mod.c
        for index in range(2):
            if mask >> index & 1:
                sign, dyadic, odd_pairs, _ = site_fields(repair_sites[index])
                delta = (
                    sign
                    * OMEGA
                    * pow(2, dyadic, modulus)
                    * pow(3, K - 2 * (odd_pairs + 11), modulus)
                ) % modulus
                constant = (constant + delta) % modulus
        residue = constant * inverse % modulus
        residues.append(residue)
        assert not (first_integer <= residue <= last_integer)

    assert len(set(residues)) == 4
    assert frozen["grammar"]["subset_count"] == str(2**80)
    assert frozen["certificate"]["future_delta_divisibility_bits"] == 295
    print("independent X-8304 verification passed")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py results/canonical.json")
    verify(Path(sys.argv[1]))
