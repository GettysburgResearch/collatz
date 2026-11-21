# Verification record: forced bands and ordinary mergers

The scientific statement and remaining open obligation are in
`research/lean-band-coupling-20261121/README.md`.

## Local source-packet execution

On 2026-11-21 the complete twelve-module packet was built with Lean 4.34.1
(commit `5045d0056413266e57c625dcd7c365b10e377c52`) and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

Command:

```sh
python -X utf8 -B research/lean-band-coupling-20261121/check.py \
  --lean /tmp/collatz-lean-runtime/lean-4.34.1-linux/bin/lean \
  --mathlib /workspace/scratch/957bb0caa6f2/lean-runtime/mathlib4 \
  --build-dir /workspace/scratch/c6766c1207a3/collatz_band_build_20261121
```

Result: all twelve modules exited zero. Every new module was compiled with
`-j1 -DwarningAsError=true`. The final audit printed twenty-four theorem
dependency sets, each contained in `propext`, `Classical.choice`, `Quot.sound`.
The exact source and generated-source hashes, durations and axiom outputs are
in `lean-local-receipt.json`; `axioms-local.log` contains the final printed
audit. `module-port.patch` records the entire explicit header/visibility port.
No definition or proof body in the four frozen upstream files was edited.

The frozen sources were obtained directly with `git show` from PR173 at
`fa0c9e2a2851e6324391e39c17afcb5913185aec`, and the build checked their
SHA256 hashes before preparing the module inputs.

## Scope of finite computation

The reserve experiment uses exact integers and independently replays every
successful witness on both ordinary forward orbits. It reports capped nodes
and exhausted finite menus distinctly. A separate targeted review compared
the original pruning algorithm against unpruned finite inverse trees on
5,133 decompositions with inputs 2 through 256; witness/exhaustion outcomes
agreed. This is a finite algorithm check, not proof of universal coverage.
The final optional partner bound is used consistently in the success test,
depth limit, pruning and exact saving audit; direct-descent endpoint cases
with a larger original-source bound are allowed.

The scientific result remains partial. In particular neither the global
source-bounded merger cover nor the induced-return descent proposition was
proved. No theorem named `Universal` is asserted without such a hypothesis.

Complete-checkout integrity and published-head execution results are recorded
separately after the corresponding real executions. No receipt here is used
as a substitute for an execution at a later commit.

## Published checkpoint 1

Actual remote commit `4beacbee05b5dfd07f8f7b0cdf2a98126cb6d64c`, tree
`9d3f9a35048896d9473b798ebc818f021b134027`, was fetched into a fresh detached
complete checkout. It contained 336 tracked files and was clean before and
after execution. Both required executions passed:

- `python -X utf8 -B tools/validate.py`: all five integrity commands passed.
- Full sequential `check.py` replay: all twelve modules passed again; the
  final twenty-four theorem dependency audits used only the standard axioms.

The exact commit/tree/commands are in `checkpoint-1.json`; the integrity
output is in `checkpoint-1-integrity.log`; every source/generated-source
hash and proof-check result is in `checkpoint-1-lean.json`. These files
record checkpoint 1, not the commit that subsequently stores its receipt.

## Follow-up source-packet execution

The added `LowerMarkedMerger.lean` extends the directed small-endpoint
argument in PR183 to ordinary component mergers and proves the two marked
induction equivalences, with their existence obligations explicit. The
complete thirteen-module packet then passed a fresh sequential replay.
Every new module was warning-free with warnings treated as errors; the
final twenty-seven theorem audits use only the standard logical axioms.

`lean-v2-receipt.json` identifies every checked source and generated source;
`axioms-v2.log` is the final audit output. The related-work note is a targeted
mathematical comparison of frozen PR180/182/183 interfaces, not a blanket
verification of their analytic or formal packages.

The final published-head execution will be recorded in the PR body after
fetching that exact commit, avoiding a self-referential receipt commit.
