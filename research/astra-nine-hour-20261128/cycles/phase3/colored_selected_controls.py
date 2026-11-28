"""Exact Fourier periods, prime-root remainders, and a ramified cancellation family."""

from fractions import Fraction
from itertools import combinations
from math import gcd, lcm
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase2"))
from semigroup_controls import bezout, build, need, physical_numerator


def trim(p):
    while p and p[-1] == 0:
        p.pop()
    return p


def divide(p, q):
    """Ordinary division by a monic integer polynomial, coefficients low first."""
    p = trim(p[:])
    quotient = [0] * max(0, len(p) - len(q) + 1)
    while len(p) >= len(q):
        shift = len(p) - len(q)
        c = p[-1]
        quotient[shift] = c
        for i, v in enumerate(q):
            p[i + shift] -= c * v
        trim(p)
    return quotient, p


def cyclotomics(g):
    result = {}
    for ell in range(1, g + 1):
        if g % ell:
            continue
        p = [-1] + [0] * (ell - 1) + [1]
        for d, q in result.items():
            if ell % d == 0:
                p, rem = divide(p, q)
                need(not rem, "cyclotomic construction")
        result[ell] = p
    return result


def primitive_period(w):
    n = len(w)
    return next(j for j in range(1, n + 1)
                if n % j == 0 and all(w[i] == w[(i+j) % n] for i in range(n)))


def masks(holes, g):
    layers = {}
    for h, r in holes:
        layers.setdefault(h, [0] * g)[r] = 1
    return layers


def homogeneous(q, a, b):
    return abs(sum(c * a**i * b**(len(q)-1-i) for i, c in enumerate(q)))


def from_low_holes(g, N, U, holes):
    """Invert the actual colored-ray dictionary for holes below both generators."""
    a, b = bezout(U, N)
    need(all(0 <= h < min(U, N-U) and 0 <= r < g for h, r in holes),
         "low-hole family range")
    hs = []
    for i in range(g*N):
        q, h = divmod(i*U, N)
        r = (i*b + a*q) % g
        hs.append(h + N*int((h, r) in holes))
    word = tuple((hs[i] + U - hs[(i+1) % len(hs)]) // N for i in range(len(hs)))
    need(set(word) <= {0, 1}, "physical bit reconstruction")
    return word


def active_orders(layers, phis):
    return {ell for ell, p in phis.items() if ell > 1
            and any(divide(layer, p)[1] for layer in layers.values())}


def prime_remainder(layers, g, k, l, N, U, a, b, phi):
    s = k*U + l*N
    orientation, m = (1 if s > 0 else -1), abs(s)
    base = (Fraction(2)**k * Fraction(3)**l)**orientation
    shift = -orientation*(b*k-a*l)
    rows = {}
    for h, layer in layers.items():
        generation, rem = divmod(h, m)
        row = rows.setdefault(rem, [Fraction(0)]*g)
        for r, c in enumerate(layer):
            row[(r + shift*generation) % g] += c*base**generation
    return any(divide(row, phi)[1] for row in rows.values())


def spectrum_controls():
    total = inactive = root_checks = positive = 0
    for n in range(4, 16):
        for u in range(1, n):
            g = gcd(n, u)
            if g == 1:
                continue
            N, U = n//g, u//g
            a, b = bezout(U, N)
            phis = cyclotomics(g)
            for positions in combinations(range(n), u):
                w = tuple(int(i in positions) for i in range(n))
                if any(w[i:]+w[:i] < w for i in range(1, n)):
                    continue
                _, points, holes, _ = build(w)
                R = max(h for h, _ in points) - min(h for h, _ in points)
                need(1 + max((h for h, _ in holes), default=-1) == max(0, R-N+1),
                     "conductor from physical height range")
                raw_two, raw_three = 2**n, 3**u
                if raw_two > raw_three:
                    vals = [physical_numerator(w[j:]+w[:j]) for j in range(n)]
                    hi, lo = max(vals), min(vals)
                    need(3**R*(raw_three*lo)**N <= (hi*raw_two)**N,
                         "lower physical ratio bound")
                    need((hi*raw_three)**N <= 3**R*(raw_two*lo)**N,
                         "upper physical ratio bound")
                    positive += 1
                layers = masks(holes, g)
                active = active_orders(layers, phis)
                period = primitive_period(w)
                need(period == N*lcm(*active), "exact Fourier period")
                C = physical_numerator(w)
                for ell in set(phis) - active - {1}:
                    D = homogeneous(phis[ell], 2**N, 3**U)
                    need(C % D == 0, "complete inactive component")
                    inactive += 1
                if len(phis) == 2 and period == n:
                    for k in range(1, N):
                        for l in range(-k, 1):
                            if gcd(k, l) == 1 and 0 < abs(k*U+l*N) <= N//(k+1):
                                need(prime_remainder(layers, g, k, l, N, U, a, b, phis[g]),
                                     "prime component has nonzero binomial remainder")
                                root_checks += 1
                total += 1
    return total, inactive, root_checks, positive


def ramified_controls():
    count = 0
    for N in range(3, 151, 2):
        for U in range(2, N, 2):
            if gcd(N, U) > 1 or U//2 >= N-U:
                continue
            a, b = bezout(U, N)
            holes = {(0, 2), (0, b % 4), (U//2, 0)}
            w = from_low_holes(4, N, U, holes)
            need(primitive_period(w) == 4*N, "ramified primitive period")
            x, y = 3**(U//2), 2**((N-1)//2)
            c = (b-1)//2
            sign = 1 if c % 4 in (0, 3) else -1
            left = x*x - 2*sign*x*y + 2*y*y
            right = x*x + 2*sign*x*y + 2*y*y
            D4 = 2**(2*N) + 3**(2*U)
            need(left*right == D4 and gcd(left, right) == 1, "Aurifeuillean factors")
            need(gcd(D4, physical_numerator(w)) == left, "exact selected half-factor")
            count += 1
    return count


def main():
    total, inactive, roots, positive = spectrum_controls()
    n, u = 30, 18
    holes = {(0, r) for r in (0, 2, 4)} | {(1, r) for r in (0, 3)}
    word = from_low_holes(6, 5, 3, holes)
    active = active_orders(masks(holes, 6), cyclotomics(6))
    need(active == {2, 3} and primitive_period(word) == n, "inactive primitive top")
    D6 = homogeneous(cyclotomics(6)[6], 2**5, 3**3)
    need(D6 == 889 and physical_numerator(word) % D6 == 0, "inactive primitive factor")
    ramified = ramified_controls()
    print(f"{total} noncoprime necklaces through n=15 passed exact Fourier period.")
    print(f"{positive} positive rational necklaces passed both exact physical-ratio bounds.")
    print(f"{inactive} inactive components divided the actual affine numerator in full.")
    print(f"{roots} prime-component short-binomial remainders were nonzero.")
    print(f"Primitive (n,u)=({n},{u}) has support {{2,3}} and cancels full inactive D6=889.")
    print(f"{ramified} g=4 family types through odd N=149 had the exact selected Aurifeuillean factor.")


if __name__ == "__main__":
    main()
