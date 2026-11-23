# Verification scope for the literature-driven checkpoint

## Lean replay actually executed

The root researcher ran the packet's fresh-output replay with:

```sh
python research/deep-machinery-20261122/check_lean.py \
  --mathlib /workspace/scratch/46eba7b29f50/lean-runtime-next/mathlib4 \
  --lean /tmp/collatz-180-fast/bin/lean \
  --report-dir reports/2026-11-22-deep-machinery
```

**Result: PASS.** The new `WholeSourceBuffer` module and the separate
`DeepMachineryAudit` module both compiled with warnings treated as errors.
All eight public declarations were audited twice, once in the source
module and once through its compiled import. The printed axiom sets
contain only `propext`, `Classical.choice`, and `Quot.sound`.

The runtime is Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with Mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The two local modules were
built into a fresh temporary directory; the existing pinned Mathlib
objects were reused. No all-library rebuild is claimed. No earlier
repository module was added to this replay.

[Machine-readable receipt](lean-check.json) ·
[Complete build and axiom log](lean-build.log) ·
[Declaration inventory](../../research/deep-machinery-20261122/THEOREMS.json) ·
[Pinned replay configuration](../../research/deep-machinery-20261122/DEPENDENCIES.json).

The receipt records the exact SHA-256 of each compiled local source.
Publication must preserve those hashes.

## Mathematical scope

The formal module defines the actual shortcut Collatz map and proves the
first-hit clock count, the all-word surviving-target coefficient budget,
its composed application to a complete source with the original target
floor, the formal full-source buffer bound, and the exact positive-source
splice exclusion. It does not assert a legal replacement parity word.

The complete PR177 joint-witness selector is an inherited interface, not
an imported Lean module in this replay. Its concrete source identity,
first-hit, floor, capture, and target-survival premises remain explicit in
the new declarations. The written arithmetic review checks that the
pinned joint witness supplies these premises, including the choice of
clock.

The renewal comparison, entropy coding, sibling singularity, symmetric
recurrence, and canonical-current calculation are written mathematical
deductions with separately recorded reviews. Their classical and recent
source qualifications remain in the proof notes. They have not been
formalized in Lean.

Neither a universal target descent nor the canonical sibling lower bound
has been proved. No missing global statement is installed as an axiom.

## Repository publication gate

The exact published commit is to be fetched into a clean complete
checkout, with the changed-file hashes and Lean-receipt hashes matched,
and checked using:

```sh
python -X utf8 -B tools/validate.py
```

Its actual published commit, tree, tracked-file count, exit codes, and
receipt hash are reported in the PR after that execution. This local
Lean receipt is not a substitute for that complete-checkout run.
Repository integrity and successful compilation do not establish the
unproved mathematical closure.
