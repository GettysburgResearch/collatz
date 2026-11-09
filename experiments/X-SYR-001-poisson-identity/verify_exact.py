#!/usr/bin/env python3
"""Exact rational checks for research/syracuse-poisson-identity/README.md.

Standard library only.  Run:  python3 verify_exact.py
Prints a JSON summary; exits nonzero if any check fails (also under -O).

Objects.  mu = law of X = sum_{i>=1} 3^(i-1) 2^-(a_1+...+a_i) in Z_3, a_i i.i.d. with P(a) = 2^-a.
  m_n(x) = mu(x + 3^n Z_3) = P(Syrac(Z/3^n Z) = x)          (Tao's Syracuse variables)
  Q_n    = 3^n sum_x m_n(x)^2                                (normalised collision probability)
  gamma_n(j) = 3^n sum_y m_n(y) m_n(A^j y),  A(y) = 4y + 1
  (L g)(x) = 3 sum_{a>=1, 2^a x = 1 mod 3} 2^-a g((2^a x - 1)/3)   (transfer operator)

Checked exactly:
  E1  Q_(n+1) = sum_{j in Z} 4^-|j| gamma_n(j)                        for n = 0..3
  E2  sum_{j mod 3^n, 3^v | j} gamma_n(j) = 3^(n-v) Q_v               for 0 <= v <= n <= 3
  E3  <L g, L h> = sum_{j in Z} 4^-|j| <g, h o A^j> on level-k functions, k = 1, 2, 3
  E4  A is a single cycle of length 3^k on Z/3^k
  E5  the analogue for qx+1, q = 5, 7:  L*L = (q/3) sum_j 2^(-r|j|) V^j,  levels 1, 2
What this does not check: any statement about n -> infinity.
"""
from fractions import Fraction as Fr
import json
import sys


def check(cond, info=None):
    if not cond:
        raise SystemExit(f"CHECK FAILED: {info!r}")


def syracuse_level(n):
    """Exact m_n by the recursion m_k(x) = sum_{a>=1, 2^a x = 1 (3)} 2^-a m_(k-1)((2^a x - 1)/3).
    2^a mod 3^k has period P = 2*3^(k-1) in a, so the sum over a is P terms times 1/(1 - 2^-P)."""
    m = [Fr(1)]
    out = [m]
    for k in range(1, n + 1):
        M, P = 3 ** k, 2 * 3 ** (k - 1)
        geo = 1 / (1 - Fr(1, 2 ** P))
        new = [Fr(0)] * M
        for x in range(M):
            if x % 3 == 0:
                continue
            s = Fr(0)
            for a in range(1, P + 1):
                t = (pow(2, a, M) * x) % M
                if t % 3 == 1:
                    s += Fr(1, 2 ** a) * m[(t - 1) // 3]
            new[x] = s * geo
        check(sum(new) == 1, ("total mass", k))
        m = new
        out.append(m)
    return out


def poisson_weights(T):
    """w[j0] = sum over j = j0 mod T of 4^-|j|, exactly."""
    geo = 1 / (1 - Fr(1, 4 ** T))
    w = [1 + 2 * Fr(1, 4 ** T) * geo]
    for j0 in range(1, T):
        w.append((Fr(1, 4 ** j0) + Fr(1, 4 ** (T - j0))) * geo)
    return w


def general_q_identity(q, k):
    """<L_q g, L_q h> = (q/3) sum_j 2^(-r|j|) <g, h o A_q^j>, r = ord_q(2), A_q(y) = 2^r y + (2^r - 1)/q,
    checked exactly on level-k functions on Z_q.  For q = 3 this is E3."""
    r = 1
    while pow(2, r, q) != 1:
        r += 1
    M1, M0 = q ** (k + 1), q ** k
    P = 1
    while pow(2, P, M1) != 1:
        P += 1
    geo = 1 / (1 - Fr(1, 2 ** P))
    L = [[Fr(0)] * M0 for _ in range(M1)]
    for x in range(M1):
        for a in range(1, P + 1):
            t = (pow(2, a, M1) * x) % M1
            if t % q == 1:
                L[x][(t - 1) // q] += q * Fr(1, 2 ** a) * geo
    inc = (2 ** r - 1) // q
    orbit = [0]
    for _ in range(M0 - 1):
        orbit.append((2 ** r * orbit[-1] + inc) % M0)
    check(len(set(orbit)) == M0, ("single cycle", q, k))
    pos = {y: i for i, y in enumerate(orbit)}
    base = 2 ** r
    g = 1 / (1 - Fr(1, base ** M0))
    w = [1 + 2 * Fr(1, base ** M0) * g] + [(Fr(1, base ** j0) + Fr(1, base ** (M0 - j0))) * g for j0 in range(1, M0)]
    for y in range(M0):
        for y2 in range(M0):
            lhs = Fr(1, M1) * sum(L[x][y] * L[x][y2] for x in range(M1))
            rhs = Fr(q, 3) * Fr(1, M0) * w[(pos[y2] - pos[y]) % M0]
            check(lhs == rhs, ("general q", q, k, y, y2))
    return True


def main():
    N = 4
    lev = syracuse_level(N)
    Q = [3 ** n * sum(v * v for v in lev[n]) for n in range(N + 1)]
    check(Q[1] == Fr(5, 3) and Q[2] == Fr(15, 7), Q[:3])
    rep = {"Q_exact": [str(q) for q in Q], "a_exact": [str(Q[n + 1] - Q[n]) for n in range(N)]}

    gam = {}
    for n in range(0, N):
        T = 3 ** n
        m = lev[n]
        orbit = [0]
        for _ in range(T - 1):
            orbit.append((4 * orbit[-1] + 1) % T)
        check(len(set(orbit)) == T, ("E4 single cycle", n))
        pos = {y: i for i, y in enumerate(orbit)}
        g = []
        for j in range(T):
            g.append(T * sum(m[y] * m[orbit[(pos[y] + j) % T]] for y in range(T)))
        gam[n] = g
        check(g[0] == Q[n])
        w = poisson_weights(T)
        check(sum(w[j] * g[j] for j in range(T)) == Q[n + 1], ("E1", n))
        for v in range(0, n + 1):
            s = sum(g[j] for j in range(T) if j % 3 ** v == 0)
            check(s == 3 ** (n - v) * Q[v], ("E2", n, v))
    rep["E1_levels"] = list(range(0, N))
    rep["E2_checked"] = "0 <= v <= n <= %d" % (N - 1)
    rep["gamma_2"] = [str(x) for x in gam[2]]

    for k in (1, 2, 3):
        M1, M0, P = 3 ** (k + 1), 3 ** k, 2 * 3 ** k
        geo = 1 / (1 - Fr(1, 2 ** P))
        L = [[Fr(0)] * M0 for _ in range(M1)]
        for x in range(M1):
            for a in range(1, P + 1):
                t = (pow(2, a, M1) * x) % M1
                if t % 3 == 1:
                    L[x][(t - 1) // 3] += 3 * Fr(1, 2 ** a) * geo
        orbit = [0]
        for _ in range(M0 - 1):
            orbit.append((4 * orbit[-1] + 1) % M0)
        pos = {y: i for i, y in enumerate(orbit)}
        w = poisson_weights(M0)
        for y in range(M0):
            for y2 in range(M0):
                lhs = Fr(1, M1) * sum(L[x][y] * L[x][y2] for x in range(M1))
                rhs = Fr(1, M0) * w[(pos[y2] - pos[y]) % M0]
                check(lhs == rhs, ("E3", k, y, y2))
        # negative controls: a wrong affine map (4y+2, for k >= 2) and a wrong Poisson radius (1/3) must fail
        col0 = [Fr(1, M1) * sum(L[x][y] * L[x][0] for x in range(M1)) for y in range(M0)]
        if k >= 2:
            orbit2 = [0]
            for _ in range(M0 - 1):
                orbit2.append((4 * orbit2[-1] + 2) % M0)
            check(len(set(orbit2)) == M0)
            pos2 = {y: i for i, y in enumerate(orbit2)}
            check(any(col0[y] != Fr(1, M0) * w[(pos2[0] - pos2[y]) % M0] for y in range(M0)), ("control map", k))
        geo3 = 1 / (1 - Fr(1, 3 ** M0))
        w3 = [1 + 2 * Fr(1, 3 ** M0) * geo3] + [(Fr(1, 3 ** j0) + Fr(1, 3 ** (M0 - j0))) * geo3 for j0 in range(1, M0)]
        check(any(col0[y] != Fr(1, M0) * w3[(pos[0] - pos[y]) % M0] for y in range(M0)), ("control radius", k))
    rep["E3_levels"] = [1, 2, 3]
    for q, k in ((3, 2), (5, 1), (5, 2), (7, 1), (7, 2)):
        general_q_identity(q, k)
    rep["E5_general_q"] = "q = 5, 7 at levels 1, 2: L*L = (q/3) sum_j 2^(-r|j|) V^j"
    print(json.dumps(rep, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
