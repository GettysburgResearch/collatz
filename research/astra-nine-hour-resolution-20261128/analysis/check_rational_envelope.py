"""Exact finite checks of affine, cylinder, first-hit and counting interfaces."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import gcd


def branches(value):
    return (value / 2, (3 * value + 1) / 2)


def ternary_residue(value, modulus):
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def cylinder_rows(height):
    rows = [[Fraction(1)]]
    for depth in range(1, height + 1):
        modulus = 3 ** depth
        period = 2 * (modulus // 3)
        row = []
        for residue in range(modulus):
            total = Fraction(0)
            for exponent in range(1, period + 1):
                numerator = (2 ** exponent) * residue - 1
                if numerator % 3 == 0:
                    position = (numerator // 3) % (modulus // 3)
                    total += Fraction(3, 2 ** exponent) * rows[-1][position]
            row.append(total / (1 - Fraction(1, 2 ** period)))
        assert sum(row) == modulus
        rows.append(row)
    return rows


def reduced_leaves(value, length):
    if length == 0:
        yield value, 0
        return
    choices = [(2 * value, 0)]
    if ternary_residue(value, 3) == 2:
        choices.append(((2 * value - 1) / 3, 1))
    for parent, increment in choices:
        for leaf, grade in reduced_leaves(parent, length - 1):
            yield leaf, grade + increment


def check_cylinder_expansion(rows):
    checks = 0
    for denominator in (1, 2, 4, 5, 7, 8, 10, 20, 28, 40):
        for numerator in range(-22, 23):
            if gcd(numerator, denominator) != 1:
                continue
            value = Fraction(numerator, denominator)
            power = (denominator & -denominator).bit_length() - 1
            leaves = list(reduced_leaves(value, power))
            assert all(leaf.denominator % 2 for leaf, _ in leaves)
            for depth in range(power, len(rows)):
                expected = rows[depth][ternary_residue(value, 3 ** depth)]
                actual = sum(Fraction(3 ** grade, 2 ** power) *
                             rows[depth - grade][ternary_residue(leaf, 3 ** (depth - grade))]
                             for leaf, grade in leaves)
                assert actual == expected
                checks += 1
    return checks


def actual_step(numerator, denominator):
    return (3 * numerator + denominator) // 2 if numerator % 2 else numerator // 2


def check_signed_leaves():
    instances = 0
    for denominator in (1, 5, 7, 11):
        for target in range(-12, 13):
            if not target:
                continue
            for depth in range(1, 5):
                sources = set()
                for exponents in product(range(1, 6), repeat=depth):
                    leaf = target
                    for exponent in exponents:
                        numerator = (2 ** exponent) * leaf - denominator
                        if numerator % 3:
                            break
                        leaf = numerator // 3
                    else:
                        assert leaf not in sources
                        sources.add(leaf)
                        current = leaf
                        grade = 0
                        for _ in range(sum(exponents)):
                            grade += current % 2
                            current = actual_step(current, denominator)
                        assert current == target and grade == depth
                        instances += 1
    return instances


def check_cycles(rows):
    for root, period in ((Fraction(-1), 1), (Fraction(-5), 3),
                         (Fraction(-19, 11), 4), (Fraction(1, 5), 3)):
        current = root
        count = 0
        for _ in range(period):
            odd = current.numerator % 2
            count += odd
            current = branches(current)[odd]
        assert current == root
        slope = Fraction(3 ** count, 2 ** period)
        assert (slope > 1) == (root < 0)
        for depth in range(count, len(rows)):
            here = rows[depth][ternary_residue(root, 3 ** depth)]
            earlier = rows[depth-count][ternary_residue(root, 3 ** (depth-count))]
            assert here >= slope * earlier
    assert (Fraction(-1), 1) in set(reduced_leaves(Fraction(1, 8), 3))


def check_positive_grid(maximum=12):
    words = [(Fraction(1, 8), 0)]
    for depth in range(1, maximum + 1):
        words = [(child, grade + bit) for value, grade in words
                 for bit, child in enumerate(branches(value))]
        by_grade = defaultdict(set)
        for value, grade in words:
            assert value.denominator == 2 ** (depth + 3)
            assert value not in by_grade[grade]
            by_grade[grade].add(value)
    return len(words), len(set(value for value, _ in words))


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Run without Python optimization so assertions execute.')
    densities = cylinder_rows(4)
    cylinder_count = check_cylinder_expansion(densities)
    signed_count = check_signed_leaves()
    check_cycles(densities)
    words, distinct = check_positive_grid()
    print(f'{cylinder_count} exact cylinder expansions; {signed_count} legal signed words; '
          f'4 physical cycle examples; {words} terminal words and {distinct} distinct positive grid points.')
