"""Check universal merger words and literal dyadic transport arithmetic."""

from fractions import Fraction


def shortcut_clock(start, depth):
    state = start
    odds = 0
    for _ in range(depth):
        if state % 2:
            odds += 1
            state = (3 * state + 1) // 2
        else:
            state //= 2
    return state, odds


def counted_merge(start, depth):
    return shortcut_clock(start, depth) == shortcut_clock(start + 1, depth)


def phi(value):
    integer = value.numerator
    low_bit = integer & -integer
    return 3 * value + Fraction(low_bit, value.denominator)


def legal_factor_counts(depth):
    """The k-bit survivors avoid every subsuffix merging by its own length."""
    previous = {0}
    counts = []
    for length in range(1, depth + 1):
        mask = (1 << (length - 1)) - 1
        current = set()
        for prefix in previous:
            for digit in (0, 1):
                word = 2 * prefix + digit
                if word & mask in previous and not counted_merge(word, length):
                    current.add(word)
        counts.append(len(current))
        previous = current
    return counts


def main():
    family_cases = 0
    for length in range(1, 66):
        odd_residue = 3 if length % 2 else 1
        for lift in range(12):
            odd_part = 4 * lift + odd_residue
            start = (1 << length) * odd_part - 2
            assert counted_merge(start, length + 2)
            family_cases += 1
    extra_word = int("101110101110", 2)
    assert shortcut_clock(extra_word, 12) == (533, 6)
    assert shortcut_clock(extra_word + 1, 12) == (533, 6)
    expected = [2, 4, 7, 11, 17, 25, 37, 53, 77, 109, 157, 220,
                313, 435, 615, 850, 1193, 1640, 2294, 3136, 4352,
                5910, 8155, 11012, 15105]
    assert legal_factor_counts(25) == expected
    transport_cases = 0
    for lower in range(1, 80, 2):
        for ones in range(1, 22, 2):
            image_parent = 3 * lower + 1
            mesh = Fraction(1, 2 ** (ones + 1))
            before_zero = lower + Fraction(1, 2) - mesh
            after_zero = before_zero + mesh / 2
            image_left = phi(before_zero)
            image_right = phi(after_zero)
            expected_index = 2 ** (ones + 1) * image_parent + 2**ones - 2
            assert image_left == expected_index * mesh
            assert image_right == (expected_index + 1) * mesh
            transport_cases += 1
    print(f"{family_cases} merger-family cases and {transport_cases} transported "
          "returns passed; full factor language through 25 bits checked")


if __name__ == "__main__":
    main()
