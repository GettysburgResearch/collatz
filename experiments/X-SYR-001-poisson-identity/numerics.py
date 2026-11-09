#!/usr/bin/env python3
"""Floating-point numerics for research/syracuse-poisson-identity/README.md.  Needs numpy.

Run:  python3 numerics.py [N]      (default N = 13, a few seconds; N = 17 needs ~6 GB and ~10 minutes)
Everything here is EMPIRICAL evidence at finite level, in binary64 with the sum over a truncated at a <= 66.
"""
import json
import math
import sys
import time
import numpy as np

AMAX = 66


def levels(N):
    m = np.array([1.0])
    out = [m]
    for n in range(1, N + 1):
        M = 3 ** n
        x = np.arange(M, dtype=np.int64)
        new = np.zeros(M)
        p = 1
        for a in range(1, AMAX + 1):
            p = (p * 2) % M
            t = x * p
            t %= M
            idx = np.nonzero(t % 3 == 1)[0]
            new[idx] += 2.0 ** (-a) * m[(t[idx] - 1) // 3]
        m = new
        out.append(m)
    return out


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 13
    t0 = time.time()
    L = levels(N)
    rep = {"N": N, "table": []}
    Q = [3 ** n * float(L[n] @ L[n]) for n in range(N + 1)]
    for n in range(1, N + 1):
        M = 3 ** n
        m = L[n]
        y = np.arange(M, dtype=np.int64)
        R = []
        for _ in range(6):
            y = (4 * y + 1) % M
            R.append(M * float(m @ m[y]))
        units = np.arange(M) % 3 != 0
        rep["table"].append({"n": n, "Q_n": Q[n], "a_(n-1)": Q[n] - Q[n - 1], "gamma_n(1..6)": R,
                             "min_density_units": float(M * m[units].min()), "max_density": float(M * m.max())})

    # singular values of the transfer operator, level k -> k+1, against sqrt(15/(17 - 8 cos))
    sv = {}
    for k in (2, 3, 4):
        M1, M0 = 3 ** (k + 1), 3 ** k
        T = np.zeros((M1, M0))
        for x in range(M1):
            for a in range(1, 80):
                t = (pow(2, a, M1) * x) % M1
                if t % 3 == 1:
                    T[x, (t - 1) // 3] += 3 * 2.0 ** (-a)
        T /= math.sqrt(3)
        s = np.sort(np.linalg.svd(T, compute_uv=False))
        pred = np.sort(np.sqrt(15 / (17 - 8 * np.cos(2 * np.pi * np.arange(M0) / M0))))
        sv[k] = {"max_abs_error": float(np.abs(s - pred).max()), "largest": float(s[-1]), "smallest": float(s[0])}
        # the operator in the two multiplicative-character bases psi_xi(y) = e(xi log_4(1+3y))
        def basis(K):
            MK, mod = 3 ** K, 3 ** (K + 1)
            lg, u = {}, 1
            for h in range(MK):
                lg[u] = h
                u = (u * 4) % mod
            h = np.array([lg[(1 + 3 * yy) % mod] for yy in range(MK)])
            return np.exp(2j * np.pi * np.outer(h, np.arange(MK)) / MK) / math.sqrt(MK)
        Kmat = basis(k + 1).conj().T @ T @ basis(k)
        col = np.sum(np.abs(Kmat) ** 2, axis=0)
        prim = [mm for mm in range(M0) if mm % 3]
        vals = sorted(set(np.round(np.abs(Kmat[:, prim]) ** 2 / col[prim] * M1, 6).ravel().tolist()))
        gram = Kmat.conj().T @ Kmat
        sv[k]["characters_are_singular_vectors_offdiag_max"] = float(np.abs(gram - np.diag(np.diag(gram))).max())
        sv[k]["distinct_values_of_3^(k+1)|K|^2/colnorm^2"] = vals
    rep["singular_values"] = sv

    # Plancherel: a_(n-1) = sum over additive frequencies of exact level n of |mu^(zeta)|^2
    pl = {}
    for n in (3, 5, 7):
        phi = np.fft.fft(L[n])
        ex = np.arange(3 ** n) % 3 != 0
        pl[n] = {"sum_exact_level": float(np.sum(np.abs(phi[ex]) ** 2)), "Q_n-Q_(n-1)": Q[n] - Q[n - 1]}
    rep["plancherel"] = pl

    # L1 oscillation ||f_N - f_m||_1 and tails of f_N
    top = L[N]
    osc = [float(np.abs(top - np.tile(L[mm], 3 ** (N - mm)) / 3 ** (N - mm)).sum()) for mm in range(N)]
    rep["L1_oscillation_m_to_N"] = osc
    f = 3 ** N * top
    units = np.arange(3 ** N) % 3 != 0
    rep["upper_tail_t2_times_Haar(f>t)"] = {str(t): float(t * t * np.mean(f > t)) for t in (2, 3, 4, 6, 8, 12, 16, 24, 32)}
    rep["lower_tail_fraction_of_units_with_f<=eps"] = {str(e): float(np.mean(f[units] <= e)) for e in (0.5, 0.3, 0.2, 0.1, 0.08, 0.06)}
    rep["p_norms_of_f_N"] = {str(p): float(np.mean(f ** p) ** (1 / p)) for p in (1.25, 1.5, 1.75)}
    rep["seconds"] = round(time.time() - t0, 1)
    print(json.dumps(rep, indent=1))


if __name__ == "__main__":
    main()
