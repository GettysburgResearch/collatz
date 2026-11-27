# Third checkpoint execution evidence

This archive records the source-frozen third research checkpoint. It is process
and bounded-verification evidence, not a proof of the Collatz conjecture.

- Local validated commit: `3b39cd46a32d92b86218dc5041ab8f08e14fe4df`.
- Published science commit: `6a22fb0404b1a8cd6d51a0924a800563851d5788`.
- Identical science tree: `36a1286976527717e7d9c5949f7064f5e96c5b4e`.
- Science parent: `7bf3e4b845582eb1e732b0dea8604ffcf159eef9`.

The source manifest records all 46 changed science paths and their Git modes,
blob identities, byte counts, and SHA-256 digests. This archive is committed
separately so no receipt claims to hash the commit that contains itself.

## What passed

`LEAN_REPLAY.json` records a fresh build of all 21 requested local dependency
modules, including 14 new modules. Lean was 4.34.1; the primary Mathlib source
was pinned at `d13f23b723b8a846827a245b89c10fc7d3f11612`. The driver combined
pinned dependency caches by symlink, excluding local module outputs from its
supplement. Every local module was rebuilt in a temporary output directory
with one worker, automatic implicit variables disabled, warnings as errors,
and asynchronous elaboration disabled. All source hashes remained unchanged.
Printed public axiom inventories were subsets of `propext`, `Classical.choice`,
and `Quot.sound`. The three checkpoints have rebuilt 42 distinct local modules.

`FINITE_REPLAY.json` records nine programs in normal and optimized Python,
with identical outputs. Four check finite identities or retained fixtures;
two check scaled residue counts and compare the selector against direct
integer inverse search. Three enumerate automaton states or tower data and
are recorded as finite calculations, not universal proof certificates.
Assertions in the two scaled programs were replaced by explicit checks before
this replay, so optimized mode retains their substantive comparisons.

`LOCAL_REGRESSIONS.json` and `PUBLISHED_REGRESSIONS.json` each record a complete
clean-checkout validator run with the repository's eleven enumerated commands.
Both passed. Those checks concern repository structure, preserved identities,
and their selected bounded old regressions; they do not certify new mathematics.
`DESCENT_AUTHOR_REPLAY.txt` retains the lane's earlier strict compilation output
separately from the root's fresh independent rebuild.

## Mathematical boundary

The finite selector decides an ordinary bounded-odd-budget question at every
lower clock, under its explicit source-height hypothesis. It does not prove
that every source eventually has a smaller visitor. The source-height and
whole-denominator analytic arguments import the stated Diophantine theorems;
those external proofs were not rebuilt. The clock estimate uses ambient
ordinary-prefix normalization. The bounded-piece decomposition and fixed
complexity assumptions are not asserted for arbitrary trajectories.

See [THIRD_CHECKPOINT.md](../../../research/astra-reciprocal-rigidity-20261127/THIRD_CHECKPOINT.md)
for the exact results, prior credit, and remaining obligations.
