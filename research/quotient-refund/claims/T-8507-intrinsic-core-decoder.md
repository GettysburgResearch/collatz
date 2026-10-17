# T-8507 — The refund architecture is one intrinsic primitive-core decoder

**Claim ID:** `T-8507`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Dependencies:** `L-8504`, `L-8505`, branch-qualified phase-`-34` physical replay  
**Scope:** every multiple of `16` with `t>=3744`

## Intrinsic state

A core state is

\[
(t,\gamma,i,C),
\]

where

\[
16\mid t,
\qquad
\gamma\in\{1,2,3\},
\qquad
i\in\{0,1,2,3\},
\]

and `C` is a positive integer coprime to six. Put

```text
beta=(2,3,2,1).
```

Define

\[
\boxed{
G=7(t+1)+\gamma-\beta_i,}
\tag{1}
\]

\[
\boxed{
D=11(t+17)-i.}
\tag{2}
\]

Both exponents are positive.

## Deterministic partial map

Form the ordinary integer

\[
\boxed{X=3^G C+1.}
\tag{3}
\]

The map is defined exactly when:

1. the high binary block divides,
   \[
   \boxed{2^D\mid X,}
   \tag{4}
   \]
2. after setting
   \[
   Y=X/2^D,
   \tag{5}
   \]
   the six-bit physical output belongs to the four tower cells,
   \[
   \boxed{
   [3^{\beta_i}Y]_{64}
   \in\{5,30,20,56\}.}
   \tag{6}
   \]

When `(6)` holds, let `j` be the unique type whose residue is obtained. Since that residue has exact binary valuation `j`, put

\[
\boxed{
C'=Y/2^j.}
\tag{7}
\]

Then

\[
\boxed{
F(t,\gamma,i,C)
=(t+16,\beta_i,j,C').}
\tag{8}
\]

This is a deterministic partial map on one unbounded positive integer and twelve finite control states. It uses no connector inverse, Hensel carry, target type, future directive, or completed `2`-adic address at runtime.

## Automatic source marker

Condition `(4)` already forces the current physical low cell. Indeed, modulo `2^(6-i)`,

\[
C\equiv-3^{-G}.
\]

Therefore

\[
2^i3^\gamma C
\equiv
-2^i3^{\beta_i-7(t+1)}
\pmod{64}.
\tag{9}
\]

Since `16|t`, the exponent of `3` may be reduced to the same four fixed checks:

```text
i=0: -3^(-5) == 5  mod64,
i=1: -3^(-4) == 15 mod32,
i=2: -3^(-5) == 5  mod16,
i=3: -3^(-6) == 7  mod8.
```

Multiplying by `2^i` gives

\[
\boxed{
2^i3^\gamma C\equiv p_i\pmod{64}.}
\tag{10}
\]

Thus no separate current-cell condition is needed.

## Exact physical conjugacy

Define the physical integer

\[
\boxed{
n=2^{11t+5+i}3^\gamma C-34.}
\tag{11}
\]

When the core decoder is defined, define

\[
\boxed{
n'=2^{11(t+16)+5+j}3^{\beta_i}C'-34.}
\tag{12}
\]

Then

\[
\boxed{
n'=T^{11(t+1)}(n),}
\tag{13}
\]

and the block has exactly `7(t+1)` odd shortcut steps.

Conversely, every legal state of the complement-counter map `T-8504`, after the first boundary, produces exactly one core state and one update `(3)--(8)`. The two deterministic maps are conjugate through the physical integer.

## Proof

Put

\[
W=2^i3^\gamma C.
\]

Equation `(10)` makes it a source word of type `i`. The scaled physical tower equation has numerator

\[
\begin{aligned}
3^{7(t+1)}W+b_i
&=2^i3^{\beta_i}
  \left(3^{7(t+1)+\gamma-\beta_i}C+1\right)\\
&=2^i3^{\beta_i}X.
\end{aligned}
\tag{14}
\]

Under `(4)--(7)`,

\[
2^i3^{\beta_i}X
=2^{11(t+17)}2^j3^{\beta_i}C'.
\tag{15}
\]

The word

\[
W'=2^j3^{\beta_i}C'
\]

has residue `p_j mod64` by `(6)`. Equation `(15)` is therefore exactly one legal local scaled-tail connector. Multiplication by the phase-`-34` boundary factor `2^(11(t+1))/64` proves `(11)--(13)`.

The converse follows by applying the exact signature factorization of `L-8505` to a `T-8504` transition; equation `L-8505/(4)` is precisely `(3)--(7)`. ∎

## Growth and prime renewal

Whenever the map is defined,

\[
\boxed{C'>2^{170}C}
\]

by `T-8506`. Consecutive cores are coprime, and every infinite orbit escapes every fixed finite prime set by `T-8505`.

## Complete counterexample criterion

One written positive integer `n_0` whose intrinsic factorization gives a state `(t_0,\gamma_0,i_0,C_0)` with a forever-defined orbit under `(3)--(8)` is an unconditional Collatz counterexample. Every physical block, positivity, type, stage, and growth claim is reconstructed from `n_0` itself.

## Exact remaining gap

No such finite core `C_0` is supplied. The sole positive target is an inductive ordinary invariant proving that the high divisibility `(4)` and the six-bit gate `(6)` recur forever.
