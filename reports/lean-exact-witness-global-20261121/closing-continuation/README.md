# Checkpoint sixteen: funded witness transport and the exact escape remainder

Date: 23 November 2026. Parent published commit:
`6de3e304bb49a93a6c5ef0e5563137e75c7defb4`.

**Collatz, the original residue-512 implication, and FloorIntervalStep
remain OPEN.** Three research lanes and a coordinating lane worked in
parallel, then compared their results with newly advanced peer heads.
This report records actual execution and the boundaries of the internal
mathematical reviews. It is not a certificate of a full Collatz proof.

## Results and evidence level

| Result | Evidence | Remaining scope |
|---|---|---|
| Four-step source family with arbitrarily large lower bounds for every possible output witness | Six new core-Lean theorems and written proof | Does not assert output-witness existence |
| Appended cycle word's exact correction and binary/ternary guards | Three new core-Lean theorems | Density and infinite analysis are written, not formalized |
| Terminal padding by r-1 gap-two steps funds the signed normalizer or gives an actual target hit of one | Written finite theorem TP-F and independent reconstruction | Funded positive endpoint still needs a complete tail or descent |
| Global excessive-measure decomposition and exact escape remainder | Written proof AE-P1/AE-P2 retaining earlier product-positivity input | Does not evaluate the residual as zero |
| Continuous power-logarithm barrier profile classification | Written proof AE-P3/AE-P4 and independent reconstruction | General slowly varying or discontinuous profiles remain outside the theorem |
| Product-space thermodynamic test | Exact written identities and primary-source statement checks | No ordinary positive integrable right eigenfunction supplied |
| Full-denominator carry identities and rational cycle-fiber controls | Written algebra, exact targeted executions, independent reconstruction | No full zero-fiber bound or integer-cycle exclusion |
| New common maximum-atom test | Exact finite-test and loss identities, independently reconstructed | Boundary contribution remains exactly the original maximum atom |

The [research overview](../../../research/lean-exact-witness-global-20261121/README.md)
contains the formulas, proofs, remaining conditions, and links to every
scientific file. The strongest new direct witness step is TP-F; unlike
mere auxiliary rank termination, its clock is explicitly funded by the
supplied source certificate.

## Fresh Lean execution

[checkpoint-sixteen.json](checkpoint-sixteen.json) records the exact
commands, output hashes, compiler version, source hashes, nine actual
axiom inventories, and inherited-file comparison.

- Lean 4.34.1, compiler `5045d0056413266e57c625dcd7c365b10e377c52`.
- Built `Collatz.NegativeCycleExtension` and `Collatz.WitnessLengthSeparation`.
- Strict-compiled each source and each dedicated audit with warnings as errors.
- All nine public declarations passed. Axiom union: `propext`,
  `Classical.choice`, `Quot.sound`.
- Forty-seven inherited Lean files outside the two edited aggregate indexes
  are byte-identical to the parent. Dependency objects were reused.
- No admitted proof, conjectural axiom, or native proof shortcut was added.
- The full historical aggregate audit and unrelated modules were not rerun.

The padding theorem and infinite analytic results are not represented as
additional Lean declarations.

## Targeted exact executions

Each script was run normally and with `-O`; the two outputs in each pair
are byte-identical and all failure guards remain enabled.

| Program | Retained checks | Receipt |
|---|---|---|
| atomic_cycle_controls.py | 24 rational cycles; 265 rotations; 72 positive ordinary CRT paths; 12 ordinary cylinder bridges | [Atomic controls](atomic-cycle-controls-replay.json) |
| target_entry_controls.py | Five four-step families; five funded normalizers; four Mersenne families; the literal first-hit source 129 precision failure | [Target controls](target-entry-controls-replay.json) |
| cycle_fiber_controls.py | Two specified cycle pairs, three complementary pairs, exact minima and crossing, 32 carry updates on ten cycles | [Cycle controls](cycle-fiber-controls-replay.json) |

These are targeted construction checks, not larger all-word searches.
The universal statements are supported by their written or Lean proofs,
not by extrapolation from these executions. TP-F's short all-parameter
proof was independently reconstructed; no additional numerical execution
is claimed for that written addendum.

## Internal review boundaries

- [REVIEW_EXTENSION.md](REVIEW_EXTENSION.md): separate reconstruction of
  the coordinator's three formal identities and constructive checker.
- [REVIEW_TARGET.md](REVIEW_TARGET.md): separate reconstruction of the six
  Lean theorem meanings, arbitrary-witness quantifier, signed normalizer,
  physical clocks and six-step family.
- [REVIEW_TARGET_PADDING.md](REVIEW_TARGET_PADDING.md): separate reconstruction
  of the full padded numerator, exact funding boundary, TP-F, negative carry,
  endpoint control, and coefficient transport.
- [REVIEW_ATOMIC_PROFILE.md](REVIEW_ATOMIC_PROFILE.md): separate reconstruction
  of joint density, ordinary finite routing, full profile classification,
  the lifted operator, and primary theorem scopes.
- [REVIEW_CYCLE_CONTROLS.md](REVIEW_CYCLE_CONTROLS.md): separate algebra and
  exact replay; includes the applied empty-interior wording correction.
- [REVIEW_MAXIMUM_ATOM_TEST.md](REVIEW_MAXIMUM_ATOM_TEST.md): separate
  reconstruction of the finite boundary, defect telescope and row sums;
  includes the ordinary-domain qualification.
- [REVIEW_COORDINATING.md](REVIEW_COORDINATING.md): coordinating reconstruction
  and actual execution, with contributions disclosed rather than called
  independent review.

Each verdict binds exact file hashes and named claims. These are internal
reconstructions, not external peer review or an audit of inherited sources.

## Repository refresh and publication

[OPEN_PR_HEADS.json](OPEN_PR_HEADS.json) inventories all 122 open PR heads
from the repository-wide refresh, separately from mathematical review.
[SOURCES.json](SOURCES.json) pins the particular source files and primary
statements actually read. Main's research map, open obligations and scoped
errata were revisited for route selection. Newer peer revisions do not
inherit older review verdicts.

[FILES.json](FILES.json) binds the changed scientific files and this report
packet. The post-commit default validator must run in a complete clean
checkout. Its exact local commit/tree identity, receipt hash, and the
remote tree/readback are recorded in PR177 after publication, avoiding a
self-referential commit record. Repository integrity checks are separate
from the mathematical evidence above. The optional historical regression
bundle is not part of this checkpoint's claim.
