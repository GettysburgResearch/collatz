"""Finite exact controls for the paired-rotation and Euclidean arguments."""
from collections import Counter
from itertools import product
from math import gcd
import json


def require(check, message):
    if not check:
        raise AssertionError(message)


def digits(a, b):
    result = []
    while a:
        q, b, a = b // a, a, b % a
        result.append(q)
    return result


def check_offset_relation(A, r):
    g = gcd(A, r)
    N = A // g
    u = pow(r // g, -1, N)
    partial = digits(u, N)
    # Consecutive convergents of [0; partial...] start at 1/0, 0/1.
    old_p, old_q = 1, 0
    p, q = 0, 1
    for a in partial:
        e = q*u - N*p
        require(0 < abs(e)*a*q <= N, "convergent remainder")
        require(a*q <= N and (e*r-g*q) % A == 0, "offset relation")
        old_p, p = p, a*p + old_p
        old_q, q = q, a*q + old_q
    require((p, q) == (u, N), "terminal convergent")
    return g, sum(partial)


def states(w):
    A, p = len(w), sum(w)
    D = 2**A - 3**p
    C = 0
    for j, b in enumerate(w):
        C = (3*C + 2**j) if b else C
    h = gcd(C, D)
    n, d = C // h, D // h
    numbers = []
    for b in w:
        require(n % 2 == b, "physical parity")
        numbers.append(n)
        n = (3*n+d) // 2 if b else n // 2
    require(n == numbers[0] and len(set(numbers)) == A, "primitive closure")
    return numbers, d


def words(limit, stats):
    for A in range(2, limit + 1):
        for w in product((0, 1), repeat=A):
            p = sum(w)
            if not p or 3**p >= 2**A:
                continue
            if any(w[r:]+w[:r] <= w for r in range(1, A)):
                continue
            n, d = states(w)
            stats["primitive_contracting_necklaces"] += 1
            for r in range(1, A):
                g, S = check_offset_relation(A, r)
                t = sum(w[i] != w[(i+r) % A] for i in range(A))
                unsigned = sum(w[i] < w[(i+r) % A] for i in range(A))
                require(t == 2*unsigned > 0, "loss count")
                # Every interval discrepancy calculated with integer scaling.
                for i in range(A):
                    require(n[(i+r) % A]+d <= 3**unsigned*(n[i]+d), "paired height")
                    counts = 0
                    lcp = 0
                    for j in range(A):
                        counts += w[(i+j) % A]
                        if lcp == j and w[(i+j) % A] == w[(i+j+r) % A]:
                            lcp += 1
                        require(abs(A*counts-(j+1)*p) <= A*(8*t*S+g), "discrepancy")
                    delta = abs(n[i]-n[(i+r) % A])
                    require(delta > 0 and delta % 2**lcp == 0, "matching run")
                    stats["phase_comparisons"] += 1
                    stats["interval_discrepancies"] += A
                stats["rotation_comparisons"] += 1


def main():
    result = Counter()
    words(13, result)
    for A in range(2, 500):
        for r in range(1, A):
            check_offset_relation(A, r)
            result["independent_euclidean_offsets"] += 1
    print(json.dumps(dict(sorted(result.items())), indent=2))


if __name__ == "__main__":
    main()
