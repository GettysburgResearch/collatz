# Replaying the least-tower pass

The portable [replay program](replay.py) checks all five new Lean modules and the five unchanged predecessor modules in dependency order. It requires a clean complete checkout and a new output directory outside it. New project `.olean` files are built from the checkout into that empty directory. The toolchain and cached Mathlib dependencies are reused at their pinned versions.

Environment: Lean 4.34.1, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`; Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.

```sh
python -X utf8 -B reports/astra-universal-closure-20261124/replay.py \
  --lean /absolute/path/to/lean-4.34.1-linux/bin/lean \
  --mathlib /absolute/path/to/mathlib \
  --leanpath-file /absolute/path/to/pinned-lean-path.txt \
  --output /absolute/path/to/new-replay-output
```

The program rejects unchecked proof tokens, omitted or duplicate public-theorem audits, unexpected transitive axioms, disappearing Python `assert` checks, differences between normal and optimized Python output, changed science bytes and a dirty source checkout. It runs repository validation with the bounded regression bundle. A zero exit is evidence for those checks, not for any unproved universal statement.

The expected science coverage is 80 public Lean theorem audits: 46 unchanged predecessor theorems and 34 new theorems. There are eight Python control programs, each run in both modes. The all-exponent progression existence, valuation/permutation arguments, cycle-order reductions and external-source discussion remain written mathematical arguments. The replay does not relabel them as kernel-checked proofs.

## Executed clean replay

The remote science commit `ae87464f6fadd2f3db77686c9883ad463198293f`, tree `be2ec250bb23b4debf8de12bf725021701fc522f`, was fetched and checked out completely with 756 tracked files. The replay ran from 18:10:26 to 18:11:17 UTC on 24 November 2026. All ten project modules compiled with warnings as errors and automatic implicit arguments disabled. All 80 public theorem audits passed; their combined transitive axiom set was exactly `propext`, `Classical.choice`, and `Quot.sound`.

All eight Python programs passed in normal and optimized modes with byte-identical outputs and no `assert` nodes. All eleven repository-validator commands, including the bounded regression bundle, exited zero. All 31 research-file hashes remained unchanged, and the checkout stayed clean at the same commit and tree. No prior project object file was reused.

[Machine receipt](fresh_replay/receipt.json), [repository validation receipt](fresh_replay/repository-validation.json), and the adjacent stdout/stderr logs record the actual commands and outcomes. [Publication record](PUBLICATION.json) pins the science commit and every research hash. The follow-up publication adds reports only; its clean checkout is checked against these hashes before the branch moves. The exact published head is reported in the PR and session.
