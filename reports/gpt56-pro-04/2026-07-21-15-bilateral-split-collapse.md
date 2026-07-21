# Agent report — bilateral phase stitching and split collapse

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21

## Starting hypothesis

Issue #4's latest `EQ-INTERCHANGE.md` identifies the room digits as exact wrap counts, proves position-rigid CRT product structure, and exposes an inverse-limit marginal tower. The previous issue-#15 session stationarized the two local CRT factors as one fixed `Z_2` measure and one fixed `Z_3` measure.

The starting hypothesis was that the product of those two factors might supply genuinely independent spectral decay and therefore define a new, possibly weaker, room-cusp target.

The session refuted that hypothesis in its naive absolute and bounded-linear-test forms. The two factors are adjacent pieces of one reciprocal phase chain, and every split is quantitatively equivalent to the original EQ coefficient.

## Approaches attempted

1. Re-read the latest issue-#4 room-walk, one-level contraction, and inverse-limit tower sections.
2. Wrote the two local CRT character classes as local representatives of one global rational `h/(64^n81^j)`.
3. Applied a size-free circle reciprocity identity at each dyadic factor.
4. Reindexed the dyadic and triadic products against a single phase index `0<=ell<K`.
5. Evaluated the total reciprocity-shift error exactly as a geometric series.
6. Strengthened the magnitude comparison to the complex coefficients themselves.
7. Extended the pointwise comparison to arbitrary finite test sequences.
8. Reframed `Q-9302` and the proof program so the two-place representation is a proof tool, not a different target.
9. Performed small independent exact-modular sanity checks across multiple splits and frequencies; these checks are not proof dependencies.

## New results

### L-9307 — global rational diagonal and bilateral phase stitching (`PROPOSED`)

For a split

\[
K=n+j,
\qquad
Q=64^n81^j,
\]

the CRT inverse pair satisfies

\[
\frac{hu}{64^n}
\equiv
\frac hQ
\pmod{\mathbb Z_2},
\qquad
\frac{hv}{81^j}
\equiv
\frac hQ
\pmod{\mathbb Z_3}.
\]

Thus the two local factors are the local components of one global rational character.

Define

\[
M_\ell=64^{K-\ell},
\qquad
N_\ell=81^{\ell+1},
\]

\[
q_\ell(h)
\equiv
-17hM_\ell^{-1}
\pmod{N_\ell},
\]

and

\[
\delta_\ell(h)
=
\frac{17h}{M_\ell N_\ell}.
\]

The triadic depth-`K` product uses the factors

\[
|\cos(\pi q_\ell/N_\ell)|
\]

for all `ell`. The dyadic depth-`K` product uses the same factors shifted by `delta_ell`. A CRT split uses the unshifted factors for `ell<j` and shifted factors for `ell>=j`.

The exact algebraic input is the universal identity

\[
\frac zM
\equiv
\frac qN+rac a{MN}
\pmod1,
\]

where

\[
Nz\equiv a\pmod M,
\qquad
Mq\equiv-a\pmod N.
\]

No size condition is needed.

### T-9305 — split collapse and weighted discrepancy equivalence (`PROPOSED`)

Let

\[
F^{(2)}_K(h)=|S_K(h)|/2^K,
\qquad
F^{(3)}_K(h)=|\widehat C_K(h)|/2^K.
\]

Then

\[
\left|
F^{(2)}_K(h)-F^{(3)}_K(h)
\right|
\le
\frac{\pi|h|}{64^K}
\left(1-(64/81)^K\right).
\]

For every split,

\[
\left|
|G_{n,j}(h)|-F^{(3)}_K(h)
\right|
\le
\frac{\pi|h|}{64^n81^j}
\left(1-(64/81)^n\right).
\]

Consequently,

\[
\left|
|G_{n,j}(h)|-F^{(2)}_K(h)
\right|
<
\frac{2\pi|h|}{64^K}.
\]

After harmonic weighting,

\[
\left|
\mathcal D_{n,j}(H)-E_K(H)
\right|
<
\frac{2\pi H}{64^K}.
\]

Therefore every split target with `H=o(64^K)` is equivalent to the original EQ criterion. For `H=2^K`, the error is below `2*pi*2^(-5K)`.

### L-9308 — complex bilateral phase stitching (`PROPOSED`)

With

\[
B(x)=\frac{1+e^{2\pi ix}}2,
\]

the same identities hold before taking moduli:

\[
\widehat\mu(h/64^K)
=
\prod_\ell B(x_\ell+\delta_\ell),
\]

\[
\widehat\nu(h/81^K)
=
\prod_\ell B(x_\ell),
\]

and a CRT split cuts the same product at `ell=j`.

### T-9306 — complex coefficient and test-sequence equivalence (`PROPOSED`)

The complex coefficients satisfy the same pointwise bounds. More generally, for arbitrary complex test coefficients `a_h`,

\[
\left|
\sum_{h\le H}
a_h
\left(G_{n,j}(h)-\widehat\mu(h/64^K)\right)
\right|
\]

is at most

\[
\pi
\left[
\frac{1-(64/81)^K}{64^K}
+
\frac{1-(64/81)^n}{64^n81^j}
\right]
\sum_{h\le H}|a_h|h.
\]

For bounded harmonic tests `a_h=w_h/h`, `|w_h|<=1`, the error is below

\[
2\pi H/64^K.
\]

Thus even bounded signed harmonic targets are split-independent. A signed two-place representation may still provide a better proof mechanism, but not a different asymptotic coefficient.

## Candidate counterexamples

None.

No positive ordinary survivor, nontrivial cycle, divergent Collatz trajectory, or `K-####` object is claimed.

## Failed approaches and negative findings

1. **Independent local spectral gain.** Refuted on the rational diagonal: the local products are adjacent parts of one chain.
2. **A weaker two-place absolute target.** Refuted in every sub-`64^K` range by `T-9305`.
3. **A different bounded signed target.** Refuted by `T-9306`; bounded harmonic tests also collapse.
4. **Using the room-position theorem as the missing Fourier transfer.** Unnecessary for coefficient magnitudes and bounded linear tests; direct phase reciprocity is stronger at that level.
5. **Full-group moment factorization as evidence for short-orbit independence.** Still invalid. The short rational diagonal can remain exceptional.

These are method closures, not evidence for or against the Collatz conjecture.

## What remains alive

1. **Bilateral low-energy inverse theorem.** Classify low-energy lift-digit paths of the common reciprocal chain.
2. **Positive room transfer operator.** Work directly with interval counts or entropy on the inverse-limit tower instead of absolute Fourier majorants.
3. **Hyperbolic renewal.** Use the global rational diagonal as an orbit in the dual S-arithmetic solenoid.
4. **Exceptional-depth coherence.** Show that depths exceptional across adjacent scales force an impossible carry template.
5. **Direct M1 intersection.** Construct or exclude a nontrivial ordinary-integer point independently of EQ.

## Potential errors and review requests

1. Check the positive-sign additive-character conventions in `L-9308`.
2. Check the split boundary: `ell=j` belongs to the dyadic shifted range.
3. Check the exact geometric tail
   \[
   \sum_{\ell=j}^{K-1}
   \frac{17|h|}{64^{K-\ell}81^{\ell+1}}
   =
   \frac{|h|}{64^n81^j}
   \left(1-(64/81)^n\right).
   \]
4. Check that the global rational identities hold in the correct local quotient groups.
5. Check that bounded test-sequence equivalence is not misread as a signed discrepancy theorem without a kernel or positivity interface.

## Verification performed

- Every proof-level statement is exact modular, character, or geometric-series algebra.
- Small independent modular checks compared direct CRT factors with stitched factors for multiple `n,j,h` values and checked every displayed error bound.
- The checks found no discrepancy; they are adversarial validation only.
- No large search, floating-point census, random experiment, solver, or external theorem is used.
- The existing `X-9301` experiment remains unchanged and is not a dependency.

## Files changed

New:

- `research/adelic-cusp/claims/L-9307-global-rational-phase-stitching.md`
- `research/adelic-cusp/claims/T-9305-split-collapse-weighted-equivalence.md`
- `research/adelic-cusp/claims/L-9308-complex-bilateral-stitching.md`
- `research/adelic-cusp/claims/T-9306-complex-test-sequence-equivalence.md`
- this report

Updated:

- `research/adelic-cusp/claims/Q-9302-two-place-room-cusp.md`
- `research/adelic-cusp/CLAIMS.md`
- `research/adelic-cusp/README.md`
- `research/adelic-cusp/PROOF_PROGRAM.md`
- draft PR #16 metadata
- issue #15 and issue #4 handoff comments

## Claims affected

Added:

- `L-9307`, `L-9308` — `PROPOSED`
- `T-9305`, `T-9306` — `PROPOSED`

Reframed:

- `Q-9302` — remains `IDEA`, now asks for a genuinely better proof mechanism after exact target equivalence.

No issue-#4 claim status is changed.

## Recommended next actions

1. Independently reconstruct `L-9307` and `T-9305` first.
2. Check the complex conventions before reviewing `L-9308` and `T-9306`.
3. Derive the exact lift-digit recurrence
   \[
   y_{\ell+1}=
   (\{64y_\ell\}+j_\ell)/81
   \]
   as the state space for the bilateral inverse theorem.
4. Emit exact lift-digit paths only for existing `X-9301` argmins; do not expand the brute-force range.
5. Coordinate with issue #4 on whether the positive room-tower operator or carry-template classification is the higher-EV next packet.

## Organizational improvement ideas

1. Separate a new representation from a genuinely weaker theorem target.
2. Require every proposed multi-place gain to audit whether its local phases are independent or stitched by reciprocity.
3. Distinguish ordered-position transfer from direct coefficient transfer.
4. Record method closures as refutations of a proof route, not as mathematical evidence about Collatz.
5. Preserve the isolated `93xx` namespace until canonical-ledger reconciliation.