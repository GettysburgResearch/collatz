# Session report — active stack cylinders and quotient fuel

Agent: `gpt56-complexity-01`  
Issue: #18  
Branch: `agent/gpt56-complexity-01/18-padic-repetition-rigidity`  
Date: 2026-07-21

## Starting hypothesis

The stationary ghost theorem left active steering open because each stage
changes the target height and high quotient.  The working hypothesis was that
the unused quotient evolves by an exact affine map whose `2`-adic precision can
be audited stage by stage.

## Approaches attempted

1. Rewrote the stack identity with
   ```text
   M_m=64^(9m+1), A_m=81^(9m+1), c_m=(M_m+17)/81.
   ```
2. Solved one transition to height `n` for its unique context residue and
   quotient carry.
3. Factored every valid context into demanded low block plus free high quotient.
4. Composed future residue cylinders backward using odd modular inverses.
5. Derived the exact initial modulus selected by a finite height directive.
6. Built exhaustive small-height and bounded balanced-directive replays.

## New results

### Proposed rigorous results

- `L-9406`: if
  ```text
  x=r_(m,n)+64^(9n+1)*y,
  ```
  then the next context is exactly
  ```text
  x'=81^(9m+1)*y+k_(m,n).
  ```
  The unused quotient is carried by an odd affine `2`-adic isometry.

- `T-9409`: every finite schedule `m_0,...,m_K` selects exactly one initial
  cylinder
  ```text
  R_K mod Q_K,
  Q_K=product_(i=1)^K 64^(9m_i+1).
  ```
  Conversely every context in that cylinder realizes the schedule integrally.

- Every infinite schedule selects one unique `2`-adic initial context.  It is an
  ordinary nonnegative integer iff the least representatives `R_K` eventually
  stabilize.

- For increments in `{17,18}`, the selected initial precision satisfies
  ```text
  54*K*m_0+459*K*(K+1)+6K
   <= log_2 Q_K
   <=54*K*m_0+486*K*(K+1)+6K.
  ```
  Thus finite tower depth consumes quadratic initial precision.

### Exact computational results

`X-9404` checks:

- 1,360 finite schedules over heights `{0,1,2,3}`;
- 5,440 exact cylinder members;
- 435,696 lower-bit perturbations, all failing;
- 5,440 quotient-isometry pairs;
- 128 contexts in complete small-modulus uniqueness scans;
- a deterministic 24-stage Fibonacci `17/18` directive prefix.

At stage 24:

```text
last height = 418,
cylinder precision = 282,888 bits,
least representative bit length = 282,888.
```

Canonical SHA-256:

```text
73a878073e3e8e39e6e950ad0e4585c522cd7fe1794639dc5b015a3b5115be3f
```

## Candidate counterexamples

None.  The balanced replay gives finite initial cylinders only.  No eventual
stabilization, ordinary infinite context, chart-lifted seed, or `K-####`
candidate is claimed.

## Failed approaches and negative information

- Precision growth alone does not prove nonordinary behavior; an ordinary
  integer may have a compact formula even when many residue digits are fixed.
- Odd-affine quotient transport is conservation of distinguishability, not a
  computational lower bound.
- The finite balanced replay has nonzero extension blocks at every recorded
  checkpoint, but this bounded observation cannot be extrapolated.
- Positivity is not automatic from the integrality cylinder theorem.

## Potential errors to audit

1. Verify the exponent `A_m=81^(9m+1)` in the quotient map.
2. Reconstruct the backward cylinder induction and ensure the modulus is the
   product of the **future** stage moduli `M_1...M_K`.
3. Audit the converse: every context in the final cylinder must replay every
   stage.
4. Check the stabilization equivalence for ordinary nonnegative representatives.
5. Keep the precision theorem separate from claims of entropy or algorithmic
   complexity.

## Files changed

- `research/padic-repetition/claims/L-9406-active-quotient-conjugacy.md`
- `research/padic-repetition/claims/T-9409-finite-tower-cylinder.md`
- `research/padic-repetition/ACTIVE_CYLINDERS.md`
- `research/padic-repetition/Q-9408-active-steering.md`
- `experiments/X-9404-active-cylinders/README.md`
- `experiments/X-9404-active-cylinders/run.py`
- `experiments/X-9404-active-cylinders/results/canonical.json`
- this report

## Claims affected

New IDs: `L-9406`, `T-9409`, `X-9404`.  `Q-9408` is narrowed from an open
transition question to the exact stabilization/block-tail problem.

## Recommended next actions

1. Independently reconstruct `L-9406` and `T-9409`.
2. Derive a direct recurrence for
   ```text
   a_K=(R_(K+1)-R_K)/Q_K.
   ```
3. Prove infinitely many nonzero `a_K` for every admissible `17/18` directive,
   or construct an eventually zero tail.
4. Add positivity and chart-class replay to any candidate stabilized context.
5. Compare `a_K` with the demand-tree lift digit and PR #16 carry-energy states.

## Organizational improvement ideas

Every finite counterexample-construction search should report its **cylinder
modulus**, least representative, and extension block—not only one found seed.
This makes finite compatibility, uniqueness, and ordinary stabilization visible
across stack, marked-spine, and compressed-cycle programs.
