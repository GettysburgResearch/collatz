"""Push 2: minimal survivors of the L-atlas systems (best-first search).

Atlas dynamics at level L (a = odd count of the supercritical stratum
member r, e_r = T^L(r)):  n valid for one block iff n mod 2^L in D_L;
then n -> 3^{a_r} x + e_r.  Multi-block validity depends on n mod 2^{LK};
the coded tree:  at depth k, T^{Lk}(n) = P_k x + gamma  (P_k = product
of stratum multipliers along the path; here all strata at the tight
a_L so P_k = 3^{a_L k}), and for each target digit d' in D_L the next
base-2^L digit of n is c = (d' - gamma) * P_k^{-1} mod 2^L, with
    gamma' = M_L * (P_k c + gamma - d') / 2^L + e_{d'},   M_L = 3^{a_L}.

Best-first (heap by partial value) => first node popped at depth k IS
the minimal integer valid for k blocks.  Survivor law prediction:
min_k ~ (2^L/|D_L|)^k.

NOTE: D_L may contain residues from several strata a; multi-block
composition requires tracking each path's multiplier product P.  We
restrict to the TIGHT stratum a_L = min supercritical a (the dominant
one; at L=11 all 308 residues have a=7 anyway -- checked).
"""

import heapq
import math
from collections import defaultdict
from core import T_iter


def atlas(L):
    amin = next(a for a in range(L + 1) if 3 ** a > 2 ** L)
    buckets = defaultdict(list)
    for r in range(2 ** L):
        v, par = T_iter(r, L)
        a = sum(par)
        if a >= amin:
            buckets[(a, v)].append(r)
    D = {}
    strata = defaultdict(int)
    for (a, v), rs in buckets.items():
        if len(rs) > 1:
            for r in rs:
                D[r] = (a, v)
                strata[a] += 1
    return D, strata, amin


def best_first(L, K_target, max_pops=2_000_000):
    D, strata, amin = atlas(L)
    print(f"L={L}: |D_L| = {len(D)}, strata {dict(strata)}, tight a = {amin}")
    Dt = {r: v for r, (a, v) in D.items() if a == amin}
    M = 3 ** amin
    B = 2 ** L
    law = B / len(Dt)
    print(f"  tight-stratum digits: {len(Dt)}; law base {law:.3f} "
          f"({math.log2(law):.3f} bits/block)")
    # heap of (A, k, P, gamma)
    heap = [(0, 0, 1, 0)]
    minK = {}
    pops = 0
    while heap and pops < max_pops and len(minK) < K_target:
        A, k, P, gamma = heapq.heappop(heap)
        pops += 1
        if k > 0 and k not in minK:
            minK[k] = A
            ratio = A ** (1 / k) if A > 0 else 0
            print(f"  depth {k:2d}: min survivor = {A}"
                  f"   (per-block {ratio:.3f} vs law {law:.3f})", flush=True)
        if k >= K_target:
            continue
        Pinv = pow(P, -1, B)
        for d, e in Dt.items():
            c = (d - gamma) * Pinv % B
            A2 = A + c * B ** k
            g2 = M * (P * c + gamma - d) // B + e
            heapq.heappush(heap, (A2, k + 1, P * M, g2))
    print(f"  ({pops} pops)")
    return minK


if __name__ == "__main__":
    print("== L = 6 sanity (compare known survivor law ~ 8x per block) ==")
    best_first(6, 8)
    print("\n== L = 11 atlas ==")
    best_first(11, 10)
    print("\n== L = 19 atlas (probe) ==")
    best_first(19, 4, max_pops=1200)
