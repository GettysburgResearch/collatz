# An infinite guarded obstruction to the inverse carry selector

**Proved scoped obstruction. No Collatz counterexample or full proof is claimed.**

The reverse-oriented use of PR170's carry family sometimes produces a
smaller physical-five failure from its endpoint. Varying its two parameters
does not provide such a return for every supplied convergent antecedent.
There is an explicit infinite family with one-step ordinary certificates
for which **no positive integral smaller inverse source exists**, even
before the source ternary-unit guard is imposed.

## IC1. Exact ordinary interface and the required guards

Source: PR170 at `656063d5efa0f5708356ab2563a4348d39bae013`,
`research/global-forcing-20261121/certificates/CARRY_COMPILER.md`, CF2--CF3.
Its source and target words are

\[
E\,1^r\,(3,b),\qquad F\,1^r\,(4,b-1),
\]

where `r>=0`, `b>=2`,
`E=(2,1,1,1,2,1,7)`, and `F=(3,6,1,2,1,1,1)`.
Both use `r+9` odd inputs and clock `r+b+18`. Their source formula is

\[
x=\frac{2^{r+b+18}q-1351\,3^{r+5}-2^{r+16}}{3^{r+9}}.
\tag{IC1}
\]

Whenever the positive odd source is integral, these are ordinary paths
`x -> q` and `5x ->5q`, with all displayed valuations exact. The full
inverse numerator supplies every successive divisibility guard, as proved
in the cited source.

For a least physical-five failure `q`, the usable return needs `x` to be
a positive odd ternary unit and `x<q`. Its convergence certificate would
be the source word followed by the **supplied certificate for q**. The
target word transfers nonconvergence of `5q` to `5x`. No new membership
assumption at a large unproved source is permitted.

Rewrite (IC1) as

\[
3^{r+5}(81x+1351)
 =2^{r+16}(2^{b+2}q-1).
\tag{IC2}
\]

For every integral `x`, the left factor `81x+1351` is a ternary unit.
Thus integrality forces the exact condition

\[
v_3(2^{b+2}q-1)=r+5.
\tag{IC3}
\]

Put `D=(2^(b+2)q-1)/3^(r+5)`. It is a positive integer, and

\[
x=\frac{2^{r+16}D-1351}{81}.
\tag{IC4}
\]

The remaining integrality condition is `2^(r+16)D=1351 mod81`;
the ternary-unit condition is checked after that division. In particular,
mere solvability of a congruence at an unrestricted exponent does not
supply the required smaller source.

## IC2. Two necessary height bounds

Assume `q>=5` and that `x` in (IC1) is an integer with `0<x<q`. Then

\[
\boxed{b<r,\qquad 2^{r+16}<81q+1351.}
\tag{IC5}
\]

The second bound follows immediately from (IC4), since `D>=1`.
For the first, suppose `b>=r`. The coefficient
`2^(r+b+18)-3^(r+9)` is positive. Multiplying `x-q` by `3^(r+9)`
and using `q>=5`, `4^r>=3^r>=2^r`, gives

\[
\begin{aligned}
3^{r+9}(x-q)
&\ge 5\,2^{18}4^r
 -(5\,3^9+1351\,3^5)3^r-2^{16}2^r\\
&\ge818476\,3^r>0,
\end{aligned}
\]

contradicting `x<q`.

These bounds also give a complete finite decision for each fixed endpoint.
Only

\[
0\le r\le \lfloor\log_2(81q+1350)\rfloor-16,
\qquad 2\le b<r
\tag{IC6}
\]

need be considered. More efficiently, enumerate the possible `b` and use
(IC3) to determine its unique possible `r`, then check (IC4), positivity,
the unit guard, strict height, and the actual ordinary words. A finite
decision at each endpoint is not a proof that every endpoint has a return.

## IC3. Infinite obstruction with supplied rank-one certificates

For every integer `H>=4`, set

\[
\boxed{q_H=\frac{2^{3^H+1}-1}{3}.}
\tag{IC7}
\]

**Theorem.** There are no integers `r>=0,b>=2` for which (IC1), with
`q=q_H`, gives a positive integer `x<q_H`. Consequently there is no
eligible ternary-unit inverse return of this carry family at `q_H`.

Each `q_H` is positive and odd and has the exact one-step first-hit
certificate `(3^H+1)`. Also

\[
v_3(q_H+1)=H,
\tag{IC8}
\]

so it is a ternary unit. For (IC8), the elementary cubing identity gives
`v_3(2^(3^j)+1)=j+1`; use
`q_H+1=2(2^(3^H)+1)/3`. Thus every member comes with an actual supplied
source certificate, rather than an unproved source-convergence premise.

### Proof of the theorem

Suppose such an integral `x<q_H` exists. By (IC5), `b<r`. Furthermore,

\[
81q_H+1351=54\,2^{3^H}+1324<2^{3^H+6},
\]

where `1324<10*2^(3^H)` holds already for `H>=2`. The strict power-of-two
bound in (IC5) therefore gives

\[
\boxed{r\le3^H-11,\qquad b+2<3^H.}
\tag{IC9}
\]

If `r+5<=H`, then (IC8) and the necessary congruence from (IC3) imply

\[
2^{b+2}=-1\pmod{3^{r+5}}.
\]

Two has order `2*3^(r+4)` modulo that modulus. Hence
`b+2>=3^(r+4)`, so `b>=3^(r+4)-2>r`, contradicting `b<r`.
The order claim follows elementarily by successive cubing from
`v_3(4-1)=1`; the half-order power is the unique element of order two.

It remains that `r+5>H`. Reducing the same congruence modulo `3^H`,
and writing `M=3^(H-1)`, shows that `b+2` is a positive odd multiple
of `M`. By (IC9) it is strictly below `3M`. Therefore

\[
b+2=M.
\tag{IC10}
\]

Let `t=2^M` and `z=t+1`. Then `v_3(z)=H` and
`q_H=(2t^3-1)/3`. Exactly,

\[
2^M q_H-1
=\frac{2t^4-t-3}{3}
=\frac{z(-9+12z-8z^2+2z^3)}{3}.
\tag{IC11}
\]

Because `H>=4`, the bracket has exact ternary valuation two: its first
term is `-9`, while every other term is divisible by 27. Thus

\[
v_3(2^M q_H-1)=H+1.
\]

Condition (IC3) now forces `r=H-4`, whereas (IC10) gives
`b=3^(H-1)-2>H-4=r`. This again contradicts `b<r` and finishes the
proof for **all** `r,b`. No bound obtained by a finite parameter search
is used in this argument.

## Consequence and exact scope

Varying `r,b` in this completed carry family cannot supply an all-endpoint
smaller-source selector for every known convergent odd ternary unit. The
obstruction persists even when the caller supplies the complete one-step
certificate for `q_H`, and even when the inverse source is allowed to be
divisible by three.

This does **not** assert that any `5q_H` fails to converge, that any `q_H`
is an actual least five failure, or that another theorem cannot exclude
this family from such a minimum. It says that the proposed carry selector
cannot itself make that exclusion: a separate ordinary target proof or a
different guarded return is required. This argument supplies no certificate
for these fivefold targets and does not show they are actual failures.

## Exact verification

`check_inverse_carry_selector.py` is standalone, accepts `--output`, and
uses explicit failures under normal and optimized Python. It verifies the
integer constants, cubing identities, source certificates and valuations,
the complete finite selector on specified obstruction endpoints, and
positive eligible return controls with both ordinary arms replayed.
`inverse_carry_selector_expected.json` records those finite scopes. The
all-`H`, all-`r,b` statement rests on IC2--IC3, not on the finite controls.
