#!/usr/bin/env python3
"""Checks for research/syracuse-critical-cascade (floating point, tolerance 1e-9,
except S7 which is exact).  Run: python3 verify_structure.py   (about 20 s)

S1 cascade form and critical moments      S5 pair-operator identity L* C_g L
S2 singular value decomposition of L      S6 renewal remainder |rho_n(S)| <= a_n
S3 flat Jacobi kernel                     S7 no resonance away from the identity
S4 selection rule for the odometer shift
"""
import cmath, itertools, json, math, sys
from fractions import Fraction
import numpy as np

TOL, AMAX, OUT, FAIL = 1e-9, 64, {}, []
def check(name, ok, info=None):
    OUT[name] = dict(ok=bool(ok), info=info)
    print(("PASS " if ok else "FAIL ") + name + ("" if info is None else f"  {info}"))
    if not ok: FAIL.append(name)
def e(x): return cmath.exp(2j * math.pi * x)
def v3(d, cap):
    d %= 3 ** cap
    return cap if d == 0 else next(i for i in range(cap) if d % 3 ** (i + 1))

def L(g):
    """Transfer operator: level-k density (array on Z/3^k) -> level k+1."""
    M = 3 * len(g); x = np.arange(M); out = np.zeros(M, dtype=g.dtype); p = 1
    for a in range(1, AMAX + 1):
        p = p * 2 % M; t = x * p % M; idx = np.nonzero(t % 3 == 1)[0]
        out[idx] += 3.0 * 2.0 ** (-a) * g[(t[idx] - 1) // 3]
    return out
def log4_table(k):
    """h -> 4^h on Z/3^{k+1}, h mod 3^k; returns dict value -> h."""
    M, tab, v = 3 ** (k + 1), {}, 1
    for h in range(3 ** k): tab[v] = h; v = v * 4 % M
    return tab
def psi(k, s):
    """psi_eta(y) = e(eta log_4(1+3y)) on Z/3^k, eta = s/3^k."""
    tab = log4_table(k)
    return np.array([e(s * tab[(1 + 3 * y) % 3 ** (k + 1)] / 3 ** k) for y in range(3 ** k)])
def Psi(k, r):
    """Left singular vector on Z/3^{k+1}, xi = r/3^k."""
    M, tab, half = 3 ** (k + 1), log4_table(k), pow(2, -1, 3 ** k)
    P = np.zeros(M, complex)
    for x in range(M):
        if x % 3 == 1: P[x] = e(r * tab[x] / 3 ** k)
        elif x % 3 == 2: P[x] = 2 * e(-r * half / 3 ** k) * e(r * tab[(-x) % M] / 3 ** k)
    return P
def inner(u, v): return np.vdot(v, u) / len(u)          # <u, v> = mean(u conj v)

# ---- S1 ---------------------------------------------------------------------
def levels(N):
    fs = [np.ones(1)]
    for _ in range(N): fs.append(L(fs[-1]))
    return fs
def cascade_step(f, J=40):
    M = len(f); idx = np.arange(M); g = np.zeros(M); w = 0.75
    for _ in range(J):
        g += w * f[idx]; w /= 4; idx = (4 * idx + 1) % M
    t = np.arange(M); out = np.zeros(3 * M)
    out[1::3] = g[(1 + 4 * t) % M]; out[2::3] = 2 * g[(1 + 2 * t) % M]
    return out
FS = levels(11)
check("S1 cascade form f_{n+1} = c * (M f_n)(y0)", max(np.abs(cascade_step(FS[n]) - FS[n + 1]).max() for n in range(10)) < TOL)
for p in (1.0, 1.5, 2.0, 2.5):
    lhs = sum((3 * 2.0 ** -a) ** p / 3 for a in range(1, 200))
    check(f"S1 moment E sum T^p = 3^(p-1)/(2^p-1), p={p}", abs(lhs - 3 ** (p - 1) / (2 ** p - 1)) < TOL, round(lhs, 9))
MP = sum(3 * 4.0 ** -a * math.log(3 * 2.0 ** -a) for a in range(1, 200))
check("S1 tilted drift m' = log 3 - (4/3) log 2", abs(MP - (math.log(3) - 4 / 3 * math.log(2))) < TOL, round(MP, 9))

# ---- S2, S3, S4 ---------------------------------------------------------------
for k in (1, 2, 3):
    M = 3 ** (k + 1); units = [r for r in range(3 ** k) if r % 3]
    P = {r: Psi(k, r) for r in units}
    err = max(np.abs(L(psi(k, r)) - 3 * e(r / 3 ** k) / (4 - e(r / 3 ** k)) * P[r]).max() for r in units)
    check(f"S2 L psi = sigma Psi, level {k}", err < TOL, f"{err:.1e}")
    gram = np.array([[inner(P[r], P[q]) for q in units] for r in units])
    check(f"S2 Psi orthogonal, norm^2 5/3, level {k}", np.abs(gram - 5 / 3 * np.eye(len(units))).max() < TOL)
    etas = {s: psi(k + 1, s) for s in range(M)}
    ok, pattern = True, {}
    for r in units:
        for s in range(M):
            val = abs(inner(P[r], etas[s])) ** 2 * M / (5 / 3)
            want = 0.0 if s % 3 == 0 else (0.6 if (s - r) % 3 == 0 else 2.4)
            ok &= abs(val - want) < 1e-7
    check(f"S3 flat kernel: 0 (3|s), 3/5 (s=r mod 3), 12/5 (s=-r mod 3), level {k}", ok)
    A = (4 * np.arange(M) + 1) % M; Aj = np.arange(M); ok = True; mags = {}
    for j in range(1, 3 ** k + 1):
        Aj = A[Aj]; vj = v3(j, k)
        for r in units:
            for q in units:
                val = abs(inner(P[r][Aj], P[q]))
                nonzero = v3(r - q, k) == vj
                ok &= (val > 1e-6) == nonzero
                if nonzero and vj < k: mags.setdefault(vj, set()).add(round(val, 6))
    check(f"S4 selection rule <Psi_r o A^j, Psi_q> != 0 iff v3(r-q) = v3(j), level {k}", ok,
          {v: sorted(m) for v, m in mags.items()})

# ---- S5 -----------------------------------------------------------------------
rng = np.random.default_rng(1); K = 3; M3, M4 = 3 ** K, 3 ** (K + 1)
u, v = rng.standard_normal(M3), rng.standard_normal(M3); Lu, Lv = L(u), L(v)
worst = 0.0
for c, B in [(0, 0), (2, 1), (-2, 5), (1, 1), (3, 7), (-1, 4), (0, 3), (4, 22), (5, 2)]:
    lam = pow(2, c, M4); x = np.arange(M4)
    lhs = np.dot(Lu, Lv[(lam * x + B) % M4]) / M4
    rhs = 0.0
    for a in range(1, 41):
        for b in range(1, 41):
            lam2 = pow(2, c + b - a, M4); num = (lam2 + pow(2, b, M4) * B - 1) % M4
            if num % 3: continue
            y = np.arange(M3)
            rhs += 3 * 2.0 ** (-a - b) * np.dot(u, v[(lam2 * y + num // 3) % M3]) / M3
    worst = max(worst, abs(lhs - rhs))
check("S5 <Lu, (Lv) o g> = sum 3 2^-(a+b) <u, v o g'>, nine affine g", worst < TOL, f"{worst:.1e}")

# ---- S6 -----------------------------------------------------------------------
def Phi(f, S): return float(np.mean(np.minimum(f, S) ** 2))
ok, rows = True, []
for n in (6, 8, 10):
    a_n = float(np.mean(FS[n + 1] ** 2) - np.mean(FS[n] ** 2))
    rho = {S: Phi(FS[n + 1], S) - sum(3 * 4.0 ** -a * Phi(FS[n], S * 2.0 ** a / 3) for a in range(1, 80))
           for S in (0.5, 1, 2, 4, 8, 16, 64, 1e6)}
    ok &= all(abs(r) <= a_n + TOL for r in rho.values()) and abs(rho[1e6] - a_n) < 1e-6
    rows.append(dict(n=n, a_n=round(a_n, 6), rho={str(S): round(r, 5) for S, r in rho.items()}))
check("S6 |rho_n(S)| <= a_n and rho_n(S) -> a_n", ok, rows)

# ---- S7 (exact) ---------------------------------------------------------------
def phi_word(w):                      # affine map y -> s*y + t as exact (s, t)
    s, t = Fraction(1), Fraction(0)
    for a in reversed(w): s, t = 3 * s / 2 ** a, (1 + 3 * t) / Fraction(2 ** a)
    return s, t
found = 0
for l in (1, 2, 3, 4):
    maps = {}
    for w in itertools.product(range(1, 7), repeat=l): maps.setdefault(phi_word(w), []).append(w)
    found += sum(len(ws) - 1 for ws in maps.values())            # phi_w injective in w
    for (s, t) in list(maps):
        for j in (-3, -2, -1, 1, 2, 3):
            found += (s * Fraction(4) ** j, Fraction(4) ** j * t + (Fraction(4) ** j - 1) / 3) in maps
check("S7 no words w != w~ with phi_w~ = A^j phi_w (lengths <= 4, letters <= 6, |j| <= 3)", found == 0)

json.dump(OUT, open(__file__.replace("verify_structure.py", "results_structure.json"), "w"), indent=1, default=str)
print("ALL PASS" if not FAIL else f"FAILED: {FAIL}"); sys.exit(1 if FAIL else 0)
