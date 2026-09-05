# Claim registry and status semantics

The registry is provenance infrastructure. Human mathematics lives in the [integrated packets](../research/integrated/README.md), with older source-pinned families in the [wider catalog](../research/RESULTS_CATALOG.md).

## Files

- [registry.json](registry.json), [canonical-1.json](registry/canonical-1.json), [canonical-2.json](registry/canonical-2.json), [roadmap.json](registry/roadmap.json) and [CANONICAL.md](CANONICAL.md) retain the original eight canonical and three roadmap records unchanged.
- [reviewed-2026-09-05.json](reviewed-2026-09-05.json) records four resident **reference assemblies**, their two immutable claim-level review matrices, source heads, proof residency, evidence policy and held replacements. It is a supplement, not a silent expansion of the canonical registry.
- [aliases.json](aliases.json) preserves historical aliases and repair relations and adds exact file-specific namespaces for colliding new claims and artifacts.

Residency does not verify a statement. A reference assembly does not turn all its source rows into accepted theorems.

## Independent status dimensions

`mathematical_status` describes the exact statement: verified, source-qualified, empirical, proposed, open, refuted or superseded. `integration_status` describes its repository role. `promotion_state` distinguishes accepted reference, accepted local proof, roadmap and retirement. `proof_residency` and `dependency_residency` separately say where proofs and load-bearing inputs reside.

`verified + accepted_with_local_proof` means an exact reviewed result has readable local proof. `source-qualified + accepted_reference_record + pending_narrow_review` preserves reviewed ingredients without accepting an unreviewed synthesis. A refutation accepted with local proof does not make its false original verified. A locally resident proof with source-pinned dependencies is not self-contained.

For the new assemblies, the exact row in the frozen review matrix is authoritative: VERIFIED, VERIFIED WITH FIXES, GAP-BLOCKED and REJECTED remain distinct. Source-author PROPOSED headers are retained as history. The technical wrappers and proposed endpoint replacements have their own integration receipts rather than a retroactive source verdict.

## Exact identifiers

The source identity is **(PR, full commit SHA, full repository path, claim ID)**. Even `PR90:T-ASTRA-030` or `PR92:T-A3-1051` is ambiguous. Use an explicit tuple or a file-specific display alias such as `CM-CLOCK:T-ASTRA-030` or `A3-SPECTRUM-PLATEAUS:T-A3-1051`, resolved through aliases.json. A display namespace is not a theorem promotion.

Older `PR<number>:<claim-id>` aliases remain usable only where the canonical record unambiguously supplies the exact source path and SHA. Source files and IDs are never silently renamed. An artifact needs its full path, source commit and schema together; a shared schema or experiment number does not identify a unique payload.

## Minimum integrated record

State exact scope and exclusions, source identity, review identity and verdict, dependency normalization/residency, proof/artifact evidence, aliases/repairs, and the local destination. Keep finite versus all-depth and ordinary versus 2-adic realization explicit. New wording or conjunctions need narrow review independently of their ingredients.

## Roadmap and replacement boundary

RD-SC-001 and RD-FC-001 remain accepted **OPEN obligations**. RD-BRIDGE-001 remains **PROPOSED** and its exact crosswalk is pending review. IC-PERIODIC-001 retains its separate pending synthesis flag. E-INTEGRATION-001/002 in [ERRATA.md](../research/integrated/ERRATA.md) are new proposed replacement wording, not accepted repairs of their unrestricted originals. None is a proof of Collatz.
