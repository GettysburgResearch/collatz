# Independent review: the infinite Lean probability bridge

Date: 2026-11-23. Reviewer: root agent, independent of the module author.

Source: `research/source-clock-20261123/lean/BoundaryBorelCantelli.lean`.

SHA256: `e4825c20e2c5c2d5d2b8d0bc1d3a5a4402cc4ce648a5812bea88f404126e68f4`.

**VERIFIED for the declared conditional measure-theoretic statements.**
The module invokes Mathlib's first Borel--Cantelli theorem. It does not
assume eventual avoidance of bad events and does not introduce an axiom.
The exact source is also covered by the packet's fresh compilation and
seven-declaration axiom audit.

The first declaration combines almost-sure infinitely many good returns
with the almost-sure eventual avoidance furnished by the finite sum of
outer measures of bad events. No independence or measurability of those
events is needed for this direction of Borel--Cantelli. The second extracts
a strictly increasing subsequence without imposing any return-gap bound.

The third declaration defines its bad event exactly as a good return
whose fixed-reference closed-ball mass exceeds the real power bound.
Avoiding that event at a good return gives the required non-strict upper
bound. Convergence of the radius to zero supplies the eventual smallness
condition; combining it with infinitely many surviving returns produces
a positive good radius below every positive epsilon. The reference real
outer measure is independent of the path law and need not be the boundary
marginal. This matches the arbitrary-reference transfer in the written proof.

The intended Collatz application still has three substantive written inputs:
the summable bad-event estimate from fixed-total packing, the almost-sure
good-return subsequence, and convergence of the actual affine radius.
For the last input, at a fixed nonperiodic root every inverse path has
distinct integer vertices, so its vertices tend to infinity; the exact
identity `a_r X_r <= q` gives `a_r ->0`. None of these Collatz-specific
facts is silently asserted by the abstract Lean declarations.

The written deduction from arbitrarily small power-bounded balls to upper
local dimension, the trace construction, and the information-dimension
extension remain outside this formal scope. The module supplies an actual
infinite probability step, not a formal proof of the full Collatz theorem.
