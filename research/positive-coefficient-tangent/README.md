# Positive coefficient tangent: the exact divergence-side fusion

**Agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Issue:** independent continuation of issue `#75`  
**Namespace:** isolated `66xx`  
**Status:** theorem-level claims are **PROPOSED** pending independent reconstruction  

**No proof of the Collatz conjecture is claimed.**

## Purpose

The active positive-direction packet in PR #76 leaves two necessary possibilities for a least counterexample:

```text
coefficient stopping time tau = infinity,
```

or a very late first coefficient crossing. PR #77 proves that the first case tends to `+infinity`, but this is not a contradiction.

This packet first asks whether a divergent orbit forces the two cases to merge. The answer is exact but negative:

1. a divergent orbit contains an escaping sequence of ordinary tail minima;
2. the coefficient stopping depths of those minima tend to infinity;
3. a subsequence converges 2-adically to an all-prefix coefficient-supercritical tangent word;
4. the same ordinary realizing minima escape to `+infinity` in the real place.

Thus compactness produces a **two-place tangent**, not one bounded ordinary seed. The missing theorem remains Archimedean tightness.

The continuation then attacks the delayed-crossing lane directly. It proves two exact residue--remainder pressure theorems:

1. a no-descent first crossing must have either logarithmically growing surplus or exponentially growing canonical residue;
2. its canonical representative, factor complexity, surplus bank, and exact real fixed point satisfy one joint inequality that can certify descent without enumerating lifts.

## Headline claims

| ID | Status | Content |
|---|---|---|
| `T-6601` | `PROPOSED` | Exact finite threshold: an infinite-stopping start larger than `H_L` has coefficient stopping depth greater than `L`. |
| `T-6602` | `PROPOSED` | Every divergent orbit has wave minima `h_i -> infinity` with `tau(h_i) -> infinity`, and an orbit-supported all-supercritical 2-adic tangent. |
| `T-6603` | `PROPOSED` | Divergence dichotomy: either some wave minimum has `tau=infinity`, or there are infinitely many distinct, increasingly deep CST counterexamples. |
| `T-6604` | `PROPOSED`; source-qualified corollary | Exact long-return/first-crossing gap inequality; sublinear-bank target failures must be recurrence-poor, and exact Farey gaps can eliminate recurrent candidates directly. |
| `T-6605` | `PROPOSED`; source-qualified corollary | Joint canonical pressure: factor repetitions, dyadic separation, the proper-prefix surplus bank, and `A_w/(2^j-3^q)` give an exact sufficient certificate for canonical descent. |
| `R-6601` | `PROPOSED` | PR #76 and PR #77 do not fuse into a proof: their compact limit can be nonordinary, while the actual ordinary roots escape. |

## Exact positive consequence

A sufficient route to eliminate divergent trajectories is now:

```text
(A) every positive integer has finite coefficient stopping time;
(B) t(n)=tau(n) for all sufficiently large n.
```

Indeed, a divergent orbit has wave minima tending to infinity. Under (A), all their coefficient stopping times are finite; under (B), their ordinary stopping times would then also be finite, contradicting the wave-minimum property.

This is weaker than demanding Terras's CST equality for every positive integer, but it remains open. To prove the full Collatz conjecture one must additionally exclude nontrivial positive cycles.

## Delayed-crossing frontier

For a first-crossing word `w`, write

```text
T_w(x)=(3^q x+A_w)/2^j,
Delta_w=2^j-3^q,
x_*(w)=A_w/Delta_w.
```

If `r^+(w)` is the canonical positive cylinder root and `y=T_w(r^+(w))`, then

```text
Delta_w*r^+(w)-A_w = 2^j*(r^+(w)-y).
```

Thus Box 2 is exactly canonical descent.

`T-6604` controls a repeated factor using the exact logarithmic crossing gap. `T-6605` adds the same-orbit odd-source product estimate and proves, for every factor length `L`,

```text
p_w(L)
>=
ceil((j-L+1)/
     (1+floor((G_j(B)-1)*x_*(w)/2^L))),

G_j(B)=3^B*exp(7/9)*j^(1/9).
```

Equivalently, a repeated-factor moat larger than `(G_j(B)-1)x_*(w)` forces descent. This is the requested direct coupling:

```text
symbolic repetition
 -> full 2^L physical separation
 -> lower ordinary height
 -> comparison with the exact non-descent threshold.
```

A surviving late first crossing must now be high-bank, recurrence-poor, or have a sufficiently large exact fixed-point threshold to pay both pressure laws.

## Read first

1. `claims/T-6605-canonical-first-crossing-pressure.md`
2. `claims/T-6604-long-return-first-crossing-barrier.md`
3. `claims/T-6601-finite-coefficient-threshold.md`
4. `claims/T-6602-wave-minimum-supercritical-tangent.md`
5. `claims/T-6603-divergence-cst-dichotomy.md`
6. `claims/R-6601-no-compactness-fusion.md`
7. `LITERATURE_AUDIT.md`
8. `../../reports/gpt56-positive-tangent-01/2026-07-31-75-positive-tangent.md`
