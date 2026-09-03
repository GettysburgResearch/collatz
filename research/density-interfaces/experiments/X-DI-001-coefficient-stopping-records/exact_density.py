#!/usr/bin/env python3
"""Exact natural density of the all-supercritical depth-N survivor set S_N.

Repository notation (IC-SC-001): for the shortcut map T, q_k(n) = number of odd
steps among the first k, C_k(n) = 3^{q_k}/2^k, and
    S_N = { n >= 1 : C_k(n) >= 1 for all 1 <= k <= N }.
Every length-N parity word occupies exactly one residue class modulo 2^N, so
    dens(S_N) = W_N / 2^N,
where W_N counts binary words v_0..v_{N-1} whose prefix weights satisfy
3^{q_k} >= 2^k for k = 1..N.  The comparison is made exact through bit lengths:
3^q >= 2^k  <=>  k <= bitlen(3^q) - 1.
This is an exact computation, not a sampled experiment.  It measures density,
which the repository firewall distinguishes from the least source m_N.
"""
import sys
from fractions import Fraction
from math import log2

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400
bl = [ (3**q).bit_length() for q in range(NMAX + 2) ]

def ok(k, q):
    return k <= bl[q] - 1          # 3^q >= 2^k

# dp[q] = number of admissible words of the current length with weight q
dp = {0: 1}
print("# N  W_N  dens(S_N)=W_N/2^N  log2(dens)/N")
for k in range(1, NMAX + 1):
    nd = {}
    for q, c in dp.items():
        for bit in (0, 1):
            q2 = q + bit
            if ok(k, q2):
                nd[q2] = nd.get(q2, 0) + c
    dp = nd
    W = sum(dp.values())
    dens = Fraction(W, 2**k)
    if k <= 40 or k % 20 == 0:
        print(k, W, f"{float(dens):.6e}", f"{(log2(W) - k)/k:+.4f}")
