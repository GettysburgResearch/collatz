# Replay policy and evidence tiers

Proof reconstruction, artifact inspection, finite regeneration, a checker run, complete encoded-corpus replay, an external formal build and large native-payload replay are distinct events. An artifact hash is an identity, not a proof. [A's evidence](../reports/prepublic-2026-09-05/reviewer-a/EVIDENCE.md), [B's validation](../reports/prepublic-2026-09-05/reviewer-b/VALIDATION.md), and [D's final handoff](../reports/prepublic-2026-09-05/reviewer-d/FINAL_HANDOFF.md) remain frozen historical records.

## One checkout, one receipt

Use Python **3.11+**, Git, and a clean complete checkout. No extra Python packages are required for these validation commands.

```bash
python -X utf8 -B tools/validate.py
python -X utf8 -B tools/validate.py --regressions --receipt ../collatz-validation.json
```

The default command checks the original registry/reading path, A/B's identities and preservation contracts, the portability fixtures, and D's exact follow-up. `--regressions` adds both D bounded suites and the fixed-height replay in normal and optimized interpreter modes. It does not run old large searches or external Lean builds. Every child command retains its own scope and failure status.

The optional JSON receipt records the actual commit, tree, interpreter, commands, output and exit codes, including failures. It must be written outside the checkout. The driver refuses dirty, incomplete or sparse inputs and checks the tracked state again afterward. It does not reset, clean or discard work. Use a separate clean checkout when necessary.

The [GitHub workflow](../.github/workflows/validate-repository.yml) invokes the same command on an ephemeral Linux runner and prints its receipt into the run log. It has only `contents: read`, a commit-pinned checkout with credentials not persisted, no repository secrets, no shared cache and no deployment. It uses ordinary PR/push events, never privileged PR-target execution. A workflow file is not a successful run: consult the [launch gates](PUBLIC_RELEASE_GATES.md) for the currently missing execution receipt.

## Windows and exact bytes

New checkouts use LF rules in `.gitattributes`. Do not use `git add --renormalize` to alter frozen evidence or rewrite a report until its hash passes. A clean clone with automatic CRLF conversion disabled avoids inherited client configuration. Preserve any local work before creating another checkout.

On Windows the A/B checker reads executable/symlink **modes** from the Git index, because the filesystem does not reproduce POSIX executable bits. It still hashes the **actual working-file bytes** and compares the resulting tree to the original frozen SHA. Changed bytes, CRLF conversion, missing/extra files, altered index modes and unresolved merges remain failures. On POSIX the existing filesystem-mode check remains active. The checked-in real-Git fixtures exercise portable mode selection; simulated Windows metadata behavior is not a native Windows full-checkout receipt.

```bash
python -X utf8 -B tools/test_integrity_portability.py
python -X utf8 -B tools/test_validation_driver.py
```

## Supported interpreter modes

Use `python -B` for historical generators and verifiers unless their entry point explicitly supports optimization. Generators may write reports; a regenerating command is not an immutable check.

`experiments/X-ASTRA-003-run-renewal/verify.py` and `experiments/X-ASTRA3-002-three-routes/verify.py` refuse `-O` and `-OO` before loading a source or report. Normal execution authenticates and delegates to byte-identical `_verify_source.py`. That underscore file is provenance, **not a supported direct entry point**. The original assertion-only optimized acceptance remains an identified defect. No historical corpus replay is inferred from wrapper changes. X-ASTRA-004 already had its own guard and is not assigned the same defect.

Later fifth-pass verifiers have explicit checks and B's normal/optimized payload replays. Those receipts do not cover earlier scripts or future edits. Generator/internal assertions are not made optimization-safe by an accompanying safe verifier.

## Nonmutating fixed-height replay

PR87 and PR88 have different protocols with originally colliding names. PR87 retains `check_fixed_height_attack.py` and `fixed-height-check-report.json`. PR88's complete frozen variant is in `archive/research-2026-09-05/pr88-source/`; its active report is `fixed-height-forward-check-report.json`.

```bash
python -B research/external/mazur-2026/check_fixed_height_forward.py --self-test
python -O -B research/external/mazur-2026/check_fixed_height_forward.py --self-test
```

This entry point authenticates the archived source, runs it with optimization disabled in a temporary directory, and compares the complete regenerated JSON without overwriting either active report. Full-payload equality checks mathematics, scope and coverage; four resealed mutations cover scope, missing rows, count and warning fields.

The prior integration authenticated the 8,617-byte source against Git blob `bc2c9874e1126756260d7ec6b79bc929609a34f2` and its 5,121-byte report against `247cee3eb8a44f91031e0148dbf84b5d1fb2c6b0`; semantic digest `d78c7b1e04c04aba446bff07899331cf4765eef2b85b9de9b428690fec7f3558`. Its recorded wrapper executions passed with four mutations rejected in each mode. This is finite depth-16 evidence, not a fixed-floor theorem; the receipt is not relabeled as a new run.

## Preserved evidence ceilings

A reconstructed narrow arithmetic, fans, intervals and counterexamples, not every complete PR90 corpus/hash. B replayed PR91 and both fifth-pass payloads with 22 resealed tests; older PR92 protocols retain their inspected/partial status. D checked its separately enumerated clauses and bounded regressions, not the entire recent corpus. Integration and passing software tests do not upgrade those evidence tiers.

External PDF fingerprints and build receipts remain attributed to their author/importer. No external Lean build, large predecessor-payload replay or independent PDF rehash is claimed by this readiness pass. Floating diagnostics in import scripts are not exact integer comparisons. No external PDFs or binary payloads are redistributed here.

## Individual structural commands

```bash
python -X utf8 -B tools/check_integration_state.py
python -X utf8 -B tools/check_review_integration.py
python -X utf8 -B tools/check_review_integration.py --self-test
python -X utf8 -B reports/prepublic-2026-09-05/integration-d/check_followup.py --self-test
```

These check structure, source identity and declared status, not Collatz. Frozen A/B assignments and D's separate follow-up remain distinct. The [earlier integration receipt](../reports/prepublic-2026-09-05/integration/README.md), [D integration receipt](../reports/prepublic-2026-09-05/integration-d/README.md) and [current preparation receipt](../reports/readiness-2026-09-06/README.md) state exactly what each session executed. No fixture run is a substitute for a complete-checkout receipt.
