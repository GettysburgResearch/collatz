"""Exact finite controls for width-language counting and rational realization."""
from fractions import Fraction as Q
from itertools import product
from math import gcd
import json


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def octave(z):
    while z >= 2:
        z /= 2
    while z < 1:
        z *= 2
    return z


def direct_words(m, width):
    result = set()
    for word in product((1, 2, 3), repeat=m):
        y = lo = hi = Q(1)
        for e in word:
            y = 3 * y / (1 << e)
            lo = min(lo, y)
            hi = max(hi, y)
            if hi >= width * lo:
                break
        else:
            result.add(word)
    return result


def matching(available, winding, circular):
    n = len(available)
    forbidden = [(j, (j + 1) % n) for j, b in enumerate(winding)
                 if b == 1 and available[(j + 1) % n]]
    require(all(available[i] and available[j] for i, j in forbidden), "both sites available")
    require(len(set(sum(([i, j] for i, j in forbidden), []))) == 2 * len(forbidden),
            "disjoint constrained edges")
    free = [i for i in range(n) if available[i]]
    expected = 2 ** (len(free) - 2 * len(forbidden)) * 3 ** len(forbidden)
    words, arrays = set(), 0
    for assignment in product((0, 1), repeat=len(free)):
        grades = [0] * n
        for i, bit in zip(free, assignment):
            grades[i] = bit
        if any(grades[i] == 0 and grades[j] == 1 for i, j in forbidden):
            continue
        word = tuple(b + grades[j] - grades[(j + 1) % n] for j, b in enumerate(winding))
        require(min(word) >= 1, "native positive exponent")
        arrays += 1
        words.add(word)
    require(arrays == expected and len(words) <= expected <= 2 * len(words), "matching count")
    require(len(winding) == n - (not circular), "edge count")
    return words, arrays


def finite_band(m, width):
    boundaries = {Q(1), Q(2)}
    for j in range(m + 1):
        for target in (Q(1), width / 2, Q(4, 3)):
            boundaries.add(octave(target * Q(2, 3) ** j))
    endpoints = sorted(boundaries)
    probes = {x for x in endpoints if x < 2}
    probes.update((a + b) / 2 for a, b in zip(endpoints, endpoints[1:]))
    words = set()
    for z0 in probes:
        phases = [octave(z0 * Q(3, 2) ** j) for j in range(m + 1)]
        available = [z < width / 2 for z in phases]
        winding = [1 + (3 * z >= 4) for z in phases[:-1]]
        found, _ = matching(available, winding, False)
        words.update(found)
    require(words == direct_words(m, width), "full finite physical discrepancy language")
    return len(probes), len(words)


def realize(word, width):
    p, h = len(word), sum(word)
    determinant, carry, elapsed = (1 << h) - 3 ** p, 0, 0
    for j, e in enumerate(word):
        carry += (1 << elapsed) * 3 ** (p - 1 - j)
        elapsed += e
    x = initial = Q(carry, determinant)
    odd = []
    for e in word:
        require(x.numerator % 2 == 1 and x.denominator == initial.denominator,
                "exact native odd state and common denominator")
        odd.append(x)
        x = (3 * x + 1) / (1 << e)
    require(x == initial and len(set(odd)) == p, "primitive ordinary rational orbit")
    require(max(odd) * 3 ** p <= width * min(odd) * (1 << h), "actual odd width")
    require(determinant % x.denominator == 0 and gcd(x.denominator, 6) == 1, "whole determinant")
    return initial


def cyclic_band(p, h, marks):
    residues = [(j * h) % p for j in range(p)]
    available = [r < marks for r in residues]
    winding = [(r + h) // p for r in residues]
    words, arrays = matching(available, winding, True)
    # eta=marks/p means R=2^(1+marks/p); raise both sides to p to stay integral.
    roots = set()
    for word in words:
        require(sum(word) == h, "clock preservation")
        initial = realize(word, Q(4))
        x = initial
        phases = []
        for e in word:
            phases.append(x)
            x = (3 * x + 1) / (1 << e)
        require((max(phases) * 3**p)**p <=
                (min(phases) * (1 << h))**p * (1 << (p + marks)),
                "sharp actual width with moving clock")
        roots.add(initial)
    require(len(roots) == len(words), "distinct roots")
    return arrays, len(roots)


def main():
    cells = finite_words = models = arrays = roots = 0
    for m in range(1, 8):
        for width in map(Q, (2, '9/4', '12/5', '8/3', 3, '7/2', 4)):
            ncell, nword = finite_band(m, width)
            cells += ncell
            finite_words += nword
    for p, h in [(5, 8), (7, 12), (8, 13), (11, 18), (13, 21)]:
        for marks in sorted({0, 1, p // 3, h - p, h - p + 1, p}):
            narray, nroot = cyclic_band(p, h, marks)
            models += 1
            arrays += narray
            roots += nroot
    require(2 ** 5 * 3 < Q(5, 2) ** 5, "width 2*3^(1/5) < 5/2")
    print(json.dumps({"exact_phase_cells_and_endpoints": cells,
                      "finite_words_summed_over_bands_and_lengths": finite_words,
                      "circular_models": models, "circular_grade_arrays": arrays,
                      "distinct_rational_roots_summed_over_models": roots}, sort_keys=True))


if __name__ == "__main__":
    main()
