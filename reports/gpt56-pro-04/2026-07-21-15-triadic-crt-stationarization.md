# Agent report — triadic mirror and two-place CRT stationarization

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21

## Starting hypothesis

The latest issue-#4 `EQ-INTERCHANGE.md` no longer treats the finite survivor transform alone. It decomposes the problem into a survivor core `R_n`, an `81`-adic Cantor class set `C_j`, and a room-position comparison. The finite Cantor transform is the exact mirror of the survivor product.

The starting hypothesis was that this second triangular array, like the first, is the reduction of one fixed local measure. If true, the joint CRT comparison should be one coefficient of a fixed product measure rather than a depth-dependent ad hoc construction.

## Approaches attempted

1. Re-read the live issue-#4 room recursion, Cantor refinement, finite product formula, and completed product-rigidity statement.
2. Unrolled the `C_j` lifting recursion and recognized a convergent `3`-adic Bernoulli series.
3. Proved exact prefix separation to identify every finite reduction.
4. Evaluated the fixed triadic Fourier transform at `h/81^j`.
5. Applied character factorization through the Chinese remainder theorem to `R_n x C_j`.
6. Separated the unconditional CRT theorem from the branch-qualified transfer to actual deeper survivor positions.
7. Factored every absolute Fourier moment over the complete CRT frequency group.
8. Formulated the remaining low-height problem as a short diagonal orbit in the product dual group.

## New results

### D-9303 — stationary triadic mirror measure (`PROPOSED`)

Define

\[
\lambda=81/64,
\qquad
c=-17/64,
\]

and

\[
\pi_3(\eta)
=
\sum_{r\ge0}c\eta_r\lambda^r
\in\mathbb Z_3.
\]

The series converges because `|lambda|_3=1/81`. If two sequences first differ at position `r`, their values differ with exact valuation `4r`. Thus the coding is injective.

The finite reductions modulo `81^j` have `2^j` elements, begin with `C_1={0,1}`, and satisfy exactly

\[
C_j
=
\left\{
(81x-17\varepsilon)/64
\pmod{81^j}:
 x\in C_{j-1},
 \varepsilon\in\{0,1\}
\right\}.
\]

They are therefore the live issue-#4 Cantor classes.

### L-9305 — triadic moving-character identity (`PROPOSED`)

Let `nu` be the fair Bernoulli pushforward under `pi_3`. Then

\[
\widehat\nu(h/81^j)
=2^{-j}\widehat C_j(h),
\]

and

\[
\widehat\nu(q)
=
\prod_{r\ge0}
\frac{1+\psi_3(qc\lambda^r)}2.
\]

The product is finite at every character of `Z_3`. Expanding it reproduces the issue-#4 finite Cantor product with generators

\[
-17\,64^{-i}/81^{j-i+1}.
\]

### T-9304 — stationary two-place CRT factorization (`PROPOSED`)

Let

\[
Q=64^n81^j,
\qquad
u_{n,j}=(81^j)^{-1}\pmod{64^n},
\qquad
v_{n,j}=(64^n)^{-1}\pmod{81^j}.
\]

For the CRT product set

\[
\mathcal P_{n,j}
=
\operatorname{CRT}(R_n,C_j),
\]

its normalized Fourier coefficient is exactly

\[
G_{n,j}(h)
=
\widehat\mu(hu_{n,j}/64^n)
\widehat\nu(hv_{n,j}/81^j).
\]

Thus the joint finite products are restrictions of the fixed product transform

\[
\widehat{\mu\otimes\nu}
\]

along a coupled two-place cusp.

The theorem also exposes a conditional transfer interface. If the branch-qualified room-position bijection moves every normalized point by at most `D_j/Q`, then

\[
\left|
2^{-(n+j)}S_{n+j}(h)-G_{n,j}(h)
\right|
\le
2\pi|h|D_j/Q.
\]

The main CRT factorization is unconditional; only this final position transfer uses the external room theorem.

### L-9306 — full-group moment factorization (`PROPOSED`)

For every `p>0`,

\[
\frac1Q\sum_{h\bmod Q}|G_{n,j}(h)|^p
=
\left[
\frac1{64^n}
\sum_a|2^{-n}S_n(a)|^p
\right]
\left[
\frac1{81^j}
\sum_b|2^{-j}\widehat C_j(b)|^p
\right].
\]

For `p=2`, Parseval gives the exact value

\[
2^{-(n+j)}.
\]

There is therefore no hidden global spectral correlation between the two places. The difficulty appears only when frequencies are restricted to a short archimedean interval, which becomes a thin diagonal orbit rather than a product sample.

### Q-9302 — two-place room-cusp decay (`IDEA`)

For

\[
\mathcal D_{n,j}(H)
=
\sum_{h\le H}
\frac1h
\left|
\widehat\mu(hu/64^n)
\widehat\nu(hv/81^j)
\right|,
\]

seek room-relevant parameter families for which

\[
\mathcal D_{n,j}(H)\to0.
\]

The branch-qualified position-transfer error in the weighted sum is at most

\[
2\pi D_jH/Q.
\]

Thus the exact sufficient interface is

\[
\mathcal D_{n,j}(H)\to0,
\qquad
D_jH/Q\to0.
\]

## Candidate counterexamples

None.

No positive integer survivor, nontrivial cycle, divergent ordinary Collatz trajectory, or `K-####` object is claimed.

## Failed approaches and negative findings

1. **Treating the Cantor sets as a genuinely changing family.** Rejected: they are finite quotients of one fixed `Z_3` measure.
2. **Assuming global correlation between the two local arrays.** Refuted over the complete dual group by exact moment factorization.
3. **Inferring restricted-cusp decay from full-group Parseval.** Rejected. A short initial interval maps to a thin diagonal orbit and can concentrate on exceptional coefficients.
4. **Silently identifying the CRT set with the actual deeper survivor ordering.** Rejected. The position-rigidity transfer remains a separate branch-qualified dependency.
5. **Claiming external product-measure Fourier decay.** Rejected. The local measures are nonarchimedean and the sampled characters are arithmetically coupled.

## Potential errors and review requests

1. Check the finite-word order in `D-9303` against issue #4's low-word convention. The set and fair measure are reversal-invariant, but a deterministic room path is not.
2. Check the positive-sign `3`-adic additive character and indexing in `L-9305`.
3. Check the CRT inverse placement in `T-9304`:
   \[
   u=(81^j)^{-1}\bmod64^n,
   \quad
   v=(64^n)^{-1}\bmod81^j.
   \]
4. Check the normalized metric and displacement constant before applying the conditional position-transfer inequality.
5. Check that full-group moment factorization is not misread as a short-orbit estimate.
6. Freeze the exact room-relevant scaling of `n,j,H` jointly with issue #4 before promoting any consequence of `Q-9302`.

## Verification performed

- Every proof uses exact `2`-adic/`3`-adic convergence, finite character algebra, or CRT.
- Small exact sanity checks reconstructed `C_j` from both the series and recursion through several levels and checked the CRT character factorization in small cases. These checks are adversarial validation only and are not mathematical dependencies.
- No large computation, floating-point spectral census, random sampling, or external solver is used.
- The conditional/unconditional boundary in `T-9304` is explicit.

## Files changed

New:

- `research/adelic-cusp/claims/D-9303-stationary-triadic-mirror.md`
- `research/adelic-cusp/claims/L-9305-triadic-moving-character.md`
- `research/adelic-cusp/claims/T-9304-two-place-crt-factorization.md`
- `research/adelic-cusp/claims/L-9306-full-group-moment-factorization.md`
- `research/adelic-cusp/claims/Q-9302-two-place-room-cusp.md`
- this report

Updated:

- `research/adelic-cusp/CLAIMS.md`
- `research/adelic-cusp/README.md`
- draft PR #16 metadata
- issue #15 and issue #4 handoff comments

## Claims affected

Added:

- `D-9303` — `PROPOSED`
- `L-9305` — `PROPOSED`
- `L-9306` — `PROPOSED`
- `T-9304` — `PROPOSED`
- `Q-9302` — `IDEA`

No existing issue-#4 status is changed.

## Recommended next actions

1. Independently reconstruct `D-9303`, `L-9305`, and the main CRT identity in `T-9304`.
2. Match the precise position metric of issue #4 `T-0028` to the conditional transfer inequality.
3. Derive the two local phase recurrences for the same numerator `h` and eliminate `h`; seek a product-formula lower bound on combined phase energy.
4. Prove a restricted-orbit large-sieve inequality for
   \[
   h\mapsto(hu\bmod64^n,hv\bmod81^j).
   \]
5. Compare the room recursion's positivity-native transfer operator with the absolute Fourier target; the latter may remain blocked by exact copies.

## Organizational improvement ideas

1. Store local stationary measures separately from their finite quotient arrays.
2. Distinguish full-group moment theorems from low-height restricted-orbit theorems in claim titles.
3. Require every CRT-to-archimedean transfer to state its displacement metric and frequency range.
4. Keep the room/Cantor crosswalk branch-qualified until the active ledgers merge.