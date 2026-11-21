# Final combined attempt at universal closure

**Status: paper deductions and explicitly OPEN implications.** This note
combines the completed Lean results from the band packet and the final
parallel attempts to close the full theorem. It adds no axiom or Lean
proof. The shortcut map is `T(n)=n/2` on even inputs and `(3n+1)/2` on odd
inputs; markedness and positive first returns are exactly PR173's.

## 1. What least-marked induction really supplies

Write

\[
H(m)=4\lfloor\sqrt m\rfloor+\lfloor\log_2m\rfloor,
\qquad G(m)=m\,2^{H(m)}.
\]

Suppose `N` were the least positive marked input whose orbit does not
reach 1. Every smaller marked input would converge. For every positive
ordinary `m` with `G(m)<N`, the bounded-visit theorem supplies a marked
value `T^j(m)` with `j<H(m)`. The elementary orbit bound gives
`T^j(m)<=2^j*m<=G(m)<N`. Hence that marked value, and therefore `m`,
converges.

This repairs the induction interface to a genuine restricted ordinary
floor. It does not supply every smaller ordinary value. If
`d=floor(log2 N)`, the formal bridge guarantees this floor when `6m<d`.
Sharper use of the same `G` reaches a floor of quadratic order in `d`.
The marked offset is permitted to have size as large as
`70*2^d/(d+1)`, an exponentially larger scale.

The first unproved step in this proposed bootstrap is:

> Every permitted offset also reaches a marked point below the original
> `N`, or has another ordinary certificate usable at that same induction
> level.

The bounded-visit theorem supplies a clock bound, not that height
comparison. Let `mu` be the least ordinary value in the forward orbit of
the hypothetical failing `N`. This value exists by well-ordering and is
also a failure. Its next bounded marked visit must be at least `N`, so
the proved estimates give `N<=G(mu)`. Closing through the restricted floor
would require `G(mu)<N`. Repeating the same upper bound does not reverse
this inequality.

The actual binary-window obstruction and the changed quotient multiplier
are worked out in [BAND_DESCENT.md](BAND_DESCENT.md). Supplying convergence
for a smaller source does not by itself transport its certificate to that
new multiplier.

## 2. Temporal sparsity and forced visits are compatible

For an injective odd orbit `x_j`, the new Lean theorem gives zero temporal
density of marked visits. Repeated bounded visits still give infinitely
many marked states. If `q_r` are their odd-step indices, inversion of the
count therefore gives `q_r/r -> infinity`.

At a marked value `m_r=x_(q_r)`, first taking one ordinary step and then
using the forced visit gives an upper bound on the next full-clock gap:

\[
\text{gap}<1+H(T(m_r)).
\]

The odd-clock gap is no larger than this full-clock gap. This upper bound
depends on the height at that return. It is not a uniform bound along an
escaping orbit. For example, on a hypothetical exponentially growing
height scale, this allowed bound itself grows exponentially in the odd
clock, while zero density only requires the mean return gaps to diverge.
These numerical requirements are compatible; this observation does not
construct an ordinary divergent orbit.

Choosing the least value of the forward orbit gives a lower bound on
subsequent heights. It cannot replace their varying heights by that
minimum in an upper bound on the return time. Likewise, resetting the
budget to `H` of each new return does not subtract from one finite initial
budget or define a decreasing well-founded rank.

## 3. The exact remaining integer surplus

For the actual odd orbit, the checked identity is

\[
\log_2x_N-\log_2x_0
=N\log_2 3-A_N+E_N,
\qquad A_N=\sum_{j<N}\nu_2(3x_j+1),
\qquad 0\le E_N\le\sum_{j<N}1/x_j.
\]

On an injective orbit the proved cutoff estimates give `E_N/N -> 0`.
Descent below the original odd input requires an actual prefix with

\[
\boxed{A_N>N\log_2 3+E_N.}
\]

The phase and temporal-frequency theorems do not establish this integer
surplus. Uniform leading phase does not imply the needed law of the
trailing binary digits. The biased invariant law and its arbitrary finite
ordinary realizations are analyzed in [JOINING_ATTEMPT.md](JOINING_ATTEMPT.md).
The start of those finite realizations changes with the horizon, so they
give no ordinary counterexample and no fixed-source exclusion theorem.

Nontrivial cycles require a separate closure argument: the injective-orbit
hypothesis does not hold on a cycle. For an odd period of length `p>0`,
the exact cocycle gives

\[
A-p\log_2 3=E>0,\qquad E\le p/\min_j x_j.
\]

The bounded band visit and finite Fourier estimates are compatible with
these conditions. They do not exclude every positive nontrivial cycle.

## Remaining full-theorem target

The new first-return family discharges the actual descent obligation for
all its parameters. Universal closure still needs a successful ordinary
certificate transport or a sufficiently deep endpoint for **every**
marked residual, or a different global argument that handles both
injective orbits and cycles. None of the unsupported implications above
is imported as a hypothesis into an unconditional Collatz theorem.
