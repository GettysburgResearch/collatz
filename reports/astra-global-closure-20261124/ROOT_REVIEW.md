# Integration reconstruction and evidence boundary

The root reconstructed the main interfaces while integrating three parallel
research lanes. This is an integration review. The separate cross-agent reports
identify their own independent reconstruction and exact source hashes; neither
kind of review is external peer review or a proof of the conjecture.

Base: `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
Scientific entry point: [packet README](../../research/astra-global-closure-20261124/README.md).

## Mathematical checks

### Actual-source merger

The original reverse section is the one in #174 at
`c92cd473de3b85ceb945702a726d2eb7350a6af8`,
`research/psi-closure-20261121/lean/Collatz/Closure.lean`, `OpenLemma`:
for every j with 4 not dividing j, convergence of 3(27j+1)−1 implies convergence
of 27j+1. It is not its converse. The equivalence theorem does not supply this
universal implication.

For CS1 the three signed lifts are taken from the same prescribed ordinary
u. The extra factor three on the member arm is retained, giving exponent
22k−1, while the first and smaller-partner endpoints have exponent 21k.
The residue step uses only divisibility of the actual member endpoint by 1024.
The common ten-step endpoint for lifts of 52 and 68 then proves the exact
two-clock equality. Positivity and strict decrease are explicit in the Lean
conclusion. No convergence of the smaller partner is smuggled into the
algebraic certificate.

CS2 is stronger than separation of the original two arms: its written argument
considers every reduced forward-then-inverse walk. Its product comparison uses
the target of each forward odd step and the starting point of each inverse odd
step. The available small denominators depend on which single branch left the
negative cycle. Mixing denominators from all branches would invalidate this
argument. The independent review reconstructs that restriction, the candidate
tables after equal odd count, and the transfer from two mixed-adic residues to
each finite ordinary walk. The full all-walk inference is not a Lean claim.

For the shortest-length result, a modular unit equation constructs one ordinary
integer for each chosen precision. A full exponent period simultaneously gives
existence and the double-logarithmic size estimate. It does not choose fresh
sources during a proof about one fixed orbit. It does not cover every source.

### Finite causal affine rules

AR5 starts with total L and P transitions and the same per-letter clock/two-odd
coefficient law. A finite set of states makes the L recurrence bounded and
forces rational offsets x in [5,7] with odd reduced denominators. One integral
anchor produces an invariant numerator lattice on every reachable state.

The commutator is used on a finite *residue* permutation system. State
transitions need not be invertible. Positive words realize inverse residue
permutations because the latter have finite order, and both letters are
available at every intermediate state. That is why this step does not transfer
to a partial orbit-only machine. The subgroup gcd is 1 or 83 even for powers of
83. Selecting a residue before a sufficiently long L prefix both reaches the
forbidden fraction 4/D and removes the 3-primary numerator. This avoids assuming
that the ternary numerator was already zero at the chosen residue.

In the remaining 3-primary case, the proof synchronizes offsets after a bounded
word, not state identities. The offset is uniquely determined by its fractional
part. This yields exactly the full bounded-past model classified by AR2. All
six contracting slopes retain a denominator factor 83. The root helped refine
this reduction; [the separate review](structural/REVIEW_AFFINE.md) independently
reconstructed it afterwards.

### Physical series and the analytic extension

GS1 applies Bell–Smertnig to coefficients that are powers of a single rational
number. After a common period, monotonic exponents squeeze the geometric slopes
on different residue classes to equality. Eventual periodicity of physical
gaps then determines eventual periodicity of the ordinary orbit by the infinite
tail uniqueness, whose elementary integer core is formalized. A single 2-adic
evaluation does not establish rationality of a formal series. The positive real
and negative 2-adic evaluations in the injective-orbit discussion are different
limits, not an equality contradiction.

For GS2 the substitution gives an actual functional equation. Positivity keeps
its rational divisors nonzero; distinct affine fixed points keep the coefficient
of the zero-index series nonzero. The Jordan argument fixes the Padé degree
before sending the iteration index to infinity, so an uncontrolled slow-variable
degree contributes o(V). When the fast and slow roles change, the leading
weighted component either has a nontrivial moving transverse character or is
treated on the exact rational subtorus. The independent review checks the
nonvanishing step in all regimes. This is written mathematics dependent on the
stated coefficient theorem and standard height inequalities, not a Lean
transcendence proof.

The later #194 comparison is recorded separately. Its triangular substitution
result substantially overlaps GS2. The present packet makes no priority claim
for that theorem. The all-source clock-series criterion and the compiled
ordinary-tail uniqueness consumer are separately identified contributions.

## Executed formal checks

The compiler was Lean 4.34.1, release commit
`5045d0056413266e57c625dcd7c365b10e377c52`. Mathlib was at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Existing library oleans were used.
A cached copy of the runtime shared library used for the inherited-module batch
was byte-hash matched to the toolchain library (SHA-256
`6b30cc963d065fc9d2f87f7e9cbe0682b23000ae5425bccd769c5d477fa74f13`).
There is no claim of rebuilding the dependency stack or using another kernel.

All twelve packet Lean modules compiled with warnings as errors. The eight
inherited modules have a completed source-bound replay with **62 public axiom
reports out of 62**; the four new modules have 27 selected reports, including
their principal formal claims. Every printed transitive axiom list is contained
in `{propext, Classical.choice, Quot.sound}`. Final sources contain no `sorry`,
`admit`, custom mathematical axiom, or `native_decide` declaration.

The source attribution review compared all inherited theorem signatures,
hypotheses and definitions with their exact git blobs. Imports, header status,
audit directives and proof bodies were repaired; no premise was added. Eight
standalone final processes exited zero, with unchanged source hashes. See
[provenance](../../research/astra-global-closure-20261124/formal/PROVENANCE.md),
[correspondence review](audit/REVIEW_FORMAL.md), and
[completed receipt](formal/final-replay.json).

Initial failure logs are retained as development evidence. Some missing-name
failures came from narrowing broad imports. PhasePacking also needed a
positive-factor cancellation API update, deletion of already-solved tactics,
and an explicit use of its existing positivity hypothesis. CarryCocycle needed
three strict-linter sequencing repairs. Initial failed elaborations can print
`sorryAx`; those are not successful audits and are superseded by the final logs.

| Newly authored source | SHA-256 | Audit location |
|---|---|---|
| structural/CycleShadows.lean | 05ef6b77b2ce9d571c598e5a0e4a526be3412b844349476ec72408b0bf145e99 | structural/lean-audit.txt; independent analytic/structural_lean_review.json |
| audit/MemoryShadow.lean | 3c12919535f8951fb04c3f2cd74e2369409189adfc7db8ec03f8b50301b79a54 | audit/MemoryShadow.axioms.txt; audit/EXECUTION.md |
| audit/ResidueOrbit.lean | f5eb8ff6f62a344b289bbcec5bd2a13f762622a75445b1a25ee641764154a212 | audit/ResidueOrbit.axioms.txt; audit/EXECUTION.md |
| analytic/GapSeries.lean | b8f526ea2ad9593f7f1f2dfe7fc30fa6980fc80a32fd48c593159915fe2de7e0 | analytic/lean_receipt.json; analytic/GapSeries.log |

Finite controls were inspected at their stated ranges. Normal/optimized equality
is reported only where the worker actually performed both executions. The
independent structural reviewer also checked 127,842 reduced rational walks
through depth 30 and nine complete ordinary mergers. None of those counts is
used to replace an unbounded proof.

## Prepublication frontier readback

After the initial #146–191 snapshot, the remote exposed #192–194 and a later
attribution-only head for #189. The three new sources were fetched by exact
head and allocated to different reviewers. The late reports pin their source
versions and distinguish actual reconstruction from their authors' execution
receipts. They are not inputs to the already frozen new Lean proofs.

- [#192: actual phase and polynomial cycle factors](late/REVIEW_PR192.md)
- [#193: guarded partners, translated synchronization and true denominators](late/REVIEW_PR193.md)
- [#194: carry births and overlapping substitution rigidity](late/REVIEW_PR194.md)
- [Exact metadata](late/pr192-194.json)

The final repository gate is run only after committing this packet in a clean
complete checkout. It tests repository integrity and selected scoped self-tests,
not the infinite claims above. Its exact commit, tree and execution receipt
belong to the publication record. The scientific gap remains universal
ordinary-source closure, including the surviving cycles and exceptional paths.
