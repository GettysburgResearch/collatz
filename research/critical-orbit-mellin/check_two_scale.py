"""Compute the finite two-scale array by exhaustive ordinary inverse paths."""
from fractions import Fraction
from itertools import product


CYCLE_THRESHOLD = 1 - Fraction(1, 2**32)
THRESHOLDS = (Fraction(1, 100), Fraction(1, 10), Fraction(1, 2), Fraction(3, 4), CYCLE_THRESHOLD)


def inverse_source(target, word):
    state = target
    for valuation in reversed(word):
        parent, remainder = divmod((state << valuation) - 1, 3)
        if remainder or parent < 1 or parent % 2 == 0:
            return None
        state = parent
    return state


def replay(depth):
    slope_numerator = 3**depth
    counts = [0] * len(THRESHOLDS)
    totals = [Fraction(0) for _ in THRESHOLDS]
    offset_moment = Fraction(0)
    excluded_one = 0
    words = 0
    for word in product(range(1, 2 * depth + 1), repeat=depth):
        words += 1
        legal = []
        for target in range(1, 2 * slope_numerator + 1, 2):
            source = inverse_source(target, word)
            if source is not None:
                legal.append((target, source))
        assert len(legal) == 1
        target, source = legal[0]

        # Independently replay the accelerated map, and build its affine offset.
        offset, denominator, state = 0, 1, source
        for expected in word:
            value = 3 * state + 1
            valuation = (value & -value).bit_length() - 1
            assert valuation == expected
            state = value >> valuation
            offset = 3 * offset + denominator
            denominator <<= valuation
        assert state == target
        assert target * denominator == slope_numerator * source + offset
        if target == 1:
            excluded_one += 1
            continue

        normalized_offset = Fraction(offset, denominator * target)
        weight = Fraction(slope_numerator, denominator * target)
        assert normalized_offset == 1 - weight * source
        offset_moment += weight * normalized_offset
        for index, threshold in enumerate(THRESHOLDS):
            if normalized_offset >= threshold:
                counts[index] += 1
                totals[index] += weight
    cycle_detected = counts[-1] > 0
    return words, excluded_one, counts, totals, int(cycle_detected) + offset_moment / depth


if __name__ == "__main__":
    print("Q words target_one threshold qualifying D_Q")
    for q in range(1, 5):
        words, target_one, counts, totals, scalar = replay(q)
        for threshold, count, total in zip(THRESHOLDS, counts, totals):
            print(q, words, target_one, threshold, count, total)
        print("C_Q", q, scalar)
