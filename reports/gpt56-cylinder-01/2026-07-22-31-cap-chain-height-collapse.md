# Session report — cap-chain height collapse

**Agent:** `gpt56-cylinder-01`  
**Issue:** `#31`  
**Branch:** `agent/gpt56-cylinder-01/31-residue-cylinder-dichotomy`  
**Date:** 2026-07-22

## Starting hypothesis

`T-9703` reduces every hypothetical ordinary 256-stage trajectory to the
cap-correction equality

\[
S_m(w_m)=R_{m+1}(w_{m+1}).
\]

The next question was whether the resulting correction sequence still has
archimedean height comparable to its complete dyadic cylinders, or whether the
stage surplus and bounded local offsets force a much smaller global height.

## Approaches attempted

### 1. Exact full-stage samples

Several complete million-bit PR #3 stages were computed locally for constant and
simple periodic type words at scale `m=8`, with one scale-`9` comparison. Every
sample had a nonzero mismatch `S_m != R_(m+1)`. These computations were used only
to inspect scale and sign; no sampled mismatch is promoted to a claim or
committed as a universal experiment.

### 2. Search for a universal small-modulus obstruction

Parity and small-modulus residues varied across the sampled words. No universal
mod-`2`, mod-`3`, or mod-`5` obstruction was found. This route was abandoned
rather than overinterpreted.

### 3. Normalize the complete affine offset

Each local map has

\[
-q_j<C_j<N_j
\]

and corrected-stage slope `lambda_j>1`. Consequently its normalized offset has
absolute value below `lambda_j`. After composition, every one of the 256 offset
terms is below the full stage multiplier. This produces the uniform bound

\[
|\beta_m|<256\Lambda_m.
\]

This was the decisive step.

## New results

### `L-9703` — normalized stage-offset bound

All 256 corrected local slopes are strictly greater than one. The complete
stage map

\[
z_{m+1}=\Lambda_mz_m+\beta_m
\]

satisfies

\[
|\beta_m|<256\Lambda_m
\]

for every admissible type word. Equivalently the integer offset obeys

\[
|C_m|<256N_m.
\]

### `T-9704` — cap-chain height collapse

On a cap-correction chain,

\[
R_{m+1}=\Lambda_mR_m+\beta_m.
\]

Since `Lambda_m>257`,

\[
R_{m+1}+257<\Lambda_m(R_m+257).
\]

Using the exact upper bound `log_2 3<65/41`,

\[
\log_2\Lambda_m
<
\frac{161341}{10496}2^m+rac{1024}{41}.
\]

Thus

\[
\log_2(R_m+257)
<
\log_2(R_M+257)
+rac{161341}{10496}(2^m-2^M)
+rac{1024}{41}(m-M).
\]

Compared with

\[
D_m=\frac{1085579}{256}2^m+2816,
\]

this yields

\[
\limsup
\frac{\log_2(R_m+257)}{D_m}
\le
\frac{161341}{44508739}
<\frac1{275}.
\]

Any surviving ordinary correction uses asymptotically less than `0.363%` of the
available cylinder bits.

### `X-9703` — exact finite checks

The derivation checks 25 coefficient scales, 82,082 expanding composites, and
224 artificial cap steps. The separate checker uses 11,403 different
composites and 162 independently generated cap steps. All exact checks pass.

## Candidate counterexamples

None. No `K-####` identifier is created.

The height theorem makes a cap chain a highly constrained candidate residual
object, but it does not supply a finite positive marked Collatz initialization or
prove a chain exists.

## Failed approaches

- small-modulus patterns were not universal;
- finite full-stage samples cannot quantify the directive class;
- a short representative is not by itself impossible;
- the stage correction has no proved finite recurrence solely in the ordinary
  bulk `V_m`.

## Potential errors

1. `L-9703` depends on the corrected stage indexing, especially the exceptional
   last gap `t_257-t_255=3d`.
2. The local bound `-q_j<C_j<N_j` uses canonical connector digits and must not be
   generalized to arbitrary affine offsets.
3. `T-9704` is conditional on a cap chain; it is not a proof of nonexistence.
4. The asymptotic ratio concerns residual correction height, not a marked
   physical Collatz integer.
5. A p-adic lower-bound theorem still needs exact algebraicity, height, and
   nonvanishing hypotheses.

## Files changed

- `research/residue-cylinder-dichotomy/claims/L-9703-normalized-stage-offset.md`
- `research/residue-cylinder-dichotomy/claims/T-9704-cap-chain-height-collapse.md`
- `research/residue-cylinder-dichotomy/claims/Q-9702-cap-correction-chain.md`
- `experiments/X-9703-cap-chain-height/`
- packet README and claim inventory
- this append-only report

## Claims affected

- new: `L-9703`, `T-9704`, `X-9703`;
- sharpened: `Q-9702` now carries an explicit factor-greater-than-275 height gap;
- cross-links only: PR #3 `T-0027`, `T-0030`; PR #13 `LIT-KTHM-0030`;
  PR #32/PR #16 completion-height work.

## Recommended next actions

1. Independently reconstruct the suffix-product bound in `L-9703`.
2. For each fixed normalized stage word, derive the exact finite p-adic
   exponential/logarithmic expression selected by its correction cylinder.
3. Use `T-9704` to supply the ordinary-height side of a p-adic linear-form or
   product-formula contradiction, checking source-theorem thresholds exactly.
4. Make the bound uniform over the finite stage-word alphabet.
5. In parallel, test the affine ansatz `R_m=alpha_mV_m+beta_m` as a possible
   positive mechanism, without issuing a candidate before finite initialization
   and physical replay are complete.

## Organizational improvement ideas

Every completion packet should state the ratio

```text
ordinary representative bit length / complete cylinder bit length
```

with an exact coefficient, not only say that the representative is “small.” The
ratio `161341/44508739` makes the remaining theorem interface far clearer and
allows literature tools to be audited against a concrete approximation budget.
