# X-9502 — Structured audit of the H phase frontier

**Experiment ID:** `X-9502`  
**Agent:** `gpt56-h-01`  
**Issue:** [#17](https://github.com/gfreund123/collatz/issues/17)  
**Status:** `EMPIRICAL`

## Research questions

1. Do the canonical endpoint bounds `0 <= A < U`, `0 <= Y < V` hold on long
   random words?
2. Does the fixed-point phase identity
   `A=t+rho*U`, `Y=t+rho*V` hold exactly?
3. Is the proposed signed-displacement property closed under same-sign
   concatenation on tested words?
4. Do critical mechanical first-contracting words expose a counterexample to
   `C-9501`?
5. Does the naive substitute bound `t_w <= 2^(3*r_0)` fail?
6. What are finite upper candidates for the extremal representatives `mu_L` in
   a bounded alphabet search?

## Command

```bash
python run.py \
  --seed 9502 \
  --random-trials 20000 \
  --random-max-length 40 \
  --random-max-letter 10 \
  --critical-max-length 200 \
  --mu-max-length 5 \
  --mu-max-letter 12 \
  --output results/summary.json
```

## Environment

- Python 3.11 or newer
- standard library only
- exact Python integers and `fractions.Fraction`; no floating-point arithmetic
  is used for theorem checks

The decimal logarithm is used only to generate the critical mechanical words at
high precision. Every subsequent multiplier, fixed-point, phase, and cylinder
calculation is exact.

## Recorded result

The committed run checked:

- 20,000 random canonical input/output ranges;
- 20,000 exact fixed-point phase identities;
- 17,562 same-sign concatenation closures;
- 199 critical mechanical first-contracting words of lengths 2 through 200;
- no signed-displacement failure in those critical words;
- the first failure of the naive first-letter fixed-point bound at length 25;
- exhaustive finite `mu_L` upper candidates for lengths 1 through 5 over
  `r in {0,...,12}`.

Digest:

```text
cf995d0b83acd14440ad4b2442012ba07726f3b68fa51b38ef9f58f4a542d9d2
```

## Interpretation

The experiment supports `L-9511` and `L-9512`, but those claims have direct
proofs and do not depend on finite testing. It also shows that replacing the
canonical residue by the first-letter lower bound is invalid. The finite
`mu_L` data are upper candidates only; alphabet truncation is not a universal
minimum proof.

## Limitations

- No finite run proves `C-9501` or termination.
- Random testing cannot establish mixed-sign closure.
- The `mu_L` search omits letters above 12.
- Critical mechanical words are one structured family, not all first-contracting
  words.
