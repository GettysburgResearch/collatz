#!/usr/bin/env python3
"""Syracuse level densities at integer points versus true Collatz hitting fractions.

Exact identity (checked in part 1):  f_n(x) = 3^n mu_n(x mod 3^n) = sum over y with Syr^n(y) = x of 3^n / 2^s(y),
where s(y) is the number of halvings on the way from y to x, and 3^n/2^s = (x - F)/y with 0 < F < x.
Renewal heuristic (tested in part 2):  fraction of odd N whose orbit passes through x
                                        ~  2 h(x) / (x log(4/3)),  h(x) = lim_n x * sum_{Syr^n(y) = x} 1/y.
Usage: python3 hitting.py [X]      (default X = 2000000; about 1 minute)
"""
import json, math, sys
import numpy as np
X = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
TARGETS = [5, 7, 11, 13, 17, 19, 23, 25, 29, 35, 53, 85, 341, 3077]
LOG43 = math.log(4 / 3)

def cascade(f, J=30):
    M = len(f); idx = np.arange(M, dtype=np.int64); g = np.zeros(M); w = 0.75
    for _ in range(J): g += w * f[idx]; w /= 4; idx = (4 * idx + 1) % M
    t = np.arange(M, dtype=np.int64); out = np.zeros(3 * M); out[1::3] = g[(1 + 4 * t) % M]; out[2::3] = 2 * g[(1 + 2 * t) % M]
    return out
def syr(y):
    y = 3 * y + 1; s = 0
    while y % 2 == 0: y //= 2; s += 1
    return y, s

# ---- part 1: exact identity at small depth, by brute-force enumeration of predecessors -------------
def predecessors(x, depth, amax=40):
    """All (y, s) with Syr^depth(y) = x, exponents truncated at amax per step."""
    level = [(x, 0)]
    for _ in range(depth):
        nxt = []
        for y, s in level:
            for a in range(1, amax + 1):
                if (2 ** a * y - 1) % 3 == 0: nxt.append(((2 ** a * y - 1) // 3, s + a))
        level = nxt
    return level
f = np.ones(1); F = {}
for n in range(1, 16):
    f = cascade(f); F[n] = f
ident = []
for x in (5, 23, 29):
    for n in (1, 2, 3):
        pre = predecessors(x, n)
        ident.append(dict(x=x, n=n, f_n=float(F[n][x % 3 ** n]), weighted=sum(3.0 ** n / 2.0 ** s for _, s in pre),
                          harmonic=float(x * sum(1.0 / y for y, _ in pre)), all_positive=all(y > 0 for y, _ in pre)))
ok_ident = all(abs(r["f_n"] - r["weighted"]) < 1e-6 and r["all_positive"] and r["harmonic"] >= r["weighted"] for r in ident)

# ---- part 2: true hitting fractions and generations ---------------------------------------------------
tg = {x: i for i, x in enumerate(TARGETS)}
mask = np.zeros(X + 1, dtype=np.int64); gen23 = np.full(X + 1, -1, dtype=np.int32); gen23[23] = 0
for N in range(1, X + 1, 2):
    m = (1 << tg[N]) if N in tg else 0; y = N; k = 0; g = -1
    while y != 1:
        y, _ = syr(y); k += 1
        if y in tg: m |= 1 << tg[y]
        if y == 23 and g < 0: g = k
        if y < N:
            m |= int(mask[y])
            if g < 0 and gen23[y] >= 0: g = k + int(gen23[y])
            break
    mask[N] = m
    if N != 23: gen23[N] = g
odd = np.arange(1, X + 1, 2)
rows = []
for x in TARGETS:
    hit = float(np.mean((mask[1::2] >> tg[x]) & 1)); f15 = float(F[15][x]); pred = 2 * f15 / (x * LOG43)
    rows.append(dict(x=x, hit_fraction=hit, f_11_to_15=[round(float(F[n][x % 3 ** n]), 4) for n in range(11, 16)],
                     prediction_from_f15=pred, ratio=hit / pred))
g = gen23[1::2]
gens = [dict(generation=n, count=int((g == n).sum()), harmonic_times_23=float(23 * (1.0 / odd[g == n]).sum()))
        for n in (1, 2, 3, 5, 8, 12, 16, 20, 25, 30, 34, 35, 36, 37, 40, 45, 50)]
small = [dict(y=int(y), generation=int(gen23[y])) for y in (27, 31, 41, 47, 71, 107) if gen23[y] >= 0]
out = dict(X=X, identity_ok=ok_ident, identity=ident, targets=rows, tree_of_23=gens, small_members_of_tree_of_23=small)
json.dump(out, open(__file__.replace("hitting.py", "results_hitting.json"), "w"), indent=1)
print("identity f_n(x) = sum 3^n/2^s over n-th predecessors:", "PASS" if ok_ident else "FAIL")
print("   x   hit      f_15    2f_15/(x log 4/3)  ratio")
for r in rows: print("%5d  %.4f  %.4f   %.4f            %.2f" % (r["x"], r["hit_fraction"], r["f_11_to_15"][-1], r["prediction_from_f15"], r["ratio"]))
print("tree of 23: generation, count <= X, 23 * harmonic sum (truncated at X)")
for r in gens: print("  %3d %7d  %.4f" % (r["generation"], r["count"], r["harmonic_times_23"]))
print("small members:", small)
sys.exit(0 if ok_ident else 1)
