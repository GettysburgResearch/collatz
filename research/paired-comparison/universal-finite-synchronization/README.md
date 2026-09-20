# Universal finite synchronization

**PROPOSED pending independent review. No complete Collatz proof.**
Continuation of #127; parallel #128's complete comparison grammar is credited,
not reintroduced as new. Start with [the full proof](PROOF.md).

## What changes

The old compiler required `3^a-b>2^a`. A finite positive preconditioning
now gives a synchronous merger progression for **every** pair
`(3^a*d+b,d)`, `a>=0`, `b` any integer.

More substantially, every finite family of forms `3^a_i*x+b_i` has a
**single compatible** synchronous-merger progression inside **any prescribed
arithmetic class**. This synchronizes whole H ladders rather than choosing
incompatible pairwise gates.

For arbitrary positive integer slopes `A_i`, there is a complete feasibility
classification. Uniform mergers with independent clocks exist precisely
when all `A_i/(2^v2(A_i)*3^v3(A_i))` are equal. The clock differences must
be `v2(A_i)-v2(A_j)`. Arbitrary integer intercepts cause no additional
obstruction. This classifies uniform affine families, NOT individual
Collatz convergence.

The original-source lift synchronizes the source with all selected smaller
original ladder companions. Infinite families keep the entire displayed
source arm above its source and have no smaller pure ancestor at any depth.

A separate fixed-source theorem says every hypothetical least counterexample
has a **finite visit budget** for core-certified comparison catalogues, even
with companion switching, provided each original companion's clock persists
and strictly advances on reuse. This eliminates endless H recycling under
those hypotheses; it does not eliminate permanent escapes.

## Read in order

Proof Sections 1--3 give the universal construction and exact classification.
Section 4 gives the four-way identity and all-rung original-source lift.
Section 5 states and proves the fixed-source budget, including the clock
condition and its failure modes. Sections 6--7 give the finite evidence and
the unsupported universal-entry step.

## Replay from the repository root

```sh
python -B experiments/paired-comparison/universal-finite-synchronization/run.py \
  --full /tmp/ufs-full.jsonl \
  --check experiments/paired-comparison/universal-finite-synchronization/canonical.json
python -B -S experiments/paired-comparison/universal-finite-synchronization/verify.py \
  /tmp/ufs-full.jsonl \
  --summary experiments/paired-comparison/universal-finite-synchronization/canonical.json \
  --self-test
```

Both are Python standard-library programs. The generator also accepts
`--output PATH` and a smaller `--limit` for explicitly smaller comparison
ranges. Its canonical file is for limit 65536, not a smaller run.
Optimization checks use `python -O -B -S` and `python -OO -B -S`.

The full rows retain failures, all word witnesses, source inequalities,
frontier charts, and input grids. 70033 rows; whole-row SHA-256:

`f6e280c6b1253ef7e27069e0b4ca9b2e3c9db0d26b391069dc13efdbec3af61b`.

The same 65536 comparison parameters now have 6556 mergers, adding 2091
while retaining all 4465 exact parent certificates. There are 58980 OUTSIDE
outcomes. The comparison horizon is 12; these are certificate-language
counts, not a convergence census.

## Provenance and evidence limits

Base #127: `f5e7ec9a23fa691d71a5a9f518cbff5529a5ea00`.
Parallel #128: `edd48df6e9c678fa4a65b4ed8f41421dfc92518b`.
The gap, restricted signed template, VL and normalization primitives in
`run.py` retain the parent implementation and are explicitly credited.
The verifier is separately implemented, imports no generator or repository
module, and checks word numerators and raw trajectories independently.
Same-author implementation diversity is not mathematical peer review.

The execution receipt is at
`reports/paired-comparison-universal-finite-synchronization/validation.json`.
No full-checkout root validator, remote CI or Lean run is claimed. This
additive packet changes no old proofs, canonical status registries, source
branches, main, workflow, setting or license.

Review priorities: the all-intercept preconditioning inequality; finite
simultaneous gluing; the 6-free slope obstruction and converse; compatibility
with a prescribed modulus; original-root clocks; and the precise persistent
clock hypothesis in the fixed-source visit budget.
