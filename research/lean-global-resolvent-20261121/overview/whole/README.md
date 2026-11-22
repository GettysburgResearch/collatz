# Checkpoint 9: independent block cycles, total dispatch, and ordinary contact mass

**Full Collatz remains OPEN.** This checkpoint combines the latest arithmetic,
source-certificate, and harmonic-flow work after a repository-wide refresh.
It adds 37 audited Lean theorems and written developments across three routes.
The exact evidence boundary is below; no global coverage condition is supplied
as a proof.

**Current-source integration:** [the late PR183 continuation](LATEST_HEAD_INTEGRATION.md)
was read before publication. Its concurrent free-exponent and carry results
are credited. Combining the packets gives a sharper complete-word cutoff,
a proved joint source-grade/target induction, and a uniform `L²(eta)`
extension of the ordinary asynchronous residue formulas.

## Results

| Development | New result | Evidence | First remaining global step |
| --- | --- | --- | --- |
| [Independent block classification](INDEPENDENT_BLOCK_CLASSIFICATION.md) | For every fixed block architecture, classify all positive cycles with arbitrary independent repetition counts; explicit finite clock cutoff outside replayable template cycles | 12 Lean arithmetic theorems; written rotation, Matveev specialization, cutoff, and finite automaton | An upper description-complexity bound for arbitrary cycles |
| [Total affine dispatcher](AFFINE_DISPATCHER.md) | Every signed target state can consume any supplied source word, with refreshed binary horizons, an exact literal suffix, and the same rank-paid handoffs | 13 Lean theorems; exact replay of a one-pass failure and a credited asynchronous repair | Every residual low state must admit a successful paid handoff |
| [Joint source and target induction](SOURCE_TARGET_INDUCTION.md) | Ordinary descent and independent-clock smaller partners may keep the exact source certificate; paid source rewrites decrease the outer grade | 12 Lean theorems, including a universal paid capture of the credited debt-growth residue | A complete successful cover of the combined branches, measured against the original queried target |
| [Ordinary last-contact measure](ORDINARY_LAST_CONTACT_MEASURE.md) | On hypothetical escaping components, ordinary first-contact laws converge to a finite atomic measure on their last-contact sources | Written synthesis of source-qualified analytic inputs and checkpoint 8 | Quantitative control of the original-source contact tail, rather than qualitative compactness |

The [global synthesis](GLOBAL_SYNTHESIS.md) explains how these results fit
together and which next questions would affect the full theorem. The
[source and review ledger](SOURCES_AND_REVIEW.md) distinguishes the complete
145-PR metadata inventory from the selected mathematical arguments actually
read and used. It also corrects two stale cross-references in the new
literature guide and credits earlier dictionary-complexity results.

## The formal statements

[BlockRepetitionBudget.lean](lean/BlockRepetitionBudget.lean) proves the exact
dyadic reserve for every repeated binary word and the unrestricted finite
concatenation bound

\[
2^A\le[K(x+1)]^{2^r-1}.
\]

The nonfixed-block hypothesis is explicit. A fixed block is an actual cycle
output in the written classifier, not a discarded case.

[AffineDispatcher.lean](lean/Collatz/AffineDispatcher.lean) repeatedly composes
checkpoint 6's signed lifting theorem across actual source edges. If
\(3r+1=2^a u\), \(n=3^{p+1}r+d\), and the signed path from
\(d-3^p\) has \(k\) odd inputs and endpoint \(z\) after \(a\) steps,
then

\[
T^a(n)=3^{p+k}u+z.
\]

Every low target has a negative-offset initialization. Total finite dispatch
ends at degree zero or at the literal source endpoint one with an explicit
remaining debt. The first case gives a proved capture; the second remains
a physical target that needs a paid merger or another valid rewrite.

[SourceTargetInduction.lean](lean/Collatz/SourceTargetInduction.lean) adds
inner strong induction on the current target while retaining the exact
complete source certificate. It proves compatibility with lower source
grades, direct ordinary descent, and independently timed smaller partners.
Its closing theorem assumes the displayed universal `MixedCover`; that
cover is the remaining assertion, not an axiom or an established theorem.

## Reproduce the new checkpoint

The portable driver compiles the new sources and their 16 exact project
imports in a fresh output directory. It checks the runtime commits, frozen
source hashes, audit counts, and allowed axiom union. Its optional dependency
mirror is authenticated against the pinned original artifacts.

```sh
python -X utf8 -B check_whole.py \
  --lean /path/to/lean-4.34.1/bin/lean \
  --mathlib /path/to/mathlib4 \
  --out /tmp/collatz-checkpoint9-new \
  --receipt /tmp/checkpoint9-lean.json

python -X utf8 -B check_examples.py \
  --receipt /tmp/checkpoint9-examples.json
```

Lean is pinned to `5045d0056413266e57c625dcd7c365b10e377c52` and Mathlib to
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The committed
[execution report](../../../../reports/2026-11-22-whole-repository/README.md)
records the actual fresh replay: all 21 compilation/audit commands passed,
all 37 new public theorem audits passed, and the source hashes were unchanged.
The axiom union is `propext`, `Classical.choice`, and `Quot.sound`.

The analytic note and the transcendence-dependent classifier are written
proofs, not additional Lean declarations. Repository integrity is checked
separately on the complete clean published tree.
