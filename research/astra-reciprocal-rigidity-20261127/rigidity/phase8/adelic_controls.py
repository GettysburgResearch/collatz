"""Exact finite controls for stationary CRT comparison and an expanding periodic class."""

from collections import Counter
from fractions import Fraction
import json


def require(truth, message):
    if not truth:
        raise RuntimeError(message)


def step(x):
    return x // 2 if x % 2 == 0 else (3*x+1) // 2


def parities(x, length):
    bits = []
    for _ in range(length):
        bits.append(x % 2)
        x = step(x)
    return bits


def ternary_distribution(depth, bias):
    """Push an independent geometric gap through the exact 3-adic recursion."""
    distribution = {0: Fraction(1)}
    for r in range(1, depth+1):
        modulus = 3**r
        period = 2 * 3**(r-1)
        next_distribution = Counter()
        for e in range(1, period+1):
            gap_mass = bias*(1-bias)**(e-1) / (1-(1-bias)**period)
            inverse = pow(2, -e, modulus)
            for z, mass in distribution.items():
                next_distribution[inverse * (1+3*z) % modulus] += gap_mass*mass
        require(sum(next_distribution.values()) == 1, "ternary mass")
        require(max(next_distribution.values()) <= (1/(2-bias))**r, "small ball")
        mixed = Counter()
        for z, mass in next_distribution.items():
            mixed[z*pow(2,-1,modulus) % modulus] += (1-bias)*mass
            mixed[(3*z+1)*pow(2,-1,modulus) % modulus] += bias*mass
        require(mixed == next_distribution, "ternary stationarity")
        distribution = next_distribution
    return distribution


def mixed_test(k, j, r, bias):
    ternary = ternary_distribution(r, bias)
    modulus = 2**k * 3**r * 5
    site_mass = [Counter() for _ in range(j+1)]
    joint = [Counter() for _ in range(j+1)]
    support = 0
    for n in range(modulus, 2*modulus):
        if n % (3**r) not in ternary:
            continue
        bits = parities(n, k)
        odds = sum(bits[:j+r])
        mass = (bias**odds * (1-bias)**(j+r-odds)
                * Fraction(1, 2**(k-j-r)) * ternary[n % 3**r] / 5)
        y = n
        support += 1
        for t in range(j+1):
            joint[t][(y % 2**r, y % 3**r, y % 5)] += mass
            site_mass[t][y] += mass
            y = step(y)
    for t in range(j+1):
        require(sum(joint[t].values()) == 1, "ordinary CRT sample normalization")
        require(joint[t] == joint[0], "ordinary coarse joint law changed")
        require(max(site_mass[t].values()) <= Fraction(1, 2**(k-j-r)), "fair tail")
    require(len({tuple(parities(n,k)) for n in range(2**k)}) == 2**k, "word bijection")
    return {
        "k": k, "j": j, "r": r, "actual_sources": support,
        "joint_cells": len(joint[0]),
        "maximum_site_masses": [str(max(m.values())) for m in site_mass],
        "fair_tail_pointwise_bound": str(Fraction(1,2**(k-j-r))),
    }


def periodic_test():
    # The expanding physical word 1110 fixes -19/11.
    h, r = 4, 3
    precision = 2**(r+h) * 3**r * 5**r
    fixed = -19 * pow(11,-1,precision) % precision
    for t in range(1, 513):
        n = t*precision + fixed
        require(parities(n,h) == [1,1,1,0], "periodic physical word")
        y = n
        for _ in range(h):
            y = step(y)
        require(16*y == 27*n+19 and y>n, "expanding ordinary affine return")
        require((y-n) % (2**r*3**r*5**r) == 0, "same finite-place cell")
    return {"word": "1110", "rational_root": "-19/11", "integer_returns": 512}


def main():
    report = {
        "bias": "3/4",
        "stationary_ternary_cells_by_depth": [
            len(ternary_distribution(d,Fraction(3,4))) for d in range(1,6)],
        "ordinary_samples": [
            mixed_test(k,j,r,Fraction(3,4)) for k,j,r in [(7,2,2),(8,3,2)]],
        "periodic_class": periodic_test(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
