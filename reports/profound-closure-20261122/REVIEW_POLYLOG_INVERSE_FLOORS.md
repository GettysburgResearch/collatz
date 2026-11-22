# Independent review: polylogarithmic inverse horizons

**Date:** 2026-11-22 UTC.  
**Reviewer:** symbolic/literature agent, independent of the note's author.  
**Reviewed final note SHA-256:**
`d4c5b9758f0e8ee1cb8f73d40f63ce8d5da642b48612b47842fd5b049bbd3824`.

## Finding and scope

The new bounds (9), (12), (16)--(18), and (22) are valid deductions from
the explicitly retained source inputs and inverse-unit floor. No missing
cumulative block weight, discarded least-source assumption, exponent
loss, or finite-to-infinite horizon interchange was found.

This is a review of the written analytic deduction. It does not certify
a new full Collatz theorem or assert that the imported analytic inputs
have been formalized in Lean. No older builds or computations were
rerun. Exact local source hashes and the primary reference inspected are
recorded in `polylog_inverse_review_pins.json`.

## Input normalization and the actual source floor

The primary Tao statement was checked directly in the corrected author
version v7, Proposition 1.14, equations (1.26)--(1.27), together with
consistency (1.23). If `p_t(a)` is the finite Syracuse probability,
then `D_t(a)=3^t p_t(a)`. Consequently the normalized residue average

\[
3^{-t}\sum_a|D_t(a)-D_m(a\bmod3^m)|
\]

is exactly Tao's oscillation: consistency identifies the coarse
probability with the sum over the relevant fine residue fiber. There is
no missing factor of `3^t` in the asserted mixing input (7).

The pinned E4 counting source retains all total binary valuations,
including the geometric tail. At each fixed total valuation its
ordinary sources are distinct, so its residue count is legitimate;
cycles and possible repeated sources at other clocks are not discarded.
Its resulting coefficient is

\[
C\,[q(d+t+1)+3^t\Omega].
\]

For `H=D_t-D_m`, both terms vanish at nonunits because `t>=m>=1`.
Thus only inverse sources covered by the stated floor contribute.
The actual affine identity gives `omega<=q/b`, not `omega<=1` except
at a least-unit target. Dividing by the same target `q` gives precisely

\[
C_A[d+t+1+3^t/b]m^{-A}.
\]

The floor quantifies over all unit ancestors at all finite depths. Its
use as `d` changes is therefore authorized by the hypothesis, rather
than an unstated assumption about newly sampled sources.

## Finite telescope and accumulated error

For a depth `s>2m`, the chosen residual depth satisfies `m<r<=2m`.
Every comparison has `k_j>=2m+1`, so the required prefix depth
`d=k_j-2m` is positive. Setting `t=2m` in (8) makes its depth term
exactly `k_j+1`. There are at most `s/m` comparisons, each bounded by
`C_A(s+2)m^(-A)`. The resulting error is therefore

\[
C_A s(s+2)m^{-A-1}.
\]

All comparisons are at the same original target. The `P^d` action,
including its cumulative inverse weights, has already been estimated
inside each comparison; no additional randomization or uncharged
operator product is inserted between comparisons. The terminal term is
at most `3^(2m)/q<=b^(-1/2)` under `3^(4m)<=b` and `q>=b`.

For a horizon of order `(log b)^B`, the fixed choice
`A=2B+R+3` gives an error of order at most `(log b)^(-R-4)`.
The asserted weaker `O((log b)^(-R))` bound follows uniformly in the
target. `A` and its constant are selected before `b` varies.

## Obstacle and contact indexing

The imported cylinder comparison is `V_k<=kappa D_(k+1)` at every
ordinary point. The horizon shift is retained: applying the density
bound through `K+1` gives `(K+1)(K+3)` in (16), as stated.
The conclusion that a critical-size finite certificate must appear
later than every fixed polylogarithmic clock uses a larger fixed
logarithmic saving. If the limiting value is at least twice the target
threshold, monotone convergence guarantees a finite crossing of the
smaller threshold; no attainment of the supremum is required.

The pinned contact source explicitly uses first contact including time
zero. Thus

\[
F_L=\sum_{j=0}^{L-1}Q^jB_\epsilon,
\qquad F_L/V=\Pr(\tau<L),
\]

with the same strict inequality and indices as the new note. Positivity
gives `Q^j B_epsilon <= (1+epsilon)D_j`, so a horizon of size
`(log q)^B` costs at most that additional factor in the contact numerator.
Using the density bound with exponent `R+B+2` leaves the numerator
`O(q (log q)^(-R-2))`. Division by the stated spike lower bound
`eta q/log(q+2)` loses one logarithmic power and still leaves a stronger
bound than (22). The spike assumption is retained; neither its
occurrence nor an infinite sequence of such targets is asserted.

## Limits and minor corrections

The note does not replace the finite supremum by `sup_k V_k`.
Fixed-root contact probability tending to one as the horizon tends to
infinity is explicitly distinguished from contact probabilities along
moving roots and their polylogarithmic horizons. The documented
uncontrolled possibility is therefore correctly identified.

Two minor domain clarifications were requested and incorporated before
the reviewed hash was frozen:

- The logarithmic identity involving `W` and the inverse kernel is
  restricted to edges with positive kernel mass, so all logarithms exist.
- The illustrative series involving `log(j^2)` starts at `j>=2`.

Neither clarification changes the new finite-horizon theorem or its
contact-probability corollary.
