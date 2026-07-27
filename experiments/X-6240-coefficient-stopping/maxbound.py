"""Is there an ABSOLUTE bound on a counterexample to chi = sigma?

A counterexample has n <= c_w/D at j = chi(n), with D = 2^j - 3^{k_j}.
If max over qualifying words of c_w/D is bounded by C for every j, then EVERY counterexample
satisfies n <= C -- and a finite check settles the question.

max c_w is computed by the same DP with max in place of sum.
"""
import math
from math import ceil
from fractions import Fraction

ALPHA = math.log(2)/math.log(3)


def maxratio(J):
    out = []
    for j in range(2, J+1):
        M = {0: 0}                       # k -> max c so far, over above-line prefixes
        for t in range(j):
            M2 = {}
            for k, c in M.items():
                if M2.get(k, -1) < c:
                    M2[k] = c                      # 0-step
                v = 3*c + (1 << t)
                if M2.get(k+1, -1) < v:
                    M2[k+1] = v                    # 1-step
            if t+1 < j:
                need = ceil(ALPHA*(t+1) - 1e-12)
                M2 = {k: v for k, v in M2.items() if k >= need}
            M = M2
        needj = ceil(ALPHA*j - 1e-12)
        best = Fraction(0)
        bk = None
        for k, c in M.items():
            if k >= needj:
                continue
            D = (1 << j) - 3**k
            if D <= 0:
                continue
            r = Fraction(c, D)
            if r > best:
                best, bk = r, k
        out.append((j, best, bk))
    return out


rows = maxratio(70)
print(f"{'j':>4} {'k':>5} {'max c_w/D  = bound on n':>26}")
run = Fraction(0)
for j, b, k in rows:
    if b > run:
        run = b
        print(f"{j:>4} {str(k):>5} {float(b):>26.4f}   <-- new record")
    elif j % 10 == 0:
        print(f"{j:>4} {str(k):>5} {float(b):>26.4f}")
print(f"\nMAXIMUM over all j <= 70 of the bound on n : {float(run):.6f}  (exactly {run})")
print("\nIf this stays bounded, every counterexample to chi = sigma has n below it, and the")
print("question reduces to a FINITE check.")
