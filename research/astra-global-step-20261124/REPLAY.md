# Replaying the global-step packet

The compiler and Mathlib pins match the preceding PR188 checkpoint:

- Lean 4.34.1, compiler commit
  `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`.

From the repository root, with that Mathlib checkout already built:

```sh
python -B research/astra-global-step-20261124/replay_lean.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/mathlib \
  --lean-path-file /absolute/path/to/mathlib-leanpath.txt \
  --output /absolute/path/to/new-empty-build-directory
```

The replay checks both version pins, copies only the six new Lean sources,
and compiles them in dependency order. The isolated directory comes first in
the dependency path. It passes `-j1 -DwarningAsError=true`, records each exact
source hash and compiler result, and rejects unexpected axioms or a missing
printed audit. It does not rebuild the earlier research modules or download
dependencies. The analytic cycle and entropy arguments remain written proofs.

The two finite research controls use explicit exceptions and support both
normal Python and `python -O`. Their commands and exact outputs are retained
in the finite-control receipt. Neither is an exhaustive test of ordinary
Collatz trajectories.

Finally, run the required repository integrity check from a complete clean
committed checkout:

```sh
python -X utf8 -B tools/validate.py --receipt /absolute/path/outside-checkout.json
```

The integrity validator is separate from the Lean proof checker and the
mathematical review. Its success does not establish Collatz.
