"""Replay the small, exhaustive affine and unequal-clock checks with integers."""

from collections import Counter
from fractions import Fraction
from math import comb


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def walk(x, h):
    odd = 0
    for _ in range(h):
        odd += x % 2
        x = step(x)
    return x, odd


def budgeted_orbit(x, budget):
    # Every consecutive odd run ends: x + 1 loses one factor of two per step.
    seen = {}
    odd = even = 0
    while x not in seen:
        seen[x] = (odd, even)
        if x % 2:
            odd += 1
        else:
            if even == budget:
                break
            even += 1
        x = step(x)
    return seen


def check_fast_pair(h, r, s):
    x, odd_left = walk(r, h)
    y, odd_right = walk(r + 2**h, h)
    if not (0 < r < 2**h and r % 2 and odd_left == odd_right == s):
        raise AssertionError(("constructed word", h, r, s))
    if x != (3**s - 1) // 2 or y != 3 * x + 1 or step(x) != step(y):
        raise AssertionError(("constructed meeting", h, r, s))
    if budgeted_orbit(x, 0).keys() & budgeted_orbit(y, 0).keys():
        raise AssertionError(("claimed minimum cost", h, r, s))


def check_constructions():
    prescribed = branching = ancestors = 0
    for h in range(2, 61, 2):
        for s in range(1, h, 2):
            e = h - s - 1
            r = 2 ** (h - 1) - (2 ** (e + 1) + 1) // 3
            check_fast_pair(h, r, s)
            prescribed += 1

    for h in range(13, 50):
        depth = (h - 1) // 6
        frontier = [(1, 0)]
        for _ in range(depth):
            children = []
            for z, total in frontier:
                for v in range(1, 7):
                    numerator = 2**v * z + 1
                    if numerator % 9 in (3, 6):
                        children.append((numerator // 3, total + v))
            frontier = children
        if len({p for p, _ in frontier}) != 2**depth:
            raise AssertionError(("distinct auxiliary inputs", h))
        retained = 0
        for p, total in frontier:
            s = depth + h - 1 - total
            if s % 2:
                check_fast_pair(h, 2 ** (h - 1) - p, s)
                retained += 1
        if retained != 2 ** (depth - 1):
            raise AssertionError(("parity split", h))
        branching += retained

    for k in range(1, 8):
        for b in range(1, 2**k, 2):
            y, s = walk(b, k)
            g = 3**s
            period = 2 * (g // 3)
            low = (2 * g - 1).bit_length()
            for t in range(1, 13):
                if t % 3 == 0:
                    continue
                v = next(v for v in range(low, low + period) if pow(2, v, g) * t % g == y % g)
                w = (2**v * t - y) // g
                endpoint, _ = walk(b + 2**k * w, k)
                if not 0 <= w < 2 ** (period + 1) * t or endpoint != 2**v * t:
                    raise AssertionError(("ordinary ancestor", k, b, t))
                ancestors += 1
    print(f"{prescribed} prescribed pairs, {branching} branching pairs, {ancestors} ancestors")


def check():
    sources = meetings = localized = immediate = 0
    for h in range(1, 15):
        counts = Counter()
        scale = 2**h
        for r in range(1, scale, 2):
            sources += 1
            x, s = walk(r, h)
            y, s2 = walk(r + scale, h)
            gap = 3**s
            if y != x + gap or s2 != s:
                raise AssertionError(("upper-bit identity", h, r))
            counts[s] += 1
            position = Fraction(r, scale)
            if not 0 <= Fraction(x, gap) - position <= Fraction(1, 2**s):
                raise AssertionError(("initial offset", h, r))
            if budgeted_orbit(x, 0).keys() & budgeted_orbit(y, 0).keys():
                raise AssertionError(("zero-budget merger", h, r))
            p = scale // 2 - r
            mirror_odds = 0
            if p > 0:
                for _ in range(h - 1):
                    mirror_odds += p % 2
                    p = (3 * p - 1) // 2 if p % 2 else p // 2
            predicted = p == 1 and mirror_odds % 2 == 1
            if predicted != (step(x) == step(y)):
                raise AssertionError(("one-step classification", h, r))
            immediate += predicted
            budget = 4
            left = budgeted_orbit(x, budget)
            right = budgeted_orbit(y, budget)
            for point in left.keys() & right.keys():
                meetings += 1
                a1, e1 = left[point]
                a2, e2 = right[point]
                cost = max(e1, e2)
                if s < 3 or 8 * 2**cost > gap:
                    continue
                localized += 1
                ratio = Fraction(3, 2) ** (a1 - a2) * Fraction(2) ** (e2 - e1)
                radius = Fraction(1, 2**s) + Fraction(3 * 2**cost, gap)
                if ratio < Fraction(3, 2) or abs(position - 1 / (ratio - 1)) > radius:
                    raise AssertionError(("ratio interval", h, r, point))
        if any(counts[s] != comb(h - 1, s - 1) for s in range(1, h + 1)):
            raise AssertionError(("conditioned parity distribution", h))
    if localized == 0:
        raise AssertionError("No eligible merger exercised the interval bound")
    print(f"{sources} odd sources, {meetings} common states, {localized} interval checks")
    print(f"{immediate} synchronous one-step mergers in the exhaustive grid")


if __name__ == "__main__":
    check()
    check_constructions()
