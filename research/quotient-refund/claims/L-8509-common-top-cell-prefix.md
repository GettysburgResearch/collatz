# L-8509 — The four continuation residues share all but six top-boundary bits

**Claim ID:** `L-8509`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-23  
**Dependencies:** `L-8506`, `L-8507`  
**Scope:** every current intrinsic core block and its four complete continuations

## Statement

Retain the notation of `L-8507` for one current block `(j,nu)`:

\[
C=\widehat R_{j,\nu}+3\,2^{D+6}m,
\]

\[
C'=\widehat S_{j,\nu}+g_jA\,m,
\qquad
g_j=3\,2^{6-j},
\qquad
A=3^G.
\]

The complete continuation residues are

\[
m\equiv\rho_k\pmod {H_t},
\qquad
k\in\{0,1,2,3\},
\]

with

\[
H_t=2^{11(t+33)}.
\]

Put

\[
\boxed{
B_t=H_t/64=2^{11(t+33)-6}.
}
\tag{1}
\]

Then:

### 1. One common long residue

There is a unique

\[
\boxed{0\le\lambda<B_t}
\]

such that

\[
\boxed{
\rho_k\equiv\lambda\pmod {B_t}
}
\tag{2}
\]

for all four target types.

Write

\[
\boxed{
\rho_k=\lambda+B_td_k,
\qquad
0\le d_k<64.
}
\tag{3}
\]

The four six-bit cells `d_k` are distinct.

Consequently the complete next-stage test is exactly

```text
long forced block:
  m == lambda mod 2^(11(t+33)-6);

six-bit physical cell:
  ((m-lambda)/B_t) mod64 in {d_0,d_1,d_2,d_3}.
```

### 2. Exact top-cell quotient

For a legal `m`, define

\[
\boxed{
z=\frac{m-\lambda}{B_t}.}
\tag{4}
\]

Then

\[
z=d_k+64\ell
\]

for the unique next type `k`, where `ell` is the free lift of `L-8507`.

### 3. One branch-independent affine identity

At the next finite state, write its high inverse as `a'`, its high binary exponent as

\[
D'=11(t+33)-j,
\]

and its unique complete primitive source block for target `k` as

\[
\widehat R'_k=a'+2^{D'}q'_k,
\qquad
0\le q'_k<192.
\tag{5}
\]

The forced ternary lifts make all four `q'_k` congruent modulo three.

There is one integer

\[
\boxed{
K=
\frac{
\widehat S_{j,\nu}+g_jA\lambda-a'
}{2^{D'}}
}
\tag{6}
\]

independent of `k`, and every continuation satisfies

\[
\boxed{
192\sigma_k-3Ad_k+q'_k=K.
}
\tag{7}
\]

Equivalently, the current top-cell quotient and the next complete source cell obey

\[
\boxed{
192m'+q'_k=3Az+K,
}
\tag{8}
\]

where

\[
m'=\sigma_k+A\ell.
\]

Thus the four branch formulas are sections of one affine integer map. The target dependence is confined to one current six-bit cell `d_k` and one next cell `q'_k` in `{0,...,191}`.

## Proof

### Common prefix

At the next state, every complete source block has the form `(5)`. For two target types `k,l`,

\[
\widehat R'_k-\widehat R'_l
=2^{D'}(q'_k-q'_l).
\tag{9}
\]

Both blocks were chosen to have the same residue modulo three as the current output `widehat S_(j,nu)`. Since `a'` and `2^(D')` are fixed ternary units, this implies

\[
3\mid q'_k-q'_l.
\tag{10}
\]

In `L-8507`,

\[
\Delta_k=
\frac{\widehat R'_k-\widehat S_{j,\nu}}{g_j},
\qquad
g_j=3\,2^{6-j}.
\]

Equations `(9)--(10)` give

\[
\Delta_k-\Delta_l
\equiv0
\pmod {2^{D'-(6-j)}}.
\]

But

\[
D'-(6-j)=D'+j-6=11(t+33)-6,
\]

so the modulus is exactly `B_t`. Multiplication by the odd unit `A^(-1)` in the definition of `rho_k` preserves this congruence, proving `(2)`.

The representation `(3)` follows because `H_t=64B_t`. Distinctness of the `rho_k` from `L-8507` makes the four `d_k` distinct.

### Affine identity

Substitute

\[
\rho_k=\lambda+B_td_k,
\qquad
\widehat R'_k=a'+2^{D'}q'_k
\]

into the exact continuation equation

\[
\widehat S_{j,\nu}+g_jA\rho_k-\widehat R'_k
=g_jH_t\sigma_k.
\tag{11}
\]

The two exact products are

\[
g_jB_t=3\,2^{D'},
\]

\[
g_jH_t=3\,2^{D'+6}=192\,2^{D'}.
\]

After division by `2^(D')`, equation `(11)` becomes

\[
\frac{
\widehat S_{j,\nu}+g_jA\lambda-a'
}{2^{D'}}
+3Ad_k-q'_k
=192\sigma_k.
\]

This proves the integrality of `(6)` and identity `(7)`.

Finally, `z=d_k+64ell`, so

\[
\begin{aligned}
192m'+q'_k
&=192(\sigma_k+A\ell)+q'_k\\
&=K+3Ad_k+192A\ell\\
&=K+3Az.
\end{aligned}
\]

This proves `(8)`. ∎

## Constructive meaning

The remaining top-boundary problem is even smaller than four residues in a huge modulus.

```text
one forced low block of 11(t+33)-6 bits,
then one four-of-64 top-cell choice,
then one branch-independent affine transport.
```

This is the exact most-significant analogue of the source-cell/Hensel decompositions elsewhere in the repository. It identifies the object a causal compiler must generate: the common long residue `lambda`. The next type consumes only the six bits immediately above it.

## Gap audit

- A common low prefix does not prove that any finite ordinary quotient matches it forever.
- Four allowed top cells do not cover all 64 cells.
- The affine identity does not remove the next changing-modulus condition.
- No inverse-limit point is promoted to an ordinary integer.
