# Execution and review record: dyadic marked descents

Scientific entry: [arbitrarily strong marked descents](../../research/lean-dyadic-descent-20261121/README.md).

## Scope and publication

PR182 is stacked on PR173 at
`fa0c9e2a2851e6324391e39c17afcb5913185aec`. Checkpoint 1 is
`cd3d4f3acad8b43ea07af764f28662f0eca7634e`, tree
`2cbf2753efe39cede61ece3ed8bd8626080a06e4`.

The new result is an unconditional family of arbitrarily strong actual
marked-return contractions from suitable inputs `2^d+1`, and the analogous
result for each fixed certified odd offset. It is not universal marked-return
descent and does not prove full Collatz.

## Actual Lean execution

[LEAN_RECEIPT.json](LEAN_RECEIPT.json) records a fresh sequential build in an
empty output directory. All seven modules passed with Lean 4.34.1,
`-j1 -DwarningAsError=true`, and mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`:

1. Imported, byte-pinned `ShellCover.lean`.
2. Imported, byte-pinned `ForwardSection.lean`.
3. Imported, byte-pinned `SectionDynamics.lean`.
4. New `OffsetDescent.lean`.
5. New `MarkedOffsetReturn.lean`.
6. New `PhaseFrequency.lean`.
7. New `InfiniteDescent.lean`.

The imported sources are credited to PR173. All seven source hashes stayed
unchanged during the build and were checked again when these receipts were
recorded. This is an actual proof-file compilation, not merely inspection of
another session's compilation report.

[AXIOM_AUDIT.json](AXIOM_AUDIT.json) records a separate whitelist scan of every
printed principal axiom closure in those compiler outputs. All are subsets
of `propext`, `Classical.choice`, and `Quot.sound`. No `sorryAx`, custom
convergence axiom, or native reduction trust mechanism appears in them.
The precise theorem types preserve all conditional premises.

The reproducible [build script](../../research/lean-dyadic-descent-20261121/replay.py)
also enforces that whitelist for subsequent runs. Source files and toolchain
pins are in the scientific directory; generated binaries are not committed.

## Independent mathematical review

- [REVIEW_OFFSET.md](REVIEW_OFFSET.md) independently reconstructs the exact
  quotient threshold, natural-subtraction boundaries, marked endpoint guards,
  terminal-cycle clocks, and the three overlapping exponent windows.
- [REVIEW.md](../../research/lean-dyadic-descent-20261121/REVIEW.md) independently
  reconstructs the one-sided approximation and infinite-family proof, the
  Fourier cancellation and the low-bit bound. It discloses the reviewer's
  authorship of the imported marked-endpoint helper.

Both records pin the inspected source bytes. They are mathematical review
records, not additional claims of independent compiler runs.

## Repository integrity

[CHECKPOINT1_VALIDATION.json](CHECKPOINT1_VALIDATION.json) records the actual
clean, complete checkout at the first published commit. All five commands in
`python -X utf8 -B tools/validate.py` passed, and the checkout remained clean
with the same commit, tree and 328 tracked files.

The final published scientific commit is validated separately after
publication, with its exact receipt attached to PR182. The first-checkpoint
receipt does not claim to validate its descendants. Repository integrity and
its small built-in replay fixtures do not establish mathematical convergence.
The optional historical regression bundle was not rerun.

## Mathematical boundary retained

The infinite theorem fixes a certified offset, then selects suitable dyadic
exponents. Its proof does not work at every prescribed exponent or transfer
nonconvergence from an arbitrary marked point to a selected lift. The phase
theorem does not supply low-bit uniformity and does not cover a bounded
nontrivial cycle. These are explicit limits of the current completion attempt.
