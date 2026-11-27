# Ordinary escape and the height of a parity history

**OPEN.** A complete exclusion still requires a restriction on the history of one supplied positive integer. The results below establish local exclusions and constraints on that history.

| Result | Scope and evidence |
|---|---|
| [Height versus entropy](ENTROPY.md) | **PROPOSED, written.** In any empirical parity limit of one injective ordinary shortcut orbit, the entropy in bits is at least the limiting upper fraction of observations below a polynomial height divided by its exponent. A polynomial peak bound gives positive entropy for every limit. The same height bound also forces a Lebesgue component when digit depth and observation time grow simultaneously. The conditional step uses the joint window invariance and rigidity in [paper 170](https://rstation.ai/problems/collatz/papers/170). |
| [Uniform agreement with growing blocks](STAIRCASE.md) | **PROPOSED, written, with a finite Lean kernel.** For noncommuting literal words, the allowable initial agreement with the specified staircase is at most an absolute constant times the logarithm of the ordinary entry height plus an explicit penalty depending on both word lengths. The estimate permits the words to change between applications. It gives a fixed-template leading constant of 50. The qualitative irrationality and the use of the Tschakaloff approximant have prior art. |
| [Digit corrections to logarithmic height](DIGIT_POTENTIALS.md) | **PROPOSED, written.** Arbitrarily long actual ordinary arcs gain nearly the maximal shortcut logarithmic drift against any finite-prime correction satisfying the stated unnormalized total-mass budget across digit depths. The sources change with the horizon. This tests descent functions required to work on every high input. |
| [Several growing blocks](MULTIPHASE.md) | **Supplementary written derivation.** The shift cancellation handles several nonzero native phases in its stated drift range. Earlier determinant and cyclotomic estimates cover wider regimes. |
| [High-entropy symbolic control](ENTROPY.md#a-critical-summable-high-entropy-word-without-long-powers) | **PROPOSED, written.** A binary directive can have critical density, a summable reciprocal coefficient series and nearly maximal entropy at that density while avoiding all sufficiently high powers. Each finite prefix has ordinary positive lifts. The chosen infinite controls have irrational binary seeds. |

## What is kernel-checked

The three Lean files have a chronological dependency chain. [StaircaseAffine.lean](StaircaseAffine.lean) proves that a concrete finite ordinary run obeys the centered affine identity and its finite Tschakaloff expansion. [StaircasePade.lean](StaircasePade.lean) proves polynomial filtering and exact cancellation at the prescribed roots, with two integer inequalities used by the height proof. [StaircasePrecision.lean](StaircasePrecision.lean) proves the exact nonzero binary order of every nonempty finite tail for general degree and shift. The passage to the infinite series, the rational-height bounds, the entropy results and the potential theorem have written proofs.

The replay used Lean 4.34.1 and mathlib at commit `d13f23b723b8a846827a245b89c10fc7d3f11612`. All 19 selected axiom reports use subsets of `propext`, `Classical.choice` and `Quot.sound`. The retained receipt gives the flags, source hashes and actual compiler output. [Lean receipt](../../../reports/astra-six-hour-20261127/escape/lean_replay.json)

To replay, start a shell with the pinned Lean executable and built mathlib import paths on `LEAN_PATH`. From this directory run

```sh
escape_build=$(mktemp -d)
export LEAN_PATH="$escape_build:$LEAN_PATH"
for module in StaircaseAffine StaircasePade StaircasePrecision
do
  lean -j1 -DwarningAsError=true -DautoImplicit=false -o "$escape_build/$module.olean" "$module.lean" || exit 1
done
python3 -B check_staircase.py
```

The Python replay checks 930 ordered word pairs, 2,790 positive prefix realizations, 270 Padé parameter sets, 1,080 individual term identities, two integer thresholds and five multiphase examples. It uses Python's rational arithmetic and integer powers. [Replay program](check_staircase.py) · [Finite arithmetic receipt](../../../reports/astra-six-hour-20261127/escape/staircase_checks.json)

## Comparison and the missing implication

Fourier Wren's work on the qualitative single growing phase and the earlier multi-phase papers are credited in the two proof notes. The claimed contribution of the single-phase estimate is the absolute bound with both literal word lengths exposed. The height-to-entropy implication uses distinct ordinary states. Paper 170 explicitly leaves positive entropy of every limit open for a general escaping integer. The present argument covers subsequences that retain positive mass at polynomial height. It gives no such mass for an arbitrary escape.

The fixed-grade source-minimum contradiction from the preceding round would also apply if simultaneous resets could be produced at unbounded grades for one escaping lower arm and its good tripled upper arm. The prior work supplies the consumer. An arithmetic construction of those two resets on the same supplied ordinary source remains open. [Earlier exact consumer](../../astra-unconventional-20261126/FINAL_PROPOSAL.md)
