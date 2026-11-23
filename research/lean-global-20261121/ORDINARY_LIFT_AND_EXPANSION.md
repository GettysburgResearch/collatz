# Ordinary lifting, unbounded ladder transport, and the expansion boundary

## Status and source boundary

The statements below are proved in the Lean 4.34.1 kernel using only core
Lean and the explicitly imported PR174/PR146 definitions. They are not a
proof of full Collatz convergence. The theorem names and hypotheses below
are the executable boundary; no probability-one assertion is used.

The high-bit affine identity is already present as `CollatzUpperBit.high_bit`
in PR146, head `f431078244e868dc699fad011044f0d5e7f76437`,
`research/upper-bit-mergers/HighBit.lean`. Its first 200 lines were inspected;
the whole Mathlib file was not rebuilt for this pass. Our core-only proof
also tracks the actual odd count and connects the identity directly to the
imported ordinary `Basin` predicate.

The valuation-two ladder is credited to PR166, head
`5996b9f525ca50978bc34f423192c36a87765bf3`,
`research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md`,
FL1--FL4. Its all-exponent Lean clock/count proof is new formalization of
that mathematical family, not a new-family claim. The expansion boundary
was obtained while attempting a complete inverse descent cover in this pass.

## 1. The all-word ordinary bridge

Write `T` for the shortcut map, `T^t(n)` for its actual `t`th iterate, and
`s_t(n)` for the number of odd inputs in those `t` steps. For every natural
`n,t,q`, Lean proves

\[
T^t(n+2^tq)=T^t(n)+3^{s_t(n)}q,
\qquad s_t(n+2^tq)=s_t(n).
\]

The proof is induction on `t`. The first even shift has the exact law

\[
T(n+2q)=T(n)+
\begin{cases}q,&n\text{ even},\\3q,&n\text{ odd}.\end{cases}
\]

It therefore preserves the first parity and reduces the remaining
lifting problem to the induction hypothesis. Every quantified `q` is an
ordinary integer. No completion or existential choice of a new source
appears between the two sides.

`basin_high_bit_lift` proves membership equivalence with the displayed
ordinary endpoint. A balanced five return at `(n,t)` means both
`s_t(5n)=s_t(n)` and `T^t(5n)=5T^t(n)`. Under these two supplied hypotheses,
`balanced_five_lift` proves the same return on every `n+2^tq`.

For the actual failure predicate

\[
F(n):=(n\in C)\land(5n\notin C),
\]

`five_failure_cylinder` proves

\[
F(n+2^tq)\iff F\bigl(T^t(n)+3^{s_t(n)}q\bigr).
\]

It does not assert that every input has a nonzero balanced return, or that
a return decreases ordinary value.

Source: [OrbitLift.lean](lean/CollatzGlobal/OrbitLift.lean).

## 2. An actual unbounded family of strictly decreasing returns

For every `r,n >= 0`, put

\[
x=4^{r+2}n+1,\qquad a=3^{r+2}n+1.
\]

When the actual endpoint guard `a mod16=5` holds, the supplied pair has
a balanced return at clock `2(r+2)+4`, ending at

\[
m=\frac{3^{r+3}n+4}{16},\qquad 5m.
\]

Lean proves simultaneously:

- all ordinary shortcut equalities and exact odd counts;
- `0<m<x`;
- `F(x) iff F(m)`;
- the explicit nonempty progressions `n=4*3^(r+2)+16q`, for every `q>=0`.

The source's first `2(r+2)` clocks have `r+2` odd inputs. The target arm
has `r+1`, and ends at `b=5*3^(r+1)n+1`, satisfying `3b+2=5a`. Four
additional actual steps repair that one-count deficit: the source makes
one odd step, the target makes two, and the endpoints have ratio five.
The growth estimate `3^(r+2)<=4^(r+2)` proves strict source descent.

The one-rung case is the full ordinary cylinder

\[
F(49+64q)\iff F(7+9q),\qquad q\ge0,
\]

with a balanced return at clock six. The all-rung theorem is induction
on unrestricted `r`; it is not obtained by enumerating a finite set of
ladder lengths.

The missing selector issue is unchanged: these families cover their
displayed guarded domains. This module gives no total successful choice
for every failure.

Source: [UnboundedLadder.lean](lean/CollatzGlobal/UnboundedLadder.lean).

## 3. A universal obstruction to inverse expanding covers

The attempted new route was to cover all sufficiently large endpoints
by balanced expanding words, which would provide smaller actual inverse
sources. Lean proves a necessary obstruction for **every** actual word,
whether balanced or not:

\[
2^t<3^{s_t(n)}
\quad\Longrightarrow\quad
T^t(n)\not\equiv1\pmod{3^{s_t(n)}}.
\]

This is `expanding_endpoint_not_one_mod`. The proof avoids any assumption
about the legality of a signed or rational inverse. Its two core bounds are

\[
3^{s_t(n)}n\le2^tT^t(n),
\]

and, for a canonical binary representative,

\[
0\le n<2^t\quad\Longrightarrow\quad
0\le T^t(n)<3^{s_t(n)}.
\]

The first bound follows by induction from the nonnegative affine
corrections. For the second, the first even branch stays inside the
smaller binary box. The first odd branch lies below three times that box;
split it into its three possible high-bit lifts and apply the induction
hypothesis to the canonical remainder.

Now reduce an arbitrary source modulo `2^t`. Exact lifting preserves
the odd count and changes the endpoint by a multiple of `3^s`. If the
endpoint were congruent to one, the canonical-box bound would force its
canonical endpoint to equal one. The lower bound and strict expansion
then force the canonical source to be zero; its endpoint is zero, a
contradiction.

Consequently an expanding word ending at `q` must have
`s > v_3(q-1)` when `q>1`. Any proposed finite dictionary has bounded
`s` and leaves an infinite progression near `q=1` uncovered. The stronger
inverse-only impossibility, including unbounded dictionaries and finite
certified base sets, is proved separately in
[Forcing.lean](lean/CollatzGlobal/Forcing.lean).

Source: [Expansion.lean](lean/CollatzGlobal/Expansion.lean).
