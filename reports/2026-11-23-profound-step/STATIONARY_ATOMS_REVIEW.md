# Independent review of stationary atoms and finite periodization

Reviewer: `arithmetic_minimum` subagent. Date: 2026-11-23.

Target: `research/profound-step-20261123/STATIONARY_REAL.md`, Sections 5–6.

Frozen target SHA-256:
`0e2d6b1a718e46d5baf1acc60c1aebadc43826e642c8d2601e9b8c947479bad4`.
This hash was independently recomputed before review.

**Finding: no gap found within the stated scope.** The review checks the
written rational-atom classification and finite actual-word inequalities;
it does not claim a Lean verification, a historical dependency audit, or
complete Collatz closure.

## Section 5: recurrent atoms

The reversed-past affine identity has the correct orientation:

\[
z_0=\sum_{i=1}^h3^{i-1}2^{-A_i}+3^h2^{-A}z_h.
\]

A return to the same atom therefore gives exactly the displayed
\(C/(2^A-3^h)\). Positive gaps imply that the last summand of \(C\)
is odd and all earlier ones are even. Its first summand is a ternary
unit and all later ones are divisible by three. Thus the return identity
does establish that each atom is rational and both a 2-adic and ternary
unit.

The event of belonging to the countable atomic set is forward invariant
modulo null sets, using the conditional positive probability of a gap
and the deterministic affine update. Stationarity makes it invariant
modulo null sets. On that event, \(U(z\circ S)=z\), so the finite
atomic factor measure is invariant under the deterministic rational map
\(U\). Poincaré recurrence to each positive-mass singleton forces its
state to be periodic. A periodic predecessor of a periodic state must
belong to that same cycle, and the preceding cyclic vertex is unique.
Hence the atomic component has the repeated cycle gaps and uniform
phase weights. The conditional mean is \(A/h\), with the sign and
strict comparison to \(\log_2 3\) supplied by the same full affine
denominator.

## Section 6: finite word and its seam

For a backward word beginning at phase \(j\), the centered sum is
exactly \(B_j-B_{j-k}\), with the bridge periodically extended.
It is bounded by \(V_N\). Since \(d_N\ge0\), the maximum of the
uncentered sums through length \(m+1\) is at most
\((m+1)d_N+V_N\). Also \(L_1=d_N-\log3\); this gives the exact
cancellation in the displayed bound preceding (18).

For \(1\le m\le N\), the phases avoiding the artificial seam are
precisely \(j=m,\ldots,N\). Equation (19) correctly keeps denominator
\(N\): its counted phases are a subset of the uniform auxiliary phase
sample, rather than a newly normalized distribution. There are \(m-1\)
seam phases among \(1,\ldots,N\). Equation (21) discards \(m\)
clocks because its original time sample additionally includes \(j=0\).
The reversed affine remainder in (20) has the correct sign and moving
ordinary endpoint height.

No edits to the target were requested by this review. The source's
separation between nonatomicity and a collision exponent, and between
the moving bound \(q_j\) and a fixed real tightness bound, is retained.
