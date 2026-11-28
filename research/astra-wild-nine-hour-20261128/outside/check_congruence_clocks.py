"""Finite exact controls for the shortcut congruence and denominator results."""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import prod


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def affine(word):
    slope, offset, denominator = 1, 0, 1
    for odd in word:
        if odd:
            slope, offset = 3 * slope, 3 * offset + denominator
        denominator *= 2
    return slope, offset, denominator


def first_power(p, threshold):
    value = 1
    while value < threshold:
        value *= p
    return value


def check_prefixes():
    counts = Counter()
    for n in range(1, 42):
        for length in range(1, 8):
            for word in product(range(2), repeat=length):
                a, c, d = affine(word)
                y = Fraction(a * n + c, d)
                physical = n
                prefix = 0
                for letter in word:
                    if physical % 2 != letter:
                        break
                    physical = step(physical)
                    prefix += 1
                require(y.denominator == 2 ** (length - prefix), (n, word, y))
                if prefix == length:
                    require(y == physical, (n, word))
                    counts["integral outputs"] += 1
                counts["prefixes"] += 1
    for j, k in product(range(1, 15), repeat=2):
        word = (1, 0) * j + (0,) + (1, 0) * k
        a, c, d = affine(word)
        diff = Fraction(a + c, d) - 1
        require(diff == Fraction(-(3**k), 2 ** (2*k+1)), (j, k, diff))
        counts["sharp mixed errors"] += 1
    return counts


def inverse_ball(k):
    sites = {1}
    for _ in range(k):
        following = {2*n for n in sites}
        following.update((2*n-1)//3 for n in sites if n % 3 == 2)
        sites.update(following)
    return sorted(sites)


def check_blocks():
    length, k = 10, 4
    primes = (2, 3, 5, 7)
    moduli = {p: first_power(p, 3**length*(2**k+1) + 1) for p in primes}
    centers = inverse_ball(k)
    starts = set(range(1, 128))
    starts.update(2**81 + r for r in range(2**length))
    for p, a, h, r in product(primes, centers, (0, 1, 3, 7), range(4)):
        starts.add(a + moduli[p] * (2**h) * (2*r+1))
    counts = Counter()
    for n in sorted(starts):
        segment = [n]
        for _ in range(length):
            segment.append(step(segment[-1]))
        odds = sum(x % 2 for x in segment[:-1])
        marks = set()
        transients = set()
        for p, m in moduli.items():
            hits = [(i, a) for i, x in enumerate(segment[:-1])
                    for a in centers if (x-a) % m == 0]
            marks.update(i for i, _ in hits)
            transients.update(i for i, a in hits if a not in (1, 2))
            for i, a in hits:
                for j, b in hits:
                    if j <= i:
                        continue
                    replay = a
                    for z in segment[i:j]:
                        require(replay % 2 == z % 2, (n, p, i, j, a, b))
                        replay = step(replay)
                    require(replay == b, (n, p, i, j, a, b))
                    counts["same-prime transports"] += 1
        require(len(transients) <= len(primes)*(k+1), n)
        require(len(marks) <= 2*(length-odds)+len(primes)*(k+2), n)
        for p, m in moduli.items():
            single = {i for i,x in enumerate(segment[:-1])
                      if any((x-a) % m == 0 for a in centers)}
            require(len(single) <= 2*(length-odds)+k+2, (n,p))
            if 2*(length-odds)+k+2 < length:
                counts["nonvacuous single-prime bounds"] += 1
        counts["blocks"] += 1
    return counts


def primes_with_multiplicity(n):
    factors = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            n //= d
            factors[d] = factors.get(d, 0) + 1
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def check_auxiliary_clocks():
    counts = Counter()
    for length in range(2, 9):
        for word in product(range(2), repeat=length):
            a, c, b = affine(word)
            if c == 0:
                continue
            u = Fraction(c, b-a)
            primes = list(primes_with_multiplicity(u.denominator))
            if not primes:
                continue
            # Compare genuinely periodic residue itineraries for one extra
            # digit at each of the first two uncanceled denominator primes.
            selected = primes[:2]
            offset_factors = primes_with_multiplicity(c)
            base = prod(p**offset_factors.get(p, 0) for p in selected)
            order = prod(selected)
            modulus = order * base
            z = 5 % modulus
            residue = z % base
            states = set()
            for _ in range(order):
                require(z % base == residue and z not in states, (word,z,base))
                states.add(z)
                z = (a*z+c) * pow(b, -1, modulus) % modulus
            require(z == 5 % modulus and len(states) == order, (u, modulus))
            counts["rational phases"] += 1
            if len(selected)==2:
                counts["simultaneous prime clocks"] += 1
            if base>1:
                counts["partially canceled clocks"] += 1
    return counts


if __name__ == "__main__":
    receipt = check_prefixes() + check_blocks() + check_auxiliary_clocks()
    for name, value in sorted(receipt.items()):
        print(f"{name}: {value}")
