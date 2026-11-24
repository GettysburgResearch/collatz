# Lean proofs and replay

The ten modules in this directory compiled with Lean 4.34.1 and Mathlib v4.34.1. The run produced 90 transitive axiom reports, including two private helpers in `CommutingImages`. Every listed dependency is one of `propext`, `Classical.choice`, and `Quot.sound`. The receipt records the SHA-256 of each source and the exact dependency list for each reported declaration. The full positive-integer Collatz conjecture remains open. [Ten-module receipt](../../../reports/astra-frontier-20261124/LEAN_RECEIPT.json)

## Reproduce the frozen run

The recorded compiler was the x86-64 Linux release at Lean commit `5045d0056413266e57c625dcd7c365b10e377c52`. The Mathlib commit was `d13f23b723b8a846827a245b89c10fc7d3f11612`. Each compiler invocation used `-j1 -DwarningAsError=true -DautoImplicit=false`. The runner creates a fresh temporary directory, places it first on `LEAN_PATH`, compiles every local source into it, and checks each requested `#print axioms` against the compiler output. It uses the pinned Mathlib build cache. The only local import edges are `CommutingImages` importing `MahlerRegularity` and `MinimumCrossing` importing `CyclePacking`. Both dependencies are built during the same run. [Replay script](replay_lean.py)

From the root of the Collatz checkout, with Git, Python 3 and Elan available, run the following in a shell. Elan selects the toolchain from Mathlib's `lean-toolchain` file.

```sh
set -eu
repo_dir="$(pwd -P)"
packet_dir="$repo_dir/research/astra-frontier-20261124/lean"
replay_dir="$(mktemp -d)"
git clone --depth 1 --branch v4.34.1 https://github.com/leanprover-community/mathlib4.git "$replay_dir/mathlib4"
cd "$replay_dir/mathlib4"
test "$(git rev-parse HEAD)" = d13f23b723b8a846827a245b89c10fc7d3f11612
lake exe cache get
lake env python3 "$packet_dir/replay_lean.py" --mathlib . --receipt "$replay_dir/lean-replay.json"
python3 - "$repo_dir/reports/astra-frontier-20261124/LEAN_RECEIPT.json" "$replay_dir/lean-replay.json" <<'PY'
import json
from pathlib import Path
import sys

expected, actual = (json.loads(Path(path).read_text()) for path in sys.argv[1:])
for key in ("lean_git_commit", "mathlib_git_commit", "warning_as_error", "auto_implicit", "modules"):
    if actual[key] != expected[key]:
        raise SystemExit(f"Replay differs in {key}")
print("All 10 module hashes and 90 axiom reports match.")
PY
```

## What the kernel checked

| Module | Reports | Mathematical scope |
| --- | ---: | --- |
| [MahlerRegularity](MahlerRegularity.lean) | 13 | Eight finite identities for rational word weights, prefix sums, substitution and affine evaluation. Five further results recover an equal-length word from its prefix-one sum and show that, at every physical weight iterate, the Mahler coefficient vanishes exactly when the image words satisfy $uv=vu$. The images may have different lengths. |
| [CommutingImages](CommutingImages.lean) | 4 | If the nonempty images $u,v$ commute, every one-sided substitution fixed sequence has period equal to the length of $u$. A fixed sequence with no positive period therefore has a nonzero coefficient at every physical iterate. |
| [DigitMahler](DigitMahler.lean) | 1 | For nonzero polynomials $A,B,P$ over a field, coprime $A,B$, an integer $a\ge2$, and $\deg P=a-1$, the identity $A(X)B(X^a)=P(X)B(X)A(X^a)$ forces $\deg A=0$ and $\deg B=1$. This is the degree step in the reducible-substitution argument. |
| [RepetitionWindow](RepetitionWindow.lean) | 11 | For the literal $8r=9q+7$ and $32r=9q+5$ integer branches, a shared length-$m$ word forces the start difference to be divisible by $8^m$. The file gives the prefix-height bounds and proves the four-window repeat/mismatch obstruction at a fixed source satisfying the stated size bound. |
| [PhasePacking](PhasePacking.lean) | 8 | Finite carry-clock identity, rational normalization of an ordinary edge, cubic height bound, prefix comparison to a canonical rational trajectory, a returning-coordinate bound under contraction, and uniqueness of sufficiently small endpoints for a shared past affine word. |
| [TwoSidedPacking](TwoSidedPacking.lean) | 13 | Integer bounds from edges at two extrema, spacing and denominator cancellation with a supplied lattice and carry bound. The remaining results check the two literal shadow equations on the residue class modulo 83, their gap arithmetic, and a Bézout identity in a commutative group. |
| [CyclePacking](CyclePacking.lean) | 21 | Connects actual shortcut iterations to their parity words and affine equations. A contracting equal-clock dictionary of $K$ words bounds the minimal block-return period by $K^2$. For a supplied legal first-crossing partition it proves bounds on word length, carry, boundary height and period under the stated hypotheses. |
| [MinimumCrossing](MinimumCrossing.lean) | 4 | For a legal first coefficient crossing whose endpoint is at least its source, proves the affine inequality and integer floor bound. For a positive source it proves the strict real-logarithm bound. A separate Farey-neighbor theorem gives integer numerator and denominator bounds under the determinant and interval hypotheses. |
| [GluingKernel](GluingKernel.lean) | 5 | Checks oddness, consecutive gap-one equations and ternary divisibility for the proposed states, the terminal equation under the lift hypothesis, and the exact gap and quotient of an ordinary edge with an odd endpoint. |
| [ExplicitConcentration](ExplicitConcentration.lean) | 10 | Proves $v_3(2^{3^k}+1)=k+1$ and constructs a lift for every $N,m\ge0$. The resulting $N+1$ positive odd states all equal $-1$ modulo $3^m$, strictly increase along $N$ gap-one steps, and end with a step to 1 of gap $3^{N+m}+1$. The initial state may depend on both parameters. |

## Frozen source provenance

PR 190 at `ba58227c5a047ff3859a148a5fdaac4fd1451e4c` supplied the first eight declarations of `MahlerRegularity`. Its exact original `MahlerCore.lean` compiled with exit 0. The compiler's exported axiom table covers all eight declarations. This packet preserves those statements and proofs under explicit module imports and adds the determinant and commuting-image results. [Frozen source](https://github.com/GettysburgResearch/collatz/blob/ba58227c5a047ff3859a148a5fdaac4fd1451e4c/research/mahler-physical-scripts-20261124/MahlerCore.lean)

PR 182 at `cbec52dde5bed390a693310dd04e911033ba0cc9` supplied `RepetitionWindow` and `PhasePacking`. The original round-11 source compiled unchanged. Round 12 failed in `normalized_edge` and `cubic_height` at the unavailable lemma `mul_le_mul_right₀`. The portable file retains the statements, uses `mul_le_mul_iff_left₀` for positive right-factor cancellation, removes two tactics after already-closed goals, and explicitly uses the existing lower bound on $y$. All eight repaired declarations passed the strict replay. [Round 11 source](https://github.com/GettysburgResearch/collatz/blob/cbec52dde5bed390a693310dd04e911033ba0cc9/research/fixed-source-repetition-round11-20261124/RepetitionWindow.lean) · [Round 12 source](https://github.com/GettysburgResearch/collatz/blob/cbec52dde5bed390a693310dd04e911033ba0cc9/research/phase-packing-round12-20261124/PhasePacking.lean)

PR 191 at `37b3916633cd32a0c173b20bb18ec3a7ec290a63` supplied `TwoSidedPacking`. The portable file preserves the thirteen original statements and proof bodies and changes the module header, imports and documentation. It passed the strict replay. The two legacy-import runs on the original bytes were deliberately interrupted with exit 130 after the port passed. Source hashes, original commands and outcomes are recorded independently of the ten-module receipt. [Frozen source](https://github.com/GettysburgResearch/collatz/blob/37b3916633cd32a0c173b20bb18ec3a7ec290a63/research/two-sided-cycle-packing-20261124/TwoSidedPacking.lean) · [Frozen-source audit](../../../reports/astra-frontier-20261124/FROZEN_SOURCE_AUDIT.json)

## Written arguments and numerical evidence

The proposed rationality/transcendence dichotomy also needs the infinite-series arguments, moving-point estimates, and the passage to an actual 2-adic completion. The Lean modules establish the finite identities, determinant regularity and the polynomial-degree lemma. The written ordinary gluing theorem for an arbitrary gap word and target also uses a primitive-root argument beyond the explicit all-one family formalized here. [Substitution proof](../REDUCIBLE_SUBSTITUTIONS.md) · [Ordinary gluing proof](../BRIDGE_AUDIT.md)

The rotation that gives a one-lap first-crossing partition of an arbitrary positive cycle is a written proof. The exact 90-term rational logarithm calculation and the C++ descent census for starts 2 through 206,178,386 are executable controls. Applying those controls gives numerical bounds beyond the general inequalities checked by Lean. The additional application at a cycle minimum of at least $2^{71}$ uses Barina's published verification. The cutoff from that publication was not replayed. [Cycle argument](../CYCLE_CLOSURE.md) · [Minimum-arc certificate](../MINIMUM_ARC.md) · [Finite execution receipt](../../../reports/astra-frontier-20261124/FINITE_CONTROLS.json)
