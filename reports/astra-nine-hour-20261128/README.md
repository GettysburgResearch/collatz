# Nine-hour research pass: evidence and publication

Requested research interval: **2026-11-27 22:55:59 UTC through
2026-11-28 07:55:59 UTC**. In the user's timezone this is
00:55:59–09:55:59 on November 28.

The [scientific packet](../../research/astra-nine-hour-20261128/README.md)
contains the live theorem statements and open targets. This directory
records exact source intake, independent reconstruction, finite and Lean
replay, repository integrity, and publication checkpoints.

- [Intake](INTAKE.json): 149 open PR metadata rows, current main, previous
  pass head, and priority source pins. Inclusion is not proof review.
- [Toolchain](TOOLCHAIN.json): exact official Lean release provenance and
  the task-owned compiler installation.
- [Frontier review](FRONTIER_REVIEW.md): source interfaces read by the
  coordinator and the boundaries that control this pass.

The first theorem-bearing publication includes the
[written claim review](CHECKPOINT_01_REVIEW.md),
[finite controls](CHECKPOINT_01_CONTROLS.json),
[critical parity counts](CRITICAL_PROBE_24.json), and the explicit
[initial Lean replay status](CHECKPOINT_01_LEAN_STATUS.md).
Publication records name exact scientific and published commits and
distinguish a passing complete replay from a development attempt.

The second publication includes the [expanded written review](CHECKPOINT_02_REVIEW.md),
[complete ten-module Lean replay](CHECKPOINT_02_LEAN.json), and
[paired new finite controls](CHECKPOINT_02_CONTROLS.json). The separate
[six-module frozen replay](CORE_06_LEAN.json) resolves the initial core
build before the larger snapshot. The first published commit's exact
[integrity receipt](CHECKPOINT_01_PUBLISHED_INTEGRITY.json) and
[publication record](CHECKPOINT_01_PUBLICATION.json) are retained here.

The third publication adds the [ordinary-observable and cycle review](CHECKPOINT_03_REVIEW.md),
[complete thirteen-module replay](CHECKPOINT_03_LEAN.json),
[five paired finite controls](CHECKPOINT_03_CONTROLS.json) and the
[reviewed-source manifest](CHECKPOINT_03_SOURCES.json). It preserves the
second published commit's exact [integrity receipt](CHECKPOINT_02_PUBLISHED_INTEGRITY.json)
and [publication record](CHECKPOINT_02_PUBLICATION.json). The third Lean
replay audits 353 declarations, including 39 private declarations.
