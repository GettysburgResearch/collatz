#!/usr/bin/env python3
"""Exact small-jet scanner for Q_u^(5)(1+x) over F_p.

Uses the proved block decomposition.  Every Pochhammer factor is split into
its exact x-order and a unit; the Rogers--Szego recurrence computes F-block
jets in O((u-b)J^2).  This avoids constructing the degree-2u(u+1) Q-polynomial.
"""

from __future__ import annotations

import argparse
import random


def add(a, b, p, j):
    return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
            for i in range(j + 1)]


def sub(a, b, p, j):
    return [((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p
            for i in range(j + 1)]


def mul(a, b, p, j):
    c = [0] * (j + 1)
    for r, ar in enumerate(a[:j + 1]):
        if ar:
            lim = min(j - r, len(b) - 1)
            for s in range(lim + 1):
                c[r + s] = (c[r + s] + ar * b[s]) % p
    return c


def inv_series(a, p, j):
    if not a or a[0] % p == 0:
        raise ZeroDivisionError("nonunit series")
    z = [0] * (j + 1)
    z[0] = pow(a[0], -1, p)
    for n in range(1, j + 1):
        z[n] = -z[0] * sum(a[k] * z[n-k] for k in range(1, min(n, len(a)-1)+1)) % p
    return z


def pow_series(a, n, p, j):
    if n < 0:
        return pow_series(inv_series(a, p, j), -n, p, j)
    z = [1] + [0] * j
    b = a[:j+1] + [0] * max(0, j + 1 - len(a))
    while n:
        if n & 1:
            z = mul(z, b, p, j)
        b = mul(b, b, p, j)
        n >>= 1
    return z


def qpow(n, p, j):
    return pow_series([1, 1] + [0] * max(0, j - 1), n, p, j)


def W(n, p):
    z = n
    h = p
    while h <= n:
        z += (p - 1) * (h // p) * (n // h)
        h *= p
    return z


def V(u, b, p):
    return W(2*u + 1, p) - W(u, p) - W(u-b, p) - W(2*b + 1, p) + 2*W(b, p)


def factor_unit(i, p, j):
    """(1-(1+x)^i)/x^(p^v_p(i)), truncated; constant is nonzero."""
    pv = 1
    a = i
    while a % p == 0:
        a //= p
        pv *= p
    # -( ((1+x^pv)^a - 1) / x^pv )
    z = [0] * (j + 1)
    choose = 1
    for s in range(1, j // pv + 2):
        choose = choose * (a - s + 1) // s
        d = pv * (s - 1)
        if d <= j:
            z[d] = (-choose) % p
    return z


def factorial_units(n, p, j):
    out = [[1] + [0] * j]
    for i in range(1, n + 1):
        out.append(mul(out[-1], factor_unit(i, p, j), p, j))
    return out


def d_unit(u, b, units, p, j):
    z = mul(units[2*u + 1], mul(units[b], units[b], p, j), p, j)
    den = mul(units[u], mul(units[u-b], units[2*b + 1], p, j), p, j)
    return mul(z, inv_series(den, p, j), p, j)


def f_jet(N, b, p, j):
    """F_{N,b}(1+x) through x^j via Rogers--Szego recurrence."""
    t = qpow(2*b + N + 1, p, j)
    one_plus_t = add([1] + [0] * j, t, p, j)
    hm1 = [1] + [0] * j
    if N == 0:
        h = hm1
    else:
        h = one_plus_t
        for n in range(1, N):
            one_minus_qneg = sub([1] + [0] * j, qpow(-n, p, j), p, j)
            hn = sub(mul(one_plus_t, h, p, j),
                     mul(t, mul(one_minus_qneg, hm1, p, j), p, j), p, j)
            hm1, h = h, hn
    return mul(qpow(2*b*(b+1), p, j), h, p, j)


def q5_normalized_jet(u, p, j):
    vals = [V(u, b, p) for b in range(u + 1)]
    m = min(vals)
    relevant = [b for b, v in enumerate(vals) if v <= m + j]
    units = factorial_units(2*u + 1, p, j)
    total = [0] * (j + 1)
    for b in relevant:
        z = mul(d_unit(u, b, units, p, j), f_jet(u-b, b, p, j), p, j)
        sh = vals[b] - m
        for r in range(j + 1 - sh):
            total[r + sh] = (total[r + sh] + z[r]) % p
    first = next((r for r, a in enumerate(total) if a), None)
    return m, first, total, relevant, vals


def primes(n):
    z = []
    for p in range(3, n + 1, 2):
        if all(p % d for d in range(3, int(p**0.5) + 1, 2)):
            z.append(p)
    return z


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--u", type=int)
    ap.add_argument("--p", type=int)
    ap.add_argument("--jet", type=int, default=8)
    ap.add_argument("--random", type=int, default=0)
    ap.add_argument("--max-u", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=1729)
    args = ap.parse_args()
    jobs = []
    if args.u is not None and args.p is not None:
        jobs.append((args.u, args.p))
    rng = random.Random(args.seed)
    ps = primes(97)
    for _ in range(args.random):
        jobs.append((rng.randrange(args.max_u + 1), rng.choice(ps)))
    for u, p in jobs:
        m, first, coeffs, relevant, vals = q5_normalized_jet(u, p, args.jet)
        v0 = V(u, 0, p)
        mins = [b for b, v in enumerate(vals) if v == m]
        print({"u": u, "p": p, "m": m, "first": first,
               "order": None if first is None else m + first,
               "v0": v0, "bound": 2*v0 + 1,
               "mins": mins, "relevant": relevant, "coeffs": coeffs})


if __name__ == "__main__":
    main()


