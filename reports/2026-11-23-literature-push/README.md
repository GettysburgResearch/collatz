# Literature-push evidence and review index

23 November 2026. Parent:
a9b23dcee61a4b65a63aa4e7ca653d875a405037.

The scientific entry point is
[the research README](../../research/literature-push-20261123/README.md).
These reports preserve source and execution boundaries. They do not
constitute a universal Collatz proof.

## Source snapshot and prior record

[REPOSITORY_SNAPSHOT.json](REPOSITORY_SNAPSHOT.json) records the 30
recently updated PR metadata records inspected at the start of this pass.
Each lane's ledger pins the exact source commit, file and read scope:
[arithmetic](arithmetic-sources.json),
[rigidity](rigidity-sources.json), and
[boundary](boundary-sources.json).

The previous PR178 title/body/head are preserved in
[PR178_PREVIOUS.json](PR178_PREVIOUS.json) and its
[Markdown body](PR178_PREVIOUS.md). They are historical records, not
the new checkpoint's claims.

## Written mathematical reviews

| Review | Scope and reviewer status |
|---|---|
| [boundary-arithmetic-review.md](boundary-arithmetic-review.md) | Independent reconstruction of the full arbitrary-pattern theorem, primitive word, complete polynomial gcd and full prime-power numerical bound. |
| [root-analytic-review.md](root-analytic-review.md) | Independent review of the scalar theorem, exact deflation, critical two-center criterion, finite-filter test, primary renewal application and source-qualified depth budget. |
| [boundary-general-density-review.md](boundary-general-density-review.md) | Independent review of the general-density addendum, including both maximum-principle estimates and the full arithmetic-germ hypotheses. |
| [rigidity-general-density-review.md](rigidity-general-density-review.md) | Additional reconstruction of the addendum; contribution of its initial hole estimate is explicitly disclosed. |
| [arithmetic-final-index-review.md](arithmetic-final-index-review.md) | Author integration check of research README Section 2 after the specified corrections. |
| [rigidity-index-review.md](rigidity-index-review.md) | Author integration check of Section 3 and the formal arithmetic scope. |
| [boundary-index-review.md](boundary-index-review.md) | Author integration check of Section 4, including the precise scaled-test error and positive-weight normalization. |

Each verdict binds listed source bytes and claim ranges. Author
integration checks are not counted as independent reviews of their
authors' theorem proofs. Upstream trace existence, reciprocal bounds
and selection inputs retain their source-qualified status.

## Formal arithmetic

The author receipts are
[rigidity-repunits-lean-receipt.json](rigidity-repunits-lean-receipt.json)
and [rigidity-packet-lean-receipt.json](rigidity-packet-lean-receipt.json).
Their proof boundaries are explained in
[the repunit proof report](rigidity-repunits-proof.md) and
[the packet proof report](rigidity-packet-proof.md).

[Root's independent build receipt](root-lean-review.json) records fresh
compilation of both source modules and both audit modules, with source
hashes checked against the frozen author builds. All 22 authored theorem
declarations and six definitions were audited. The axiom union is
propext, Classical.choice and Quot.sound.

[root-formal-review.md](root-formal-review.md) records the independent
statement-and-proof review and the exact boundary of that formal verdict.

Builds used Lean 4.34.1, compiler commit
5045d0056413266e57c625dcd7c365b10e377c52, mathlib
d13f23b723b8a846827a245b89c10fc7d3f11612, autoImplicit=false and
warningAsError=true. Existing mathlib objects were reused; the local
proof modules were rebuilt in a separate empty output directory.

The formal result includes the actual arbitrary-finite-pattern full
numerical gcd divisibility. The word construction, complete polynomial
gcd, denominator magnitude, potential theory and renewal theory are
outside this Lean boundary.

## Exact finite controls

[arithmetic-check-receipt.json](arithmetic-check-receipt.json) records
normal and optimized Python executions with identical results.
The corresponding outputs are
[normal](arithmetic-check-normal.json) and
[optimized](arithmetic-check-optimized.json).

The selected controls cover nine two-, three- and four-pattern examples,
three complete polynomial gcds over Q, 6,268 rational steps and 6,268
ordinary finite-realizer steps. They include a prime shared by the
residual factors, a nontrivial embedding gcd, a near-critical high-floor
example and two rejected hypotheses. They support exact formulas;
the universal family theorem is the written argument and the stated
formal arithmetic.

[Root's replay receipt](root-arithmetic-replay.json) and
[output](root-arithmetic-check.json) record independent execution and
byte-identical agreement with the author output.
[boundary-arithmetic-controls.json](boundary-arithmetic-controls.json)
records the separate reviewer's independently constructed four controls,
including two direct complete polynomial gcd calculations.

## Frozen bytes and exact release

The lane freeze manifests are
[arithmetic](arithmetic-freeze.json),
[boundary](boundary-freeze.json),
[rigidity](rigidity-freeze.json),
[repunit core](rigidity-repunits-freeze.json), and
[packet arithmetic](rigidity-packet-freeze.json).

[FROZEN_CHECKS.json](FROZEN_CHECKS.json) records the final prepublication
hash checks. [MANIFEST.json](MANIFEST.json) binds all files in this
checkpoint except itself, with the fixed parent commit.

After the new commit exists, the required command is executed on its
clean, complete detached checkout:

    python -X utf8 -B tools/validate.py --receipt <outside-checkout>

The resulting receipt is external to that commit to avoid a
self-reference. The PR release record preserves its exact commit, tree,
file count, checks and receipt hash, and remote readback verifies that
the branch and PR point at the tested commit. This gate checks repository
integrity and its stated bounded controls; it does not prove Collatz or
formally validate the written analytic arguments.
