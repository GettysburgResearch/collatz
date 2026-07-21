# Session report: H-frontier iteration 02

**Agent:** `gpt56-h-01`  
**Issue:** [#17](https://github.com/gfreund123/collatz/issues/17)  
**Branch:** `agent/gpt56-h-01/17-h-exact-frontier`  
**Date:** 2026-07-21

## Starting point

PR #19 had isolated two central interfaces:

1. `Q-9501`, the unproved mixed-sign carry step behind universal
   contracting-cylinder descent;
2. `Q-9502`, exclusion of a bounded representative tree with positive capital.

The aim of this iteration was to stop treating the phase inequality as a single
opaque induction and to derive stronger analytic restrictions on any surviving
one-sided ray.

## Approaches attempted

1. Reparameterized the displacement by the real affine fixed point.
2. Proved canonical ranges for both the exact input residue and its endpoint.
3. Split concatenation into same-sign and mixed-sign cases.
4. Tested the remaining mixed-sign frontier on random and critical mechanical
   words.
5. Extended survivor harmonic summability to all subcritical valuation weights.
6. Derived an exact recurrence coupling multiplier capital to the odd core.
7. Tested and refuted a tempting but false first-letter fixed-point shortcut.
8. Enumerated short prefix-expanding representative candidates.

## New proposed results

### L-9511 — canonical phase coordinates

Every exact word satisfies

\[
0\le A<U,\qquad0\le Y<V,
\]

and, with `t=B/(U-V)` and `rho=(A-Y)/(U-V)`,

\[
A=t+rho U,\qquad Y=t+rho V.
\]

This reduces `C-9501` exactly to `0 <= rho < 1` and proves one half of each
signed inequality without induction.

### L-9512 — same-sign closure

The signed phase interval is rigorously closed under concatenation whenever the
two component determinants have the same sign. Therefore every minimal failure
must be a mixed-sign crossing. This is a strict reduction of `Q-9501`.

### T-9504 — weighted survivor moments

For every `0 < lambda < 8`,

\[
\sum_{p\in I}\frac{\lambda^{r(p)}}p<\infty.
\]

Along a hypothetical nonperiodic survivor this gives

\[
\sum_i\lambda^{r_i}(8/9)^{K_i}<\infty
\]

and a joint wall/spike counting bound.

### T-9505 — capital--core budget

For `c_* = log 9 / log 8`, every hypothetical nonperiodic survivor satisfies

\[
K_{i+1}=c_*K_i-\frac{\log u_i}{3\log2}+eta_i,
\]

where `eta_i` converges. Hence

\[
\limsup K_{i+1}/K_i\le c_*,
\qquad
\sum_i c_*^{-(i+1)}\log u_i<\infty.
\]

This creates an exact interface between real escape and the previously derived
fresh-prime requirement.

## Refutation

`R-9503` records that the fixed point of a first-contracting word need not lie
below the first one-letter residue. A length-25 critical mechanical word is an
explicit exact counterexample to that proposed shortcut.

## Experiment X-9502

The exact standard-library audit recorded:

- 20,000 random canonical endpoint checks;
- 20,000 phase identities;
- 17,562 same-sign closure checks;
- 199 critical first-contracting words through length 200;
- finite `mu_L` upper candidates through length 5 over letters at most 12;
- no tested signed-displacement failure;
- digest `cf995d0b83acd14440ad4b2442012ba07726f3b68fa51b38ef9f58f4a542d9d2`.

## Failed approaches and corrections

- Canonical range bounds alone do not settle mixed-sign closure.
- Abstract affine tuples satisfying the ratio bounds can violate the desired
  mixed-sign conclusion; actual word structure is essential.
- Bounding the fixed point by the first exact letter is false.
- Weighted harmonic moments remain subcritical; `lambda=8` is not obtained.
- The discounted core budget is compatible with fresh primes appearing at
  increasingly late times and therefore is not itself a contradiction.

## Current frontier

The finite descent side is narrowed to a word-specific mixed-sign theorem. For
first-crossing descent, it is enough to handle an expanding prefix followed by
one final letter in `{0,1,2}`.

The infinite side now has two simultaneous constraints:

1. subcritical weighted wall/spike summability for every `lambda<8`;
2. a finite `c_*`-discounted odd-core budget, despite infinitely many fresh odd
   primes.

A breakthrough can come from either:

- proving the actual-word mixed-sign crossing using the explicit offset/ghost
  digits; or
- proving a quantitative fresh-prime lower bound incompatible with the
  capital--core budget.

## Files added

- `research/h-frontier/claims/ITERATION_02.md`
- `experiments/X-9502-h-structured-frontier/README.md`
- `experiments/X-9502-h-structured-frontier/run.py`
- `experiments/X-9502-h-structured-frontier/requirements.txt`
- `experiments/X-9502-h-structured-frontier/results/summary.json`
- `reports/gpt56-h-01/2026-07-21-17-h-frontier-iteration-02.md`

## Handoff

**CURRENT CLAIMS:** `L-9511`, `L-9512`, `T-9504`, `T-9505`, `R-9503`,
`Q-9503`, `X-9502`  
**BLOCKING STEP:** word-specific mixed-sign crossing or a quantitative
fresh-prime/core-budget contradiction  
**REVIEW FIRST:** `research/h-frontier/claims/ITERATION_02.md`  
**MAIN RISK:** silently treating subcritical weighted moments or finite critical
word tests as a critical/universal theorem
