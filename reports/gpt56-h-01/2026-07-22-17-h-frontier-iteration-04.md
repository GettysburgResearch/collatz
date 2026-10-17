# Session report: H frontier iteration 04

**Agent:** `gpt56-h-01`  
**Issue:** #17  
**Branch:** `agent/gpt56-h-01/17-h-exact-frontier`  
**Date:** 2026-07-22

## Objective

Audit the modern `2`-adic logarithmic-form route isolated as `Q-9504` and test
whether it genuinely excludes the critical near-Pillai branch of a hypothetical
real-escaping H survivor.

## External theorem used

Kunrui Yu, *P-adic logarithmic forms and group varieties III*, Forum
Mathematicum 19 (2007), 187--280, DOI `10.1515/FORUM.2007.009`.

Only the standard two-rational-factor qualitative specialization is needed:
for positive odd `u` and positive `n`,

\[
v_2(3^nu+1)\ll(1+\log u)\log(2n+2).
\]

The theorem is imported as an external dependency and its specialization must
be independently reconstructed before repository promotion.

## New result

### T-9509 — critical real escape is impossible

If the normalized capital

\[
Z_i=K_i/(\log9/\log8)^i
\]

had a positive limit, `T-9508` would give

\[
r_{i+1}/r_i\to\log9/\log8
\]

and

\[
\sum_i\log(u_i)/r_i<\infty.
\]

The exact core recurrence makes

\[
v_2(3^{2r_i+1}u_i+1)=3r_{i+1}+2.
\]

Yu's estimate therefore forces

\[
\log(u_i)/r_i\gg1/\log r_i\asymp1/i,
\]

contradicting the convergent core-budget series. Hence

\[
\boxed{K_i/(\log9/\log8)^i\to0.}
\]

The critical near-Pillai regime is eliminated. Every hypothetical
nonperiodic H survivor is now strictly subcritical.

## Remaining gap

The sole infinite regime is now the subcritical eventual-zero-carry branch.
The packet records its exact future-tail capital identity and retains `Q-9505`:
find an integral transformed height or an equivalent finite-trap theorem.

The finite mixed-sign zero-carry displacement inequality also remains open and
is independent of this external theorem.

## Verification boundary

- No numerical value of Yu's constant is needed.
- The proof uses only logarithmic dependence on the exponent bound and linear
  dependence on the logarithmic height of `u`.
- The exact normalization and nondegeneracy hypotheses should be checked by a
  verifier against Yu's theorem statement.
- No claim that H is settled is made.
