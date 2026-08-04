#!/usr/bin/env python3
"""Independent checker for X-8612; imports no authoring module."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path


X = 2**71 + 1
A, B = 2_733_776_749, 6_586_818_670
C, D = 27_172_759_629, 65_470_613_321
P, Q = A + C, B + D


def log_bounds(z: Fraction, n: int) -> tuple[Fraction, Fraction]:
    # Independently sum powers directly rather than carrying z^(2j+1).
    terms = [2 * z ** (2 * j + 1) / (2 * j + 1) for j in range(n)]
    lower = sum(terms, Fraction(0))
    upper = lower + 2 * z ** (2 * n + 1) / (
        (2 * n + 1) * (1 - z * z)
    )
    return lower, upper


def quotient_bounds(
    nlo: Fraction, nhi: Fraction, dlo: Fraction, dhi: Fraction
) -> tuple[Fraction, Fraction]:
    return nlo / dhi, nhi / dlo


def phi(n: int) -> int:
    return sum(gcd(j, n) == 1 for j in range(1, n + 1))


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def ordered_count(s: int, w: int) -> int:
    if w < 0:
        return 0
    # Choose each high valuation through its weight a-1>=2; weight zero is a=1.
    states = {(0, 0): 1}
    for i in range(s):
        nxt = {}
        for (_, used), count in states.items():
            for weight in (0, *range(2, w - used + 1)):
                key = (i + 1, used + weight)
                nxt[key] = nxt.get(key, 0) + count
        states = nxt
    return states.get((s, w), 0)


def burnside(s: int, w: int) -> int:
    numerator = 0
    for r in divisors(gcd(s, w)):
        numerator += phi(r) * ordered_count(s // r, w // r)
    assert numerator % s == 0
    return numerator // s


def rotations(word: tuple[int, ...]):
    for j in range(len(word)):
        yield word[j:] + word[:j]


def brute_necklaces(s: int, w: int) -> int:
    alphabet = (1, *range(3, w + 2))
    representatives = {
        min(rotations(word))
        for word in product(alphabet, repeat=s)
        if sum(x - 1 for x in word) == w
    }
    return len(representatives)


def independent_normal_form_check() -> int:
    checked = 0
    for length in range(1, 8):
        for word in product(range(1, 7), repeat=length):
            chi = 2 * length - sum(word)
            if chi <= 0:
                continue
            ones = [j for j, a in enumerate(word) if a == 1]
            highs = [(j, a) for j, a in enumerate(word) if a >= 3]
            excess = sum(a - 2 for _, a in highs)
            assert len(ones) - excess == chi

            base = list(word)
            selected = ones[:excess]
            for j, _ in highs:
                base[j] = 2
            for j in selected:
                base[j] = 2
            assert set(base) <= {1, 2}
            assert sum(base) == sum(word)
            assert base.count(1) == chi

            support = sum(a != 2 for a in word)
            omega = support - chi
            assert omega == sum(a - 1 for a in word if a != 2)
            assert sum(x != y for x, y in zip(word, base)) == omega
            checked += 1
    return checked


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("canonical", type=Path)
    args = parser.parse_args()
    data = json.loads(args.canonical.read_text())

    ln2 = log_bounds(Fraction(1, 3), 160)
    ln43 = log_bounds(Fraction(1, 7), 90)
    lne = log_bounds(Fraction(1, 6 * X + 1), 3)

    alpha = quotient_bounds(ln43[0], ln43[1], ln2[0], ln2[1])
    beta = quotient_bounds(
        ln43[0] - lne[1],
        ln43[1] - lne[0],
        ln2[0],
        ln2[1],
    )

    low = Fraction(A, B)
    high = Fraction(C, D)
    med = Fraction(P, Q)

    assert C * B - A * D == 1
    assert low < beta[0] < beta[1] < med
    assert med < alpha[0] < alpha[1] < high
    assert Fraction(P - 1, Q) < beta[0]

    # Standard Farey identity: for any a/b < p/q < c/d with bc-ad=1,
    # q=d(pb-aq)+b(cq-pd)>=b+d.
    assert Q == B + D
    assert P == A + C
    assert data["cycle_odd_state_length_floor"] == Q
    assert data["cycle_signed_charge_floor"] == P
    assert data["cycle_non2_support_floor"] == P
    assert data["verified_exponent"] == 71
    assert data["stern_brocot_iterations"] == 136

    normal_cases = independent_normal_form_check()
    assert data["normal_form_cases"] == normal_cases

    cases = 0
    for s in range(1, 8):
        for w in range(11):
            assert burnside(s, w) == brute_necklaces(s, w)
            cases += 1
    assert data["necklace_formula_cases"] == cases

    print("independent charge-cylinder, packet-normal-form, and Burnside checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
