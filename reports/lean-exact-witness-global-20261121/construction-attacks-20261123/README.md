# Construction attacks: execution, source, and review record

23 November 2026. **Full Collatz and the original residue-512 implication
remain OPEN.**

[Scientific packet](../../../research/lean-exact-witness-global-20261121/construction-attacks-20261123/README.md)
· [Root execution receipt](ROOT_REPLAY.json)
· [Source ledger](SOURCES.json)
· [Latest PR metadata snapshot](LATEST_PR_SNAPSHOT.json)

This checkpoint contains four new arguments and four new Lean modules.
It continues remote PR177 at `3124c03a6a672cb70cdd5604eaf2d4eb19a467e3`.
The corresponding local parent is `1f6c718ce598d83009c8295556b39342353ac8a8`;
both have tree `9e468ca108726fba529adf7a2d8611e62341274d`.

## New results and exact formal scope

| Lane | Written result | New Lean declarations | Lean boundary |
| --- | --- | ---: | --- |
| [Template selection](descent/README.md) | All-exponent two-power gap; every nonintegral actual prefix-template score exceeds its source; finite minimization and cycle equivalence | 13 | Finite ordinary algebra, carry/center consumers, descent window, horizon and sublevel bounds, supplied-word compiler; the analytic gap and global cycle equivalence are written |
| [Full ordinary sources](transport/README.md) | Same-root projection, complete weighted fibers, finite free-energy certificate, full/unit pressure comparison | 6 | Ordinary reachability, height and finite mass aggregation; countable geometric fibers and Green-function analysis are written |
| [Witness charge](witness/README.md) | Exact merger classifications, infinite four-step all-clock obstruction, finite-seed power obstruction, unbounded joint-edit cost | 21 | Complete-charge uniqueness, literal cylinder lifts, half/power germ consumers, four-step profiles and barriers, alignment bound; general rational-slope interpretation and displayed affine cell are written |
| [Arithmetic germ](germ/README.md) | Density-free criterion with explicit complex and ternary radius bounds | 6 | Explicit positive potential-game strategy and integer inverse identities; analytic rationality and infinite germs are written |

Total: **46 newly audited declarations**. The two unchanged descent
dependencies contain earlier declarations which are not counted again.
Matveev's theorem and Chambert-Loir--Nous's theorem are external primary
inputs in written proofs. No custom Lean axiom represents either theorem.

## Actual executions

`ROOT_REPLAY.json` records twelve final root executions: strict compilation
of each of the four new modules, and normal/optimized executions of each
of the four exact finite checkers. It includes full argv, cwd, selected
environment differences, timestamps, exit codes, stdout/stderr hashes,
source hashes and printed axiom audits. The transport lane is refreshed
after the nonempty-source correction; other lanes retain their unchanged
final executions. Every recorded command exited zero, every pair has
byte-identical checker output, and every declaration's axiom set is a
subset of `propext`, `Classical.choice`, and `Quot.sound`.

Runtime: Lean4.34.1, compiler
`5045d0056413266e57c625dcd7c365b10e377c52`; Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The witness module uses
`Std`. The other three use the pinned Mathlib environment. The descent
module also imports two unchanged local modules whose fresh producer
builds and exact artifact hashes are recorded; root reuses those exact
artifacts rather than replaying an old whole-proof suite.

| Exact finite control | Coverage |
| --- | --- |
| Template selection | 8,190 words, 24,570 actual traces, 24,393 nonintegral cases, 14,984 native-window descents, 1,023 complete-witness compilers; all 26 continued-fraction digits through the cutoff |
| Full-source projection | 25 predecessor pools, 13,700 actual atoms, 126,062 suffix steps, 201 complete finite fiber rectangles with 7,035 atoms; failed stronger height/multiplicity/projection claims retained |
| Witness charge | 49 half-germ and 1,770 power-germ classifications, 2,496 cylinder controls, 640 terminal-cycle controls, lifted positive families, retained four-step tuples, one exact finite closed-product edit optimum |
| Deflated actual germ | 153 known convergent sources, 4,107 ordinary steps, 4,260 coefficient equalities, 64 inverse coefficients; strict rational capacity margins and failed fitted-germ controls |

These finite controls validate the algebra, implementations and finite
certificates with their stated scope. They do not establish convergence
for untested sources. In the template proof, the infinite large-exponent
range comes from the explicit analytic argument, not extrapolation of
the finite checks.

## Independent internal reviews

| Frozen object | Reviewer | Record and verdict |
| --- | --- | --- |
| Template manuscript, module, checker | `finite_mass`, not an author or contributor of its carry bound | [REVIEW_TEMPLATE_SELECTION.md](reviews/REVIEW_TEMPLATE_SELECTION.md): VERIFIED at stated scope; primary Matveev interface and separate exact CF replay |
| Full-source manuscript, module, checker | `witness_construction`, not an author | [REVIEW_UNIT_PROJECTION.md](reviews/REVIEW_UNIT_PROJECTION.md): VERIFIED WITH FIXES; normalized trials require nonempty G and N>=1 |
| Witness manuscript, module, checker | `macro_selection`, not an author | [REVIEW_WITNESS_CHARGE.md](reviews/REVIEW_WITNESS_CHARGE.md): VERIFIED at stated scope; independent strict compile and exact checker replay |
| Density-free germ manuscript | `finite_mass`, not an author | [REVIEW_DENSITY_FREE_GERM.md](reviews/REVIEW_DENSITY_FREE_GERM.md): VERIFIED at stated written source-qualified scope; primary local-domain/game hypotheses and frozen cycle selection reconstructed |

The source hashes in each review delimit its verdict. Root contributed
the carry-maximization idea to the template lane and authored the germ
lane; root's additional reconstructions are not counted as independent
reviews. These are internal research reviews, not an external peer-review
or a certification of the full Collatz conjecture.

The independent CF implementation and actual result are preserved as
[review_template_cf.py](reviews/review_template_cf.py) and
[template_cf_review.json](reviews/template_cf_review.json). It imports no
author checker and does not repeat the ordinary-word census.

## Latest sources and publication boundary

The continuation refreshed the fifteen most recently updated PR records.
It read the complete new PR182 arithmetic-germ selection note, and the
two relevant PR178 density/filter notes, at exact heads. PR175's new
body was read for orientation; its underlying new risk26 sources were
not reviewed here. The previous checkpoint's all-PR inventory remains
its own historical evidence. This distinction is recorded in
`LATEST_PR_SNAPSHOT.json` and `SOURCES.json`.

Publication uses the owned PR177 branch with a checked expected head.
After a local commit, the required default repository validator is run
in a clean complete checkout with its receipt outside that checkout.
The PR body records the checked local commit/tree, validator receipt
hash, final published commit/tree/parent, and the remote read-back.
Repository integrity is not counted as mathematical evidence.

`FILES.json` binds the changed files of this checkpoint except itself.
Older manifests describe their original commits. In particular the
cumulative index is deliberately updated here; an earlier index hash
is not a claim about the new tree. No older scientific proof file is
modified by this checkpoint.

## First unsupported construction

The all-template theorem does not build an ordinary descent; the
rank/cycle equivalence does not exclude cycles. The source projection
does not construct the absolute moving-root mass. The charge barriers
do not rule out general pointwise mergers and do not construct their
successful unbounded edit budgets. The analytic criterion does not
construct the complete actual rational germ or its two radius bounds.
These are the exact open continuations; no successful universal output
certificate is claimed.
