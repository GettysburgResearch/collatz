#!/usr/bin/env python3
"""Independent small-instance verifier for X-8601."""
from itertools import combinations
from math import comb


def compositions(total: int, parts: int):
    for bars in combinations(range(1, total), parts - 1):
        previous = 0
        word = []
        for endpoint in bars + (total,):
            word.append(endpoint - previous)
            previous = endpoint
        yield tuple(word)


def affine_constant(word: tuple[int, ...]) -> int:
    constant = 0
    exponent_sum = 0
    for exponent in word:
        constant = 3 * constant + (1 << exponent_sum)
        exponent_sum += exponent
    return constant


def exact_hits(m: int, K: int):
    denominator = 2**K - 3**m
    hits = []
    for word in compositions(K, m):
        constant = affine_constant(word)
        if constant % denominator == 0:
            hits.append((word, constant // denominator))
    return hits


def main() -> int:
    assert exact_hits(1, 2) == [((2,), 1)]
    expected_empty = [(8, 13), (10, 16), (11, 18), (13, 21), (14, 23)]
    for m, K in expected_empty:
        assert len(list(compositions(K, m))) == comb(K - 1, m - 1)
        assert exact_hits(m, K) == []
    print("direct enumeration passed for the trivial control and all forced windows through m=14")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
