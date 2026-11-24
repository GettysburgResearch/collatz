"""Finite checks of physical source aliases and the three-label score algebra."""

from functools import cache
from itertools import product
import json


def require(test):
    if not test:
        raise ValueError('finite identity failed')


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


@cache
def prefix(n, length):
    odd = 0
    for _ in range(length):
        odd += n % 2
        n = step(n)
    return n, odd


def score(phase, child, parent):
    return int((child, parent) == (0, phase)) - int((child, parent) == (phase, 0))


def run():
    checked_lifts = 0
    checked_heads = 0
    for power in range(6):
        factor = 2 ** power
        for parent in range(1, 129):
            for digit in range(factor):
                offset, weight = prefix(digit, power)
                actual, actual_weight = prefix(factor * parent + digit, power)
                require(actual == 3 ** weight * parent + offset and actual_weight == weight)
                checked_lifts += 1
            for r in range(81):
                child = 81 * parent + r
                vertical_parent = factor * child // 81
                require(vertical_parent - factor * parent == factor * r // 81)
                require(0 <= vertical_parent - factor * parent < factor)
                require(prefix(factor * child, power)[0] == child)
                checked_heads += 1

    binary_squares = 0
    all_squares = 0
    max_defect = 0
    for phase in (1, 2):
        for a, b, c, d in product(range(3), repeat=4):
            defect = score(phase, a, b) - score(phase, c, d) - score(phase, a, c) + score(phase, b, d)
            if len({a, b, c, d}) <= 2:
                require(defect == 0)
                binary_squares += 1
            require(abs(defect) <= 4)
            max_defect = max(max_defect, abs(defect))
            all_squares += 1
    return {
        'actual_shortcut_affine_lifts': checked_lifts,
        'actual_scaled_head_paths': checked_heads,
        'abstract_scored_squares': all_squares,
        'abstract_scored_squares_with_at_most_two_labels': binary_squares,
        'maximum_absolute_square_defect': max_defect,
        'scope': 'Exact finite equalities. The three abstract labels do not supply an ordinary nonconvergent witness.',
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
