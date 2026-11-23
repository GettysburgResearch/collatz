#!/usr/bin/env python3
"""Exact finite controls for the infinite-dictionary lattice theorem.
No bounded search is reported as proof of an all-time conclusion.
Assertions are not used, so normal and optimized Python do identical work.
"""
from fractions import Fraction
from itertools import product
import hashlib
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def data(word):
    p, q, c = 1, 1, 0
    for bit in word:
        require(bit in (0, 1), "nonbinary word")
        if bit:
            p, q, c = 3*p, 2*q, 3*c+q
        else:
            p, q, c = p, 2*q, c
    return p, q, c


def replay(n, word):
    require(isinstance(n, int) and n > 0, "ordinary positive source required")
    xs = [n]
    for bit in word:
        require(n % 2 == bit, "wrong literal parity")
        n = (3*n+1)//2 if bit else n//2
        xs.append(n)
    return xs


def least_source(word, lift=0):
    p, q, c = data(word)
    n = (-c*pow(p, -1, q)) % q
    if n == 0:
        n = q
    return n+lift*q


def certificate(u, defects, K):
    p, q, c = data(u)
    require(K >= 1 and p < q, "contracting nonempty run required")
    d = q-p
    for t in defects:
        r, s, b = data(t)
        e = d*b-(s-r)*c
        require(r*p**K+abs(e) < s*q**K, "cutoff not paid")
    return p, q, c


def finite_trace(u, defects, ks, K, lift):
    """Terminal lookahead is retained to certify the last boundary lattice."""
    require(len(defects) == len(ks), "length mismatch")
    p, q, c = certificate(u, defects, K)
    require(all(k >= K for k in ks), "short run")
    word = tuple(b for k, t in zip(ks, defects) for b in u*k+t)+u*K
    n = least_source(word, lift)
    xs = replay(n, word)
    d, D, clock = q-p, q**K, 0
    hs = []
    for j in range(len(ks)+1):
        x = xs[clock]
        require((d*x-c) % D == 0, "missing next-boundary lattice")
        hs.append((d*x-c)//D)
        if j == len(ks):
            break
        k, t = ks[j], defects[j]
        v = xs[clock+k*len(u)]
        r, s, b = data(t)
        e = d*b-(s-r)*c
        y = xs[clock+k*len(u)+len(t)]
        require(q**k*(d*v-c) == p**k*(d*x-c), "repeated displacement")
        require(s*q**k*(d*y-c) == r*p**k*(d*x-c)+q**k*e,
                "complete macro transport")
        require(r*p**k*D+abs(e)*q**k < s*q**k*D, "larger exponent unpaid")
        clock += k*len(u)+len(t)
    for a, b in zip(hs, hs[1:]):
        require(b == 0 if a == 0 else abs(b) < abs(a), "integer descent")
    for j, h in enumerate(hs):
        require(abs(h) <= max(abs(hs[0])-j, 0), "finite quotient clock")
    return len(ks), len(word)


def main():
    count = {"cutoff_words": 0, "ordinary_traces": 0, "macro_edges": 0,
             "literal_steps": 0, "paid_integer_edges": 0,
             "zero_edges": 0, "rejected_controls": 0}
    u = (1, 0)
    for B in range(1, 9):
        words = [tuple(w) for length in range(B+1)
                 for w in product((0, 1), repeat=length)]
        certificate(u, words, 2*B)
        count["cutoff_words"] += len(words)
        if B <= 5:
            for t in words:
                for lift in (0, 1):
                    K = 2*B
                    edges, clocks = finite_trace(u, [t, tuple(reversed(t)), ()],
                                                 [K, K+1, K+3], K, lift)
                    count["ordinary_traces"] += 1
                    count["macro_edges"] += edges
                    count["literal_steps"] += clocks

    for ks in ([1, 1], [1, 2, 3, 1], [7, 2, 11], [1, 20, 2]):
        for lift in (0, 1, 2):
            edges, clocks = finite_trace((1, 0, 0), [(1,)]*len(ks), ks, 1, lift)
            count["ordinary_traces"] += 1
            count["macro_edges"] += edges
            count["literal_steps"] += clocks

    for a in range(5):
        for b in range(1, 13):
            for e in range(-8, 9):
                if a+abs(e) >= b:
                    continue
                for x in range(-10, 11):
                    if (a*x+e) % b:
                        continue
                    y = (a*x+e)//b
                    require(y == 0 if x == 0 else abs(y) < abs(x),
                            "paid affine edge failed")
                    count["paid_integer_edges"] += 1
                    count["zero_edges"] += int(x == 0)

    # Equality in the cutoff permits a nonzero integer fixed point.
    require(2*1 == 1*1+1 and not 1+abs(1) < 2, "strict boundary control")
    count["rejected_controls"] += 1

    # A legal source macro may leave zero if its endpoint lacks lookahead.
    certificate((1, 0), [(1,)], 2)
    require(replay(1, (1, 0)*2+(1,))[-1] == 2, "lookahead control")
    require((2-1) % 16 != 0, "lookahead unexpectedly retained")
    count["rejected_controls"] += 1

    # Odd-denominator rational cycle: all branches legal in the rational
    # extension, but the normalized fixed point is 6/7, not an integer.
    x = Fraction(11, 7)
    z = x
    for bit in (1, 0, 0, 1):
        require(z.denominator % 2 == 1 and z.numerator % 2 == bit,
                "rational parity control")
        z = (3*z+1)/2 if bit else z/2
    require(z == x, "rational cycle did not close")
    h = (5*x-1)/8
    require(h == Fraction(6, 7) and 128*h == 72*h+48 and 72+48 < 128,
            "integrality control")
    count["rejected_controls"] += 1

    # Wrong literal parity is rejected by ordinary replay.
    try:
        replay(13, (0, 0, 0, 1))
    except ValueError:
        count["rejected_controls"] += 1
    else:
        raise ValueError("damaged parity accepted")

    base = Path(__file__).resolve().parent
    print(json.dumps({"status": "PASS", "scope": "exact finite controls; no census proof",
                      "counts": count,
                      "source_sha256": {
                          name: hashlib.sha256((base/name).read_bytes()).hexdigest()
                          for name in ("LatticeDescent.lean", "INFINITE_DICTIONARY_DESCENT.md",
                                       "check_lattice_descent.py")}},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

