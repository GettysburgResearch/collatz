"""P8 (issue #4): supercritical collision-fiber widths via the exact
coalescence recursion, computed independently and extended past L=22.

Recursion (independent reimplementation of the PR #3 L-0003 statement,
derived directly from the collision identity T^L(2^L q + r) =
3^{a_r} q + T^L(r)):

    a_{L+1}(2k)   = a_L(k),           s_{L+1}(2k)   = s_L(k)
    a_{L+1}(2k+1) = 1 + a_L(u),       s_{L+1}(2k+1) = 3^{a_L(u)} q + s_L(u)
                    where 3k+2 = 2^L q + u.

Fibers at level L = level sets of (a_L, s_L); supercritical strata
3^a > 2^L. Outputs per level: supercritical residue count, |D_L|
(residues in fibers of size >= 2 -- cross-checks atlas_spectrum.py by a
different algorithm), max fiber width, and the top of the width
histogram. PR #3's X-0002 reports max widths 2,3,4,5,8,12,18 at
L=6..22; this run re-derives those and extends to L=26.

Exact integer arithmetic throughout (int64 safe: s < 3^{a}*3 and keys
s*32+a < 2^63 for L <= 26).
"""
import numpy as np

LMAX = 26

a = np.array([0, 1], dtype=np.int8)          # level 1
s = np.array([0, 2], dtype=np.int64)         # T(0)=0, T(1)=2

print(" L  supercrit    |D_L|   maxw  width histogram (w:count, w>=2 top 6)",
      flush=True)

for L in range(1, LMAX + 1):
    if L >= 6:
        # supercritical strata at this level
        amin = next(x for x in range(L + 1) if 3 ** x > 2 ** L)
        sup = a >= amin
        nsup = int(sup.sum())
        keys = s[sup] * 32 + a[sup]
        _, inv, cnt = np.unique(keys, return_inverse=True,
                                return_counts=True)
        widths = cnt
        in_collision = int((widths[inv] >= 2).sum())
        maxw = int(widths.max()) if len(widths) else 0
        hist = np.bincount(widths)
        top = [(w, int(hist[w])) for w in range(len(hist) - 1, 1, -1)
               if hist[w]][:6]
        print(f"{L:3d} {nsup:10d} {in_collision:8d} {maxw:6d}  {top}",
              flush=True)
        del keys, inv, cnt, widths, hist
    if L == LMAX:
        break
    # build level L+1
    n = 1 << L
    k = np.arange(n, dtype=np.int64)
    m = 3 * k + 2
    q = m >> L
    u = m & (n - 1)
    a2 = np.empty(2 * n, dtype=np.int8)
    s2 = np.empty(2 * n, dtype=np.int64)
    a2[0::2] = a
    s2[0::2] = s
    au = a[u]
    a2[1::2] = au + 1
    s2[1::2] = (3 ** au.astype(np.int64)) * q + s[u]
    del k, m, q, u, au
    a, s = a2, s2

print("done", flush=True)
