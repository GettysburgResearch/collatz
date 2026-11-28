"""Exact arithmetic behind smooth-divisor variation and multiplier separation."""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import prod
import json


def require(condition, explanation):
    if not condition:
        raise ValueError(explanation)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


@lru_cache(maxsize=None)
def visits_five(n):
    if n == 5:
        return True
    if n in (1, 2):
        return False
    return visits_five(step(n))


def signature_checks():
    primes = (2, 3, 5, 7, 11, 13)
    # At each prime condition an independent geometric valuation to be at most two.
    laws = [[Fraction(p**(2 - a), p * p + p + 1) for a in range(3)] for p in primes]
    variation_mean = Fraction()
    edge_mean = Fraction()
    law_mass = Fraction()
    signature_count = 0
    for exponents in product(range(3), repeat=len(primes)):
        weight = prod(laws[j][a] for j, a in enumerate(exponents))
        states = [1]
        for p, a in zip(primes, exponents):
            states.append(states[-1] * p**a)
        marks = list(map(visits_five, states))
        variation = sum(left != right for left, right in zip(marks, marks[1:]))
        sampled = marks[::2]
        sampled_variation = sum(left != right for left, right in zip(sampled, sampled[1:]))
        require(sampled_variation <= variation, "sampled switches need canonical switches")
        law_mass += weight
        variation_mean += weight * variation
        signature_count += 1
    for j, p in enumerate(primes):
        for prefix in product(range(3), repeat=j):
            d = prod(primes[i]**a for i, a in enumerate(prefix))
            prefix_weight = prod(laws[i][a] for i, a in enumerate(prefix))
            for a in (1, 2):
                edge_mean += (prefix_weight * laws[j][a]
                              * (visits_five(d) != visits_five(d * p**a)))
    require(law_mass == 1 and variation_mean == edge_mean, "Euler expansion of variation")
    conditions = 0
    for n in range(1, 1601):
        for z in (2, 3, 5, 7, 11):
            d, m = 1, n
            for p in primes:
                if p > z:
                    break
                while m % p == 0:
                    d, m = d * p, m // p
            require(n == d * m and all(m % p for p in primes if p <= z),
                    "complete smooth signature and rough cofactor")
            conditions += 1
    return {"conditioned_geometric_signatures": signature_count,
            "exact_signature_factorizations": conditions,
            "prescribed_target_variation": str(variation_mean)}


def trace(x, h):
    k, e, offset = 0, 0, Fraction()
    rows = []
    y = x
    for t in range(h + 1):
        require(2**t * y == 3**k * x + e, "native integer affine numerator")
        require(e == offset * 3**k, "positive initial-source offset")
        rows.append((y, k, e))
        if y % 2:
            offset += Fraction(2**t, 3**(k + 1))
            e = 3 * e + 2**t
            k += 1
        y = step(y)
    return rows


def multiplier_checks():
    h = 13
    stats = Counter()
    for n in range(1, 385):
        for p in (5, 7, 10, 11):
            left = trace(n, h)
            right = trace(p * n, h)
            stats["native_affine_rows"] += len(left) + len(right)
            for s, (x, a, e) in enumerate(left):
                for u, (y, b, f) in enumerate(right):
                    if x != y:
                        continue
                    common = 2**min(s, u)
                    coefficient = (2**u * 3**a - p * 2**s * 3**b) // common
                    residual = (2**s * f - 2**u * e) // common
                    require(coefficient != 0 and coefficient * n == residual,
                            "non-group multiplier leaves a nonzero integer coefficient")
                    require(abs(residual) < 3**max(s, u), "unequal-time cofactor height")
                    stats["all_native_meetings"] += 1
                    if s != u:
                        stats["equalities_at_distinct_dates"] += 1
    for n in range(3**h, 3**h + 256):
        for p in (5, 7):
            medium = {row[0] for row in trace(n, h)}
            larger = {row[0] for row in trace(p * n, h)}
            require(medium.isdisjoint(larger), "exact gcd exclusion before barrier")
            stats["disjoint_full_prefix_pairs"] += 1
    return dict(stats)


if __name__ == "__main__":
    print(json.dumps({"smooth_signatures": signature_checks(),
                      "multiplier_meetings": multiplier_checks()}, indent=2, sort_keys=True))
