# L-0035 — Linear-grid block cylinders and quotient overlap

Claim ID: `L-0035`  
Title: Every finite linear-height tower word has one canonical ordinary cylinder and an exact overlapping quotient map  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-23  
Dependencies: `L-0031`  
Scope: stabilized phase-`-34` tower types on height grids with spacing `16`  
Related counterexample candidates: none

## 1. Local tower data

For a height `t` divisible by `16`, put

\[
N_t=3^{7(t+1)},
\qquad
T_t=2^{11(t+1)}.
\]

Use the stabilized type data

\[
p=(5,30,20,56),
\qquad
b=(9,54,36,24).
\]

The scaled-tail recurrence of `L-0031` is

\[
\boxed{T_{t'}W'=N_tW+b_i,}
\tag{1}
\]

when the current type is `i`, the next tower begins at height `t'`, and the two scaled tails satisfy

\[
W\equiv p_i\pmod {64},
\qquad
W'\equiv p_j\pmod {64}.
\]

## 2. One-transition canonical cylinder

Take `t'=t+16`. For ordered types `(i,j)`, define

\[
\boxed{
R_t(i,j)=
\left[
\bigl(T_{t+16}p_j-b_i\bigr)N_t^{-1}
\right]_{64T_{t+16}},}
\tag{2}
\]

and

\[
\boxed{
S_t(i,j)=
\frac{N_tR_t(i,j)+b_i}{T_{t+16}}.}
\tag{3}
\]

Then

\[
R_t(i,j)\equiv p_i\pmod {64},
\qquad
S_t(i,j)\equiv p_j\pmod {64},
\tag{4}
\]

and every ordinary integer in this exact edge cylinder has the unique form

\[
\boxed{
W=R_t(i,j)+64T_{t+16}Y,
\qquad Y\ge0.}
\tag{5}
\]

Its output is

\[
\boxed{
W'=S_t(i,j)+64N_tY.}
\tag{6}
\]

### Proof

The target congruence in (1) is

\[
N_tW+b_i\equiv T_{t+16}p_j
\pmod {64T_{t+16}}.
\]

Since `N_t` is odd, it has exactly one solution modulo the displayed power of two, namely (2). The relation

\[
N_tp_i+b_i\equiv0\pmod {64}
\]

from the stabilized tower anchors gives the first congruence in (4); the defining modulus in (2) gives the second. Substituting (5) into (1) gives (6). ∎

## 3. Exact overlap of two transitions

Consider

```text
(i,t) -> (j,t+16) -> (k,t+32).
```

Define

\[
\boxed{
C_t(i,j,k)=
\frac{S_t(i,j)-R_{t+16}(j,k)}{64}.}
\tag{7}
\]

This is an integer by (4). The output (6) belongs to the second cylinder exactly when

\[
\boxed{
N_tY+C_t(i,j,k)=T_{t+32}Y'.}
\tag{8}
\]

Put

\[
\boxed{
y_t(i,j,k)=
[-C_t(i,j,k)N_t^{-1}]_{T_{t+32}},}
\tag{9}
\]

\[
\boxed{
c_t(i,j,k)=
\frac{N_ty_t(i,j,k)+C_t(i,j,k)}{T_{t+32}}.}
\tag{10}
\]

Then `c_t(i,j,k)` is a nonnegative integer, and all ordinary overlapping transitions are

\[
\boxed{
Y=y_t(i,j,k)+T_{t+32}h
\longmapsto
Y'=c_t(i,j,k)+N_th,
\qquad h\ge0.}
\tag{11}
\]

### Proof

Equation (8) is obtained by equating (6) with the input form (5) for the second edge and dividing by `64`. The odd coefficient `N_t` gives one residue (9), hence (10)--(11).

For nonnegativity, (3) gives `S_t(i,j)<64N_t+1`, while

\[
0\le R_{t+16}(j,k)<64T_{t+32}.
\]

Therefore

\[
-T_{t+32}<C_t(i,j,k)\le N_t.
\]

The numerator in (10) is a multiple of `T_(t+32)` and is strictly greater than `-T_(t+32)`, so it is nonnegative. ∎

## 4. Arbitrary finite block

Fix a block width `L>=1`, a base height `B` divisible by `16`, and types

\[
(i_0,i_1,\ldots,i_L)\in\{0,1,2,3\}^{L+1}.
\]

Put

\[
t_j=B+16j.
\]

Composing (1) gives

\[
\boxed{
2^{E_L(B)}W_L
=
3^{A_L(B)}W_0+\tau_{B,L}(i_0,\ldots,i_{L-1}),}
\tag{12}
\]

where the toll is positive and

\[
\boxed{
A_L(B)=7L(B+1)+56L(L-1),}
\tag{13}
\]

\[
\boxed{
E_L(B)=11L(B+1)+88L(L+1).}
\tag{14}
\]

Exactly as in Section 2, the terminal condition

\[
W_L\equiv p_{i_L}\pmod {64}
\]

selects one canonical input residue modulo

\[
64\,2^{E_L(B)}.
\]

Every finite block therefore has one exact ordinary input cylinder and transports its free high quotient by the odd multiplier `3^(A_L(B))`.

## Interpretation

The 256-transition corrected stage is only one member of a much simpler family. Every finite linear-height word has:

```text
finite tower word
+ one canonical low binary block
+ one arbitrary ordinary high quotient.
```

Two consecutive words overlap through the one-dimensional affine quotient map (11). The positive construction problem is therefore an integer-first invariant for this quotient map, not an inverse-limit choice of all future cylinders.

## Gap audit

- Equation (11) proves every finite overlap but does not select one ordinary `Y_0` satisfying infinitely many future residues.
- The exact future language can require unbounded integer state; a residue-only lasso is not a certificate.
- Strict quotient growth requires an additional multiplier-versus-next-radix inequality, supplied by `T-0040`.
- No positive Collatz counterexample is claimed.

## Adversarial tests

`X-0018` checks all sixteen one-transition cylinders, all sixty-four overlapping triples, every width-two type word, and a representative set of width-two overlaps using exact standard-library integers.