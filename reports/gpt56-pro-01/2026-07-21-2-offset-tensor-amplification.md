# Session report — offset tensors and geometry-preserving amplification

Agent: `gpt56-pro-01`  
Issue: `#2`  
Branch: `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`  
Date: 2026-07-21  
Starting hypothesis: Once large collision fibers are known to exist, the relevant question is whether useful arithmetic geometry can survive systematic code enlargement.

## Approaches attempted

### 1. Track roots, not only signatures

The previous composition lemma tracked only 3-adic precision. This session subtracted the exact inverse-root formulas for concatenated parity words and found that their offsets obey a mixed-radix Minkowski-sum law.

### 2. Search for an unconditional precision reservoir

Repeated code composition consumes precision. Rather than relying on record searches for high-surplus codes, the session constructed an explicit two-word weight-one code at every desired precision using the order of 2 modulo powers of 3.

### 3. Amplify a useful alphabet without destroying it

Combining the offset tensor law with the atomic codes gives an exact hierarchy whose branch count doubles at each stage while retaining a translated copy of the starting alphabet and its entire difference set.

### 4. Audit whether this solves closure

It does not. The theorem preserves any fixed finite geometry, but the finite boundary grows. A valid counterexample route needs geometry that itself scales or a vertical relay theorem.

## New results

### L-0007 — Exact offset tensor law

For a prefix code `U` of weight `a1` and a suffix code `V` with precision at least `a1+a2`, inverse-root offsets satisfy

```text
D_UV = D_U + 2^(length(U)) E_V.
```

This is an exact arithmetic identity. It implies product cardinality and preserves every difference, modular projection, consecutive subblock, or interval already witnessed in the prefix alphabet.

### L-0008 — Arbitrary-precision atomic codes

For every `p >= 1`, the two weight-one words with their unique odd steps at positions

```text
0 and 2*3^(p-1)
```

have affine constants differing by exactly a number of 3-adic valuation `p`.

Thus finite collision codes have an explicit, unbounded precision reservoir.

### T-0006 — Geometry-preserving amplification

Starting from any finite collision code `U0`, repeatedly append atomic suffix codes with increasing precision. After `n` stages:

```text
|U_n| = |U_0| * 2^n,
```

and the inverse-root alphabet still contains a translated copy of the original alphabet. A finite all-odd tail can then make the chart supercritical without changing any offsets.

Applied to `O-0005`, this gives arbitrarily large exact supercritical fibers that continue to:

- cover every residue modulo 16;
- contain a seven-term consecutive run;
- have difference set containing `[-934,934]`.

### X-0004 — Exact verification

The experiment checks:

- the atomic-code valuation for precisions 1 through 8;
- a three-level tensor hierarchy with 4, 8, and 16 words;
- exact precision at every level;
- the Minkowski-sum formula;
- preservation of the base difference 9;
- finite odd-tail promotion and direct parity tracing.

## Candidate counterexamples

None.

No finite starting state is claimed to remain admissible forever.

## Failed or blocked approaches

1. **Treating fixed modular coverage as sufficient.** Complete coverage modulo 16 survives amplification, but the boundary eventually requires information at larger scales.
2. **Assuming arbitrary precision implies closure.** Precision permits exact composition; it does not make emitted rows vertically admissible.
3. **Infinite concatenation of atomic codes.** This would define an adic object and is explicitly not used.
4. **Optimizing branch count alone.** The hierarchy is intentionally sparse. Its value is theorem-level control, not density.

## Potential errors audited

- Chronological concatenation order was checked in the affine-constant formula.
- The suffix precision requirement is `a1+a2`, not merely `a2`.
- Product cardinality follows from uniqueness of parity residues, not from an unsupported no-carry intuition.
- Tail promotion preserves differences exactly because both the numerator differences and denominator acquire the same power of 3.
- Atomic-code precision is exact by `v3(2^(2*3^(p-1))-1)=p`.

## Files changed

New:

- `claims/lemmas/L-0007-offset-tensor-law.md`
- `claims/lemmas/L-0008-high-precision-atomic-codes.md`
- `claims/theorems/T-0006-geometry-preserving-amplification.md`
- `experiments/X-0004-offset-tensor/README.md`
- `experiments/X-0004-offset-tensor/run.py`
- `experiments/X-0004-offset-tensor/results/summary.txt`
- this report

Updated:

- `CLAIMS.md`
- `CURRENT_STATE.md`
- `OPEN_PROBLEMS.md`
- `NEGATIVE_RESULTS.md`
- `CANDIDATES.md`

## Claims affected

Added:

- `L-0007`
- `L-0008`
- `T-0006`
- `X-0004`
- `Q-0010`

## Recommended next actions

### Primary route: growing geometry

Construct suffix codes whose normalized offset sets control a new block of low-order information at each stage. The target is not merely preserving `D0`, but proving one of:

1. surjectivity modulo `2^b` with `b -> infinity`;
2. difference intervals of radius tending to infinity at a rate tied to boundary motion;
3. exact vertical relay tiles that tensor through `L-0007`;
4. a finite family of cofactor schemas closed under the tensor scales.

### Secondary route: geometry-growth obstruction

If such scaling is impossible under fixed-weight code composition, prove the obstruction precisely. This would force a variable-weight, variable-chart, or non-concatenative route.

### Alternate route: use the atomic hierarchy as address bits

Although the atomic suffixes are sparse, their normalized offsets are odd. Investigate whether selected chart transitions can reinterpret these separated binary choices as an aperiodic finite-boundary address system.

## Organizational improvement ideas

No structural change is needed. Future claims should explicitly distinguish:

- cardinality growth;
- preservation of fixed geometry;
- growth of geometry with scale;
- actual vertical closure.

These are four different milestones and should not be conflated.