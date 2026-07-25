"""T-6181 — criticality of the mx+1 family under the T-6131 framework.

For T_m(n) = (mn+1)/2 on odd n, n/2 on even, divergence requires odd-step density
    liminf k_L/L  >=  alpha_m = log2/log m.
Typical density is 1/2, so:
    alpha_m > 1/2  (i.e. m < 4)  ->  divergence is ATYPICAL: measure 0, dimension H_2(alpha_m)
    alpha_m < 1/2  (i.e. m > 4)  ->  divergence is TYPICAL: measure 1, dimension 1
The framework therefore PREDICTS that 3x+1 has (at most) rare divergent orbits while 5x+1 has
almost-everywhere divergence.  Both predictions are checked empirically below.
"""
import math
from math import log, log2

H2 = lambda p: -p*log2(p) - (1-p)*log2(1-p)          # noqa: E731


def T(n, m):
    return (m*n + 1)//2 if n % 2 else n//2


print(f"{'m':>4} {'alpha_m':>9} {'regime':>13} {'dim of divergence set':>22} "
      f"{'codim':>8} {'typical drift/step (nats)':>26}")
for m in (3, 5, 7, 9, 11, 181):
    a = log(2)/log(m)
    drift = 0.5*log(m/4)
    if a > 0.5:
        print(f"{m:>4} {a:>9.5f} {'SUBcritical':>13} {H2(a):>22.6f} {1-H2(a):>8.6f}"
              f" {drift:>26.5f}")
    else:
        print(f"{m:>4} {a:>9.5f} {'SUPERcritical':>13} {'1 (full measure)':>22} {0.0:>8.6f}"
              f" {drift:>26.5f}")
print("\n  m = 4 is the critical multiplier: alpha_4 = 1/2 exactly, drift 0, codimension 0.")
print("  m = 3 is the ONLY odd multiplier in the subcritical range 2 < m < 4,")
print(f"  and it sits only {1-H2(log(2)/log(3)):.6f} into it (max possible 1).")

# --- empirical check of the two predictions -------------------------------------------
def fate(n, m, cap=10**30, steps=3000):
    """'cycle' if the orbit repeats, 'diverges' if it exceeds cap."""
    seen = set()
    for _ in range(steps):
        if n > cap:
            return "diverges"
        if n in seen:
            return "cycle"
        seen.add(n)
        n = T(n, m)
    return "cycle" if n < cap else "diverges"


for m in (3, 5):
    N = 20000
    d = sum(1 for n in range(1, N+1) if fate(n, m) == "diverges")
    print(f"\n  m={m}: of the first {N} integers, {d} ({100*d/N:.2f}%) exceed 10^30 within"
          f" 3000 steps")
    if m == 3:
        print("        framework predicts ~0% (measure zero)          -> "
              f"{'CONFIRMED' if d == 0 else 'REFUTED'}")
    else:
        print("        framework predicts ~100% (full measure)        -> "
              f"{'CONFIRMED' if d > 0.9*N else 'REFUTED'}")
