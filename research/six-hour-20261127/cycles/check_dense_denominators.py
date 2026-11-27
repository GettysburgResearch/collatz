"""Exact binary-gap controls, including Hamming distances at every proper lag."""
from hashlib import sha256
from math import gcd, lcm
from random import Random
import json


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def check(a, b, q, r, seed):
    base = [(i*b + a-1) // a for i in range(a+1)]
    baseline = [y-x for x, y in zip(base, base[1:])]
    centers = [i for i in range(1, a)
               if baseline[i-1] == 1 and baseline[i] == 2]
    n = q*r
    p = a*n
    A = b*n
    bits = Random(seed)
    variables = {i: [bits.randrange(2) for _ in range(q if j % 2 == 0 else r)]
                 for j, i in enumerate(centers)}
    all_dates = []
    for j in range(n):
        all_dates.extend(j*b+s+(values[j % len(values)] if (values := variables.get(i)) else 0)
                         for i, s in enumerate(base[:-1]))
    gaps = [y-x for x, y in zip(all_dates, [*all_dates[1:], A])]
    require(set(gaps) == {1, 2}, "binary word")
    profile = [a * E - i * b for i, E in enumerate(all_dates)]
    require(max(profile) - min(profile) < 2*a, "discrepancy width")
    # One exact bit per binary odd clock. Rotate and compare every proper shift.
    word = int("".join(str(e-1) for e in gaps), 2)
    mask = (1 << p)-1
    min_distance = min((word ^ (((word << v) & mask) | (word >> (p-v)))).bit_count()
                       for v in range(1, p))
    require(32 * min_distance >= p, "dense Hamming distances at every lag")
    C = 0
    for E in all_dates:
        C = 3*C + (1 << E)
    P = 3**a
    Q = 2**b
    D = Q**n - P**n
    g = gcd(C,D)
    d = D // g
    require(lcm(Q**q - P**q, Q**r - P**r) % d == 0, "complete denominator support")
    start = C // g
    curr = start
    lo = hi = curr
    for e in gaps:
        new, rem = divmod(3*curr+d, 1 << e)
        require(rem == 0 and new % 2, "actual odd phase")
        curr = new
        lo = min(lo, curr)
        hi = max(hi, curr)
    require(curr == start and d > 1, "rational periodic closure")
    require(64 * lo >= a*a*d and hi <= 4*a*a*d, "quadratic height control")
    return {"block_odd": a, "block_native": b, "q": q, "r": r, "seed": seed,
            "odd_period": p, "all_proper_lags_checked": p-1,
            "minimum_gap_hamming": min_distance,
            "all_window_defects_at_least": (min_distance+1)//2,
            "whole_bits": D.bit_length(), "reduced_bits": d.bit_length(),
            "reduced_sha256": sha256(d.to_bytes((d.bit_length()+7)//8, "big")).hexdigest()}


if __name__ == "__main__":
    print(json.dumps([check(*args) for args in
                      [(70,111,5,7,20261127), (70,111,7,11,101),
                       (559,886,5,7,257)]], indent=2))
