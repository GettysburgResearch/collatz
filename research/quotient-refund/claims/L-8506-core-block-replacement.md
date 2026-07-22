# L-8506 — The intrinsic core decoder has four exact mixed-radix blocks

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

Thus every core satisfying the high divisibility gate has the unique form

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

## Four canonical target blocks

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

and `S_(t;gamma,i,j)` is a positive odd integer coprime to three.

The four source blocks `R_(t;gamma,i,j)` are distinct modulo `2^(D+6)`.

## Exact high-tail replacement

For every ordinary integer `ell>=0`,

\[
\boxed{
C
=R_{t;\gamma,i,j}+2^{D+6}\ell}
\tag{9}
\]

is a legal core step with target type `j`, and its exact next core is

\[
\boxed{
C'
=S_{t;\gamma,i,j}
+2^{6-j}3^G\ell.}
\tag{10}
\]

Conversely, every core on which `T-8507` is defined belongs to exactly one of the four cylinders `(9)`, and its output is `(10)`.

Thus one intrinsic state performs the mixed-radix replacement

\[
\boxed{
R_j+2^{D+6}\ell
\longmapsto
S_j+2^{6-j}3^G\ell,}
\tag{11}
\]

with the same finite ordinary high tail `ell`.

## Uniform supercriticality

The high-tail multiplier in branch `j` is

\[
\lambda_{t;\gamma,i,j}
=
\frac{2^{6-j}3^G}{2^{D+6}}
=
\frac{3^G}{2^{D+j}}.
\tag{12}
\]

The proof of `T-8506` gives

\[
\boxed{
\lambda_{t;\gamma,i,j}>2^{170}}
\tag{13}
\]

for every finite state and target type at `t>=3744`.

## Proof

Equation `(1)` is the unique solution to the high binary divisibility in `T-8507`. Substitution gives `(2)--(4)`.

The six-bit target condition is

\[
3^{\beta_i}(h+Aq)\equiv p_j\pmod{64}.
\]

Since `A` and `3^(beta_i)` are odd, it has the unique solution `(5)` modulo `64`. Writing

\[
q=\kappa_{t;\gamma,i,j}+64\ell
\]

and substituting into `(3)--(4)` gives `(9)` and

\[
\frac{AC+1}{2^D}
=h+A\kappa_{t;\gamma,i,j}+64A\ell.
\]

The first two terms have residue `3^(-beta_i)p_j mod64`, whose exact binary valuation is `j`. Division by `2^j` proves `(7)` and `(10)`. The quotient is odd. The numerator `AC+1` is congruent to one modulo three, so the quotient is also coprime to three.

The four target residues `p_j` are distinct modulo `64`, so their quotient cells and source blocks are distinct. The converse follows from uniqueness of the high residue `(1)` and the six-bit residue `(5)`. Formula `(12)` is immediate, and `(13)` is `T-8506`. ∎

## Constructive meaning

At every scale the local arithmetic is completely compiled into four finite blocks. Infinite existence is not a local branch problem: every branch has infinitely many positive ordinary representatives and enormous growth. The missing theorem is exact compatibility of the output `(10)` with one of the four next-scale source blocks.
