"""Exact finite identities used in stopped-clock and complete semiprime transfer."""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import prod
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def counted(n, t):
    k = 0
    for _ in range(t):
        k += n % 2
        n = step(n)
    return n, k


def first_record(source, targets, suffix):
    n, bits, visited = source, [], set()
    while n not in targets and n not in visited:
        visited.add(n)
        bits.append(n % 2)
        n = step(n)
    if n not in targets:
        return None
    s, k = len(bits), sum(bits)
    tail = tuple(bits[-suffix:]) if suffix else ()
    mark = Fraction(source * 3**k, 2**s * n)
    require(0 < mark <= 1, "native first survival is in (0,1]")
    return (s, k, n, tail), mark


def clock_check():
    stats = Counter()
    for targets, suffix in (({1}, 2), ({5, 7}, 1), ({7, 11}, 2)):
        t = 6
        lower = 2 ** (t + suffix) * max(targets) + 1
        for x in range(lower, lower + 512):
            a = first_record(x, targets, suffix)
            doubled = first_record(2 * x, targets, suffix)
            if a is None:
                require(doubled is None, "even branch preserves a miss")
            else:
                (s, k, y, v), mark = a
                require(doubled == ((s + 1, k, y, v), mark), "native even transfer")
            stats["even_branch_records"] += 1
            if x % 2:
                tripled = first_record(3 * x + 1, targets, suffix)
                if a is None:
                    require(tripled is None, "odd branch preserves a miss")
                else:
                    (s, k, y, v), mark = a
                    expected = mark * Fraction(3 * x + 1, 3 * x)
                    require(tripled == ((s, k - 1, y, v), expected),
                            "native odd transfer with first survival")
                stats["odd_branch_records"] += 1
            for d in (1, 2, 3, 5):
                if counted(x, t) != counted(x + d, t):
                    continue
                b = first_record(x + d, targets, suffix)
                if a is None:
                    require(b is None, "counted merge preserves both misses")
                    stats["synchronized_misses"] += 1
                else:
                    require(b is not None and b[0] == a[0], "complete stopped record")
                    require(b[1] * x == a[1] * (x + d), "true surviving mark ratio")
                    stats["synchronized_hits"] += 1
    pairs = [(1, 1), (2, 1), (3, 2), (8, 5), (19, 12), (65, 41),
             (84, 53), (485, 306), (1054, 665), (24727, 15601)]
    for (a, b), (c, d) in zip(pairs, pairs[1:]):
        require(abs(a * d - b * c) == 1, "adjacent clock basis")
        for m in range(2, 22):
            for i in range(m):
                for j in range(m):
                    if i or j:
                        require((a * i + b * j) % m or (c * i + d * j) % m,
                                "nontrivial clock detected by one basis vector")
                        stats["unimodular_character_tests"] += 1
    return dict(stats)


def distinct_prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        if n % d:
            d += 1
            continue
        factors.append(d)
        n //= d
        if n % d == 0:
            return ()
        d += 1
    if n > 1:
        factors.append(n)
    return tuple(factors)


def semiprime_check():
    factors = {n: distinct_prime_factors(n) for n in range(1, 16500)}
    w = {n for n, ps in factors.items() if n % 2 and len(ps) == 2}
    stats = Counter()
    for x in (60, 180, 360):
        for h in (3, 9, 15):
            direct = sum(sum(u + j in w for j in range(1, h + 1)) ** 2
                         for u in range(x + 1, 2 * x + 1))
            diagonal, positive_pairs = 0, 0
            for j in range(1, h + 1):
                for n in range(x + 1 + j, 2 * x + 1 + j):
                    if n not in w:
                        continue
                    diagonal += 1
                    for shift in range(1, h - j + 1):
                        if n + shift in w:
                            require(shift % 2 == 0, "odd semiprimes have even differences")
                            positive_pairs += 1
            require(direct == diagonal + 2 * positive_pairs, "finite triangular moments")
            stats["shifted_second_moments"] += 1
    for x in (1024, 4096, 8192):
        for r in (3, 4, 5):
            for z in (7, 17, 31):
                enumerated = Counter()
                for prefix in range(1, z + 1, 2):
                    if len(factors[prefix]) != r - 2:
                        continue
                    for m in range(x // prefix + 1, (2 * x) // prefix + 1):
                        if m in w and set(factors[prefix]).isdisjoint(factors[m]):
                            parts = tuple(sorted(factors[prefix] + factors[m]))
                            if parts[-1] in factors[m]:
                                enumerated[prefix * m] += 1
                actual = Counter()
                for n in range(x + 1, 2 * x + 1, 2):
                    parts = factors[n]
                    if len(parts) != r:
                        continue
                    for rest in combinations(parts[:-1], r - 2):
                        if prod(rest) <= z:
                            actual[n] += 1
                    require(actual[n] <= r - 1, "at most one partner choice per small prime")
                    stats["factorization_multiplicity_bounds"] += 1
                require(actual == enumerated, "two independent partner-deletion enumerations")
                stats["partner_population_comparisons"] += 1
    return dict(stats)


if __name__ == "__main__":
    print(json.dumps({"stopped_clocks": clock_check(),
                      "semiprime_population": semiprime_check()}, indent=2, sort_keys=True))
