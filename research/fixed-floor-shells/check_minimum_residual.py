"""Integer upper enclosure for the surviving terminal pressure. Requires NumPy."""

from fractions import Fraction

import numpy as np


DEPTH = 16
PRECISION = 1 << 36
LAST_VALUATION = 24
BLOCK_SIZE = 1 << 16


def main():
    cap = (3**DEPTH).bit_length() - 1 - DEPTH
    missing = cap + 1
    minimum = np.array([0], dtype=np.uint8)
    hits = np.array([False])
    pressure = np.array([PRECISION], dtype=np.uint64)
    for depth in range(1, DEPTH + 1):
        previous_size = len(pressure)
        modulus = 3 * previous_size
        next_minimum = np.full(modulus, missing, dtype=np.uint8)
        next_hits = np.tile(hits, 3)
        next_pressure = np.zeros(modulus, dtype=np.uint64)
        largest = int(pressure.max())
        assert 9 * largest + 4**LAST_VALUATION < 2**64
        omitted = (3 * largest + 4**LAST_VALUATION - 1) // 4**LAST_VALUATION
        # A node has at most one parity of legal valuations, whose squared
        # multipliers sum to at most 12/5. The extra roundoff is < 1 per term.
        assert Fraction(12, 5) * largest + LAST_VALUATION + omitted < 2**64
        for first_residue in (1, 2):
            next_pressure[first_residue::3] = omitted
            for left in range(0, previous_size, BLOCK_SIZE):
                right = min(left + BLOCK_SIZE, previous_size)
                indices = np.arange(left, right, dtype=np.int64)
                positions = slice(first_residue + 3 * left, first_residue + 3 * right, 3)
                for exponent in range(3 - first_residue, LAST_VALUATION + 1, 2):
                    scale = 1 << exponent
                    offset = (scale * first_residue - 1) // 3
                    parents = (offset + scale * indices) % previous_size
                    divisor = 4**exponent
                    rounded = (9 * pressure[parents] + divisor - 1) // divisor
                    next_pressure[positions] += rounded
                    if exponent <= cap + 1:
                        np.minimum(next_minimum[positions], minimum[parents] + exponent - 1,
                                   out=next_minimum[positions])
        boundary = (3**depth).bit_length() - 1 - depth
        next_hits |= next_minimum <= boundary
        minimum, hits, pressure = next_minimum, next_hits, next_pressure

    # Sum in checked chunks rather than assuming that the full numerator
    # fits in NumPy's fixed-width accumulator.
    unhit_mass = 0
    for left in range(0, len(hits), BLOCK_SIZE):
        right = min(left + BLOCK_SIZE, len(hits))
        values = pressure[left:right][~hits[left:right]]
        if len(values):
            assert len(values) * int(values.max()) < 2**64
            unhit_mass += int(values.sum())
    crossed = Fraction(int(hits.sum()), len(hits))
    remainder = Fraction(467, 500) * Fraction(unhit_mass, PRECISION * len(hits))
    low, high = (1 - crossed - remainder) * 10**6, (1 - crossed) * 10**6
    lower = low.numerator // low.denominator
    upper = -(-high.numerator // high.denominator)
    print("Certified odd-root density enclosure:", lower, upper, "over 1000000")
    print("Exact reached residues:", int(hits.sum()), "over", len(hits))
    print("Upper scaled unhit pressure numerator:", unhit_mass)


if __name__ == "__main__":
    main()
