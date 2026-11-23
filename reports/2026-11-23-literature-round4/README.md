# Round-four review and execution record

Date: 23 November 2026. Parent checkpoint:
`a7fd3ac9e5bff7412858df23d776bb847e9c1371`.

The [science entry point](../../research/literature-round4-20261123/README.md)
states the mathematical results and limits. These are in-session
research reviews and executions, not external peer acceptance or a
proof of the Collatz conjecture.

## Fresh formal execution

`LEAN_RECEIPT.json` records seven successful commands in an initially
empty output directory. The three unchanged local dependencies are
`CycleWordAlgebra`, `CycleCancellation` and `CarryFibers`; the new modules
are `ActualLawRigidity`, `TriadicRigidity` and `CycleRigidity`. The final
command compiles `RoundFourAudit.lean`.

The compiler was Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with Mathlib pinned at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Builds used one thread and
warnings as errors. All 25 new public declarations were axiom-audited;
only `propext`, `Classical.choice` and `Quot.sound` appear. Input hashes
were checked before and after the build.

The all-time integral-pair classification is formal. Its rational
denominator interpretation and full stopping-time application are
written. The complete CRT/de Bruijn construction, necklace quotient,
gap gcd and logarithmic certificate asymptotics are also written. The
receipt does not claim that all older Lean files were recompiled.

## Exact executable controls

`EXACT_RECEIPT.json` records normal and optimized executions of
`research/literature-round4-20261123/exact_replay.py`, which imports the
reusable `verify_triadic.py`. The outputs are byte-identical and retained
as `EXACT_CONTROLS.json` and `EXACT_CONTROLS_OPTIMIZED.json`.

- Five actual ordinary periodic-shadow fixtures: 6,025 distinct states,
  5,985 sampled endpoints and source boxes, 77 full telescope checks,
  and 84 exact forward/backward local product equalities. Every literal
  edge and every sampled complete carry identity is checked. Fixtures
  include `m<L`, a single-period sample, biased gaps and a large floor.
- The same fixtures check bounded downward ratios, complete carry
  quotients, the source-height payment, and the first mismatch when a
  fixed source is followed beyond the prescribed periodic prefix.
  Longer-depth nonproduct controls allow accidental product equality
  immediately above the prescribed depth.
- 1,027 known convergent sources, 4,106 supplied-candidate verifier
  decisions, nine false candidates with matching short parity prefixes,
  and 128 power-of-two denominator/horizon controls.
- 81,924 exact cut determinants through complete word length 12;
  585 primitive positive rational roots, one primitive positive integral
  root in this bounded census, and 43 primitive weight classes for
  root-selection neutrality. The denominator-47 small-gap and
  denominator-13 large-gap controls are retained.

All guards use explicit failures and survive `python -O`. Uniform
finite test weights are used; these are not canonical harmonic-flow
weights. These finite computations are controls on written universal
arguments, not proofs by extrapolation.

Reproduce the exact replay from the repository root:

```bash
python -X utf8 -B research/literature-round4-20261123/exact_replay.py
python -O -X utf8 -B research/literature-round4-20261123/exact_replay.py
```

For Lean, use the pinned compiler and Mathlib, place a fresh output
directory first in `LEAN_PATH`, and build the three dependencies before
the three new modules and the audit. The receipt retains the exact
commands, outputs and file hashes from this execution.

## Review and source identity

`TRIADIC_ESCAPE_REVIEW.md` independently reconstructs the integral rank,
reduced-denominator statistic, candidate verifier and both conservative
and adaptive certificate statements. It also reviews the sharp minimum
of the conservative horizon across all sources of a given bit length.

`ACTUAL_LAW_CYCLE_REVIEW.md` independently reconstructs the actual finite
realization, signed shadow, source-height payment, local product law and
cross-box collision, and reviews the frozen checker. A second source
review is in `SOURCE_ACTUAL_LAW_REVIEW.md`.

`ROOT_REVIEW.md` records the principal reconstruction, including the
complete cycle arithmetic, exact root-count obstruction, and the formal
boundaries of all three lanes. Each review distinguishes source reading
from execution. `PR182_BEFORE.json` preserves the preceding PR metadata
and description. The research `SOURCES.json` records current read pins
and primary literature scope.

`CHECKOUT_VALIDATION.json` records the clean complete local science
checkpoint before the two receipt files were added. `SOURCE_BINDING.json`
binds that checkpoint's science, review and execution files and all 40
older tracked Lean files. The default five-command repository gate is
an integrity check, separate from mathematical verification. A fresh
checkout of the published head is additionally checked and reported in
the PR after the exact remote commit has been read back.
