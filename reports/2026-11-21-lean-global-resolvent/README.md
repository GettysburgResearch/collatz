# Lean global-attempt checkpoints

## Checkpoint 1

The [scientific guide](../../research/lean-global-resolvent-20261121/README.md) identifies the exact theorem statements and open closing conditions. [checkpoint1-lean.json](checkpoint1-lean.json) records the actual core build and axiom audit, including every compiled source hash. The accompanying logs preserve actual output.

The new proofs establish exact least-failure geometry, source-rank normalization and global equivalences. They do not discharge the closing assertions. Principal dependency reports contain only `propext`, `Classical.choice` and `Quot.sound`.

Repository structural validation is run on the full clean published checkout. Its exact commit, result and receipt are recorded in the pull request. Scientific compilation and repository integrity are different checks; neither an equivalence nor a structural gate is a full convergence proof.
