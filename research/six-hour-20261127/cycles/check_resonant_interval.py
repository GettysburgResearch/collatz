"""Exact cyclotomic and four-defect controls for the resonant interval."""
from fractions import Fraction
from hashlib import sha256
from math import gcd, prod
import json


def require(ok, msg):
    if not ok:
        raise ArithmeticError(msg)


def divisors(n):
    return [k for k in range(1, n + 1) if n % k == 0]


def digest(n):
    return sha256(n.to_bytes((n.bit_length() + 7) // 8, "big")).hexdigest()


def check(primes, a, b):
    R = prod(primes)
    n = 6 * R
    periods = [n // 2, *(n // (3 * t) for t in primes)]
    B = n // 3
    L = len(periods)
    P = 3**a
    Q = 2**b
    require(L + 6 < a < b - L - 6 and P < Q, "block controls")
    weights = [3 ** (L-1-i) * 4**i for i in range(L)]
    c = 3 ** (a-L) * (4**L + sum(weights)) - 4**L * 2 ** (a-L)
    offsets = []
    dates = []
    for j in range(n):
        bits = [int(j % t == 0) for t in periods]
        offsets.append(c + 3 ** (a-L) * sum(k * s for k, s in zip(weights, bits)))
        dates.extend(j * b + 2*i + s for i, s in enumerate(bits))
        dates.extend(j * b + s for s in range(2 * L, a + L))
    p = a * n
    A = b * n
    require(len(dates) == p and dates == sorted(set(dates)), "native odd dates")
    start = dates[0]
    E = [x-start for x in dates] + [A+x-start for x in dates]
    v = a * B
    u = b * B
    J = [i for i in range(p) if E[i+v] - E[i] != u]
    require(J == [0, a*R, 3*a*R, 4*a*R], "four direct exception locations")
    h = max((i-J[j-1]) % p for j, i in enumerate(J))
    require(3*h == p and p*u == A*v, "spacing and resonance")
    first = min(u, E[v])
    Z = sum(3 ** (p-h-i) * ((1 << (E[i]+u-first)) - (1 << (E[i+v]-first)))
            for i in J)
    require(Z % 2, "nonzero odd sparse residual")
    C = 0
    D = Q**n - P**n
    qpow = 1
    for value in offsets:
        C = P*C + qpow*value
        qpow *= Q
    Codd = 0
    for clock in E[:p]:
        Codd = 3*Codd + (1 << clock)
    require(gcd(D, Codd) == gcd(D, C), "block and odd reduced denominators")
    require(gcd(D, Z) == gcd(D, (Q**B - P**B) * C), "actual multiplier gcd")
    d = D // gcd(C, D)
    factors = {}
    phi = {}
    active = set()
    lost = set()
    Kprod = 1
    for ell in divisors(n):
        proper = [f for f in factors if ell % f == 0]
        M, rem = divmod(Q**ell - P**ell, prod(factors[f] for f in proper))
        require(rem == 0, "homogenized cyclotomic factor")
        factors[ell] = M
        phi[ell] = ell - sum(phi[f] for f in proper)
        K = sum((n // t) * k for t, k in zip(periods, weights) if t % ell == 0)
        if K:
            active.add(ell)
            if ell > 1:
                require(K % gcd(M, C) == 0, "complete active prime-power control")
                Kprod *= K
        if periods[0] % ell == 0 and B % ell:
            lost.add(ell)
    require(prod(factors.values()) == D, "complete determinant")
    inactive_prod = prod(m for ell, m in factors.items() if ell not in active)
    require(C % inactive_prod == 0, "joint inactive factors")
    active_high = prod(factors[ell] for ell in active if ell > 1)
    require(active_high <= d * Kprod and d <= (Q-P) * active_high, "C1")
    require(Z % prod(M for ell, M in factors.items() if ell not in lost) == 0,
            "joint sparse residual factors")
    rho = Fraction(1,2) + Fraction(1,6)*(1-prod(Fraction(r-1,r) for r in primes))
    require(sum(phi[ell] for ell in active) == n * rho, "character densities")
    require(3 * sum(phi[ell] for ell in lost) == n, "residual character fraction")
    return {
        "primes": primes, "blocks": n, "odd_period": p, "native_period": A,
        "character_fraction": str(rho), "sparse_residual_character_fraction": "2/3",
        "exception_count": len(J), "largest_spacing": h, "whole_bits": D.bit_length(),
        "reduced_bits": d.bit_length(), "sparse_gcd_bits": gcd(D, Z).bit_length(),
        "reduced_sha256": digest(d),
    }


if __name__ == "__main__":
    print(json.dumps([check(primes, 41, 65)
                      for primes in [[5], [7], [5, 7], [5, 11]]], indent=2))
