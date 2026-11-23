# Ordinary lattice descent through an infinite block dictionary

23 November 2026. **Written theorem with an end-to-end Lean ordinary-word consumer. Full Collatz remains OPEN.**

This closes the specific infinite-dictionary boundary left in the previous [UNEQUAL_BLOCK_COMMUTATOR.md](../../universal-step-20261123/commutator/UNEQUAL_BLOCK_COMMUTATOR.md), Section 5: repetition counts may now vary independently from block to block, defect words may change arbitrarily, and the number of blocks is unbounded. The result excludes escape and nonconstant cycle boundaries in the stated language. It is an ordinary-integer descent theorem, not a finite-word census.

The key arithmetic is that a long *actual* repetition supplies a large divisor of a fixed-point displacement. A sufficiently small affine error then strictly decreases the resulting integer quotient. No external analytic theorem is used, and no literature-priority claim is made.

## 1. Complete words and the cutoff certificate

Use the shortcut map

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd}.\end{cases}
\]

Fix a nonempty binary word `u` with complete affine data

\[
F_u(x)=\frac{Px+C}{Q},\quad P=3^{p(u)},\quad Q=2^{|u|},\quad C\ge0,
\qquad d:=Q-P>0. \tag{LD1}
\]

Thus `u` is coefficient-contracting and has real fixed point `q=C/d`. A prescribed word is applied only when every indicated ordinary parity branch is actually legal.

Let `t_i` be any indexed family of finite binary defect words, with

\[
F_{t_i}(x)=\frac{R_i x+B_i}{S_i},\quad R_i=3^{p(t_i)},\quad S_i=2^{|t_i|},\quad B_i\ge0.
\]

The index set need not be finite, lengths need not be bounded, and an empty defect is permitted. Define

\[
E_i=dB_i-(S_i-R_i)C. \tag{LD2}
\]

Fix `K>=1` for which **every allowed defect** satisfies the exact integer certificate

\[
\boxed{R_iP^K+|E_i|<S_iQ^K.} \tag{LD3}
\]

These parameters come from complete words. No polynomial factor, truncated carry, or unproved distribution estimate is substituted.

Consider an actual positive ordinary orbit whose entire future parity word, from a specified boundary source `x_0`, is

\[
u^{k_0}t_{i_0}\,u^{k_1}t_{i_1}\,u^{k_2}t_{i_2}\cdots,
\qquad k_j\ge K. \tag{LD4}
\]

Let `x_j` be its actual positive integer at the start of the j-th macroblock and `v_j` its value after `u^{k_j}`. Run lengths, labels, and defect lengths may all change independently.

### Theorem LD-T: explicit all-time descent

Every `z_j=d x_j-C` is divisible by `D=Q^K`. Define the signed ordinary integer

\[
h_j=(d x_j-C)/Q^K,\qquad H=|h_0|.
\]

Then

\[
\boxed{|h_j|\le\max(H-j,0).} \tag{LD5}
\]

At every macroboundary `j>=H`,

\[
\boxed{d x_j=C.} \tag{LD6}
\]

Every defect used thereafter has `E_{i_j}=0` and fixes `q`. If `q` is not a positive integer, **no all-time positive ordinary orbit has language (LD4)**. If it is a positive integer, every such orbit reaches it by at most `H` macrosteps; the word `u` then supplies its genuine finite positive Collatz cycle. This does not presume that an arbitrary word with an integer fixed point has the standard cycle.

The bound counts macrosteps. Their lengths are unbounded, so no shortcut-clock bound is asserted without extra hypotheses.

## 2. The ordinary lattice and exact transport

One actual application of `u` satisfies

\[
Q(dy-C)=P(dx-C).
\]

Induction over `k` literal copies, retaining every intermediate integer, gives

\[
Q^k(dv-C)=P^k(dx-C). \tag{LD7}
\]

Since `gcd(P,Q)=1`, the complete `Q^k` divides `dx-C`. This is ordinary divisibility, not an inference from finite approximation to an infinite orbit. In (LD4), `Q^K|z_j` at every boundary, including the next one, because that boundary also begins at least `K` actual copies.

Combining the defect edge `S_i y=R_i v+B_i` with (LD7) gives

\[
\boxed{S_iQ^k(dy-C)=R_iP^k(dx-C)+Q^kE_i.} \tag{LD8}
\]

Both complete carries are retained. The sign of `E_i` is unrestricted.

## 3. Every independent exponent is paid

For `k>=K` and `P<Q`,

\[
P^kQ^K\le P^KQ^k.
\]

Multiplying (LD3) by `Q^k` therefore proves

\[
\boxed{R_iP^kQ^K+|E_i|Q^k<S_iQ^kQ^K.} \tag{LD9}
\]

Substituting `z_j=D h_j` and `z_{j+1}=D h_{j+1}` into (LD8) yields

\[
b h_{j+1}=a h_j+e,\qquad a=R_iP^kD,\quad b=S_iQ^kD,\quad e=Q^kE_i,
\qquad \boxed{a+|e|<b}. \tag{LD10}
\]

If `h_j!=0`, its integer magnitude is at least one, and

\[
b|h_{j+1}|\le a|h_j|+|e|\le(a+|e|)|h_j|<b|h_j|.
\]

Its magnitude drops by at least one. If `h_j=0`, then `b|h_{j+1}|=|e|<b`, so `h_{j+1}=0`. Induction proves (LD5). Substituting both zero displacements in (LD8), using `Q^k>0`, gives `E_i=0` for every subsequent defect.

The next-boundary lattice is essential to this normalized argument. A finite prefix ending immediately after its final defect does not automatically supply it. For a finite certificate, append `K` legal copies of `u` at the last boundary, or supply its exact divisibility separately. With that lookahead, the same finite clock bound holds through all displayed edges.

## 4. Infinite families and effective selection of K

For a fixed finite defect dictionary, a suitable `K` always exists: divide (LD3) by `S_iQ^K`, then use `P/Q<1` and `Q>1`. Searching positive integers `K` with exact integer arithmetic terminates. Expanding defects, including the one-step odd word, are allowed.

Finiteness is unnecessary. Suppose a possibly infinite family has known uniform finite bounds

\[
R_i/S_i\le L,\qquad |E_i|/S_i\le H_*.
\]

Any `K>=1` satisfying

\[
\boxed{L(P/Q)^K+H_*/Q^K<1} \tag{LD11}
\]

certifies that entire family. Also

\[
E_i/S_i=d\bigl(F_{t_i}(q)-q\bigr).
\]

Thus bounded normalized multiplier and bounded endpoint displacement at the single fixed real point `q` suffice even for unbounded defect lengths. These bounds still have to be established for the allowed words; coefficient contraction alone does not supply them.

### Full cycle consequence

A positive integer cycle over a finite concatenation of the allowed macros can be repeated to obtain an all-time ordinary path. Formula (LD6) and periodicity force **every** boundary to equal `q` and every used defect to fix it. This covers an unbounded number of macroblocks, all independent exponents `k_j>=K`, and all orderings.

In the earlier two-word setting `{u,u^k t}`, pure copies of `u` can be absorbed into the following run. If `E_t!=0`, no positive integer cycle using defects remains once every defect-separated run meets this cutoff. Unlike the prior fixed-k result, all larger run lengths can now be freely mixed in one cycle. Pure-u cycles retain their separate integer fixed-point condition.

## 5. Two entire languages

### Nonintegral center and unbounded run lengths

Take `u=100`, with `(P,Q,C)=(3,8,1)`, `d=5`, and `q=1/5`. Let the defect be the single expanding bit `t=1`, with `(R,S,B)=(3,2,1)`. Here `E=6`, and `K=1` works:

\[
3\cdot3+6=15<16=2\cdot8.
\]

Consequently **no positive ordinary integer** has an all-time itinerary

\[
(100)^{k_0}1\,(100)^{k_1}1\,(100)^{k_2}1\cdots,\qquad k_j\ge1,
\]

even for unbounded, aperiodic run lengths. Finite prefixes still have ordinary witnesses. This theorem excludes one fixed ordinary witness for the infinite word and does not confuse those two quantifiers.

### Standard-cycle runs and every bounded defect word

Take `u=10`, so `(P,Q,C)=(3,4,1)` and `q=1`. Fix `B>=1`, and allow **every** binary defect word of length at most `B`. An explicit uniform cutoff is

\[
\boxed{K=2B.} \tag{LD12}
\]

To prove this without enumerating words, put `a=(3/2)^B`. Every allowed word has `R/S<=a`. Both branches on a nonnegative real input are bounded above by `(3x+1)/2`, so `0<F_t(1)<=2a-1`. Since `a>=3/2`,

\[
|E|/S=|F_t(1)-1|\le2a-2.
\]

The left side of (LD11), with these bounds and `K=2B`, is at most

\[
(27/32)^B+2(3/32)^B-2(1/16)^B<1. \tag{LD13}
\]

For `B=1` it equals `29/32`. For `B>=2`, discard the negative term and bound both other powers by their values at two, obtaining at most `747/1024<1`.

Every actual positive orbit with a full tail

\[
(10)^{k_0}t_0\,(10)^{k_1}t_1\cdots,\qquad k_j\ge2B,\quad |t_j|\le B,
\]

therefore reaches 1. At its specified first boundary the integer clock is

\[
H=(x_0-1)/16^B.
\]

The quotient is integral because the actual first run supplies the lattice. It bounds the number of macroblocks to a boundary equal to 1. A hypothetical nonconvergent orbit cannot have any such complete tail, for any fixed `B`.

## 6. Repository synthesis and the missing universal inference

The latest source pins and precise inspection scopes are in the adjacent report's `SOURCES.json`.

- PR175 forces a residual polynomial denominator larger than every hypothetical integer-cycle state. Numerical evaluation cancellation remains open. This proof imports no estimate on that gcd.
- PR178 classifies globally nonincreasing additive prime potentials. This height is a signed affine displacement divided by a divisor supplied by actual repetitions; it is not completely additive.
- PR180's global cycle-defect budget uses an explicit predecessor-density premise. That premise is not imported here.
- PR183 treats a fixed finite number of independently powered atoms. Here the number of defects is unbounded and the run-length alphabet infinite, while every defect must satisfy the displayed cutoff.
- PR185 retains the complete numerical divisibility question after polynomial cancellation. Here ordinary intermediate integers supply the decisive lattice; no proper denominator factor substitutes for closure.

The **remaining universal inference** is a coverage theorem placing every unresolved ordinary trajectory in a certified language of this kind, or another compatible descent handling transitions that violate (LD3). No such coverage theorem is proved. Arbitrary word complexity is not bounded by this argument. Calling an arbitrary cycle one atom still requires checking that atom's own integer fixed point.

## 7. Exact formal boundary

[LatticeDescent.lean](LatticeDescent.lean) uses core/Std only. It proves signed integer paid-edge descent and zero absorption, the explicit all-time clock, literal affine repetition and its coprime lattice, complete defect transport, the cutoff's extension to every larger independent exponent, and an all-time consumer for arbitrary changing defects.

The final `ordinary_word_language_hit` declaration consumes literal positive shortcut traces with every parity and intermediate endpoint. Its conclusion is (LD6) at the explicit quotient clock; its cutoff is exactly (LD3), rather than an assumed convergence conclusion. No finite-alphabet hypothesis is present.

The real uniform-bound specialization (LD11), explicit estimate (LD12)--(LD13), and prose cycle/coverage consequences are written deductions, not additional Lean declarations. Twenty public declarations are audited. Their exact compiler output and source hash are recorded separately. No external analytic theorem, universal Collatz premise, or custom research axiom is installed.

