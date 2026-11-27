"""Exact finite checks for the reduced 3-power rational source sector."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import comb, gcd
import json


HORIZONS = (0, 1, 4, 8, 16, 32, 64, 128, 256)


def require(condition, context):
    if not condition:
        raise RuntimeError(context)


def ordinary_step(z):
    return (3*z+1)//2 if z%2 else z//2


def rational_step(a, q):
    if a%2:
        a = (3*a+q)//2
        if q%3 == 0:
            a //= 3
            q //= 3
    else:
        a //= 2
    return a, q


@lru_cache(None)
def last_passing_clock(z, k):
    slack = 8*k
    for i in range(1, HORIZONS[-1]+1):
        slack += 8*(z%2)-5
        z = ordinary_step(z)
        if slack < 0:
            return i-1
    return HORIZONS[-1]


def direct_counts(j):
    n = 8*j
    Q = 2**n
    den = 3**(5*j)
    counts = Counter()
    for a in range(Q//2+1, 7*Q//2, 2):
        if a%3 == 0:
            continue
        old = a
        q = den
        g = 0
        for i in range(1, n+1):
            g += a%2
            a, q = rational_step(a, q)
            if 8*g < 5*i:
                break
        else:
            require(q == 1 and gcd(old, den) == 1, "independent actual clearance")
            counts[(a, g-5*j)] += 1
    return counts


def catalogue(j):
    n = 8*j
    Q = 2**n
    words = Counter()
    endpoints = Counter()
    max_offset = Counter()
    max_z = Counter()
    modulus = {k: 3**k for k in range(3*j+1)}
    inverses = {k: pow(v, -1, Q) for k, v in modulus.items()}

    def visit(i, g, C):
        if i < n:
            if 8*g >= 5*(i+1):
                visit(i+1, g, C)
            visit(i+1, g+1, 3*C+2**i)
            return
        k = g-5*j
        require(0 <= C < 25*modulus[k]*Q, "finite offset cap")
        if k == 0:
            require(13*C <= 319*(Q-3**(5*j)), "exact-grade mechanical upper")
        words[k] += 1
        max_offset[k] = max(max_offset[k], C)
        r = (-C*inverses[k]) % Q
        require(r%2 == 1, "odd numerator residue")
        first = Q//2+(r-Q//2) % Q
        unit_lifts = 0
        for a in range(first, 7*Q//2, Q):
            if a%3 == 0:
                continue
            unit_lifts += 1
            numerator = modulus[k]*a+C
            require(numerator%Q == 0, "ordinary endpoint")
            z = numerator//Q
            require(0 < z < 29*modulus[k], "ordinary size")
            endpoints[(z, k)] += 1
            max_z[k] = max(max_z[k], z)
        require(unit_lifts == 2, "two reduced lifts per passing word")

    visit(0, 0, 0)
    require(n*words[0] >= comb(n, 5*j), "cyclic-rotation lower bound")
    if j <= 2:
        require(endpoints == direct_counts(j), "independent source/word census")
    D = sum(endpoints.values())
    require(D == 2*sum(words.values()), "whole population identity")
    survival = {L: sum(count for pair, count in endpoints.items()
                       if last_passing_clock(*pair) >= L) for L in HORIZONS}
    require(survival[0] == D, "initial denominator")
    return {"j": j, "n": n, "source_denominator": 3**(5*j), "Q": Q,
            "accepted_words_by_excess": dict(sorted(words.items())),
            "reduced_sources": D, "distinct_endpoint_excess_pairs": len(endpoints),
            "max_C_by_excess": dict(sorted(max_offset.items())),
            "max_endpoint_by_excess": dict(sorted(max_z.items())),
            "conditional_numerators": survival}


def affine(bits):
    g = C = 0
    for i, bit in enumerate(bits):
        if bit:
            C = 3*C+2**i
            g += 1
    return g, C


def lifted_target(y, j):
    H = y.bit_length()-1
    n = 8*j
    t = n-H
    length = t-8
    odds = 5*(j-1)
    require(27*odds <= 17*length, "bounded steep slope")
    ceil_div = lambda a, b: (a+b-1)//b
    core = [ceil_div((i+1)*odds, length)-ceil_div(i*odds, length)
            for i in range(length)]
    tail = [int(x) for x in ("11110100" if y%3 == 1 else "11111000")]
    bits = core+tail
    g, C = affine(bits)
    require(g == 5*j, "prescribed clearing grade")
    q = 3**g
    a = 2**t*y-C
    Q = 2**n
    require(Q//2 <= a < 7*Q//2 and gcd(a, 6) == 1, "lift in reduced shell")
    now, den, tally = a, q, 0
    for i, bit in enumerate(bits, 1):
        require(now%2 == bit and now>0, "positive prescribed rational prefix")
        tally += bit
        now, den = rational_step(now, den)
        require(8*tally >= 5*i, "prefix gate")
    require((now, den) == (y, 1) and 8*tally-5*t == 5*H,
            "specified ordinary target and exact surplus")
    return {"target": y, "j": j, "landing_clock": t, "gate_credit": 5*H,
            "source_numerator_bits": a.bit_length(),
            "source_denominator_bits": q.bit_length(),
            "normalized_numerator_floor_times_1024": a*1024//Q,
            "actual_reduced_denominator": True}


def main():
    n0 = 29*3**41
    require(n0 < 2**71 < 29*3**42, "reported-verification cutoff range")
    K = 41
    r = Fraction(3, 5)
    tail = 160*r**(K+1)*((8*(K+1)+3)/(1-r)+8*r/(1-r)**2)
    require(tail < Fraction(68, 1_000_000), "explicit tail")
    print(json.dumps({"scope": "finite source and word populations; no infinite survivor search",
                      "censuses": [catalogue(j) for j in (1, 2, 3)],
                      "long_target_controls": [lifted_target(y, 350) for y in (1023, 1024, 1025)],
                      "verified_range_tail_upper": str(tail),
                      "max_endpoint_for_excess_41": n0}, indent=2))


if __name__ == "__main__":
    main()

