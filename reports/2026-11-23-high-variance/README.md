# High-variance checkpoint: actual execution and review scope

Date: 23 November 2026. [Scientific packet](../../research/high-variance-20261123/README.md).
Full Collatz remains open. Execution timestamps inside JSON receipts are UTC.

## Fresh finite Lean replay

[LEAN_RECEIPT.json](LEAN_RECEIPT.json) records sequential fresh compilation of
both new modules and a generated exhaustive 24-theorem audit. All commands
used -j1 and warningAsError=true. Lean 4.34.1 is pinned to compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`; Mathlib is tracked-clean at
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

Only installed Mathlib dependency objects were reused; neither a Mathlib
source rebuild nor a replay of the older PR182 proof packet is claimed.
The new project output directory was initially empty. All proof-source
hashes agree before and after the replay. The final receipt reflects the
clarified generic Edge documentation in ForcedRoute, not earlier draft bytes.

[AXIOM_AUDIT.json](AXIOM_AUDIT.json) and the generated
[HighVarianceAudit.lean](HighVarianceAudit.lean) cover all 24 public theorem
statements. Each dependency closure uses only a subset of propext,
Classical.choice and Quot.sound. No sorryAx or custom Collatz axiom occurs.
The finite formalization boundary is stated next to each scientific claim.

## Exact arithmetic controls

[EXACT_RECEIPT.json](EXACT_RECEIPT.json) binds the actual normal and optimized
executions to the same unchanged checker bytes. The complete results are
[CYCLE_CONTROLS.json](CYCLE_CONTROLS.json) and
[CYCLE_CONTROLS_OPTIMIZED.json](CYCLE_CONTROLS_OPTIMIZED.json).
Both runs check four complete constructions and reject four deliberately
damaged inputs. Every rational parity step and every finite ordinary witness
step is replayed. KMP primitivity and exact complete carries/denominators are
checked independently of the construction's marker proof.

[SECOND_SELECTOR_CONTROL.json](SECOND_SELECTOR_CONTROL.json) records root's
additional exact k=2 control using the same final checker source.
[CYCLE_INDEPENDENT_CONTROLS.json](CYCLE_INDEPENDENT_CONTROLS.json) records
the reviewer's separate Fraction-based rational replay on four controls.
These are finite executions; the arbitrary-modulus theorem and its infinite
height subsequence are written proofs.

## Semantic reconstruction

[CYCLE_REVIEW.md](CYCLE_REVIEW.md) reconstructs the complete written cycle
argument and checks the finite module and checker. It explicitly discloses
the reviewer's contribution to the amplification strengthening. The initial
all-modulus construction was reconstructed independently, and another agent
also reconstructed its base arithmetic and height proof.

[REVIEW_CYCLE_WORD_ALGEBRA.md](REVIEW_CYCLE_WORD_ALGEBRA.md) separately reviews
root's finite implementation against the chronological complete-word
convention. The reviewer authored the written construction and discloses
that contribution. These are scoped internal reviews, not external peer review.

[SEMANTIC_REVIEW.md](SEMANTIC_REVIEW.md) collects the final route proof and
normal-label control reviews, including the generic Edge interface
qualification. Source hashes and execution bindings are recorded in
[SOURCE_BINDING.json](SOURCE_BINDING.json).

## Checkout and publication

[CHECKOUT_VALIDATION.json](CHECKOUT_VALIDATION.json) is the actual default
five-command integrity gate on the clean complete scientific checkpoint.
It is an execution, not an API-tree inspection or mathematical proof check.
The receipt is added in a report-only follow-up; its checked source commit
is identified inside the receipt. The same gate is run on the final published
commit, whose exact receipt is preserved in PR182's description after readback.

The optional historical bounded-regression bundle was not rerun: the new
proof and explicit arithmetic risks were tested by the commands above.
The previous published PR description, including its own historical
execution evidence, is preserved verbatim as structured metadata in
[PR182_BEFORE.json](PR182_BEFORE.json).
