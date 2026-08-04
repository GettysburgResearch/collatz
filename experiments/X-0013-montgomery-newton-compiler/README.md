# X-0013 — Offset Montgomery lifts and cycle-aligned Newton compilation

Experiment ID: `X-0013`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of proposed exact claims `L-0026`, `L-0027`, `T-0025`, and `O-0010`

## Research questions

1. Is every connector tile an exact offset Montgomery reduction?
2. Can its correction word be extended by an arbitrary finite precision block using only the current finite quotient?
3. Does the corrected 256-stage precision obey
   \[
   Q_{m+1}=2Q_m-11?
   \]
4. Can one Newton lift generate enough finite precision for every connector in the current stage and the next-stage prefix?
5. Do the generated inverses reproduce the deepest within-stage connector seeds among all four source and target tower types?
6. Is the quadratic moving bulk the finite approximation to
   \[
   -\frac74\log_2(3)
   \]
   with exact one-bit-per-stage convergence?

## Method

`run.py` uses exact Python integers only. It:

- exhaustively checks small odd moduli, signed offsets, initial precisions, and extension lengths for the offset Montgomery lift;
- verifies that the lifted correction is the direct canonical solution modulo the larger power of two;
- reconstructs the four phase-`-34` tower cores and verifies
  \[
  K_t=11(t+1),
  \qquad
  G_t=7(t+1);
  \]
- verifies the exact stage precision recurrence
  \[
  Q_{m+1}=2Q_m-11;
  \]
- lifts the stage-start inverse from `Q_m` to the full `2*Q_m` Newton workspace;
- proves that this workspace covers the deepest connector target in the 256-step stage;
- generates the next-stage inverse by squaring the full workspace and truncating;
- compares every generated inverse with direct modular inversion;
- reconstructs all sixteen source/target connector seeds at representative first, internal, near-boundary, and deepest stage positions;
- computes the 2-adic logarithm series modulo powers of two;
- checks
  \[
  \nu_2(u_\infty-u_m)=m+1;
  \]
- verifies the quadratic bulk recurrence;
- records the 64-bit logarithmic-bulk fingerprint.

## Command

```bash
python3 -m py_compile experiments/X-0013-montgomery-newton-compiler/run.py
python3 experiments/X-0013-montgomery-newton-compiler/run.py
```

## Expected output

```text
verified offset Montgomery precision lifts
verified full Newton workspace, deepest connectors, and eleven-bit slack
verified 2-adic logarithmic bulk and exact convergence rate
all Montgomery-Newton compiler checks passed
```

The checked-in copy is `results/summary.txt`.

## Interpretation

The experiment separates two questions that had been conflated.

### Connector-control precision

This is now finite-word computable. One Newton lift doubles the stage-start inverse precision. The resulting finite workspace contains every within-stage connector inverse, and its square contains the complete next-stage prefix. The negative-cycle geometry asks for exactly eleven fewer bits than the full doubled precision.

### Ordinary residual realization

This remains open. Computing the required low residue does not prove that the physical output residual has that residue. The remaining counterexample problem is a self-feeding ordinary Montgomery quotient, not generation of the inverse-prefix control word.

## Limitations

- All checks are finite.
- The experiment does not construct a residual invariant set.
- It does not initialize a marked ordinary Collatz orbit.
- The logarithmic limit is a completion object and is never used as starting data.
- No positive-integer counterexample is proposed.
