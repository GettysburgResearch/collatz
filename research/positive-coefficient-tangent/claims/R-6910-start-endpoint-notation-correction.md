# R-6910 — start/endpoint correction for the shifted denominator equation

**Claim ID:** `R-6910`  
**Status:** **PROVED / EDITORIAL-MATHEMATICAL CORRECTION**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Affected claim:** earlier draft of `L-6909`

## Finding

The earlier draft displayed

\[
A_w=n(2^j-3^q)+d3^q
\]

and then described `n` as the starting value satisfying

\[
T_w(n)=n+d.
\]

Those two uses are incompatible.

Let

\[
T_w(x)=\frac{3^q x+A_w}{2^j}=y,
\qquad
d=y-x,
\qquad
D=2^j-3^q.
\]

Then direct rearrangement gives the two correct identities

\[
\boxed{A_w=xD+d2^j}
\]

and

\[
\boxed{A_w=yD+d3^q.}
\]

Therefore:

- if `n` denotes the **start**, the coefficient of `d` is `2^j`;
- if `n` denotes the **endpoint**, the coefficient of `d` is `3^q`, and the start is `n-d`.

## Repository action

`L-6909` has been replaced by a universal corrected classification which:

1. distinguishes the start and endpoint explicitly;
2. removes the unnecessary lateness hypothesis;
3. proves the converse as well as the forward identity;
4. sharpens the displacement bound from `d<j/2` to
   \[
   d<q/3<j/3.
   \]

No downstream exclusion may use the old start-labelled `d3^q` formula.

## Scope

This correction does not invalidate the core shifted-denominator idea. It repairs the coordinate naming and strengthens the exact theorem.