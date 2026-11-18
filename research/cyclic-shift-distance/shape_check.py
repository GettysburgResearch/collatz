"""Finite controls for circular heights and edited mechanical factors."""

from collections import deque
from fractions import Fraction
from itertools import product
from math import gcd


def heights(word):
    length = len(word)
    weight = sum(word)
    result = [0]
    for bit in word:
        result.append(result[-1] + length * bit - weight)
    assert result[-1] == 0
    return result[:-1]  # All heights are scaled by the common factor length.


def shift_distances(word):
    length = len(word)
    return [sum(bit != word[(i + r) % length] for i, bit in enumerate(word)) for r in range(length)]


def diameter_of_generated_group(length, shifts):
    queue = deque([0])
    distances = {0: 0}
    while queue:
        position = queue.popleft()
        for r in shifts:
            neighbor = (position + r) % length
            if neighbor not in distances:
                distances[neighbor] = distances[position] + 1
                queue.append(neighbor)
    return len(distances), max(distances.values())


def check_geometry():
    count = 0
    for length in range(2, 11):
        for word in product((0, 1), repeat=length):
            height = heights(word)
            bank = max(height) - min(height)
            distances = shift_distances(word)
            for r, d in enumerate(distances):
                assert all(2 * abs(height[(i + r) % length] - h) <= length * d
                           for i, h in enumerate(height))
                # Test the lattice-covering estimate for every relevant reduced slope.
                for k in range(1, length + 1):
                    a = (2 * k * r + length) // (2 * length)
                    if gcd(a, k) != 1 or abs(r * k - a * length) * k > length:
                        continue
                    assert 4 * k * bank <= length * k * k * d + 4 * length * length
            for threshold in set(distances):
                shifts = [r for r, d in enumerate(distances) if d <= threshold]
                n, diameter = diameter_of_generated_group(length, shifts)
                assert diameter * len(shifts) < 3 * n
                assert 2 * len(shifts) * bank <= length * length * (1 + 3 * threshold)
            count += 1
    return count


def edit_distance(source, target):
    previous = list(range(len(target) + 1))
    for i, bit in enumerate(source, start=1):
        current = [i]
        for j, other in enumerate(target, start=1):
            current.append(min(current[-1] + 1, previous[j] + 1, previous[j - 1] + (bit != other)))
        previous = current
    return previous[-1]


def mechanical_words(alpha, length):
    thresholds = {Fraction(0)}
    thresholds.update((-i * alpha) % 1 for i in range(1, length + 1))
    output = set()
    for phase in thresholds:
        partial = [(i * alpha + phase).__floor__() for i in range(length + 1)]
        output.add(tuple(b - a for a, b in zip(partial, partial[1:])))
    assert len(output) <= length + 1
    return output


def check_edits():
    pairs = 0
    slopes = {Fraction(a, b) for b in range(1, 7) for a in range(b + 1)}
    for source_length in range(2, 7):
        for word in product((0, 1), repeat=source_length):
            height = heights(word)
            bank = max(height) - min(height)
            unique_lengths = [
                h for h in range(1, source_length + 1)
                if len({word[i:i + h] for i in range(source_length - h + 1)}) == source_length - h + 1
            ]
            for target_length in (source_length - 1, source_length, source_length + 1):
                targets = set().union(*(mechanical_words(alpha, target_length) for alpha in slopes))
                for target in targets:
                    e = edit_distance(word, target)
                    assert bank <= source_length * (e + 2)
                    assert all(source_length <= (e + 2) * h for h in unique_lengths)
                    pairs += 1
    return pairs


if __name__ == "__main__":
    print(f"Checked height and shift bounds on {check_geometry()} binary circles.")
    print(f"Checked {check_edits()} source/target edit-distance pairs.")
