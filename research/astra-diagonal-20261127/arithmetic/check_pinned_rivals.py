"""Replay the native and rival odd words and the denominator-five all-depth floor."""

from fractions import Fraction
import json


def odd_step(n, correction=1):
    value = 3 * n + correction
    power = (value & -value).bit_length() - 1
    return value >> power, power


def trajectory(start, length):
    value = start
    letters = []
    for _ in range(length):
        value, letter = odd_step(value)
        letters.append(letter)
    return value, letters


def native_class(word):
    residue, modulus = 1, 2
    for letter in reversed(word):
        modulus <<= letter
        residue = ((2**letter * residue - 1) * pow(3, -1, modulus)) % modulus
    return residue, modulus


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def shortcut_word(start, steps):
    n = start
    parity = []
    for _ in range(steps):
        parity.append(n % 2)
        n = shortcut(n)
    return n, parity


def state_cycle(start, correction):
    orbit = []
    state = start
    while state not in orbit:
        orbit.append(state)
        state = odd_step(state, correction)[0]
    return tuple(sorted(orbit[orbit.index(state):]))


def main():
    specs = (
        ("121212121222212122", 1, 1, 30, 30, 663632570),
        ("12211212222121221", 4, 1, 27, 27, 250702913),
        ("21212121212222121221", -1, 8, 32, 29, 6474939905),
    )
    verified = []
    for digits, shift, divisor, native_clock, rival_clock, end in specs:
        word = list(map(int, digits))
        r, m = native_class(word)
        multipliers = [Fraction(1)]
        for e in word:
            multipliers.append(multipliers[-1] * 3 / (2**e))
        spread = max(multipliers) / min(multipliers)
        assert spread == Fraction(65536, 19683)
        old_words = None
        for t in range(2):
            source = r + m * t
            assert (source + shift) % divisor == 0
            other = (source + shift) // divisor
            assert trajectory(source, len(word))[1] == word
            out, p = shortcut_word(source, native_clock)
            out2, p2 = shortcut_word(other, rival_clock)
            assert out == out2
            if t == 0:
                assert out == end
                old_words = p, p2
            else:
                assert old_words == (p, p2)
        verified.append(dict(word=digits, residue=r, modulus=m, terminal_at_base=end,
                             clock=[native_clock, rival_clock], shift=shift, divisor=divisor,
                             spread=str(spread)))
    bad = (23, 29, 37)
    other = {(1,), (5,), (19, 31, 49)}
    below = {n: state_cycle(n, 5) for n in range(1, 23, 2)}
    triples = {n: state_cycle(n, 5) for n in range(3, 51, 6)}
    assert set(below.values()) <= other and set(triples.values()) <= other
    assert state_cycle(23, 5) == state_cycle(51, 5) == bad
    print(json.dumps(dict(cylinders=verified, denominator_five=dict(
        target=bad, small_sources=below, smaller_odd_triples=triples,
        least_bad_source=23, least_bad_triple=51)), indent=2))


if __name__ == "__main__":
    main()
