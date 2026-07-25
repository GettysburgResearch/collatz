"""X-6200 step 4: replace the binomial by the true residue Markov chain (O-6202's next attack).

State = node residue mod 3.  Under doubling: 0->0, 1->2, 2->1 (no descent available).
Descent is available only from state 2, and its child's residue is uniform on {0,1,2}
(parent uniform mod 9 given residue 2 mod 3).  Tracking the descent count b:

  N_{d+1}(0,b) = N_d(0,b) + (1/3) N_d(2,b-1)
  N_{d+1}(1,b) = N_d(2,b) + (1/3) N_d(2,b-1)
  N_{d+1}(2,b) = N_d(1,b) + (1/3) N_d(2,b-1)

This is exact given the mod-9 equidistribution, and it automatically encodes the absorption of
state 0.  Compare with the binomial the old escape model assumed, and with the measurement.
"""
import math
from math import comb

D = 34
N = [[0.0]*(D+2) for _ in range(3)]
N[1][0] = 1.0                      # root n = 1 has residue 1 mod 3
for d in range(D):
    M = [[0.0]*(D+2) for _ in range(3)]
    for b in range(D+1):
        M[0][b] += N[0][b]
        M[1][b] += N[2][b]
        M[2][b] += N[1][b]
        if b+1 <= D:
            for r in (0, 1, 2):
                M[r][b+1] += N[2][b]/3.0
    N = M
tot = sum(N[r][b] for r in range(3) for b in range(D+1))
dist = [sum(N[r][b] for r in range(3))/tot for b in range(D+1)]

# measured distribution at depth 34, trivial cycle excluded
from collections import Counter
def kids(n):
    out=[(2*n,0)]
    if n % 3 == 2:
        c=(2*n-1)//3
        if c != 1: out.append((c,1))
    return out
lvl=[(1,0)]
for _ in range(D): lvl=[(m,b+t) for n,b in lvl for m,t in kids(n)]
obs=Counter(b for _,b in lvl); NM=len(lvl)

print(f"depth {D}:  measured {NM:,} paths;  Markov model total {tot:,.0f};  (4/3)^{D} = "
      f"{(4/3)**D:,.0f}\n")
print(f"{'b':>4} {'measured':>11} {'Markov':>11} {'binomial':>11} {'M/meas':>8} {'B/meas':>8}")
for b in range(0, 20):
    o = obs.get(b, 0)/NM
    m = dist[b]
    bi = comb(D, b)*(0.25**b)*(0.75**(D-b))
    if o or m > 1e-4 or bi > 1e-4:
        print(f"{b:>4} {o:>11.5f} {m:>11.5f} {bi:>11.5f} "
              f"{m/o if o else float('inf'):>8.3f} {bi/o if o else float('inf'):>8.3f}")
mo = sum(b*obs.get(b,0) for b in obs)/NM
mm = sum(b*dist[b] for b in range(D+1))
print(f"\nmean b : measured {mo:.4f}   Markov {mm:.4f}   binomial {D/4:.4f}")
vo = sum((b-mo)**2*obs.get(b,0) for b in obs)/NM
vm = sum((b-mm)**2*dist[b] for b in range(D+1))
print(f"var  b : measured {vo:.4f}   Markov {vm:.4f}   binomial {D*3/16:.4f}")
print(f"max  b : measured {max(obs)}        Markov support to {max(b for b in range(D+1) if dist[b]>1e-9)}")
