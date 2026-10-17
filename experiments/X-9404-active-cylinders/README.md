# X-9404 — Active stack cylinder verification

Experiment ID: X-9404  
Agent: `gpt56-complexity-01`  
Issue: #18  
Associated claims: L-9406, T-9409  
Classification: exact finite verification and bounded directive replay

## Research question

Does a prescribed active stack-height schedule select exactly one initial
residue cylinder, while the unused high quotient evolves by odd affine
isometries?

## Environment

- Python 3.11 or newer;
- standard library only;
- exact arbitrary-precision integer arithmetic;
- no network, solver, randomness, or external data.

## Replay

```bash
python3 -B -m py_compile experiments/X-9404-active-cylinders/run.py
python3 -B experiments/X-9404-active-cylinders/run.py \
  --check-results experiments/X-9404-active-cylinders/results/canonical.json
```

To regenerate:

```bash
python3 -B experiments/X-9404-active-cylinders/run.py \
  --write-results experiments/X-9404-active-cylinders/results/canonical.json
```

Canonical SHA-256:

```text
73a878073e3e8e39e6e950ad0e4585c522cd7fe1794639dc5b015a3b5115be3f
```

## Frozen scope

1. **Finite height grid.** All `1,360` schedules of one through four stages
   over heights `{0,1,2,3}`.
2. **Cylinder membership.** `5,440` exact member replays and `435,696`
   lower-bit perturbation replays, every perturbation failing before completion.
3. **Quotient isometry.** `5,440` exact odd-affine quotient-pair checks.
4. **Small exhaustive uniqueness.** Complete scans of `128` contexts for the
   two one-stage cases with modulus `64`.
5. **Balanced directive.** A deterministic Fibonacci `17/18` increment prefix
   through `24` stages, with nested cylinders replayed at ten checkpoints.
6. **Precision scale.** The 24-stage checkpoint fixes exactly `282,888` initial
   binary digits; its least representative also has bit length `282,888`.

## Interpretation boundary

The finite checks validate the exact edge algebra, backward cylinder recursion,
and frozen precision counts. They do not prove nonstabilization for every
infinite directive, exclude an ordinary M1 witness, or resolve the Collatz
conjecture. The universal claims rest on their written proofs and remain
`PROPOSED` pending independent reconstruction.
