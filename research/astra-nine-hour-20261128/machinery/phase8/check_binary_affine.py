#!/usr/bin/env python3
"""Exact finite tests for tilted dyadic affine changes and joint word ranks."""

from fractions import Fraction as F
from itertools import product
from math import floor


def require(ok, message):
    if not ok:
        raise ValueError(message)


def valuation(x, p=2):
    require(x != 0, "zero valuation")
    v = 0
    n, d = abs(x.numerator), x.denominator
    while n % p == 0:
        v += 1
        n //= p
    while d % p == 0:
        v -= 1
        d //= p
    return v


def residue(x, modulus):
    x = F(x)
    return (x.numerator * pow(x.denominator, -1, modulus)) % modulus


def word(x, t):
    x = F(x)
    count = 0
    offset = 0
    for j in range(t):
        odd = residue(x, 2)
        x = ((3 * x + 1) if odd else x) / 2
        count += odd
        offset = (3 * offset + 2**j) if odd else offset
    return count, offset, x


def weight(theta, n, count):
    return theta**count * (1 - theta)**(n - count)


def affine_fixtures():
    theta = F(2, 3)
    q = 1 - theta
    cases = [(F(2), F(1)), (F(1, 2), F(1, 2)), (F(3), F(1, 3)),
             (F(1, 3), F(1)), (F(1), F(1, 9)), (F(6), F(-1)),
             (F(1, 6), F(-1, 2)), (F(-1), F(0)), (F(5), F(0)),
             (F(1), F(1, 5)), (F(1, 2), F(1, 4)), (F(6), F(1, 2))]
    ratios = 0
    for index, (a, b) in enumerate(cases):
        r = valuation(a)
        found = False
        for n in range(max(0, -r), 10):
            masses = F(0)
            for x in range(2**n):
                gx = a*x+b
                if gx and valuation(gx) < 0:
                    continue
                count, du, y = word(x, n)
                other, dv, z = word(gx, n+r)
                w = weight(theta, n, count)
                sig = weight(theta, n+r, other)
                masses += sig
                require(sig / w == q**r*(theta/q)**(other-count), "cylinder ratio")
                ratios += 1
                if y == z and a*3**other == F(2)**r*3**count:
                    found = True
                    require(3**other*b == F(2)**r*du-dv, "cleared offset")
                    for j in (1, 3):
                        y2 = word(x+2**n*j, n)
                        z2 = word(gx+a*2**n*j, n+r)
                        require(y2[2] == z2[2] and (y2[0], z2[0]) == (count, other),
                                "whole dyadic ball did not match")
            if r >= 0:
                expected = F(0) if b and valuation(b)<0 else weight(theta, r, word(b, r)[0])
            else:
                expected = F(0) if b and valuation(b)<r else F(1)
            require(masses == expected, "pushforward support mass")
        require(found == (index < 7), f"finite affine fixture {a}, {b}, found {found}")
    return len(cases), ratios


def lattice_fixtures():
    rank_cases = collisions = 0
    for n in range(1, 6):
        groups = {}
        for w in product(range(1, 5), repeat=n):
            total = sum(w)
            beta = F(0)
            for e in reversed(w):
                beta = (1 + 3*beta)/2**e
            lam = F(3**n, 2**total)
            cell = (total, residue(beta, 3**n))
            groups.setdefault(cell, []).append((beta, lam))
        for rows in groups.values():
            rows.sort()
            for (b1, lam), (b2, _) in zip(rows, rows[1:]):
                require(b2 > b1 and ((b2-b1)/lam).denominator == 1, "fixed-total spacing")
                collisions += 1
            for beta, lam in rows:
                for tail in (F(0), F(5, 7), F(2), F(137, 11)):
                    real = beta + lam*tail
                    recovered = [c for c, _ in rows if floor((real-c)/lam) == floor(tail)]
                    require(recovered == [beta], "rank did not identify actual offset")
                    rank_cases += 1
    return rank_cases, collisions


if __name__ == '__main__':
    cases, ratios = affine_fixtures()
    ranks, collisions = lattice_fixtures()
    print(f"PASS {cases} affine maps, {ratios} exact likelihoods, {ranks} joint ranks, "
          f"{collisions} same-total/same-trit neighbors")
