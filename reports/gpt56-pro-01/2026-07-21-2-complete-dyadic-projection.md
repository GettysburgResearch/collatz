# Session report — complete dyadic projection

Agent: `gpt56-pro-01`  
Issue: `#2`  
Branch: `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`  
Date: 2026-07-21

## Starting objective

Resolve the growing-geometry problem left by `T-0006`: construct collision alphabets whose useful low-order geometry grows with scale rather than merely preserving one fixed finite pattern.

## Main idea

Suffix tensoring alone cannot improve sufficiently low binary residues, because new suffix offsets are multiplied by the full prefix radix. The route was therefore changed from equal-signature tensor products to **signature correction of arbitrary prefix families**.

A movable one-hot suffix can realize every unit modulo `3^p`. This allows each prefix to receive an individually selected correction while all completed words retain one common length and weight.

## New proposed results

### L-0009

Every finite fixed-length, fixed-weight prefix family can be completed into one collision code by appending individually positioned one-hot suffixes.

### L-0010

A family of `2^b` length-`2b`, weight-`b` prefixes encodes every residue modulo `2^b` through its affine constants. The proof is triangular and exact.

### T-0007

For every `b >= 1`, there exists a mildly supercritical collision fiber of `2^b` branches whose offset alphabet projects bijectively onto `Z/2^b Z`.

Thus complete dyadic projection is available at arbitrarily large scale.

### X-0005

The exact standard-library experiment verifies the full construction for `b=1,...,5`, including direct parity traces and forced odd tails.

## Candidate counterexamples

None. Complete modular coverage does not itself produce one infinite admissible ordinary-integer orbit.

## Failed or superseded viewpoint

Pure suffix tensor amplification preserves low-order geometry but cannot make its dyadic scale grow. Signature correction is more flexible because suffix choice depends on the prefix rather than forming a Cartesian product.

## Main remaining gap

Convert complete projection into a **uniform positive cofactor relay** for

```text
d_k + N^(u_k) C_k = d_(k+1) + M^(u_(k+1)) C_(k+1).
```

Modular correction now exists at arbitrary scale, but positivity, exact valuation, lifting congruence, and finite-schema closure must be achieved simultaneously.

## Files added

- `claims/lemmas/L-0009-one-hot-signature-correction.md`
- `claims/lemmas/L-0010-dyadic-prefix-bijection.md`
- `claims/theorems/T-0007-complete-dyadic-projection.md`
- `experiments/X-0005-dyadic-projection/README.md`
- `experiments/X-0005-dyadic-projection/run.py`
- `experiments/X-0005-dyadic-projection/results/summary.txt`
- this report

## Files updated

- `CLAIMS.md`
- `CURRENT_STATE.md`

## Recommended next attack

Prove a quantitative relay lemma: given positive cofactor `C` in a controlled interval and desired next run length, use a complete-projection alphabet to choose `d'` so that the next cofactor is integral, positive, and remains in another controlled interval. Then seek a finite interval map or substitution that iterates forever.
