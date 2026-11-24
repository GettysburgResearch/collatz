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

The publication receipt and fresh replay logs are added after the remote science commit has been fetched and replayed in a clean complete checkout. Their exact commits, timestamps, command exits and source hashes are authoritative for what was actually executed.
