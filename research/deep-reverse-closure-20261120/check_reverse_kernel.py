#!/usr/bin/env python3
"""Exact affine replays for K1--K3; not a proof of the open kernel closures."""
from fractions import Fraction
import json


def need(ok, message):
    if not ok:
        raise ValueError(message)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, a):
    return (a * x[0], a * x[1])


def aff(a, b):
    return (Fraction(a), Fraction(b))


def native(x):
    need(x[0].denominator == x[1].denominator == 1, "nonintegral affine state")
    need(x[0] >= 0 and x[1] > 0, "nonpositive source progression")
    need(x[0] % 2 == 0, "parity is not constant across the progression")
    odd = int(x[1] % 2)
    return (mul(add(mul(x, 3), aff(0, 1)), Fraction(1, 2)) if odd
            else mul(x, Fraction(1, 2))), odd


def path(x, clocks):
    values = [x]
    odds = 0
    for _ in range(clocks):
        x, odd = native(x)
        values.append(x)
        odds += odd
    return x, odds, values


def integer_step(n):
    need(isinstance(n, int) and n > 0, "invalid ordinary state")
    return (3*n+1)//2 if n % 2 else n//2


def integer_path(n, clocks):
    values = [n]
    for _ in range(clocks):
        n = integer_step(n)
        values.append(n)
    return values


def integral(x):
    need(x.denominator == 1, "nonintegral coefficient")
    return int(x)


def generic(c):
    need(c == 1 or c >= 3, "forbidden fourth valuation")
    if c == 1:
        z0 = 83
    else:
        z0 = pow(pow(2, c-2, 81), -1, 81)
        if z0 % 2 == 0:
            z0 += 81
    z = aff(162, z0)
    X = mul(add(mul(z, 2**(c+6)), aff(0, -175)), Fraction(1, 81))
    Y = mul(add(X, aff(0, 1)), Fraction(1, 2))
    k = mul(add(X, aff(0, -1)), Fraction(1, 128))
    for value in X + Y + k:
        integral(value)
    need((k[0] % 2 == 0 and k[1] % 2 == 1) if c == 1
         else (k[0] % 4 == 0 and k[1] % 4 == 2), "wrong index class")
    upper, odd_count, upper_values = path(X, c+6)
    need(upper == z and odd_count == 4, "upper certificate peel failed")
    need(all(v[1] > 1 for v in upper_values[:-1]), "upper prefix reaches 1 early")
    if c == 1:
        end, _, _ = path(Y, 7)
        target = mul(add(z, aff(0, 1)), Fraction(1, 6))
    elif c % 2 == 0:
        r = (c-4)//2
        end, _, _ = path(Y, c+6)
        target, _ = native(mul(z, 3**r))
    else:
        r = (c-3)//2
        end, _, _ = path(Y, c+4)
        target = add(mul(z, 2*3**r), aff(0, 1))
    need(end == target, "residual endpoint identity failed")
    return sum(len(str(integral(v))) for v in end), len(upper_values)


def rank_five():
    rows = [(1, 70, 32), (3, 22, 10), (4, 68, None), (5, 118, None)]
    need(pow(2, 162, 243) == 1, "wrong multiplicative period")
    need(all(pow(2, d, 243) != 1 for d in (1, 2, 3, 6, 9, 18, 27, 54, 81)),
         "multiplicative period is not minimal")
    tested = 0
    for c, residue, power_start in rows:
        residue_set = [a for a in range(1, 163)
                       if (pow(2, a+c+6, 243)-525-pow(2, c+6, 243)) % 243 == 0]
        need(residue_set == [residue], "wrong final-gap progression")
        for j in range(4):
            a = residue + 162*j
            z = (2**a-1)//3
            X = (2**(a+c+6)-525-2**(c+6))//243
            need(243*X == 2**(a+c+6)-525-2**(c+6), "upper integrality")
            Y = (X+1)//2
            need(X % 128 == 1 and ((X-1)//128) % 4 != 0, "upper domain")
            upper = integer_path(X, a+c+6)
            need(upper[-1] == 1 and 1 not in upper[:-1], "upper first hit")
            need(sum(v % 2 for v in upper[:-1]) == 5, "upper rank")
            if c in (1, 3):
                clock = 10 if c == 1 else 8
                h = a-4 if c == 1 else a
                first = integer_path(Y, clock)
                need(first[-1] == 2**h+1 and 1 not in first, "binary lift checkpoint")
                shadow = integer_path(first[-1], h+1)
                power = power_start + 81*j
                need(shadow[-1] == integer_step(3**power), "pure-power merger")
                need(all(v > 1 for v in shadow), "early shadow hit")
            elif c == 4:
                lower = integer_path(Y, a+9)
                need(lower[8] == 2**(a+1), "power-of-two checkpoint")
                need(lower[-1] == 1 and 1 not in lower[:-1], "lower first hit")
                need(sum(v % 2 for v in lower[:-1]) == 5, "lower rank")
            else:
                lower = integer_path(Y, 9)
                need(lower[-1] == 2**(a+1)-1, "Mersenne checkpoint")
            tested += 1
    return tested


def corruption_controls():
    rejected = 0
    for bad in [aff(1, 3), aff(2, -1), aff(Fraction(1, 3), 1)]:
        try:
            native(bad)
        except ValueError:
            rejected += 1
    try:
        generic(2)
    except ValueError:
        rejected += 1
    need(rejected == 4, "invalid fixture accepted")
    return rejected


def main():
    cells = steps = checksum = 0
    for c in [1, *range(3, 163)]:
        digest, nsteps = generic(c)
        cells += 1
        steps += nsteps
        checksum += digest
    report = {
        "scope": "exact affine family identities and finite rank-five controls; open kernel closures unproved",
        "source_pr": 146,
        "source_head": "e238c63a5d57f96bb063b7472498d1977df51951",
        "affine_cells": cells,
        "upper_states_checked": steps,
        "endpoint_digit_checksum": checksum,
        "rank_five_ordinary_examples": rank_five(),
        "invalid_fixtures_rejected": corruption_controls(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
