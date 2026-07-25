"""The real reason the escape model fails.

The model assumed the number of rare steps b along a depth-d path is Binomial(d, 1/4)
(that is what C(d,b)3^(-b) normalised by (4/3)^d says).  But the rare branch is available iff
n = 2 mod 3, and under doubling the residue ALTERNATES 1 -> 2 -> 1 -> ..., so along a doubling
chain the rare branch is available at every OTHER level, not at a random 1/3 of them, while a
residue-0 chain never has it.  The steps are strongly correlated.

This measures the true distribution of b and compares it with the model's.
"""
from collections import Counter
from math import comb

DEPTH = 34


def kids(n):
    out = [(2*n, 0)]
    if n % 3 == 2:
        out.append(((2*n - 1)//3, 1))
    return out


level = [(1, 0)]
for d in range(DEPTH):
    level = [(m, b+t) for n, b in level for m, t in kids(n)]
N = len(level)
obs = Counter(b for _, b in level)
print(f"depth {DEPTH}: {N:,} paths  (model predicts (4/3)^{DEPTH} = {(4/3)**DEPTH:,.0f})\n")
print(f"{'b':>4} {'observed':>12} {'frac':>9} {'Binom(d,1/4)':>14} {'obs/model':>10}")
mean_o = sum(b*c for b, c in obs.items())/N
for b in range(0, DEPTH+1):
    o = obs.get(b, 0)
    m = comb(DEPTH, b)*(0.25**b)*(0.75**(DEPTH-b))
    if o or m > 1e-4:
        print(f"{b:>4} {o:>12,} {o/N:>9.5f} {m:>14.5f} {(o/N)/m if m else 0:>10.3f}")
print(f"\nmean b: observed {mean_o:.4f},  model d/4 = {DEPTH/4:.4f}")
var_o = sum((b-mean_o)**2*c for b, c in obs.items())/N
print(f"var  b: observed {var_o:.4f},  model d*3/16 = {DEPTH*3/16:.4f}")
print(f"\nmax b observed {max(obs)} (model allows {DEPTH})")
print("""
The mean matches -- it must, since the branching factor is 4/3 either way -- but the SHAPE
does not: the true distribution is narrower and truncated, because rare steps cannot occur on
consecutive levels along a doubling chain (the residue must return to 2 mod 3 first).  The
escape model integrates over the tail of this distribution, which is exactly where the two
disagree, so it mis-estimates how many nodes stay below X.""")
