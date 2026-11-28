"""Exact strict ballot counts at odd-map endpoints, including the next odd bit."""

from collections import Counter
from itertools import combinations
from math import comb


def verify(condition, description):
    if not condition:
        raise ValueError(description)


def check_length(length):
    counts = Counter()
    for odds in range(1, length + 1):
        for starts in combinations(range(1, length), odds - 1):
            positions = (0,) + starts
            boundaries = positions[1:] + (length,)
            gap_survives = all(2 * i > t for i, t in enumerate(boundaries, 1))
            odd_set = set(positions)
            surplus = 0
            native_survives = True
            for time in range(length):
                surplus += 1 if time in odd_set else -1
                native_survives &= surplus > 0
            verify(gap_survives == native_survives, "native intermediate minimum")
            counts[odds] += int(native_survives)
        formula_numerator = max(2 * odds - length, 0) * comb(length, odds)
        verify(length * counts[odds] == formula_numerator, "strict ballot count")

    # Independently recover every such word as a true shortcut orbit modulo
    # 2^(length+1), conditioning on an odd initial AND final value.
    realized = Counter()
    for start in range(1, 2 ** (length + 1), 2):
        state = start
        surplus = 0
        odds = 0
        positive = True
        for time in range(length):
            if state % 2:
                odds += 1
                surplus += 1
                state = (3 * state + 1) // 2
            else:
                surplus -= 1
                state //= 2
            positive &= surplus > 0
        if state % 2 and positive:
            realized[odds] += 1
    verify(counts == realized, "one actual odd representative per positive word")


if __name__ == "__main__":
    for length in range(1, 16):
        check_length(length)
    print("15 exact clock lengths passed both ballot and physical endpoint checks")
