"""Bound the ternary residue mass of first contracting inverse words."""

from fractions import Fraction


def first_contractions(depth):
    """Count words at the first prefix with 2**sum(exponents) < 3**length."""
    cap = (3**depth).bit_length() - 1
    surviving = [1] + [0] * cap
    counts = []
    for length in range(1, depth + 1):
        threshold = (3**length).bit_length() - 1
        next_row = [0] * (cap + 1)
        partial = 0
        count = 0
        for weight in range(1, cap + 1):
            partial += surviving[weight - 1]
            if weight <= threshold:
                count += partial
            else:
                next_row[weight] = partial
        counts.append(count)
        surviving = next_row
    return counts


if __name__ == '__main__':
    depth = 200
    counts = first_contractions(depth)
    mass = sum(Fraction(count, 3**length) for length, count in enumerate(counts, 1))
    if counts[:2] != [1, 1] or mass >= Fraction(518, 1000):
        raise AssertionError('first-contraction word bound failed')
    if Fraction(27, 32)**40 >= Fraction(2, 1000):
        raise AssertionError('infinite geometric tail bound failed')
    print('First 200 word-count levels give mass below 0.518; tail below 0.002.')
