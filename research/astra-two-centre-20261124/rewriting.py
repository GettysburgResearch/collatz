"""Exact full-neighborhood peak certificate. Uses only the Python standard library."""
from fractions import Fraction
from math import lcm


def require(condition, message):
    if not condition:
        raise ValueError(message)


def neighbors(value, slope):
    """Shifted integer value at the seed and its affine slope under translation."""
    yield 2 * value - 1, 2 * slope
    if value % 2:
        yield (value + 1) // 2, slope / 2
    else:
        yield 3 * value // 2, 3 * slope / 2
    if value % 3 == 0:
        yield 2 * value // 3, 2 * slope / 3


def certificate(seed, ratio):
    source = seed, Fraction(1)
    interior = {source}
    pending = [source]
    boundary = set()
    while pending:
        point = pending.pop()
        for value, slope in neighbors(*point):
            if slope >= ratio:
                require(value - 1 >= ratio * (seed - 1), "boundary below peak")
                boundary.add((value, slope))
            else:
                require(value >= seed and slope >= 1, "interior below floor")
                if (value, slope) not in interior:
                    interior.add((value, slope))
                    pending.append((value, slope))
    period = lcm(*(6 * slope.denominator for _, slope in interior))
    require(all((period * slope).denominator == 1 and (period * slope) % 6 == 0
                for _, slope in interior), "translation changes an interior guard")
    return len(interior), len(boundary), period


def weighted_rank_test(bound=1_000_000):
    """Exact weighted time to 1; a common denominator keeps each edge integral."""
    scale = lcm(*range(1, 65))
    costs = {1: 0}
    worst_source, worst_cost, worst_bits = 1, 0, 1
    first_failures = {}
    max_bits = 1
    for source in range(2, bound + 1):
        node = source
        trail = []
        while node not in costs:
            trail.append(node)
            node = node // 2 if node % 2 == 0 else (3 * node + 1) // 2
        for prev in reversed(trail):
            bits = max(prev, node).bit_length()
            max_bits = max(bits, max_bits)
            require(scale % bits == 0, "inexact edge toll")
            costs[prev] = costs[node] + scale // bits
            node = prev
        bits = source.bit_length() - 1
        cost = costs[source]
        if cost * worst_bits > worst_cost * bits:
            worst_source, worst_cost, worst_bits = source, cost, bits
        for coefficient in (1, 2, 3):
            if cost >= coefficient * bits * scale:
                first_failures.setdefault(coefficient, source)
    return worst_source, Fraction(worst_cost, worst_bits * scale), first_failures, max_bits


if __name__ == "__main__":
    result = certificate(9664, 1024)
    require(result == (3402, 1137, 7342984060644141028475928576), "peak receipt")
    print("interior, boundary, period =", result)
    worst_source, ratio, first_failures, max_bits = weighted_rank_test()
    require(worst_source == 27 and ratio == Fraction(237739, 102960), "worst ratio")
    require(first_failures == {1: 3, 2: 27} and max_bits == 35, "coverage receipt")
    print("weighted rank: worst source, ratio, first failures, max bits =",
          worst_source, ratio, first_failures, max_bits)
