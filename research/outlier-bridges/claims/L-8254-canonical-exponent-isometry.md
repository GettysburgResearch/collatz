# L-8254 — Canonical exponent isometry and arbitrary finite high-word compiler

**Claim ID:** `L-8254`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-outlier-01`  
**Reviewing agents:** none yet  
**Created:** 2026-07-23  
**Last updated:** 2026-07-23  
**Issue:** #52  
**Dependencies:** `L-8253`; elementary lifting-the-exponent identities  
**Scope:** canonical representatives of the high-branch cylinders  
**Related counterexample candidates:** none

## Statement

Let

\[
N=2^{36}9^9
\tag{1}
\]

and

\[
\boxed{
L=2^{33}3^{16}
=369\,768\,517\,790\,072\,832.}
\tag{2}
\]

Then

\[
9^L\equiv1\pmod {2^{36}},
\qquad
8^L\equiv1\pmod {9^9},
\tag{3}
\]

and

\[
\boxed{
\nu_2(9^L-1)=36.}
\tag{4}
\]

Fix an integer residue `r>=44`. Define `u_r` as the unique integer in

\[
0<u_r<N
\tag{5}
\]

satisfying

\[
\boxed{
\begin{aligned}
u_r&\equiv a8^{-r}\pmod {9^9},\\
u_r&\equiv b9^{-r}\pmod {2^{36}},
\end{aligned}}
\tag{6}
\]

where `a,b` are the constants of `L-8253`.

For every ordinary `k>=0`, put

\[
\boxed{s=r+Lk.}
\tag{7}
\]

Then the canonical nonnegative representative of the label-`s` branch is

\[
\boxed{
X_s=\frac{8^su_r-a}{9^9},}
\tag{8}
\]

with

\[
0\le X_s<2^{3s+36}.
\tag{9}
\]

Its reset coordinate is

\[
Y_s=a+9^9X_s=8^su_r,
\tag{10}
\]

and its exact first output is

\[
\boxed{
H_r(k)
=
\frac{9^{r+Lk+9}u_r+1}{2^{36}}.}
\tag{11}
\]

For all distinct nonnegative integers `k,l`,

\[
\boxed{
\nu_2\bigl(H_r(k)-H_r(l)\bigr)
=
\nu_2(k-l).}
\tag{12}
\]

Consequently `H_r` extends uniquely to an isometry of `Z_2`. For every `h>=1`, it induces a permutation

\[
\boxed{
\mathbf Z/2^h\mathbf Z
\longrightarrow
\mathbf Z/2^h\mathbf Z.}
\tag{13}
\]

In particular, let

\[
\tau=(t_1,\ldots,t_n),
\qquad t_j\ge44,
\tag{14}
\]

be any finite desired future high-run word. That word determines one exact output cylinder

\[
Y_1\equiv R_\tau\pmod {2^{h_\tau}},
\tag{15}
\]

where

\[
\boxed{
h_\tau=\sum_{j=1}^{n}(3t_j+36).}
\tag{16}
\]

There is a unique

\[
\boxed{k_\tau\pmod {2^{h_\tau}}}
\tag{17}
\]

such that the canonical label

\[
s=r+Lk_\tau
\tag{18}
\]

has an ordinary canonical state `X_s` whose deterministic orbit begins

\[
\boxed{(s,t_1,\ldots,t_n).}
\tag{19}
\]

Therefore every finite high-run word has an exact ordinary realization whose initial top lift is canonical.

For an infinite future word, the compatible residues `(17)` determine one

\[
K_\infty\in\mathbf Z_2.
\tag{20}
\]

This compiler produces an ordinary finite initial exponent exactly when the nested binary expansion of `K_infinity` is eventually zero, so that `K_infinity` is a nonnegative ordinary integer. Finite surjectivity does not imply that condition.

## Motivation

Every finite branch word was already known to define a compatible `2`-adic cylinder. The new point is that all future finite information can be compiled into **one ordinary exponent parameter** while keeping the initial state at the canonical representative of its first branch.

The progression length `L` freezes both finite-place addresses:

```text
s mod ord_(2^36)(9),
s mod ord_(9^9)(8).
```

Varying the quotient `k` then changes the output by an exact `2`-adic isometry. No finite output cylinder is missed.

This makes the ordinary boundary completely explicit:

```text
finite future word
  -> one residue of k modulo a power of two;

infinite future word
  -> one K_infinity in Z_2;

ordinary witness
  -> K_infinity has finite binary support.
```

The last arrow is the only unresolved one.

## Proof

### 1. Exact orders

For `j>=0`, LTE gives

\[
\nu_2(9^{2^j}-1)=j+3.
\tag{21}
\]

Hence the multiplicative order of `9` modulo `2^36` is `2^33`.

Similarly,

\[
\nu_3(8^{2\cdot3^j}-1)
=
\nu_3(8^2-1)+j
=2+j.
\tag{22}
\]

Since `9^9=3^18`, the order of `8` modulo `9^9` is `2*3^16`.

Their least common multiple is `(2)`, proving `(3)`. Since `v2(L)=33`, LTE gives

\[
\nu_2(9^L-1)
=
\nu_2(9-1)+\nu_2(9+1)+\nu_2(L)-1
=3+1+33-1
=36,
\]

proving `(4)`.

### 2. The canonical unit is constant on the progression

For a label `s`, the reset normal form of `L-8253` requires

\[
Y_s=8^su_s\equiv a\pmod {9^9},
\tag{23}
\]

and

\[
9^{s+9}u_s\equiv-1\pmod {2^{36}}.
\tag{24}
\]

Identity `2^36 a-9^9 b=1` turns `(24)` into

\[
u_s\equiv b9^{-s}\pmod {2^{36}}.
\tag{25}
\]

The two moduli in `(6)` are coprime, so `u_r` exists uniquely modulo `N`. Equations `(3)` imply that the same `u_r` satisfies `(23)--(25)` for every `s=r+Lk`.

For `s>=44`, equation `(8)` is positive and integral. Moreover

\[
8^su_r
<
8^s2^{36}9^9,
\]

so `(9)` holds. Hence `X_s` is precisely the least nonnegative branch representative.

Formula `(11)` now follows from `L-8253` equation

\[
Y'=(9^{s+9}u_s+1)/2^{36}.
\]

### 3. Isometry

Assume `k>l`. From `(11)`,

\[
H_r(k)-H_r(l)
=
9^{r+Ll+9}u_r
\frac{9^{L(k-l)}-1}{2^{36}}.
\tag{26}
\]

The prefactor is odd. Put `d=k-l`. Because `9^L congruent 1 mod8`, LTE and `(4)` give

\[
\nu_2(9^{Ld}-1)
=36+\nu_2(d).
\tag{27}
\]

Taking valuations in `(26)` proves `(12)`.

An isometry on the nonnegative integers is uniformly continuous and has dense domain in `Z_2`, so it extends uniquely to `Z_2`. Equality `(12)` shows that two inputs are congruent modulo `2^h` exactly when their outputs are. Thus the induced map modulo `2^h` is injective, hence bijective on the finite ring, proving `(13)`.

### 4. Finite high-word cylinders

For one branch `t`, `L-8253` writes

\[
Y=2^{3t}u,
\qquad
u_2(Y)=3t,
\qquad
u\equiv-9^{-(t+9)}\pmod {2^{36}}.
\]

Thus the domain is one residue modulo `2^(3t+36)`. Parameterizing its free lift and using the odd multiplier in the output shows that the preimage of one residue modulo `2^h` at the next state is one residue modulo `2^(3t+36+h)` at the current state.

Induction over `(14)` proves `(15)--(16)`. The output of `(11)` automatically lies in `Y=a mod9^9`, so no additional odd condition remains. Permutation `(13)` gives the unique residue `(17)`, proving `(18)--(19)`.

The residues for successive prefixes are nested. Their inverse limit is `(20)`. The initial label `s=r+LK_infinity` is an ordinary nonnegative integer precisely when the binary expansion of `K_infinity` terminates. This is not implied by the existence of all finite residues.

## Dependency audit

1. `L-8253` supplies the reset normal form and canonical branch semantics.
2. LTE supplies `(21)--(22)` and `(27)`.
3. The finite-word cylinder induction is elementary odd-affine arithmetic.
4. No external literature theorem is used.

## Gap audit

This result does **not** construct an infinite ordinary path.

Specifically:

- the isometry proves finite surjectivity, not eventual-zero support;
- `K_infinity` may be a genuinely nonordinary `2`-adic integer;
- prescribing an affine or periodic future word remains a completion ghost;
- no growth conclusion applies without an ordinary finite exponent;
- no `K-####` object is proposed.

## Adversarial tests

`X-8252` checks:

- the two exact multiplicative orders;
- `v2(9^L-1)=36` modulo sufficiently deep powers of two;
- isometry `(12)` on several base residues and finite quotient grids;
- permutation `(13)` through the declared finite moduli;
- finite-word compilation and direct replay for a deterministic corpus.

## Suggested next attack

Treat the nested `k` residues as the output of a binary encoder. The desired event

```text
infinite high word -> finite-support K_infinity
```

is exactly a catastrophic-compression event. Apply the convolutional-code bridge from the original outlier audit to finite-memory approximations of this compiler, while preserving the nonlinear exponent feedback.
