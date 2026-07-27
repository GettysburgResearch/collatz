"""T-6245's race, extended: merge chiscan shards, rebuild nu_L, and rerun nu_{j-1} vs Bmax(j).

chiscan emits, per shard, the least n in that shard with chi(n) = c, for each c.  The shards
partition the range, so the merge is a pointwise minimum.  Then

        nu_L = min{ n >= 2 : chi(n) > L } = min{ arr[c] : c > L },

valid for every L strictly below the largest chi seen (below that, some scanned n witnesses it;
at or above it, the scan range may simply not reach far enough).
"""
import glob
import sys
from fractions import Fraction


def bmax_exact(J):
    """exact Bmax(J) = (sum_{m<k} 3^(k-1-m) 2^(a_m)) / (2^J - 3^k), k = floor(J log2/log3)"""
    p2 = 1 << J
    k, p3 = 0, 1
    while p3 * 3 < p2:
        p3 *= 3; k += 1
    if not (p3 < p2 < p3 * 3):
        return None
    N, pw2, a, q = 0, 1, 0, 1
    for m in range(k):
        while pw2 * 2 <= q:
            pw2 *= 2; a += 1
        N = 3 * N + pw2
        q *= 3
    return Fraction(N, p2 - p3)


arr, hi = {}, 0
for f in sorted(glob.glob(sys.argv[1] if len(sys.argv) > 1
                          else '../X-6170-uniform-floor/results/chiscan-s*.txt')):
    for line in open(f):
        if line.startswith('#'):
            assert 'skip_big = 0 ; skip_len = 0' in line, "UNDECIDED n IN " + f + ": " + line
            hi = max(hi, int(line.split('[')[1].split(']')[0].split(', ')[1]))
            continue
        c, n = line.split()
        c, n = int(c), int(n)
        if c not in arr or n < arr[c]:
            arr[c] = n

M = max(arr)
suf, best = {}, None
for c in range(M, 0, -1):
    if c in arr:
        best = arr[c] if best is None else min(best, arr[c])
    suf[c] = best
nu = {L: suf[L + 1] for L in range(1, M) if suf.get(L + 1) is not None}

print("# scanned [2, %d]; largest chi seen = %d; nu_L valid for L <= %d" % (hi, M, M - 1))
print("# X-6170 previously reached L = 375 (nu_375 = 63728127)")
print()
print("%6s %16s %14s %14s" % ("j", "nu_{j-1}", "Bmax(j)", "ratio"))
fails, last = [], None
for j in range(2, M + 1):
    if j - 1 not in nu:
        continue
    b = bmax_exact(j)
    if b is None:
        continue
    r = nu[j - 1] / float(b)
    if r <= 1:
        fails.append((j, float(b)))
    if j % 50 == 0 or j > M - 3 or j in (376, 377):
        print("%6d %16d %14.4f %14.3e" % (j, nu[j - 1], float(b), r))
    last = (j, r)
print()
print("j where nu_{j-1} <= Bmax(j) :", [j for j, _ in fails])
if fails:
    print("largest such j = %d, and Bmax there = %.4f" % (max(j for j, _ in fails),
                                                          max(b for _, b in fails)))
print("criterion holds for every j in [%d, %d]; ratio at j = %d is %.3e"
      % ((max(j for j, _ in fails) + 1) if fails else 2, last[0], last[0], last[1]))
print()
ls = sorted(nu)
print("nu_L growth: log2(nu_L)/L at L = %d is %.6f ; at L = %d is %.6f"
      % (375, __import__('math').log2(nu[375]) / 375,
         ls[-1], __import__('math').log2(nu[ls[-1]]) / ls[-1]))
