# L-6604 — explicit Rhin swap floor for every acyclic first-crossing failure

**Claim ID:** `L-6604`  
**Status:** **PROPOSED / SOURCE-DEPENDENT**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** `T-6604`, `T-6606`; Rhin's linear-form lower bound in the normalization quoted by Rozier--Terracol  
**Scope:** every acyclic canonical first-crossing target failure  

## 1. Imported logarithmic-form bound

Rozier--Terracol quote the following theorem of Rhin. For integers `u_0,u_1,u_2`, if

\[
H=\max\{|u_1|,|u_2|\}\ge2,
\]

then the nonzero form

\[
\Lambda=u_0+u_1\log2+u_2\log3
\]

satisfies

\[
\boxed{|\Lambda|\ge H^{-13.3}.}
\tag{1}
\]

For a first crossing,

\[
\lambda=j\log2-q\log3>0,
\qquad0<q<j,
\]

so `(1)` gives

\[
\boxed{\lambda\ge j^{-13.3}.}
\tag{2}
\]

The primary Rhin source and the exact quoted normalization must be independently audited before status promotion.

## 2. Explicit repeated-factor inequality

Let `v` be an acyclic canonical first-crossing target failure of length `j`, and let

\[
I=\mathcal I(v)
\]

be its mechanical swap distance.

`T-6605` gives the bank bound

\[
B(v)<I+1.
\tag{3}
\]

`T-6606` forces a repeated factor of length

\[
L_*=\left\lfloor{j-2\over2(I+1)}\right\rfloor.
\tag{4}
\]

`T-6604` and `(2)--(3)` imply

\[
2^{L_*}+1
<
3^{I+1}\left(j^{14.3}+{j\over2}\right).
\]

Since `j>=2`,

\[
j^{14.3}+{j\over2}
\le{3\over2}j^{14.3}.
\]

Therefore

\[
\boxed{
L_*
<
(I+1)\log_2 3
+14.3\log_2 j
+\log_2(3/2).}
\tag{5}
\]

## 3. Closed swap floor

Put

\[
c=\log_2 3
\]

and

\[
A_j=14.3\log_2j+1+\log_2(3/2).
\tag{6}
\]

Because

\[
L_*
\ge
{j-2\over2(I+1)}-1,
\]

inequality `(5)` gives, with `z=I+1`,

\[
{j-2\over2z}<cz+A_j.
\]

Equivalently,

\[
2cz^2+2A_jz-(j-2)>0.
\]

The positive root is

\[
R_j=
{-A_j+\sqrt{A_j^2+2c(j-2)}\over2c}.
\tag{7}
\]

Since `z` is a positive integer and `z>R_j`,

\[
\boxed{
I
\ge
\max\left\{
0,
\left\lfloor
{-A_j+\sqrt{A_j^2+2(\log_2 3)(j-2)}
 \over2\log_2 3}
\right\rfloor
\right\}.}
\tag{8}
\]

This is an explicit all-length lower bound on the integrated displacement of every acyclic canonical first-crossing failure.

## 4. Asymptotic form

Because `A_j=O(log j)`, equation `(7)` gives

\[
R_j
=
\sqrt{{j\over2\log_2 3}}
-O(\log j).
\]

Since

\[
{1\over\log_2 3}
={\log2\over\log3}=\alpha,
\]

we obtain

\[
\boxed{
I
\ge
\sqrt{\alpha j\over2}
-O(\log j).}
\tag{9}
\]

This recovers `T-6610` with an explicit effective error term.

## 5. Current Farey-gate scale

For orientation, at the proposed delayed-crossing floor

\[
j=217\,976\,794\,617,
\]

formula `(8)` places the required swap budget on the order of

```text
2.62 * 10^5
```

units. This decimal is scheduling information only; a project certificate should evaluate `(8)` with directed logarithm intervals before registering an exact integer floor.

## 6. Consequence for candidate architectures

The following certificate formats are now uniformly excluded for Box 2:

```text
fixed finite number of edits of the mechanical word;
polylogarithmically many edits;
j^theta edits for every fixed theta<1/2;
finite-state or substitutional repairs whose total mechanical displacement is o(sqrt j).
```

A surviving acyclic target failure must carry genuinely growing support of at least square-root scale.

## 7. Gap audit

- The lower bound is on integrated right-shift distance, not directly on Hamming distance.
- Square-root and larger displacement families remain open.
- The primary Rhin theorem normalization is imported through Rozier--Terracol and requires independent source inspection.
- No CST or Collatz proof is claimed.
