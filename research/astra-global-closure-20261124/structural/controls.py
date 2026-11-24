"""Reproduce the finite controls for the two negative-cycle shadows."""
from fractions import Fraction
from collections import defaultdict
from hashlib import sha256
from math import prod


def check(condition, message):
    if not condition:
        raise ValueError(message)


def T(x):
    return (3*x+1)//2 if x % 2 else x//2


def S(x):
    return (3*x-1)//2 if x % 2 else x//2


CYCLE = (17, 25, 37, 55, 82, 41, 61, 91, 136, 68, 34)


def bounded_controls():
    check(tuple(map(S, CYCLE)) == CYCLE[1:] + CYCLE[:1], "cycle")
    rows = defaultdict(list)
    for b in range(1, 137):
        x = b
        prev = x
        for _ in range(28):
            if x in CYCLE or x in (1, 5):
                break
            prev, x = x, S(x)
        check(x in CYCLE or x in (1, 5), "negative classification")
        if x in CYCLE:
            check(b >= 17, "negative basin minimum")
            if b not in CYCLE and b % 3 == 1:
                rows[(prev, x)].append(b)
    check(dict(rows) == {(23, 34): [31, 46, 124], (122, 61): [49, 73, 109],
                         (50, 25): [67, 100]}, "entrance branches")
    fwd = [25, 37, 55, 82, 61, 91, 136]
    for a in range(1, 5):
        factors = lambda xs: prod(Fraction(2*x+1, 2*x) for x in xs[:a])
        check(factors(fwd) > factors([31, 34, 46, 124]), "prefix product")
    positive = {}
    for z in [0, 1]:
        cells = set()
        for y in range(1, 17+z):
            x, odds = y, 0
            for t in range(24):
                check(3**odds < 16*2**t, "finite multiplier")
                if t == 23:
                    check(x in (1, 2), "tail")
                for m in range(1, 4):
                    b = (17+z)*2**m-x
                    if b >= 17 and 3**odds >= 2**(m+t):
                        cells.add((m, b))
                odds += x % 2
                x = T(x)
        positive[z] = sorted(cells)
    check(positive == {0: [(1, 17), (1, 26)], 1: [(1, 19), (1, 28)]},
          "late shadow classification")
    print("negative first-entrance rows", dict(rows))
    print("late shadow supersets", positive)


def menu(depth):
    mod = 2**depth
    inverse_three = pow(3, -1, mod)
    z = 7
    successes = []
    for d in range(mod//4):
        starts = [z-b for b in (17, 1, 5, 7, 10)]
        weights = [0]*5
        for h in range(1, depth+1):
            for j, x in enumerate(starts):
                weights[j] += x % 2
                starts[j] = T(x)
            if any((x, w) == (starts[0], weights[0])
                   for x, w in zip(starts[1:], weights[1:])):
                successes.append(d)
                break
        z = (z*inverse_three) % mod
    return successes


def power_certificate(k, L):
    """Produce and validate the exponent, without expanding the huge number 2**e."""
    p, b = 33*k, 22*k-1
    steps = b+L
    M = 3**steps
    target = (18*3**b*pow(2**p, -1, M)-7) % M
    e = int(target % 3 == 2)
    value, increment, unit, checkmod = 2**e, 2, 4, 3
    for _ in range(1, steps):
        checkmod *= 3
        for _ in range(3):
            if value % checkmod == target % checkmod:
                break
            value = value*unit % M
            e += increment
        else:
            raise ValueError("ternary logarithm lift")
        increment *= 3
        unit = pow(unit, 3, M)
    check(pow(2, e, M) == target, "prescribed member power")
    check(((pow(2, e, M)+7)//(3**b)*2**p-18) % (3**L) == 0, "unit source")
    check((7*pow(3, 1-k, 1024)-17) % 1024 == 52, "class-148 partner")
    print("symbolic ordinary witness", {"k": k, "L": L, "exponent_bits": e.bit_length(),
                                        "exponent_decimal_sha256":
                                        sha256(str(e).encode("ascii")).hexdigest()})
    return e


if __name__ == "__main__":
    bounded_controls()
    check(menu(8) == [47], "eight-step class 48")
    hits = menu(16)
    check(len(hits) == 3736 and 147 in hits, "16-bit menu")
    print("equal-count partner successes at depth 16:", len(hits), "of", 2**14)
    power_certificate(148, 3)
    power_certificate(148, 33*148)
