#!/usr/bin/env python3
"""
E2: synchronized finite-step merges between two 3-type families on residue classes of the exponent.

F(i) = cF*3^i + dF,  G(i) = cG*3^i + dG   (cG may carry a power of 3 = exponent shift).
After t steps T^t(F(i)) = (aF*3^i + bF)/2^t, where (aF,bF) depends only on the parity vector of
F(i), hence only on i modulo ord(3 mod 2^t) = 2^(t-2) (t>=3).  If (aF,bF) == (aG,bG) at step t then
T^t(F(i)) = T^t(G(i)) for EVERY i in that residue class: an exact certificate for the class
(checked symbolically here; the Lean file proves the ones that are used).
Conversely an identity T^a(F(i)) = T^b(G(i)) valid for infinitely many i in a class with fixed
(a,b) forces a = b and equal coefficients (compare the 3^i-coefficients and constants).
Density figures: 'exact' counts classes with modulus <= 2^K; beyond that it is a sample.
"""
import sys
from collections import defaultdict

def sieve(label, F, G, K=12, T=60):
    cF, dF = F; cG, dG = G
    M = T + 8
    MOD = 1 << M
    times = {}
    for i in range(1 << K):
        p = pow(3, i, MOD)
        x = (cF*p + dF) % MOD
        y = (cG*p + dG) % MOD
        ax, bx, ay, by = cF, dF, cG, dG
        tm = None
        for t in range(T):
            pw = 1 << t
            if x & 1:
                x = (3*x + 1) >> 1; ax *= 3; bx = 3*bx + pw
            else:
                x >>= 1
            if y & 1:
                y = (3*y + 1) >> 1; ay *= 3; by = 3*by + pw
            else:
                y >>= 1
            if ax == ay and bx == by:
                tm = t + 1
                break
        times[i] = tm
    tot = 1 << K
    merged = [i for i in range(tot) if times[i] is not None]
    exact = [i for i in merged if times[i] <= K + 2]
    classes = defaultdict(set)
    for i in merged:
        t = times[i]
        m = 1 if t <= 1 else (2 if t <= 3 else 1 << (t - 2))
        if m <= tot:
            classes[t].add((i % m, m))
    print(f"{label}: merged within {T} steps: {len(merged)}/{tot} = {len(merged)/tot:.4f}"
          f"   (exact classes, t<={K+2}: {len(exact)/tot:.4f})")
    shown = 0
    for t in sorted(classes):
        cl = sorted(classes[t])
        m = cl[0][1]
        rs = [r for r, _ in cl]
        if shown < 6:
            print(f"     t={t:<3} i mod {m}: {rs[:12]}{' ...' if len(rs) > 12 else ''}  ({len(rs)} class(es))")
            shown += 1
    return times

if __name__ == "__main__":
    print("== powers of three against powers of three ==")
    for dl in range(1, 9):
        sieve(f"3^i vs 3^(i+{dl})", (1, 0), (3**dl, 0))
    print("== repunit side (3^m - 1 = 2 R_m ~ Mersenne 2^m - 1) against ladder side (3^m + 1 = 2 L_m ~ 3^(m-1)) ==")
    sieve("3^m-1 vs 3^m+1   [R_m vs L_m]", (1, -1), (1, 1))
    for dl in range(1, 5):
        sieve(f"3^(m+{dl})-1 vs 3^m+1", (3**dl, -1), (1, 1))
        sieve(f"3^m-1 vs 3^(m+{dl})+1", (1, -1), (3**dl, 1))
    print("== repunit side against itself ==")
    for dl in range(1, 7):
        sieve(f"3^m-1 vs 3^(m+{dl})-1", (1, -1), (3**dl, -1))
    print("== other small constants ==")
    for d in (2, -2, 4, -4, 5, -5, 7, -7):
        sieve(f"3^i vs 3^i{d:+d}", (1, 0), (1, d))
        sieve(f"3^i vs 3^(i+1){d:+d}", (1, 0), (3, d))
