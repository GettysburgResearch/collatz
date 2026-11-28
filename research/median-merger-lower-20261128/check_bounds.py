"""Exact certificates for median-time Collatz collisions. Standard library only."""

from collections import Counter
from fractions import Fraction
from math import comb


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def deadline(x):
    """Largest h with (4/3)^h <= x^2, using integer arithmetic."""
    lo, hi = 0, 5 * x.bit_length()
    while lo + 1 < hi:
        h = (lo + hi) // 2
        if 4**h <= x*x * 3**h:
            lo = h
        else:
            hi = h
    require(4**lo <= x*x * 3**lo and 4**hi > x*x * 3**hi, "deadline")
    return lo


def odd_window_bound(x):
    """Unordered cross-block pairs, verified from the full binary period."""
    if x < 12:
        raise ValueError("an odd binary window requires x >= 12")
    t = (x // 6).bit_length() - 1
    total = 0
    for s in range(1, t + 1):
        z = 3**s
        high = 2*z + (z + 2**s - 1) // 2**s - 1
        width = high - z + 1 - (high // 3 - (z - 1) // 3)
        quotient, remainder = divmod(comb(t - 1, s - 1), width)
        total += width * quotient**2 + (2*quotient + 1) * remainder
    return t, total


def first_one(n, limit, cache, cache_size):
    """Use only witnessed paths, with at most limit uncached forward steps."""
    trail = []
    while n not in cache and len(trail) < limit:
        trail.append(n)
        n = step(n)
    if n not in cache:
        return None
    length = cache[n]
    for value in reversed(trail):
        length += 1
        if value <= cache_size:
            cache[value] = length
    return length if length <= limit else None


def lift_certificate(x, seed_limit, h, bands=1):
    """Use witnessed odd cores, normalized to (x/4,x] by powers of four."""
    cache = {1: 0}
    hist = Counter()
    require(bands >= 1, "at least one lower band")
    for m in range(1, min(seed_limit, x // 16**bands) + 1, 2):
        shift = 2 * (((x // m).bit_length() - 1) // 2)
        require(shift >= 4*bands and 4 * (m << shift) > x >= m << shift, "lift")
        if shift > h:
            continue
        tau = first_one(m, h - shift, cache, seed_limit)
        if tau is not None:
            hist[tau + shift] += 1
    even = sum(v for t, v in hist.items() if t % 2 == 0)
    odd = sum(hist.values()) - even
    phase_pairs = even**2 + odd**2
    ties = sum(count * hist[t + 4*j] for j in range(1, bands + 1)
               for t, count in hist.items())
    guaranteed = bands * phase_pairs - ties
    if bands == 1:
        require(8 * guaranteed >= 3 * (even + odd)**2, "four-step tie bound")
    require(4 * guaranteed >= (2*bands - 1) * (even + odd)**2, "multiple-band bound")
    return even + odd, guaranteed


def gate_rectangle(x):
    """All cross pairs from [1,x/4] and (3x/4,x], one orientation."""
    h = deadline(x)
    cache = {1: 0}
    def histogram(values):
        result = Counter()
        for n in values:
            tau = first_one(n, h + 2, cache, x)
            if tau is not None:
                result[tau] += 1
        return result
    low = histogram(range(1, x // 4 + 1))
    high = histogram(range(3*x // 4 + 1, x + 1))
    # The endpoint 1 at date t includes hits t, t-2, ... . An arrival at
    # 4 at date t is exactly a first visit to 1 at t+2.
    low_at_one = [0, 0]
    high_at_one = [0, 0]
    total = 0
    for t in range(h):
        p = t % 2
        low_at_one[p] += low[t]
        high_at_one[p] += high[t]
        total += low_at_one[p] * high[t + 2] + high_at_one[p] * low[t + 2]
    return total


def direct_checks():
    for x in (24, 64, 128, 216):
        h = deadline(x)
        t, promised = odd_window_bound(x)
        b = 2**t
        lower = Counter()
        upper = Counter()
        for m in range(b + 1, 2*b, 2):
            low, high = m, 3*m + 1
            for _ in range(t):
                low, high = step(low), step(high)
            lower[low] += 1
            upper[high] += 1
        actual = sum(count * upper[y] for y, count in lower.items())
        require(actual >= promised and lower == upper, "full-parity certificate")
        count = 0
        for n in range(1, x // 4 + 1):
            for m in range(3*x // 4 + 1, x + 1):
                a, b = n, m
                for _ in range(h):
                    if a == b:
                        break
                    if {a, b} == {1, 4}:
                        count += 1
                        break
                    a, b = step(a), step(b)
        require(count == gate_rectangle(x), "direct first-meeting census")


if __name__ == "__main__":
    direct_checks()
    x = 2**71
    t, lower = odd_window_bound(x)
    print("binary window, X, time, unordered separated pairs:", x, t, lower)
    x = 2**24
    seeds, lower = lift_certificate(x, 2**20, deadline(x))
    print("two lifts, X, deadline, cores, unordered pairs:", x, deadline(x), seeds, lower)
    seeds, lower = lift_certificate(x, 2**16, deadline(x), bands=2)
    print("three lifts, X, deadline, cores, unordered pairs:", x, deadline(x), seeds, lower)
    x = 2**20
    lower = gate_rectangle(x)
    print("opposite quarters, X, deadline, gate pairs:", x, deadline(x), lower)
    print("conditional first-meeting fraction:", Fraction(lower, (x//4)**2))
