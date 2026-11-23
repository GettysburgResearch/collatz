# Verification scope: coherent boundary and global source attempts

Date: 23 November 2026. Starting PR180 checkpoint:
`5e29f56f6d44669a8aa9134e5617b78d65c074c2`.

**Collatz remains open.** The checkpoint contains three research notes,
two public finite-algebra Lean declarations, an exact complete finite
source control, and independent in-session reconstruction reviews. The
infinite arguments retain their explicitly identified upstream inputs;
the support-dimension result additionally retains the qualified routing
manuscript input.

## 1. New Lean execution

Executed the packet harness with these installed dependencies:

```text
python research/high-variance-20261123/check_lean.py \
  --lean /workspace/scratch/c6766c1207a3/collatz_work/nov23_runtime/lean-4.34.1-linux/bin/lean \
  --mathlib /workspace/scratch/c6766c1207a3/mathlib_nov23_runtime \
  --report-dir reports/2026-11-23-high-variance
```

**PASS.** The final proof source and separate audit module were compiled
into a fresh temporary output directory with warnings as errors. The
audit printed exactly the two public declarations in the inventory and
reported only `propext`, `Classical.choice`, and `Quot.sound`.

Compiler: Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`.
Mathlib commit: `d13f23b723b8a846827a245b89c10fc7d3f11612`.
The dependency checkout had no modified tracked sources. The five direct
Mathlib imports were checked against their pinned source hashes. Installed
dependency objects were reused; no historical project module was imported
or rebuilt.

The final compiled hashes are:

- `FibreReconstruction.lean`:
  `d81acc83862914d097261ef92753ef1455bded005e291db3088a0b1c46a71cec`.
- `FibreAudit.lean`:
  `91af2030f41f788084fdc5bbc503f00e7238e71679caea63c73b01d4f5c65076`.

The statements prove the literal coherent-edge increment and the finite
normalization, reciprocal-moment and variance identities. The finite
reconstruction permits signed real weights. Its probabilistic
interpretation needs additional positivity; the declaration does not
assert that a signed tilt is a probability. No construction of an infinite
path law, limit, dimension theorem or Collatz convergence statement is
formalized or added as an axiom.

[Compiler receipt](lean-check.json) · [Compiler output](lean-build.log) ·
[Public inventory](../../research/high-variance-20261123/THEOREMS.json) ·
[Source reconstruction](REVIEW_FIBRE_LEAN.md).

## 2. Complete integer control

Both commands passed and produced output byte-identical to the frozen
`global-source-control.json`:

```text
python -X utf8 -B research/high-variance-20261123/check_global_source.py
python -X utf8 -B -O research/high-variance-20261123/check_global_source.py
```

The checker exhausts the inverse queues and separately checks closure
under every legal gap one, two and three. Its node and orbit guards abort
on exhaustion of resources; they never certify a truncated tree. It
replays every first-hit source word in the complete two-four census,
compares all eligible initial exponents, checks the exact grade maxima,
and replays the source floor and the target's actual descent/convergence.
Its all-length coverage rests on the proof decomposition in the note,
not on searching to an arbitrarily selected depth.

The control contains 1371 odd first-hit sources. Its target `2^51-1`
first descends at shortcut time 138 and first reaches one at time 384.
It therefore does not satisfy the badness hypothesis of a joint
counterquery. These successful checks are not a convergence result for
arbitrary targets or a proof that every bounded-gap inverse cluster is
finite.

[Execution receipt](global-source-check.json) ·
[Independent reconstruction](REVIEW_GLOBAL_SOURCE.md).

## 3. Independent mathematical reconstruction

Each research lane was checked by a researcher other than its author:

| Note | Reconstruction focus |
|---|---|
| Coherent analytic gluing | Common ordinary coordinate, exact boundary support, conditional path densities, distinct trace tilt, positive deformation range, integer rigidity, routing overlap and root cost |
| Actual boundary entropy | Full-path conditioning, arbitrary-resolution common-frame information, fixed-root nonatomicity, retained moving normalization, simultaneous trace selection and both rare-cylinder costs |
| Whole inverse clusters | Original-target lower-grade permission, all-length replacement, complete tree identities, unrestricted family and exhaustive finite-grade control |

The reviews are bound to exact final proof hashes in
[REVIEW_SCOPE.json](REVIEW_SCOPE.json). The analytic author corrected
path-cylinder wording, the small-scale choice in the Frostman argument,
and the orientation of a relative-entropy sentence. The source author
made the finite-tree unit-root hypothesis explicit. The entropy note
retains the distinction between a nonatomic path law and a possibly
overlapping real boundary pushforward. The final reviews apply to those
corrected bytes.

These are internal mathematical reconstructions, not external peer review.
They neither audit the full external manuscript chains nor certify the
unproved global closing step.

## 4. Source and publication identity

The repository refresh records all 122 open-PR metadata rows, with 29
targeted inspected files separately pinned by full commit, Git blob and
SHA256. Literature access and proof limits are recorded separately.
The prior PR description is preserved in
[pr-description-before.json](pr-description-before.json).

Before publication, the new JSON, relative links, proof/review bindings,
compiled source identities and complete checkpoint manifest are checked.
The required complete-checkout command is run after the local commit and
again on a fetched published commit:

```text
python -X utf8 -B tools/validate.py --receipt <path-outside-checkout>
```

Its five default checks concern repository integrity and frozen review
identities. They are separate from the mathematical deductions, finite
integer control and Lean evidence above. The optional historical replay
bundle is not part of this pass. The exact commit, tree, cleanliness,
gate outcome and remote PR read-back are recorded in the updated PR
description, after those operations occur. No pre-publication source
inspection is relabeled as execution on the remote commit.

[Checkpoint file hashes](FILES.json).
