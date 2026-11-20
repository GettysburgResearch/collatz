# Publication validation

## Actual scientific input

The scientific commit was created on GitHub and its tree matched the local
staged tree. The attached executions use a separate direct GitHub clone,
with complete reachable history, checked out at that same scientific
commit. These executions are attributed to the fetched commit:

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
`/workspace/scratch/957bb0caa6f2/collatz-global-direct-verify`.
No sparse checkout, skip-worktree entries, missing tracked files, or dirty
tracked/untracked files were accepted by the packet runner.

## Git history correction before publication

A local clone used in the earlier documentation commit
`4a18d0930b3936b23f8403ce7f770324576b925f` had every tracked scientific
file, and its checks passed, but it omitted two ancestor objects from the
source's shallow history. That clone is not the input of the attached
receipts. It was replaced with a direct GitHub clone and both complete
publication commands were rerun.

The direct clone reports `git rev-parse --is-shallow-repository` as
`false`. `git rev-list --objects --missing=print` at the scientific commit
reports 928 reachable objects and no missing objects. The checkout contains
all 369 tracked paths and is clean. The new receipts below supersede the
earlier local-clone receipts; the scientific tree and frozen reports did
not change.

## Executed checks

| Execution | Actual scope | Result |
|---|---|---|
| Packet replay | 14 author/reviewer programs, each under normal and `-OO` Python | 28 successful executions |
| Complete output comparisons | All 14 deterministic reports in both modes, plus the exceptional ordinary-prefix artifact in both modes | 30 complete-byte matches |
| Frozen content checks | All 51 manifest paths and the manifest itself before and after | Unchanged and matching |
| Repository gate | `tools/validate.py --regressions` | All 11 commands passed |

The packet execution ran from `2026-11-20T23:54:32.014720+00:00` to
`2026-11-20T23:54:37.606317+00:00`. The repository gate ran from
`2026-11-20T23:54:32.022538+00:00` to `2026-11-20T23:54:36.819473+00:00`. These recorded times are UTC.
The two checks used the same read-only scientific checkout and distinct
receipt paths outside it. They both retained the same head and tree.

The actual invocations were:

```sh
python -X utf8 -B reports/2026-11-21-global-certificate-closure/verify_packet.py --receipt /workspace/scratch/957bb0caa6f2/global-certificate-direct-science-receipt.json
python -X utf8 -B tools/validate.py --regressions --receipt /workspace/scratch/957bb0caa6f2/global-certificate-direct-repository-receipt.json
```

The earlier dirty preflight is not substituted for these publication runs
and is not the receipt attached here. The packet receipt records actual
arguments, execution modes, command statuses, durations, output hashes,
complete comparison results, and before/after Git and manifest states.
The repository receipt retains its complete command output.

## Attached evidence

| Receipt | SHA-256 |
|---|---|
| [Scientific replay](science_receipt.json) | `dac92a5c533dfa81f23732fa8aaa09dab93c371cdf63563ed6f6398cd0981f3f` |
| [Repository integrity and bounded regressions](repository_receipt.json) | `ba60f73e7f955855b61a5ee6f82d98bb0ce561c342cbeaf271fe29d4b97b68ac` |

The documentation-only descendants attach and refresh these two receipts
and update only this file and the report README. Their scientific files,
deterministic reports, runner, source snapshot, and manifest are unchanged
from the scientific commit. The attached receipts certify executions at that
scientific commit, not a fictional earlier execution at the later child.

These checks establish repository integrity, reproducible finite exact
calculations, and consistency with frozen reports. The all-parameter
mathematical statements rely on the written proofs and separate internal
reviews. No remote CI, Lean build, external referee acceptance, or full
Collatz proof is claimed.
