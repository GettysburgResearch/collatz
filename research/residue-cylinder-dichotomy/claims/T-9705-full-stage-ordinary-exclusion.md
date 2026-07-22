# T-9705 — Universal ordinary exclusion for the corrected 256-stage class

**Claim ID:** `T-9705`  
**Title:** Every infinite corrected 256-transition directive has infinitely many nonzero residue blocks and its unique 2-adic completion is not any signed ordinary integer  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-22  
**Dependencies:** `L-9701`--`L-9706`, `T-9703`, `T-9704`; frozen PR #3 corrected-stage interface; Evertse 1984 Corollary 1  
**Scope:** the complete frozen class of arbitrary physically overlapping corrected 256-transition stage directives

## Theorem

For every infinite directive in the frozen corrected-stage class,

```text
a_k != 0 for infinitely many k,                       (1)
```

and the unique completion selected by its nested initial cylinders satisfies

```text
alpha in Z_2 but alpha not in Z.                       (2)
```

In particular, no signed ordinary residual and hence no positive ordinary marked Collatz initialization realizes the complete infinite directive.

This proves side **A** of the residue-cylinder dichotomy for the genuinely supercritical normalized 256-transition class. The quantifier is over the whole directive class, not sampled schedules or eventually periodic controls.

## Proof

Fix an arbitrary infinite physically overlapping directive. `L-9701` gives one unique 2-adic initial completion satisfying every finite complete-stage cylinder.

Assume for contradiction that this completion is a signed ordinary integer. Exact complete-stage equivalence propagates it to a signed integer trajectory through every prescribed stage.

`L-9705` proves that the signed quotient has only two possible tails:

1. `Y_m=0`, producing the cap stitch `S_m=R_(m+1)`;
2. `Y_m=-1`, producing the co-cap stitch
   ```text
   3^(A_m)-S_m=2^(D_(m+1))-R_(m+1).
   ```

Increase the starting scale so the appropriate tail and the stabilized connector formulas both hold.

`L-9704` converts either tail to a positive connector-free endpoint sequence and an exact 258-coordinate homogeneous stage relation. Its 256 internal coordinates are `{2,3}`-units.

`L-9706` proves that the primitive stage tuples are

- nondegenerate;
- `(1,1/50,{2,3})`-admissible in Evertse's sense; and
- pairwise projectively distinct.

Corollary 1 of Evertse's 1984 theorem permits only finitely many such projective zero sums. The infinite stage trajectory would produce infinitely many. Contradiction.

Thus the unique completion is not any signed ordinary integer.

If the cumulative new residue blocks were eventually zero, the least initial representatives would stabilize to a nonnegative ordinary integer. That has just been excluded. Therefore (1) follows. ∎

## Why the supercritical stage still fails

The current complete stage expands relative to its own denominator, so the direct finite trap of `T-9702` does not apply. The proof instead uses three different completion-height effects:

1. the **next** complete radix contracts the signed stage quotient to `0` or `-1`;
2. cap and co-cap representatives occupy less than one part in 275 of their complete cylinders;
3. after the connector-free change of coordinate, the entire outside-`{2,3}` content of a 258-term zero sum is confined to two endpoints and consumes less than `1/50` of the projective height.

The last inequality is exactly within Evertse's `d<1` admissibility range.

## Ordinary-integer audit

- Finite compatible prefixes are never treated as an infinite initialization.
- The 2-adic completion is assumed ordinary only for contradiction.
- Negative ordinary integers are covered by the co-cap alternative.
- No logarithm digits, entropy surplus, or precomputed infinite word is initialized.
- No fixed-word repetition or finite-rank endpoint hypothesis is used.
- No `K-####` candidate is created because the theorem excludes every ordinary initialization in the frozen class.

## Dependency and status audit

- Every native claim remains `PROPOSED` pending independent reconstruction.
- The frozen PR #3 tower and stage formulas retain their source-branch status.
- Evertse's 1984 Corollary 1 is an external black box; `L-9706` reproduces and checks its exact native hypotheses.
- No PR #3, PR #13, PR #16, PR #19, PR #20, PR #32, PR #34, or issue #21 status is silently promoted.

## Review priorities

1. Reconstruct the scaled connector-free coordinate and physical identity.
2. Check the signed `Y=-1` co-cap normalization.
3. Reproduce the co-cap completion-height transfer.
4. Inspect Evertse's original Corollary 1.
5. Audit the primitive gcd bound and outside-prime product.
6. Verify projective distinctness after primitive normalization.
7. Reconstruct the bridge from an ordinary initial completion to the signed stage trajectory.

There is no remaining mathematical gap inside the stated frozen class if these interfaces pass independent review.