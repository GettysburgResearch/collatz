# Replay policy and evidence tiers

A proof reconstruction, artifact inspection, finite regeneration, checker run, full encoded-corpus replay, external formal build and large native-payload replay are distinct events. An artifact hash is an identity, not a proof of its mathematical content. [A's evidence](../reports/prepublic-2026-09-05/reviewer-a/EVIDENCE.md) and [B's validation](../reports/prepublic-2026-09-05/reviewer-b/VALIDATION.md) are preserved unchanged.

## Supported interpreter modes

Use `python -B` for historical generators and verifiers unless a particular entry point explicitly documents optimized support. Generators may write reports; do not treat a regenerating command as an immutable check.

`experiments/X-ASTRA-003-run-renewal/verify.py` and `experiments/X-ASTRA3-002-three-routes/verify.py` now refuse `-O` and `-OO` before loading a source or report. Normal execution authenticates and delegates to the byte-identical `_verify_source.py` alongside it. The underscore file is retained for provenance and is **not a supported direct entry point**. The old assertion-only optimized acceptance remains an identified defect of the original bytes. No entire historical corpus replay is inferred from this wrapper change. X-ASTRA-004 already had its own optimized-mode guard and is not assigned the same defect.

Later fifth-pass verifiers have explicit checks and Reviewer B's normal/optimized payload replays. That evidence does not automatically extend to earlier scripts or future edits. Source generators/internal assertions are not advertised as optimization-safe merely because their accompanying verifier is safe.

## Nonmutating fixed-height replay

PR87 and PR88 have different finite protocols with colliding original names. PR87 retains its own `check_fixed_height_attack.py` and `fixed-height-check-report.json`. PR88's entire frozen source variant is in `archive/research-2026-09-05/pr88-source/`; its active report has the distinct name `fixed-height-forward-check-report.json`.

From the repository root:

```bash
python -B research/external/mazur-2026/check_fixed_height_forward.py --self-test
python -O -B research/external/mazur-2026/check_fixed_height_forward.py --self-test
```

The new entry point authenticates the archived source, runs it with optimization disabled in a temporary directory, and compares the complete regenerated JSON. It never rewrites either active report. It checks mathematics, scope and coverage by full-payload equality, not just a resealable digest. Four resealed mutations test scope, missing rows, count and warning fields.

During integration the exact 8,617-byte original checker matched Git blob `bc2c9874e1126756260d7ec6b79bc929609a34f2`. Its regenerated 5,121-byte report matched Git blob `247cee3eb8a44f91031e0148dbf84b5d1fb2c6b0`; semantic digest `d78c7b1e04c04aba446bff07899331cf4765eef2b85b9de9b428690fec7f3558`. Both new wrapper commands passed with all four resealed mutations rejected. This remains finite evidence through the source's declared depth 16, not a fixed-floor theorem.

## Preserved evidence ceilings

Reviewer A independently reconstructed narrow arithmetic, fans, headline intervals and counterexamples, but did not replay all complete PR90 encoded corpora or their aggregate hashes. Reviewer B replayed PR91 and both fifth-pass verifier payloads with 22 resealed tests; older PR92 protocols remain inspected/partially reconstructed. Integration has not upgraded those evidence labels.

The external dossier's PDF fingerprints and recorded build receipts are attributed to their original author/importer. No external Lean build, large predecessor payload replay, or independent PDF rehash was performed in this integration. Some import-checker quantities are floating diagnostics; exact integer comparisons must not be conflated with them. No PDFs or external binary payloads are redistributed by this integration.

## Structural commands

```bash
python -B tools/check_integration_state.py
python -B tools/check_review_integration.py
python -B tools/check_review_integration.py --self-test
```

These check repository structure, identity, source preservation and declared status boundaries, not Collatz. Report a full-checkout run only when it actually happened. The integration-session environment has connector access but no authenticated local checkout; see [launch gates](PUBLIC_RELEASE_GATES.md) and the exact [integration receipt](../reports/prepublic-2026-09-05/integration/README.md).
