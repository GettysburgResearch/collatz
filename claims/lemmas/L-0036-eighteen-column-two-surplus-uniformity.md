# L-0036 — Eighteen-column words are uniformly distributed through two surplus ternary digits

Claim ID: `L-0036`  
Title: One odd symbol in each eighteen-column block gives exact unit uniformity modulo `3^(b+2)`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-23  
Dependencies: `D-0001`, elementary additive Fourier inversion on a finite cyclic group  
Scope: structured fixed-weight parity words at every weight `b >= 1`  
Related counterexample candidates: none

## Setup

Put

\[
q=2^{18},
\qquad
D=\{2^s:0\le s<18\}.
\]

For `b >= 1`, choose one odd position in each consecutive block of eighteen
positions.  Thus

\[
p_j=18j+s_j,
\qquad
0\le s_j<18,
\qquad
0\le j<b.
\]

The parity-affine constant is

\[
B_b(s_0,\ldots,s_{b-1})
=
\sum_{j=0}^{b-1}3^{b-1-j}2^{18j+s_j}.
\tag{1}
\]

Reverse the block order and multiply by the unit `q^(1-b)`.  Equation (1)
becomes

\[
\widetilde B_b
=
\sum_{r=0}^{b-1}3^r q^{-r}d_r,
\qquad d_r\in D.
\tag{2}
\]

Multiplication by `q^(1-b)` only permutes residue classes modulo a power of
three.

## Theorem

As the `18^b` structured words vary, their constants are distributed uniformly
over the units modulo `3^(b+2)`:

\[
\boxed{
\#\{s:B_b(s)\equiv x\pmod {3^{b+2}}\}
=
\begin{cases}
2^{b-1}3^{b-1},&3\nmid x,\\
0,&3\mid x.
\end{cases}}
\tag{3}
\]

Consequently every unit signature modulo `3^b` has every one of its nine lifts
modulo `3^(b+2)`.  Equivalently, the structured family supplies two complete
surplus ternary correction digits at every weight.

## Proof

The eighteen powers

\[
2^0,2^1,\ldots,2^{17}
\]

are exactly the unit group modulo `27`.  Let an additive character have exact
conductor `3^k`.

For one digit set `D`, its character sum has the following values.

1. At the trivial character it is `18`.
2. At either nontrivial character modulo three it is
   \[
   9(\zeta_3+\zeta_3^2)=-9.
   \]
3. At a primitive character modulo `9` or `27` it is zero, because `D` is a
   complete unit residue system modulo `27`; equivalently these are the
   corresponding Ramanujan sums.

Take Fourier inversion on `Z/3^(b+2)Z`.  For a character of conductor `3^k`,
the factor indexed by `r` in (2) has effective conductor `3^(k-r)`; the unit
`q^(-r)` does not change the conductor.

If `2 <= k <= b+1`, choose `r=k-2`.  That factor has conductor `9` and vanishes.
If `k=b+2`, choose `r=b-1`; that factor has conductor `27` and vanishes.  Thus
all characters of conductor at least nine disappear.

Only the trivial character and the two conductor-three characters survive.
The trivial product is `18^b`.  A conductor-three product is

\[
-9\,18^{b-1},
\]

because only the `r=0` factor is nontrivial.  Fourier inversion therefore gives

\[
N_b(x)
=
{18^b-9\,18^{b-1}
(\zeta_3^{-x}+\zeta_3^{-2x})
\over3^{b+2}}.
\tag{4}
\]

When `3|x`, the root-of-unity sum is `2`, and (4) is zero.  When `x` is a unit,
the sum is `-1`, and

\[
N_b(x)
=
{18^b+9\,18^{b-1}\over3^{b+2}}
=2^{b-1}3^{b-1}.
\]

This proves (3).  Since every lift of a unit modulo `3^b` remains a unit, the
two-surplus conclusion follows. ∎

## Terminal-map interpretation

In the stationary coordinate

\[
x_{r+1}=q{x_r-d_r\over3},
\qquad d_r\in D,
\tag{5}
\]

one legal digit requires `d_r == x_r (mod 3)`.  The nine eligible digits cover
all possible successor residues modulo `9`; six keep the successor a unit and
three enter the terminal nonunit classes.  Theorem (3) is the exact all-depth
Fourier shadow of this nine-choice quotient map.

It does **not** yet prove that the same length-`18b` family covers all units
modulo `3^(2b)`.  That stronger terminal-map surjectivity is separately audited
in `X-0020` at finite depths and remains an efficiency question.  `L-0037` and
`T-0042` give an unconditional, but much longer, arbitrary-precision compiler.

## Gap audit

- Two surplus ternary digits are not the `b` surplus digits required by a
  full-offset gadget of weight `b`.
- The theorem is exact for every `b`; no finite census is extrapolated.
- It does not orient a physical Collatz branch or prove an ordinary top
  boundary.
- No counterexample integer is claimed.