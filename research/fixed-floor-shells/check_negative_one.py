"""Exact finite checks for the negative-one inverse shadow."""

from fractions import Fraction
from math import comb


MIRROR_DISTORTION = 3**10
LAST_FINITE_START = (8 * MIRROR_DISTORTION) // 3


def check_distortion():
    total = Fraction()
    cutoff = 256
    for k in range(1, cutoff):
        high_words = 0
        minimum_count = 2 ** (k - 1)
        for odd_cut in reversed(range(k + 1)):
            minimum_count = min(minimum_count, k + 2 * 3**odd_cut + high_words)
            high_words += comb(k, odd_cut)
        total += Fraction(minimum_count, 3 * 2**k - 1)

    assert 27 * 16**5 <= 31**5
    ratio_low = Fraction(31, 32)
    ratio_high = Fraction(50, 51)
    # Sum_{k>=cutoff} k/2^k = (cutoff+1)/2^(cutoff-1).
    tail = (
        2 * ratio_low**cutoff / (1 - ratio_low)
        + ratio_high**cutoff / (1 - ratio_high)
        + Fraction(cutoff + 1, 2 ** (cutoff - 1))
    ) / 2
    assert total + tail < 10
    return (1000 * (total + tail)).__ceil__()


def check_small_starts():
    # For paths first hitting 1, store exact odd depth and valuation total.
    # A known disjoint cycle or a path leading to one is marked with None.
    data = {1: (0, 0)}
    minimum = None
    minimizers = []
    for start in range(3, LAST_FINITE_START + 1, 2):
        x = start
        path = []
        seen = set()
        while x not in data and x not in seen:
            seen.add(x)
            value = 3 * x - 1
            exponent = (value & -value).bit_length() - 1
            path.append((x, exponent))
            x = value >> exponent
        result = data.get(x)
        for x, exponent in reversed(path):
            if result is not None:
                q, divisions = result
                result = (q + 1, divisions + exponent)
            data[x] = result
        if data[start] is None:
            continue
        q, divisions = data[start]
        multiplier = Fraction(2**divisions, 3**q)
        if minimum is None or multiplier < minimum:
            minimum = multiplier
            minimizers = [start]
        elif multiplier == minimum:
            minimizers.append(start)
    assert minimum == Fraction(8, 3) and minimizers == [3]
    return len(data)


if __name__ == '__main__':
    print('Reciprocal log bound, in thousandths:', check_distortion())
    print('Largest finite starting threshold:', LAST_FINITE_START)
    print('Distinct mirror states classified:', check_small_starts())
