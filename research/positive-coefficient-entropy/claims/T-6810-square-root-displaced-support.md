# T-6810 — Every surviving acyclic first-crossing failure has square-root displaced support

**Claim ID:** `T-6810`  
**Status:** **PROPOSED / SOURCE-DEPENDENT**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6808`, `L-6811`; the exact long-return barrier from the coefficient-tangent packet; Rhin's logarithmic-form bound in the normalization quoted by Rozier--Terracol  
**Scope:** unbounded families of acyclic canonical coefficient-first-crossing failures

## 1. Statement

Put

\[
\alpha={\log2\over\log3}.
\]

Let `v_j` be an unbounded family of coefficient-first-crossing words of
length `j`, and let `w_j` be the corresponding upper-mechanical extremizer.
For each word, let

\[
R_j
=
\#\{i:d_i(v_j)<d_i(w_j)\}
\]

be the number of displaced odd positions.

Assume that:

1. the canonical ordinary source of `v_j` does not descend at the crossing;
2. the represented finite segment contains no repeated physical state.

Then

\[
\boxed{
\liminf_{j\to\infty}
{R_j\over\sqrt j}
\ge
\sqrt{\alpha\over2}
=
0.5615\ldots.}
\tag{1}
\]

In particular, every cofinal acyclic target-failure family with

\[
R_j=o(\sqrt j)
\]

is impossible.

This strictly strengthens the cube-root support floor in `T-6808`.

## 2. Bank is bounded by support

Let

\[
e_m=S_m(v)-S_m(w)\ge0
\]

be the integer prefix-excess path and put

\[
H=\max_{m<j}e_m,
\qquad
B=\max_{m<j}(S_m(v)-\alpha m).
\]

`L-6808` proves

\[
B<H+1
\tag{2}
\]

and

\[
H\le R.
\tag{3}
\]

Therefore

\[
\boxed{B<R+1.}
\tag{4}
\]

This is the load-bearing improvement over the earlier estimate `B<I+1`.

## 3. Support forces a long repeated factor

Put

\[
L_R=
\left\lfloor{j-2\over2(R+1)}\right\rfloor.
\tag{5}
\]

`L-6811` proves that, whenever `L_R>=1`, the proper prefix contains a
repeated factor of length `L_R`.

By the acyclicity assumption, the corresponding physical source states are
distinct.  The exact return/gap theorem therefore gives

\[
\boxed{
2^{L_R}+1
<
3^B
\left({j\over\lambda_j}+{j\over2}\right),}
\tag{6}
\]

where

\[
\lambda_j=j\log2-q\log3>0.
\]

Equation `(6)` is elementary once the repeated physical factor is supplied.

## 4. Source-qualified logarithmic form

The quoted specialization of Rhin's theorem gives

\[
\boxed{
\lambda_j\ge j^{-13.3}.}
\tag{7}
\]

The exact primary-source normalization remains an explicit review
obligation.

For `j>=2`, equations `(4)`, `(6)`, and `(7)` imply

\[
2^{L_R}+1
<
{3\over2}
3^{R+1}j^{14.3}.
\tag{8}
\]

Hence, writing

\[
c=\log_2 3,
\qquad
A_j=14.3\log_2j+1+\log_2(3/2),
\tag{9}
\]

we obtain

\[
L_R<c(R+1)+14.3\log_2j+\log_2(3/2).
\tag{10}
\]

## 5. Exact square-root floor

Set

\[
z=R+1.
\]

The floor in `(5)` gives

\[
L_R\ge{j-2\over2z}-1.
\tag{11}
\]

Combining `(10)--(11)`,

\[
{j-2\over2z}<cz+A_j.
\]

Equivalently,

\[
\boxed{
2cz^2+2A_jz-(j-2)>0.}
\tag{12}
\]

The positive root is

\[
\rho_j
=
{-A_j+\sqrt{A_j^2+2c(j-2)}\over2c}.
\tag{13}
\]

Since `z` is an integer and `z>rho_j`,

\[
\boxed{
R
\ge
\max\left\{
0,
\left\lfloor
{-A_j+\sqrt{A_j^2+2(\log_2 3)(j-2)}
 \over2\log_2 3}
\right\rfloor
\right\}.}
\tag{14}
\]

This is an explicit all-length source-qualified support floor.

## 6. Asymptotic extraction

Because `A_j=O(log j)`, equation `(13)` gives

\[
\rho_j
=
\sqrt{j\over2\log_2 3}
-O(\log j).
\]

Since

\[
{1\over\log_2 3}
={\log2\over\log3}
=\alpha,
\]

we obtain `(1)`.

## 7. Source-free candidate form

For one concrete candidate family, no generic logarithmic-form theorem is
needed.  If an exact directed bound

\[
\lambda_j\ge\lambda_0(j)>0
\]

is available, every acyclic target failure must satisfy

\[
\boxed{
2^{\lfloor(j-2)/(2(R+1))\rfloor}+1
<
3^{R+1}
\left({j\over\lambda_0(j)}+{j\over2}\right).}
\tag{15}
\]

The reverse inequality is a complete finite contradiction for that family.

## 8. Strategic meaning

The earlier geometry required only cube-root-growing support because it first
passed through total swap area.  `L-6811` counts edited binary positions
directly and closes that loss.

A surviving acyclic Box-2 obstruction is now forced to have

```text
at least sqrt(alpha*j/2)-O(log j) distinct displaced odd positions;
```

not merely a large total displacement concentrated on a few positions.

Together with `T-6809`, those positions begin after an initial mechanical
agreement of only logarithmic length.  Together with `L-6810`, the resulting
near-return also separates from its old parity tail within logarithmic depth.

## 9. Gap audit

- Square-root and larger support remains possible.
- The theorem says nothing about the modular distribution of the displacement
  numerator across the complete denominator.
- A repeated physical state is the positive-cycle alternative and is not
  silently discarded.
- The exponent `13.3` and its normalization are source-dependent.
- No universal CST, Box-2, Box-1, or Collatz proof is claimed.
