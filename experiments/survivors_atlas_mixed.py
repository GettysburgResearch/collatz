"""Mixed-strata best-first survivor search (full D_L, per-path multipliers)."""
import heapq, math
from survivors_atlas import atlas

def best_first_mixed(L, K_target, max_pops=3_000_000):
    D, strata, amin = atlas(L)
    B = 2 ** L
    law = B / len(D)
    print(f"L={L}: |D_L|={len(D)} strata {dict(strata)}; mixed law base "
          f"{law:.3f} ({math.log2(law):.3f} bits/block)", flush=True)
    heap = [(0, 0, 1, 0)]
    minK = {}
    pops = 0
    while heap and pops < max_pops and len(minK) < K_target:
        A, k, P, gamma = heapq.heappop(heap)
        pops += 1
        if k > 0 and k not in minK:
            minK[k] = A
            print(f"  depth {k:2d}: min = {A}  per-block "
                  f"{A ** (1/k):.3f} vs law {law:.3f}", flush=True)
        if k >= K_target:
            continue
        Pinv = pow(P, -1, B)
        for d, (a, e) in D.items():
            c = (d - gamma) * Pinv % B
            heapq.heappush(heap, (A + c * B ** k, k + 1,
                                  P * 3 ** a,
                                  3 ** a * (P * c + gamma - d) // B + e))
    print(f"  ({pops} pops)", flush=True)

best_first_mixed(11, 12)
