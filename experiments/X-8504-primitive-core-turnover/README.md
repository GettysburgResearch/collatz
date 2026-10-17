# X-8504 — Primitive-core turnover audit

**Agent:** `gpt56-cylinder-01`  
**Issue:** #43  
**Claim:** `T-8505`  
**Status:** exact finite interface audit

## Question

For exact two-step refunded connector chains, do the middle and terminal boundary words have the claimed exact `2`- and `3`-adic signatures, and are their prime-to-six cores coprime integers greater than one?

## Implementations

- `derive.py` constructs all ordered type triples at two large heights and two exact second-level lifts.
- `verify.py` is separately written, imports no derivation code, uses a different height and a different lift parametrization.

## Replay

```bash
python3 -B experiments/X-8504-primitive-core-turnover/derive.py \
  --output experiments/X-8504-primitive-core-turnover/results/canonical.json \
  --summary experiments/X-8504-primitive-core-turnover/results/summary.txt

python3 -B experiments/X-8504-primitive-core-turnover/verify.py \
  experiments/X-8504-primitive-core-turnover/results/canonical.json
```

## Frozen result

```text
two-step chains:             256
exact binary signatures:     512
exact ternary signatures:    512
coprime adjacent cores:      256

semantic digest:
9610e5be23c04c02a1a1ee3a95c40ce7a96939c103cc67558862c3e3c1de0e09
```

Independent checker:

```text
two-step chains:          32
coprime core checks:      32
all independent checks passed
```

## Limitations

This experiment validates the local arithmetic behind the primitive-core clause. It does not prove the Evertse finite-support argument or construct an infinite ordinary path.
