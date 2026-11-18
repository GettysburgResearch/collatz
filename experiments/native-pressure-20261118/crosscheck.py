"""Independent full-affine-cycle probability bounds and finite native law replay."""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import argparse

BITS = 168
SCALE = 1 << BITS


def ceildiv(a, b):
    return -(-a // b)


def refine(lo, hi):
    m = len(lo)
    # L:r -> 4r+1 is a single 3^j-cycle. Check this directly at every
    # used modulus and enclose its resolvent by iterating backwards.
    order = [0]
    n = 1 % m
    while n:
        order.append(n)
        n = (4 * n + 1) % m
    if len(order) != m:
        raise ValueError("wrong affine period")
    values_lo = [0] * m
    values_hi = [0] * m
    low = 0
    high = ceildiv(4 * max(hi), 3)
    passes = max(2, (BITS + m - 1) // m + 2)
    for _ in range(passes):
        for i in reversed(order):
            low = lo[i] + (low // 4)
            high = hi[i] + ceildiv(high, 4)
            values_lo[i], values_hi[i] = low, high
    new_lo = [0] * (3 * m)
    new_hi = [0] * (3 * m)
    for k in range(m):
        for r, index, denom in ((3*k+1, (4*k+1) % m, 4),
                                (3*k+2, (2*k+1) % m, 2)):
            new_lo[r] = values_lo[index] // denom
            new_hi[r] = ceildiv(values_hi[index], denom)
    return new_lo, new_hi


def collision_control(receipt):
    lower = upper = [SCALE]
    scale = 1 << receipt["fraction_bits"]
    rows = receipt["ternary_collision_intervals"]
    for j, (a, b) in enumerate(rows):
        m = len(lower)
        if a * SCALE**2 > scale * m * sum(x*x for x in lower):
            raise ArithmeticError("ternary lower bound not contained")
        if b * SCALE**2 < scale * m * sum(x*x for x in upper):
            raise ArithmeticError("ternary upper bound not contained")
        if j + 1 < len(rows):
            lower, upper = refine(lower, upper)


def check_lifts(receipt, limit=16, max_odds=5):
    observed = Counter()
    for k in range(limit + 1):
        endpoints = Counter()
        for n in range(1 << k, 2 << k):
            p = 0
            for _ in range(k):
                if n & 1:
                    p += 1
                    n = 3*n + 1
                n //= 2
            endpoints[n] += 1
            if p <= max_odds:
                observed[p, n % 3 ** p] += 1 << (limit - k)
        energy = 0
        for y, multiplicity in endpoints.items():
            band = 1
            while 3*band <= y:
                band *= 3
            energy += band * multiplicity**2
        if energy != receipt["ordinary_collision_numerators_denominator_4k"][k]:
            raise ValueError("ordinary collision mismatch")
    expected = Counter({(0, 0): (1 << (limit + 1)) - 1})
    for p in range(1, max_odds + 1):
        modulus = 3 ** p
        for total in range(p, limit + 1):
            # Split at the p-1 interior locations to get every positive
            # valuation vector. Evaluate the independent suffix-sum formula.
            for cuts in combinations(range(1, total), p-1):
                starts = (0, *cuts)
                residue = sum(3 ** (p-i-1) * pow(2, -(total-start), modulus)
                              for i, start in enumerate(starts)) % modulus
                expected[p, residue] += (1 << (limit-total+1)) - 1
    if observed != expected:
        raise ArithmeticError("ordinary input and truncated exponent law disagree")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", type=Path)
    args = parser.parse_args()
    receipt = json.loads(args.receipt.read_text())
    collision_control(receipt)
    check_lifts(receipt)
    print("Verified ternary collision bounds and ordinary collision/lift laws through shell 16")
