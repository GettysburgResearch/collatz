#!/usr/bin/env python3
"""Independent exhaustive small-case checks and count audit for X-8602."""
from itertools import product
from math import comb


def constant(word):
    c = 0
    k = 0
    for exponent in word:
        c = 3 * c + (1 << k)
        k += exponent
    return c


def direct_binary(m, K):
    denominator = 2**K - 3**m
    hits = []
    for bits in product((0, 1), repeat=m):
        if sum(bits) != K - m:
            continue
        word = tuple(1 + bit for bit in bits)
        c = constant(word)
        if c % denominator == 0:
            hits.append((word, c // denominator))
    return hits


def direct_one_large(m, K):
    denominator = 2**K - 3**m
    hits = []
    words = set()
    for position in range(m):
        for special in range(3, K - (m - 1) + 1):
            twos = K - special - (m - 1)
            if twos < 0 or twos > m - 1:
                continue
            for bits in product((0, 1), repeat=m - 1):
                if sum(bits) != twos:
                    continue
                word = list(1 + bit for bit in bits)
                word.insert(position, special)
                item = tuple(word)
                words.add(item)
    for word in words:
        c = constant(word)
        if c % denominator == 0:
            hits.append((word, c // denominator))
    return hits


def main():
    assert direct_binary(1, 2) == [((2,), 1)]
    assert direct_binary(8, 13) == []
    # Independent direct comparison on a nontrivial small shape.
    assert direct_one_large(8, 13) == []

    binary_count = comb(41, 24)
    one_large_count = sum(
        41 * comb(40, 24 - (special - 1))
        for special in range(3, 26)
    )
    assert binary_count == 151_584_480_450
    assert one_large_count == 35_397_011_688_418
    assert binary_count + one_large_count == 35_548_596_168_868
    print("small direct searches and all conceptual-count identities passed")


if __name__ == "__main__":
    main()
