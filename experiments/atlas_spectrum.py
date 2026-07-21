"""Pushes 1+3: the atlas spectrum to L=30 and the entropy-model test.

Atlas: D_L = { r mod 2^L : exists s != r, a_s = a_r, T^L(s) = T^L(r) },
restricted to supercritical strata 3^{a_r} > 2^L.  (Collision identity:
T^L(2^L q + r) = 3^{a_r} q + T^L(r).)

ENTROPY MODEL (push 3).  Stratum a has C(L,a) residues (Terras) whose
T^L-values live in [0, ~3^a).  If values were uniform (birthday model),
expected residues-in-collision per stratum ~ C(L,a)^2/3^a (when << C).
Dominant stratum is the tightest supercritical one, giving

    gamma_inf = 2 H(log_3 2) - 1  ~  0.8996  < 1,
    per-step cost  ->  1 - gamma_inf ~ 0.1004 bits/step,

i.e. cost per block GROWS ~ 0.1004 L + O(log L): the atlas hierarchy has
a ceiling strictly below 1 and never becomes cost-free.  This file
computes exact |D_L| (numpy, chunked) for L <= 26, class-sampled
estimates for L = 28, 30, and the model prediction
   E|D_L| = sum_a C * (1 - (1 - 1/3^a)^(C-1))   (a supercritical)
for comparison.
"""

import numpy as np
import math
from math import comb

CHUNK = 1 << 22


def stats_for_L(L, keep_mod=None, keep_classes=None):
    """Return sorted array of keys (v*(L+1)+a) for all r < 2^L with
    supercritical a, optionally filtered to v % keep_mod in keep_classes."""
    keys = []
    amin = next(a for a in range(L + 1) if 3 ** a > 2 ** L)
    for start in range(0, 1 << L, CHUNK):
        n = min(CHUNK, (1 << L) - start)
        v = np.arange(start, start + n, dtype=np.int64)
        a = np.zeros(n, dtype=np.int64)
        for _ in range(L):
            odd = (v & 1).astype(bool)
            v = np.where(odd, (3 * v + 1) >> 1, v >> 1)
            a += odd
        mask = a >= amin
        v, a = v[mask], a[mask]
        if keep_mod is not None:
            m2 = np.isin(v % keep_mod, keep_classes)
            v, a = v[m2], a[m2]
        keys.append(v * (L + 1) + a)
    keys = np.concatenate(keys)
    keys.sort(kind="stable")
    return keys


def collision_count(keys):
    """number of elements participating in a key appearing >= 2 times."""
    if len(keys) == 0:
        return 0
    # boundaries of equal runs
    diff = np.diff(keys)
    run_starts = np.concatenate(([0], np.nonzero(diff)[0] + 1))
    run_lens = np.diff(np.concatenate((run_starts, [len(keys)])))
    return int(run_lens[run_lens >= 2].sum())


def model_D(L):
    tot = 0.0
    for a in range(L + 1):
        if 3 ** a <= 2 ** L:
            continue
        C = comb(L, a)
        p = 1.0 - (1.0 - 1.0 / 3 ** a) ** (C - 1)
        tot += C * p
    return tot


def main():
    H = lambda x: -x * math.log2(x) - (1 - x) * math.log2(1 - x)
    l32 = math.log(2) / math.log(3)
    print(f"entropy model: gamma_inf = 2H(log_3 2) - 1 = "
          f"{2 * H(l32) - l32 * math.log2(3):.5f}; slope "
          f"{1 - (2 * H(l32) - 1):.5f} bits/step\n")
    print(" L    |D_L|      gamma_L   cost    model|D|   model_cost")
    for L in range(16, 27):
        keys = stats_for_L(L)
        D = collision_count(keys)
        del keys
        g = math.log2(D) / L
        mD = model_D(L)
        mg = math.log2(mD) / L
        print(f"{L:2d}  {D:9d}   {g:.4f}   {(1-g)*L:5.2f}   {mD:9.0f}"
              f"   {(1-mg)*L:5.2f}", flush=True)
    # sampled larger L: keep v in a few classes mod 64; collisions require
    # equal v so classes are closed: per-class counts exact, estimate =
    # (sum over kept classes)/(fraction kept) -- unbiased.
    for L, kmod, kcls in ((28, 64, (0, 1, 2, 3, 4, 5, 6, 7)),
                          (30, 64, (0, 1, 2, 3))):
        keys = stats_for_L(L, kmod, kcls)
        D_part = collision_count(keys)
        del keys
        frac = len(kcls) / kmod
        D_est = D_part / frac
        g = math.log2(D_est) / L
        mD = model_D(L)
        mg = math.log2(mD) / L
        print(f"{L:2d}  ~{D_est:8.0f}   {g:.4f}   {(1-g)*L:5.2f}   {mD:9.0f}"
              f"   {(1-mg)*L:5.2f}   (sampled {frac:.3f} of classes,"
              f" part={D_part})", flush=True)


if __name__ == "__main__":
    main()
