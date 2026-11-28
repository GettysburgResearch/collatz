"""Exact finite checks for physical references and pre-crossing ordinary words."""
from fractions import Fraction
from itertools import product
from math import gcd
from random import Random
import json


def check(condition, label):
    if not condition:
        raise ValueError(label)


def height(x):
    return max(abs(x.numerator), x.denominator)


def rationals(limit):
    return sorted({Fraction(a, b) for b in range(1, limit + 1)
                   for a in range(-limit, limit + 1)})


def two_exponent(n):
    return (n & -n).bit_length() - 1


def step(x, bit):
    return ((3 * x + 1) if bit else x) / 2


def affine(word):
    grade = carry = 0
    for j, bit in enumerate(word):
        if bit:
            carry = 3 * carry + 2**j
            grade += 1
    return 2**len(word), 3**grade, carry


def source_residue(word):
    M, N, C = affine(word)
    return -C * pow(N, -1, M) % M


def convergents(a, b):
    p0, p1, q0, q1 = 0, 1, 1, 0
    while b:
        quotient, rest = divmod(a, b)
        p0, p1 = p1, quotient * p1 + p0
        q0, q1 = q1, quotient * q1 + q0
        yield p1, q1
        a, b = b, rest


def long_reference(word, H):
    b = H.bit_length() - 1
    precision = len(word) - b
    M = 2**precision
    check(M > 2 * H**2, "reconstruction requested on a short word")
    R = source_residue(word[:precision])
    scale, multiplier, carry = affine(word)
    hits = []
    for k, q in convergents(R, M):
        a = q * R - k * M
        if abs(a) <= H and q <= H and q % 2 and gcd(a, q) == 1:
            start = Fraction(a, q)
            if height((multiplier * start + carry) / scale) <= H:
                hits.append(start)
    check(len(hits) <= 1, "uniqueness")
    return hits


def valuations_and_reconstruction():
    valuations = reconstructed = retained = escaped = 0
    for n in range(1, 8):
        for word in product((0, 1), repeat=n):
            for x in rationals(5):
                bad_at = None
                initial_power = two_exponent(x.denominator)
                y = x
                for j, bit in enumerate(word):
                    if not initial_power and bad_at is None and y.numerator % 2 != bit:
                        bad_at = j
                    y = step(y, bit)
                power = two_exponent(y.denominator)
                expected = initial_power + n if initial_power else (
                    0 if bad_at is None else n - bad_at)
                check(power == expected, "exact dyadic escape length")
                valuations += 1
                escaped += int(power > 0)
    for H, length in ((1, 3), (2, 7), (3, 8), (5, 10)):
        refs = rationals(H)
        for word in product((0, 1), repeat=length):
            M, N, C = affine(word)
            brute = [x for x in refs if height((N * x + C) / M) <= H]
            check(brute == long_reference(word, H), "complete Euclidean decision")
            reconstructed += 1
            retained += len(brute)
    return {"valuation_tests": valuations, "nonintegral_terminals": escaped,
            "long_words_against_exhaustive_search": reconstructed,
            "long_words_admitting_a_reference": retained}


def min_pieces(word, H, physical):
    refs = rationals(H)
    best = [0] + [len(word) + 1] * len(word)
    for i in range(len(word)):
        for start in refs:
            y = start
            for j in range(i, len(word)):
                bit = word[j]
                if physical and (y.denominator % 2 == 0 or y.numerator % 2 != bit):
                    break
                y = step(y, bit)
                if 2**two_exponent(y.denominator) > H:
                    break
                if height(y) <= H:
                    best[j + 1] = min(best[j + 1], best[i] + 1)
    return best[-1]


def sharp_cuts():
    cases = []
    for k in range(1, 7):
        word = tuple(([0] * 14 + [1]) * k)
        affine_cost = min_pieces(word, 2, False)
        native_cost = min_pieces(word, 3, True)
        check(affine_cost == k and native_cost == k + 1, "sharp physical cut count")
        cases.append([k, affine_cost, native_cost])
    return cases


def crossing_families():
    rng = Random(261128)
    tested = total_vertices = min_runs = 0
    exact_costs = []
    for b in (8, 11, 16):
        h = 9 * b
        labels = {0, 2**h - 1, sum(2**i for i in range(0, h, 2))}
        labels.update(rng.getrandbits(h) for _ in range(61))
        sources = set()
        for mask in sorted(labels):
            word = tuple(bit for i in range(h)
                         for bit in ((1, 1, 1, 0) if mask & (1 << i) else (1, 1, 0, 1)))
            n = 2**len(word) + source_residue(word)
            check(n not in sources, "tile injection")
            sources.add(n)
            states, bits = [n], []
            odd_power = 1
            for j in range(40 * b):
                x = states[-1]
                bit = x % 2
                bits.append(bit)
                if bit:
                    odd_power *= 3
                states.append((3 * x + 1) // 2 if bit else x // 2)
                check(odd_power > 2**(j + 1) and states[-1] > n, "crossing or descent")
            check(tuple(bits[:len(word)]) == word, "native tile prefix")
            check(len(set(states)) == len(states), "simple full ordinary path")
            runs = sum(bit and (j == 0 or not bits[j - 1]) for j, bit in enumerate(bits))
            check(runs >= 9 * b, "odd-run floor")
            min_runs = min(runs, min_runs) if min_runs else runs
            if b == 8 and len(exact_costs) < 5:
                a, p = min_pieces(bits, 2, False), min_pieces(bits, 2, True)
                exact_costs.append([a, p])
            total_vertices += len(states)
            tested += 1
    return {"ordinary_sources": tested, "ordinary_vertices": total_vertices,
            "minimum_odd_runs_observed": min_runs,
            "first_five_height_two_costs_affine_then_physical": exact_costs}


if __name__ == "__main__":
    print(json.dumps({"pre_crossing": crossing_families(),
                      "sharp_piece_counts": sharp_cuts(),
                      "valuation_and_reconstruction": valuations_and_reconstruction()},
                     sort_keys=True))
