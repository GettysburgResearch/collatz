# Publication validation

## Actual scientific input

The scientific commit was created on GitHub, fetched into the working
branch, compared with the complete staged tree, and then checked out in a
separate full clone. These executions are attributed to that fetched commit:

| Item | Value |
|---|---|
| Scientific commit | `9acf568f44c5ca655265b888fc27c5b37f1f10db` |
| Scientific tree | `6757a91322d9d5c0a2e20a06653eb391fe98732d` |
| Parent main commit | `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` |
| Tracked paths in the scientific checkout | 369 |
| Frozen manifest paths | 51 |
| Manifest SHA-256 | `71052d28fc99c311c711c702157e0409276263344b3bec9b84545decc75e2c33` |
| Checkout condition | Complete and clean before and after both runs |

[Scientific commit on GitHub](https://github.com/GettysburgResearch/collatz/commit/9acf568f44c5ca655265b888fc27c5b37f1f10db).
The actual checkout was
`/workspace/scratch/957bb0caa6f2/collatz-global-verify-9acf568`.
No sparse checkout, skip-worktree entries, missing tracked files, or dirty
tracked/untracked files were accepted by the packet runner.

## Executed checks

| Execution | Actual scope | Result |
|---|---|---|
| Packet replay | 14 author/reviewer programs, each under normal and `-OO` Python | 28 successful executions |
| Complete output comparisons | All 14 deterministic reports in both modes, plus the exceptional ordinary-prefix artifact in both modes | 30 complete-byte matches |
| Frozen content checks | All 51 manifest paths and the manifest itself before and after | Unchanged and matching |
| Repository gate | `tools/validate.py --regressions` | All 11 commands passed |

The packet execution ran from `2026-11-20T23:49:57.601332+00:00` to
`2026-11-20T23:50:03.110678+00:00`. The repository gate ran from
`2026-11-20T23:49:57.587664+00:00` to `2026-11-20T23:50:02.408380+00:00`. These recorded times are UTC.
The two checks used the same read-only scientific checkout and distinct
receipt paths outside it. They both retained the same head and tree.

The actual invocations were:

```sh
python -X utf8 -B reports/2026-11-21-global-certificate-closure/verify_packet.py --receipt /workspace/scratch/957bb0caa6f2/global-certificate-science-receipt.json
python -X utf8 -B tools/validate.py --regressions --receipt /workspace/scratch/957bb0caa6f2/global-certificate-repository-receipt.json
```

The earlier dirty preflight is not substituted for these publication runs
and is not the receipt attached here. The packet receipt records actual
arguments, execution modes, command statuses, durations, output hashes,
complete comparison results, and before/after Git and manifest states.
The repository receipt retains its complete command output.

## Attached evidence

| Receipt | SHA-256 |
|---|---|
| [Scientific replay](science_receipt.json) | `3ad78968c720a07bad410ce6117226efcec5e0e6aa2344173324a3d0a1a20d28` |
| [Repository integrity and bounded regressions](repository_receipt.json) | `28cd7f9216735771c0984f7251f0296ec38ea939c30cec6bab03bc34c67de015` |

The later documentation-only child attaches these two receipts and updates
only this file and the report README. Its scientific files, deterministic
reports, runner, source snapshot, and manifest are unchanged from the
scientific commit. The attached receipts certify executions at that
scientific commit, not a fictional earlier execution at the later child.

These checks establish repository integrity, reproducible finite exact
calculations, and consistency with frozen reports. The all-parameter
mathematical statements rely on the written proofs and separate internal
reviews. No remote CI, Lean build, external referee acceptance, or full
Collatz proof is claimed.
