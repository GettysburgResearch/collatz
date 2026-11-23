# An unbounded affine carry program for complete source witnesses

## Result and remaining central claim

The new module [`lean/Collatz/ContextSurgery.lean`](lean/Collatz/ContextSurgery.lean)
kernel-checks a backward carry program through an arbitrary supplied source
word. Its arithmetic state is unbounded. Every accepted run constructs an
actual integral prefix, preserves the literal complete tail, and supplies a
successful original interval query whenever its full source grade decreases.
An early exit may discard the unprocessed prefix and change the initial even
run if the resulting known source already captures the original target.

The missing claim is **success of such a program on every joint minimal
counterquery**. The module does not assume that claim. No universal residue
implication, `FloorIntervalStep`, or Collatz convergence theorem is obtained.

This is a direct attempt to exploit the full supplied certificate. It does
not replace source maximality by unrestricted word sorting or replace the
original target by a newly selected one.

## 1. Carry the changed suffix backward

Use the existing prefix convention

\[
 3^{|W|}q+C(W)=2^{A(W)}u,
 \qquad A(W)=\sum W.
\]

Suppose the unchanged source edge is

\[
 3n+1=2^a m.
\]

At the already transformed suffix, retain the exact relation

\[
 m'=2^d m+B,
 \qquad d,B\in\mathbb N.
\]

Replacing the preceding gap by a positive `b` is guaranteed to be valid
with new source `n'=2^{d'}n+B'` when the following arithmetic guard is met:

\[
 \boxed{a+d'=d+b,\qquad
        3B'+1=2^{d'}+2^b B.}
 \tag{1}
\]

Indeed, multiply the old edge by `2^{d'}` and use (1):

\[
\begin{aligned}
3n'+1
 &=2^{d'}(3n+1)+(3B'+1-2^{d'})\\
 &=2^{a+d'}m+2^bB
  =2^b(2^dm+B)=2^bm'.
\end{aligned}
\]

The Lean theorem `carry_step_identity` proves this equality with natural
arithmetic. The natural carry state restricts this particular program to
nonnegative offsets and integral nonnegative powers of two; it is not
claimed to represent every conceivable source surgery.

`CarryWord W V d B D E` records an arbitrary number of these exact steps,
processed from right to left. It retains the same intermediate carry at
every composition boundary. `carry_word_append` composes any two adjacent
runs only at that shared state. `carry_word_clock` proves

\[
 A(W)+D=d+A(V).
 \tag{2}
\]

This version replaces one odd gap by one odd gap, so `|W|=|V|`, but neither
length is bounded, and all the gaps and carry values are unrestricted.
An early exit, described below, may shorten the complete output certificate.
The user's allowance of other lengths and arbitrarily large exponents is
not converted into a completeness assumption for this narrower program.

## 2. Actual prefix and complete-tail semantics

`carry_word_prefix` establishes the central semantic statement:

\[
 \operatorname{Prefix}(q,W,u)
 \Longrightarrow
 \operatorname{Prefix}(2^Dq+E,V,2^du+B).
 \tag{3}
\]

The proof splits each supplied old prefix using the existing integral
`prefix_cons_iff`, applies (1), and recursively constructs the new actual
prefix. Thus it is not only a rational affine identity with unchecked
intermediate divisions.

For a carry which starts at `(d,B)=(0,0)`, the splice endpoint is unchanged.
`carry_word_certificate` consequently proves

\[
 \operatorname{Certificate}(q,W\mathbin{++}T)
 \Longrightarrow
 \operatorname{Certificate}(2^Dq+E,V\mathbin{++}T).
 \tag{4}
\]

The tail `T` in (4) is the original supplied tail. No new convergence oracle
or replacement witness for its endpoint is used.

The new source is at least the old one, since `2^D>=1` and `E>=0`.
Therefore, for the original powered source `S=2^e q`, every original target
`0<t<=2S+1` remains captured by

\[
 S'=2^e(2^Dq+E).
\]

`carry_interval_rule` applies the existing original induction hypothesis
when

\[
 \Gamma(e,V\mathbin{++}T)<\Gamma(e,W\mathbin{++}T).
 \tag{5}
\]

Both the complete-source grade comparison and the complete retained tail
appear explicitly in this theorem. A successful carry is not allowed to
switch to an unrelated rank.

## 3. A target-dependent exit before full propagation

Insisting on transforming the entire context is unnecessary. Suppose the
original word splits as

\[
 H\mathbin{++}W\mathbin{++}T,
\]

and its actual state after `H` is `u`. A carry on `W` alone gives a complete
certificate at `p=2^D u+E` with word `V++T`.

The theorem `suffix_exit_rule` deletes `H` and returns immediately if some
new initial even exponent `f` satisfies both

\[
 t\le2^{f+1}p+1,
 \qquad
 \Gamma(f,V\mathbin{++}T)
 <\Gamma(e,H\mathbin{++}W\mathbin{++}T).
 \tag{6}
\]

The original target `t` is unchanged. The proof obtains the suffix endpoint
by splitting the supplied complete certificate, proves it equals the
separately supplied actual state `u`, constructs its new complete tail, and
uses precisely the original interval induction hypothesis.

This exit retains the freedom emphasized by the joint minimum: discarded
prefix grades may pay for a larger new even exponent or a different earlier
inverse choice. Its capture inequality is a real remaining obligation;
source exhaustion alone does not imply it.

## 4. Exact ternary guards and a seed that must change its context

The seed

\[
 [4,1]\longrightarrow[3,3],\qquad q\longrightarrow2q+3
 \tag{7}
\]

has the same endpoint and lowers the source gap multiset. Lean records its
two backward carry states as

\[
 (0,0)\longrightarrow(2,1)\longrightarrow(1,3).
\]

This is a seed for the unbounded program, not a proposed complete cover of
the remaining words.

One cannot leave a preceding nonempty word unchanged. The theorem
`unchanged_context_blocks_seed` proves, at every length,

\[
 W\ne[],\quad\operatorname{Prefix}(q,W,u)
 \Longrightarrow
 \neg\operatorname{Prefix}(p,W,2u+3)
 \quad\hbox{for every }p.
 \tag{8}
\]

For the last common gap `a`, the old last edge has
`2^a u=3z+1`. The putative new last edge would give
`3z'+1=2(3z+1)+3*2^a`, which is impossible modulo three. The formal proof
peels the common word until this last edge. It does not assume that a local
improvement can be inserted under an arbitrary unchanged prefix.

A lifted endpoint divisible by three has no inverse odd predecessor at any
positive gap. `dead_endpoint` proves this directly. A useful repair must
therefore occur **before** reaching that endpoint, or the program must
already satisfy (6). If an earlier inverse choice is

\[
 3p+1=2^b u,
\]

then raising that choice by two gives

\[
 3(4p+1)+1=2^{b+2}u,
 \qquad (4p+1)\bmod3=(p+1)\bmod3.
 \tag{9}
\]

`raise_gap_two` and `raised_predecessor_residue` prove (9). This changes the
next ternary guard. It also changes the grade, so it is not a free repair.

For example, a greedy carry through the two preceding gaps in
`[2,2,4,1]` can stop at the multiple of three 51. Choosing the earlier gap
three instead of one yields the actual alternative

\[
 [2,2,4,1]\longrightarrow[2,3,3,3],
 \qquad q\longrightarrow4q+13.
\]

The original source 65 becomes 273; both words end at 11. This calculation
shows why a dead branch does not by itself refute the branching carry
program. It is illustrative arithmetic; the general checked results are
(1)--(6) and (9).

## 5. A complete, all-length boundary for pure gap elimination

The more restrictive strategy “erase the internal four using (7), then
grow back through gaps at most three” is not complete, even if an arbitrary
number of new gaps is allowed.

The original actual context

\[
 461\xrightarrow{3}173\xrightarrow{3}65
 \xrightarrow{2}49\xrightarrow{2}37
 \xrightarrow{4}7\xrightarrow{1}11
\]

is checked in `all_length_seed_growth_failure`. The seed replaces the
suffix source 37 by 77. But the entire inverse tree of 77 over gaps at most
three is

\[
 \{77,51,205,273\}.
\]

Indeed, the only such predecessors of 77 are 51 and 205; the only such
predecessor of 205 is 273; the two multiples of three have none. The theorem
`seventy_seven_predecessors` proves closure of this finite set and inducts
over an arbitrary prefix word. Consequently no such word ending at 77 has
source at least 461.

This is an all-length obstruction to the specified odd-source regrowth
strategy. It is **not** a counterexample to `suffix_exit_rule`, which may
use a different even exponent and the original target's slack; nor is 461
asserted to be a joint minimal counterquery. Retaining an output gap four,
using other original prefix grades, changing the splice, or proving a
target merger remain available.

## 6. Central status and verification boundary

The outstanding mathematical step is to show that every `JointBadQuery`
admits a successful rank-accounted carry, early exit, or other target
return. No such exhaustive theorem is presently proved. The original
source floor, minimum grade, maximum source at that grade, and arbitrary
length supplied tail remain available for that proof; none is replaced by
the seed example or by the obstruction in Section 5.

`ContextSurgery.lean` compiled directly with Lean 4.34.1 and
`-DwarningAsError=true`. It uses core arithmetic and the existing source
certificate definitions. There is no custom axiom, admitted proof, or
native-decision step. Its finite inverse-tree assertion is proved by an
unrestricted word induction. The parent checkpoint records the aggregate
build and theorem-dependency audit separately.
