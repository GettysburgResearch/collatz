"""Replay the two independently periodic swap tracks with exact integer arithmetic."""

from fractions import Fraction
from hashlib import sha256
from math import gcd, isqrt
import json


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def numerator(word):
    value = 0
    for j, bit in enumerate(word):
        if bit:
            value = 3 * value + (1 << j)
    return value


def prime(value):
    return value >= 2 and all(value % d for d in range(2, isqrt(value) + 1))


def construct(m, q, r, t, tested_multiplier=0):
    base = [((j + 1) * q // m) - (j * q // m) for j in range(m)]
    sites = [j for j in range(m - 1) if base[j:j + 2] == [1, 0]][:2]
    check(len(sites) == 2, "two disjoint marked pairs are required")
    B, A = 2**m, 3**q
    D = B - A
    check(D > 0 and gcd(m, q) == 1, "grade conditions")
    check(prime(r) and prime(t) and r != t and min(r, t) > max(3, D), "track periods")
    c0 = numerator(base)
    c1, c2 = [(1 << j) * 3**sum(base[j + 2:]) for j in sites]
    blocks = {}
    for e in range(2):
        for f in range(2):
            word = base.copy()
            for j, flag in zip(sites, (e, f)):
                if flag:
                    word[j:j + 2] = [0, 1]
            check(numerator(word) == c0 + c1 * e + c2 * f, "affine-track additivity")
            blocks[e, f] = word

    k = (-r * (c0 + c2 * pow(t, -1, D)) * pow(c1, -1, D)) % D or D
    check(1 <= k < r, "nonconstant first forcing")
    dr, dt = B**r - A**r, B**t - A**t
    qr, qt = dr // D, dt // D
    qk = (B**k - A**k) // D
    x = Fraction(c0, D) + Fraction(c1 * A**(r - k) * qk, dr) + Fraction(c2 * A**(t - 1), dt)
    den = x.denominator
    check(den == qr * qt and gcd(den, 6 * D) == 1, "predicted exact reduced denominator")
    check(all(den % p for p in range(2, min(r, t) + 1) if prime(p)), "minimum prime factor")
    n = m * r * t
    if tested_multiplier:
        check(all(den % p for p in range(2, isqrt(n * tested_multiplier**2) + 1) if prime(p)),
              "specified square-root sieve")

    a = x.numerator
    smallest = largest = a
    boundaries = []
    blocks_used = set()
    for j in range(r * t):
        boundaries.append(a)
        e, f = int(j % r < k), int(j % t == 0)
        blocks_used.add((e, f))
        initial = a
        for bit in blocks[e, f]:
            smallest = min(smallest, a)
            largest = max(largest, a)
            check(a % 2 == bit, "reduced source has wrong native parity")
            a = ((3 * a + den) if bit else a) // 2
        check(B * a == A * initial + den * (c0 + c1 * e + c2 * f), "macro recurrence")
    check(a == x.numerator and len(blocks_used) == 4, "native closure and independent flags")
    boundaries.sort()
    boundary_gap = min(b - a for a, b in zip(boundaries, boundaries[1:]))
    check(0 < boundary_gap < den, "all boundary phases distinct, with subunit real spacing")
    check(len(boundaries) == r * t and gcd(m, q) == 1, "least-period grade and block witness")
    return dict(macro_clock=m, macro_grade=q, macro_defect=D, tracks=[r, t], first_track_duty=k,
                least_period=n, exact_reduced_denominator_bits=den.bit_length(),
                reduced_denominator_sha256=sha256(den.to_bytes((den.bit_length() + 7) // 8, 'big')).hexdigest(),
                phase_minimum_floor=smallest // den, phase_maximum_ceiling=-(-largest // den),
                distinct_boundary_phases=r*t, subunit_boundary_spacing=True,
                sieve_primes_checked_through=max(min(r, t), isqrt(n * tested_multiplier**2)))


if __name__ == '__main__':
    cases = [(8, 5, 17, 19, 0), (7, 4, 53, 59, 0), (8, 5, 181, 241, 1)]
    print(json.dumps([construct(*case) for case in cases], indent=2, sort_keys=True))
