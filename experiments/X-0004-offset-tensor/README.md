# X-0004 — Offset-tensor and geometry-preserving amplification checks

Experiment ID: `X-0004`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of proposed finite claims `L-0007`, `L-0008`, and `T-0006`

## Research question

Can high-precision finite parity codes enlarge a useful collision alphabet while preserving its exact inverse-root geometry?

## Method

`run.py` uses standard-library exact integer arithmetic only. It:

1. verifies the explicit atomic code
   \[
   V_p=\{e_0,e_{2\cdot3^{p-1}}\}
   \]
   has exact precision \(p\) for \(1\le p\le8\);
2. starts from the two-word base code
   ```text
   1010000
   0001001
   ```
   whose affine constants are `7` and `88`;
3. successively appends atomic suffix codes of precisions `3`, `4`, and `5`;
4. verifies at each level the exact tensor formula
   \[
   D_{UV}=D_U+2^{L_U}E_V;
   \]
5. checks cardinality doubling, precision, unique inverse roots, and preservation of the base difference `9`;
6. promotes the first composite code by a finite all-odd tail and directly traces every branch, confirming that the tail leaves the offset alphabet unchanged.

## Command

```bash
python3 -m py_compile experiments/X-0004-offset-tensor/run.py
python3 experiments/X-0004-offset-tensor/run.py
```

## Expected output

```text
verified L-0008 for precisions 1..8
level=1 words=4 length=26 weight=3 precision=3
level=2 words=8 length=81 weight=4 precision=4
level=3 words=16 length=244 weight=5 precision=5
verified finite odd-tail promotion: prefix_length=26 tail=37 branches=4
all offset-tensor checks passed
```

The checked-in copy is `results/summary.txt`.

## Validation status

The exact assertions and direct trajectory checks were independently reproduced during the authoring session in the available Python execution environment. The GitHub branch itself could not be cloned into the container because the GitHub CLI is unavailable there; reviewers should rerun the two commands above directly from a checkout.

## Interpretation

The experiment confirms a theorem-directed mechanism:

- precision can be supplied independently by explicit atomic suffix codes;
- branch count can be multiplied exactly;
- all previously established finite alphabet geometry can be retained;
- the finite drift tail does not change inverse-root offsets.

This does not establish vertical closure or an infinite admissible orbit.

## Limitations

- The atomic-code lengths grow exponentially in precision.
- The example preserves a fixed difference rather than producing modular coverage growing with depth.
- All constructions are finite.
- No counterexample candidate is proposed.