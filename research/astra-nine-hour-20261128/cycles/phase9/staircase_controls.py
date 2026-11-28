"""Exact finite controls for rational threshold inversion and its two digit boxes."""
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase8"))
from grid_clock_controls import backward, eventual_clock, forward, require


def word(a, q):
    return [2**(((i+1)*a)//q-(i*a)//q) for i in range(q)]


def weights(radices):
    out = []
    prefix = 1
    for i, B in enumerate(radices):
        out.append(prefix*3**(len(radices)-1-i))
        prefix *= B
    return out, prefix


def trajectory(radices, x):
    values = [x]
    for B in radices:
        x = (3*x+B-1)//B
        values.append(x)
    return values


def greatest(radices):
    ws, power = weights(radices)
    D = power - 3**len(ws)
    require(D > 0, "positive denominator required")
    maximum = sum((B-1)*w for B, w in zip(radices, ws))
    current = maximum//D + 1
    while True:
        path = trajectory(radices, current)
        if path[-1] == current:
            return path
        require(path[-1] < current, "descending greatest-vector iteration")
        current = path[-1]


def check_inversion():
    n = 0
    for q in range(1, 66):
        for a in range((3**q).bit_length(), 2*q+1):
            if gcd(a, q) != 1:
                continue
            ratio = Fraction(a, q)
            path = greatest(word(a, q))
            U = path[0]
            sorted_ranks = [None]*q
            for t, x in enumerate(path[:-1]):
                sorted_ranks[t*a % q] = x
            require(sorted_ranks == sorted(sorted_ranks) and sorted_ranks[-1] <= 2*U,
                    "ordered greatest vector")
            require(4*U-3*path[-2] in (2, 3), "mandatory greatest-vector seam")
            require(eventual_clock(U-1, forward) >= ratio > eventual_clock(U, forward),
                    "exact threshold of arbitrary rational")
            n += 1
    for a, q, expected in ((8,5,41), (65,41,1079), (485,306,78663)):
        require(greatest(word(a, q))[0] == expected, "upper-convergent endpoint")
    print(f"{n} reduced rational thresholds, including missed clocks; three plateau endpoints.")


def digit_values(ws, radices):
    return {sum(w*r for w, r in zip(ws, digits))
            for digits in product(*(range(B) for B in radices))}


def check_apery():
    schedules = 0
    cases = 0
    for b in product(range(1, 4), repeat=4):
        B = [2**v for v in b]
        ws, power = weights(B)
        three = 3**len(b)
        D = power-three
        if D <= 0 or power > 512:
            continue
        A = digit_values(ws, B)
        T = digit_values(ws, [3]*len(b))
        require(len(A) == len({x % power for x in A}) == power, "binary uniqueness")
        require(len(T) == len({x % three for x in T}) == three, "ternary uniqueness")
        by_residue = {v % power: v for v in A}
        diff = [0]*D
        for n in range(max(A)+D+three+1):
            diff[n % D] += (n in A) - (n in T)
            m = n-three
            in_semigroup = m >= by_residue[m % power]
            require(diff[n % D] == in_semigroup, "every-class prefix interlacing")
            cases += 1
        require(all(z == 1 for z in diff), "one completed excess per class")
        ap_fixed = sorted(x//D for x in A if x % D == 0)
        actual = [x for x in range(max(A)//D+1) if trajectory(B, x)[-1] == x]
        require(actual == ap_fixed, "whole fixed-point spectrum")
        require(max(actual) == greatest(B)[0], "last class point")
        schedules += 1
    print(f"{schedules} nonmechanical or mechanical schedules, {cases} complete prefix checks.")


def check_pairs():
    for K, ratio, expected in ((35, Fraction(8,5), {35,46,61,40,53}),
                               (6, Fraction(5,3), {6,8,10})):
        z = K
        orbit = set()
        while z not in orbit:
            orbit.add(z)
            pred, _, _ = backward(K, z)
            require(forward(K, pred+1)[0] == z+1, "adjacent upper/lower orbit")
            z = pred
        require(z == K and orbit == expected, "adjacent orbit support")
        require(eventual_clock(K, forward) == eventual_clock(K+1, forward) == ratio,
                "retained clock despite destroyed upper orbit")
    print("Two true grid controls keep the clock after breaking the adjacent upper orbit.")


if __name__ == "__main__":
    check_inversion()
    check_apery()
    check_pairs()
