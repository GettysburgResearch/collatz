# Formalization scope and reproducible execution

Executed checks and the status of the final replay are recorded in [the report](../../reports/astra-phase-and-cycle-20261124/README.md). Compilation of a finite kernel does not certify the surrounding real analysis or the entire Collatz conjecture.

## Pinned environment

- Lean `leanprover/lean4:v4.34.1`, release commit `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- The byte-exact upstream actual-scalar file from PR182 commit `f94a2ae1caba9a1857feda892ee1779695eea9d2`, Git blob `85385ac9b4dbc2bab8b3f78f02d4f865ed16d2b8`.
- The replay script authenticates both the Git blob and SHA-256 before compilation. It requires fresh objects for every contributed source and the vendored source. The report distinguishes completed checks from a pending full replay.

## Theorems included in the new audit

| Module | Public theorem(s) | Exact mathematical scope |
|---|---|---|
| `OneRun.lean` | `one_run`, `one_run_length` | Finite actual-edge arithmetic with explicit positivity, oddness, carry equation and carry-floor inputs; includes zero-carry divisibility. |
| `ThreeRunCore.lean` | `three_run_length` | Independent `Std` proof of the upper-digit run inequality in natural-number arithmetic, from the explicit physical/carry equations and endpoint floor. |
| `OrdinaryShadow.lean` | `smaller_nonconverger` | Infinite natural L/P path with the stated modulo-83 condition produces a smaller positive ordinary source whose literal shortcut orbit never reaches one. |
| `PhaseBounds.lean` | `three_run_bound` | Finite upper-digit run bound from complete physical and carry clocks, with only the final carry floor required. |
| `PhaseBounds.lean` | `carry_lt`, `actual_floor`, `actual_clock`, `actual_three_run` | The carry is constructed from the ceiling of the **actual** real scalar. Its floor and clock are derived from the pinned actual-scalar theorem; the upper-run bound applies to its actual orbit. |
| `ActualOneRun.lean` | `actual_one_run` | Connects the finite lower-run theorem to the actual scalar and actual odd map at any supplied shift of one positive odd source. |

`AllAxioms.lean` lists all ten new public theorems. It separately audits five selected upstream results: real summability, the scalar upper bound, recurrence, strict lower bound, and `converges_iff_triadic`. These inherited results are not counted as new theorems. Inclusion in the audit source is not itself a successful execution; consult the report for the completed receipt.

The allowed transitive axiom set is exactly a subset of `propext`, `Classical.choice`, and `Quot.sound`. The replay rejects missing reports, extra public theorem declarations absent from the audit, `sorryAx`, and any other reported axiom. It also treats compiler warnings as errors.

## Written deductions outside the kernel scope

PS2's real-power inequalities, the approximation exponents, PS3's asymptotic optimality, PS4–PS6's unbounded canonical-word/fiber constructions, and the cycle polynomial/Galois arguments remain written mathematics. Their finite exact controls and independent written reviews are separate evidence. The complete real scalar construction is inherited and vendored unchanged; its original source passed a worker compile, while the report tracks its place in the final fresh-source replay. The new contribution does not insert scalar recurrence or Collatz convergence as an axiom.

The residual denominator size corollary also retains the precise PR185 logarithmic-forms and continued-fraction input. We have reconstructed the new cyclotomic count and coefficient-support argument, not re-formalized Matveev's theorem or independently replayed every upstream analytic proof.

## Replay command

With the pinned Mathlib checkout and its dependencies already built:

```sh
python -B research/astra-phase-and-cycle-20261124/replay_lean.py \
  --lean /absolute/path/to/lean-4.34.1-linux/bin/lean \
  --mathlib /absolute/path/to/mathlib \
  --output /absolute/path/outside/the/repository/fresh-replay
```

The output directory must be new or empty. The script records the source Git head and dirty status, every source hash, toolchain identity, commands, standard output and error, fresh object hashes, and the full axiom inventory. If a known dependency `LEAN_PATH` is supplied, `--lean-path` avoids a second Lake invocation. Compilation is sequential to control memory use.

The final report distinguishes exact original upstream replays from any explicitly recorded header/visibility port used to accommodate Lean's module loading. Any such port must retain the original source, generated source, exact diff and hashes; theorem statements and proof bodies must stay unchanged.
