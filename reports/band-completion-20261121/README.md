# Band completion checkpoint: execution record

This report records execution evidence for
[the scientific packet](../../research/band-completion-20261121/README.md).
Full Collatz remains open. These checks apply to the encoded conditional
certificates, exact ordinary obstruction families, and entrance estimates.

## Complete Lean replay

The root replay compiled all four pinned upstream modules, all three new
modules, and the generated audit module in a separate output directory.
**All eight compiler commands passed with warnings treated as errors.**
The audit printed all **43 public theorems** in the three new modules; their
axiom dependencies are subsets of `propext`, `Classical.choice`, and
`Quot.sound`. The source contains no admitted proofs or custom axioms.

The full command records, source and generated-input SHA-256 digests, binary
artifact digests, elapsed times, and actual output are in
[`lean-replay.json`](lean-replay.json). The replay used Lean 4.34.1 and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`; the Mathlib tracked source tree was
clean. Its dependency cache was reused, while every listed Collatz module was
compiled from its recorded source.

The three local development outputs are also retained here. They precede the
complete root replay and do not add further theorem coverage.

## Exact source boundary

PR 173 is frozen at `fa0c9e2a2851e6324391e39c17afcb5913185aec`.
The four original files under `lean/vendor` remain byte-identical to the source
pin and are authenticated by `upstream-files.json`. The replay generates the
supported `module`, `public import`, and `@[expose] public section` headers.
It gives public visibility to `GridAt`, its decidability instance, and
`visit_exists`, which exposed definitions name. No formula, hypothesis,
or proof body of the upstream development is changed.

The mass note additionally uses the primitive-survivor decomposition in
PR 176 at `ad9a0611d22b48c0fd0c1da31091179654ba31a9` as a source-qualified
input to an ordinary mathematical corollary. PR 176 is not imported by these
Lean files and was not recompiled in this replay. The note explicitly labels
its infinite-packet formulas, cutoff estimate, primitive-mass coupling, and
other unformalized calculations. They are not among the 43 audited theorems.

The replay occurred before the first publication commit. Its source hashes
bind the tested proof files to the later published tree; this report does not
claim that the prepublication working tree was a clean commit checkout.

## Repository validation

The complete-checkout integrity and regression gate **passed all 11 child
commands** at published checkpoint
`59dfcfc48f0db641b7b66d3ead64a11d060737ae`, tree
`f501b2cbf9322f3c271930173fcf9f606e257907`. The clean, complete checkout
remained unchanged after execution. The exact receipt is
[`checkpoint1-repository-validation.json`](checkpoint1-repository-validation.json).

The checked proof sources in that published checkout were also hashed against
the successful Lean replay; all three source digests matched. The subsequent
checkpoint adds this receipt and updates documentation, with no Lean source
changes. A final-head repository replay is reported in the PR description
without recursively committing a receipt for its own commit.

This repository gate checks declared integrity and bounded regressions; it
does not prove universal Collatz convergence.

## Focused mathematical cross-check

A separate route agent reconstructed the unbounded successful offset family,
the outer-band obstruction, and the never-entered mass bound and primitive
coupling. No constant, quantifier, or clock error was found in those claims.
The suggested wording was tightened to say an unbounded family of scales and
non-strict survival through clock zero. This focused check does not certify
the missing global return or absorption estimate.
