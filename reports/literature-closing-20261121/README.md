# Literature-closing checkpoint: evidence and replay

**Four new modules compiled; all 69 public theorems passed the combined axiom
audit. Full Collatz remains OPEN.** The proof statements, written extensions,
and remaining hypotheses are in the
[research packet](../../research/literature-closing-20261121/README.md).

## Formal execution

- Lean: **4.34.1**, release commit
  `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib: **d13f23b723b8a846827a245b89c10fc7d3f11612**, with no tracked source
  modifications.
- Every new source compiled with `-j 1 -DwarningAsError=true`.
- All 69 public theorem declarations were printed in one generated audit.
  Their dependencies are subsets of `propext`, `Classical.choice`, and
  `Quot.sound`; one theorem needs no axioms. No `sorryAx`, new custom axiom,
  or `native_decide` certificate is used.

| Module | Public theorems | Formal scope |
|---|---:|---|
| `EntranceRenewal` | 23 | First entrance identities, exceptional odd source cutoff, summability, exact complete atomwise renewal |
| `RetainedTransport` | 7 | Source-weight bounds, marked-step injectivity, finite fresh-return inequality, retained-atom budgets under explicit hypotheses |
| `BandArithmetic` | 14 | Actual affine carries, evaluated local products, positive offset lower bounds, finite-return products, parity/source displacement certificates |
| `MixedBaseNormalForm` | 25 | Actual ordinary rewrite clocks, global normalization, blocked suffix and erasure rank, all-prefix `f11` merger, explicitly conditional closure equivalence |

[`lean-replay.json`](lean-replay.json) is the combined execution receipt.
Each of its four successful individual compiler runs is also preserved under
[`individual/`](individual/). The driver checked exact source, artifact,
arguments, working directory, and import-path equality before reusing those
completed runs. It then executed `LiteratureAudit.lean` against all four
actual compiled modules. A reuse record is not represented as a second
compiler execution.

[`dependency-replay.json`](dependency-replay.json) binds the seven required
prior modules and their audit to this replay. Those unchanged dependencies
were rebuilt after the earlier runtime artifacts were no longer present.
The receipt records a stopped pending dependency invocation and the explicit
path-based resumption; all eight listed final commands exited successfully.
This rebuild supplies imports for the new proofs, not a new mathematical
review of the earlier research.

The initial new-source compiles exposed local elaboration or linter issues.
The corrections made a parity simplification explicit, instantiated two
implicit lengths, corrected local decidability and context-association
proofs, replaced deprecated tactic names, and repaired the infinite-sum
proof's function reduction and zero-sum invocation. All final source hashes
are bound by the successful receipts. The later `terminal_double_one_merger`
is a separately identified constructive addition.

## Written mathematics and finite execution

The following are written mathematical results, rather than extra theorems
included in the 69-declaration formal count:

- The accelerated inverse-branch constant eight, the resulting infinite
  measure inequality, its exceptional total-mass bound, the critical
  logarithmic transport envelope, and the shift sharpness example.
- AR-4 and AR-5's all-parameter ordinary marked-return constructions, the
  interpretation of the displayed local factors as local norms, and the
  coupled-remainder calculations.
- The complete mixed-base normal-form grammar and the extension from the
  formal `f11` case to every odd-length terminal string of ternary ones.

Narrow independent reconstruction is recorded in the packet's
[`arithmetic/REVIEW_TRANSPORT.md`](../../research/literature-closing-20261121/arithmetic/REVIEW_TRANSPORT.md),
[`mergers/ARITHMETIC_REVIEW.md`](../../research/literature-closing-20261121/mergers/ARITHMETIC_REVIEW.md),
and [`mergers/INDEPENDENT_MERGER_REVIEW.md`](../../research/literature-closing-20261121/mergers/INDEPENDENT_MERGER_REVIEW.md).
Each review retains its exact source and claim boundary. Later proof-only
compiler repairs are certified by the final formal replay; editorial
coverage notes do not extend the scope of a mathematical review.

The exact arithmetic regression passed on 16,384 actual odd prefixes,
4,591 periodic-shadow break depths, 18,396 preperiod identities, 1,023 marked
parity lifts, 350 AR-4 close returns, and 230 AR-5 marked triples. The last
family includes 3,447-bit ordinary sources. The mixed-base executable checked
ten global affine rule certificates and five finite exact ordinary traces;
its root replay reproduced the stored report byte-for-byte. The root
execution metadata are in [`finite-execution.json`](finite-execution.json).
These finite checks corroborate their specified implementations and do not
constitute a universal convergence computation.

## Repository checkpoints

The first literature checkpoint was pushed as
`cc046e189366e7e876fc283b80459e64faa9c486`, with the new Lean status explicitly
pending. Its clean complete-checkout validation passed all five required
commands and left the checkout unchanged; the full receipt is
[`checkpoint1-validation.json`](checkpoint1-validation.json).

The checked proof checkpoint and its clean complete-checkout receipt will be
recorded in a follow-up receipt commit. The latest exact-head gate is stated
in PR 183 after remote readback. Source binding to the formal replay is
checked again before the final publication; an integrity gate is not a
mathematical proof.

## Global boundary

The actual repeated-return domination estimate and cycle exclusion are not
established. `BlockedErasureCover` is an explicit hypothesis, not a custom
axiom or an unconditional theorem. Neither rank decrease nor proximity to a
power of two is promoted to a universal ordinary merger. The final public
claims remain those stated in the research packet and its four Lean files.
