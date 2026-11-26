# Exact scope of the 2026-11-26 continuation

The [science overview](../../research/unconventional-20261126/README.md) is
the reading entrypoint. This directory records source identity, execution,
and the boundaries of the evidence. **It does not certify Collatz.**

## New exact-source Lean replay

The coordinator ran [replay.py](replay.py) from the actual workspace sources,
compiling into a fresh external directory. All ten files passed with
`-DwarningAsError=true`. The source bytes were checked again after each
execution. Every listed declaration was queried with `#print axioms`; only
`propext`, `Classical.choice`, and `Quot.sound` occurred.

| File in the new research packet | Declarations | Formal scope |
|---|---:|---|
| `adelic/PeriodicWindows.lean` | 6 | Native word composition, actual traces, cleared defect divisibility |
| `PhysicalShadow.lean` | 8 | Entire-clock divisibility and uniqueness of a fixed rational shadow |
| `CoreBranching.lean` | 12 | Two distinct unit predecessors at four native clocks; all-depth injective binary tree |
| `adelic/PatchRigidity.lean` | 3 | Small integer congruence discrepancies and ternary divisibility |
| `CoprimeCancellation.lean` | 4 | Exact reduced denominator after cancelling a common factor |
| `AlignedCycles.lean` | 4 | Integer order preservation for fixed digits and 01/10 tiles; restricted cycle exclusion |
| `FinalProposal.lean` | 6 | Positivity and the equivalence with the two explicitly unproved final obligations |
| `renewal/RenewalArithmetic.lean` | 5 | Opposite-end divisibility and signed carry-string injectivity |
| `adelic/PrimitiveTracks.lean` | 3 | Finite periodic-forcing algebra |
| `operator/HybridRoot.lean` | 2 | Literal paired-coordinate inverse guards and the slope bound |
| **Total** | **53** | **Selected finite interfaces, not the full written analysis** |

Compiler: Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`.
Mathlib: `d13f23b723b8a846827a245b89c10fc7d3f11612`.
The manifest and dependency revisions are recorded in
[REPLAY_RECEIPT.json](REPLAY_RECEIPT.json); raw axiom outputs are in
[lean-logs](lean-logs). No new axiom, `sorry`, or unproved declaration was
used to replace either final obligation. A checked theorem taking an open
proposition as a parameter remains conditional.

The Hausdorff estimates, Subspace Theorem arguments, infinite operator
analysis, prime-uniform logarithmic forms, and infinite families of cycles
are **written mathematics**. No Lean proof of those complete theorems is
claimed. No independent implementation of Lean's kernel was run here.

## Finite arithmetic replay

The first seven scripts were each executed twice, with ordinary Python and with
`-O`. Their complete JSON payloads matched the checked-in outputs, and the
ordinary/optimized output bytes were identical. The receipt records both
exit codes, hashes, and elapsed times. They cover periodic windows,
denominator/cycle identities, the two primitive constructions, the finite
electrical certificates, mixed-root neighborhoods, and renewal arithmetic.

The additional eighth script, `operator/gate_controls.py`, subsequently
passed the same full-payload and normal/optimized byte comparisons in
[GATE_REPLAY.json](GATE_REPLAY.json). It computes exact weighted first exits
at nine cutoffs through 100,000, compares with direct path following through
1,000, and verifies the finite transport identity through 1,000. Thus the
combined execution covers **eight scripts and sixteen executions**. The
current replay driver includes all eight. No limiting decay follows from
these finitely many gates.

The all-phase coherent replay uses exact large-integer native updates and
outward rational intervals. Its 865,445-step fixture certifies a gap of at
least 2.752799, but tests exactly the primes 5 and 71. The finite test is not
an execution over an unbounded prime sieve. The additional 7,275-step
fixture has gap at least 1.056149 and tests prime 31.

The baseline JavaScript controls were also rerun. All integer payloads
match. The recorded initial wrapper comparison and the separate floating
illustration discrepancy are retained in
[BASELINE_CONTROLS.json](BASELINE_CONTROLS.json).

## Earlier candidates and external work

The unmodified two earlier `import Mathlib` files encountered a missing
cached dependency. Fourteen declarations then passed with **only imports
replaced** and original proof bodies preserved. Benign original linter
warnings are retained in [BASELINE_LEAN.json](BASELINE_LEAN.json). This does
not become an exact-byte compilation claim for those earlier complete files.
The new ten-file replay above does compile its exact checked-in bytes.

[SOURCE_INTAKE.json](SOURCE_INTAKE.json) pins the baseline and the selected
other PR heads. Thirty PRs received metadata coverage, not thirty full proof
audits. Literature statements remain attributed to their authors; no external
formal library or large predecessor data set was rebuilt. The earlier PR
description is preserved in [PREVIOUS_PR.json](PREVIOUS_PR.json).

The starting 373-file checkout passed all five required repository checks:
[BASELINE_VALIDATION.json](BASELINE_VALIDATION.json). A final clean-checkout
receipt is recorded after committing the complete continuation. Repository
integrity is a distinct check from mathematical truth.

## Reproduce

With the pinned native compiler and a built pinned Mathlib checkout:

```bash
python3 -X utf8 -B reports/unconventional-20261126/replay.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/mathlib4 \
  --out /absolute/new/path/outside/the/repository
```

Use `--only lean` or `--only controls` for the corresponding bounded scope.
The output directory must not already exist. The driver neither installs
dependencies nor changes the source tree. The recorded source manifest can
be checked separately with `verify_manifest.py`.
