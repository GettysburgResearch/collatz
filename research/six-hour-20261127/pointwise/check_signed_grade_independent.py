"""Independent physical-clock controls for the signed-grade frontier.

This implementation visits native physical states, rather than obtaining
the signed clock by summing accelerated valuations. All checks survive -O.
"""
from collections import Counter
from fractions import Fraction
import json


def require(condition, context):
    if not condition:
        raise ArithmeticError(context)


def physical(x, sign):
    return (3 * x + sign) // 2 if x % 2 else x // 2


def first_mark(x, mark):
    seen = set()
    odds = time = 0
    while x != mark and x not in seen:
        seen.add(x)
        odds += x % 2
        x = physical(x, -1)
        time += 1
    return (odds, time) if x == mark else None


def split(c, m, A, D, upper_odds=None):
    x, y, q = c, m, 0
    for t in range(D):
        require(x % 2 == y % 2, ('parities', c, m, A, D, t))
        q += x % 2
        x, y = physical(x, 1), physical(y, -1)
        require(x > 0 and y > 0, ('positive', c, m, t))
        require(x + y == A * 3 ** q * 2 ** (D - t - 1),
                ('transport', c, m, A, D, t))
    if upper_odds is not None:
        require(q <= upper_odds, ('count', c, m, D, upper_odds, q))
    while x % 2 == 0:
        x //= 2
    if upper_odds is not None:
        require(x <= A * 3 ** upper_odds, ('odd-height', c, m, D))
    return x, q


def main():
    counts = Counter()
    for A, B, P in [(1, 1, 1), (5, 2, 3), (17, 7, 11)]:
        for c in range(1, 2002, 2):
            for D in range(1, 15):
                m = A * 2 ** D - c
                if m <= 0:
                    continue
                counts['all_positive_splits'] += 1
                split(c, m, A, D)
                result = first_mark(m, A)
                if result is None:
                    continue
                b, t = result
                if b % B == 0 and t == D + P * (b // B):
                    require(t >= D, ('funded', A, c, D))
                    split(c, m, A, D, b)
                    counts[f'marked_{A}'] += 1

    # Independently retain every physical suffix of the seven possible bases.
    branches = []
    for d in range(-3, 4):
        value = 51 * Fraction(2) ** d - 5
        v = 0
        while value.denominator != 1:
            value *= 2
            v -= 1
        while int(value) % 2 == 0:
            value /= 2
            v += 1
        B = int(value)
        hit = first_mark(B, 17)
        require(hit is None or (hit[0] + 1) % 7 != 0, ('branch', d))
        branches.append({'d': d, 'v': v, 'B': B, 'first_hit': hit})

    # Large parameters, selected independently of the author's consecutive sweep.
    for k in [1, 2, 7, 31, 127, 257, 1024]:
        c = (4 ** k - 1) // 3
        D = 2 * k
        m = 17 * 2 ** D - c
        require(first_mark(m, 17) == (7, D + 11), ('one-family', k))
        split(c, m, 17, D, 7)
        counts['large_one_family'] += 1
        c5 = 10 * c + 3
        e = 2 * k + 1
        for d in range(-3, 4):
            D = e + d
            if D < 1:
                continue
            m = 17 * 2 ** D - c5
            if m <= 0:
                continue
            hit = first_mark(m, 17)
            require(hit is None or hit[0] % 7 != 0, ('five-family', k, d))
            counts['large_five_family_branches'] += 1

    for modulus in [1, 3, 9, 27, 81, 243, 729, 2187, 6561]:
        # Recurrence c(k+1)=4c(k)+1 avoids modular exponentiation enumeration.
        residue = 0
        seen1, seen5 = set(), set()
        for _ in range(modulus):
            seen1.add(residue)
            seen5.add((10 * residue + 3) % modulus)
            residue = (4 * residue + 1) % modulus
        require(residue == 0 and len(seen1) == len(seen5) == modulus,
                ('ternary_permutation', modulus))
        counts['ternary_residues_per_family'] += modulus

    # Exact integer inequalities used in the two asymptotic estimates.
    exact = {
        '3^28 < 2^45': 3 ** 28 < 2 ** 45,
        '(2187/2048)^32 > 8': 2187 ** 32 > 8 * 2048 ** 32,
        '(2187/2048)^128 > 3^7': 2187 ** 128 > 3 ** 7 * 2048 ** 128,
        '(2187/2048)^16 > 2': 2187 ** 16 > 2 * 2048 ** 16,
        '19^7 < 2^30': 19 ** 7 < 2 ** 30,
        '5/48 < 153/1009': Fraction(5, 48) < Fraction(153, 1009),
    }
    require(all(exact.values()), 'strict asymptotic margins')
    print(json.dumps({'counts': dict(sorted(counts.items())), 'branches': branches,
                      'exact_margins': exact}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
