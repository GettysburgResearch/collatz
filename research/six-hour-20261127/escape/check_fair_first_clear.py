"""Double-count the fair meander and its exact ordinary first-clear intervals."""
from collections import Counter
from fractions import Fraction
from math import comb, gcd
import json


def require(test, info):
    if not test:
        raise ArithmeticError(info)


def tails(K):
    n = 2*K
    total = comb(n, K)
    p = Counter()
    for h in range(1, K+1):
        p[h] = (1 << h)*h*comb(n-h-1, K-1)//K
    require(sum(p.values()) == total, ("ballot total", K))
    for h in p:
        require(sum(p[j] for j in p if j >= h) == (1 << h)*comb(n-h, K),
                ("exact Rayleigh tail", K, h))
    return p


def run(K):
    n, q = 2*K, 3**K
    Q = 1 << n
    rows = Counter()
    failures = Counter()
    direct = {}
    for a in range(Q//2, 13*Q//2):
        if gcd(a, 6) != 1:
            continue
        v, den, g, pair = a, q, 0, None
        for t in range(1, n+1):
            b = v%2
            v = (3*v+den)//2 if b else v//2
            d = gcd(v, den)
            v, den = v//d, den//d
            g += b
            if 2*g < t:
                break
            if den == 1 and pair is None:
                pair = (n-t, v)
        else:
            require(pair is not None, "not cleared")
            h, y = pair
            require(y%3 != 2, ("illegal target", y))
            rows[h] += 1
            direct[a] = pair
            ok = True
            for t in range(1, 25):
                b = v%2
                g += b
                v = (3*v+1)//2 if b else v//2
                if 3**(g-K) < 1 << t:
                    ok = False
                if ok:
                    failures[t] += 1
    expected = tails(K)
    require(rows == {h:4*v for h, v in expected.items()}, ("time law", K))
    profiles = 0
    covered = set()
    assertmax = Fraction(0)
    for h in expected:
        t = n-h
        for w in range(1 << t):
            if w.bit_count() != K or not ((w >> (t-1)) & 1):
                continue
            C = g = 0
            for i in range(t):
                bit = (w >> i)&1
                if bit:
                    C = 3*C+(1 << i)
                g += bit
                if 2*g < i+1:
                    break
            else:
                profiles += 1
                low = (Q//2+C+(1 << t)-1) >> t
                high = (13*Q//2+C+(1 << t)-1) >> t
                ys = [y for y in range(low, high) if y%3 != 2]
                require(len(ys) == 4*(1 << h), "uniform finite first-clear row")
                flat = {y for y in range(1 << (h-1), 13 << (h-1)) if y%3 != 2}
                overlap = len(flat.intersection(ys))
                assertmax = max(assertmax, Fraction(len(ys)-overlap, len(ys)))
                for y in ys:
                    a = (1 << t)*y-C
                    require(direct[a] == (h,y) and a not in covered,
                            ("row mismatch", n, h, a))
                    covered.add(a)
    require(len(covered) == len(direct), "incomplete pair population")
    return {"n": n, "all_sources": len(direct), "prefixes": profiles,
            "clock_histogram": dict(sorted(rows.items())),
            "largest_conditional_tv": str(assertmax),
            "survival_at_critical_continuation_ticks": {k:failures[k] for k in (1, 4, 8, 16, 24)}}


if __name__ == "__main__":
    print(json.dumps({"complete_fair_sectors": [run(K) for K in (2, 3, 5, 7)],
                      "ballot_total_only": {K:sum(tails(K).values()) for K in (32, 64, 128)}},
                     indent=2, sort_keys=True))
