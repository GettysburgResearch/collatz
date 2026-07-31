# Session report — universal shifted equation and polynomial sparsity

**Agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Date:** 2026-07-31  
**Issue:** #75  
**Draft PR:** #83  
**Branch:** `agent/gpt56-positive-tangent-01/75-coefficient-envelope`

## Request

Extend the shifted full-denominator equation to arbitrary high-bank, positive-entropy, genuinely nonperiodic first-crossing words.

## Audit finding

The earlier draft of `L-6909` used `n` as both the start and the endpoint. Direct algebra shows:

\[
A_w=x(2^j-3^q)+d2^j
\]

for the start `x`, while

\[
A_w=y(2^j-3^q)+d3^q
\]

for the endpoint `y=x+d`.

The requested `d3^q` equation is therefore correct with endpoint notation. `R-6910` records the correction and `L-6909` has been replaced by the strengthened theorem.

## Universal theorem

For every first-crossing word and every positive non-descending realization,

\[
A_w=xD+d2^j=yD+d3^q,
\qquad
D=2^j-3^q,
\qquad
y=x+d.
\]

Conversely, every integer displacement satisfying

\[
0\le d<\frac{A_w}{2^j},
\qquad
D\mid A_w-d3^q
\]

produces one positive ordinary realization following the exact word.

No bank, entropy, periodicity, pulse, or lateness assumption is used.

The first-crossing harmonic identity

\[
\frac{A_w}{3^q}
=\frac13\sum_{i:v_i=1}3^{-D_i}
\]

sharpens the displacement range to

\[
0\le d<\frac q3<\frac j3.
\]

## Entropy advance

Let `E_j` be all length-`j` first-crossing words possessing a positive non-descending realization. Every such word has a witness

\[
x<\frac{j}{3(1-e^{-\lambda_j})}
\le\frac{2j}{3\lambda_j},
\qquad
\lambda_j=j\log2-q\log3.
\]

One integer has one parity prefix, so the witness map is injective and

\[
|E_j|<\frac{2j}{3\lambda_j}.
\]

Under an effective Baker/Matveev lower bound `lambda_j>=c_0 j^(-mu)`,

\[
|E_j|=O(j^{\mu+1}).
\]

Thus the complete exceptional language has zero exponential family growth and every member is describable by `O(log j)` bits through its polynomial-sized ordinary witness.

This closes positive family entropy at arbitrary bank. It does not yet prove low internal subword complexity for every individual exceptional word.

## Files changed

```text
L-6909  corrected and strengthened universal classification
R-6910  explicit start/endpoint correction
T-6911  exact count and polynomial sparsity theorem
README   updated claim map and current frontier
LATEST   updated global reduction
```

## Honest frontier

The remaining possibility is not an arbitrary positive-entropy cloud. It is a polynomially sparse sequence of high-bank, genuinely nonperiodic words which may still have rich internal factor structure and must solve the short residue equation

\[
A_w=n(2^j-3^q)+d3^q,
\qquad
0\le d<j/3,
\]

with `n` the endpoint.

A residue-avoidance theorem or growing-support full-denominator theorem is still required. No proof of Collatz is claimed.