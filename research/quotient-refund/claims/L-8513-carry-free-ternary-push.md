# L-8513 — Every Hensel-quotient connector is a carry-free ternary block push

**Claim ID:** `L-8513`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-23  
**Dependencies:** `L-8512`  
**Scope:** every legal intrinsic Hensel-quotient transition

## Statement

Use the exact Hensel-quotient transition of `L-8512`:

\[
\boxed{
q=\varrho_j+H_t\ell
\quad\longmapsto\quad
q'=\tau_j+3^G\ell,}
\tag{1}
\]

where

\[
H_t=2^{11(t+33)},
\qquad
0\le\varrho_j<H_t,
\qquad
\ell\in\mathbf Z_{\ge0},
\tag{2}
\]

\[
G=7(t+1)+\gamma-\beta_i,
\qquad
A=3^G,
\tag{3}
\]

and

\[
\tau_j=
\frac{A\varrho_j+h-x_j}{H_t}.
\tag{4}
\]

Then:

### 1. Canonical output block

\[
\boxed{0\le\tau_j<A=3^G.}
\tag{5}
\]

Thus `tau_j` is one canonical block of exactly `G` ternary positions.

### 2. Exact ordinary high-tail preservation

Equation `(1)` is the mixed-radix replacement

\[
\boxed{
\varrho_j+H_t\ell
\longmapsto
\tau_j+3^G\ell,}
\tag{6}
\]

with the same finite ordinary high tail `ell` on both sides.

In least-significant-first base-three notation, the output quotient consists of the canonical `G`-trit block of `tau_j` followed by the ordinary ternary digits of `ell`. No carry propagates from `tau_j` into `ell`.

Equivalently,

\[
\boxed{
\tau_j=q'\bmod 3^G,
\qquad
\ell=\left\lfloor\frac{q'}{3^G}\right\rfloor.}
\tag{7}
\]

### 3. Exact inverse on the marked branch

For fixed finite state and target `j`, every output quotient in the image cylinder

\[
q'\equiv\tau_j\pmod {3^G}
\]

has the unique predecessor

\[
\boxed{
q=\varrho_j+H_t
\left\lfloor\frac{q'}{3^G}\right\rfloor.}
\tag{8}
\]

The source is a legal primitive core exactly when the recovered tail belongs to one of the two allowed residue classes modulo three from `L-8512`.

### 4. Finite-chain canonical tile

Fix any finite legal path of `r` intrinsic transitions. Repeatedly composing `(6)` gives one exact tile

\[
\boxed{
R_r+Q_r\ell
\longmapsto
S_r+P_r\ell,}
\tag{9}
\]

where

\[
Q_r=\prod_{n=0}^{r-1}H_{t_n},
\qquad
P_r=\prod_{n=0}^{r-1}3^{G_n},
\tag{10}
\]

and

\[
\boxed{0\le R_r<Q_r,
\qquad
0\le S_r<P_r.}
\tag{11}
\]

All intermediate divisibility and primitive gates are equivalent to membership in the marked finite path cylinder used to define `(9)`; the one ordinary high tail is preserved through the whole path.

## Proof

`L-8512` already proves `tau_j>=0`. Since

\[
0\le\varrho_j\le H_t-1,
\]

and

\[
0\le x_j<H_t,
\]

it remains to bound `h`. From

\[
h=\frac{Aa+1}{2^D}
\]

and

\[
0\le a\le2^D-1,
\]

one has

\[
h< A.
\]

Because `h` is an integer,

\[
0\le h\le A-1.
\]

Therefore

\[
A\varrho_j+h-x_j
\le
A(H_t-1)+(A-1)
=A H_t-1.
\]

After division by `H_t`,

\[
\tau_j<A.
\]

This proves `(5)`. Equations `(6)--(8)` are then ordinary Euclidean division in base `3^G`; the strict bound `(5)` rules out every carry into the high tail.

For the finite-chain statement, compose two canonical tiles

\[
R+Qx\mapsto S+Px,
\]

\[
R'+Q'y\mapsto S'+P'y.
\]

Compatibility of the marked path selects one unique residue

\[
x=x_0+Q'z
\]

because `P` is odd and hence invertible modulo the dyadic modulus `Q'`. Substitution gives a composite source modulus `QQ'` and output multiplier `PP'`. The new source block is the least representative modulo `QQ'`, so it lies in `[0,QQ')`. The output at zero high tail is an actual canonical finite-path output. Since each local output block lies below its local odd radix, induction—or the same elementary cap argument as in `L-9702`—gives `0<=S_new<PP'`. Iteration proves `(9)--(11)`. ∎

## Constructive meaning

The ordinary quotient is not merely “large enough to carry a stack.” It is already an exact mixed-radix stack object:

```text
pop:
  one complete dyadic cylinder block varrho_j mod H_t;

push:
  one canonical G-trit block tau_j;

preserve:
  the same finite ordinary high tail ell;

route:
  one fixed toll symbol b_j and one two-of-three primitive lift.
```

The positive problem is therefore a self-routing mixed-radix stack problem, not an inverse-limit interpretation problem. A successful certificate must prove that the pushed ternary blocks and preserved high tail later decode into the required affine dyadic toll blocks.

## Gap audit

- A carry-free push does not prove the pushed blocks later form legal dyadic input blocks.
- The bases `H_t` and `3^G` change with the height and finite state.
- The finite-chain tile depends on the marked path; it does not choose an infinite path from one ordinary seed.
- High-tail preservation does not imply the least initial representatives stabilize.
- No self-replicating stack word or counterexample integer is supplied.