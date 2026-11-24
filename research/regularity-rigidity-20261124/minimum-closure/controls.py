"""Exact finite controls for the bounded-minimum excursion and inverse screen."""
from functools import lru_cache
import hashlib
import json


def require(ok, msg):
    if not ok:
        raise RuntimeError(msg)


def ceildiv(a, b):
    return (a + b - 1) // b


def strip():
    N, D = 4096, 128
    Rn, Rd, Qn, Qd = 16003, 3000, 100001, 100000
    require((16 * 2**30 + 7) * Rd <= 3 * 2**30 * Rn, "height cap")
    require(Qd * (3 * 2**30) <= Qn * (3 * 2**30 - N), "error cap")
    require(Rn < 8 * Rd and Rn * Qn < 8 * Rd * Qd, "grade window")
    last = D * Rn // Rd
    dp = [{0: 1} for _ in range(D, last + 1)]
    M = 1
    for j in range(1, N + 1):
        M *= 3
        a0 = M.bit_length() - 1
        ranges = {}
        for a in range(max(j, a0 - 4), min(2 * j, a0 + 4) + 1):
            b = 1 << a
            lo = ceildiv(D * Qd * b, Qn * M) - 1
            hi = (Rn * D * b) // (Rd * M)
            ranges[a] = (max(D, lo), min(last, hi))
        for k, old in enumerate(dp):
            i = D + k
            new = {}
            for a, c in old.items():
                for b in (a + 1, a + 2):
                    lr = ranges.get(b)
                    if lr is not None and lr[0] <= i <= lr[1]:
                        new[b] = new.get(b, 0) + c
            dp[k] = new
    C = sum(sum(d.values()) for d in dp)
    require(C**1000 < 3**(479 * N), "strict exponent 479/1000")
    return {"steps": N, "bins": len(dp), "count": str(C), "bits": C.bit_length(), "exponent_numerator": 479, "exponent_denominator": 1000}


def mechanical():
    K = 192
    a, p, b, q = 84, 53, 485, 306
    require(b * p - a * q == 1 and p + q > K + 1, "Farey gap")
    require(2**a < 3**p and 2**b > 3**q, "log bracket")
    A, P = a + b, p + q
    words = set(tuple((A * (i + 1) + t) // P - (A * i + t) // P for i in range(K + 1)) for t in range(P))
    factors = set()
    product_checks = 0
    for w in words:
        require(all(e in (1, 2) for e in w), "binary gap alphabet")
        for i in range(len(w)):
            S = 0
            for j in range(i, len(w)):
                S += w[j]
                require(2**S <= 3**(j - i + 2), "subword slope <= 3")
                product_checks += 1
        code = 0
        for j, e in enumerate(w):
            code = (code << 1) | (e - 1)
            if j >= 1:
                factors.add((j + 1, code))

    @lru_cache(None)
    def back(w, length, d, c):
        # Returning True is only a necessary possibility, not ordinary realization.
        if d == 0 and c == 0:
            return True
        if not length or c > length * (1 << d):
            return False
        if (d > 0 and (c <= 0 or c % 2 == 0)) or (d == 0 and c % 2):
            return False
        e = 1 + (w & 1)
        num = 3 * c - (1 << d) + 1
        if num < 0:
            return False
        for f in range(1, d + e + 1):
            dd = d + e - f
            if num % (1 << f):
                continue
            cc = num >> f
            if (dd == 0 and cc % 2) or (dd > 0 and (cc == 0 or cc % 2 == 0)):
                continue
            r = 1 if e == 2 else 2
            z = (pow(2, dd, 3) * r + cc) % 3
            if pow(2, f, 3) * z % 3 != 1:
                continue
            if back(w >> 1, length - 1, dd, cc):
                return True
        return False

    tests = 0
    for length, w in sorted(factors):
        e = 1 + (w & 1)
        r = 1 if e == 2 else 2
        for c in range(2, length, 2):
            if c % 3 != (-r) % 3 and not (e == 2 and c % 3 == 1):
                continue
            tests += 1
            require(not back(w >> 1, length - 1, 0, c), "active/terminal crossing")
    info = back.cache_info()
    return {"depth": K, "slope_bracket": [[a, p], [b, q]], "factor_words": len(words), "prefixes_with_next_gap": len(factors), "subword_product_checks": product_checks, "crossing_tests": tests, "cache_hits": info.hits, "cache_misses": info.misses}


def rational_controls():
    from math import gcd
    tested = 0
    min_controls = []
    for A, p in [(5, 3), (8, 5), (27, 17), (46, 29), (65, 41), (149, 94), (485, 306), (1539, 971)]:
        require(gcd(A, p) == 1 and 2**A > 3**p and 2 * A > 3 * p and A < 2 * p, "slope")
        D = 2**A - 3**p
        e = [(A * (i + 1) + p - 1) // p - (A * i + p - 1) // p for i in range(p)]
        C = 0
        for i, gap in enumerate(e):
            C = (C << gap) + 3**i
        z = C
        max_z = C
        for gap in e:
            require(z > 0 and z % 2 == 1 and z % 3 != 0 and gcd(z, D) == 1, "literal rational phase")
            require(C <= z < 2 * C, "minimum and span")
            max_z = max(max_z, z)
            w = (z << gap) - D
            require(w % 3 == 0, "inverse integer numerator")
            z = w // 3
            tested += 1
        require(z == C and (C * pow(D, -1, 9)) % 9 == 1, "lap and minimum residue")
        min_controls.append({"p": p, "A": A, "denominator_bits": D.bit_length(), "floor_minimum": C // D})
    return {"rational_phase_controls": tested, "cycles": min_controls}


if __name__ == "__main__":
    print(json.dumps({"strip": strip(), "mechanical": mechanical(), "rational": rational_controls()}, indent=2))
