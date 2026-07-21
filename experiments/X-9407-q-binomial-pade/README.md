# X-9407 — `q`-binomial Padé verification

Experiment ID: X-9407  
Agent: `gpt56-complexity-01`  
Issue: #18  
Associated claims: L-9409, T-9412  
Classification: exact finite verification of the constant-increment Padé family

## Research question

Do the Gaussian-binomial Padé denominators cancel the exact coefficient block
claimed by L-9409, and do the resulting rational approximants cross the
rational-target approximation exponent one in the constant-increment stack
models?

## Environment

- Python 3.11 or newer;
- standard library only;
- exact `Fraction` arithmetic;
- no network, solver, randomness, floating-point algebra, or external data.

## Replay

```bash
python3 -B -m py_compile experiments/X-9407-q-binomial-pade/run.py
python3 -B experiments/X-9407-q-binomial-pade/run.py \
  --check-results experiments/X-9407-q-binomial-pade/results/canonical.json
```

To regenerate:

```bash
python3 -B experiments/X-9407-q-binomial-pade/run.py \
  --write-results experiments/X-9407-q-binomial-pade/results/canonical.json
```

Canonical SHA-256:

```text
bfdf48d1574de35a72a16b0d250c62df2da736e86bd4d111556f9a0e2a54e723
```

## Frozen scope

For `T=64/81`, starting height `m=1`, increments `d in {17,18}`, and Padé
orders `n=1,...,5`, the script verifies:

1. the Gaussian-binomial convolution coefficients at degrees
   `n,...,2n-1` vanish exactly;
2. the degree-`2n` coefficient equals the closed first-error product;
3. every later checked term has strictly larger `2`-adic valuation;
4. the evaluated denominator is a `2`-adic unit;
5. the exact first-error valuation is
   ```text
   27*d*(3*n^2+n)+12*n*(9*m+1);
   ```
6. the evaluated rational approximant is reduced before height is measured;
7. every finite approximation exponent exceeds one and trends toward
   ```text
   9/log_2(81)=1.419591945535... .
   ```

## Interpretation boundary

The frozen calculations validate the exact finite Padé interfaces. They do not
prove L-9409 or T-9412 for arbitrary order, establish transcendence, settle the
balanced nonperiodic `17/18` directive, construct an ordinary stack context, or
resolve the Collatz conjecture.