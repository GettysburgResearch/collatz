# Finite Lean kernel audit

Lean 4.34.1 at `5045d0056413266e57c625dcd7c365b10e377c52` accepted the repaired module with mathlib v4.34.1 at `d13f23b723b8a846827a245b89c10fc7d3f11612`. The standalone command `lean -j 1 -DwarningAsError=true -DautoImplicit=false FixedBundle.lean` exited 0. All 80 authored declarations, including private helpers, were examined by `#print axioms`. The 119 print results include 39 repeated inspections from the source files. The only reported axioms were `propext`, `Classical.choice`, and `Quot.sound`.

| Frozen source | Theorems and lemmas | Definitions | Individual original-header run | Result inside repaired module |
|---|---:|---:|---|---|
| PR182 `PhasePacking.lean` | 8 | 0 | Timeout after 150 seconds, exit 124 | Passed with five proof edits |
| PR182 `RepetitionWindow.lean` | 11 | 5 | No completed individual result | Passed with original declaration bodies |
| PR187 `RepeatObstruction.lean` | 8 | 1 | Timeout after 180 seconds | Passed with original declaration bodies |
| PR188 `CarryCocycle.lean` | 6 | 1 | No completed individual result | Passed with three proof edits |
| PR188 `ResidueDefect.lean` | 6 | 1 | No completed individual result | Passed with original declaration bodies |
| PR189 `CarryBudget.lean` | 6 | 1 | Interrupted, exit 130, empty output | Passed with original declaration bodies |
| PR190 `MahlerCore.lean` | 8 | 5 | No completed individual result | Passed with original declaration bodies |
| PR191 `TwoSidedPacking.lean` | 13 | 0 | No completed individual result | Passed with original declaration bodies |
| **Total** | **66** | **14** | | **80 declarations passed** |

The module replaces the individual imports with nine selected mathlib imports, retains the source namespaces and appends an axiom inspection for every authored declaration. All theorem statements and binder names are preserved. The supplementary original-header batch was interrupted during import, with exit 130 and an empty log. The timeouts and interruptions provide no source-level compiler diagnosis. The finite results carry the hypotheses written in their declarations.

The five edits to `PhasePacking.lean` replace an unavailable multiplication-cancellation name twice, remove two redundant calls to `ring` after `field_simp`, and use the retained hypothesis `hy` explicitly when proving nonnegativity of a square. The three edits to `CarryCocycle.lean` replace single-goal tactic sequences flagged by the strict linter. The unified diff records the exact proof changes.

The standalone standard-library `RunSupport.lean` and `CarryBudgetStd.lean` files each passed with `-j 1 -DwarningAsError=true`, using the compiler default for `autoImplicit`. The former printed both new theorems. The latter printed all six carry theorems. The standalone `BoundedBirth.lean` also set `-DautoImplicit=false` and printed all five theorems and both definitions. Its weights are evaluated at the rational point one third, with denominators cleared.

The repaired module has SHA-256 `f5a292583bacc29aafb0bd1d8032849a5a3c5085f02b5d1162fb8257be4346e5`. Its complete log has SHA-256 `2df0af4b6c3b67eac1fe8bead61d28c63ca2f18d48e417e0e9247200df05bc50`. The replay generator reconstructs the exact module from the pinned Git objects, with a separate mode for the original-header files and their appended axiom inspections.
