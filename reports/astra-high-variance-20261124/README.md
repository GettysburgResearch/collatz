# Execution record: unrestricted closing attempts and ordinary comparisons

This report accompanies the [research packet](../../research/astra-high-variance-20261124/README.md).
Collatz remains open. The universal closing attempts, written infinite arguments,
Lean results, finite arithmetic certificates and repository integrity have separate scopes.

The source checkpoint includes [replay.py](replay.py), which compiles every new
Std-only module into a fresh output directory, records each printed theorem's
transitive axioms, and runs each arithmetic control in ordinary and optimized
Python. It then runs the required complete-checkout repository validator.
The replay refuses a dirty source checkout, source mutation, missing audits,
unexpected axioms, optimized-away assertions, or differing paired outputs.

The execution receipt and exact outcome will be added after replay of the clean
published source checkpoint. This initial report is a reproduction specification,
not a claim that the integrating replay has already run.

Use Lean 4.34.1, one worker, and warnings as errors. Every new Lean module imports
only Std; no Mathlib or unchanged earlier project module is needed. Choose an
output directory outside the repository that does not yet exist:

```sh
python -X utf8 -B reports/astra-high-variance-20261124/replay.py \
  --lean /absolute/path/to/lean \
  --output /absolute/path/to/new-output-directory
```

Fresh object identities, source SHA-256 values, stdout/stderr logs, command exit
codes and normal/optimized comparisons are execution evidence. They do not prove
the written analytic estimates or supply any missing universal descent premise.
