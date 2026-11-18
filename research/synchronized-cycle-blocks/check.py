"""Finite exact controls for the equal-weight phase bound. Run with Python 3."""

from fractions import Fraction
from functools import reduce
from itertools import product
from math import gcd


def physical_digits(length):
    denominator = 2**length
    digits = {}
    for source in range(denominator):
        value = source
        word = ""
        for _ in range(length):
            bit = value % 2
            word += str(bit)
            value = (3 * value + 1 if bit else value) // 2
        multiplier = 3 ** word.count("1")
        assert word not in digits
        digits[word] = denominator * value - multiplier * source
    return digits


def boundary_values(schedule, multiplier, denominator):
    length = len(schedule)
    full = denominator**length - multiplier**length
    values = []
    for phase in range(length):
        constant = 0
        scale = 1
        for step in range(length):
            constant = multiplier * constant + scale * schedule[(phase + step) % length]
            scale *= denominator
        values.append(Fraction(constant, full))
    for phase, value in enumerate(values):
        assert denominator * values[(phase + 1) % length] == multiplier * value + schedule[phase]
    return values


def main():
    swaps = 0
    schedules = 0
    for length in range(2, 11):
        digits = physical_digits(length)
        for word, digit in digits.items():
            for position in range(length - 1):
                if word[position : position + 2] != "01":
                    continue
                suffix = word[position + 2 :]
                other = word[:position] + "10" + suffix
                stride = 2**position * 3 ** suffix.count("1")
                assert digit - digits[other] == stride
                swaps += 1
        if length > 4:
            continue
        for weight in range(1, length):
            multiplier = 3**weight
            denominator = 2**length
            alphabet = [c for word, c in digits.items() if word.count("1") == weight]
            for period in range(2, 5):
                for schedule in product(alphabet, repeat=period):
                    if len(set(schedule)) == 1:
                        continue
                    values = boundary_values(schedule, multiplier, denominator)
                    divisor = reduce(gcd, (c - min(schedule) for c in schedule))
                    full = denominator**period - multiplier**period
                    for value in values:
                        delta = (value - values[0]) * full
                        assert delta.denominator == 1 and delta.numerator % divisor == 0
                    if full > 0:
                        assert min(values) > Fraction(min(schedule), denominator - multiplier)
                        assert max(values) < Fraction(max(schedule), denominator - multiplier)
                    schedules += 1
    assert boundary_values((2, 1), 3, 4) == [Fraction(10, 7), Fraction(11, 7)]
    # Synthetic affine digits: the prime 7 in G cancels in the period-two denominator.
    assert boundary_values((8, 1), 3, 4) == [4, 5]
    print(f"Verified {swaps} physical swap differences and {schedules} formal mixed schedules.")


if __name__ == "__main__":
    main()
