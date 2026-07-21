# X-9408 — Block Gaussian-binomial Padé verification

Experiment ID: X-9408  
Agent: `gpt56-complexity-01`  
Issue: #18  
Associated claims: L-9410, T-9414, T-9415, R-9403  
Classification: exact finite verification and bounded height measurement

## Research question

Does the explicit common denominator in L-9410 simultaneously cancel every
phase of a periodic stack block, and do the finite reduced approximants display
the predicted above-threshold behavior for periods two and three?

## Environment

- Python 3.11 or newer;
- standard library only;
- exact `Fraction` arithmetic;
- no network, solver, randomness, or external data.

## Replay

```bash
python3 -B -m py_compile experiments/X-9408-block-pade/run.py
python3 -B experiments/X-9408-block-pade/run.py \
  --check-results experiments/X-9408-block-pade/results/canonical.json
```

To regenerate:

```bash
python3 -B experiments/X-9408-block-pade/run.py \
  --write-results experiments/X-9408-block-pade/results/canonical.json
```

Canonical SHA-256:

```text
9895b3723a3a5d19f43ef5158c18a0511f58f923df2f1919a68771f1f322583c
```

The frozen replay uses large exact rational numbers and may take roughly half a
minute on a typical contemporary machine.

## Frozen scope

1. **Period two.** The word `(17,18)` at Padé orders `1,2,3`.
2. **Period three.** The word `(17,17,18)` at Padé orders `1,2`.
3. **Exact phase cancellation.** Every one of the `r` phases has `n`
   consecutive zero block coefficients.
4. **Exact first error.** The first nonzero combined coefficient has the
   valuation stated in L-9410 and is strictly smaller than the next two.
5. **Denominator unit.** Every evaluated common denominator is a `2`-adic unit.
6. **Reduced height.** The final rational approximant is reduced exactly and its
   numerator/denominator bit length is frozen.
7. **Threshold constants.** The universal asymptotic constants are recorded for
   period lengths `1` through `6`.

Selected exact measurements:

| word | order | error `v_2` | reduced height bits | bit-length exponent |
|---|---:|---:|---:|---:|
| `17,18` | 1 | 14,454 | 12,175 | 1.187186858316 |
| `17,18` | 2 | 55,368 | 48,307 | 1.146169292235 |
| `17,18` | 3 | 122,742 | 108,409 | 1.132212270199 |
| `17,17,18` | 1 | 56,664 | 53,775 | 1.053723849372 |
| `17,17,18` | 2 | 222,840 | 214,373 | 1.039496578394 |

The measured ratios are not the theorem; they are finite adversarial checks of
the formulas and trend toward the rigorous limiting lower bounds

```text
period 2: 1.104127068750...,
period 3: 1.025260849553... .
```

## Interpretation boundary

The experiment proves only its frozen exact arithmetic. The universal Padé
identity and irrationality results rest on the written proofs. It does not
prove anything about period length at least four, the balanced nonperiodic
`17/18` directive, an ordinary M1 witness, or the Collatz conjecture.
