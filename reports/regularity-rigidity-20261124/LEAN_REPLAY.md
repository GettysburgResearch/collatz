# Lean replay of regularity rigidity and fixed-clock fibers

The three original files contain 19 theorem statements. The repaired source preserves the text of every theorem signature, including its named hypotheses. Four further modules cover finite ordinary inverse fibers, relative states, cell counts and a fixed-clock paired route. The claims below concern the shortcut map on ordinary integers, with chronological source parity words. [Source PR 200 at its frozen head](https://github.com/GettysburgResearch/collatz/tree/abf36c63b4d0181541d7e029d390d6f636940750/research/regularity-rigidity-20261124)

## Frozen source and repairs

The original Git objects below come from PR 200 at `abf36c63b4d0181541d7e029d390d6f636940750`. To isolate proof errors on Lean 4.34.1, the first control changed only the broad import to explicit module-mode imports and opened a public section. All three controls exited 1 with warnings treated as errors. The SHA-256 values identify the original Git bytes. The final receipt identifies the compiled bytes. The legacy broad-import files themselves were not executed in this replay. [Axiom and source receipt](LEAN_RECEIPT.json)

| Source | Original Git blob | Original SHA-256 | Repair after the import-only control |
| --- | --- | --- | --- |
| [LeanCore.lean](../../research/regularity-rigidity-20261124/LeanCore.lean) | `2de01bd821dd5cb31faaff1a414f06af71f22d1a` | `6389af01a7c44ced22a00aadbbe23121e17d0b59325545cadbe98bbb4082c2b1` | Used the current names `ite_true` and `ite_false`. Explicitly retained the redundant probability upper-bound sign hypothesis `hs` in the proof to preserve the public named argument. The original exponent rewrite and telescoping calculation passed. |
| [ReturnRigidity.lean](../../research/regularity-rigidity-20261124/continuation/ReturnRigidity.lean) | `98581e87bb8a2e43390b913867eaff93a866f07a` | `a1c172ef035e78f08c56bdbfa17248da06ffbad80b233fa017e5760f7813311e` | Passed the proof `hq0 : 0 ≤ q` to `mul_nonneg`. The original code supplied the real number `q`. The probability-domain assumptions `hp0` and `hp1` were explicitly retained with their original names after the repaired proof exposed the unused-variable diagnostics. |
| [PointwiseFiber.lean](../../research/regularity-rigidity-20261124/pointwise-fibers/PointwiseFiber.lean) | `36867d2f2b390cda447d9f0d92d029af2800800f` | `d020c273cd946f452a7da141381421878237f8b35a7bcfe7c72f0291ee958f17` | Removed `ring` after `field_simp` had already closed the pressure identity. All five theorem bodies otherwise retain their original arguments. |

## Mathematical coverage

| Module | Theorems audited | Scope |
| --- | ---: | --- |
| LeanCore | 7 | One-step cylinder lift on signed ordinary inputs, exponent splitting, weighted phase increment, probability-height inequality, block mismatch and deterministic prefix transfer. |
| ReturnRigidity | 7 | Rational affine action and composition, deterministic state continuation, symmetric quadratic drift, common submass, constant-prediction error floor and covariance identity. |
| PointwiseFiber | 5 | Exact-target arithmetic for two carries, half-scale height from a supplied real offset, normalized rational pressure, low incidence on a finite family and inherited labels on a supplied ordinary pair. |
| [OrdinaryFiber](../../research/regularity-rigidity-20261124/pointwise-fibers/OrdinaryFiber.lean) | 16 | Recovers every actual parity and the exact supplied endpoint from the integer affine equation in both directions. One additional ternary digit tests whether the inverse is a unit. Under equal clocks and odd counts, the fivefold carry relation is equivalent to the two ordinary endpoint-and-word laws, assuming the first cleared equation. A compatible finite family gives equally many distinct positive odd unit starts in the half-scale interval. Fixed-length, fixed-weight carry injectivity gives the uniform exact ceiling `⌊K/3^p⌋+1` for carry at most `K`, including for all ordinary words in a specified target fiber. |
| [RelativeState](../../research/regularity-rigidity-20261124/pointwise-fibers/RelativeState.lean) | 3 | From two literal finite orbits, the common clock, the odd-count balance and the definition of `D`, derives `2^e D = 3^minus C_v − 5·3^plus C_u`. With positive companion carry and source offset at most `b/c`, it proves `cD > −5·3^plus b`. Thus `D=−4` is impossible at equal odd counts and offset at most one half when the companion starts odd. |
| [FinitePressure](../../research/regularity-rigidity-20261124/pointwise-fibers/FinitePressure.lean) | 2 | At one clock type with `G=2^e/3^p`, selected event mass at least `u`, at most `2·3^p` cells, mass per cell at most `N/2^e` and multiplicity at most `1+B G`, proves `u·2^e ≤ 2·(1+B G)·# {cells with N≥uG/4}`. The event mass, its local domination and the cap are explicit inputs. |
| [TwoBlockRouter](../../research/regularity-rigidity-20261124/pointwise-fibers/TwoBlockRouter.lean) | 6 | Ordinary kernel reduction checks all 243 target residues for the split at total clock 119. For every supplied positive odd ordinary ternary unit, constructs a split into two padded A blocks, each of length at least six, a positive odd intermediate and a positive odd unit source. Both chronological word pairs are physically realized and their endpoints at the two marks are fivefold. Each source block has two odd inputs and each companion block has two. |

All local theorem declarations, including private proof helpers, have a compiler-reported transitive axiom table. The allowed dependencies are `propext`, `Classical.choice` and `Quot.sound`. In particular the finite routing certificate uses `decide +kernel`. Every theorem statement in the four added modules is checked with the same settings as the original 19.

The finite ordinary attachment applies to whatever family satisfies the listed clock, carry, offset and divisibility tests. Its size can depend on the prescribed target. The 119-clock construction supplies one source at each target. A lower bound of order `G^(1-o(1))` for every fixed positive ordinary target remains open. The renewal and analytic estimates used to produce event mass at favorable clock types are written arguments with their stated dependencies. The four-A clock-88 certificate is a separate exact computation. The Collatz conjecture remains open.

## Reproduce

The run used Lean 4.34.1 at `5045d0056413266e57c625dcd7c365b10e377c52` and Mathlib at `d13f23b723b8a846827a245b89c10fc7d3f11612`. The runner checks those revisions and reads the built Mathlib and dependency oleans. It sets a fresh temporary module directory first on its search path, compiles each local dependency in order and checks each requested axiom report against the compiler output. The seven files use `-j1 -DwarningAsError=true -DautoImplicit=false --json`. The source SHA-256 and axiom dependencies of each local theorem are recorded in the receipt. [Replay script](../../research/regularity-rigidity-20261124/replay_lean.py)

Run the following from the root of the Collatz checkout with Git, Python 3 and Elan installed.

```sh
set -eu
packet="$(pwd -P)/research/regularity-rigidity-20261124"
work="$(mktemp -d)"
git clone --depth 1 --branch v4.34.1 https://github.com/leanprover-community/mathlib4.git "$work/mathlib4"
cd "$work/mathlib4"
lake exe cache get
lake env python3 "$packet/replay_lean.py" --mathlib . --check "$packet/../../reports/regularity-rigidity-20261124/LEAN_RECEIPT.json" --receipt "$work/replay.json"
```
