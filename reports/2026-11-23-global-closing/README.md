# Checkpoint 18: execution and mathematical review

23 November 2026. Scientific entry point:
[ordinary-source closing routes](../../research/lean-global-resolvent-20261121/overview/global-closing/README.md).
Full Collatz remains open. The new results are written mathematics with
exact finite controls; this checkpoint adds no Lean declaration and does
not re-run the historical Lean corpus.

## Mathematical review

- [Coordinating reconstruction](ROOT_REVIEW.md) covers the ordinary insertion
  theorem, actual entropy/anchor/collision arguments, and complete paired
  cycle identities. It discloses author and reviewer contributions.
- [Independent generic-ray review](GENERIC_RAY_REVIEW.md) reconstructs the
  entire infinite construction, every-clock pressure bounds, critical mean,
  nonatomicity, irrationality and finite ordinary realization.
- [Independent all-gap review](REVIEW_ALL_GAP.md) reconstructs the new
  entropy and collision deductions, retaining the source-qualified
  stationary input and the missing upper bound.

These are internal agent reviews bound to exact file hashes. Their verdicts
do not extend to later peer heads or every earlier source theorem.

## Exact finite controls

| Record | New coverage |
|---|---|
| [Insertion controls](CHECK_RESULT.json) | 46,101 rational edit candidates; all 155 positive integral candidates replayed; seven joint integrality cancellations; 40 further family cases. Normal and optimized execution each retain 100,318 explicit conditions. |
| [Actual collision controls](all-gap-collision-controls.json) | 37,627 finite integer/Fraction checks across actual distinct segments and complete word cylinders, plus four false-variant controls. Includes 7,476 sliding entropy bounds, 1,120 occupation bounds, 6,821 full-gap identities, 13,557 reduced-anchor divisibilities and 1,360 CRT word-return controls. |
| [Generic-ray controls](GENERIC_RAY_CONTROLS.json) | Six finite regulator cases, every interstitial barrier, minimal new records, finite block-count changes, exact ordinary prefix realizers, the two series orientations, and four damaged controls. The rational-parameter fixture is not claimed to be the critical iid input. |
| [Paired-cycle controls](PAIRED_TENSOR_CONTROLS.json) | Six paired rational cycles, including the integer core and four high-floor cases. All 13,589 literal paired shortcut steps, full gcd reductions, tensor identities and both companion lower bounds are checked. |

The uniform theorems follow from the written proofs, not from these finite
records. The integration runner executes each new checker normally and
with `python -O`, requires identical output, compares it with the frozen
record, and confirms no frozen input was changed. It uses standard-library
exact arithmetic only.

Author execution records are [insertion](insertion-execution.json),
[actual collision](collision-execution.json), and [paired cycles](cycle-execution.json).
The generic-ray normal/optimized execution is reproduced in the common
[integration receipt](integration-execution.json). The separate independent
generic-ray reviewer inspected the checker and results but does not claim
another execution.

## Frozen sources and repository coverage

The scientific packet's [source union](../../research/lean-global-resolvent-20261121/overview/global-closing/SOURCES.json)
contains 21 distinct repository source windows. Twenty content objects
were available and hashed during integration. One PR183 context entry
was inspected through PR metadata only; the underlying object was
unavailable and no theorem from it is imported here.

The original per-lane windows are preserved as [generic ray](generic-ray-sources.json),
[insertions](insertion-sources.json), [collisions](collision-sources.json), and
[cycles](cycle-sources.json). They also record primary literature access
and applicability scope. The primary Atkinson recurrence statement was
read by the coordinator; its stationary almost-everywhere conclusion is
not substituted for a pointwise conclusion on every generic sequence.

[Source refresh](source-refresh.json) freezes the 50-entry PR metadata
catalogue and central branch heads. Four central peer heads advanced
relative to checkpoint 17. The [previous PR description](previous-pr-description.json)
preserves the earlier published checkpoint. The review covers the research
map, active source families, designated new mathematics and the machinery
guide; it is not a claim of a new audit of every historical file.

## Reproduction

```sh
python -X utf8 -B research/lean-global-resolvent-20261121/overview/global-closing/verify_checkpoint18.py \
  --receipt /tmp/checkpoint18-scoped.json
python -X utf8 -B tools/validate.py --receipt /tmp/checkpoint18-integrity.json
```

The first is the scoped new-control replay. `manifest.json` binds the
scientific packet, reviews, individual source windows, frozen results,
author records and report. It excludes itself and the integration receipt
to avoid a hash cycle. The integration receipt records the manifest hash.

The second command is the required clean complete-checkout integrity gate.
It is run after the local commit and again on the exact fetched published
head; its receipt stays outside the checkout and its exact result is
reported in the PR. Repository integrity is not mathematical verification.
