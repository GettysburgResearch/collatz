"""Exact finite controls for the surviving suffix and marked-row construction."""

import itertools
import json
from math import comb


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def next_odd(x):
    numerator = 3 * x + 1
    gap = (numerator & -numerator).bit_length() - 1
    return gap, numerator >> gap


def inverse(gap, target):
    quotient, remainder = divmod((target << gap) - 1, 3)
    require(remainder == 0 and quotient > 0 and quotient % 2, "illegal inverse")
    return quotient


def small_clocks():
    survivors = 0
    for source in range(32):
        current, odds = source, 0
        for clock in range(71):
            if current > 2:
                require(1 << (5 * clock) <= (1 << (8 * odds)) * source**5,
                        "raw rate")
                survivors += 1
            if clock == 70:
                require(current <= 2, "small cutoff")
            odds += current % 2
            current = step(current)
    return {"raw_cells": 32 * 71, "surviving_cells": survivors, "cutoff_cells": 32}


def routed_prefix(gate, total, requested):
    """Reconstruct the two-gap correction after fixing every later mark."""
    missing = 1 + ((total - (gate % 3 == 2) - requested[1:].count(2)) % 2)
    marks = (*requested, missing)
    remaining, target = total, gate
    backwards = []
    for residue in reversed(marks[2:]):
        gap = next(e for e in range(1, 7)
                   if pow(2, e, 9) * target % 9 == 1 + 3 * residue)
        target = inverse(gap, target)
        remaining -= gap
        backwards.append(gap)

    congruence = (pow(2, remaining, 27) * target - 3 - 9 * marks[0]) % 27
    first = next(f for f in range(1, 19) if pow(2, f, 27) == congruence)
    second = remaining - first
    require(second > 0, "second gap")
    source = inverse(first, inverse(second, target))
    return source, [first, second, *reversed(backwards)]


def replay_row(b):
    m = (b - 7) // 5
    k = b - m
    gate = 6 * 2**k - 1
    endpoint = 6 * 3**k - 1
    starts = set()
    require(4 * m + 7 <= k and m >= 2 and endpoint * 64 > b, "row parameters")
    require(3 * gate + 1 <= 2**((4 * b + 4) // 5 + 7), "dyadic carry threshold")
    for word in itertools.product((1, 2), repeat=m - 1):
        source, prefix = routed_prefix(gate, k + 2 * m, word)
        require(source not in starts, "source collision")
        starts.add(source)
        actual, clock = source, 0
        marks = []
        for i, expected in enumerate([*prefix, *([1] * k)]):
            if i == m:
                require(actual == gate, "wrong gate")
            marks.append(actual % 3)
            gap, actual = next_odd(actual)
            require(gap == expected, "forward gap mismatch")
            clock += gap
        require(tuple(marks[:m - 1]) == word, "mark mismatch")
        require(clock == 2 * b and actual == endpoint, "endpoint or clock")
        require((3*gate+1) * 3**b * source <= 3*gate * 4**b * endpoint, "carry")
    require(len(starts) == 2**(m - 1), "coverage")
    following, further_odds = endpoint, 0
    while following != 1 and further_odds < 10000:
        _, following = next_odd(following)
        further_odds += 1
    require(following == 1, "sample did not reach one")
    return {"b": b, "m": m, "k": k, "starts": len(starts),
            "certified_odd_steps_from_q_to_one": further_odds}


def immediate_terminals():
    for k in range(8):
        exponent = 3**(k + 1) + 1
        p, remainder = divmod(2**(exponent - 1) + 1, 3**(k + 2))
        require(not remainder and p > 0, "convergent family divisibility")
        current = 6 * 2**k * p - 1
        for _ in range(k):
            gap, current = next_odd(current)
            require(gap == 1, "convergent family climb")
        require(current == 6 * 3**k * p - 1, "convergent family target")
        require(next_odd(current) == (exponent, 1), "immediate stop")
    return 8


def barrier_counts(cutoff):
    """Compare physical affine numerators and exact barrier inventories."""
    words = 0
    comparisons = 0
    for b in range(1, cutoff + 1):
        histogram = [0] * (b + 1)
        for rest in itertools.combinations(range(1, 2 * b), b - 1):
            odd_positions = {0, *rest}
            carry = height = peak = 0
            for t in range(2 * b):
                if t in odd_positions:
                    height -= 1
                    carry = 3 * carry + (1 << t)
                else:
                    height += 1
                    peak = max(peak, height)
            require(height == 0, "unbalanced raw path")
            require((carry + 4**b) * 2**peak <= 2 * 3**peak * 4**b,
                    "carry exceeds barrier envelope")
            histogram[peak] += 1
            words += 1
        require(sum(histogram) == comb(2*b-1, b-1), "initial down-step count")
        for h in range(1, b + 1):
            reflected = comb(2*b-1, b-h-1) if h < b else 0
            require(sum(histogram[h:]) == reflected, "first-barrier reflection")
            comparisons += 1
    return {"odd_depth_cutoff": cutoff, "balanced_words": words,
            "barrier_histogram_checks": comparisons}


if __name__ == "__main__":
    print(json.dumps({"small": small_clocks(), "barriers": barrier_counts(10),
                      "rows": [replay_row(b) for b in
                      (17, 22, 27, 35, 42, 52, 57)],
                      "immediate_terminal_examples": immediate_terminals()},
                     indent=2, sort_keys=True))
