# X-9402 — Complexity-criticality and transducer interfaces

Experiment ID: X-9402  
Agent: `gpt56-complexity-01`  
Issue: #18  
Associated claims: D-9402, L-9403, T-9404, T-9405, T-9406, R-9401  
Classification: exact finite verification and bounded illustrative computation

## Research question

How does the repetition-height mechanism scale across general expanding digit
charts, and what finite-state resources are required to transfer a
low-complexity directive into an emitted survivor code?

## Environment

- Python 3.11 or newer;
- standard library only;
- deterministic seed `9402` for the bounded transducer census;
- no network, solver, or external data.

## Replay

```bash
python3 -B -m py_compile experiments/X-9402-complexity-criticality/run.py
python3 -B experiments/X-9402-complexity-criticality/run.py \
  --check-results experiments/X-9402-complexity-criticality/results/canonical.json
```

To regenerate the frozen result:

```bash
python3 -B experiments/X-9402-complexity-criticality/run.py \
  --write-results experiments/X-9402-complexity-criticality/results/canonical.json
```

Canonical result SHA-256:

```text
a7903f3ea552cf7e96884832473b9bb4c86ec99be3da47e58ab4017f9e51f79b
```

## Frozen scope

The script checks:

1. **General periodic height.** Exact `Fraction` reconstruction, odd reduced
   denominator, strict `<N^(r+s)` height, and real digit-range containment for
   10,680 prefix/period cases across five chart ratios.
2. **First-difference separation.** Exact valuation
   `L*m+v_2(d_m-e_m)` on 39,360 distinct finite-code pairs.
3. **Finite-state transfer.** The factor-key inequality for 128 deterministic
   non-erasing transducers (`Q,B<=4`) at 896 parameter combinations over a
   Fibonacci directive.
4. **Local coding.** All 256 binary radius-one sliding-block maps at 1,792
   factor-length checks.
5. **Growing-gap loophole.** The exact two-one factor construction behind
   T-9406 at four finite scales for gap increments `153/162`.
6. **Criticality constants.** Frozen numerical values for the ratios
   `64/81`, `512/729`, `2^17/3^11`, `2^22/3^14`, and `2^44/3^28`.

## Interpretation boundary

The finite checks prove only their frozen arithmetic and combinatorial cases.
They do not prove the universal theorem files, construct an ordinary survivor,
close an infinite stack grammar, or resolve the Collatz conjecture.  Universal
claims rest on their written proofs and remain `PROPOSED` pending independent
reconstruction.