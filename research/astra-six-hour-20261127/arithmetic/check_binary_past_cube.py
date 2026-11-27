#!/usr/bin/env python3
"""Exact finite controls for extremal energy on a binary Collatz predecessor tree."""
from collections import Counter
from itertools import product
from math import gcd
import json


def tile_stream():
    time, clock = 0, 0
    while True:
        if 2 ** (clock + 3) >= 3 ** (time + 2):
            yield "A"
            time += 2
            clock += 3
        else:
            yield "B"
            time += 1
            clock += 2


def spell(skeleton, bits):
    bits = iter(bits)
    word = []
    for tile in skeleton:
        if tile == "B":
            word.append(2)
        else:
            word.extend((2, 1) if next(bits) else (1, 2))
    return word


def affine(word):
    carry, scale = 0, 1
    for e in word:
        carry = 3 * carry + scale
        scale <<= e
    return carry, scale


def energy(values, modulus=None):
    sums = Counter()
    for x in values:
        for y in values:
            sums[(x + y) % modulus if modulus else x + y] += 1
    return sum(m * m for m in sums.values())


def positive_path(word):
    carry, scale = affine(word)
    modulus = scale * 2
    residue = (scale - carry) * pow(3 ** len(word), -1, modulus) % modulus
    x = residue + (modulus << 64)
    minimum = maximum = x
    for e in word:
        numerator = 3 * x + 1
        assert numerator % (2 ** (e + 1)) == 2 ** e
        x = numerator >> e
        minimum, maximum = min(minimum, x), max(maximum, x)
    assert 3 * maximum < 8 * minimum
    return minimum.bit_length()


def main():
    schedule = tile_stream()
    skeleton = tuple(next(schedule) for _ in range(9))
    k = skeleton.count("A")
    patterns = list(product((0, 1), repeat=k))
    words = [spell(skeleton, bits) for bits in patterns]
    n, T = len(words[0]), sum(words[0])
    q = 3 ** n
    raw = [affine(word)[0] for word in words]
    inverse = pow(2 ** T, -1, q)
    residues = [x * inverse % q for x in raw]
    assert len(set(residues)) == 2 ** k
    assert energy(raw) == energy(residues, q) == 6 ** k

    # Distinct recurrences of the same skeleton in one mechanical path.
    full_tiles, found = [], []
    schedule = tile_stream()
    next_free = 0
    while len(found) < len(patterns):
        full_tiles.append(next(schedule))
        start = len(full_tiles) - len(skeleton)
        if start >= next_free and tuple(full_tiles[start:]) == skeleton:
            found.append(start)
            next_free = len(full_tiles)
    decisions = {i: 0 for i, tile in enumerate(full_tiles) if tile == "A"}
    for start, bits in zip(found, patterns):
        stream = iter(bits)
        for j, tile in enumerate(skeleton, start):
            if tile == "A":
                decisions[j] = next(stream)
    full = spell(full_tiles, [decisions[i] for i in sorted(decisions)])
    minimum_bits = positive_path(full)

    # A separate family makes the physical odd endpoints a literal integer cube.
    # Choose an identical twenty-bit class at the endpoint of every past.
    binary_modulus = 2 ** 20
    increments = []
    for j in range(k):
        index = 1 << (k - j - 1)
        delta = (residues[index] - residues[0]) % q
        increments.append(binary_modulus * (delta * pow(binary_modulus, -1, q) % q))
    base = residues[0] + q * ((1 - residues[0]) * pow(q, -1, binary_modulus)
                              % binary_modulus) + ((q * binary_modulus) << 64)
    endpoints = [base + sum(bit * step for bit, step in zip(bits, increments))
                 for bits in patterns]
    assert all(y % binary_modulus == 1 for y in endpoints)
    assert [y % q for y in endpoints] == residues and gcd(q, binary_modulus) == 1
    lower, upper = min(endpoints), max(endpoints)
    for y, word in zip(endpoints, words):
        for e in reversed(word):
            numerator = (y << e) - 1
            assert numerator % 3 == 0
            y = numerator // 3
            assert y > 0 and y % 2 == 1
            lower, upper = min(lower, y), max(upper, y)
    assert 3 * upper < 8 * lower and energy(endpoints) == 6 ** k
    print(json.dumps({
        "skeleton": "".join(skeleton), "free_tiles": k,
        "odd_window": n, "total_clock": T, "distinct_words": len(words),
        "raw_energy": energy(raw), "modular_energy": energy(residues, q),
        "single_ordinary_path_odd_edges": len(full),
        "single_ordinary_path_shortcuts": sum(full),
        "single_ordinary_path_disjoint_occurrences": len(found),
        "single_ordinary_path_minimum_bit_length": minimum_bits,
        "single_ordinary_path_ratio_strictly_below_8_over_3": True,
        "separate_physical_endpoint_energy": energy(endpoints),
        "separate_endpoints_common_binary_class": 1,
        "separate_endpoints_binary_modulus": binary_modulus,
        "separate_paths_joint_ratio_strictly_below_8_over_3": True
    }, indent=2))


if __name__ == "__main__":
    main()
