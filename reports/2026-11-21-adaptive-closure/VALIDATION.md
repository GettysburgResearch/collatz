# Actual published-parent validation

The scientific commit was created through GitHub, its tree was compared
with the locally frozen tree, and that actual remote object was fetched
into a complete detached checkout before execution.

| Identity | Value |
| --- | --- |
| Scientific commit | `7bdbfcfd52312b373e86c47538b140fa9c71d745` |
| Scientific tree | `991288e889ac5b4722055f5badc90b44e5be685f` |
| Parent/main | `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` |
| Tracked files | 351 |
| Starting and ending checkout status | Clean |
| Frozen manifest entries | 34 |
| Manifest SHA-256 | `37848aedebe7d902b5f3337f6eb54cfaffd89b1f20f6e6d63199f31afc4112b5` |

## Scientific execution

Actual command:

```bash
python -X utf8 -B research/adaptive-closure-20261121/replay.py --receipt <outside-checkout>/adaptive-scientific-replay.json
```

All five programs were executed normally and with `-OO`: ten successful
executions, empty stderr, and exact byte agreement with every frozen
expected report. All manifest entries matched before execution, and the
checkout remained clean at the same head and tree afterward.

[Exact scientific receipt](published-scientific-replay.json), SHA-256
`448dbb0c06f5e31a2df2b52b4958c3d96fe7eefcb30b3e863a84fe8c9505e454`.
Execution finished at `2026-11-20T23:35:01.819955+00:00`.

## Complete repository gate

Actual command:

```bash
python -X utf8 -B tools/validate.py --regressions --receipt <outside-checkout>/adaptive-scientific-repository-validation.json
```

All eleven commands passed on the same scientific commit. This checks
repository structure, frozen identities, portability controls and the
selected bounded regression bundle. It does not prove the new theorems
or the Collatz conjecture.

[Exact repository receipt](published-scientific-repository-validation.json),
SHA-256 `aad7e3e47b186a3c73ec4a8049c8535161d700d8317ea31c15c5538a38bd6206`.
Execution finished at `2026-11-20T23:34:55.518091+00:00`.

## Documentation-child boundary

This child changes the report index and adds this note and the two exact
parent receipts. All scientific manuscripts, programs, bounded outputs,
review notes, and the manifest are unchanged. The child's parent,
exact tree, clean status and all 34 manifest identities are checked
after remote publication. The required repository gate is run again on
the child, while the ten scientific executions retain their actual
parent-commit attribution. Final receipts are preserved in the PR body
to avoid a self-referential commit identity.

No remote CI execution, accepted theorem-registry promotion, external
referee acceptance, or proof-assistant formalization is claimed.
