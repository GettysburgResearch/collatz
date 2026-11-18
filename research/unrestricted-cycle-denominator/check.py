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


def check():
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

    for edit in ("0", "1", "011", "1011010", baseline):
        edit_a, edit_c, edit_b = affine(edit)
        new_a, new_c, new_b = affine(word + edit)
        bound = (edit_a - edit_b) * state.numerator + state.denominator * edit_c
        assert bound and bound % gcd(abs(new_b - new_a), new_c) == 0
    print(f"Verified {len(word)} rotations, full denominator {full.bit_length()} bits, "
          f"reduced denominator {predicted.denominator.bit_length()} bits and five edits.")


if __name__ == "__main__":
    check()
