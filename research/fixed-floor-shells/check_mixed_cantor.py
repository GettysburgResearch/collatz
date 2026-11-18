"""Exact Haar cost of the finite universal screen, before any ordinary sampling."""

from fractions import Fraction


def crossing_bound(b):
    theta = Fraction(1, 2**b)
    coefficient = Fraction(1)
    mass = Fraction(1)
    while coefficient > theta:
        coefficient *= Fraction(2, 3)
        mass *= Fraction(3, 4)
    return theta**2 - (theta**2 - coefficient**2) * mass


def main():
    horizon = 80
    cutoff = 10
    max_occupation = Fraction(29, 11)
    initial_occupation = 1 + Fraction(2, 3)**horizon * (max_occupation - 1)
    assert 2**cutoff * (initial_occupation - 1) < 1
    total = Fraction(1, 2**cutoff)
    table = []
    for b in range(1, cutoff + 1):
        count = 0
        for label in range(1, 2**b, 2):
            if (pow(2, b + 1, 3) - label) % 3 == 0:
                continue
            vertex = label
            excess = 0
            for _ in range(horizon):
                value = 3 * vertex - 1
                exponent = (value & -value).bit_length() - 1
                vertex = value >> exponent
                excess += exponent - 1
                if excess > b:
                    break
            if excess <= b:
                count += 1
        table.append(count)
        total += count * crossing_bound(b)
    assert table == [0, 2, 1, 2, 3, 4, 6, 8, 13, 20]
    assert total < Fraction(137394, 10**6)
    initial_good = Fraction(2, 3) - Fraction(517167, 10**6)
    assert initial_good - total > Fraction(12, 1000)
    print('retained affine tests by b:', table)
    print('residual cost < 137394/1000000; common good unit mass > 12/1000')


if __name__ == '__main__':
    main()
