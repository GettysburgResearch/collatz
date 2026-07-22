# Session report — stage quotient exhaustion

**Agent:** `gpt56-cylinder-01`  
**Issue:** `#31`  
**Branch:** `agent/gpt56-cylinder-01/31-residue-cylinder-dichotomy`  
**Date:** 2026-07-22

## Starting hypothesis

The first `97xx` packet excluded the direct dyadic-boundary connector class by
uniform contraction, but explicitly stopped at PR #3's genuinely supercritical
256-transition stage. The working hypothesis was that new work elsewhere in the
repository might supply either:

1. an ordinary forward-generated bulk that closes the zipper; or
2. a stronger completion-height comparison that pays the entire next stage
   cylinder rather than only the current stage denominator.

## Repository peek

The following live work was inspected before continuing.

- **PR #32:** independent adversarial reconstruction passed `ADEL/L-9309`,
  `T-9307`, `T-9308`, `L-9310`, `T-9311`, and `T-9312`. This substantially
  strengthens confidence in completion-height arguments as a reusable method.
- **PR #3:** `T-0030` now generates the logarithmic bulk by the positive ordinary
  recurrence `V_(m+1)=V_m+2^(m+1)V_m^2`; `T-0028`/`T-0029` also expose the
  padding counter as a finite-prefix address tape. These remove two oracle-style
  objections but leave full residual-cylinder membership open.
- **PR #20:** `T-9414`/`T-9415` exclude eventually periodic positive increment
  tails of period at most three in the active stack system. This is relevant
  methodology but not a direct theorem about PR #3 stage words.
- **Issue #29 comment:** reports a `Theta(K^2)` completion-height pressure for an
  eventually-zero active-cylinder tail, with an explicit warning that 2-adic
  series membership is weaker than stabilization. The unpublished files were
  not used as dependencies.

## Approaches attempted

### 1. Direct giant stage computation

An attempt was made to compute complete PR #3 stage corrections at the first
full scales with ordinary Python big integers. The raw offsets are already
million-bit objects and this was not a productive proof route in the available
session. No partial output from that failed attempt is used or recorded as
evidence.

### 2. Current-slope contraction

The ratio `N_m/q_m` is greater than one, exactly as PR #3 `T-0024` states. The
finite trap from `T-9702` therefore cannot be transferred at the current-stage
scale.

### 3. Pay the next cylinder

The decisive normalization is instead

\[
\varepsilon_m=N_m/q_{m+1}.
\]

Because the next complete stage modulus nearly squares while the current odd
multiplier does not, `epsilon_m` is exponentially tiny. This gives a direct
height recurrence for `z_m/q_m`.

## New results

### `L-9702` — canonical composite cap

A finite chain of canonical local tiles

\[
\rho_j+q_jy\mapsto\psi_j+N_jy,
\qquad
0\le\rho_j<q_j,
\quad
0\le\psi_j<N_j,
\]

has one complete canonical tile

\[
R+Qy\mapsto S+Py
\]

with

\[
0\le R<Q,
\qquad
0\le S<P.
\]

The proof is a finite mixed-radix induction and preserves equivalence with all
intermediate integrality conditions.

### `T-9703` — stage quotient exhaustion

For PR #3's corrected 256-stage exponents,

\[
\log_2\frac{3^{A_m}}{2^{D_{m+1}}}
<
-\frac{22173699}{5248}2^m+\frac{1024}{41}<-2.
\]

If an ordinary nonnegative infinite stage trajectory exists, put

\[
r_m=z_m/2^{D_m}.
\]

Then

\[
r_{m+1}<\varepsilon_m(1+r_m).
\]

While `r_m>=1`, the ratio more than halves; once below one, it remains below
one. Exact cylinder membership then forces

\[
z_m=R_m,
\qquad
Y_m=0,
\qquad
S_m=R_{m+1}
\]

at every sufficiently late scale.

The unbounded ordinary quotient channel is therefore not the final infinite
object. Every ordinary trajectory must eventually become a zero-quotient
cap-correction chain.

### `Q-9702` — exact remaining obstruction

The supercritical dichotomy is now reduced to

\[
S_m(w_m)=R_{m+1}(w_{m+1})
\]

at every late scale. Negative progress means excluding every infinite chain;
positive progress means generating one by a finite rule and then supplying one
finite marked initialization, exact replay, positivity, and growth.

### `X-9702` — exact finite audit

The experiment checks the exponent arithmetic at 17 scales, 160,434 canonical
composite chains, and 64 deterministic quotient paths. The independent checker
directly enumerates 178,808 different composite residue systems and 25 separate
quotient paths. All checks pass with frozen digests.

## Candidate counterexamples

None. No `K-####` identifier is created.

A cap-correction tail would be materially closer to a candidate than a generic
2-adic zipper, but it would still need a finite initial positive integer and a
proof of its entire physical future.

## Failed approaches

- direct brute computation of complete million-bit stage offsets was too costly
  and supplied no proof;
- current-stage positive slope cannot yield a finite trap;
- PR #20's short-period theorem has no proved translation to stage-word tails;
- the ordinary generator `V_m` remains auxiliary until it is placed in the
  exact cap-correction equations.

## Potential errors

1. `T-9703` depends on the frozen exact interface of PR #3 `T-0027`, whose native
   status is still `PROPOSED`.
2. The cap bound requires nonnegative canonical local caps, not merely integral
   local quotients.
3. The residual tail result must not be advertised as a finite marked Collatz
   initialization.
4. A tiny correction interval is not itself proof that no correction exists.
5. Stage-word compatibility across adjacent scales must be retained in any
   future cap-chain search.

## Files changed

- `research/residue-cylinder-dichotomy/claims/L-9702-canonical-composite-cap.md`
- `research/residue-cylinder-dichotomy/claims/T-9703-stage-quotient-exhaustion.md`
- `research/residue-cylinder-dichotomy/claims/Q-9702-cap-correction-chain.md`
- `experiments/X-9702-stage-quotient-exhaustion/`
- packet indices/audits updated in the same namespace
- this append-only report

## Claims affected

- new: `L-9702`, `T-9703`, `Q-9702`, `X-9702`;
- narrowed: `Q-9701` is superseded as a broad zipper formulation by the sharper
  cap-correction target, but its historical statement is preserved;
- cross-links only: PR #3 `T-0027`, `T-0030`; PR #32; PR #20
  `T-9414`/`T-9415`.

## Recommended next actions

1. Independently reconstruct `L-9702` and the normalized-height proof of
   `T-9703`.
2. Compute structured `R_m,S_m` data with a faster exact backend only as a
   conjecture generator; search for type-independent low-block or sign
   obstructions.
3. Substitute the ordinary bulk `V_m` into the equality
   `S_m=R_(m+1)` and derive exact coefficient conditions.
4. Seek a completion-height numerator for a long cap-correction run, now using
   the exponentially tiny bound on `R_(m+1)/q_(m+1)`.
5. Test eventual periodic normalized stage rules against a native
   exponential-polynomial obstruction before attacking arbitrary adaptive
   directives.

## Organizational improvement ideas

The repository would benefit from a shared five-field completion-height
interface:

```text
current correction | current cap | current odd multiplier |
current radix | next radix
```

The distinction between `N_m/q_m` and `N_m/q_(m+1)` is decisive here. Recording
both ratios in every regenerating-stage packet would prevent future positive
slope claims from silently omitting the next cylinder consumed by the proposed
state.
