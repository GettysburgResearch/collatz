# Unbounded source-gap checkpoint receipts

The mathematical statements and their remaining coverage obligation are in
[`UNBOUNDED_GAP_REWRITES.md`](../../../research/lean-exact-witness-global-20261121/UNBOUNDED_GAP_REWRITES.md).
The frozen latest-source inspection is in
[`LATEST_SOURCE_SYNTHESIS.md`](../../../research/lean-exact-witness-global-20261121/LATEST_SOURCE_SYNTHESIS.md).

- `checkpoint-five.json` pins all 16 Lean source inputs and records the
  fresh-output build and complete audit commands.
- `build.txt` is the actual clean Lean 4.34.1 build output, 17 jobs.
- `axioms.txt` is the actual expanded audit output. The complete-cover
  propositions are printed explicitly as remaining hypotheses.
- `pump-replay.json` records 21 selected exact affine-family replays,
  including pump depth 1000, in normal and optimized Python. These replay
  instances check the independent generator; the arbitrary-index theorem is
  the Lean proof, and neither supplies global guard coverage.

From the owned `lean` directory, the proof commands are:

```sh
lake build
lake env lean -DwarningAsError=true Audit.lean
```

The exact generator accepts any nonnegative pump index and any parent first
gap at least five. For example, from the repository root:

```sh
python research/lean-exact-witness-global-20261121/gap-search/high/unbounded_pump.py --pump 1000 --first-gap 5
```

The repository integrity/regression gate is separately run in a complete
clean checkout before publication. Its actual checked local commit, exact
tree, and publication head are recorded in the PR update. The source-hash
manifest distinguishes that repository gate from the fresh Lean build; a
passing repository gate is not evidence for the unproved complete cover.
