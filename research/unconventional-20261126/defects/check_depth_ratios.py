#!/usr/bin/env python3
"""Exact controls for the reset-depth ratio and full-duration statements."""

from functools import reduce
from math import gcd


def check(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def v2(n):
    check(n > 0, "positive valuation input")
    return (n & -n).bit_length() - 1


def actual_blocks(x, count):
    shifted = [x + 1]
    depths = []
    for _ in range(count):
        duration = 0
        while True:
            numerator = 3*x+1
            exponent = v2(numerator)
            x = numerator >> exponent
            duration += 1
            if exponent > 1:
                break
        check(duration == v2(shifted[-1]), "incorrect complete run")
        shifted.append(x + 1)
        depths.append(exponent-1)
    return shifted, depths


def word_residue(bits):
    # Lift by one input bit at a time, maintaining the scaled affine carry.
    start = 0
    current = 0
    multiplier = 1
    for d, odd in enumerate(bits):
        if (current % 2) != odd:
            start += 1 << d
            current += multiplier
        if odd:
            current = (3*current + 1) // 2
            multiplier *= 3
        else:
            current //= 2
    return start


def order_two(g, bound):
    if g == 1:
        return 1
    y = 1
    for e in range(1, bound + 1):
        y = 2*y % g
        if y == 1:
            return e
    raise ArithmeticError("order failed")


def verify_split(shifted, depths):
    runs = [v2(y) for y in shifted]
    w = [y >> a for y, a in zip(shifted, runs)]
    g = reduce(gcd, w)
    b_star = reduce(gcd, depths)
    check(g == gcd(shifted[0], (1 << b_star)-1), "exact gcd failed")
    order = order_two(g, b_star)
    check(b_star % order == 0, "order does not divide common depth")
    T = sum(runs[:-1])
    B = sum(depths)
    D = T + B
    root = 3**T * (w[0] // g)
    for e in set((b_star, order)):
        factor = ((1 << e)-1) // g
        coords = [root]
        Dprefix = Tprefix = 0
        for j, (t, b) in enumerate(zip(runs, depths)):
            head = 3 ** (T-Tprefix-t) << (Dprefix+t-runs[0])
            coords.extend((head * factor) << h for h in range(0, b, e))
            Dprefix += t+b
            Tprefix += t
        check(min(coords) > 0 and coords[0] % 2, "sum degeneracy")
        check(len(coords) == 1 + B // e, "wrong dimension")
        check(sum(coords)*g == shifted[-1] << (D-runs[0]), "split sum mismatch")
        check(v2(sum(coords)) == D-runs[0]+runs[-1], "lost terminal dyadic valuation")
    return g, order, runs


def construct(profile, b, runs, terminal):
    check(reduce(gcd, profile) == 1 and b % 2 == 1 and b >= 3, "bad CRT family")
    depths = [m*b for m in profile]
    bits = []
    for t, depth in zip(runs, depths):
        bits.extend([1]*t+[0]*depth)
    bits.extend([1]*terminal+[0])
    binary = 1 << len(bits)
    H = (1 << b)-1
    residue = word_residue(bits)
    root = residue + binary*(((-1-residue)*pow(binary, -1, H)) % H)
    root += binary*H*((-root*pow(binary*H, -1, 3)) % 3)
    x = root + 3*binary*H
    shifted, actual_depths = actual_blocks(x, len(depths))
    g, order, actual_runs = verify_split(shifted, actual_depths)
    check(x % 6 == 3 and actual_runs == [*runs, terminal], "terminal or first durations")
    check(actual_depths == depths and g == H and order == b, "CRT depth or gcd")
    return x.bit_length(), (shifted[-1]-1).bit_length(), g.bit_length()


def main():
    ordinary = 0
    nontrivial_orders = 0
    for x in range(1, 20000, 2):
        for r in (1, 2, 3):
            shifted, depths = actual_blocks(x, r)
            g, order, _ = verify_split(shifted, depths)
            if g > 1 and order < reduce(gcd, depths):
                nontrivial_orders += 1
            ordinary += 1
    crt = 0
    for profile in ((1,), (1,2), (2,1), (2,3), (2,4,3), (1,7)):
        for b in (3, 7, 13, 31):
            for u in (1, 5, 2*b):
                construct(profile, b, [k*b+2 for k in profile], u)
                crt += 1
    print("direct ordinary windows:", ordinary)
    print("nontrivial gcd with order strictly below common depth:", nontrivial_orders)
    print("exact CRT trajectories with prescribed terminal valuation:", crt)
    print("example (1:2), b=31, initial odd runs 20,55, terminal valuation 14; bit lengths:",
          construct((1,2), 31, (20,55), 14))


if __name__ == "__main__":
    main()
