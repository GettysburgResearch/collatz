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

The complete-checkout integrity and regression gate will be run on the first
published checkpoint. Its receipt will be added in a subsequent checkpoint.
A passing repository gate checks the repository's declared integrity and
bounded regressions; it does not prove universal Collatz convergence.
