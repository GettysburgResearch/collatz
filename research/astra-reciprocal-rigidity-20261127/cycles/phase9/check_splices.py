"""Exact finite controls for concatenated laps and proper cyclic factors."""

from fractions import Fraction
from functools import cache
from itertools import product
from math import gcd


def require(condition, message):
    if not condition:
        raise ValueError(message)


@cache
def anchor(word):
    intercept = 0
    for position, bit in enumerate(word):
        if bit:
            intercept = 3 * intercept + (1 << position)
    coefficient_gap = (1 << len(word)) - 3**sum(word)
    upper_intercept = (1 << (len(word) - sum(word))) * (3**sum(word) - (1 << sum(word)))
    require(0 <= intercept <= upper_intercept, "sorted-bit intercept bound")
    return Fraction(intercept, coefficient_gap)


def advance(value, bit):
    require(value.numerator % 2 == bit, "wrong native parity")
    return (3 * value + 1) / 2 if bit else value / 2


def words(length):
    return product((0, 1), repeat=length)


def check_splices():
    alphabet = [word for length in range(1, 4) for word in words(length)]
    lists = extrema = wrapped = 0
    for blocks in product(alphabet, repeat=3):
        phases = [anchor(block) for block in blocks]
        low, high = min(phases), max(phases)
        if low == high or low < 0 <= high:
            continue
        lists += 1
        for index in range(len(blocks)):
            ordered = blocks[index:] + blocks[:index]
            root = anchor(sum(ordered, ()))
            require(low < root < high, "positive convex coefficients")
            phase = phases[index]
            if phase not in (low, high):
                continue
            extrema += 1
            run_length = 0
            for offset, block in enumerate(ordered):
                if anchor(block) != phase:
                    break
                run_length += len(block)
                if index + offset >= len(blocks):
                    wrapped += 1
            difference = (root - phase) * root.denominator * phase.denominator
            require(difference.denominator == 1 and difference != 0, "extremal separation")
            require(difference.numerator % (1 << run_length) == 0, "dyadic divisor")
            require(root.denominator * phase.denominator * (high - low) > (1 << run_length),
                    "combined extremal run")
    require(anchor((1, 0)) == 1 and anchor((1,)) == -1 and anchor((1, 0, 1)) == -7,
            "mixed-side counterexample")
    return lists, extrema, wrapped


def check_factors():
    cycles = factors = representations = 0
    for length in range(2, 11):
        for necklace in words(length):
            rotations = [necklace[i:] + necklace[:i] for i in range(length)]
            if min(rotations) != necklace or len(set(rotations)) != length:
                continue
            cycles += 1
            for lap in rotations:
                source = anchor(lap)
                denominator = source.denominator
                for size in range(1, length):
                    factor = lap[:size]
                    shadow = anchor(factor)
                    q = shadow.denominator
                    k = (source - shadow) * denominator * q / (1 << size)
                    require(k.denominator == 1 and k != 0, "nonzero integral proper-factor pin")
                    y, x = source, shadow
                    odd_count = 0
                    for position, bit in enumerate(factor, 1):
                        odd_count += bit
                        y, x = advance(y, bit), advance(x, bit)
                        expected = k * 3**odd_count * (1 << (size - position))
                        require(denominator * q * (y - x) == expected, "transported pin")
                        representations += 1
                    delta = denominator * (y - source)
                    gap = abs((1 << size) - 3**odd_count)
                    require(delta.denominator == 1 and delta != 0, "displacement")
                    require(q // gcd(q, denominator) == gap // gcd(gap, delta.numerator),
                            "full denominator vs integer displacement")
                    factors += 1
    return cycles, factors, representations


if __name__ == "__main__":
    lists, extrema, wrapped = check_splices()
    cycles, factors, representations = check_factors()
    print(f"{lists} same-side mixed lists, {extrema} extremal runs, {wrapped} wrapped run steps")
    print(f"{cycles} primitive necklaces, {factors} proper factors, {representations} pin transports")
