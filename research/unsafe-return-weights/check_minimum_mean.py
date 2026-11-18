"""Replay the homogeneous minimum comparison across whole dyadic shells."""

from fractions import Fraction


def orbit_data(source, length):
    state = source
    odd_count = 0
    word = 0
    minimum = source
    homogeneous = Fraction(1)
    for time in range(1, length + 1):
        odd = state % 2
        word = 2 * word + odd
        odd_count += odd
        state = (3 * state + 1) // 2 if odd else state // 2
        scale = Fraction(3**odd_count, 2**time)
        if not source * scale <= state <= 2 * source * scale:
            raise AssertionError((source, time, state, scale))
        homogeneous = min(homogeneous, scale)
        minimum = min(minimum, state)
    return word, minimum, homogeneous


def main():
    for length in range(1, 13):
        lower = 2**length
        words = set()
        observed = 0
        homogeneous = Fraction(0)
        for source in range(lower, 2 * lower):
            word, minimum, scale = orbit_data(source, length)
            words.add(word)
            observed += minimum
            homogeneous += source * scale
        if len(words) != lower or not homogeneous <= observed <= 2 * homogeneous:
            raise AssertionError(length)
        print(f"k={length}, sources={lower}, sum of physical prefix minima={observed}")


if __name__ == "__main__":
    main()
