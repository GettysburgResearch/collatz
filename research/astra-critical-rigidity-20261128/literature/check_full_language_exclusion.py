"""Exact controls for the explicit two-clock parity word and its finite factors."""

from fractions import Fraction
from itertools import product
from math import isqrt

A, N = 128, 243


def require(condition, description):
    if not condition:
        raise ArithmeticError(description)


def cell(first, second):
    return "111" + ("01" if first else "10") + ("01" if second else "10")


def cycle_word(m):
    return "".join(cell(j % m == 0, j % (m + 1) == 0) for j in range(m * (m + 1)))


def carry(word):
    value = 0
    for i, bit in enumerate(word):
        if bit == "1":
            value = 3 * value + (1 << i)
    return value


def predicted_root(m):
    def impulse(period, change):
        return Fraction(change * N ** (period - 1), A**period - N**period)

    return Fraction(227, A - N) + impulse(m, 24) + impulse(m + 1, 32)


def least_period(word):
    border = [0] * len(word)
    for i in range(1, len(word)):
        j = border[i - 1]
        while j and word[i] != word[j]:
            j = border[j - 1]
        if word[i] == word[j]:
            j += 1
        border[i] = j
    proposed = len(word) - border[-1]
    return proposed if len(word) % proposed == 0 else len(word)


def shortest_periodic_partition(word, bound):
    # For each start and candidate period, compute the longest permitted factor.
    # All shorter lengths are permitted as well. Right-to-left optimum cannot
    # increase when a leading symbol is deleted, so taking the longest is optimal.
    size = len(word)
    common = [0] * (bound + 1)
    pieces = [0] * (size + 1)
    for start in range(size - 1, -1, -1):
        longest = 1
        for period in range(1, bound + 1):
            if start + period < size and word[start] == word[start + period]:
                common[period] += 1
            else:
                common[period] = 0
            longest = max(longest, min(size - start, period + common[period]))
        pieces[start] = 1 + pieces[start + longest]
    return pieces[0]


def factor_is_periodic(word, bound):
    return any(all(word[i] == word[i - p] for i in range(p, len(word)))
               for p in range(1, bound + 1))


def brute_partition(word, bound):
    best = [0]
    for j in range(1, len(word) + 1):
        best.append(1 + min(best[i] for i in range(j)
                            if factor_is_periodic(word[i:j], bound)))
    return best[-1]


def lex_word(index):
    # Bijection 1,2,3,... -> empty, 0, 1, 00, 01, ...
    return bin(index)[3:]


def copies(group):
    # ceil(sqrt(ceil(log2(group+2))))
    return 1 + isqrt((group + 1).bit_length() - 1)


def main():
    for first, second in product((False, True), repeat=2):
        require(carry(cell(first, second)) == 227 + 24 * first + 32 * second,
                "cell carry")

    clocks = [2, 3, 4, 5, 7, 8, 11, 16, 24, 32]
    rows = []
    total_vertices = 0
    for m in clocks:
        word = cycle_word(m)
        root = predicted_root(m)
        determinant = (1 << len(word)) - 3 ** word.count("1")
        require(Fraction(carry(word), determinant) == root, "impulse superposition")
        require(((A**m - N**m) * (A ** (m + 1) - N ** (m + 1)))
                % root.denominator == 0, "full denominator divisibility")
        require(least_period(word) == 7 * m * (m + 1), "native period")
        require("000" not in word + word[:2], "zero runs")
        x = root
        for bit in word:
            require(x.denominator == root.denominator and -60 < x < 0, "signed orbit bound")
            require(x.numerator % 2 == int(bit), "physical parity")
            x = (3 * x + 1) / 2 if bit == "1" else x / 2
            total_vertices += 1
        require(x == root, "native closure")
        rows.append((m, len(word), root.denominator.bit_length(),
                     shortest_periodic_partition(word, 7)))

    for length in range(1, 9):
        for digits in product("01", repeat=length):
            word = "".join(digits)
            for bound in (1, 2, 3):
                require(shortest_periodic_partition(word, bound) == brute_partition(word, bound),
                        "periodic-factor partition")

    stages = 0
    combined = ""
    for t in range(1, 7):
        base = cycle_word(2**t)
        for _ in range(copies(t)):
            stages += 1
            combined += base + "1" + lex_word(stages)
    require(all(lex_word(i) in combined for i in range(1, stages + 1)), "literal connectors")
    require(len({lex_word(i) for i in range(1, 128)}) == 127, "length-lex enumeration")
    print("m, period, reduced denominator bit length, minimum period-at-most-7 pieces")
    for row in rows:
        print(*row)
    print("native negative rational vertices", total_vertices)
    print("six finite groups", stages, "stages,", len(combined), "letters")


if __name__ == "__main__":
    main()
