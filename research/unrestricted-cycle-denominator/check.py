"""Replay a finite full-gcd example with exact shortcut arithmetic."""

from fractions import Fraction
from math import gcd, prod


def affine(word):
    slope, offset, denominator = 1, 0, 1
    for bit in word:
        if bit == "1":
            slope *= 3
            offset = 3 * offset + denominator
        denominator *= 2
    return slope, offset, denominator


def block(bits, odd_count, length):
    pairs = "".join("01" if bit else "10" for bit in bits)
    return pairs + "1" * (odd_count - len(bits)) + "0" * (length - odd_count - len(bits))


def test_boundary_identity(word, count):
    length = len(word) // count
    weight = word.count("1") // count
    blocks = [affine(word[i:i + length]) for i in range(0, len(word), length)]
    sums = [0]
    for i in range(0, len(word), length):
        sums.append(sums[-1] + word[i:i + length].count("1") - weight)
    assert sums[-1] == 0
    peak = max(sums)
    a, c, b = affine(word)
    start = Fraction(c, b - a)
    state = start
    normalized = []
    forcings = []
    multiplier = Fraction(3**weight, 2**length)
    for i, (block_a, block_c, block_b) in enumerate(blocks):
        normalized.append(3 ** (peak - sums[i]) * state)
        forcings.append(Fraction(3 ** (peak - sums[i + 1]) * block_c, block_b))
        state = (block_a * state + block_c) / block_b
    assert state == start
    for i, z in enumerate(normalized):
        assert normalized[(i + 1) % count] == multiplier * z + forcings[i]

    mean = sum(forcings) / count
    partial = [0]
    for value in forcings:
        partial.append(partial[-1] + value - mean)
    discrepancy = max(partial) - min(partial)
    assert max(normalized) - min(normalized) <= 2 * discrepancy
    return discrepancy


def test_coprime_seam():
    word = "1101010"
    length = len(word)
    weight = word.count("1")
    width = pow(weight, -1, length)
    reference = (width * weight - 1) // length
    multiplier = Fraction(3**reference, 2**width)
    blocks = [(word * width)[i:i + width] for i in range(0, width * length, width)]
    excess = [0]
    for block_word in blocks:
        excess.append(excess[-1] + block_word.count("1") - reference)
    peak = max(excess)
    forcing = [Fraction(3 ** (peak - excess[i + 1]) * affine(w)[1], 2**width)
               for i, w in enumerate(blocks)]
    total = sum(multiplier ** (length - 1 - i) * f for i, f in enumerate(forcing))
    start = total / (Fraction(1, 3) - multiplier**length)
    assert start == 3**peak * Fraction(101, 47)
    forcing[-1] += Fraction(2, 3) * start
    trajectory = [start]
    for f in forcing:
        trajectory.append(multiplier * trajectory[-1] + f)
    assert trajectory.pop() == start
    mean = sum(trajectory) / length
    variance = sum((v - mean) ** 2 for v in trajectory) / length
    assert variance == Fraction(204860, 108241) < Fraction(length**2 - 1, 12)


def check():
    test_coprime_seam()
    odd_count, length = 41, 65
    periods = (5, 7)
    baseline = block((False, False), odd_count, length)
    slope, constant, denominator = affine(baseline)
    predicted = Fraction(constant, denominator - slope)
    for column, period in enumerate(periods):
        bits = [j == column for j in range(len(periods))]
        impulse = affine(block(bits, odd_count, length))[1] - constant
        predicted += Fraction(impulse * slope ** (period - 1), denominator**period - slope**period)

    word = "".join(
        block([i % p == 0 for p in periods], odd_count, length)
        for i in range(prod(periods))
    )
    assert (word + word).find(word, 1) == len(word)
    a, numerator, b = affine(word)
    full = b - a
    assert Fraction(numerator, full) == predicted
    for period in periods:
        factor = (denominator**period - slope**period) // (denominator - slope)
        clean = factor // gcd(factor, denominator - slope)
        assert clean > 1 and predicted.denominator % clean == 0

    state = predicted
    for bit in word:
        assert state.numerator % 2 == int(bit)
        assert state.denominator == predicted.denominator
        state = ((3 * state + 1) if bit == "1" else state) / 2
    assert state == predicted

    assert test_boundary_identity(word, prod(periods)) < Fraction(prod(periods) - 1, 2)
    test_boundary_identity("11100100", 2)  # unequal block weights
    test_boundary_identity("10", 1)  # actual positive integer cycle
    for edit in ("0", "1", "011", "1011010", baseline):
        edit_a, edit_c, edit_b = affine(edit)
        new_a, new_c, new_b = affine(word + edit)
        bound = (edit_a - edit_b) * state.numerator + state.denominator * edit_c
        assert bound and bound % gcd(abs(new_b - new_a), new_c) == 0
    print(f"Verified {len(word)} rotations, full denominator {full.bit_length()} bits, "
          f"reduced denominator {predicted.denominator.bit_length()} bits and five edits.")


if __name__ == "__main__":
    check()
