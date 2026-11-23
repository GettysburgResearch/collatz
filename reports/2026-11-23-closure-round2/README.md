# Verification report for the second closing-attempt checkpoint

The scientific entry point is
[the closing-attempt packet](../../research/closure-round2-20261123/README.md).
Full Collatz, unrestricted cycle exclusion, and exclusion of escaping ordinary
components remain open. This directory records actual executions and scoped
internal reviews.

## Formal proof boundary

| Module | New public statements | Scope |
|---|---:|---|
| `CycleCancellation.lean` | 6 | Complete moving-letter carry identity, derived denominator coprimalities, and full numerical gcd transport |
| `TwoSidedPressure.lean` | 12 | Attainment from explicit positive bounded weights; exact ordinary path balance; one common root for all supplied forward and incoming unit paths; finite consequences |

The new modules and their unchanged local carry dependency were freshly
compiled with Lean 4.34.1, compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. All four commands exited zero
with warnings treated as errors. The [receipt](LEAN_RECEIPT.json) records
the full commands, timestamps, final source hashes and all axiom output.
[RoundTwoAudit.lean](RoundTwoAudit.lean) audits every new public statement.
Only `propext`, `Classical.choice` and `Quot.sound` occur.

The infinite escaping-orbit product, its positivity and floor bound, the
cycle-neighborhood and window injections, and the infinite measure arguments
remain written mathematics. The Lean statements do not assume a Collatz
completion or install an analytic conjecture as an axiom.

## Exact replay boundary

[EXACT_RECEIPT.json](EXACT_RECEIPT.json) records four successful Python
commands: normal and optimized runs of each checker, with identical JSON
results in the two modes.

- [Cycle controls](CYCLE_CONTROLS.json) retain the literal full denominator,
  known positive cycle repetitions, the denominator-one case, and an explicitly
  abstract longer-displacement modulus. A forged denominator of one passes
  unit and zero-residue checks but is rejected by the full-denominator guard.
- [Combined exact controls](EXACT_CONTROLS.json) include 6,411 complete words
  through length twelve, 31,865 moving-letter identities, 16,561 adjacent
  disjoint-gcd checks, 6,065 cyclic-cut separation checks, and 198 cyclic
  window injections. The pressure replay retains endpoint collisions and
  repeated visits at a periodic root; deleting the latter is detected.
- The finite source control follows `7 -> 11 -> 17 -> 13 -> 5`: three
  supercritical forward prefixes do not make the fourth supercritical.
  It is not presented as an infinite pressure maximizer.

These are bounded exact controls. No finite search is promoted to absence of
all positive cycles or all escaping orbits.

## Reviews and contributions

- [Cycle finite-algebra review](CYCLE_ALGEBRA_REVIEW.md): the escape researcher
  independently reconstructed the six new declarations and their imported
  chronological convention.
- [Common-root review](SOURCE_MAXIMUM_REVIEW.md): the escape researcher
  independently reconstructed the twelve declarations and the written
  infinite-product application, including the unit-domain restriction.
- [Pressure review](CYCLE_AGENT_PRESSURE_REVIEW.md): the cycle researcher
  independently reconstructed the ordinary residual decomposition, rational
  pole budget, periodic-root sum, Haar calculation and retained-source limit.
- [Principal review](ROOT_REVIEW.md): mathematical reconstruction, source
  checks, contribution disclosures and fresh execution scope.

Review verdicts bind the specific hashes printed in the reports. These are
internal reviews, not claims of external peer review or formal verification
of every written infinite argument. The principal researcher supplied the
ordinary reference/loss identity and the combined exact replay; independent
pressure reconstruction is credited separately above.

## Complete-checkout integrity and source binding

The five required commands in `tools/validate.py` passed in the clean complete
science checkout at commit `83504cbbe91a78dde0bc9537eeb33894649feeae`, tree
`04f7a32e157146149e3240ca50839d1217ad400c`, with 461 tracked files.
[CHECKOUT_VALIDATION.json](CHECKOUT_VALIDATION.json) is the actual receipt,
written outside that checkout and added afterward. These checks verify
repository structure and specified bounded controls, not the Collatz theorem.

[SOURCE_BINDING.json](SOURCE_BINDING.json) binds the final science, compiler
receipts and reviews to the checked bytes. It also checks every pre-existing
tracked Lean file against the preceding published checkpoint. The subsequent
receipt commit changes only verification material. The eventual remote commit
has the same final tree; its exact-head readback and final complete-checkout
validation are reported in the pull request.
