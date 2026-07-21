# T-9302 — Conditional density-one full EQ

**Claim ID:** T-9302  
**Title:** Frequency blocks plus valuation-stratified depth periods imply full weighted EQ on density-one depths  
**Status:** SUPERSEDED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9302`, `T-9303`; branch-qualified frequency-block mean  
**Scope:** historical conditional density-one synthesis  
**Superseded by:** `T-9309`

## Historical statement

Assume the branch-qualified frequency-block estimate used in `L-9302`. Put

\[
b=2^{-1/2},
\qquad
\gamma_0=\log_{81}\sqrt2.
\]

Then, for every

\[
0<\alpha<\gamma_0,
\]

the complete weighted EQ sum

\[
E_K=\sum_{1\le h\le2^K}rac{|S_K(h)|}{2^K h}
\]

tends to zero along a natural-density-one set of depths. The proof combines:

1. `T-9303` on the growing low-frequency window;
2. valuation-stratum summation;
3. `L-9302` on the high-frequency harmonic tail;
4. Markov's inequality and exact depth-annulus tiling.

## Supersession reason

`T-9308` now proves the high-frequency tail unconditionally from lift-prefix entropy. Substituting it for the branch-qualified shell input yields `T-9309`:

> The complete weighted EQ criterion holds along a natural-density-one set of depths with no external mathematical hypothesis.

`T-9309` retains the valuation-stratified low-window argument of this file but removes its sole external dependency. The historical theorem is therefore superseded, not refuted.

## Dependency and status audit

- The original full proof remains in Git history.
- `T-9303` remains an active self-contained theorem and is a dependency of `T-9309`.
- `L-9302` remains a reusable conditional analytic lemma.
- No issue-#4 status is changed.
- `SUPERSEDED` does not mean `REFUTED`.
- Density-one EQ does not imply all-depth EQ and does not decide M1.

## Suggested review order

Review `L-9309`, `T-9307`, `T-9308`, `T-9303`, and `T-9309` in that order.