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

This packet asks whether a divergent orbit forces the two cases to merge. The answer is exact but negative:

1. a divergent orbit contains an escaping sequence of ordinary tail minima;
2. the coefficient stopping depths of those minima tend to infinity;
3. a subsequence converges 2-adically to an all-prefix coefficient-supercritical tangent word;
4. the same ordinary realizing minima escape to `+infinity` in the real place.

Thus compactness produces a **two-place tangent**, not one bounded ordinary seed. The missing theorem remains Archimedean tightness.

## Headline claims

| ID | Status | Content |
|---|---|---|
| `T-6601` | `PROPOSED` | Exact finite threshold: an infinite-stopping start larger than `H_L` has coefficient stopping depth greater than `L`. |
| `T-6602` | `PROPOSED` | Every divergent orbit has wave minima `h_i -> infinity` with `tau(h_i) -> infinity`, and an orbit-supported all-supercritical 2-adic tangent. |
| `T-6603` | `PROPOSED` | Divergence dichotomy: either some wave minimum has `tau=infinity`, or there are infinitely many distinct, increasingly deep CST counterexamples. |
| `R-6601` | `PROPOSED` | PR #76 and PR #77 do not fuse into a proof: their compact limit can be nonordinary, while the actual ordinary roots escape. |

## Exact positive consequence

A sufficient route to eliminate divergent trajectories is now:

```text
(A) every positive integer has finite coefficient stopping time;
(B) t(n)=tau(n) for all sufficiently large n.
```

Indeed, a divergent orbit has wave minima tending to infinity. Under (A), all their coefficient stopping times are finite; under (B), their ordinary stopping times would then also be finite, contradicting the wave-minimum property.

This is weaker than demanding Terras's CST equality for every positive integer, but it remains open. To prove the full Collatz conjecture one must additionally exclude nontrivial positive cycles.

## Read first

1. `claims/T-6601-finite-coefficient-threshold.md`
2. `claims/T-6602-wave-minimum-supercritical-tangent.md`
3. `claims/T-6603-divergence-cst-dichotomy.md`
4. `claims/R-6601-no-compactness-fusion.md`
5. `LITERATURE_AUDIT.md`
6. `../../reports/gpt56-positive-tangent-01/2026-07-31-75-positive-tangent.md`
