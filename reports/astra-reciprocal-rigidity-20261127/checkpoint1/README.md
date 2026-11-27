# First checkpoint: independent replay and publication identity

The scientific packet is **PROPOSED**. Collatz remains open. These are execution
records for the first checkpoint, not additional mathematical assumptions.

## Frozen science

- Published commit: `5c67ddfcc9a376cb6f6dde0a0d05c74d7b9ae3ee`.
- Scientific tree: `a6f837910687c00b0bf8aa0e439998c43484046a`.
- Local prepublication commit: `3dab945fc1f43aba0d032f46358f42271c1104c1`.
- Draft pull request: [#211](https://github.com/GettysburgResearch/collatz/pull/211).

The local and published commits have exactly the same Git tree. Publication used
the connected GitHub API after ordinary Git push could not authenticate. The
published commit was fetched and its tree identity checked before the local branch
was aligned. A complete clean checkout of the published commit then passed the
repository regression validator. No main-branch update was made.

## What was independently replayed

[LEAN_REPLAY.json](LEAN_REPLAY.json) records a fresh local-output rebuild of fourteen
modules. [RIGIDITY_REPLAY.json](RIGIDITY_REPLAY.json) separately rebuilds the three
modules in the `CutoffRank` chain, giving **fifteen distinct modules** in total.
The latter consumer prints the five advertised rigidity theorem inventories;
the two underlying source modules do not print their own inventories.
All compilation commands use Lean 4.34.1, the pinned Mathlib revision,
`autoImplicit=false`, `warningAsError=true`, and `Elab.async=false`.
Every printed dependency inventory is contained in
`[propext, Classical.choice, Quot.sound]`. The receipts retain source hashes,
compiler output, exit codes, durations, and before/after source checks.

The 648-source prefix certificate was evaluated by Lean's kernel. Its consumer
proves an all-time conclusion for the stated ramp family. The larger finite
tables remain separately identified as Python computations.

[FINITE_REPLAY.json](FINITE_REPLAY.json) records seven programs run both normally
and under `-O`. Outputs match the retained controls and agree between modes.
Before the scientific checkpoint, the rigidity checker was changed from Python
assertions to explicit failures, so optimization does not remove those checks.
This is bounded arithmetic verification, not universal orbit verification.

## Repository integrity

[LOCAL_INTEGRITY.json](LOCAL_INTEGRITY.json) and
[LOCAL_REGRESSIONS.json](LOCAL_REGRESSIONS.json) authenticate the clean local
science commit. [PUBLISHED_REGRESSIONS.json](PUBLISHED_REGRESSIONS.json) authenticates
the clean published commit directly. These run the repository's existing integrity
and bounded regression gates; they do not verify new written mathematics.

[DESCENT_AUTHOR_REPLAY.txt](DESCENT_AUTHOR_REPLAY.txt) preserves the earlier author's
Lean output as supplementary evidence. It is not substituted for the independent
root replay. [MANIFEST.json](MANIFEST.json) records the evidence file hashes and
the publication identity.

## Resource interruption and scope

The independent root replay completed without a failed mathematical module.
Its long `ShiftBalance` duration occurred during heavy shared-memory paging.
Parallel phase-two compilation was stopped and subsequently serialized; those
interrupted exploratory runs are not claimed as successful verification.

The author's optional cold Mathlib dependency rebuild was interrupted after
215 of 285 dependency compilations. The completed root replay used the pinned
dependency cache with fresh outputs for this packet. No complete independent
rebuild of Mathlib or of external number-theory developments is claimed.

The analytic natural-boundary arguments, the full ordinary construction behind
their coefficient arrays, and imported quantitative cycle and first-exit inputs
retain the written/source-qualified status stated in the scientific packet.

