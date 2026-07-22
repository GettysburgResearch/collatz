# Q-9702 — Cap-correction chain dichotomy

**Claim ID:** `Q-9702`  
**Title:** Exclude or construct an infinite corrected-stage cap chain  
**Status:** `RESOLVED NEGATIVELY BY T-9705`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-22  
**Resolved:** 2026-07-22  
**Dependencies:** `T-9703`, `T-9704`, `L-9704`--`L-9706`, `T-9705`  
**Scope:** arbitrary physically overlapping infinite corrected 256-stage directives  
**Related counterexample candidates:** none

## Original question

After nonnegative quotient extinction, could an infinite directive satisfy

\[
S_m(w_m)=R_{m+1}(w_{m+1})
\tag{1}
\]

at every sufficiently late scale and thereby produce one ordinary infinite residual? The signed extension also exposes the dual possibility

\[
3^{A_m}-S_m
 =2^{D_{m+1}}-R_{m+1}.
\tag{2}
\]

## Resolution

No. `T-9705` excludes both alternatives uniformly over the complete directive class.

`L-9704` removes every connector inverse and writes one full stage as a 258-coordinate homogeneous zero sum. The 256 internal coordinates have prime support contained in `{2,3}`. `T-9704` and `L-9705` force the two cap or co-cap endpoints to have combined outside-prime height

\[
{6498\over346819}<\frac1{50}
\tag{3}
\]

relative to the projective stage height. Primitive normalization costs at most `216`; positivity rules out every proper vanishing subsum; and a 2-adic ratio separates distinct scales.

Corollary 1 of Evertse (1984) allows only finitely many such nondegenerate `(1,1/50,{2,3})`-admissible projective zero sums. An infinite cap or co-cap tail would produce infinitely many. Contradiction.

## Consequence

For every infinite directive,

```text
a_k != 0 infinitely often,
the unique Z_2 completion is not in Z.
```

No positive ordinary initialization exists, and no `K-####` candidate is created.

## Status boundary

The resolution remains `PROPOSED` pending independent reconstruction of the native chain and inspection of the external theorem. No source-branch status is promoted by this file.
