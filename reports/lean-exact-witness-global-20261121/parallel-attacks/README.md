# Parallel-attack checkpoint execution evidence

This directory records the actual fresh build and exact generator replays
for the alphabet-four and low-interval continuation of PR177. The mathematical
claims and remaining universal obligation are in the
[research packet](../../../research/lean-exact-witness-global-20261121/README.md).

- `checkpoint-seven-build.txt`: a clean-output Lean 4.34.1 build, **27 jobs**.
- `checkpoint-seven-axioms.txt`: the complete audit with warnings treated
  as errors; **92 declarations**, two with no axioms and all others using
  only subsets of `propext`, `Classical.choice`, and `Quot.sound`.
- `checkpoint-seven.json`: hashes of all **26 Lean input files**, the new
  mathematical notes and implementations, and the exact scope of the runs.
- `cofinal-replay.json`: **30** complete-source rewrites from six supplied
  certificates and five requested bounds up to `2^1024`. Each output
  certificate and strict rank decrease was checked. The receipt keeps
  exact child values, word hashes, and grade counts; the generator can
  reproduce every full word. Normal and optimized Python outputs match.
- `denominator-clear-replay.json`: **22** whole-affine progression checks
  at eleven denominator powers, each at the generated minimal first gap
  and seventeen further halvings. Normal and optimized outputs match.
- The analytic quotient replay and the exact negative-residual path are
  recorded separately in
  [`../section-mass/critical-inverse-trace.json`](../section-mass/critical-inverse-trace.json).

The arbitrary-bound and arbitrary-index assertions are the Lean theorems,
not extrapolations from these selected runs. The inverse Green-function
argument is written mathematics and is not claimed as a Lean theorem.

The repository-wide gate is separate from the proof build. It is run in a
complete clean checkout of the final local commit before publication:

```sh
python -X utf8 -B tools/validate.py --regressions --receipt /tmp/collatz-parallel-clean-gate.json
```

Its receipt is outside that checked checkout so the gate checks the same
clean tree that is published. The final checked tree identity, remote commit,
and actual gate result are recorded in PR177. A connector-created commit may
have a different commit ID from the local checked commit; publication requires
their complete tree IDs to be identical.

Full Collatz and the original residue implication remain open. These receipts
do not change the hypotheses of any conditional closing theorem.
