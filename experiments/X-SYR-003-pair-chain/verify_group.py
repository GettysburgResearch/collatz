#!/usr/bin/env python3
"""Checks for research/syracuse-pair-chain (floating point, tolerance 1e-9).  About 10 s.

Q_n(lam, B) = 3^n P(X~ = lam X + B mod 3^n) on the affine group of Z/3^n.
G1 mass 1 and Q_1 = W, ||W||^2 = 11/9      G4 exact L^2 formula on the group
G2 pair recursion Q_{n+1} = T Q_n          G5 blow-up at resonant maps x -> 2^c x
G3 martingale in n                         G6 Gram matrix of the two level-1 modes
"""
import json, sys
import numpy as np
TOL, OUT, FAIL = 1e-9, {}, []
def check(name, ok, info=None):
    OUT[name] = dict(ok=bool(ok), info=info); print(("PASS " if ok else "FAIL ") + name + ("" if info is None else f"  {info}"))
    if not ok: FAIL.append(name)
def cascade(f, J=40):
    M = len(f); idx = np.arange(M); g = np.zeros(M); w = 0.75
    for _ in range(J): g += w * f[idx]; w /= 4; idx = (4 * idx + 1) % M
    t = np.arange(M); out = np.zeros(3 * M); out[1::3] = g[(1 + 4 * t) % M]; out[2::3] = 2 * g[(1 + 2 * t) % M]
    return out
FS = [np.ones(1)]
for _ in range(13): FS.append(cascade(FS[-1]))
Q = [float(np.mean(f * f)) for f in FS]; A = [Q[i + 1] - Q[i] for i in range(len(Q) - 1)]
def pair(n):
    """Q_n as dict lam -> array over B, lam a unit mod 3^n."""
    M = 3 ** n; f = FS[n]; x = np.arange(M)
    return {lam: np.array([np.dot(f, f[(lam * x + B) % M]) / M for B in range(M)]) for lam in range(M) if lam % 3}
P = {n: pair(n) for n in (1, 2, 3, 4)}

W = {(0, 0): 5/3, (0, 1): 2/3, (0, 2): 2/3, (1, 0): 4/3, (1, 1): 4/3, (1, 2): 1/3}   # (c mod 2, B mod 3)
ok = all(abs(P[1][lam][B] - W[(0 if lam == 1 else 1, B)]) < TOL for lam in (1, 2) for B in range(3))
check("G1 Q_1 = W (total branch weight)", ok)
check("G1 mass: mean of Q_n over B is 1 for every lam", max(abs(v.mean() - 1) for n in P for v in P[n].values()) < TOL)
check("G1 ||W||^2 = 11/9", abs(np.mean([np.mean(v ** 2) for v in P[1].values()]) - 11 / 9) < TOL)

def T(n):
    """Apply the pair operator to Q_n, giving a function at level n+1."""
    M, M1 = 3 ** n, 3 ** (n + 1); out = {}
    for lam in range(M1):
        if lam % 3 == 0: continue
        res = np.zeros(M1)
        for a in range(1, 46):
            for b in range(1, 46):
                lam2 = lam * pow(2, b - a, M1) % M1; pb = pow(2, b, M1); wgt = 3 * 2.0 ** (-a - b)
                num = (lam2 + pb * np.arange(M1) - 1) % M1; adm = num % 3 == 0
                res[adm] += wgt * P[n][lam2 % M][(num[adm] // 3) % M]
        out[lam] = res
    return out
for n in (1, 2):
    Tn = T(n); check(f"G2 Q_{n+1} = T Q_{n}", max(np.abs(Tn[l] - P[n + 1][l]).max() for l in Tn) < 1e-8)
for n in (1, 2, 3):
    M = 3 ** n; err = 0.0
    for lam in P[n]:
        avg = sum(P[n + 1][l].reshape(3, M).mean(axis=0) for l in (lam, lam + M, lam + 2 * M)) / 3
        err = max(err, np.abs(avg - P[n][lam]).max())
    check(f"G3 martingale: level-{n} average of Q_{n+1} is Q_{n}", err < TOL)
def formula(n): return sum((2 * Q[v] - A[v]) ** 2 / (6 * 3 ** v) for v in range(n)) + Q[n] ** 2 / 3 ** n
for n in (1, 2, 3, 4):
    brute = float(np.mean([np.mean(v ** 2) for v in P[n].values()]))
    check(f"G4 ||Q_{n}||^2 = sum (2Q_v - a_v)^2/(6 3^v) + Q_n^2/3^n", abs(brute - formula(n)) < TOL, round(brute, 10))
OUT["limit ||Q||^2"] = formula(13) - Q[13] ** 2 / 3 ** 13; print("     limit ||Q||^2 =", round(OUT["limit ||Q||^2"], 6))
ok, rows = True, []
for c in (1, -1, 2, -2, 3):
    for m in (2, 4, 6, 8):
        M = 3 ** (m + 1); f = FS[m + 1]; x = np.arange(M); val = float(np.dot(f, f[pow(2, c, M) * x % M]) / M)
        ok &= val >= 2.0 ** (-abs(c)) * Q[m] - TOL; rows.append((c, m, round(val, 4), round(2.0 ** (-abs(c)) * Q[m], 4)))
check("G5 Q_{m+1}(x -> 2^c x) >= 2^-|c| Q_m (resonant points blow up)", ok, rows[-4:])
d, u, gram = np.array([-1., 0., 1.]) / np.sqrt(2 / 3), np.array([1., -2., 1.]) / np.sqrt(2), []
for n in range(1, 15):
    d, u = cascade(d), cascade(u); gram.append((n, float(np.mean(d * d)), float(np.mean(u * u)), float(np.mean(d * u))))
OUT["G6 gram"] = gram
for r in gram[-3:]: print("     n=%d  |L^n d|^2=%.6f  |L^n u|^2=%.6f  <L^n d, L^n u>=%.6f" % r)
inc = [gram[i + 1][2] - gram[i][2] for i in range(10, 13)]
check("G6 companion mode converges, increment ratio near 3/4", 0.70 < inc[2] / inc[1] < 0.80, round(inc[2] / inc[1], 3))
json.dump(OUT, open(__file__.replace("verify_group.py", "results_group.json"), "w"), indent=1, default=str)
print("ALL PASS" if not FAIL else f"FAILED: {FAIL}"); sys.exit(1 if FAIL else 0)
