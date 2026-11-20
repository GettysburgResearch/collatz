# Publication validation

## Actual remote scientific commit

The repository gate was executed on the full, clean checkout of the published scientific commit:

- Commit: `99e0e9d7a1762ea965331f75f39e7c2e88944090`.
- Tree: `0e1b8a601d433d5f415bdbb7d00f43c6e716470c`.
- Started UTC: `2026-11-20T23:11:34.568586+00:00`.
- Finished UTC: `2026-11-20T23:11:39.578691+00:00`.
- Result: all 11 commands exited successfully; the tracked checkout was identical before and after validation.
- Exact receipt: [repository-validation.json](repository-validation.json).
- Receipt SHA-256: `ec32c6afadc480c7bc39207382d52618e06ac1246418d4addb3d331270afec55`.

The command was:

```sh
python3 -X utf8 -B tools/validate.py --regressions --receipt /absolute/path/outside/checkout.json
```

This receipt and this document are added in a documentation-only child of that remote scientific commit. The final published child is checked again in a full clean checkout; its exact head and the hash of its external receipt are recorded in the pull-request description. This avoids pretending that a commit can contain its own final commit-hash receipt.

## Scientific execution and review scope

The ten actual executions in [scientific-executions.json](scientific-executions.json) cover four production checkers and a separately implemented paired-path reconstruction, each in normal and optimized Python. All completed successfully with empty stderr, and each normal/optimized pair produced byte-identical output.

The [content manifest](content-manifest.json) freezes the scientific manuscripts, checkers, source snapshot, scoped reviews and finite outputs. The sole formatting normalization from reviewed author bytes is documented exactly in [import-normalization.json](import-normalization.json). Publication validation documents are excluded from that scientific manifest to avoid self-reference.

The manuscript proofs, the independent internal proof reviews, the finite arithmetic replays, and the repository gate are distinct evidence. The repository gate checks structure, frozen identities and selected bounded regressions. It does not prove a new universal mathematical statement. No remote CI execution, external referee acceptance or formal verification is claimed.
