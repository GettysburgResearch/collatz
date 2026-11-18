"""Enclose the true ordinary bilateral survival densities using finite ternary levels."""

import argparse
from fractions import Fraction

import numpy as np


PRECISION = 1 << 34
LAST_EXPONENT = 23
BLOCK_SIZE = 1 << 15


def upper_pressure_total(values):
    total = 0
    for left in range(0, len(values), BLOCK_SIZE):
        block = values[left:left + BLOCK_SIZE]
        assert not len(block) or len(block) * int(block.max()) < 2**64
        total += int(block.sum(dtype=np.uint64))
    return total


def decimal_interval(lower, upper):
    scale = 10**6
    low = scale * max(0, lower)
    high = scale * upper
    return low.numerator // low.denominator, -(-high.numerator // high.denominator)


def calculate(depth):
    ranks = [(Fraction(1), 0, 0)]
    for length in range(1, depth + 1):
        for total in range(length, (3**length).bit_length()):
            ranks.append((Fraction(3**length, 2**total), length, total))
    ranks.sort()
    rank_lookup = {(length, total): index for index, (_, length, total) in enumerate(ranks)}
    assert len({slope for slope, _, _ in ranks}) == len(ranks)
    cap = (3**depth).bit_length() - 1 - depth
    missing = cap + 1
    minimum = np.array([0], dtype=np.uint16)
    winner = np.array([0], dtype=np.uint16)
    pressure = np.array([PRECISION], dtype=np.uint64)
    previous_second_moment = Fraction(1)
    for length in range(1, depth + 1):
        small_modulus = len(winner)
        modulus = 3 * small_modulus
        next_minimum = np.full(modulus, missing, dtype=np.uint16)
        next_winner = np.tile(winner, 3)
        next_pressure = np.zeros(modulus, dtype=np.uint64)
        maximum = int(pressure.max())
        assert 9 * maximum + 4**LAST_EXPONENT < 2**64
        tail = (3 * maximum + 4**LAST_EXPONENT - 1) // 4**LAST_EXPONENT
        assert Fraction(12, 5) * maximum + LAST_EXPONENT + tail < 2**64
        for unit in (1, 2):
            for start in range(0, small_modulus, BLOCK_SIZE):
                stop = min(start + BLOCK_SIZE, small_modulus)
                positions = slice(unit + 3*start, unit + 3*stop, 3)
                indices = np.arange(start, stop, dtype=np.int64)
                next_pressure[positions] = tail
                for exponent in range(3 - unit, LAST_EXPONENT + 1, 2):
                    factor = 2**exponent
                    parents = ((factor * unit - 1)//3 + factor * indices) % small_modulus
                    rounded = (9 * pressure[parents] + 4**exponent - 1) // 4**exponent
                    next_pressure[positions] += rounded
                    if exponent <= cap + 1:
                        np.minimum(next_minimum[positions], minimum[parents] + exponent - 1,
                                   out=next_minimum[positions])
        boundary = (3**length).bit_length() - 1 - length
        new_ranks = np.zeros(missing + 1, dtype=np.uint16)
        for excess in range(boundary + 1):
            new_ranks[excess] = rank_lookup[length, length + excess]
        np.maximum(next_winner, new_ranks[next_minimum], out=next_winner)
        minimum, winner, pressure = next_minimum, next_winner, next_pressure
        counts = np.bincount(winner, minlength=len(ranks))
        second_moment = sum(slope**2 * int(count)/modulus
                            for (slope, _, _), count in zip(ranks, counts))
        increment = second_moment - previous_second_moment
        if length > 1:
            assert increment <= last_increment
        last_increment = increment
        previous_second_moment = second_moment

    upper = [Fraction(0) for _ in range(depth + 1)]
    loss = [Fraction(0) for _ in range(depth + 1)]
    for index, (slope, length, _) in enumerate(ranks):
        if not counts[index]:
            continue
        upper[length] += slope * int(counts[index]) / modulus
        numerator = upper_pressure_total(pressure[winner == index])
        loss[length] += Fraction(467*numerator, 500*PRECISION*modulus) / slope
    return [(upper[j] - loss[j], upper[j]) for j in range(depth + 1)], last_increment


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--depth', type=int, default=12, choices=range(1, 17))
    args = parser.parse_args()
    intervals, increment = calculate(args.depth)
    print('Ternary depth', args.depth)
    print('Ordinary survival probability, integer bounds in millionths')
    for j, (lower, upper) in enumerate(intervals):
        print(j, *decimal_interval(lower, upper))
    print('Upper bound for the infinite tilted survival probability in millionths',
          decimal_interval(0, increment)[1])


if __name__ == '__main__':
    main()
