# L-0037 — Fixed-weight parity constants represent every 3-adic unit at arbitrary precision

Claim ID: `L-0037`  
Title: A recursive discrete-log compiler represents every unit modulo `3^P` by a parity word of any prescribed weight `a <= P`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-23  
Dependencies: `D-0001`, `L-0001`, elementary lifting the exponent  
Scope: finite parity words and exact modular affine constants  
Related counterexample candidates: none

## Statement

Let

\[
1\le a\le P
\]

and let `y` be a unit modulo `3^P`.  Then there are strictly increasing
nonnegative positions

\[
0\le p_0<p_1<\cdots<p_{a-1}
\]

such that the weight-`a` parity-affine constant

\[
\boxed{
B(p_0,\ldots,p_{a-1})
=
\sum_{j=0}^{a-1}2^{p_j}3^{a-1-j}}
\tag{1}
\]

satisfies

\[
\boxed{B(p_0,\ldots,p_{a-1})\equiv y\pmod {3^P}.}
\tag{2}
\]

The positions can be chosen with the explicit common-length bound

\[
\boxed{
p_{a-1}<G(a,P):=3^P-3^{P-a}.}
\tag{3}
\]

Thus every target has a weight-`a` representative after padding all words with
high zero symbols to the common length `G(a,P)`.

## Primitive-root lemma

For every `P >= 1`, the element `2` has exact multiplicative order

\[
\boxed{\operatorname{ord}_{3^P}(2)=2\cdot3^{P-1}.}
\tag{4}
\]

Indeed, for `m >= 0`, lifting the exponent gives

\[
\nu_3(2^{2\cdot3^m}-1)
=
\nu_3(4^{3^m}-1)
=
\nu_3(4-1)+\nu_3(3^m)
=m+1.
\]

Hence `2` generates the full unit group modulo every power of three.

## Recursive compiler

Write `Rep(a,P,y)` for the following finite algorithm.

### Base case `a=1`

Choose the unique canonical exponent

\[
0\le e<2\cdot3^{P-1}
\]

with

\[
2^e\equiv y\pmod {3^P}.
\]

Return the one-position word `(e)`.

### Recursive case `a>1`

1. Compute the fixed prefix
   \[
   (p_0,\ldots,p_{a-2})=\operatorname{Rep}(a-1,P-1,1).
   \]
2. Let `B_0` be its affine constant, evaluated modulo `3^P`.
3. Put
   \[
   u\equiv y-3B_0\pmod {3^P}.
   \]
   Since `u == y (mod 3)`, it is a unit.
4. Choose `e` with `2^e == u (mod 3^P)` and add a multiple of
   `2*3^(P-1)` until
   \[
   p_{a-1}:=e+k(2\cdot3^{P-1})>p_{a-2}.
   \]
5. Return the prefix followed by `p_(a-1)`.

The discrete logarithm itself is causal and finite.  Starting with the parity
of the exponent modulo two, lift from `3^m` to `3^(m+1)` by testing exactly the
three candidates

\[
e,
\quad e+2\cdot3^{m-1},
\quad e+2(2\cdot3^{m-1}).
\tag{5}
\]

Exactly one candidate is correct.

## Proof of correctness

The base case follows from (4).  In the recursive case, appending one final odd
symbol changes the affine constant by

\[
B_{\rm new}=3B_0+2^{p_{a-1}}.
\tag{6}
\]

The construction makes the second term congruent to `u`, so (6) is congruent to
`y` modulo `3^P`.

It remains to prove the length bound.  The base exponent at precision
`P-a+1` is at most

\[
2\cdot3^{P-a}-1.
\]

At every later recursive level, the least order-lift needed to move the new
position above the previous maximum adds at most

\[
2\cdot3^{m-1}
\]

at precision `m`.  Therefore

\[
\begin{aligned}
p_{a-1}
&\le
\sum_{m=P-a+1}^{P}2\cdot3^{m-1}-1\\
&=3^P-3^{P-a}-1,
\end{aligned}
\]

which is (3). ∎

## Causal meaning

`Rep(a,P,y)` is not an existence proof requiring a future infinite digit tape.
Its input is one finite modular target `y`; its output is one finite increasing
list of odd positions.  Every operation is ordinary modular exponentiation,
three-way Hensel lifting, comparison, and integer addition.

The positions can be enormous.  In particular the theorem is an
**arbitrary-precision fallback**, not the desired linear-cost selector.
`L-0036` and `O-0012` address the efficient structured families.

## Verification

`X-0020` exhaustively checks every unit target for all

\[
1\le a\le P\le8,
\]

checks every full-offset target through `b=6`, and replays representative
weight-`176`, precision-`352` compilations using modular powers only.

## Gap audit

- The theorem proves finite modular representation, not a full Collatz orbit.
- The length bound is exponential in the precision.
- Causal generation of a collision branch does not imply that a pre-existing
  ordinary integer lies in that complete parity cylinder.
- Canonical most-significant closure remains a separate obligation.