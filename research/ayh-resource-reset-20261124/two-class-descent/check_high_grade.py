"""Exact finite checks of normalized offsets and fixed-weight dyadic meshes."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
import json


def word_data(word):
    power = 0
    numerator = 0
    for index, bit in enumerate(word):
        numerator = (3 if bit else 1) * numerator + bit * 2**index
        power += bit
    return power, numerator


def step(x):
    return ((3 * x + 1) if x % 2 else x) // 2


def require(value):
    if not value:
        raise RuntimeError('finite shadow identity failed')


def main():
    total = 0
    for length in range(1, 15):
        seen = defaultdict(set)
        for word in product((0, 1), repeat=length):
            p, numerator = word_data(word)
            residue = numerator % 2**length
            require(residue not in seen[p])
            seen[p].add(residue)
            total += 1
    paths = 0
    largest = Fraction(0)
    for length in range(1, 9):
        for offset in (-7, 0, 11, 3 ** (2*length) + 5):
            grade = 2 * length
            start = -Fraction(offset, 3**grade)
            freq = Counter()
            for residue in range(2**length):
                x = 2**length+residue
                y = 3**grade * x + offset
                s = grade
                ideal = start
                word = []
                for _ in range(length):
                    b, e = x % 2, y % 2
                    s += e-b
                    ideal = (3**b * ideal + b)/2
                    x, y = step(x), step(y)
                    word.append(b)
                actual = x-Fraction(y, 3**s)
                error = abs(actual-ideal)
                require(error < Fraction(1, 2**length))
                p, numerator = word_data(word)
                require(ideal == (3**p * start+numerator)/2**length)
                freq[tuple(word)] += 1
                largest = max(largest, error * 2**length)
                paths += 1
            require(len(freq) == 2**length and max(freq.values()) == 1)
    print(json.dumps({'fixed_weight_words': total, 'physical_fresh_histories': paths,
                      'max_scaled_error_tested': str(largest)}, sort_keys=True))


if __name__ == '__main__':
    main()
