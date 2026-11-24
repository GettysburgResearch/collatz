"""Exact finite controls for the telescoping identity and the marked cylinder."""

from fractions import Fraction
from itertools import product


def require(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut(value):
    return (3 * value + 1) // 2 if value % 2 else value // 2


def check_telescopes():
    cases = 0
    for length in range(10):
        for bits in product((0, 1), repeat=length):
            for seed in (Fraction(0), Fraction(2, 7), Fraction(11)):
                tail = seed
                correction = Fraction(1)
                for bit in reversed(bits):
                    if bit == 0:
                        correction *= 1 + 1 / (1 + tail)
                    tail = (3**bit * tail + bit) / 2
                slope = Fraction(3 ** sum(bits), 2**length)
                require((1 + tail) / (1 + seed) == slope * correction,
                        "rational telescoping identity failed")
                cases += 1
    return cases


def check_cylinder(lifts):
    for lift in range(lifts):
        source = 49 + 64 * lift
        companion = 5 * source
        source_count = companion_count = 0
        bits = []
        for clock in range(1, 7):
            bits.append(source % 2)
            source_count += source % 2
            companion_count += companion % 2
            source, companion = shortcut(source), shortcut(companion)
            root = source_count == companion_count and companion == 5 * source
            require(root == (clock == 6), "incorrect first return clock")
        require(bits == [1, 0, 1, 0, 0, 0], "incorrect source parity word")


if __name__ == "__main__":
    cases = check_telescopes()
    check_cylinder(1024)
    print(f"Verified {cases} rational telescopes and 1024 marked-cylinder lifts.")
