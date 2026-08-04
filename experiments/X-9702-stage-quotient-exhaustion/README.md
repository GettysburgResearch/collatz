# X-9702 — Exact stage-quotient exhaustion checks

**Experiment ID:** `X-9702`  
**Status:** `EMPIRICAL / EXACT FINITE CHECK`  
**Agent:** `gpt56-cylinder-01`  
**Issue:** `#31`  
**Associated claims:** `L-9702`, `T-9703`, `Q-9702`

## Research question

Do the finite algebraic interfaces used by `T-9703` replay exactly?

1. Do the PR #3 exponent formulas imply
   `3^(A_m)/2^(D_(m+1)) < 1/4` by exact rational arithmetic?
2. Does every finite chain of canonical local odd-affine tiles have a canonical
   composite cap `0 <= S < P`?
3. In exact sample zippers with `q_(m+1)>4N_m`, does the ordinary free quotient
   become zero and thereafter force `S_m=R_(m+1)`?

The experiment does **not** prove the universal infinite theorem and does not
compute a Collatz counterexample.

## Files

- `derive.py` — formula-based derivation, exhaustive small composite audit, and
  deterministic sample zipper construction;
- `verify.py` — independently written checker that does not import `derive.py`;
- `results/canonical.json` — frozen exact payload;
- `results/summary.txt` — compact reproducibility summary.

## Commands

Run from the repository root:

```bash
python3 -B -m py_compile \
  experiments/X-9702-stage-quotient-exhaustion/derive.py \
  experiments/X-9702-stage-quotient-exhaustion/verify.py

python3 -B experiments/X-9702-stage-quotient-exhaustion/derive.py \
  --output experiments/X-9702-stage-quotient-exhaustion/results/canonical.json \
  --summary experiments/X-9702-stage-quotient-exhaustion/results/summary.txt

python3 -B experiments/X-9702-stage-quotient-exhaustion/verify.py \
  --check-results experiments/X-9702-stage-quotient-exhaustion/results/canonical.json
```

## Frozen results

```text
stage exponent rows: 17
exhaustive local tiles: 54
exhaustive composite chains: 160434
composite-cap digest: 62f0d9653787fb06b3c326e055920abd44c8d5e11dfb220a64b17991a3f5e527
deterministic quotient paths: 64
deterministic quotient stages: 512
maximum positive-quotient steps: 4
quotient-path digest: 1b48eb9fcfab91f312c9562bf9d90a8123f0764307985b6971c7c6078bbf17f7
payload digest: f6d6e951887b09f7aeb6968392e100efb4fbfecc31995fe0ed9d916f663800e7
all derivation checks passed
```

Independent checker:

```text
independent composite chains: 178808
independent composite digest: 2ae3900c132e3a62eae013d622fdacebc75aec480f60f703e9a5e194ee66a035
independent quotient paths: 25
verified zero-tail steps: 163
independent quotient digest: 1bf6e2d4f70c2f2fdf2898f7e620cd6915e0c58e1b18a16a54fdc1f11e2a182e
committed payload digest: f6d6e951887b09f7aeb6968392e100efb4fbfecc31995fe0ed9d916f663800e7
all independent stage-quotient checks passed
```

## Independent-checker separation

The derivation computes composite corrections from the affine composition
formula. The checker instead enumerates every residue modulo the complete small
radix and accepts the unique residue whose **direct local replay** remains
integral and nonnegative. It uses a different finite parameter family.

The two scripts also construct different quotient-path families and record
different digests.

## Environment

- Python 3 standard library only;
- exact integers and `fractions.Fraction` only;
- no random seed or floating-point value on the critical path.

## Interpretation

The finite checks support the following proof interfaces:

- exact exponent arithmetic;
- exact canonical cap range;
- exact normalized-height inequality;
- exact zero-quotient tail behavior.

The theorem's quantifier over every infinite stage directive comes from the
mathematical proof in `T-9703`, not from these finite checks.

## Limitations

- No full 256-transition PR #3 stage offset is recomputed here.
- No sampled cap-correction mismatch is promoted to a universal obstruction.
- No ordinary marked initialization, infinite physical replay, or growth proof
  is supplied.
