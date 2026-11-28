"""Exhaustive small ternary minima and independent positive-source search."""

from collections import defaultdict
from math import comb


def require(condition, message):
    if not condition:
        raise ValueError(message)


def odd_step(value):
    numerator = 3 * value + 1
    exponent = (numerator & -numerator).bit_length() - 1
    return numerator >> exponent, exponent


def next_level(previous, depth):
    modulus = 3 * len(previous)
    old_max = max(cost for cost in previous if cost is not None)
    max_exponent = old_max + 4 - depth
    level = [None] * modulus
    for y in range(modulus):
        if y % 3 == 0:
            continue
        residue = y
        best = None
        for e in range(1, max_exponent + 1):
            residue = 2 * residue % modulus
            if residue % 3 != 1:
                continue
            old = previous[(residue - 1) // 3]
            if old is not None:
                candidate = e + old
                best = candidate if best is None else min(candidate, best)
        require(best is not None and depth + 1 <= best <= 4 * (depth + 1),
                "unit inverse minimum outside exact elementary bounds")
        level[y] = best
    return level


def positive_minima(depth):
    entries = {}
    for seed in range(1, 8000, 2):
        if seed % 3 == 0:
            continue
        y = seed
        s = 0
        for _ in range(depth):
            y, e = odd_step(y)
            s += e
        if y <= 120:
            entries[y] = min(s, entries.get(y, s))
    return entries


def exhaustive_levels():
    previous = [None, 0, 0]
    rows = registry = 0
    observed = []
    for depth in range(1, 10):
        previous = next_level(previous, depth - 1)
        q = len(previous)
        found = positive_minima(depth)
        for y in range(1, 121, 2):
            if y % 3 == 0:
                continue
            cost = previous[y % q]
            # Every minimizing source lies below this exact universal cap.
            if 2**cost * y <= 7999 * 3**depth:
                require(found.get(y) == cost, "source census contradicted ternary minimum")
                registry += 1
        gaps = []
        for y, cost in enumerate(previous):
            if cost is None:
                continue
            b = (4 * y + 1) if y % 3 == 1 else (16 * y + 5)
            gap = previous[b % q] - cost
            gaps.append(gap)
            rows += 1
        signed_gap = previous[(-11) % q] - previous[-1]
        require(previous[-1] == depth, "signed all-ones cost")
        require(400 * 2**depth <= 4**(previous[(-11) % q] - depth) * 450 * 121,
                "signed energy check")
        observed.append((depth, min(gaps), max(gaps), signed_gap))
    print(f"all unit ternary rows={rows}, independently complete positive minima={registry}")
    print(f"depth,min-gap,max-gap,signed-gap={observed}")


def sibling_cutoffs():
    cases = visits = 0
    for m in range(1, 80, 2):
        if m % 3 == 0:
            continue
        a = m
        total = 0
        hit_by_seed = defaultdict(set)
        for j in range(1, 8):
            a, cost = odd_step(a)
            total += cost
            d = 3
            limit = (4 * a * 2**(total+d)) // (3**(j+1))
            for seed in range(1, limit + 80, 2):
                if seed % 3 == 0:
                    continue
                x = seed
                s = 0
                for _ in range(j):
                    x, e = odd_step(x)
                    s += e
                # x=b_h(a) iff (3x+1)/(3a+1)=4^h for integer h>=1.
                large, small = 3*x+1, 3*a+1
                if large % small:
                    continue
                ratio = large // small
                if ratio < 4 or ratio & (ratio-1):
                    continue
                twice_h = ratio.bit_length() - 1
                if twice_h % 2 or s + twice_h > total + d:
                    continue
                require(seed <= limit, "missed admissible positive source")
                hit_by_seed[seed].add(j)
                visits += 1
            cases += 1
        require(all(len(js) == 1 for js in hit_by_seed.values()),
                "one source entered two synchronous side cuts")
    require(visits > 10, "too few actual first-sibling witnesses")
    print(f"complete all-sibling cutoffs={cases}, qualifying physical witnesses={visits}")


def composition_budget():
    for r in range(1, 8):
        for total in range(r, 36):
            require(sum(comb(s-1, r-1) for s in range(r, total+1)) == comb(total, r),
                    "bounded first low-visit composition budget")
    print("bounded-composition totals=224")


if __name__ == "__main__":
    exhaustive_levels()
    sibling_cutoffs()
    composition_budget()
