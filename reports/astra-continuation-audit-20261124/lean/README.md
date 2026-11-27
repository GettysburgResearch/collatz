# Finite Lean reconstruction at PR 201

**Source head** `73a145ca99448a78219bd149e273f33b6e3fda4b` (PR 201). **Toolchain** Lean 4.34.1, release commit `5045d0056413266e57c625dcd7c365b10e377c52`, mathlib v4.34.1 at `d13f23b723b8a846827a245b89c10fc7d3f11612`.

Across the working modules and two generated certificate modules, this audit checks **46 distinct theorems**. Of those, 22 are the frozen candidate theorems and 24 are new. The final inventory includes 24 additional definitions, structures and inductives, for **70 distinct printed declarations**. The separate import-only pass repeats the same 22 frozen theorems.

## Frozen source replay

All 22 theorem statements and original proof bodies in the four candidate files pass after replacing their first line, `import Mathlib`, with the narrower imports listed in the receipt. The first replay mode obtains the original bytes from the pinned Git blobs and performs only that substitution. It includes the authors' original axiom queries. The unmodified umbrella-import programs were not executed.

| Frozen candidate | Theorems | Scope of checked statements | Further changes in the working copy |
| --- | ---: | --- | --- |
| `KilledMoment.lean` | 4 | Rational majorant, abstract survival block, forced moment recursion on a finite block, and real inequality for charging. | Status comment, sequential field simplification/ring tactic, scoped unused-binder linter option for the retained hypotheses of `green_charge`. |
| `continuation/OctavePhase.lean` | 7 | Native budgets, carry uniqueness, rational and natural constants, finite variation and peak charge. | Status comment, sequential congruence/ring tactic, local exponentiation threshold 400. |
| `prefix-density/PrefixDensity.lean` | 7 | Generic orbit iteration, incompatible anchors, finite clock and logarithm certificates, affine lift and divisibility. | Status comment. |
| `two-end-bridge/TwoEndBridge.lean` | 4 | Three affine equations composed, residue lifting, additive retention and rational normalization. | Narrowed imports alone. |

Every binder and theorem statement in the four working copies is preserved. The second replay mode checks these copies along with the new modules under [verified](../../../research/killed-green-head-closure-20261124/verified/). The compiler's `#print axioms` result is recorded individually. The allowed union is `propext`, `Classical.choice`, and `Quot.sound`. The checker rejects an unrecognized dependency or an incomplete inventory.

## Actual inverse paths at a prescribed terminal

[OrdinaryGapWord.lean](../../../research/killed-green-head-closure-20261124/verified/OrdinaryGapWord.lean) defines a chronological word by appending gaps of length `e+1`. Its path relation records positive odd vertices and the exact equality `3y+1=2^(e+1)q` at each step. Consequently each exponent is the full odd-to-odd valuation. The source can initially be any signed integer.

Write `d` for the number of letters, `s` for the total gap length and `C` for the integer carry. For any positive odd terminal `q`, integer `r`, and integer precision `K≥0`, the checked theorem `source_class_iff` gives

    3^(d+K) divides 2^s q − C − 3^d r
      iff there is a literal path from some x ≡ r (mod 3^K) to q.

The implication from divisibility to a path peels the last gap, cancels a power of two modulo three and derives positivity and oddness of the previous integer. It then invokes the induction hypothesis at that integer. The independent theorem `Path.shortcut_iterate` proves that this very source reaches `q` after exactly `s` applications of the ordinary shortcut map. The formula for the map on signed integers agrees with the usual shortcut on all its positive inputs.

At positive precision with a unit class, `unit_source_class_iff` proves that the source is a unique ordinary unit. The gap equation excludes multiples of three at later vertices. The converse uniqueness needed for counting is also formalized. Two legal words at the same odd depth starting from the same source must be identical, and their terminals must agree (`Path.unique_at_depth`). These facts justify the finite path and injectivity steps when concatenated words in the written bridge are counted. A quantitative supply of middle words still requires a separate bound.

## Exact-clock carry cutoff and router

[ExactClockRouter.lean](../../../research/killed-green-head-closure-20261124/verified/ExactClockRouter.lean) proves the normalized carry recursion and `0≤β≤(3/2)^d−1` for every finite word. Hence a slice with `εq≤β` and `ε>0` has the checked terminal cutoff `q≤((3/2)^d−1)/ε`.

For two positive gaps `f,e` with total `t`, a supplied positive odd terminal `z`, prescribed unit class `r mod 3^K` with `K≥1`, and the explicit congruence

    2^f ≡ 2^t z − 3 − 9r    (mod 3^(K+2)),

the checked `two_gap_router` returns the positive odd unit `x=(2^t z−2^f−3)/9`, its residue, its literal two-gap path and its actual endpoint at shortcut clock `t`. In the Lean signature the naturals `a,b,K` encode the positive gaps and precision by adding one. The existence of a suitable first gap for every sufficiently large total is separately proved in the [escape analysis](../../../research/killed-green-head-closure-20261124/escape-analysis/README.md).

## Directed tripling certificates over entire progressions

[TriplingCover.lean](../../../research/killed-green-head-closure-20261124/verified/TriplingCover.lean) proves soundness of the affine row transitions, concatenation of a word, coverage by subdivision, and the full recursive checker. For a reflexive transitive relation `R`, its hypotheses are exactly the five explicit families of directed edges in `Rules r R`. The root conclusion for each allowed residue is

    for every n ≥ 0, R (2n+1) (3(2n+1)).

The ordinary moves are the shortcut even/odd branches in either direction. The fifth move supplies forward tripling at `6s+r`. For the actual reachability interpretation, take the reflexive transitive closure of these five families. For convergence implications, take implication between the corresponding invariant labels. Forward tripling remains an allowed extra move in the theorem.

[cover_source.py](cover_source.py) translates the exact two preorder tables into explicit Lean trees and lists of move letters. It supplies no precomputed arithmetic result or unchecked leaf theorem. Each generated file uses `decide +kernel` on the complete tree at `(2,1)`, then applies the soundness theorem. Both closed checks depend on **no axioms**. Both universal directed tripling statements depend only on `propext` and `Quot.sound`.

| Table | Full progression leaves | Distinct dictionary words | Letters checked over all leaves |
| --- | ---: | ---: | ---: |
| [Residue 1](../../../research/killed-green-head-closure-20261124/global-bridge/cover1.txt) | 948 | 261 | 35,627 |
| [Residue 5](../../../research/killed-green-head-closure-20261124/global-bridge/cover5.txt) | 1,263 | 312 | 49,015 |

The finite certificate data, generated inputs, named theorem dependencies and process exits are bound in the receipt. The numerical table dimensions and distortion ranges in the companion [global-bridge packet](../../../research/killed-green-head-closure-20261124/global-bridge/README.md) also have an independent Python replay. The Lean checker certifies coverage, legality and the exact endpoint. Query-count inequalities, distortion constants and the reductions to external results are written deductions.

## Replay

With the frozen Collatz commit available as a local Git object and mathlib's dependencies and compiled libraries installed at the pins above, run from the repository root:

```sh
python -B reports/astra-continuation-audit-20261124/lean/replay.py \
  --mathlib /path/to/mathlib4 --lean /path/to/lean-4.34.1/bin/lean > /tmp/replay.json
```

The runner uses one Lean worker, reconstructs the import-only inputs, checks the working copies, generates each closed certificate module in a temporary directory and kernel-checks both complete trees. The [recorded receipt](RECEIPT.json) contains original blob IDs, source SHA-256 hashes, hashes of the actual inputs including extra read-only axiom queries, and per-declaration transitive axiom lists. The imported mathlib cache was already built.

## Mathematical boundary

The formal results concern finite words, exact paths, explicit inequalities and the stated conditional consumers. They do not prove the killed Green estimate for the physical chain, an atom floor or renewal theorem, a uniform upper tail on the exceptional exact-clock row, or universal convergence. The analytic inputs and orbit quantifiers retain the status given in their respective written proofs.
