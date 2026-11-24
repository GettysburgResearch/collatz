# Replaying the Lean checkpoint

Use Lean 4.34.1 (compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`) and a built Mathlib checkout at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Supply its compiled dependency
search path, for example the `LEAN_PATH` printed by its `lake env` environment.
The replay program does not download or rebuild Mathlib.

From the repository root:

```sh
python -B research/astra-closure-20261124/replay_lean.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/mathlib \
  --lean-path-file /absolute/path/to/mathlib-leanpath.txt \
  --output /absolute/path/to/new-empty-build-directory
```

The program checks both version pins, copies the exact eleven sources into
the empty build directory, and compiles them in dependency order. The new
directory precedes Mathlib's path, binding all local imports to freshly built
objects. Every invocation uses `-j1 -DwarningAsError=true`. Its JSON receipt
records source hashes, exact commands, exit codes, stdout, stderr, and printed
axioms. It rejects unexpected axiom names. Build products remain outside the
repository. A correct receipt documents the observed compilation; it does not
promote the neighboring written analytic claims to formal proofs.

The eleven inputs comprise ten research modules and the exact pinned upstream
`ActualScalar.lean` dependency. The source is vendored for an independent replay
without needing to fetch another PR's Git history. Original per-agent compile
receipts and the root norm-certificate receipt are in
`reports/astra-closure-20261124/`. Source hashes bind those original executions
to the integrated files. The actual scalar's fresh dependency build produced
the same object bytes as the object used by the downstream agent builds.

For the three finite controls, run both interpreter modes:

```sh
python -B research/astra-closure-20261124/strict_controls.py
python -O -B research/astra-closure-20261124/strict_controls.py
python -B research/astra-closure-20261124/canonical_window_controls.py
python -O -B research/astra-closure-20261124/canonical_window_controls.py
python -B research/astra-closure-20261124/cycle_filter_controls.py
python -O -B research/astra-closure-20261124/cycle_filter_controls.py
```

Compare these outputs with `strict_controls.json`, `WINDOW_CONTROLS.json`, and
the `identical_control_output` field of `CYCLE_CHECKS.json`. Their checks use
explicit exceptions, so optimized Python retains the checks.

Finally, from a complete clean committed checkout, run the repository's
required structural validation:

```sh
python -X utf8 -B tools/validate.py --receipt /absolute/path/outside-checkout.json
```

This last command checks repository integrity, frozen review identities, and
selected bounded self-tests. It is separate from the Lean build and mathematical
review.
