# Positive coefficient entropy packet

**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Branch:** `agent/gpt56-positive-entropy-01/75-supercritical-entropy`  
**Base:** draft PR #77 at `1c8ed3c7edbb190d59490d2f92a3c342c2f856eb`  
**Status:** draft mathematical research

## Objective

This packet attacks the `tau=infinity` branch of the positive coefficient gate.

For a shortcut-Collatz orbit, put

\[
D_k=q_k-\frac{\log2}{\log3}k.
\]

All-time coefficient supercriticality is exactly

\[
D_k\ge0
\qquad(k\ge0).
\]

Draft PR #77 proposes that any ordinary positive orbit satisfying this condition tends to `+infinity`. The present packet asks for a stronger, source-specific obstruction:

> How much coefficient surplus and physical height must one actual ordinary orbit generate in order to support all of its exact parity factors?

## Main chain

### `L-6801` — parity-factor dyadic separation

If the same length-`L` parity factor occurs at two times `i<j`, then

\[
2^L\mid x_i-x_j.
\]

Thus repeated symbolic information has an exact physical height cost.

For all-time-supercritical paths, repeated states are impossible, so a factor can occur at most

\[
1+X_N/2^L
\]

times below height `X_N`.

### `T-6801` — bounded surplus is impossible

Combining the dyadic occurrence bound with a crude forbidden-run entropy estimate gives

\[
\liminf_{N\to\infty}
\frac{B_N}{\log_2\log_2N}
\ge1-\frac{\log2}{\log3}.
\]

This closes the complete bounded-surplus subcase.

### `T-6802` — entropy pressure and polynomial records

A sharper weight-entropy count optimizes the factor length against the orbit height.

Let `beta_*` solve

\[
\beta_*\log_2 3
=1-H_2(\alpha-\beta_*),
\qquad
\alpha=\frac{\log2}{\log3},
\]

and put

\[
\kappa_*
=
\frac{\beta_*}{1-\beta_*\log_2 3},
\qquad
\delta_*=\kappa_*\log_2 3.
\]

Then every ordinary all-time-supercritical path satisfies

\[
\boxed{
\liminf_{N\to\infty}
\frac{B_N}{\log_2N}
\ge\kappa_*}
\]

and

\[
\boxed{
\liminf_{N\to\infty}
\frac{\log_2(X_N/n)}{\log_2N}
\ge\delta_*.}
\]

Numerically,

```text
kappa_* = 0.0226230967722...
delta_* = 0.0358567600340...
```

so

\[
X_N\ge nN^{0.03585676-o(1)}.
\]

No random model, independence assumption, or almost-everywhere theorem is used.

### `R-6801` — pointwise ergodic firewall

Spatial valuation laws and Haar-almost-everywhere genericity do not imply genericity of every ordinary positive orbit. The positive integers form a countable Haar-null subset of `Z_2`, and measure zero does not mean empty.

This identifies the exact logical failure in a current February 2026 claimed proof based on funnel density, Birkhoff, and Borel--Cantelli.

## Current combined positive dichotomy

Conditional on proposed PR #76 `T-6707` and proposed PR #77 `T-6709`, a least positive counterexample must satisfy one of:

```text
A. tau=infinity:
   the orbit tends to +infinity;
   its surplus records obey B_N >= (kappa_*-o(1))*log_2 N;
   its physical records obey X_N >= n*N^(delta_*-o(1));

B. tau finite:
   tau >= 217,976,794,617.
```

The present packet materially strengthens lane A but does not eliminate it.

## Why this is genuine progress

The new theorem is not:

- another finite-prefix enumeration;
- a compatible free parity word;
- a `2`-adic completion;
- a probabilistic average;
- or a conclusion conditional only on a pre-existing abstract path.

It is a deterministic theorem about one actual ordinary orbit. It couples:

```text
exact dyadic integrality
+ physical orbit height
+ finite-factor multiplicity
+ binary entropy.
```

It proves that a putative divergent ordinary orbit must pay a quantitative polynomial height cost merely to realize its parity language.

## What remains

A full proof still needs both of the following.

### Supercritical lane

Prove that no ordinary positive orbit can satisfy `D_k>=0` for every `k`.

The strongest current deterministic target is to improve endpoint-weight entropy to a full corridor pressure and then couple that pressure to a pointwise residue or return theorem. High factor complexity by itself is not mixing.

### Delayed-crossing lane

For every later rational approximant in the microscopic first-crossing window, prove that the maximum admissible affine remainder is smaller than the minimum needed for no descent.

The promising improvement is to impose simultaneously:

- the `485/306` all-prefix ballot barrier;
- every intermediate no-descent inequality;
- Ostrowski/continued-fraction block decomposition;
- exact path-merging and mod-9 preimage losses.

## Literature positioning

See `LITERATURE_AND_GLOBAL_STATUS.md`.

The closest 2026 results are:

- Angeltveit's exact finite verification and descent sieves;
- Rozier--Terracol's paradoxical-sequence theory;
- Chang's map-balance and one-bit orbit-mixing reduction;
- Gilbert's exact pruned-graph conjugacy.

None supplies the missing pointwise theorem.

## Review order

1. `claims/L-6801-parity-factor-dyadic-separation.md`
2. `claims/T-6802-entropy-pressure-polynomial-records.md`
3. `claims/T-6801-supercritical-surplus-entropy-floor.md`
4. `claims/R-6801-almost-everywhere-is-not-pointwise.md`
5. `LITERATURE_AND_GLOBAL_STATUS.md`
6. session report under `reports/gpt56-positive-entropy-01/`

## Status boundary

All new theorem-level mathematical claims remain **PROPOSED** pending independent reconstruction, except the elementary logical firewall `R-6801`, which is marked as a proved method boundary.

No proof of Collatz, counterexample, nontrivial cycle, or `K-####` object is claimed.
