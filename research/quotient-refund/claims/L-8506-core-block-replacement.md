# L-8506 — The intrinsic core decoder has eight exact ordinary blocks

**Claim ID:** `L-8506`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Dependencies:** `T-8507`  
**Scope:** one intrinsic core state at every multiple of `16` with `t>=3744`

## Setup

Fix the finite state `(t,gamma,i)` of `T-8507` and put

\[
G=7(t+1)+\gamma-\beta_i,
\qquad
D=11(t+17)-i,
\qquad
A=3^G.
\]

Let

\[
\boxed{
a=[-A^{-1}]_{2^D},}
\tag{1}
\]

\[
\boxed{
h=\frac{Aa+1}{2^D}.}
\tag{2}
\]

Thus every odd integer satisfying the high binary divisibility has the unique form

\[
C=a+2^Dq,
\qquad q\in\mathbf Z_{\ge0},
\tag{3}
\]

and

\[
\frac{AC+1}{2^D}=h+Aq.
\tag{4}
\]

The primitive-core state additionally requires `3` not to divide `C`.

## Four binary target blocks

For each target type `j in {0,1,2,3}`, define the unique six-bit quotient cell

\[
\boxed{
\kappa_{t;\gamma,i,j}
=
\left[
A^{-1}
\left(3^{-\beta_i}p_j-h\right)
\right]_{64}.}
\tag{5}
\]

Put

\[
\boxed{
R_{t;\gamma,i,j}
=a+2^D\kappa_{t;\gamma,i,j},}
\tag{6}
\]

\[
\boxed{
S_{t;\gamma,i,j}
=
\frac{h+A\kappa_{t;\gamma,i,j}}{2^j}.}
\tag{7}
\]

Then

\[
0\le R_{t;\gamma,i,j}<2^{D+6},
\tag{8}
\]

and `S_(t;gamma,i,j)` is a positive odd integer coprime to three. The four binary source blocks are distinct modulo `2^(D+6)`.

## Exact ternary source gate

For a fixed `j`, exactly two residues

\[
\nu\in\{0,1,2\}
\]

satisfy

\[
\boxed{
3\nmid
R_{t;\gamma,i,j}+2^{D+6}\nu.}
\tag{9}
\]

Call this two-element set `V_(t;gamma,i,j)`. For each allowed `nu`, define

\[
\boxed{
\widehat R_{t;\gamma,i,j,\nu}
=R_{t;\gamma,i,j}+2^{D+6}\nu,}
\tag{10}
\]

\[
\boxed{
\widehat S_{t;\gamma,i,j,\nu}
=S_{t;\gamma,i,j}+2^{6-j}3^G\nu.}
\tag{11}
\]

These are eight canonical ordinary source blocks modulo

\[
3\cdot2^{D+6}.
\]

## Exact high-tail replacement

For every target `j`, allowed ternary residue `nu`, and ordinary integer `m>=0`,

\[
\boxed{
C
=\widehat R_{t;\gamma,i,j,\nu}
+3\cdot2^{D+6}m}
\tag{12}
\]

is a legal primitive-core step with target type `j`, and its exact next core is

\[
\boxed{
C'
=\widehat S_{t;\gamma,i,j,\nu}
+3\cdot2^{6-j}3^Gm.}
\tag{13}
\]

Conversely, every core on which `T-8507` is defined belongs to exactly one of the eight cylinders `(12)`, and its output is `(13)`.

Thus one intrinsic state performs eight mixed-radix replacements

\[
\boxed{
\widehat R_{j,\nu}
+3\cdot2^{D+6}m
\longmapsto
\widehat S_{j,\nu}
+3\cdot2^{6-j}3^Gm.}
\tag{14}

## Uniform supercriticality

The high-tail multiplier in every block over target `j` is

\[
\lambda_{t;\gamma,i,j}
=
\frac{3\cdot2^{6-j}3^G}{3\cdot2^{D+6}}
=
\frac{3^G}{2^{D+j}}.
\tag{15}
\]

The proof of `T-8506` gives

\[
\boxed{
\lambda_{t;\gamma,i,j}>2^{170}}
\tag{16}
\]

for every finite state and target type at `t>=3744`.

## Proof

Equation `(1)` is the unique solution to the high binary divisibility in `T-8507`. Substitution gives `(2)--(4)`.

The six-bit target condition is

\[
3^{\beta_i}(h+Aq)\equiv p_j\pmod{64}.
\]

Since `A` and `3^(beta_i)` are odd, it has the unique solution `(5)` modulo `64`. Write

\[
q=\kappa_{t;\gamma,i,j}+64\ell.
\]

Substitution in `(3)--(4)` gives

\[
C=R_{t;\gamma,i,j}+2^{D+6}\ell,
\]

\[
C'=S_{t;\gamma,i,j}+2^{6-j}3^G\ell.
\tag{17}
\]

The source `C` must be coprime to three. Because `2^(D+6)` is a ternary unit, exactly one residue of `ell mod3` makes `C` divisible by three, and the other two are the set in `(9)`. Writing

\[
\ell=\nu+3m
\]

proves `(10)--(14)`.

The quotient `C'` is always coprime to three because `3^G C+1` is congruent to one modulo three and the denominator is a power of two. It is odd because the target residue `p_j` has exact binary valuation `j`. Distinctness follows from the distinct target residues and the two distinct ternary lifts. Formula `(15)` is immediate, and `(16)` is `T-8506`. ∎

## Constructive meaning

At every scale the local ordinary arithmetic is completely compiled into eight finite blocks. Infinite existence is not a local branch problem: every block has infinitely many positive representatives and enormous growth. The missing theorem is exact compatibility of the output `(13)` with one of the eight next-scale source blocks.
