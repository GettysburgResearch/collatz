# Final tests of three proposed closing arguments

**Collatz remains OPEN.** These written results were developed in the last
research window after the main [formal packet](../unconventional/README.md)
was frozen and published. They add no Lean theorem and do not change its
95-module, 403-declaration build. Their role is to test precise proposed
ways of turning that progress into a universal proof.

## 1. One actual root can defeat growing-clock comparisons

[APERIODIC_HORIZONS.md](APERIODIC_HORIZONS.md) constructs the ordinary root
`2^128-1`, with zero digits at depths `128,256,512,...` and ones elsewhere.
At all pairs of depths `i,j`, its opposite endpoints cannot meet within
respective physical clocks `floor((128+i)/128)` and
`floor((128+j)/128)`. Every word containing zero has no third consecutive
copy on this address. This is an infinite written theorem about actual
ordinary integers on one fixed root. The address is not asserted to be an
actual basin-color wall; longer physical clocks remain available. Choosing
even N in the general construction also keeps all zero positions on the
same parity. A separate construction handles any fixed horizon and bounds
powers of every word, with the root depending on that horizon. Qualitative
power caps do not imply all the particular numerical caps of the main packet.

## 2. Fixed-source arithmetic compactness is valid but still needs every digit

[FIXED_POOL.md](FIXED_POOL.md) proves that leastness makes the saturation
of the finite cheap-source pool finite. A prepeak query exists exactly
when that same pool meets a target phase modulo `3^d` at every depth `d`.
The witnesses may change with d; the parent and cheap pool may not.
First-return excursions give a complete decision with unrestricted clocks.
The empty-pool case is immediate; maxima over the saturation are used for
nonempty pools. This supplies an exact local-to-global criterion, without
proving its pointwise premise on every residual parent.

Two fully enumerated nearby ordinary families pass through 26 and 22
ternary digits, respectively, and fail at the next digit despite more than
50 million cheap starts. One changes the original exponent class, the
other its cofactor. Neither is a remaining e6 defect. The fixed pool through
53,024,287 visits exactly the 350 pure Mersenne ascent labels with exponents
1 through 25. The much larger actual budgets for e6 parameters are not
exhausted by that computation.

## 3. Subcritical gains do not annihilate supercritical exit mass

[MOMENT_INTERPOLATION.md](MOMENT_INTERPOLATION.md) gives the exact common
component partition for the two sums. The initial source contributes a
positive mass that the fresh-branch maximum bound does not remove. An
explicit sparse modification of the integer map retains both moment
estimates, usual slopes, uniform interval compression, branching and any
prescribed finite initial cutoff, while an explicit component escapes.
It changes odd additive constants from 1 to 7 at specified sites; it is
not a counterexample to Collatz. Complete gate support at every cutoff
recovers the original odd edges and distinguishes this model. A successful
use of that support requires an additional arithmetic argument.

## Evidence

The coordinator reconstructed the three written proofs and ran the
standalone finite controls. The original 95-module Lean build remains the
formal boundary. [Review and executions](../../../reports/ayh-resource-reset-20261124/bridge-tests-20261126/README.md)
records the independent replays and the external computational input used
only for the stronger leastness interpretation of the two nearby controls.
