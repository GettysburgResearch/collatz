# Publication handoff — no new publication in this authoring session

**Status: UNPUBLISHED.** Date: 2026-09-21.

The previous work is already on GitHub as PR #132 at
`7687eec1ac364009d644cb8d015f1fe3b28730cc` (tree
`50e69780a9c5146e96d9dea4c1836dd4e918e228`). Its current metadata was
read back in this session. Do not duplicate or republish that packet.

This new packet is an addition-only continuation intended for
`research/astra-escape-restarts-20260921`, based on that exact head.
No new commit, branch, PR or issue comment was created here. Current
GitHub connector actions expose reads but not publication actions, and
direct Git transport failed DNS. The attached patch is not a claim of a
remote write.

## Added source locations

- `research/astra-exit-merging/escape-restarts/`: proof, guide, sources/limits.
- `experiments/X-AEM-007-escape-restarts/`: generator, exact kernel,
  independent verifier, contract harness, canonical summary and guide.
- `reports/astra-exit-merging-07/`: this handoff, draft PR text, execution
  receipt. Fresh publisher receipts should be separate additions.

Apply on a new branch based on the pinned parent, preserving all existing
proofs, statuses and original execution receipts. Recheck remote heads
before publishing. Keep the PR stacked on #132 until the base is integrated.
Do not merge or update main as part of this handoff.

## Replays

```sh
python -B -S experiments/X-AEM-007-escape-restarts/run.py --full aer-full.json --check experiments/X-AEM-007-escape-restarts/canonical.json
python -B -S experiments/X-AEM-007-escape-restarts/verify.py aer-full.json --summary experiments/X-AEM-007-escape-restarts/canonical.json --self-test
python -O -B -S experiments/X-AEM-007-escape-restarts/verify.py aer-full.json --summary experiments/X-AEM-007-escape-restarts/canonical.json --self-test
python -O -B -S experiments/X-AEM-007-escape-restarts/contract_check.py
```

On a complete actual checkout, also run the repository's normal validation
and bounded regression protocol. That full-checkout validation was NOT run
by this author. The standalone packet patch was applied in a fresh directory
and its verifier rerun; that is a different evidence tier.

## Review priorities

Check K's four positive-domain rows; B's actual K-to-R return; C's whole
cylinder; D's expanding G followed by the specifically guarded B; the common
D-2 inequality; exact finite-word inverse/forward congruence agreement;
strict initial rejection by the pinned #129 selector; original-source CRT,
independent clocks and whole-arm lower bound. In particular, neither G alone
nor every positive R parameter is claimed to contract under the new rules.

No independent mathematical acceptance is supplied. Numerical additions are
against #129 only, not the complete latest project collection. Full rows are
regenerable and need not be committed as a large artifact.
