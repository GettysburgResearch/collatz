# R-6502 — Subspace/Ridout applicability boundary at the Lane-A cusp

**Claim ID:** `R-6502`  
**Title:** Standard product-formula, Ridout, and moving-target inputs do not close Lane A without a second independent form  
**Status:** `PROVED AS AN EXACT APPLICABILITY AUDIT`  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-08-01  
**Dependencies:** `L-6505`; source statements only for theorem positioning  
**Scope:** the currently proposed canonical source/end cusp attack  
**Related candidates:** none

## 1. Purpose

`R-6501` proves that scalar surplus, mean-bank, record, and low-band estimates can all hold on a compatible inverse-limit parity path. The present audit asks a different question:

> Does the additional fixed-integer equation
> \[
> A+n3^q=s2^k
> \]
> already cross a standard product-formula, Ridout, or moving-target Subspace-Theorem threshold?

The answer is no, for one exact reason: every available power saving is the valuation shadow of that same affine equation.

## 2. One-place Ridout route

The source congruence gives

\[
\left|n+\frac{A}{3^q}\right|_2
=2^{-k}|s|_2.
\tag{1}
\]

At a cusp,

\[
3^q=2^{k+o(k)},
\qquad
H\!\left(-\frac{A}{3^q}\right)=3^{q+o(q)}.
\]

Thus `(1)` has height exponent

\[
\left|n+\frac{A}{3^q}\right|_2
=H^{-1+o(1)}.
\tag{2}
\]

This is below the `2+epsilon` approximation exponent at which a Roth/Ridout finiteness theorem could be invoked. The fact that the target `n` is rational does not create a stronger contradiction; ordinary rational approximants can attain exponent one for elementary divisibility reasons.

## 3. Three-variable Subspace route

`L-6505` constructs three determinant-one systems of forms at `infinity,2,3` for

\[
X=(A,3^q,2^k)
\]

and proves the normalized estimate

\[
\prod_{v,i}
\frac{|L_{i,v}(X)|_v}{\|X\|_v}
\le H(X)^{-4+o(1)}.
\tag{3}
\]

For three variables this appears to cross the usual `H^{-3-epsilon}` threshold.

But the point satisfies identically

\[
X_0+nX_1-sX_2=0,
\tag{4}
\]

and the moving coefficient height obeys

\[
h(1,n,-s)=o(h(X)).
\tag{5}
\]

Therefore any moving-target conclusion of linear degeneracy is already exhausted by `(4)`. Invoking the theorem and then treating `(4)` as new information would be circular.

## 4. Quotient audit

After quotienting `(4)`, use

\[
Y=(3^q,2^k).
\]

The exact coordinate product is

\[
|Y_1Y_2|_\infty
|Y_1Y_2|_2
|Y_1Y_2|_3=1.
\tag{6}
\]

Normalizing by the projective height gives exactly

\[
H(Y)^{-2}.
\tag{7}
\]

There is no `H(Y)^{-2-epsilon}` gain. In projective dimension one, the quotient lands on the product-formula baseline rather than across a Diophantine-approximation threshold.

## 5. S-unit route

The normalized split

\[
U=\frac{A}{s2^k},
\qquad
V=\frac{n3^q}{s2^k},
\qquad
U+V=1
\tag{8}
\]

is a valid fixed equation. Evertse--Schlickewei--Schmidt applies only after the solutions lie in one finite-rank multiplicative group.

`T-6507` proves the contrapositive structural conclusion: an actual infinite cusp sequence must generate unbounded multiplicative rank. Hence a fixed-`S` application is a genuine class exclusion but not a universal Lane-A proof.

## 6. Exact single missing inequality

All standard routes would close Lane A if one additional form or rank bound were available.

### Product-formula version

Find a second quotient form, independent of the coordinates and of `(4)`, with coefficient height `o(k)` and a fixed `epsilon>0` such that along every cusp subsequence

\[
\boxed{
\prod_{v\in S}
\frac{|M_{1,v}(Y)M_{2,v}(Y)|_v}{\|Y\|_v^2}
\le H(Y)^{-2-\varepsilon}.}
\tag{9}
\]

### Multiplicative-rank version

Prove that simultaneous zero canonical source/end rates force

\[
\boxed{
\operatorname{rank}
\langle(U_1,V_1),\ldots,(U_J,V_J)\rangle
=o(\log J).}
\tag{10}
\]

This contradicts `T-6507`.

### Bilateral-capacity version

Prove the overload inequality `(16)` of `L-6506` for one subexponential capacity scale.

Any one of `(9)--(10)` or the capacity overload closes Lane A. None is currently supplied by a general black-box theorem.

## 7. Re-audit of `R-6501`

`R-6501` remains valid and load-bearing. The new product-formula work does not invalidate its countermodel because:

1. an abstract parity completion need not supply one fixed source `n`;
2. even when the fixed-source affine relation is imposed formally, its Subspace smallness is linearly degenerate;
3. finite compatibility does not control the multiplicative rank of the actual correction pairs;
4. the quotient still sits exactly at product-formula equality.

Therefore no contradiction may be inferred from scalar drift/density estimates plus the phrase “Subspace Theorem.”

## 8. Source boundary

- The fixed-target Subspace and Ridout thresholds are used only for applicability comparison.
- The Ru--Vojta moving-target framework requires a nondegeneracy/coherence audit; the exact relation `(4)` already violates the needed independence for a contradiction.
- The only imported theorem used positively in this wave is the fixed-equation finite-rank theorem in `T-6507`, with its normalization stated there.

## 9. Conclusion

The fixed ordinary integer is genuinely stronger than an inverse-limit path, but its first adelic manifestation supplies exactly one hyperplane and no more. The surviving problem is not to repeat that hyperplane at higher precision. It is to prove a second independent arithmetic restriction tied to the internal Collatz numerator or to the same orbit's bilateral canonical cuts.
