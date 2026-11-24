"""Exact finite controls for the rank-two cancellation and Apéry factor tests."""

from itertools import accumulate, combinations
from math import gcd, prod
import json


def require(test, context):
    if not test:
        raise RuntimeError(context)


def generator(p, A, modulus):
    u = pow(p, -1, A)
    v = (1 - u * p) // A
    return pow(2, u, modulus) * pow(3, v, modulus) % modulus


def word_data(gaps):
    p, A = len(gaps), sum(gaps)
    modulus = abs(2**A - 3**p)
    E = [0, *accumulate(gaps[:-1])]
    C = sum(2**e * 3**(p - 1 - i) for i, e in enumerate(E))
    raw = [p * e - A * i for i, e in enumerate(E)]
    T = [s - min(raw) for s in raw]
    return p, A, modulus, C, T


def check_physical():
    words = reciprocal = 0
    numerical = {}
    for p in range(2, 9):
        for A in range(p + 1, 2*p + 1):
            if gcd(p, A) != 1:
                continue
            for cuts in combinations(range(1, A), p - 1):
                edges = (0, *cuts, A)
                gaps = [j - i for i, j in zip(edges, edges[1:])]
                _, _, D, C, T = word_data(gaps)
                a = A - p
                require(all(T[(i+1) % p] + a == T[i] + p*(e-1)
                            for i, e in enumerate(gaps)), (gaps, "edge"))
                require(len({s % p for s in T}) == p, (gaps, "Apéry"))
                require(all(s <= a*j for j, s in enumerate(sorted(T))), (gaps, "rank"))
                if D > 1:
                    z = generator(p, A, D)
                    require(pow(z, p, D) == 2 % D and pow(z, A, D) == 3 % D,
                            (gaps, "generator"))
                    M = sum(pow(z, t, D) for t in T)
                    require(gcd(D, M) == gcd(D, C), (gaps, "whole gcd"))
                H = max(T)
                if set(T) == {H-t for t in T}:
                    k = T.index(H-T[0])
                    require(all(T[(k-i) % p] == H-T[i] and
                                gaps[(k-i-1) % p] == gaps[i] for i in range(p)),
                            (gaps, "reflection"))
                    reciprocal += 1
                if gaps == [2, 2, 2, 1, 1]:
                    numerical = {"p": p, "A": A, "gaps": gaps, "exponents": T,
                                 "C": C, "D": D, "reduced_denominator": D//gcd(D, C)}
                words += 1
    require(numerical.get("C") == 653 and numerical["reduced_denominator"] == 13,
            numerical)
    return {"words": words, "reciprocal": reciprocal, "nonprogression": numerical}


def gaps_from_set(p, A, S):
    by_residue = {s % p: s for s in S}
    require(len(S) == len(by_residue) == p and 0 in S, "not a normalized transversal")
    a = A-p
    T = [by_residue[-a*i % p] for i in range(p)]
    gaps = [(A+T[(i+1) % p]-T[i])//p for i in range(p)]
    require(min(gaps) >= 1 and sum(gaps) == A, "illegal cycle")
    return gaps


def next_clock(p):
    A = (3**p).bit_length()
    while gcd(A, p) != 1:
        A += 1
    return A


def check_lifts():
    cases = []
    for b, outer, lengths in [
        (7, (0, 1, 3, 4, 5, 6, 9), (17, 32, 49, 128)),
        (6, (0, 2, 3, 4, 5, 7), (17, 49)),
    ]:
        outer_res = {t % b: t for t in outer}
        c = max(outer_res[(t+1) % b]-t for t in outer)
        for L in lengths:
            p = b*L
            A = next_clock(p)
            a, D = A-p, 2**A-3**p
            w0 = a//c
            w = w0-(w0-a) % b
            m = L*w
            require(w > 0, (b, L, w))
            S = {i*a+m*t for i in range(L) for t in outer}
            gaps = gaps_from_set(p, A, S)
            _, _, _, C, T = word_data(gaps)
            require(set(T) == S, (p, "normalized lift"))
            z = generator(p, A, D)
            step = pow(z, m, D)
            inner = sum(pow(z, i*a, D) for i in range(L)) % D
            H = sum(pow(step, t, D) for t in outer) % D
            require(gcd(D, inner*H) == gcd(D, C), (p, "total modulus"))
            require((pow(z, L*a, D)-1) % gcd(D, inner) == 0, (p, "inner order"))
            entry = {"p": p, "A": A, "base": b, "m": m,
                     "span": max(S), "gcd": gcd(D, C)}
            if b == 7:
                tor = sum(pow(step, t, D) for t in range(7)) % D
                core = (1-pow(step, 2, D)+pow(step, 3, D)) % D
                require(tor*core % D == H, (p, "cubic factorization"))
                entry.update(nontorsion_degree=3*m, cubic_gcd=gcd(D, core))
            cases.append(entry)
    return cases


def check_lattice():
    checked = squareful = noncoprime = 0
    for p in range(2, 18):
        for A in range(p, 3*p):
            D = abs(2**A-3**p)
            if D == 1:
                continue
            for r, s in ((-2, 3), (1, -2), (3, 2), (-3, -1), (5, 0), (0, 5)):
                delta = A*s+p*r
                if not delta:
                    continue
                v = pow(2, r, D)*pow(3, s, D) % D
                for core in (v*v-v-1, v*v+v+1, v*v-1, v-1):
                    G = gcd(D, core)
                    if G == 1:
                        continue
                    for i, j in ((-2, 3), (3, -4), (0, 1)):
                        U = pow(2, i*A+j*r, G)*pow(3, -i*p+j*s, G) % G
                        require(U == pow(v, j, G), (p, A, r, s, G, "local lift"))
                    squareful += any(G % (q*q) == 0 for q in (5, 7, 11, 13, 17, 19))
                    noncoprime += gcd(A, p) != 1
                    checked += 1
    require(squareful and noncoprime, "missing composite controls")
    return {"nontrivial_gcds": checked, "verified_square_prime_divisor": squareful,
            "noncoprime_clocks": noncoprime}


def check_binary_digits():
    cases = 0
    for j in range(3, 9):
        p = 2**j
        A = next_clock(p)
        for choice in range(2**max(1, j-2)):
            steps = [2**i * (3 if choice & (1 << i) else 1) for i in range(j)]
            steps.sort()
            S = {0}
            for w in steps:
                S |= {s+w for s in S}
            gaps = gaps_from_set(p, A, S)
            _, _, D, C, _ = word_data(gaps)
            require(all(w <= (A-p)*2**i for i, w in enumerate(steps)),
                    (p, steps, "sorted step cap"))
            z = generator(p, A, D)
            values = [1+pow(z, w, D) for w in steps]
            require(gcd(D, prod(values)) == gcd(D, C), (p, steps, "digit gcd"))
            for w, value in zip(steps, values):
                G = gcd(D, value)
                require((pow(z, 2*w, D)-1) % G == 0, (p, w, "order"))
            cases += 1
    return cases


if __name__ == "__main__":
    print(json.dumps({"physical": check_physical(), "pullback_lifts": check_lifts(),
                      "local_lattice": check_lattice(), "binary_digit_masks": check_binary_digits()},
                     indent=2, sort_keys=True))
