# Validation record

This initial file distinguishes checks already executed during preparation
from the clean-checkout publication receipts, which will be added only
after execution at the published scientific commit.

## Executed during preparation

- Root ran `python -X utf8 -B research/structural-reset-20261120/check_prime_height.py`.
  PASS: 20 deliberately selected seeds, 32 transitions each, 4,560 affine
  pair checks, 5,700 exact local-budget checks, 1,440 exact finite-history
  checks, and nine one-step-predecessor controls. The largest actual
  division exponent in these inputs was 2048. This is a bounded exact
  regression, not a convergence proof or a test of every prime set.
- The component author ran its exact symbolic checker: PASS on all 480
  affine residue cells, with at most nine primitive conditional-law
  applications per reduction. Its optimized entry point was actually
  tested and rejected as intended. The author's adjacent receipt records
  those executions. Publication-checkout replays will have separate receipts.
- Written proof reconstruction and SHA-256 pins are recorded in the
  adjacent root report and the two nonauthor review files. These events
  are not described as formal verification.

No complete-checkout validation is claimed by this preparation record.
The required repository driver will be run after committing these bytes
in a clean, complete worktree, with its receipt written outside that
worktree and preserved in the subsequent publication record.
