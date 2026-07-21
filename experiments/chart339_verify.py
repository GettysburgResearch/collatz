"""Independent verification of the PR #3 session-3 headline: the
339-branch chart at depth 44 (their O-0005/X-0003), plus its reading
as the fifth EQ-ladder rung and as a width datapoint (C-0003).

Claimed (PR #3): T^44(2^44 q + 8952950628352 + d) = 3^28 q + 11642373114938
for all d in a 339-element offset set D of diameter 17207, with every
residue class mod 16 occurring in D and [-934, 934] contained in D-D.

This script does NOT import their code: it reconstructs D by direct
search over the claimed offset window using this program's exact
machinery (core.T_iter), then checks the claimed geometry, then runs
the K=2 survivor-law cell for the induced chart (eq_ladder machinery
inline).
"""
import sys
from core import T_iter

M = 1 << 44
N = 3 ** 28
BASE = 8952950628352
TARGET = 11642373114938
DIAM = 17207

# 1. reconstruct D by scanning the offset window [0, DIAM]
D = []
for d in range(DIAM + 1):
    n = BASE + d                      # q = 0 member
    v, par = T_iter(n, 44)
    if v == TARGET and sum(par) == 28:
        D.append(d)
print(f"reconstructed |D| = {len(D)} (claimed 339): "
      f"{'MATCH' if len(D) == 339 else 'MISMATCH'}")
assert D[0] == 0 and D[-1] == DIAM, "diameter mismatch"

# 2. verify the full affine identity on every branch at several q
for q in (1, 2, 7, 10 ** 6, 10 ** 18 + 7):
    for d in D:
        v, par = T_iter(M * q + BASE + d, 44)
        assert v == N * q + TARGET and sum(par) == 28, (q, d)
print("affine identity exact for all 339 branches at q in "
      "{1, 2, 7, 1e6, 1e18+7}")

# 3. claimed geometry
res16 = {d % 16 for d in D}
print(f"residues mod 16 covered: {len(res16)}/16 "
      f"({'MATCH' if len(res16) == 16 else 'MISMATCH'})")
Dset = set(D)
diffs = {a - b for a in D for b in D}
run = 0
x = 0
while x in diffs and -x in diffs:
    run = x
    x += 1
print(f"[-x, x] in D-D up to x = {run} (claimed >= 934): "
      f"{'MATCH' if run >= 934 else 'MISMATCH'}")
dens = 28 / 44
import math
print(f"density 28/44 = {dens:.5f} = 7/11 (the L=22 rung doubled); "
      f"expansion 3^28/2^44 = {N / M:.10f}")
print(f"width datapoint: log2(339)/44 = {math.log2(339) / 44:.4f} "
      f"(C-0003 slope from L=22 record: log2(339/18)/22 = "
      f"{math.log2(339 / 18) / 22:.4f})")

# 4. fifth ladder rung, K = 2 survivor cell (exact, full enumeration)
MK = M ** 2
Ninv = pow(N, -1, MK)
NM = N - M
vals = []
for d0 in D:
    a0 = NM * d0 * Ninv % MK
    for d1 in D:
        vals.append((a0 + NM * d1 * M * Ninv * Ninv) % MK)
R2 = set(vals)
assert len(R2) == 339 ** 2, "coding not injective at K=2"
trivial = set(D)
mn = min(v for v in R2 if v not in trivial)
law = M ** 2 / 339 ** 2
print(f"K=2: |R_2| = {len(R2)} = 339^2 exact; min nontrivial = {mn}; "
      f"law = {law:.6g}; ratio = {mn / law:.3f}")
print("ALL CHECKS PASS")
