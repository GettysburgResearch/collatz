"""Exact deterministic controls for the native and octave order theorems."""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import gcd


def require(condition):
    if not condition:
        raise ArithmeticError('an exact order control failed')


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def orbit(x, clock):
    states = [x]
    for _ in range(clock):
        states.append(step(states[-1]))
    return states


def grade(path):
    return sum(x % 2 for x in path[:-1])


def grade_census(max_clock):
    checked = 0
    reversing = 0
    for h in range(1, max_clock + 1):
        rows = [[] for _ in range(h + 1)]
        for a in range(2**h):
            path = orbit(a, h)
            rows[grade(path)].append(path[-1])
        for p, row in enumerate(rows):
            r = h - p
            wraps = row[1:] + [row[0] + 3**p]
            reversal = any(v > w for v, w in zip(row, wraps))
            require(reversal == ((p >= 2 and r >= 4) or (p >= 5 and r >= 3)))
            checked += 1
            reversing += reversal
    return {'max_clock': max_clock, 'grade_classes': checked, 'reversing_classes': reversing}


def reversing_gadget(p):
    k = p - 2
    h = p + 4
    u = (25 * pow(3, -k, 32)) % 32
    a = (2 ** (k + 1) * u - 2) % 2**h
    left, right = orbit(a, h), orbit(a + 1, h)
    require(grade(left) == grade(right) == p and left[-1] == right[-1] + 1)
    return a, h


def program(grades):
    start = z = H = P = 0
    for p in grades:
        residue, h = reversing_gadget(p)
        lift = (residue - z) * pow(3**P, -1, 2**h) % 2**h
        start += 2**H * lift
        z += 3**P * lift
        paths = (orbit(z, h), orbit(z + 1, h))
        require(paths[0][-1] == paths[1][-1] + 1)
        z = paths[1][-1]
        H += h
        P += p
    check = (orbit(start, H), orbit(start + 1, H))
    elapsed = 0
    for i, p in enumerate(grades):
        elapsed += p + 4
        require(check[1][elapsed] - check[0][elapsed] == (-1) ** (i + 1))
    require(sorted(path[-1] for path in check) == [z, z + 1])
    return start, z, H, P


def close_to_one(grades):
    a, z, H, P = program(grades)
    lift = (12 - z) * pow(3**P, -1, 8) % 8
    a += 2**H * lift
    z += 3**P * lift
    c = 5 + 3 * ((z - 12) // 8)
    modulus = 3 ** (P + 1)
    period = 2 * 3**P
    m = next(i for i in range(period) if pow(2, i, modulus) == c % modulus)
    m += period
    a += 8 * 2**H * ((2**m - c) // modulus)
    paths = [orbit(a + j, H + 3) for j in range(2)]
    require(paths[0][-1] == paths[1][-1] == 2**m)
    require(all(grade(path) == P + 1 for path in paths))
    require(len({v for path in paths for v in path[: H + 1]}) == 2 * (H + 1))
    return {'gadgets': grades, 'clock_before_fusion': H, 'common_power_exponent': m,
            'least_prefix_height_bits': min(v.bit_length() for path in paths for v in path[: H + 1])}


def primitive_words(n):
    for bits in product((0, 1), repeat=n):
        if all(bits < bits[j:] + bits[:j] for j in range(1, n)):
            yield bits


def phases(bits):
    p = sum(bits)
    D = 2 ** len(bits) - 3**p
    if p == 0 or D <= 0:
        return None
    C = 0
    for i, digit in enumerate(bits):
        C = 3 * C + 2**i if digit else C
    x = Fraction(C, D)
    d, z = x.denominator, x.numerator
    odd = []
    for digit in bits:
        require(z % 2 == digit)
        if digit:
            odd.append(z)
        z = (3 * z + d) // 2 if digit else z // 2
    require(z == x.numerator and len(set(odd)) == p)
    return d, odd


def inversions(odd, d):
    triples = []
    for x in odd:
        for y in odd:
            for k in range(1, y.bit_length()):
                if 0 < 3 * (y - 2**k * x) < d * (2**k - 1):
                    triples.append((x, y, k))
    return triples


def cycle_census(max_clock):
    counts = Counter()
    sample = {}
    for n in range(1, max_clock + 1):
        for bits in primitive_words(n):
            cycle = phases(bits)
            if cycle is None:
                continue
            d, odd = cycle
            g = gcd(n, len(odd))
            count = len(inversions(odd, d))
            require(count >= g - 1 and (count - g + 1) % 2 == 0)
            counts[g] += 1
            if g not in sample and count == g - 1:
                sample[g] = {'word': ''.join(map(str, bits)), 'denominator': d, 'inversions': count}
    return {'max_clock': max_clock, 'counts_by_gcd': dict(counts), 'sharp_examples': sample}


def odd_step(x):
    y = 3 * x + 1
    return y // (y & -y)


def main():
    long_grades = [(j + 1) * 41 // 6 - j * 41 // 6 for j in range(40)]
    a, z, H, P = program(long_grades)
    contraction = [orbit(859 + j, 46) for j in range(2)]
    require([path[-1] for path in contraction] == [890, 866])
    require([grade(path) for path in contraction] == [29, 29] and 3**29 < 2**46)
    require([min(path) for path in contraction] == [47, 91])
    v = 41
    for _ in range(39):
        v = odd_step(v)
    require(v == 5 and odd_step(v) == 1 and inversions([5, 41], 1) == [(5, 41, 3)])
    require(phases((0, 0, 1, 1, 1)) is not None and not inversions([19, 31, 49], 5))
    result = {'grade_census': grade_census(14), 'cycle_census': cycle_census(14),
              'known_basin': close_to_one([2, 2, 2]),
              'forty_adjacent_reversals': {'total_clock': H, 'total_grade': P,
                  'start_sha256': sha256(str(a).encode()).hexdigest(),
                  'smaller_terminal_sha256': sha256(str(z).encode()).hexdigest()},
              'ordinary_nesting': {'first': 41, 'odd_steps': 39, 'second': v},
              'contracting_reversal': {'sources': [859, 860], 'images': [890, 866], 'clock': 46, 'grade': 29}}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
