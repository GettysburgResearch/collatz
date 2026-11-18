"""Complete bounded replay and finite arithmetic controls for rotation distance."""

from collections import Counter
from fractions import Fraction
from itertools import product


def next_value(x):
    return (3 * x + 1 if x % 2 else x) // 2


def itinerary(x, length):
    bits = []
    for _ in range(length):
        bits.append(x % 2)
        x = next_value(x)
    return tuple(bits), x


def numerator(word):
    constant = 0
    for j, bit in enumerate(word):
        if bit:
            constant = 3 * constant + (1 << j)
    return constant


def verify_cutoff():
    assert 4**1024 > 36 * 3**1024 * 1024**28
    assert 3 * 1025**28 < 4 * 1024**28


def bounded_replay():
    remaining = {}
    for length in range(2, 1024):
        scale = 2**length
        width = 3 ** (length // 2 + 1)
        weights = set()
        power = 1
        for weight in range(1, length):
            power *= 3
            full = scale - power
            if full <= 0:
                break
            if full < width:
                weights.add(weight)
        if weights:
            remaining[length] = weights
    assert set(remaining) == {2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 16}
    tested = 0
    hits = Counter()
    for length, weights in remaining.items():
        scale = 2**length
        observed = set()
        for residue in range(scale):
            word, endpoint = itinerary(residue, length)
            assert word not in observed
            observed.add(word)
            weight = sum(word)
            if weight not in weights:
                continue
            tested += 1
            multiplier = 3**weight
            full = scale - multiplier
            constant = scale * endpoint - multiplier * residue
            assert constant == numerator(word)
            source, remainder = divmod(constant, full)
            if remainder or source <= 0:
                continue
            replay, final = itinerary(source, length)
            assert replay == word and final == source
            assert source in (1, 2)
            hits[length] += 1
        assert len(observed) == scale
    assert hits[2] == 2
    return tested, dict(hits)


def rational_controls():
    checked = 0
    for length in range(2, 9):
        scale = 2**length
        for word in product((0, 1), repeat=length):
            weight = sum(word)
            multiplier = 3**weight
            full = scale - multiplier
            if not weight or full <= 0:
                continue
            words = [word[i:] + word[:i] for i in range(length)]
            if len(set(words)) != length:
                continue
            phases = [Fraction(numerator(w), full) for w in words]
            for shift in range(1, length):
                distance = sum(a != b for a, b in zip(word, words[shift]))
                assert distance >= 2 and distance % 2 == 0
                counts = [sum(w[:shift]) for w in words]
                assert max(counts) - min(counts) <= distance // 2
                for i, start in enumerate(phases):
                    j = (i + shift) % length
                    assert phases[j] / start <= Fraction(3 ** (distance // 2) * scale, multiplier)
                    match = 0
                    while words[i][match] == words[j][match]:
                        match += 1
                    delta = numerator(words[i][match:]) - numerator(words[j][match:])
                    assert full * (start - phases[j]) == 2**match * delta
                    assert 0 < abs(delta) < 3 ** (length - match)
                checked += 1
    return checked


if __name__ == "__main__":
    verify_cutoff()
    tested, hits = bounded_replay()
    print(f"Tested {tested} residual words. Trivial-cycle hits by length: {hits}.")
    print(f"Checked {rational_controls()} primitive rational word-shift controls.")
