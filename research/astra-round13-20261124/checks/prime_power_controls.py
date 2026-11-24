"""Exact polynomial gcd controls for positive-clock primitive/repeated words."""
from collections import Counter
from itertools import combinations
from math import gcd
from functools import reduce


def trim(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def gcd_degree(a, b):
    while b:
        while a and len(a) >= len(b):
            offset = len(a) - len(b)
            top = a[-1]
            a = [v * b[-1] for v in a]
            for i, coef in enumerate(b):
                a[offset + i] -= top * coef
            trim(a)
            content = reduce(gcd, a, 0)
            if content > 1:
                a = [v // content for v in a]
        a, b = b, a
    return len(a) - 1


def prime_power_base(n):
    for prime in range(2, n + 1):
        if n % prime:
            continue
        while n % prime == 0:
            n //= prime
        return prime if n == 1 else None
    return None


def run():
    counts = Counter()
    for total in range(2, 19):
        for p in range(2, total + 1):
            g = gcd(total, p)
            prime = prime_power_base(g)
            if not prime or 2**total <= 3**p:
                continue
            a, b = total // g, p // g
            m = g // prime
            top = [0] * (b * m * (prime - 1) + 1)
            for j in range(prime):
                top[b * m * j] = 2 ** (a * m * (prime - 1 - j))
            for inner in combinations(range(1, total), p - 1):
                d = (0,) + inner + (total,)
                gaps = tuple(v - u for u, v in zip(d, d[1:]))
                periodic = gaps == gaps[p // prime:] + gaps[:p // prime]
                q = [2**i for i in reversed(d[:-1])]
                vanishes = gcd_degree(q, top) > 0
                if g != 4 or b % 2:
                    if periodic != vanishes:
                        raise ValueError("prime-power periodicity mismatch")
                    counts['ordinary_repeated' if periodic else 'ordinary_nonperiodic'] += 1
                else:
                    if periodic and not vanishes:
                        raise ValueError("periodic exceptional word has nonzero top norm")
                    counts['exceptional'] += 1
    base = (0, 1, 2, 5, 7, 11, 15, 18)
    for k in range(33):
        q = [2**(v + i*k) for i, v in reversed(tuple(enumerate(base)))]
        t = 2**k
        if gcd_degree(q, [1024 * t**4, 0, 0, 0, 1]) != 2:
            raise ValueError("exceptional gcd degree mismatch")
        numerator = sum(coef * 3**i for i, coef in enumerate(q))
        denominator = 2**20 * t**8 - 3**8
        expected = (32*t*t-9) * (32*t*t+9) * (32*t*t-24*t+9)
        if denominator // gcd(numerator, denominator) != expected:
            raise ValueError("complete reduced denominator mismatch")
    counts['exceptional_family'] = 33
    return counts


if __name__ == '__main__':
    print(dict(sorted(run().items())))
