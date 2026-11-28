"""Exact canonical divisor incidence, finite clock labels, and Haar two-child moments."""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import prod
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


@lru_cache(maxsize=None)
def first_clock(n, target):
    if n == target:
        return 0
    if n == 1:
        return None
    later = first_clock(step(n), target)
    return later + 1 if later is not None else None


def prime_bases(limit):
    primes = []
    least = list(range(limit + 1))
    for p in range(2, limit + 1):
        if least[p] != p:
            continue
        primes.append(p)
        for m in range(p * p, limit + 1, p):
            if least[m] == m:
                least[m] = p
    return primes, least


def factor_chain(n, least):
    d, chain, primes = 1, [1], []
    while n > 1:
        p = least[n]
        primes.append(p)
        while n % p == 0:
            n //= p
            d *= p
        chain.append(d)
    return chain, primes


def variations():
    limit = 16384
    primes, least = prime_bases(limit)
    stats = Counter()
    for n in range(1, limit + 1):
        sites, _ = factor_chain(n, least)
        for target in (1, 5, 85):
            times = [first_clock(m, target) for m in sites]
            true = [t is not None for t in times]
            fast = [t is not None and t <= 5 * m.bit_length() for t, m in zip(times, sites)]
            truth_changes = sum(a != b for a, b in zip(true, true[1:]))
            clock_changes = sum(a != b for a, b in zip(fast, fast[1:]))
            errors = sum(a != b for a, b in zip(true, fast))
            require(abs(clock_changes - truth_changes) <= 2 * errors,
                    "two canonical edges at most per relabelled site")
            stats["canonical_clock_comparisons"] += 1
            stats["genuine_five_changes"] += truth_changes if target == 5 else 0
            stats["finite_five_changes"] += clock_changes if target == 5 else 0

    for z in (3, 5, 11, 19):
        small = [p for p in primes if p <= z]
        euler = {p: prod(Fraction(q - 1, q) for q in small if q <= p) for p in small}
        for target in (1, 5, 85):
            direct = Fraction()
            by_links = Fraction()
            for m in range(2, 4097):
                _, factors = factor_chain(m, least)
                largest = factors[-1]
                if largest <= z and first_clock(m, target) is not None:
                    direct += euler[largest] / m
            for p in small:
                power = p
                while power <= 4096:
                    for d in range(1, 4096 // power + 1):
                        _, factors = factor_chain(d, least)
                        if factors and factors[-1] >= p:
                            continue
                        if first_clock(d * power, target) is not None:
                            by_links += euler[p] / (power * d)
                    power *= p
            require(direct == by_links, "largest-prime Euler incidence at each occupied site")
            stats["finite_euler_occupancy_identities"] += 1

    for w, z in ((2, 11), (3, 17), (5, 29)):
        low_v = prod(Fraction(p - 1, p) for p in primes if p <= w)
        high_v = prod(Fraction(p - 1, p) for p in primes if p <= z)
        for m in range(1, z + 1):
            _, factors = factor_chain(m, least)
            full_band = (high_v / (low_v * m) if all(w < p <= z for p in factors)
                         else Fraction())
            moderate = high_v / (low_v * m) if all(p > w for p in factors) else Fraction()
            require(full_band == moderate, "upper prime bound on the retained band")
            stats["exact_moderate_band_atoms"] += 1
    return dict(stats)


def path_rows(n, t):
    odd, bits = 0, 0
    for j in range(t):
        b = n % 2
        odd += b
        bits += b << j
        n = step(n)
    return odd, bits, n


def parity_checks():
    stats = Counter()
    for t in range(1, 13):
        for a, b in ((1, 3), (1, 5), (1, 7), (3, 11), (7, 17)):
            gap_squares, mixed_total = 0, 0
            for r in range(2**t):
                g, aw, ay = path_rows(a * r, t)
                k, bw, by = path_rows(b * r, t)
                gap = g - k
                gap_squares += gap**2
                mixed_total += (aw ^ bw).bit_count()
                g1 = gap + ay % 2 - by % 2
                # The new lift toggles both parities of the native affine endpoints.
                g2 = gap + (ay + a * 3**g) % 2 - (by + b * 3**k) % 2
                require(g1 + g2 == 2 * gap, "true siblings have opposite grade increments")
                require(g1**2 + g2**2 == 2 * gap**2 + 2 * int(ay % 2 != by % 2),
                        "two-child second-moment identity")
                stats["physical_sibling_moments"] += 1
            require(gap_squares == mixed_total, "native finite Haar grade covariance")
            stats["complete_haar_variance_identities"] += 1
    for k in range(3, 12):
        mod, period = 2**k, 2**(k - 2)
        for u in (1, 3, 5, 7, 11, 17):
            count = sum(pow(3, j, mod) == u % mod for j in range(period))
            require(count == int(u % 8 in (1, 3)), "exact slope valuation residue class")
            stats["embedded_valuation_level_counts"] += 1
    return dict(stats)


if __name__ == "__main__":
    print(json.dumps({"canonical_links": variations(), "multiplier_parity": parity_checks()},
                     indent=2, sort_keys=True))
