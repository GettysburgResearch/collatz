"""Exact finite controls for the reducible binary substitution argument."""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import lcm


def zero_positions(word):
    ones = 0
    positions = []
    for letter in word:
        if letter == "1":
            ones += 1
        else:
            positions.append(ones)
    return positions


def words(alphabet, max_length):
    for length in range(1, max_length + 1):
        yield from product(alphabet, repeat=length)


def check_substitutions(counts):
    for image in words("01", 6):
        v = "".join(image)
        a, b = v.count("0"), v.count("1")
        if a < 2 or not b or v[0] != "0":
            continue
        image_positions = zero_positions(v)
        for d in range(1, 5):
            def expand(word):
                return "".join(v if letter == "0" else "1" * d for letter in word)

            for initial_ones in ([0, 2] if d == 1 else [0]):
                word = "1" * initial_ones + "0"
                for _ in range(3):
                    word = expand(word)
                old_positions = zero_positions(word)
                new_positions = zero_positions(expand(word))
                for i, previous in enumerate(old_positions):
                    for t, before_zero in enumerate(image_positions):
                        expected = b * i + d * previous + before_zero
                        if new_positions[a * i + t] != expected:
                            raise ValueError((v, d, i, t))
                        counts["zero_position_recurrences"] += 1
                if d == 1:
                    exponents = [(a - 1) * k - b * i for i, k in enumerate(new_positions)]
                    for ell in (1, 2, 3):
                        for n, value in enumerate(exponents):
                            h, r = divmod(n, a ** ell)
                            if value != exponents[h] + exponents[r] - exponents[0]:
                                raise ValueError((v, ell, n))
                            counts["digit_concatenations"] += 1
                counts["finite_substitution_examples"] += 1
            x_exp, y_exp = 1, 0
            for n in range(1, 9):
                x_exp, y_exp = a * x_exp, a * y_exp + b * d ** (n - 1)
                if a == d:
                    clock_sum = n * a ** (n - 1)
                else:
                    clock_sum = (a ** n - d ** n) // (a - d)
                if (x_exp, y_exp) != (a ** n, b * clock_sum):
                    raise ValueError((v, d, n))
                counts["triangular_matrix_powers"] += 1


def periodic_centers(alphabet, max_length, branches, label, counts):
    periods = {}
    for word in words(alphabet, max_length):
        slope, offset = Fraction(1), Fraction(0)
        for symbol in word:
            branch_slope, branch_offset = branches[symbol]
            offset += slope * branch_offset
            slope *= branch_slope
        periods[word] = offset / (1 - slope)
    for left, x in periods.items():
        for right, y in periods.items():
            length = lcm(len(left), len(right))
            same_word = left * (length // len(left)) == right * (length // len(right))
            if (x == y) != same_word:
                raise ValueError((left, right))
            counts[label] += 1


def main():
    counts = Counter()
    check_substitutions(counts)
    parity = {0: (Fraction(2), Fraction(0)), 1: (Fraction(2, 3), Fraction(-1, 3))}
    periodic_centers((0, 1), 5, parity, "parity_block_pairs", counts)
    gaps = {g: (Fraction(2 ** g, 3), Fraction(-1, 3)) for g in (1, 2, 3)}
    periodic_centers((1, 2, 3), 3, gaps, "gap_block_pairs", counts)
    for name, value in sorted(counts.items()):
        print(name, value)


if __name__ == "__main__":
    main()

