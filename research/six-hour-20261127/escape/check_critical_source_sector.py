"""Exact integer checks of the critical gate and the compact rational sector."""

from collections import Counter
from math import gcd
import json


def check(condition, description):
    if not condition:
        raise ArithmeticError(description)


def grade(n):
    g = 0
    while 3**g < 1 << n:
        g += 1
    return g


def words(n):
    # C is the real affine numerator, W/3^g=sum_{i<depth}2^i/3^g_i.
    rows = [(0, 0, 0)]
    for j in range(n):
        Q = 1 << j
        rows = [(g + e, (3*C+Q if e else C), (3 if e else 1)*(W+Q))
                for g, C, W in rows for e in (0, 1)
                if 3**(g+e) >= 2*Q]
    return rows


def forward(a, q, n):
    num, g = a, 0
    passed = True
    for i in range(n):
        if num % 2:
            num = (3*num+q)//2
            g += 1
        else:
            num //= 2
        if 3**g < 1 << (i+1):
            passed = False
    return passed, g, num


def table(n):
    Q = 1 << n
    K = grade(n)
    q = 3**K
    count = Counter()
    maxima = {}
    expected = set()
    endpoints = Counter()
    for g, C, W in words(n):
        check(3*C <= W, ("normalized marked visits", n, C, W))
        k = g-K
        count[k] += 1
        residue = (-C * pow(3**k, -1, Q)) % Q
        first = Q//2 + (residue-Q//2) % Q
        sources = [a for a in range(first, 13*Q//2, Q) if gcd(a, 6) == 1]
        check(len(sources) == 4, ("four reduced lifts", n, residue))
        for a in sources:
            z, rem = divmod(3**k*a+C, Q)
            check(rem == 0 and z > 0, ("ordinary endpoint", n, a))
            endpoints[z] += 1
            maxima[k] = max(maxima.get(k, 0), z)
            if n <= 12:
                check(a not in expected, ("duplicate within full sector", n, a))
                expected.add(a)
                passed, native_g, num = forward(a, q, n)
                check(passed and native_g == g and num == q*z,
                      ("physical forward match", n, a))
    if n <= 12:
        scanned = {a for a in range(Q//2, 13*Q//2)
                   if gcd(a, 6) == 1 and forward(a, q, n)[0]}
        check(scanned == expected, ("independent full rational census", n))
    return {"n": n, "critical_grade": K, "critical_word_counts_by_excess": dict(count),
            "max_ordinary_endpoint_by_excess": maxima,
            "distinct_endpoints": len(endpoints), "reduced_sources": sum(endpoints.values()),
            "full_rational_scan": n <= 12}


def balanced(n):
    q = 3**grade(n)
    g = C = 0
    for i in range(n):
        if 3**g < 1 << (i+1):
            g += 1
            C = 3*C + (1 << i)
    check(9*C >= g*(1 << n), ("critical mechanical offset grows", n))
    return {"depth": n, "grade": g, "offset_floor": C >> n,
            "critical_den_to_binary_ratio_floor": q >> n}


def lift_example(n, h, b, y):
    # Balanced core taken AFTER an initial run to test a prescribed
    # real lift, not to sample the asymptotic pool of bounded-occupation cores.
    K = grade(n)
    t = n-h
    m, l = t-b-8, K-b-5
    core = [((i+1)*l+m-1)//m-(i*l+m-1)//m for i in range(m)]
    tail = [1, 1, 1, 1, 0, 1, 0, 0] if y % 3 == 1 else [1, 1, 1, 1, 1, 0, 0, 0]
    bits = [1]*b + core + tail
    C = g = 0
    for i, e in enumerate(bits):
        if e:
            g += 1
            C = 3*C + (1 << i)
        check(3**g >= 1 << (i+1), ("critical lift gate", n, i))
    Q = 1 << n
    q = 3**K
    a = (1 << t)*y-C
    check(sum(bits) == K and gcd(a, 6) == 1, "full lift denominator")
    check(Q//2 <= a < 13*Q//2 and 32*abs(C-q) <= q, "compact real lift")
    ok, native, end = forward(a, q, t)
    check(ok and native == K and end == q*y, "actual prescribed rational lift")
    return {"depth": n, "earlier_landing_by": h, "ones_prelude": b,
            "target": y, "denominator_exponent": K,
            "numerator_bits": a.bit_length()}


if __name__ == "__main__":
    print(json.dumps({"finite_sectors": [table(n) for n in (5, 8, 12, 16, 20)],
                      "mechanical_words": [balanced(n) for n in (32, 256, 2048)],
                      "compact_lifts": [lift_example(512, 55, 30, 5*(1 << 55)+r)
                                        for r in range(3)]}, indent=2, sort_keys=True))
