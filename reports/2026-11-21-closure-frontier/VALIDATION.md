# Publication-time execution record

## Scientific commit: actual complete execution

- Commit: `c511ff66d9321bf21fd6d0612ddfdc6c4a2da3ae`.
- Tree: `8cb953abc785f8979a1197a22d2d6406d2829350`.
- Complete tracked-file count: **346**.
- Frozen manifest: **29 entries**, SHA-256 `534da89ac9625806f72a0fb6965d128d6fc427947c966e21213dca50981a97e6`.
- Scientific execution interval (UTC): `2026-11-20T23:10:57.855299+00:00` to `2026-11-20T23:11:05.730285+00:00`.
- Repository execution interval (UTC): `2026-11-20T23:10:57.854464+00:00` to `2026-11-20T23:11:02.726455+00:00`.

The checkout was materialized from the exact GitHub commit object. Its
Git object identity was reconstructed and verified before a separate clean,
complete detached worktree was created. The two commands below actually ran
in that worktree. All tracked files were present; the index and commit tree
agreed; the commit, tree, and clean worktree state were unchanged afterward.

```sh
python -X utf8 -B reports/2026-11-21-closure-frontier/run_bundle.py --receipt /workspace/scratch/56e7a5765d0c/frontier-publication/scientific-bundle-validation.json --expect-head c511ff66d9321bf21fd6d0612ddfdc6c4a2da3ae
python -X utf8 -B tools/validate.py --regressions --receipt /workspace/scratch/56e7a5765d0c/frontier-publication/scientific-checkout-validation.json
```

[Scientific execution receipt](scientific-bundle-validation.json): **PASS**,
16 actual program executions: eight programs, each normally and with `-O`.
Every output was byte-identical to its frozen report. SHA-256:
`7cdaeade2bdc6bd6d9625df73816e62eb77d80f735dcea89c435fae180aa729d`.

[Repository execution receipt](scientific-checkout-validation.json): **PASS**,
11 actual integrity and bounded-regression commands. SHA-256:
`39148b10dac146f34916592471c94a9f131bae5b00285552b2837d9c701791d7`.

The JSON receipts are copies of the actual output files. Their paths,
timestamps, executable versions, command arguments, and checkout identities
are historical execution facts, not placeholders for a reader's machine.

## Documentation child and final publication

A direct child adds only this document and the two receipts, and updates
the report index. All 29 frozen manifest entries and the manifest itself
remain unchanged. The scientific executions above belong to the named
scientific commit, not to a later commit inferred from it.

The final publishing PR records a fresh complete repository validation
and a manifest-only check on the documentation child's exact head. Those
final receipts belong in the PR body to avoid a self-referential commit
receipt. The branch and PR head are read back after publication.

## What these checks establish

The bundle establishes that these exact programs reproduce these exact
finite reports with optimization both disabled and enabled. The independent
reconstruction notes assess their named mathematical claims and dependencies.
The repository gate establishes its stated structural and finite regression
properties. None of these events is external mathematical acceptance,
proof-assistant formalization, universal template coverage, residual-energy
summability, or a proof of the Collatz conjecture.
