# X-6601 — exact finite first-crossing wrap regression

**Associated claims:** `T-6604`, `T-6605`, `T-6606`, `L-6601`, `T-6607`, `L-6602`  
**Status:** **EXACT FINITE REGRESSION / NOT AN ALL-LENGTH PROOF**  
**Agent:** `gpt56-positive-tangent-01`  

## Purpose

This bounded audit reconstructs every admissible first-coefficient-crossing word through length 24 and stress-tests the complete theorem interface:

- exact affine numerator and physical parity replay;
- canonical initial residue and endpoint;
- upper-mechanical extremizer and exact swap distance;
- Hamming/factor-complexity bounds from the swap budget;
- forced repeated-factor length;
- the common real/2-adic displacement numerator;
- earliest-edit 2-adic valuation;
- wrap/no-wrap split;
- quotient and descent-defect transport;
- dangerous-wrap window.

No finite result is extrapolated beyond its declared horizon.

## Implementations

```text
run.py       author-side generator and checker
verify.py    independent reconstruction; imports no author-side module
results/canonical.json
```

Both implementations use Python arbitrary-precision integers and the standard library only. No floating-point quantity enters a proof decision.

## Frozen scope

```text
maximum word length:                 24
valid first-crossing lengths:        15
total first-crossing words:      81,118
nonmechanical wrap words:        35,067
nonmechanical no-wrap words:     46,036
nontrivial canonical failures:        0
```

The sole equality is the trivial shortcut cycle:

```text
j=2,
word=10,
root=endpoint=1.
```

Semantic transcript:

```text
e06b458b7ab7681df89538fbdd038f9b8693dcedb829f6b74d4a1bb0a938dcb2
```

File SHA-256 values from the publishing workspace:

```text
run.py
71e8bab293b442aae10e5df52267b476a2d9fa7978f666bd44e004a9f7f6d403

verify.py
5bdd5b76a653223083a9ef03caa23b9451f9ce31dccd321c3914d788c26b9273

results/canonical.json
348a28d70d17f5b1514f3eaa29402dcc2110c9876eef8a812d3fb40877ba71a7
```

## Replay

```bash
python3 -B -m py_compile \
  experiments/X-6601-first-crossing-wrap/run.py \
  experiments/X-6601-first-crossing-wrap/verify.py

python3 -B experiments/X-6601-first-crossing-wrap/run.py \
  --max-length 24 \
  --check-results \
  experiments/X-6601-first-crossing-wrap/results/canonical.json

python3 -B experiments/X-6601-first-crossing-wrap/verify.py \
  experiments/X-6601-first-crossing-wrap/results/canonical.json
```

## What this does not prove

- no theorem for lengths greater than 24;
- no uniform positivity of the mechanical descent defect;
- no exclusion of every dangerous wrap level;
- no exclusion of nontrivial positive cycles;
- no proof of Collatz.

The finite corpus is an adversarial regression suite for the symbolic identities. The all-length conclusions remain the mathematical obligations in the claim files.
