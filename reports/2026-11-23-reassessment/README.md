# Reassessment evidence index

23 November 2026. Parent:
c91b80a3156e640ad471cf30c47721145ae21eb1.

**Full Collatz remains OPEN.** This directory records provenance and
verification for the additive packet
[research/reassessment-20261123](../../research/reassessment-20261123/README.md).
It does not change earlier packets or their byte-bound reviews.

## Research and independent review

| Lane | Written result | Independent reviewer and scope |
| --- | --- | --- |
| Construction | Finite exponential lower bound for the inherited same-source canonical stream; precise unresolved upper estimate | /root; [construction-review.md](construction-review.md), complete written argument and used primary statements |
| Collision | Universal finite-clock explosion, exact capacity flux, and all-template actual-source repeat budget | source_construction; [construction-collision-review.md](construction-collision-review.md), written arguments and a fresh strict Lean build |
| Cycle | Source-qualified ordered-group additive-potential classification, finite ordinary circulation, and failed complete-gcd upper target | actual_collision; [collision-cycle-review.md](collision-cycle-review.md), primary semigroup input, written deductions and a fresh strict Lean build |

The collision review verdict is **VERIFIED WITH FIXES**: the author repaired
the later-window repeat bound to retain the noncycle condition at that
actual window. The corrected bytes are recorded in
[collision-freeze.json](collision-freeze.json) and
[construction-collision-review-freeze.json](construction-collision-review-freeze.json).

The first cross-route synthesis has a separate narrow scope review:
[cycles-integration-scope-review.md](cycles-integration-scope-review.md).
It binds the stated synthesis hash and is not a re-audit of all its sources.

## Formal scope

The author receipts are
[collision-lean-receipt.json](collision-lean-receipt.json) and
[cycles-lean-receipt.json](cycles-lean-receipt.json).
The independent receipts are
[construction-collision-lean-review.json](construction-collision-lean-review.json)
and [collision-cycle-lean-review.json](collision-cycle-lean-review.json).

Four authored/audit source files were built, in two module pairs. All 14
authored theorem declarations were audited. The only reported axioms are
propext, Classical.choice, and Quot.sound. One finite product theorem
uses no axioms. Strict warning settings were enabled.

The formal scope is the deterministic summability inequality and its flow
floor, plus the five exact ordinary edges, product identities, finite
additive-potential obstruction and integer hyperbola identity. The global
semigroup classification, stochastic-process and flux consequences, growth
gap and repeated-word deduction are independently reviewed written
mathematics. No complete Collatz theorem is asserted by these builds.

Lean: 4.34.1, compiler
5045d0056413266e57c625dcd7c365b10e377c52.
Mathlib: d13f23b723b8a846827a245b89c10fc7d3f11612.
Pinned dependency objects were reused; all new project modules were built
by both author and reviewer. The older proof corpus was not rebuilt.

## Source provenance and publication

- [REPOSITORY_SNAPSHOT.json](REPOSITORY_SNAPSHOT.json) inventories all 145
  fetched PR records at the reassessment snapshot, plus the unchanged main
  and the parent of this work. This is a repository-orientation inventory,
  not 145 independent proof reviews.
- [construction-sources.json](construction-sources.json),
  [collision-sources.json](collision-sources.json), and
  [cycles-source-ledger.json](cycles-source-ledger.json) give each lane's
  immutable source pins and primary literature.
- PR178_PREVIOUS.json preserves the exact previous title and body at the
  parent head; PR178_PREVIOUS.md is its readable copy with trailing spaces
  removed.
- MANIFEST.json binds every new packet and report file except itself.
  Review and compilation hashes must still agree with the committed bytes.
- The required default tools/validate.py gate is run separately on a clean,
  complete detached checkout of the new commit, with its receipt outside the
  checkout. The resulting commit, tree, receipt and validation scope are
  recorded in PR178 after creation. Integrity checks do not prove new
  mathematics.
