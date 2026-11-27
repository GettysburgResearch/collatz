"""Exact cyclic-offset and first-denominator-clearance controls."""
from collections import Counter
from math import gcd
import json


def check(p, detail):
    if not p:
        raise ArithmeticError(detail)


def grade(n):
    k = 0
    while 3**k < 1 << n:
        k += 1
    return k


def rotations(n):
    passed, comparison = 0, 0
    minima = {}
    K = grade(n)
    for word in range(1 << n):
        g = word.bit_count()
        if g < K:
            continue
        r = 0
        for start in range(n):
            used = 0
            for i in range(n):
                used += (word >> ((start+i) % n)) & 1
                if 3**used < 1 << (i+1):
                    break
            else:
                r += 1
        check(r > 0 and (g <= r or 3**(g-r) <= 1 << (n-r)), (n, word, g, r))
        passed += 1
        comparison += r
        minima[g-K] = min(minima.get(g-K, n), r)
    return {"n": n, "near_or_above_critical_words": passed,
            "passing_rotations_with_multiplicities": comparison,
            "minimum_rotation_count_by_excess": minima}


def census(n):
    Q = 1 << n
    K = grade(n)
    q = 3**K
    rows = Counter()
    targets = Counter()
    for a in range(Q//2, 13*Q//2):
        if gcd(a, 6) != 1:
            continue
        v, den, g, hit = a, q, 0, None
        for i in range(1, n+1):
            if v % 2:
                v = (3*v+den)//2
                g += 1
            else:
                v //= 2
            d = gcd(v, den)
            v, den = v//d, den//d
            if 3**g < 1 << i:
                break
            if den == 1 and hit is None:
                check(g == K and v % 3 != 2, (n, a, "first clear"))
                hit = (n-i, v)
        else:
            check(hit is not None, (n, a, "no clearance"))
            h, y = hit
            check(2*y >= 1 << h, (n, a, "preimage height"))
            z = y
            for _ in range(h):
                z = (3*z+1)//2 if z%2 else z//2
            check(z == v, (n, a, "ordinary suffix"))
            rows[h] += 1
            targets[y] += 1
    return {"n": n, "rows_by_remaining_clock": rows,
            "first_clear_support": len(targets), "minimum_target": min(targets),
            "maximum_target": max(targets), "all_sources": sum(rows.values())}


def exact_lift(n, h, b, y):
    K, t = grade(n), n-h
    m, l = t-b-1, K-b-1
    core = [((i+1)*l+m-1)//m-(i*l+m-1)//m for i in range(m)]
    bits = [1]*b + core + [1]
    C, g = 0, 0
    for i, e in enumerate(bits):
        C = (3*C+(1 << i)) if e else C
        g += e
        check(3**g >= 1 << (i+1), ("gate", i))
    q = 3**K
    Q = 1 << n
    a = (1 << t)*y-C
    check(Q//2 <= a < 13*Q//2 and gcd(a, 6) == 1, "compact reduced source")
    v, den = a, q
    for i, e in enumerate(bits, start=1):
        check(v%2 == e and den > 1, "word and uncleared denominator")
        v = (3*v+den)//2 if e else v//2
        d = gcd(v, den)
        v, den = v//d, den//d
    check(den == 1 and v == y, "true first-clear terminal")
    return {"n": n, "h": h, "prelude": b, "first_clear": y,
            "grade": K, "earlier_physical_time": t}


if __name__ == "__main__":
    ys = [5*(1 << 55)+r for r in range(3)]
    print(json.dumps({"rotation_censuses": [rotations(n) for n in range(1, 13)],
                      "first_clear_censuses": [census(n) for n in (5, 8, 12)],
                      "first_clear_lifts": [exact_lift(512, 55, 30, y) for y in ys if y%3 != 2]},
                     indent=2, sort_keys=True))
