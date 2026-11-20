# Actual scientific-commit validation

The real GitHub scientific commit was fetched into a complete clean
checkout before these executions:

- Commit: `72566fabe6f6525fbdec3efbe1a588477270f8a0`
- Tree: `6efa52ec034438f30c21805ca59e8d4d2cc6e021`
- Parent: `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`
- Complete tracked file count: 346.

The local scientific tree and the uploaded tree were compared exactly.
No pre-publication workspace receipt is substituted for a fetched-commit
execution.

## Scientific replay

[scientific-replay-receipt.json](scientific-replay-receipt.json) records:

- All 30 content-manifest entries matched their byte counts and SHA-256
  hashes.
- All three compressed exploratory reports decompressed to their frozen
  raw hashes, and their selected count fields matched the summary.
- All six scientific programs passed normally and with `-OO`: 12 actual
  successful executions.
- Every output matched its frozen JSON report byte for byte.
- The commit, tree and completely clean worktree state were unchanged
  before and after execution.

These programs replay exact finite arithmetic and controls. The author
and reviewer implementations for the ladder and GRH interface are
separate. The renewal theorem is supported by its written proof,
independent proof review and exact finite rational checks. No external
GRH theorem or S-unit theorem is proved by these programs.

## Complete repository validation

[checkout-validation-receipt.json](checkout-validation-receipt.json)
records all eleven commands in `tools/validate.py --regressions` passing
on the same commit and tree, with the same complete 346-file checkout
after execution. These are repository integrity and selected bounded
regressions, not mathematical verification of the full conjecture.

## Documentation child and final read-back

These receipts and this record are appended in a documentation-only
child of the tested scientific commit. Its changes are restricted to
four paths under `reports/2026-11-20-grh-closure/`: this file, the two
receipts, and the guide's publication link. All 30 scientific manifest
entries are preserved byte for byte.

The final remote PR head and its fetched tree are reported in the PR
description after read-back. The final child is checked separately for
its parent, four-path metadata-only difference, complete clean checkout,
all scientific hashes and relative Markdown links. The twelve scientific
executions and eleven-command gate above are attributed to their actual
scientific parent, not retroactively to this child.

The result remains a proposed research contribution. Internal AI review,
an exact finite replay and a clean repository gate are different types
of evidence. None is human referee acceptance, a Lean build, or a proof
of full Collatz convergence.
