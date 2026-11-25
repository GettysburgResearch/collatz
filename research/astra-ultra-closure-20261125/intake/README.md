# Checked intake of two previously uncompiled candidates

**VERIFIED WITH FIXES, at the formal statement level.** These copies make the indicated finite Lean arguments executable on the project's pinned Lean 4.34.1 and Mathlib revision `d13f23b723b8a846827a245b89c10fc7d3f11612`. They do not establish either source's open analytic or universal premise.

## PR207: eleven unchanged statements and proofs

[DiffusiveRows.lean](DiffusiveRows.lean) comes from PR207 at `b56c4dc2c28a184cf55638bb80c49a9d4662fc81`, path `research/diffusive-central-row-closure-20261124/DiffusiveRows.lean`. The umbrella `import Mathlib` is replaced by three narrow imports available in the pinned dependency cache. Apart from the provenance comment, all eleven statements and proof bodies are unchanged. The original source could not start in this environment because the umbrella `Mathlib.olean` was absent; that initial failure is not evidence of a defect in its proofs.

The checked lemmas concern finite iterates, clock arithmetic, affine carries, gates, and iteration about a fixed point. They do not prove the source-qualified row-count floor, the superdiffusive estimates, their uniformity, or Collatz.

## PR200: six preserved statements, repaired proofs

[MinimumClosure.lean](MinimumClosure.lean) comes from PR200 at `81ea4c1754d73c98d1451447527e6b2ba56977cc`, path `research/regularity-rigidity-20261124/minimum-closure/MinimumClosure.lean`. All six original public theorem headers are preserved. The same import adjustment is followed by these proof repairs:

* Replace `linear_combination`, unavailable under the narrow imports, by multiplication of the given equality and `nlinarith`.
* Adapt the use of `one_le_pow₀` to its pinned Mathlib signature.
* Replace the unsuccessful forward-convergence induction with two explicit helpers, `good_step` and `good_iterate`. The zero-clock case handles the actual `1,2` cycle; the successor case transports the supplied hit using the correct iterate identity.
* Audit every public theorem, including the two helpers and the two original theorems omitted from the original print list.

The final theorem still takes both the minimum principle and universal smaller-multiple descent as explicit hypotheses. Its successful compilation proves the stated implication. It supplies no proof of the descent hypothesis. There is no new project axiom.

## Evidence

Both repaired copies compile with warnings treated as errors and implicit auto-bound variables disabled. Every printed transitive axiom is among `propext`, `Classical.choice`, and `Quot.sound`. See the [independent review](../../../reports/astra-ultra-closure-20261125/core-review.md) and [clean replay](../../../reports/astra-ultra-closure-20261125/VERIFICATION.md) for exact commands and source identities. The source originals remain unchanged at their frozen commits.
