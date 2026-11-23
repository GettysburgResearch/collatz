# Frozen sources and review boundary

This is a theorem-bearing exploratory delta on PR176 checkpoint 10,
`31c4a880ea4acf6eec4783e68bfc75e2cf8e7fe6`. The main branch observed at
the start was `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Source heads
below were frozen on 22 November 2026; verdicts do not extend to later
pushes. No other contributor's branch was changed.

## Exact dependencies of the new proofs

The record theorem imports only `Collatz.BoundedGapCofinal`. Its complete
project closure consists of thirteen byte-identical modules from PR177
at `a0a0d76f91b4e3846c1b1f0706cad56cb6098317`, rooted at
`research/lean-exact-witness-global-20261121/lean/Collatz/` in that source.
Each exact source path, resident path and SHA256 is in
[DEPENDENCIES.json](DEPENDENCIES.json).

The mathematical inputs are the complete affine certificate identity;
the well-foundedness, transitivity and permutation invariance of `Less`;
`CollatzGapMultiset.ordinary_step`; and the cofinal large-even and high-gap
replacement theorems in `BoundedGapCofinal.lean`. The new proof takes a
maximum only within a fixed grade permutation class. It does not assume
a bounded grade downset or a source-size-monotone grade.

The sibling module has no project import. It uses Lean
`5045d0056413266e57c625dcd7c365b10e377c52` (4.34.1) and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`, specifically the natural
multiplicity/LTE and coprimality libraries and the listed arithmetic
tactics. No mathematical claim from a web paper is an extra formal
assumption.

## Fresh source comparisons

These comparisons directed the attempted global proof. They are not
additional imports or a claim to have rebuilt the refreshed branches.

| Source and frozen head | Exact source paths and claims used | Evidence in this pass |
|---|---|---|
| [PR177](https://github.com/GettysburgResearch/collatz/pull/177), `8ef9bf0d828fc533721dee1f90c5d78fac80ad39` | `research/lean-exact-witness-global-20261121/`: current source-progress and rooted-floor developments, compared against the inherited complete-certificate interface | Read-only source comparison; refreshed branch not imported |
| [PR180](https://github.com/GettysburgResearch/collatz/pull/180), `ab3973099f0d285bbe88972382ad599bb02cd460` | `research/lean-joint-20261122/MIXED_COVER.md` and `lean/MixedCoverAttack.lean`: fixed-grade source ceiling, same-grade finite defect, remaining `[3,2,2]` family and its ten-step target identity | Source-qualified inputs to the attempted coupled proof; the new source ceiling is separately derived in Lean from the old exact imports |
| Same PR180 head | `research/lean-joint-20261122/ORDINARY_BOUNDARY.md`, `CONTACT_CLOCK.md`, `FINITE_SPIKE_CLOSURE.md`: all-layer reference, original versus reset contact clocks, finite inverse horizon | Read-only mathematical comparison; no new vanishing or uniform-tail conclusion attributed to these results |
| [PR185](https://github.com/GettysburgResearch/collatz/pull/185), `53f01ca5b443ef57ef2160b4996dbb2cc87f7395` | `research/multiple-attacks-20261122/CONTACT_RETURN_FINITE_REFERENCE.md`, `HARMONIC_KERNEL_FACTORIZATION.md`, `STOPPED_MIXING_INTERFACE.md`: contact-time contraction, right factorization and stopped-mixing interface | Read-only mathematical comparison; escaping sectors and source-qualified inputs retained |
| [PR175](https://github.com/GettysburgResearch/collatz/pull/175), `728389c2ad4796853948250a90188b0697483d92` | `research/lean-global-closure-20261121/LITERATURE_DIRICHLET_BOUNDARY.md`: current analytic boundary | Read-only comparison; no external harmonic comparison imported as a theorem |
| PR176 baseline above | `research/lean-global-resolvent-20261121/overview/profound/`: `MOVING_TILT_WINDOW.md`, `SPARSE_BOUNDARY_MASS.md`, `ENDPOINT_TILT_CRITICALITY.md` | Previously published exact-source criteria used only to identify the missing estimate, not claimed as new results |

The finite fixed-grade source ceiling is credited to fresh PR180's
interface. The record selection and the resulting cofinal source-only
obstruction are the new argument. The sibling obstruction uses standard
3-adic valuation arithmetic; no claim of novelty for LTE is made.

## Independent reconstruction and exact scope

- **Record module and actual-grade theorem: VERIFIED.** Root and the
  joining/analytic agent reconstructed the record selection and the
  `C=S-1` contradiction. The arithmetic agent independently checked the
  written extension to general well-founded certificate orders, including
  the natural threshold, transitivity and terminal boundary. That
  extension is written mathematics, not an extra formal theorem.
- **Sibling note and formal arithmetic core: VERIFIED.** Root reviewed the
  formal identities. The joining/analytic agent independently checked
  integrality, every positive odd intermediate state, exact valuations,
  the source-unit guard, the empty word and the complete geometric sum.
  The sum bounds original source weights only, not canonical potentials.
- **Analytic continuation: GAP/BLOCKED.** Root corrected an initial
  overextension to cycles: the harmonic profile used here is on a domain
  killed at periodic states. The frozen note explicitly claims no cycle
  argument. Neither the sibling comparison, a fixed-source long-clock
  bound, nor critical moving-tilt decay was proved.
- **Coupled arithmetic continuation: GAP/BLOCKED.** No complete successful
  target selector, record-word grammar, or all-parameter companion return
  was obtained. The record theorem does not refute target-changing
  recursion or arbitrary-target `MixedCover`.

The three explanatory notes and three Lean files were copied unchanged
from the reviewed agent packets. The record agent additionally reviewed
the integrated README and this wrapper for scope and contribution claims;
that narrow wording review passed without corrections. Their SHA256 hashes
at integration are:

| File | SHA256 |
|---|---|
| `SOURCE_RECORDS.md` | `404a98808aa849e4734c97c4af5c25eeab1885cb91a25a695192bcac6e4ee106` |
| `FIXED_SOURCE_SIBLING_LIFTS.md` | `96d8e66d57a88faf1787fff7d0854598bfbf62aae5e8058202d17be10a829913` |
| `DIRECT_FLOW_ATTEMPTS.md` | `0bf5ab18f75cf70cf06083fa4827b12fa39cd04e74cdf9e6164cf4d685c00c30` |
| `lean/Collatz/SourceRecords.lean` | `e2042e116b9a03f2ed872262bc909441471daad6c1f7e1546e00f96af64e82fc` |
| `lean/AuditSourceRecords.lean` | `f745bacb9b0ca54b783387d043d30621be6379811caacca3f2c12fd710924dfb` |
| `lean/SiblingPrefixLift.lean` | `419a972456767cd95af4ffc3fb3e8fd4dc69143de5f6818ba9116a21e26b2f45` |

See [the execution report](../../../../reports/2026-11-22-central-attempt/README.md)
for fresh integrated compilation. Source inspection, written proof review,
Lean compilation and the repository integrity gate are separate evidence.
