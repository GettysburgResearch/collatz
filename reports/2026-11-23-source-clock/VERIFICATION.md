# Verification scope for the source-clock checkpoint

Date: 2026-11-23. Scientific entry point:
[research summary](../../research/source-clock-20261123/README.md).

## Formal execution actually completed

The packet's fresh Lean run passed. It compiled `BoundaryMass`,
`BoundaryBorelCantelli`, and `BoundaryAudit`, with warnings treated as errors.
All seven public declarations were covered by the audit and reported only
`propext`, `Classical.choice`, and `Quot.sound`.

The compiler was Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, binary SHA256
`e8baaa71855a616dc351028f3ad2200051b0671f423a1696a100e809302d5550`.
Mathlib was pinned to `d13f23b723b8a846827a245b89c10fc7d3f11612`.

Four missing Mathlib dependencies were compiled in order into a fresh
temporary overlay: `OuterMeasure.Defs`, `Basic`, `AE`, and `BorelCantelli`.
All other installed Mathlib objects were reused through read-only links.
The runtime's sources and cache were not modified. No historical project
proof module was imported or rebuilt.

[Exact execution receipt](lean-check.json) and [compiler output](lean-build.log)
record source hashes, import pins, dependency build status, timings, theorem
inventory and axiom output. The reproducible command is:

```bash
python -X utf8 -B research/source-clock-20261123/check_lean.py \
  --mathlib /absolute/path/to/pinned/mathlib \
  --lean /absolute/path/to/pinned/lean \
  --report-dir /absolute/path/to/new/report-directory
```

The four finite inequalities and the three conditional Borel--Cantelli
declarations are formal proofs. The actual trace construction, analytic
bad-event bounds, good-return construction and information-dimension theorem
remain written mathematics with explicit dependencies. The audit does not
convert those dependencies into verified Lean facts.

## Mathematical reconstruction reviews

[REVIEW_SCOPE.json](REVIEW_SCOPE.json) binds every reviewed artifact to exact
SHA256 bytes and a frozen in-session review. The boundary proof received
independent reconstructions from both other research lanes. The information
extension received a separate reconstruction, including its constants and
the absolutely continuous reweighting argument. Root independently checked
the stopped-trace, semigroup, collision-model and Borel--Cantelli notes.
The target reviewer checked that the four finite Lean statements match
their intended applications.

These are scoped independent in-session checks, not external peer review
or a new audit of the inherited analytic literature. No source theorem
is upgraded from SOURCE-QUALIFIED by being cited here.

## Exact source and file identities

[SOURCES.json](../../research/source-clock-20261123/SOURCES.json) pins 14
inspected source files by full commit, path and content hash.
[open-pr-snapshot.json](open-pr-snapshot.json) records the initial metadata
refresh of all 122 open PRs; only selected source interfaces were used.
The prior PR180 description is preserved in
[pr180-prior-description.json](pr180-prior-description.json).

[FILES.json](FILES.json) covers every new packet file except the manifest
itself. Run the bounded identity checker from a checkout with the frozen
source commits available:

```bash
python -X utf8 -B research/source-clock-20261123/check_packet.py \
  --receipt /absolute/path/outside-checkout/packet-check.json
```

It checks the exact file set and hashes, frozen source text, review bindings,
compiled-source identities, all seven audited names, dependency pins, JSON,
and relative links. It does not rerun old numerical searches or certify
the analytic proofs.

## Clean-checkout and published-checkout gate

Repository integrity is a separate execution tier. The required command is

```bash
python -X utf8 -B tools/validate.py \
  --receipt /absolute/path/outside-checkout/integrity.json
```

The publication procedure runs it on a clean complete local checkout,
then fetches the published commit into another complete checkout and runs
the same gate plus the packet identity check there. These executions occur
after this report is frozen. Their exact commit, tree, exit codes, tracked
file count and receipt hashes are recorded in the updated PR metadata,
following remote readback. A copy of this report alone is not evidence
that either later execution succeeded.

The optional historical regression bundle is outside this pass's scope.
Repository integrity is not proof of Collatz.
