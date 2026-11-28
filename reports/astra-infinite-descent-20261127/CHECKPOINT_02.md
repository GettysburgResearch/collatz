# Second reproducible checkpoint

The complete fresh strict replay passed **42 Lean modules** and audited
**1,901 declarations**, including private helpers and generated declarations.
Every recursively collected axiom belongs to `propext`, `Classical.choice`,
or `Quot.sound`. The replay ran from 14:24:05 to 14:27:00 UTC on
2026-11-27 in a new object directory.

This checkpoint formalizes arbitrary finite additive patterns with a common
ordinary first-hit clock and odd grade, arbitrary source progressions, and
independently prescribed residues of clock and grade in every sufficiently
large relative window. It adds finite native inversion, periodic carry,
and character-cancellation kernels. The complete spectral denominator
and compact correction arguments have written reviews with separate
external-input boundaries.

## Exact evidence

- [Fresh Lean replay](CHECKPOINT_02_LEAN.json): the same pinned compiler,
  Mathlib source and eight dependency revisions as checkpoint one; all
  packet modules compiled from source with a fresh local import graph.
  The audit includes every declaration originating in those modules.
- [Clean checkout integrity](CHECKPOINT_02_INTEGRITY.json): the required
  complete-checkout validator passed with clean state before and after.
- [New finite controls](CHECKPOINT_02_BOUNDED.json): four programs ran
  normally and with Python `-O`. All eight runs returned zero, and each
  output pair was byte-identical. These cover 1,024 literal common first
  arrivals, 768 arithmetic-progression routes, near-octave native carries,
  and exact spectral supports with exhaustive bounded binary controls.
  Unchanged programs already replayed at checkpoint one were not rerun.
- [Further written review](COORDINATOR_REVIEW_03.json): exact source hashes
  and independently reconstructed steps for the spectral denominator,
  conditional global correction set, marked placement, and finite
  character arguments. The preceding review is in
  [COORDINATOR_REVIEW_02.json](COORDINATOR_REVIEW_02.json).

The frozen scientific source commit is
`9a7fb6b7f2b84fe2e4d0a9a5059d172039d3a589`, tree
`5713e490f3de1004882deb59f00b1768376939b1`. Publication adds these receipts
without changing those scientific bytes. All source hashes are recorded
in the replay. The first published head
`8cac31f51d9a5a2bd03c211495dec8f90c2aa48e` was also materialized and
[validated exactly](PUBLISHED_01_INTEGRITY.json) in a clean complete
checkout after its GitHub publication.

## Limits of the checkpoint

The universal reciprocal-mass estimate is still open. The compactness
result is conditional on its pinned prior written analytic inputs and
isolates, rather than excludes, a finite maximizing escaping class.
The spectral denominator theorem treats its stated physical regime;
it does not exclude every possible positive integer cycle. The Lean
replay verifies the actual theorem statements, including explicit
hypotheses, and does not validate all written analysis or rebuild
Mathlib and Lean themselves.
