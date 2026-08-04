# X-8201 — Exact sparse-resultant audit for fixed negative-cycle pulse supports

**Experiment ID:** `X-8201`
**Associated claim:** `L-8201`
**Issue:** #52
**Agent:** `gpt56-outlier-01`
**Status:** exact finite computation on the declared corpus; `L-8201` remains `PROPOSED`

## Research question

Do the chain pulse formula, one-variable Sylvester-resultant identities, exact 2-adic nonvanishing certificate, coordinate caps, and PR #51 two-pulse specialization hold in exact arithmetic across a broad deterministic corpus?

## Files

```text
run.py                 author-side generator/checker
verify.py              independent implementation; imports no derivation module
results/canonical.json frozen exact artifact
```

Both implementations use only Python arbitrary-precision integers and the standard library.

## Declared parameter range

- primitive negative accelerated cycles:
  - `(1,2)`;
  - `(1,1,1,2,1,1,4)`;
- repetitions:
  - first primitive: `1..5`;
  - second primitive: `1..2`;
- every primitive rotation;
- every support containing the rotated position zero, through support size `5`;
- exhaustive pulse-height grid `1..4` for support sizes through `4`;
- 38 deterministic structured height vectors for support size `5`.

## Verification performed

For each instance the scripts check:

1. exact negative-cycle integrality and valuation replay;
2. direct perturbed affine numerator against the PR #47 pulse cocycle;
3. chain-polynomial telescoping;
4. the two-by-two Sylvester determinant for every pulse coordinate;
5. the Bézout identity and divisibility equivalence;
6. `v_2(E_i)=v_2(c_i)` for every resultant;
7. the coefficient-norm bound and every cap on divisor hits;
8. exact reduction to PR #51's `K(M)` and `J(X)` in the two-pulse case.

## Commands

```bash
python3 -B -m py_compile \
  experiments/X-8201-pulse-resultant-caps/run.py \
  experiments/X-8201-pulse-resultant-caps/verify.py

python3 -B experiments/X-8201-pulse-resultant-caps/run.py \
  --check-results \
  experiments/X-8201-pulse-resultant-caps/results/canonical.json

python3 -B experiments/X-8201-pulse-resultant-caps/verify.py \
  experiments/X-8201-pulse-resultant-caps/results/canonical.json
```

## Frozen output

```text
negative-cycle words:             24
fixed-support packets:         8,842
pulse instances:             875,356
resultant identities:      3,651,452
valuation certificates:    3,651,452
two-pulse K/J matches:          5,856
formal positive divisor hits:       5
maximum cap bit length:              30
```

All five formal hits are the trivial all-`2` valuation word and reconstruct `n=1`:

```text
(1,2)^r -> (2,2)^r,  1<=r<=5.
```

Transcript SHA-256:

```text
59cb5594a945fe98c9d86564a8ea93f37dc343cd5bc5701d8ee4fe67aad0fea7
```

## Interpretation

The computation is a high-volume adversarial check of the proof interface. It does not prove the general theorem and does not search all pulse heights. The theorem's finiteness comes from the symbolic cap proof, not from this bounded corpus.

## Limitations

- support size above `5` is not included in the frozen experiment;
- repetition ranges are finite;
- the corpus contains no nontrivial positive cycle;
- exact agreement of two programs is not independent mathematical review;
- the experiment does not address arbitrary valuation words or divergent orbits.
