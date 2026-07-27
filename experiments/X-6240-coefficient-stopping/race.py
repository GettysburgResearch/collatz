"""T-6245: the race between nu_L (X-6170) and Bmax(j) (T-6243).

If m is the orbit minimum of a Collatz counterexample then T^L(m) >= m for every L, so
  * for every i < chi(m) the word of m is above the line, hence  m >= nu_{chi(m)-1};
  * at i = chi(m) the word drops below, and T^{chi(m)}(m) >= m gives  m <= Bmax(chi(m)).
So  nu_{j-1} <= Bmax(j)  at j = chi(m).  Wherever  nu_{j-1} > Bmax(j),  no counterexample
minimum has chi(m) = j.

Both sides are computable: nu_L exactly by X-6170's scan, Bmax(j) exactly by T-6243(a).
"""
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

nu = {}
for line in open('experiments/X-6170-uniform-floor/results/uniform.txt'):
    if line.startswith('#'):
        continue
    p = line.split()
    nu[int(p[0])] = int(p[2])

print("# T-6245 race:  nu_{j-1}  vs  Bmax(j)")
print("# a counterexample minimum with chi(m) = j needs nu_{j-1} <= Bmax(j)")
print("%5s %14s %16s %14s %s" % ("j", "nu_{j-1}", "Bmax(j)", "ratio", "verdict"))
fails, rows = [], []
for j in range(2, 377):
    if j - 1 not in nu:
        continue
    b = bmax_exact(j)
    if b is None:
        continue
    r = nu[j - 1] / float(b)
    rows.append((j, nu[j - 1], float(b), r))
    if r <= 1:
        fails.append((j, float(b)))
    if j <= 70 or j % 25 == 0 or j > 370:
        print("%5d %14d %16.4f %14.2f %s" % (j, nu[j - 1], float(b), r,
                                             "EXCLUDED" if r > 1 else "open"))
print()
print("j where nu_{j-1} <= Bmax(j):", [j for j, _ in fails])
print("max Bmax(j) over those j    : %.4f" % max(b for _, b in fails))
print("all such j are <= %d" % max(j for j, _ in fails))
print()
print("for every j in [%d, 376] the criterion holds; ratio at j=376 is %.3e"
      % (max(j for j, _ in fails) + 1, rows[-1][3]))
