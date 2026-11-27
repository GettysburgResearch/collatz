# Fourth reproducible checkpoint

The corrected strict end-to-end replay passed **74 Lean modules** and audited
**3,117 declarations**, including **1,486 private declarations**. Every
transitive axiom is one of `propext`, `Classical.choice`, or `Quot.sound`.
The complete successful invocation ran from `2026-11-27T16:39:43.336367+00:00` to `2026-11-27T16:46:47.759942+00:00` in a
new object directory. It includes all six pinned PR206 modules and the
new kernel proof of all 192 supplied canonical returns.

## What this checkpoint adds

- **All 192 supplied canonical returns.** For every supplied
  `m = 12*2^(18*k)-1`, `1 <= k <= 192`, the original canonical parent
  `z = (2^(m+7)-271)/81` meets a smaller canonical `Y`, and `3Y` has an
  actual three-odd-departure path to 1 at a clock at most `m`. Nine new
  modular kernel certificates complete the prior 183 entries. This
  theorem does not assert that `Y` or `z` itself reaches 1.
- **Original all-visit trace.** An independently reconstructed written
  synchronization proof gives the uniform first-row source cutoff
  `O(1/sqrt(log R))` and the original PR193 dyadic mean estimate
  `sum_{D <= j < 2D} Q*_j = O(sqrt D)`. The finite integer flux,
  first-hit transport and physical loss telescopes are in Lean. The
  full infinite probability and transport arguments are written proofs.
  The needed exponential rate remains open.
- **Formal boundedness criterion indexed by grade.** All positive orbits
  are bounded exactly when the reciprocal-source-damped complete
  first-arrival rows vanish uniformly at large odd grade. The grade
  limit is not proved. The new once-around cycle occupation theorem
  also excludes the repeated endpoint from its simple-path count.
- **Cycle restrictions.** The written all-shift height argument applies
  to every proper rotation, including nonunit shifts; separate results
  control odd-rotation complexity, primary spectral coordinates and
  moving denominator windows. The finite height comparison kernel is
  in Lean. The stated external Diophantine and complexity inputs remain
  explicit, and no all-cycle exclusion follows.
- **Native-five pressure.** A new Lean finite-bank obstruction permits
  arbitrary common-even padding. Exact counts, primitive pressure and
  high-grade inverse fibers have separate written proofs. The latter
  distinguish growing chosen sources from an arbitrary supplied source.

## Exact evidence

[Fresh Lean replay](CHECKPOINT_04_LEAN.json) records all source hashes,
compiler/dependency pins, strict flags, logical module roots, declaration
coverage for every module and the complete recursive axiom audit. The
prebuilt pinned Mathlib dependencies were checked for identity and clean
tracked sources; they were not rebuilt from scratch.

[Clean complete-checkout integrity](CHECKPOINT_04_INTEGRITY.json) checks
repository structure and retained pins, with the same source identity
before and after. Untracked cleanliness was separately checked after
the run. This validator is not a mathematics verifier.

[Eight exact finite programs](CHECKPOINT_04_BOUNDED.json) each passed
normally and with Python optimization enabled; all 16 runs returned zero
and each pair of outputs was byte-identical. The programs cover native
first arrivals, finite-bank entropy, primary spectra, all-shift and
odd-clock cycle controls, mantissa flux, the signed original trace,
physical sparse rows and the nine newly supplied modular returns. Their
hashes match the frozen source. Earlier unchanged controls retain their
own historical receipts.

[Coordinator review 05](COORDINATOR_REVIEW_05.json) identifies 20 exact
sources and what was independently reconstructed. [Source intake 03](SOURCE_INTAKE_03.json)
records the original trace statistic, prior first-return and pressure
inputs, newly pinned PR206 files and primary cycle literature. The
previous published head `1edd36feaf08cb848d5d97d00328b376831f609e`
also passed [its own exact complete-checkout validation](PUBLISHED_03_INTEGRITY.json).

## Source identity and failed integration runs

The frozen scientific and reusable-script commit is `38f673ab32b2bd3aee5adc80b8fd4350fa76f3d6`, tree
`0e0ff28fd4190bf453468dd42419d31a682fb701`. The first attempt failed at a nested-module private import;
a second compiled every mathematical module but failed in the generated
audit. Both failures and the unsuccessful intermediate module-header
change are preserved in the [integration record](../../research/astra-infinite-descent-20261127/BUILD_INTEGRATION.md).

The final script sets each flat module's logical root explicitly and
uses the legacy-root private import semantics for the aggregate audit.
It requires every packet module to appear in that audit. The successful
receipt above is a complete new invocation of the corrected script;
failed attempts are not counted as passing runs. Publication adds these
receipts without changing the checked mathematical sources.

**Collatz remains open.** None of the uniform limiting assertions,
the global trace rate, or the unrestricted cycle exclusion has been
established by this checkpoint.
