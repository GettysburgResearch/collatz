"""Exact finite controls for native macro gluing and short junction repairs."""

from fractions import Fraction
from itertools import permutations, product
from math import gcd, lcm
from random import Random


def require(expression, message):
    if not expression:
        raise ArithmeticError(message)


def carry(bits):
    value = 0
    for index, bit in enumerate(bits):
        if bit:
            value = 3 * value + (1 << index)
    return value


def native_path(start, length):
    current = Fraction(start)
    bits = []
    for _ in range(length):
        require(current.denominator % 2 == 1, "source must be integral at 2")
        bit = current.numerator % 2
        bits.append(bit)
        current = (3 * current + 1) / 2 if bit else current / 2
    return start, current, tuple(bits)


def multiplier(bits):
    return Fraction(3 ** sum(bits), 1 << len(bits))


def affine(bits, start):
    return multiplier(bits) * start + Fraction(carry(bits), 1 << len(bits))


def test_joins(pieces):
    word = sum((item[2] for item in pieces), ())
    determinant = (1 << len(word)) - 3 ** sum(word)
    value = carry(word)
    true_residual = value - determinant * pieces[0][0]
    position = odd_count = 0
    residuals = []
    deltas = []
    for i, (start, end, bits) in enumerate(pieces):
        require(affine(bits, start) == end, "recorded affine endpoint")
        position += len(bits)
        odd_count += sum(bits)
        difference = end - pieces[(i + 1) % len(pieces)][0]
        deltas.append(difference)
        scale = (1 << position) * 3 ** (sum(word) - odd_count)
        residuals.append(scale * difference)
    require(sum(residuals) == true_residual, "complete gluing residual")
    denominator = lcm(*(Fraction(item).denominator for path in pieces for item in path[:2]))
    require((denominator * true_residual).denominator == 1, "cleared residual")
    if determinant > 0:
        common = gcd(determinant, value)
        require(int(denominator * true_residual) % common == 0, "full modulus retained")
        root = Fraction(value, determinant)
        require(native_path(root, len(word))[1:] == (root, word), "canonical root replay")
    for first in range(len(pieces)):
        effective = deltas[first]
        transported = pieces[first][1]
        for last in range(first, len(pieces)):
            if last > first:
                effective = multiplier(pieces[last][2]) * effective + deltas[last]
                transported = affine(pieces[last][2], transported)
            next_origin = pieces[(last + 1) % len(pieces)][0]
            require(effective == transported - next_origin, "cluster transport")
            position = sum(len(p[2]) for p in pieces[: last + 1])
            odd_count = sum(sum(p[2]) for p in pieces[: last + 1])
            scale = (1 << position) * 3 ** (sum(word) - odd_count)
            require(scale * effective == sum(residuals[first : last + 1]), "cluster compression")
    return true_residual, deltas


def test_interval_edits(left, right, blocks):
    rebased = list(left)
    predicted = 0
    for start, end in blocks:
        old = left[start:end]
        new = right[start:end]
        require(sum(old) == sum(new), "separate odd clock preserved")
        rebased[start:end] = new
        predicted += (1 << start) * 3 ** sum(left[end:]) * (carry(new) - carry(old))
    require(tuple(rebased) == right, "unchanged gaps")
    require(predicted == carry(right) - carry(left), "full window difference")
    require((predicted != 0) == (left != right), "carry injection at equal clocks")


def main():
    random = Random(192043)
    gluing_cases = edit_cases = 0
    for count in range(1, 8):
        for _ in range(120):
            pieces = []
            for _ in range(count):
                start = Fraction(random.randrange(1, 10000), random.choice((1, 1, 5, 7, 9)))
                pieces.append(native_path(start, random.randrange(1, 39)))
            test_joins(pieces)
            gluing_cases += 1
    for size in range(2, 6):
        for left_raw in product((0, 1), repeat=2 * size):
            left = tuple(left_raw)
            for shift in range(1, size):
                first = left[:size]
                last = left[size:]
                right = first[shift:] + first[:shift] + last[-shift:] + last[:-shift]
                test_interval_edits(left, right, [(0, size), (size, 2 * size)])
                edit_cases += 1
    for order in permutations(range(4)):
        starts = [1, 47, 5, 27]
        pieces = [native_path(starts[i], [24, 21, 10, 34][i]) for i in order]
        test_joins(pieces)
        gluing_cases += 1
    # The inserted copy 5 -> 8 -> 4 has the same two bits as 1 -> 2 -> 1.
    # The two actual discontinuities therefore repair through one short piece.
    residual, deltas = test_joins([native_path(1, 40), native_path(5, 2), native_path(1, 42)])
    require(residual == 0 and deltas == [-4, 3, 0], "genuine zero clustered branch")
    print(f"{gluing_cases} path gluings, {edit_cases} window repairs, one exact short-cluster cancellation")


if __name__ == "__main__":
    main()
