# Literature-round proof and execution evidence

**Full Collatz remains open.** The scientific entry point is
[LITERATURE_SYNTHESIS.md](../../../research/lean-dyadic-descent-20261121/LITERATURE_SYNTHESIS.md).
This report separates the new kernel-checked finite results from the
source-qualified written analytic argument and from repository integrity.

## Fresh Lean replay

The actual replay started at `2026-11-22T00:00:41.313348+00:00` and finished
at `2026-11-22T00:01:25.402434+00:00`. All six invocations succeeded:

| Compilation unit | Role | Exit code | Seconds |
|---|---|---:|---:|
| ShellCover.lean | Frozen prerequisite | 0 | 23.409 |
| OffsetDescent.lean | Frozen prerequisite | 0 | 4.074 |
| CertificateBoundary.lean | Frozen prerequisite | 0 | 5.903 |
| AffineRigidity.lean | New finite, algebraic and continuous interfaces | 0 | 3.687 |
| LiteratureCertificate.lean | New complete inverse-prefix and lookahead obstruction | 0 | 4.791 |
| LiteratureAudit.lean | All new public theorem dependency closures | 0 | 2.224 |

The compiler was Lean **4.34.1**, commit
`5045d0056413266e57c625dcd7c365b10e377c52`. Mathlib was the tracked-clean
commit `d13f23b723b8a846827a245b89c10fc7d3f11612`. The runner compiled every
local prerequisite into an initially empty output directory; it reused no
prebuilt local proof module. Mathlib's pinned build cache was used normally.
All invocations used `-j1 -DwarningAsError=true`.

The combined audit covers **26 public statements**: twelve from
`AffineRigidity` and fourteen from `LiteratureCertificate`. Their dependency
closures contain only subsets of `propext`, `Classical.choice`, and
`Quot.sound`. No `sorryAx`, `native_decide`, custom stopping-time axiom, or
external analytic hypothesis supplies any of these statements.

The exact source hashes matched before and after compilation. The
[receipt](LEAN_RECEIPT.json), [complete inventory](AXIOM_AUDIT.json), and
[generated audit source](LiteratureAudit.lean) preserve the actual results.
The runner is
[replay_literature.py](../../../research/lean-dyadic-descent-20261121/replay_literature.py).

The earlier **91 public statements across seven modules** remain unchanged
and retain their original [continuation](../continuation/README.md) and
[reassessment](../reassessment/README.md) receipts. Across these three
checkpoints the combined audit inventory is **117 statements in nine added
modules**, not a claim of 117 novel mathematical theorems or of one fresh
replay of all nine in this round.

## Mathematical scope

The coefficient and forced-band results from the earlier checkpoints are
unchanged. The new certificate theorem quantifies over all finite inserted
prefixes and all initial even runs, with the supplied complete suffix
retained literally. Its bound is sharp and its unbounded witness family is
fully certified. The forward-lookahead obstruction allows the source and
target to change with the proposed horizon. Its explicit suffix has a large
gap; asymmetric common-future mergers and deeper suffix edits remain
outside the excluded strategy.

The affine module proves algebraic, finite and continuous statements on
auxiliary additive groups. It retains genuine additive division, cyclic
generation or dense range, and continuity where needed. It does not
formalize the measurable solenoid proof or manufacture regularity for an
ordinary component label.

The written analytic result and the zero-entropy control have separate
[semantic review records](SEMANTIC_REVIEW.md). Those are independent internal
collaborating-agent reviews, not external peer review or Lean checking.
The earlier FLOOR/LOG inputs remain source-qualified. The stronger
joint-clock natural-density claim is not an input to the new rigidity
argument.

## Repository identity and publication

[SOURCE_BINDING.json](SOURCE_BINDING.json) binds the checked proof inputs,
runner, separately reviewed notes, and complete-checkout receipt.
[CHECKOUT_VALIDATION.json](CHECKOUT_VALIDATION.json) records all five required
repository commands at the clean local scientific commit. The actual
published-head receipt is included in the updated PR description after the
remote write, avoiding a self-referential receipt commit.

These integrity commands do not verify the mathematical results. The
optional regression bundle is not substituted for proof checking and is
not claimed as a new execution in this round.

[PR182_BEFORE.json](PR182_BEFORE.json) preserves the preceding published
description, its exact head `2d478a6588f33a72fc3a5bdc085a928b5cf78737`, and
its actual published-checkout validation receipt.
