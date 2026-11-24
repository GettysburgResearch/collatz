#!/usr/bin/env python3
"""Exact finite controls for the dyadic companion, separation bounds and ordinary lifts."""

from fractions import Fraction
from functools import cache
import json
from math import gcd


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def rational_step(x):
    require(x.denominator % 2 == 1, "binary parity requires odd denominator")
    return x / 2 if x.numerator % 2 == 0 else (3 * x + 1) / 2


def v2(x):
    require(x != 0, "v2 of zero is not finite")
    a = abs(x)
    return (a & -a).bit_length() - 1


def dyadic_residue(x, bits):
    modulus = 2**bits
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


@cache
def convergent_companion(n):
    require(n > 0, "positive ordinary input required")
    x, word = n, []
    for _ in range(20000):
        if x == 1:
            break
        word.append(x % 2)
        x = step(x)
    else:
        raise ValueError(f"finite convergence control timed out at {n}")
    d = Fraction(9)
    for e in reversed(word):
        d = e + Fraction(2 ** (1 + e), 3) * d
    return d


def companion_mod(n, bits):
    x = n
    value, weight, exponent = 0, 1, 0
    modulus = 2**bits
    third = pow(3, -1, modulus)
    while exponent < bits:
        e = x % 2
        value = (value + e * weight) % modulus
        weight = weight * 2 ** (1 + e) * third % modulus
        exponent += 1 + e
        x = step(x)
    return value


def aux_positive(w):
    if w % 2 == 0:
        return 3 * w // 2
    require(w % 4 == 1, "forbidden integral companion class")
    return (3 * w + 1) // 4


def main():
    theta = Fraction(61**2 * 193**3, 20**2 * 64**3 * 256)
    require(theta == Fraction(26750481097, 26843545600), "odd contraction constant")
    require(Fraction(27, 32) < theta < 1, "both branches contract")
    require(2 * theta**256 < 1, "contraction over 256 steps")
    require(256**16 > 2 * 243**16, "physical growth over sixteen steps")
    require(3**31 < 2**50 and 12 * 4**31 < 2**20 * 3**31, "base rational heights")

    delays = []
    for start in range(2, 64):
        w = start
        for j in range(18):
            if w % 4 == 3:
                delays.append(j)
                break
            w = aux_positive(w)
        else:
            raise ValueError(f"small companion {start} survived all 18 tests")
    require(max(delays) == 17, "sharp represented prefix delay")

    separation_cases = 0
    for n in range(1, 129):
        d = convergent_companion(n)
        require(dyadic_residue(d, 96) == companion_mod(n, 96), "independent dyadic digits")
        require(d == n % 2 + Fraction(2 ** (1 + n % 2), 3) * convergent_companion(step(n)),
                "actual discounted recurrence")
        for a in range(-12, 13):
            for h in range(5):
                trial = Fraction(a, 3**h)
                diff = d - trial
                if diff:
                    size = 5 + h + n.bit_length() + (abs(a) + 1).bit_length()
                    require(v2(diff.numerator) <= 10**6 * size, "separation control")
                    separation_cases += 1

    p, k, m = 17, 27, 2
    modulus = m * 3**p
    center = Fraction(3**p - 2**p, 2**k - 3**p)
    require(gcd(center.denominator, modulus) == 1, "rational center not integral modulo control")
    y = center.numerator * pow(center.denominator, -1, modulus) % modulus
    while y <= center:
        y += modulus
    x = center + Fraction(2**k, 3**p) * (y - center)
    require(x.denominator == 1, "ordinary pullback lost integrality")
    x = int(x)
    z = x
    for i in range(k):
        require(z % 2 == int(i < p), "physical ordinary word")
        z = step(z)
    require(z == y and x % m == y % m, "endpoint and common residue")
    require(1 < Fraction(x, y) < Fraction(2**k, 3**p), "height window")
    beta = Fraction(2**(k + p), 3**k)
    sx, sy = 3 + 2 * convergent_companion(x), 3 + 2 * convergent_companion(y)
    require(sx > beta * sy, "strict partial series ratio")
    require(beta > 2, "offer a nontrivial exact fixture")

    k_neighbor = 64
    n = 2**k_neighbor - 1
    left = 3 + 2 * convergent_companion(n)
    right = 3 + 2 * convergent_companion(n + 1)
    require(left >= Fraction(4, 3)**k_neighbor, "left series lower bound")
    require(right == 3 + 18 * Fraction(2, 3)**k_neighbor, "right dyadic ray")

    z = Fraction(19, 5)
    dsum, factor = Fraction(0), Fraction(1)
    for _ in range(5):
        e = z.numerator % 2
        dsum += e * factor
        factor *= Fraction(2**(1 + e), 3)
        z = rational_step(z)
    require(z == Fraction(19, 5) and factor == Fraction(256, 243), "rational control cycle")
    dcycle = dsum / (1 - factor)
    require(dcycle < 0 and dcycle.denominator % 3 != 0 and dcycle.denominator > 1,
            "denominator-one scope of integral exclusion")

    print(json.dumps({
        "physical_controls": 128,
        "dyadic_bits_each": 96,
        "different_triadic_trials": separation_cases,
        "integral_companions_checked": len(delays),
        "maximum_illegality_clock": max(delays),
        "same_residue_convergent_pair": [x, y],
        "physical_word": [p, k - p],
        "term_multiplier": str(beta),
        "adjacent_convergent_pair": [n, n + 1],
        "rational_cycle_companion": str(dcycle),
    }, indent=2))


if __name__ == "__main__":
    main()
