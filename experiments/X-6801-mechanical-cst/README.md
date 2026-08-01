# X-6801 — Exact upper-mechanical first-crossing descent certificate

**Experiment ID:** `X-6801`  
**Associated theorem:** `T-6806`  
**Status:** exact finite certificate plus exact analytic induction interface  
**Agent:** `gpt56-positive-entropy-01`

## Scope

The experiment reconstructs every valid upper-mechanical coefficient-first-crossing word with

```text
2 <= j < 373
```

and computes its exact canonical source and endpoint.

It also certifies the three integer inequalities used to begin the
source-qualified analytic induction at

```text
j = 373, 374, 375.
```

## Result

```text
valid finite rows:       234
nontrivial failures:       0
sole equality:
  j=2, word=10, root=endpoint=1
```

For every other finite row,

```text
canonical_root > canonical_endpoint.
```

The exact analytic base rows verify

```text
H_j^10 > 6^10 j^143
(j+3)^143 < 2^10 j^143
```

for `j=373,374,375`, with

```text
L_j = floor((j-1)/3),
H_j = 2(2^L_j+1)-3(j-1).
```

## Independent implementations

```text
run.py
  builds the affine numerator, uses modular inversion for the canonical root,
  and emits the canonical artifact;

verify.py
  imports no generator module and reconstructs the canonical pair by exact
  one-bit rectangle lifting.
```

Both use Python arbitrary-precision integers and the standard library only.

## Replay

```bash
python3 -B -m py_compile \
  experiments/X-6801-mechanical-cst/run.py \
  experiments/X-6801-mechanical-cst/verify.py

python3 -B experiments/X-6801-mechanical-cst/run.py \
  --output /tmp/X-6801.json

python3 -B experiments/X-6801-mechanical-cst/run.py \
  --check-results \
  experiments/X-6801-mechanical-cst/results/canonical.json

python3 -B experiments/X-6801-mechanical-cst/verify.py \
  experiments/X-6801-mechanical-cst/results/canonical.json
```

Expected verifier output:

```text
all independent X-6801 checks passed
5d88f47548ca6716b7c10cf839dc7d65eb6efdff748b35cca9d709aa36771d2e
```

## File hashes from the authoring replay

```text
run.py
6024ad9990b27a7113dc68172c01302ade01f1ae0713ce01819e41c17327307e

verify.py
9831755383c1f608072c0e63d050c09245a6fc6dc795d14843e59a793496f689

results/canonical.json
d4ebf6c092d9423e0c1e2088050c50cb31cadd6ad8761b6b179613f265d5afaf
```

## Proof boundary

The experiment does not prove Rhin's theorem.  The all-length conclusion in
`T-6806` is source-qualified by the bound

```text
j log 2-q log 3 >= j^(-13.3).
```

The finite artifact does not prove:

- descent for arbitrary nonmechanical first crossings;
- absence of nontrivial positive cycles;
- CST;
- Box 1;
- Collatz.
