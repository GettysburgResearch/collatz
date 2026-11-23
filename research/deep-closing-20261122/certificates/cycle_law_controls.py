#!/usr/bin/env python3
"""Finite controls for GRH_AFFINE_CYCLE_ATTEMPT.md; no cycle search claim."""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def carry_from_positions(word):
    positions = [j for j, bit in enumerate(word) if bit]
    p = len(positions)
    return sum(3 ** (p - 1 - i) * 2**j for i, j in enumerate(positions))


def carry_from_append(word):
    c = 0
    for j, bit in enumerate(word):
        c = 3**bit * c + bit * 2**j
    return c


def shortcut(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def primitive(word):
    a = len(word)
    return not any(a % d == 0 and word == word[:d] * (a // d)
                   for d in range(1, a))


def validate_record(record):
    word = tuple(record["word"])
    require(all(b in (0, 1) for b in word), "nonbinary word")
    require(record["p"] == sum(word), "odd count")
    require(record["D"] == 2 ** len(word) - 3 ** sum(word), "denominator")
    require(record["C"] == carry_from_positions(word), "carry numerator")


def main():
    counts = {"length_max": 12, "word_checks": 0, "law_checks": 0,
              "positive_integral_words": 0, "primitive_integral_words": 0,
              "binomial_pairs": 0, "damaged_controls_rejected": 0}
    for a in range(1, 13):
        for p in range(1, a + 1):
            residues = set()
            denominator = 2**a - 3**p
            histogram = Counter()
            primitive_zeros = 0
            for positions in combinations(range(a), p):
                pos = set(positions)
                word = tuple(int(j in pos) for j in range(a))
                c = carry_from_positions(word)
                require(c == carry_from_append(word), "append carry")
                rotated_c = carry_from_positions(word[1:] + word[:1])
                require(2 * rotated_c == (c if word[0] == 0
                                          else 3 * c + denominator),
                        "dependent cyclic rotation identity")
                require(c % 2**a not in residues, "binary residue injectivity")
                residues.add(c % 2**a)
                counts["word_checks"] += 1
                if denominator <= 0:
                    continue
                histogram[c % denominator] += 1
                if c % denominator:
                    continue
                x = c // denominator
                require(x > 0, "fixed point positivity")
                start = x
                for bit in word:
                    require(x % 2 == bit, "ordinary parity realization")
                    x = shortcut(x)
                require(x == start, "full return")
                counts["positive_integral_words"] += 1
                rotations = {word[j:] + word[:j] for j in range(a)}
                require(all(carry_from_positions(v) % denominator == 0
                            for v in rotations), "rotation divisibility")
                if primitive(word):
                    require(len(rotations) == a, "free primitive rotation")
                    primitive_zeros += 1
                    counts["primitive_integral_words"] += 1
            require(len(residues) == comb(a, p), "binary injective count")
            if denominator > 0:
                w = comb(a, p)
                require(sum(histogram.values()) == w, "law normalization")
                tv = sum(abs(Fraction(histogram[r], w) - Fraction(1, denominator))
                         for r in range(denominator)) / 2
                require(tv >= 1 - Fraction(w, denominator), "TV support bound")
                require(primitive_zeros % a == 0, "primitive zero count")
                if primitive_zeros:
                    require(Fraction(histogram[0], w) >= Fraction(a, w),
                            "primitive zero atom threshold")
                require(Fraction(p, comb(a - 1, p - 1)) == Fraction(a, w),
                        "odd-start rotation normalization")
                counts["law_checks"] += 1

    for a in range(1, 129):
        for p in range(1, a + 1):
            if 4 * a <= 7 * p:
                require(comb(a, p)**7 < 120**a, "exact binomial cone")
                counts["binomial_pairs"] += 1

    record = {"word": [1, 0, 1, 0], "p": 2, "C": 7, "D": 7}
    validate_record(record)
    for field in ("p", "C", "D"):
        bad = dict(record)
        bad[field] += 1
        try:
            validate_record(bad)
        except ValueError:
            counts["damaged_controls_rejected"] += 1
        else:
            raise ValueError("damaged control accepted: " + field)
    require(counts["damaged_controls_rejected"] == 3, "damage rejection count")
    counts["status"] = "PASS"
    counts["scope"] = "finite arithmetic controls; not unrestricted cycle exclusion"
    print(json.dumps(counts, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
