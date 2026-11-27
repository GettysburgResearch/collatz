"""Exact finite checks for the claims in CYCLE_INDEX.md, using the standard library."""

from fractions import Fraction
from math import comb, gcd
from random import Random
import json


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def cycle_numerator(word):
    value = 0
    for step, odd in enumerate(word):
        if odd:
            value = 3 * value + (1 << step)
    return value


def replay(word):
    clock = len(word)
    grade = sum(word)
    denominator = (1 << clock) - 3**grade
    start = cycle_numerator(word)
    current = start
    phases = []
    for bit in word:
        phases.append(current)
        check(current % 2 == bit, "native parity mismatch")
        current = (3 * current + denominator) // 2 if bit else current // 2
    check(current == start, "cycle did not close")
    return phases, denominator


def actual_step(value):
    return (3 * value + 1) // 2 if value % 2 else value // 2


def exhaustive():
    marked_total = 0
    positive_total = 0
    anchor_windows = 0
    for clock in range(1, 15):
        positive = set()
        minima = set()
        ordinary = set()
        for code in range(1 << clock):
            word = tuple((code >> j) & 1 for j in range(clock))
            phases, denominator = replay(word)
            marked_total += 1
            if denominator < 0 or not phases[0]:
                continue
            point = Fraction(phases[0], denominator)
            check(point not in positive, "one phase was assigned two distinct native words")
            positive.add(point)
            positive_total += 1
            if point.denominator == 1:
                ordinary.add(point.numerator)
                value = point.numerator
                for bit in word:
                    check(value % 2 == bit, "ordinary replay disagrees with rational replay")
                    value = actual_step(value)
                check(value == point, "ordinary row fails to return")
            minimum_index = phases.index(min(phases))
            minimum = Fraction(phases[minimum_index], denominator)
            if minimum in minima:
                continue
            minima.add(minimum)
            for length in (clock // 2 + 1, clock, 2 * clock + 1):
                grade = sum(word[(minimum_index + j) % clock] for j in range(length))
                a, d = minimum.as_integer_ratio()
                check((3 * a + d)**grade >= (1 << length) * a**grade,
                      "minimum-anchored grade failed")
                anchor_windows += 1
        theory = sum(comb(clock, p) for p in range(1, clock + 1)
                     if 3**p < (1 << clock))
        check(len(positive) == theory, "positive rational count")
        check(ordinary == ({1, 2} if clock % 2 == 0 else set()), "extra bounded-clock root")
    return dict(all_words=marked_total, positive_roots=positive_total,
                exact_anchor_windows=anchor_windows)


def construct(clock, grade, width, primes, seed):
    rng = Random(seed)
    determinant = (1 << clock) - 3**grade
    modulus = 1
    for prime in primes:
        remaining = determinant
        while remaining % prime == 0:
            modulus *= prime
            remaining //= prime
    check(modulus > 1, "finite fixture should test an actual prime factor")
    groups = []
    for start in range(0, clock, width):
        end = min(clock, start + width)
        weight = end * grade // clock - start * grade // clock
        groups.append((end - start, weight))
    # Retain one predecessor for each newly reached residue.  We can stop the
    # patch as soon as all targets are represented, before sampling the outside.
    parents = {0: None}
    switches = []
    before = 0
    for j, (size, weight) in enumerate(groups):
        check(size == width and 1 <= weight < width, "unsuitable patch block")
        delta = pow(2, j * width, modulus) * pow(3, grade - before - 1, modulus) % modulus
        switches.append(delta)
        for old in tuple(parents):
            new = (old + delta) % modulus
            if new not in parents:
                parents[new] = (old, j)
        before += weight
        if len(parents) == modulus:
            break
    check(len(parents) == modulus, "finite patch did not cover every residue")
    word = []
    for j, (size, weight) in enumerate(groups):
        if j < len(switches):
            # Relative to 10, using 01 adds one unit in that pair's affine carry.
            suffix = [1] * (weight - 1) + [0] * (size - weight - 1)
            rng.shuffle(suffix)
            word.extend([1, 0] + suffix)
        else:
            block = [1] * weight + [0] * (size - weight)
            rng.shuffle(block)
            word.extend(block)
    target = -cycle_numerator(word) % modulus
    while target:
        previous, j = parents[target]
        word[j * width:j * width + 2] = [0, 1]
        target = previous
    phases, denominator = replay(word)
    check(denominator == determinant, "full determinant changed")
    common = gcd(phases[0], denominator)
    reduced = denominator // common
    check(common % modulus == 0 and gcd(reduced, modulus) == 1, "full local factor")
    check(gcd(clock, grade) == 1 and len(set(phases)) == clock, "least period")
    sorted_phases = sorted(phases)
    gap = min(b - a for a, b in zip(sorted_phases, sorted_phases[1:]))
    check(gap >= denominator, "fixture phases are closer than ordinary integers")
    check(reduced > 1, "fixture unexpectedly integral")
    return dict(clock=clock, grade=grade, full_denominator_bits=denominator.bit_length(),
                reduced_denominator_bits=reduced.bit_length(), local_factor=modulus,
                tested_primes=primes, patch_blocks=len(switches),
                phase_minimum_floor=min(phases) // denominator,
                minimum_real_spacing_floor=gap // denominator)


if __name__ == '__main__':
    fixtures = [(65, 41, 4, [19, 29]), (485, 306, 6, [929]),
                (24727, 15601, 9, [5])]
    result = dict(exhaustive=exhaustive(),
                  patches=[construct(n, p, width, primes, 826 + n)
                           for n, p, width, primes in fixtures])
    print(json.dumps(result, indent=2, sort_keys=True))
