# Retained-source collision: direct pressure comparison

**Status, 23 November 2026: escape and full Collatz remain OPEN.**

The [direct attack](PRESSURE_COLLISION_ATTACK.md) combines the newest
critical collision lower bound in PR185 with PR177's exact ordinary atomic
pressure measure. It proves an arithmetic off-diagonal collision upper
for the pressure measure and then retains the actual density needed to
transfer that estimate to the requested inverse endpoint law.

The density grows at every inverse clock. Every `L^p` norm with `p>1`
diverges at least polynomially in the time-window length, and the relative
entropy costs at least `(s-1) log(M+1)` asymptotically. Using the new
critical running-height theorem, the literal global-density comparison is
quantitatively incapable of producing the desired critical upper bound at
any usable precision. A sharper comparison uses only one density factor;
the critical square-root gain still forces a growing logarithmic loss,
uniformly even if the pressure exponent is tuned toward one as the window
grows. The coordinating root agent contributed this sharpening, independently
reconstructed in the lane and its review. This excludes that specific transfer argument;
it does not lower-bound the actual off-diagonal collisions or exclude a
nonuniform bilinear approach.

The alternative repetition attack is checked on the same ordinary source:
425 and 911 occur on the orbit from 41, are equal modulo 81, and have
different four-gap past words with totals below `4 log_2 3`. Thus residue
collisions cannot be silently converted into repeated gap words. A genuine
consecutive repetition does obey the exact original-source divisibility
`2^(kA) | ((2^A-3^m)x-B)`, proved in Lean.

## Evidence

- [Frozen sources](SOURCES.json): full peer heads, source paths and Git blobs.
- [Finite Lean core](lean/PressureCollisionCore.lean): ten public theorems.
- [Axiom audit](lean/PressureCollisionAudit.lean).
- [Compiler receipt](../../../reports/2026-11-23-global-closure/escape-lean-build.json)
  and [actual audit output](../../../reports/2026-11-23-global-closure/escape-lean-audit.log).

Both Lean modules compiled with Lean 4.34.1, Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`, `autoImplicit=false`, and
warnings treated as errors. Their only axiom dependencies are the usual
`propext`, `Classical.choice`, and `Quot.sound`. The analytic pressure
and asymptotic deductions are written proofs, not Lean declarations.

To reproduce the focused compilation, place the local proof output
directory, Mathlib's `.lake/build/lib/lean`, and its package build
directories on `LEAN_PATH`. Compile `PressureCollisionCore.lean` into that
output directory, then `PressureCollisionAudit.lean`, with the strict
options recorded in the receipt. No historic Lean corpus or new cycle
census is required for this packet.
