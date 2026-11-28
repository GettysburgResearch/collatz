"""Primitive normalization in arbitrary open reference packets, in exact arithmetic."""
from fractions import Fraction
from itertools import combinations
from math import gcd, prod
from random import Random
import json


def check(ok, reason):
    if not ok:
        raise ValueError(reason)


def valuation(n, p):
    value = 0
    n = abs(n)
    check(n > 0, "zero valuation input")
    while n % p == 0:
        value += 1
        n //= p
    return value


def rough(n):
    return abs(n) // (2**valuation(n, 2) * 3**valuation(n, 3))


def vp_abs(n, p):
    return Fraction(1, p**valuation(n, p))


def height(q):
    return max(abs(q.numerator), q.denominator)


def physical(n, length, q):
    grade = carry = 0
    for j in range(length):
        if n % 2:
            grade += 1
            carry = 3 * carry + 2**j
            n = (3 * n + q) // 2
        else:
            n //= 2
    return n, grade, carry


def packet(n, lengths, rng, force_pair, q=1):
    states, refs, shifts, grades = [n], [], [0], [0]
    ref = q * Fraction(rng.randrange(-11, 12), rng.choice([2, 3, 4, 5, 6, 7, 9]))
    first_jump = None
    for idx, length in enumerate(lengths):
        end, grade, carry = physical(states[-1], length, q)
        check(2**length * end == 3**grade * states[-1] + q * carry, "native law")
        target = (3**grade * ref + q * carry) / 2**length
        check(ref != states[-1], "reference separation")
        refs.append((ref, target))
        states.append(end)
        shifts.append(shifts[-1] + length)
        grades.append(grades[-1] + grade)
        if idx == 1 and force_pair:
            jump = -first_jump * Fraction(3**grade, 2**length)
        else:
            jump = Fraction(rng.randrange(-6, 7), rng.choice([1, 2, 3, 5, 6, 9]))
        if idx == 0:
            first_jump = jump
        ref = target - jump
    m = len(lengths)
    C = prod(q.denominator for pair in refs for q in pair)
    H = max(2, q * max(height(x / q) for pair in refs for x in pair))
    check(all(height(x) <= H for pair in refs for x in pair), "scaled references")
    P = 2 * C * H
    d, g = shifts[-1], grades[-1]
    terms = [C * 3**g * (n - refs[0][0])]
    for i in range(1, m):
        terms.append(C * (refs[i - 1][1] - refs[i][0]) *
                     2**shifts[i] * 3**(g - grades[i]))
    Z = C * 2**d * (states[-1] - refs[-1][1])
    check(sum(terms) == Z and Z, "reference telescope")
    check(all(q.denominator == 1 for q in [*terms, Z]), "integer clearing")
    terms, Z = [q.numerator for q in terms], Z.numerator
    high = min(states) > 10 * (m + 1) * 3**m * H
    if high:
        check(terms[0] > sum(abs(t) for t in terms[1:]), "boundary root dominance")
    retained = [i for i, x in enumerate(terms) if x]
    removed = 0
    while True:
        found = next((indices for count in range(2, len(retained))
                      for indices in combinations(retained[1:], count)
                      if not sum(terms[i] for i in indices)), None)
        if found is None:
            break
        retained = [i for i in retained if i not in found]
        removed += len(found)
    z = [terms[i] for i in retained]
    G = gcd(*z)
    primitive = [a // G for a in z]
    total = sum(primitive)
    check(total == Z // G, "pruned total")
    actual = prod(abs(t) for t in primitive) * vp_abs(total, 2)
    actual *= prod(vp_abs(t, 2) for t in primitive[1:])
    actual *= prod(vp_abs(t, 3) for t in primitive)
    predicted = (prod(rough(t) for t in z) * vp_abs(Z, 2) /
                 vp_abs(z[0], 2) / rough(G)**len(z))
    check(actual == predicted, "full product after primitive scaling")
    check(actual <= Fraction(C * (n + H) * P**m, 2**d), "numerical product bound")
    check(2**valuation(G, 2) <= C * (n + H), "complete dyadic part")
    check(3**valuation(G, 3) <= C * (states[-1] + H), "complete ternary part")
    if len(primitive) > 1:
        check(rough(G) <= P, "complete outside part")
        if high:
            T = max(map(abs, primitive))
            check(T == primitive[0] and T * 2*m*C*P*(n+H) >= 2**d,
                  "primitive height floor")
        for idx, y in zip(retained[1:], primitive[1:]):
            a = max(0, shifts[idx] - valuation(G, 2))
            b = max(0, g - grades[idx] - valuation(G, 3))
            scale = 2**a * 3**b
            check(y % scale == 0 and 1 <= abs(y // scale) <= P, "clamped coefficient")
    return high, removed, rough(G) > 1, (C % 6 == 0), gcd(states[-1], q) > 1


def main():
    rng = Random(26112802)
    total = dominated = removed = rough_scaling = mixed = 0
    for size in range(2, 9):
        for case in range(80):
            lengths = [rng.randint(1, 12) for _ in range(size)]
            bits = rng.choice([25, 140, 300])
            n = 2**bits + rng.getrandbits(min(bits, sum(lengths)))
            a, b, c, d, _ = packet(n, lengths, rng, case % 2 == 0 and size >= 3)
            total += 1
            dominated += a
            removed += b
            rough_scaling += c
            mixed += d
    rational_cases = shrinking = 0
    for q in (3, 5, 7, 9, 15, 25, 27):
        for i in range(24):
            n = q * (2**180 + rng.getrandbits(30)) + 1
            lengths = [rng.randint(1, 12) for _ in range(6)]
            *_, shrank = packet(n, lengths, rng, i % 2 == 0, q)
            shrinking += int(shrank)
            rational_cases += 1
    print(json.dumps({"ordinary_packets": total,
                      "positive_rational_packets": rational_cases,
                      "rational_packets_with_reduced_denominator_loss": shrinking,
                      "all_ordinary_boundaries_above_dominance_threshold": dominated,
                      "deleted_nonzero_coordinates_in_proper_zero_subsums": removed,
                      "nontrivial_prime_to_six_primitive_gcd": rough_scaling,
                      "common_reference_scales_divisible_by_six": mixed,
                      "claim": "finite normalization and height identities only"},
                     sort_keys=True))


if __name__ == "__main__":
    main()
