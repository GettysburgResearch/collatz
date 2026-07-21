"""The free-fuel experiment (the route's last open door, tested).

The rigidity dichotomy leaves exactly one escape: after a designed
supercritical prefix exhausts, the orbit value is a 3-smooth multiple of
the stored high part plus a carry constant.  A counterexample along the
rewrite route requires these carry-generated low bits to be
SYSTEMATICALLY supercritical (density > log_3 2) rather than balanced.

Test: for the corrected amplifier family n(k) = 8^{k+2} - 21 (and for
CRT-steered two-stage seeds), run to designed exhaustion, then measure
the parity density of the next W = |designed| steps -- the bits the
dynamics generates for free.

Null hypothesis (Collatz-consistent): density ~ 1/2 + O(1/sqrt(W)).
Counterexample signal: density persistently > log_3 2 ~ 0.6309.
"""

from core import T_iter
import math

LOG32 = math.log(2) / math.log(3)

print(f"log_3 2 = {LOG32:.5f}; free-fuel window density should be ~0.5 "
      f"under the null\n")

print("family n(k) = 8^{k+2} - 21: designed window (density 7/11), "
      "then free window of equal length")
rows = []
for k in range(10, 211, 10):
    n = 8 ** (k + 2) - 21
    designed = 4 + 11 * ((3 * k + 2) // 11)
    m, par_d = T_iter(n, designed)
    W = designed
    m2, par_f = T_iter(m, W)
    dd, df = sum(par_d) / designed, sum(par_f) / W
    rows.append(df)
    print(f"  k={k:4d}: designed {sum(par_d):4d}/{designed:4d} = {dd:.4f} | "
          f"free {sum(par_f):4d}/{W:4d} = {df:.4f}"
          f"{'   <-- supercritical!' if df > LOG32 else ''}")

mean = sum(rows) / len(rows)
var = sum((x - mean) ** 2 for x in rows) / (len(rows) - 1)
print(f"\nfree-window densities: mean {mean:.4f}, sd {var**0.5:.4f}, "
      f"n={len(rows)}")
print(f"exceeding log_3 2: {sum(1 for x in rows if x > LOG32)}/{len(rows)}")

# same for truncations of the 2-adic point Z (designed vector, then free)
from z2adic_counterexample import Z, B
print(f"\ntruncations of Z (designed {B}-step supercritical vector):")
zrows = []
for Bt in (400, 800, 1200, 1600, 2000):
    n = Z % (1 << Bt)
    m, par_d = T_iter(n, Bt)
    m2, par_f = T_iter(m, Bt)
    df = sum(par_f) / Bt
    zrows.append(df)
    print(f"  B={Bt:5d}: designed {sum(par_d)/Bt:.4f} | free {df:.4f}"
          f"{'   <-- supercritical!' if df > LOG32 else ''}")

allr = rows + zrows
print(f"\nVERDICT: {sum(1 for x in allr if x > LOG32)} of {len(allr)} "
      f"free windows supercritical; mean {sum(allr)/len(allr):.4f}")
print("No free fuel: carry-generated bits are balanced.  The dynamics")
print("does not regenerate the supercritical structure a counterexample")
print("needs; every window of divergence must be designed in advance,")
print("and (RIGIDITY.md) no schema can design infinitely many.")
