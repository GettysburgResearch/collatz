"""Exact finite checks for the real/ternary signed transfer calculation."""

from fractions import Fraction
from itertools import product


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def valuation_three(value):
    n = abs(value.numerator)
    d = value.denominator
    require(n > 0 and d % 3 != 0, "pole must be distinct and ternary integral")
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


def affine(word):
    multiplier = Fraction(1)
    offset = Fraction(0)
    for bit in word:
        if bit:
            multiplier *= 3
            offset = 3 * offset + 1
        multiplier /= 2
        offset /= 2
    return multiplier, offset


def inverse(y, word):
    for bit in reversed(word):
        if bit:
            if (2 * y - 1) % 3:
                return None
            y = (2 * y - 1) // 3
        else:
            y *= 2
    return y


def check_one_generation(z, y, base):
    def pole(z0, y0):
        return base ** valuation_three(Fraction(y0) - z0)

    a, b = Fraction(2, 5), Fraction(7, 4)
    even, odd = z / 2, (3 * z + 1) / 2
    left = a * pole(even, y) + b / base * pole(odd, y)
    right = a * pole(z, 2 * y)
    if y % 3 == 2:
        right += b * pole(z, (2 * y - 1) // 3)
    else:
        right += b / base
    require(left == right, "one-generation transfer identity")


def main():
    base = Fraction(13, 5)
    tested = 0
    for d in range(9):
        for word in product((0, 1), repeat=d):
            q = sum(word)
            mult, offset = affine(word)
            z = offset - mult
            require(z.denominator != 1 or z == -1, "unexpected integral pole")
            for y in range(1, 49):
                actual = inverse(y, word)
                v = valuation_three(y - z)
                require((actual is not None) == (v >= q), "wrong inverse threshold")
                if actual is not None:
                    require(actual > 0 and mult * actual + offset == y,
                            "wrong inverse source")
                    require(v == q + valuation_three(Fraction(actual + 1)),
                            "wrong diagonal valuation")
                    require(mult * actual <= y, "wrong physical weight")
                check_one_generation(z, y, base)
                tested += 1
    print(f"{tested} pole/target pairs: transport, integral diagonal, and positive weights pass")


if __name__ == "__main__":
    main()
