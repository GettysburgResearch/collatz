#!/usr/bin/env python3
"""Syracuse level densities by the cascade recursion (cost about 30 * 3^n per level).

    f_{n+1}(x) = c(x) * (M f_n)(y0(x)),   M = (3/4) sum_{i>=0} 4^-i f(A^i y),  A y = 4y + 1,
    c = 1, y0 = (4x-1)/3 on x = 1 mod 3;  c = 2, y0 = (2x-1)/3 on x = 2 mod 3;  f = 0 on 3 | x.

Usage: python3 fast_levels.py N [out.json]     (N = 18 needs about 9 GB and 5 minutes)
Per level: Q_n = ||f_n||^2, gamma_n(j) = <f_n, f_n o A^j> for j = 1, 2, also truncated at S,
tails t^2 m{f_n > t}, truncated second moments Phi_n(S) = ||min(f_n, S)||^2, max and unit minimum.
"""
import json, sys, time
import numpy as np

N = int(sys.argv[1]); OUT = sys.argv[2] if len(sys.argv) > 2 else None
J, CH = 30, 3 ** 14
TS = [1.5, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48]
SS = [2, 4, 8, 16, 32, 64, 128]

def stats(f, n):
    M = len(f); q = 0.0; mx = 0.0; mn = np.inf
    tail = np.zeros(len(TS)); phi = np.zeros(len(SS))
    g = np.zeros((2, len(SS) + 1))                      # gamma(1), gamma(2); last column untruncated
    for lo in range(0, M, CH):
        x = np.arange(lo, min(lo + CH, M), dtype=np.int64); fx = f[x]
        a1 = (4 * x + 1) % M; f1 = f[a1]; f2 = f[(4 * a1 + 1) % M]
        q += float(np.dot(fx, fx)); mx = max(mx, float(fx.max()))
        u = fx[x % 3 != 0]
        if u.size: mn = min(mn, float(u.min()))
        for i, t in enumerate(TS): tail[i] += np.count_nonzero(fx > t)
        for i, S in enumerate(SS):
            h = np.minimum(fx, S); phi[i] += float(np.dot(h, h))
            g[0, i] += float(np.dot(h, np.minimum(f1, S))); g[1, i] += float(np.dot(h, np.minimum(f2, S)))
        g[0, -1] += float(np.dot(fx, f1)); g[1, -1] += float(np.dot(fx, f2))
    return dict(n=n, Q=q / M, gamma1=g[0, -1] / M, gamma2=g[1, -1] / M, max=mx, min_units=mn,
                tail=[t * t * c / M for t, c in zip(TS, tail)], Phi=list(phi / M),
                gamma1_trunc=list(g[0, :-1] / M), gamma2_trunc=list(g[1, :-1] / M))

f = np.ones(1); rows = []; t0 = time.time()
for n in range(N):
    M = 3 ** n
    idx = np.arange(M, dtype=np.int64); g = np.zeros(M); w = 0.75
    for _ in range(J):
        g += w * f[idx]; w /= 4
        idx *= 4; idx += 1; idx %= M
    del idx
    t = np.arange(M, dtype=np.int64); fn = np.zeros(3 * M)
    fn[1::3] = g[(1 + 4 * t) % M]; fn[2::3] = 2 * g[(1 + 2 * t) % M]
    del t, g; f = fn
    row = stats(f, n + 1); row["seconds"] = round(time.time() - t0, 1); rows.append(row)
    print(n + 1, f"Q={row['Q']:.6f} gamma1={row['gamma1']:.6f} gamma2={row['gamma2']:.6f} "
                 f"max={row['max']:.2f} min={row['min_units']:.5f} t={row['seconds']}", flush=True)
if OUT: json.dump(dict(TS=TS, SS=SS, rows=rows), open(OUT, "w"), indent=0)
