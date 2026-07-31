# T-6911 — non-descending first crossings are polynomially sparse

**Claim ID:** `T-6911`  
**Status:** **PROPOSED**; the polynomial corollary is **SOURCE-DEPENDENT** on an effective lower bound for `j log 2-q log 3`  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Dependencies:** corrected `L-6909`; elementary affine algebra; an effective Baker/Matveev lower bound only in Sections 4--5  
**Scope:** every first-coefficient-crossing word having at least one positive non-descending ordinary realization; the coefficient bank and internal factor complexity are unrestricted

## 1. Exceptional language

For every `j>=1`, let `E_j` be the set of length-`j` shortcut-parity words `w` such that:

1. `w` is a first coefficient crossing;
2. some positive ordinary integer `x` follows `w`; and
3. `T_w(x)>=x`.

No restriction is imposed on bank size, factor complexity, pulse support, or periodicity.

## 2. Exact ordinary-height bound

Write

\[
T_w(x)=Cx+R,
\qquad
C=\frac{3^q}{2^j}=e^{-\lambda},
\qquad
\lambda=j\log2-q\log3>0.
\]

Corrected `L-6909` gives

\[
R
=
\frac{C}{3}
\sum_{i:v_i=1}3^{-D_i},
\qquad
D_i=q_i-\frac{\log2}{\log3}i.
\tag{1}
\]

First crossing gives `D_i>=0` for every `i<j`, so

\[
\boxed{0<=R<q/3<j/3.}
\tag{2}
\]

If `T_w(x)>=x`, then

\[
x(1-C)<=R,
\]

and therefore

\[
\boxed{
x<\frac{j}{3(1-e^{-\lambda})}.}
\tag{3}
\]

At a first crossing the final step is even and the previous coefficient is at least one, hence

\[
0<\lambda<=\log2.
\]

Using `1-e^(-lambda)>=lambda/2` on this interval,

\[
\boxed{x<\frac{2j}{3\lambda}.}
\tag{4}
\]

This bound is source-free and independent of the maximum bank.

## 3. Exact cardinality bound

For each `w in E_j`, choose its least positive non-descending realization `x_w`.

Different parity words have different `x_w`, because one ordinary start has one actual length-`j` parity prefix. Thus `w -> x_w` is injective and

\[
\boxed{
|E_j|
<
\frac{j}{3(1-e^{-\lambda_j})}
<=
\frac{2j}{3\lambda_j}.}
\tag{5}
\]

Here `lambda_j` is the unique positive logarithmic gap associated with the valid first-crossing weight at length `j`; if no such weight exists, `E_j` is empty.

Equation `(5)` is an exact reduction from an exponentially large ballot-word set to one Diophantine gap.

## 4. Polynomial sparsity

A reviewed effective Baker/Matveev theorem for the multiplicatively independent algebraic numbers `2` and `3` supplies constants

\[
c_0>0,
\qquad
\mu>0
\]

such that

\[
\boxed{
\lambda_j=j\log2-q\log3>=c_0j^{-\mu}.}
\tag{6}
\]

Combining `(5)` and `(6)`,

\[
\boxed{
|E_j|
<=
\frac{2}{3c_0}j^{\mu+1}.}
\tag{7}
\]

Therefore the complete exceptional language has zero exponential growth:

\[
\boxed{
\limsup_{j\to\infty}
\frac1j\log_2(1+|E_j|)=0.}
\tag{8}
\]

This holds with no coefficient-bank restriction. Allowing a linear or larger bank does not restore exponentially many non-descending first-crossing words.

## 5. Logarithmic description length

Given `(j,x_w)`, the word `w` is reconstructed by running the shortcut map from `x_w` for `j` steps and recording the parities.

Equation `(4)` and `(6)` give

\[
x_w=O(j^{\mu+1}).
\]

Hence every exceptional word has a description using only `O(log j)` bits for `j` and `x_w`.

Equivalently, for any fixed effective coding scheme,

\[
\boxed{\operatorname{description\_length}(w)=O(\log j).}
\tag{9}
\]

Thus no cofinal family of non-descending first-crossing words can require a positive fraction of its word length merely to identify its members.

## 6. Universal shifted-denominator form

Corrected `L-6909` applies to every member, regardless of bank or internal complexity. If

\[
y=T_w(x)=x+d,
\]

then

\[
\boxed{
A_w
=y(2^j-3^q)+d3^q,
\qquad
0<=d<q/3<j/3,}
\tag{10}
\]

and the start is `x=y-d`.

If `n` denotes the start instead, the correct form is

\[
\boxed{
A_w
=n(2^j-3^q)+d2^j,
\qquad
T_w(n)=n+d.}
\tag{11}
\]

The endpoint-labelled form `(10)` is exactly the equation requested for arbitrary high-bank and nonperiodic first-crossing words.

## 7. Interpretation of entropy

Equation `(8)` closes positive **family entropy**: there cannot be exponentially many exceptional words at length `j`.

It does not by itself bound the internal subword complexity of one exceptional word. A short deterministic description can still produce a finite word with many distinct factors.

Therefore the remaining possibility is a polynomially sparse family of highly structured words which may still have large internal factor complexity.

## 8. Consequence for the frontier

Any unbounded family of delayed first-crossing failures must now be simultaneously:

```text
polynomially sparse across words of the same length;
describable from one polynomial-sized ordinary start;
subject to a displacement d<j/3;
nonperiodic unless it is a positive cycle;
and high-bank whenever the separate return theorems rule out its internal complexity class.
```

The remaining problem is not a positive-entropy cloud of arbitrary words. It is a thin exceptional sequence requiring a residue-avoidance or return theorem.

## 9. Gap audit

- The exact cardinality bound `(5)` is source-free; polynomial sparsity uses `(6)`.
- Zero family entropy does not imply low internal factor complexity for each member.
- Aperiodic zero-entropy exceptional sequences are not excluded here.
- The theorem proves sparsity, not emptiness.
- No proof of Collatz is claimed.