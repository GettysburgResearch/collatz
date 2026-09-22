#!/usr/bin/env python3
"""Independent exact contraction and height audit for T-9605."""
from __future__ import annotations

from itertools import combinations, permutations
from math import ceil

S = 11


def centered(word: tuple[int, ...]) -> tuple[int, int]:
    prefix = 0
    value = 0
    for index, letter in enumerate(word):
        value += 3 ** (len(word) - 1 - index) * 2**prefix * (4 - 2**letter)
        prefix += letter
    return value, 2**prefix - 3 ** len(word)


def canonical_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[shift:] + word[:shift] for shift in range(len(word)))


def cyclic_margin(highs: tuple[int, ...]) -> tuple[int, int]:
    seen: set[tuple[int, ...]] = set()
    best: int | None = None
    for positions in combinations(range(S), len(highs)):
        for assignment in set(permutations(highs)):
            word = [1] * S
            for position, value in zip(positions, assignment):
                word[position] = value
            representative = canonical_rotation(tuple(word))
            if representative in seen:
                continue
            seen.add(representative)
            defect, denominator = centered(representative)
            margin = defect - 2 * denominator
            best = margin if best is None else max(best, margin)
    assert best is not None
    return len(seen), best


def main() -> None:
    expected_binary = {
        4: (30, -241076),
        5: (42, -3648644),
        6: (42, -18123908),
        7: (30, -81541820),
        8: (15, -344996540),
        9: (5, -1500282896),
        10: (1, -6012387344),
        11: (1, -24051320846),
    }
    for high_count, expected in expected_binary.items():
        assert cyclic_margin((3,) * high_count) == expected

    expected_thresholds = {
        (3, 3, 5): (45, -147764),
        (3, 4, 4): (45, -251444),
        (3, 7): (10, -15572),
        (4, 6): (10, -447700),
        (5, 5): (5, -663764),
        (8,): (1, -79892),
    }
    for highs, expected in expected_thresholds.items():
        assert cyclic_margin(highs) == expected

    residual = [
        (),
        (3,), (4,), (5,), (6,), (7,),
        (3, 3), (3, 4), (3, 5), (4, 4), (3, 6), (4, 5),
        (3, 3, 3), (3, 3, 4),
    ]
    for highs in residual:
        ones = S - len(highs)
        high_sum = sum(highs)
        total = ones + high_sum
        for radius in (23, 24):
            retained = radius - ceil(radius / S)
            upper = 2 ** (high_sum + 1) * (3**ones - 2**ones) * 4**retained
            denominator = 2 ** (total + 2 * radius) - 3 ** (S + radius)
            assert upper < 2 * denominator

    print("independent T-9605 contraction and R>=23 height audit passed")


if __name__ == "__main__":
    main()
