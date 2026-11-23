# Global-closure execution and review record

Date: 23 November 2026. Repository: GettysburgResearch/collatz.
Base: 2169884b64871b448cda16c7d74a0d5914ed870b.
Publication destination: [PR178](https://github.com/GettysburgResearch/collatz/pull/178),
branch research/lean-global-20261121.

The [scientific entry point](../../research/global-closure-20261123/README.md)
contains the claims and remaining global obligations. This report records
what was actually checked, without treating repository integrity, source
inspection or a conditional closing theorem as proof of universal Collatz.

## Research and review roles

| Role | Work |
|---|---|
| closure_dual | Constructed the triadic paired-state rank, its concrete Lean trajectory, the finite congruence certificate and the coupled-carry attempt |
| closure_collision | Attempted the actual same-law collision upper through ordinary pressure measures and repeated-word arithmetic |
| closure_cycle | Attempted unrestricted cycle exclusion with Mahler rigidity and the complete integral character lattice |
| coordinating root | Refreshed all PR metadata and selected sources, revisited global ordinal orders, contributed the bounded-numerator estimate used in the finite triadic horizon and the linear-density pressure comparison with its uniform exponent bound, reconstructed the new arguments and coordinated publication |

The root's contributions are disclosed: root synthesis is not counted as
an independent review of those results. The cycle reviewer reconstructed
the finite horizon independently, and the duality reviewer independently
checked the linear-density pressure comparison.

The review records are narrowly scoped, identify exact file hashes, and
remain internal mathematical reviews:

- [duality-review.md](duality-review.md): independent reconstruction of the
  paired-state theorem and finite arithmetic certificate, with a fresh
  strict Lean compile and axiom audit.
- [escape-review.md](escape-review.md): independent reconstruction of the
  ordinary off-diagonal estimate, actual density costs, critical-scale
  comparison and common-source collision.
- [cycles-review.md](cycles-review.md): full-word polynomial and torus
  calculations; source-qualified use of Adamczewski--Bell.
- [order-review.md](order-review.md): the narrowly stated direct ordinal
  interpretation obstruction and terminating two-rule subsystem.

The cycle review requested that “integral triangular diagonalization” mean
one **by an integral triangular torus automorphism**. The author corrected
that wording before the final reviewed hashes. The order review requested
explicit rule names in its step-count paragraph, also fixed before hashing.

## Formal execution

Both new implementation modules and their dedicated audit modules were
compiled freshly with Lean 4.34.1, commit
5045d0056413266e57c625dcd7c365b10e377c52, against the read-only Mathlib
checkout d13f23b723b8a846827a245b89c10fc7d3f11612.

| Module | Authored public theorem declarations | Formal scope |
|---|---:|---|
| TriadicDualClosure | 12 | Exact rational update, all-odd-tail contradiction, nonzero all-time numerator, rank decrease, concrete paired trajectory and all-time candidate convergence |
| PressureCollisionCore | 10 | Finite pair-density comparison, retained-atom density cost, repeated affine-word divisibility and one literal common-source word collision |

The triadic audit also covers its six public definitions, two
inductive/structure declarations, and selected generated constructors and
projections. The theorem counts are inventories of formal declarations,
not claims that every mathematical ingredient was newly discovered.
In particular the repeated-block divisibility is explicitly credited to
the preceding PR178 work and re-expressed in a self-contained finite form.

All listed theorem audits depend only on subsets of
propext, Classical.choice and Quot.sound. No sorryAx or custom research
axiom occurs in the audited declarations. Warnings were treated as errors.

Evidence:

- [duality-lean-receipt.json](duality-lean-receipt.json),
  [compile log](duality-lean-compile.log),
  [axiom log](duality-lean-axioms.log),
  [replay instructions](duality-replay.md).
- [escape-lean-build.json](escape-lean-build.json),
  [axiom log](escape-lean-audit.log).
- [duality-review.md](duality-review.md) records the additional independent
  fresh compile and audit of that source.

Installed Mathlib/package objects were reused. No old research proof corpus
was rebuilt. The finite horizon H and its sufficient congruence are written
proofs, independently reconstructed; they are not represented as checked
Lean declarations. The infinite measure estimates and the torus arguments
also retain written-proof scope. The complete published proof of the
external Mahler theorem was not independently reconstructed.

## Source scope

The [full metadata snapshot](../../research/global-closure-20261123/SOURCE_SNAPSHOT.json)
contains all 145 refreshed PR records, with 122 open at access time.
This is an inventory, not a review verdict on every branch.

The [late refresh](../../research/global-closure-20261123/LATE_REFRESH.md)
records a further PR176 advance and exactly two additional source reads.

Exact scientific source inspections are recorded in:

- [duality-sources.json](duality-sources.json);
- [escape/SOURCES.json](../../research/global-closure-20261123/escape/SOURCES.json);
- [cycles-sources.md](cycles-sources.md);
- the pinned rule, PR141 and ordinal references in
  [ORDER_CONSTRUCTION_ATTEMPT.md](../../research/global-closure-20261123/ORDER_CONSTRUCTION_ATTEMPT.md).

The current main README, research map, relevant catalog entries,
AGENTS.md and scoped errata were read before those arguments were reused.
The preceding PR178 description is preserved in
[the archive](archive/pr178-before-global-closure.md).

## Publication integrity

The required final-commit command is:

    python -X utf8 -B tools/validate.py --receipt <outside-checkout-path>

It is run in a clean complete checkout of the actual created Git commit.
The exact command result, tracked-file count, tree/parent identity, clean
before/after status, receipt and final remote-readback record appear in the
updated PR178 description. Keeping that final receipt outside its own
commit avoids a self-referential execution record.

The added-file manifest is [FILES.json](FILES.json). It hashes the new
packet and reports, excluding the manifest itself. The API-created tree is
compared with the local staged tree before publishing; the branch update
uses the expected prior head rather than overwriting a concurrent update.

The default gate is an integrity check. It does not certify a literature
theorem, an infinite analytic argument or the universal existence of a
triadic witness.

## Unresolved claims

The all-time triadic candidate theorem closes an actual supplied witness.
It does not construct that witness for arbitrary n. The finite certificate
makes the required height saving explicit, without proving it.

The pressure off-diagonal estimate is for the ordinary pressure measure.
The needed same-law upper bound for the moving inverse endpoint law is
still unproved. The quantitative obstruction applies to the global density
comparison actually analyzed, not all possible bilinear estimates.

The minimal torus degree is the full numerical denominator, but degree one
has not been excluded for every nontrivial primitive positive word.
The direct ordinal-interpretation observation does not exclude a different
source-dependent termination order.

Universal convergence, universal escape exclusion and unrestricted positive
cycle exclusion remain OPEN.
