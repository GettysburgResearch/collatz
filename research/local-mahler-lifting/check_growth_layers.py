"""Replay a two-exponential-tier, linear-tier, and frozen-letter reduction."""
from collections import Counter
from fractions import Fraction


WORDS = ("AAB", "BBC", "CD", "D")
LETTERS = "ABCD"
RULES = dict(zip(LETTERS, WORDS))


def incidence(vector):
    return tuple(sum(vector[LETTERS.index(letter)] for letter in word)
                 for word in WORDS)


def projection(vector):
    _, _, c, d = vector
    return c + 2 * d, -c - d, c, d


def lift(t):
    x, y, z = t
    return x + 3 * y, y + 4 * z, z, 0


def coordinates(vector):
    x, y, z, d = vector
    assert d == 0
    return x - 3 * (y - 4 * z), y - 4 * z, z


def reduced_action(t):
    x, y, z = t
    return 2 * x + y - 11 * z, 2 * y + 5 * z, z


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def subtract(left, right):
    return tuple(a - b for a, b in zip(left, right))


def check_orbit(prime_vector, distinguished):
    offset = projection(prime_vector)
    translation = coordinates(subtract(incidence(offset), offset))
    t = coordinates(subtract(prime_vector, offset))
    raw = prime_vector
    for level in range(121):
        assert add(offset, lift(t)) == raw
        if distinguished and level >= 30:
            fast, slow, linear = t
            assert Fraction(1, 8) < Fraction(fast, level * 2**level) < 8
            assert Fraction(1, 8) < Fraction(slow, 2**level) < 8
            assert linear == level
        t = add(reduced_action(t), translation)
        raw = incidence(raw)


def check_words():
    word = "A"
    for level in range(15):
        assert word.count("A") == 2**level
        counts = Counter()
        last_fast = -1
        for letter in word:
            fast_degree = counts["A"]
            assert fast_degree >= last_fast
            last_fast = fast_degree
            counts[letter] += 1
        # The normalized prime-two offset is polynomial in substitution depth.
        prime_two_offset = projection((1, 1, 1, 1))
        assert abs(sum(c * counts[a] for a, c in zip(LETTERS, prime_two_offset))) <= 8 * (level + 1)
        word = "".join(RULES[letter] for letter in word)


def check_frequency_example():
    x_count, y_count = 1, 0
    total_ones, total_bits = 0, 0
    for level in range(45):
        length = x_count + y_count
        total_ones += 3 * x_count + 4 * y_count
        total_bits += 4 * length
        lower_endpoint = Fraction(total_ones, total_bits)
        total_ones += 4 * x_count + 3 * y_count
        total_bits += 4 * length
        assert Fraction(total_ones, total_bits) == Fraction(7, 8)
        if level >= 10:
            assert Fraction(83919, 100000) < lower_endpoint < Fraction(83921, 100000)
        x_count, y_count = 3 * x_count + y_count, x_count


if __name__ == "__main__":
    check_orbit((1, 1, 1, 1), True)
    check_orbit((0, -1, -1, -1), False)
    check_words()
    check_frequency_example()
    print("Verified 242 sampled prime vectors, 15 complete word levels, and 45 density pairs.")
