# Capacity Achievability: the collision fraction is bounded below

*Packet P3 (issue #4; /loop iteration 4). Claim T-0029; resolves
Q-0004. Companion check inline in the session report; formula verified
exactly at L = 12, 16, 20.*

## Theorem (T-0029)

Let f_L = |D_L| / N_L, N_L = Σ_{3^a>2^L} C(L,a) (supercritical
residues). There is L₀ and an explicit c > 0 with

    f_L ≥ c    for all L ≥ L₀   (c ≈ 2^{−6} from this proof).

Combined with the cost-floor theorem (T-0014), the atlas capacity is
determined to Θ(log L):

    cost(L) = (1 − H(log₃2))·L + Θ(log L)  —  **the cost-floor
    theorem is now two-sided.**

## Proof

**The lift.** The six-step collision T⁶(64q+14) = T⁶(64q+15) = 81q+20
(equal weight 4) persists under refinement: for every m < 2^{L−6},
the residues 14+64m and 15+64m share their entire T-history from step
6 onward, so at depth L they lie in the same stratum a(m) = 4 +
a_{L−6}(u_m) with equal T^L-value, where u_m = (81m+20) mod 2^{L−6}
and m ↦ u_m is a bijection (81 odd). Hence every m with a(m) ≥
a_min(L) contributes BOTH members to D_L:

    |D_L| ≥ 2·#{m : a_{L−6}(u_m) ≥ a_min(L) − 4}
          = 2·Σ_{a ≥ a_min(L)−4} C(L−6, a).

(Verified exactly: 22, 176, 3473 at L = 12, 16, 20.)

**The ratio.** For a > L/2 the binomials decrease in a, so
N_L ≤ C(L, a_min)/(1 − ρ) with ρ = (L−a_min)/(a_min+1) → (1−δ)/δ
≈ 0.585 (δ = log₃2), i.e. N_L ≤ 2.42·C(L, a_min) for large L.
The numerator keeps the single term a = a_min − 4:

    f_L ≥ 2·C(L−6, a_min−4) / (2.42·C(L, a_min)).

Stirling with a_min = δL + O(1): log₂ of the ratio of binomials is
−6H(δ) + (6δ−4)·log₂((1−δ)/δ) + O(1/L) = −5.70 + 0.166 + o(1) =
−5.53 + o(1). Hence f_L ≥ 2^{−5.53−log₂1.21+o(1)} ≈ 2^{−5.8} for
L ≥ L₀. ∎ (Data: bound gives f₂₀ ≥ 0.050; truth f₂₀ = 0.59 — the
constant is far from sharp; sharpening = summing the full tail and
using the width-2+ fibers of every lifted chart, e.g. the four charts
at L = 6 quadruple the constant immediately.)

## Remarks

1. No preimage-tree machinery was needed — the lift of one collision
   plus binomial monotonicity suffices. The Applegate–Lagarias
   interface remains relevant only for sharpening the constant toward
   the measured 0.36–0.66.
2. Generalization (same proof shape): any width-w fiber at level L₁
   lifts to give |D_L| ≥ w·Σ_{a≥a_min(L)−a₁}C(L−L₁, a) — the richer
   charts (width 18 at L = 22, width 339 at L = 44) give better
   constants at large L; the family over all lifted charts is a
   natural route to the true constant.
3. Consequence for the program: with capacity two-sided, the atlas
   hierarchy's economics are closed — every remaining open question
   about the symbolic route lives in EQ (survivor equidistribution),
   exactly as the ladder synthesis (`LADDER.md` §4) anticipated.
