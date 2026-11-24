"""Small exact replays of the ordinary first-hit decoder and lift equations."""

from fractions import Fraction
from functools import reduce
from math import gcd
import json


def require(ok, context):
    if not ok:
        raise ArithmeticError(context)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def path_to_one(n):
    path = [n]
    while path[-1] != 1:
        require(len(path) < 5000, ("horizon", n))
        path.append(step(path[-1]))
    return path


def companion(path):
    d = Fraction(9)
    for x in reversed(path[:-1]):
        e = x % 2
        d = e + (2 ** (1 + e) * d) / 3
    return d


def decode(h, a):
    bits = []
    for j in range(h, 0, -1):
        e = a % 2
        b, rem = divmod(a - (3 ** j if e else 0), 4 if e else 2)
        if b < 0 or rem:
            return None
        a = b
        bits.append(e)
    if a != 4:
        return None
    y = 4
    for bit in reversed(bits):
        if not bit:
            y *= 2
            continue
        x, rem = divmod(2 * y - 1, 3)
        if rem:
            return None
        y = x
    return y


def valuation_two(z):
    require(z != 0, "valuation at zero")
    z = abs(z)
    return (z & -z).bit_length() - 1


def replay():
    N = 2048
    paths = {n: path_to_one(n) for n in range(1, N + 1)}
    values = {n: companion(path) for n, path in paths.items()}
    decodes = sample_pairs = primitive_tuples = terminal = trial_numerators = 0
    for n, path in paths.items():
        h = max(0, len(path) - 3)
        d = values[n]
        require(d.denominator == 3 ** h, ("denominator", n))
        if n not in (1, 2):
            require(decode(h, d.numerator) == n, ("inverse", n))
            decodes += 1
        a, b = step(n), step(step(n))
        require(3 * b <= n * 3 ** ((n % 2) + (a % 2)), ("pair budget", n))
    # Exhaust every attainable numerator at these levels. In each reverse
    # step the maximum numerator grows by at most 3^h plus four times its
    # previous maximum. A source reaching four in h clocks is at most 4*2^h.
    maximum = 4
    for h in range(6):
        expected = {
            d.numerator: n for n, d in values.items()
            if n not in (1, 2) and len(paths[n]) == h + 3
        }
        for a in range(maximum + 1):
            require(decode(h, a) == expected.get(a), ("trial", h, a))
            trial_numerators += 1
        maximum = 3 ** (h + 1) + 4 * maximum
    for n in range(1, 33):
        for m in range(n + 1, 513):
            r = valuation_two(m - n)
            k = (m - n) >> r
            x = n
            p = 0
            for _ in range(r):
                p += x % 2
                x = step(x)
            d = values[m] - values[n]
            require(d.denominator % 2 and valuation_two(d.numerator) == r + p,
                    ("companion precision", n, m))
            tail = paths[m][r:]
            require(tail and tail[0] == x + 3 ** p * k, ("tail start", n, m))
            odd_positions = [j for j, y in enumerate(tail[:-1]) if y % 2]
            q = len(odd_positions)
            terms = [2 ** (len(tail) - 1), -(k * 3 ** (p + q)), -(3 ** q * x)]
            terms.extend(-(2 ** j * 3 ** (q - i - 1))
                         for i, j in enumerate(odd_positions))
            require(sum(terms) == 0 and reduce(gcd, terms) == 1,
                    ("primitive tuple", n, m))
            require(all(z < 0 for z in terms[1:]), ("signs", n, m))
            sample_pairs += 1
            primitive_tuples += 1
    for t in range(64):
        r = 6 * t + 1
        u = 2 ** r
        v = 9 * u + 2
        p = 0
        for _ in range(r):
            p += v % 2
            u, v = step(u), step(v)
        require(u == 1 and v == 3 ** (3 * t + 2) + 1 and p == 3 * t,
                ("terminal", t))
        require((1 - v) // 3 ** p == -9, ("spurious fitted power", t))
        terminal += 1
    return dict(positive_sources=N, two_clock_controls=N, first_hit_decodes=decodes,
                tested_numerators=trial_numerators, companion_precisions=sample_pairs,
                primitive_lift_tuples=primitive_tuples, zero_word_terminals=terminal)


if __name__ == "__main__":
    print(json.dumps(replay(), indent=2, sort_keys=True))
