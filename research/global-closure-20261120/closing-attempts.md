# Direct closing attempts: multiplication by five and inverse pressure

**Status: PROPOSED local deductions and exact failed strengthening.** The
five-closure premise in [GCM-002](merger.md) and the global inverse-potential
estimate remain OPEN. This note records the actual attempted closing steps.

Use the shortcut map `T` and odd map
`U(n)=(3n+1)/2^v2(3n+1)`. All sources are positive ordinary integers.
Let `C` be the basin of 1. No proposed implication below is inferred from
finite agreement alone.

## GCL-001: even the one-odd-step antecedents leave a shifted-power family

For `a>=1`, put

\[
x_a=\frac{4^a-1}{3}.
\]

These are positive odd integers, `U(x_a)=1`, and `3` does not divide `x_a`
exactly when `3` does not divide `a`. The last assertion follows, for example,
from `4^a=1+3a (mod 9)`.

For every `a>=2`, there is the exact ordinary identity

\[
\boxed{\quad U^{2a-1}(5x_a)=\frac{5\,9^{a-1}-1}{4}.\quad}       \tag{1}
\]

The exponent sequence is

\[
2,\ \underbrace{1,\ldots,1}_{2a-3\text{ entries}},\ 3.
\]

Indeed `3(5x_a)+1=4(5*4^(a-1)-1)`, whose parenthesis is odd. Set
`m=a-1`. Starting at `5*2^(2m)-1`, each of the next `2m-1` odd edges
has exponent one and the ordinary state after `j` such edges is
`5*3^j*2^(2m-j)-1`. At `j=2m-1`, the next numerator is
`2(5*9^m-1)`. Since `9^m=1 (mod 8)`, its valuation is exactly three.
This proves (1), including all physical parity guards.

The same computation uses exactly `2a+2` shortcut steps. Moreover, the
endpoint in (1) exceeds the original `5x_a` for every `a>=4`, and its ratio
to that original source tends to infinity. At `a=4` the two values are
`911` and `425`. Writing these two sequences as `y_a` and `z_a=5x_a`,
one has `y_(a+1)=9y_a+2` and `z_(a+1)=4z_a+5`, which preserve the strict
inequality once established; their explicit power formulas give the
unbounded ratio. Thus this particular first-hit-plus-two-step synchronized
height descent is false. An arbitrarily longer adaptive construction is
not excluded.

Consequently, proving the five-closure premise even just for these supplied
one-step sources, with `a>=2` and `3` not dividing `a`, requires convergence
of the whole displayed shifted-power family. That convergence has not been
proved here. A supplied short path for `x` does not bound the difficulty of
the new target `5x`. This is a reduction of the attempted base case, not a
claim that the restricted family by itself suffices for full Collatz.

## GCL-002: the simplest uniform inverse-lift propagator is false

A natural plan is to induct on a supplied first-hit path of `x`: first prove
five-closure at `U(x)`, then construct a physical merger between `5x` and
`5U(x)`. Uniform affine versions of this plan already fail at `x=5`.

On the entire positive ordinary progression

\[
x=5+96t,\qquad t\ge0,
\]

one has `v2(3x+1)=4` and

\[
5x=25+480t,\qquad 5U(x)=5+90t.                       \tag{2}
\]

There do not exist two fixed legal shortcut words whose outputs on the two
arms in (2) agree for all `t>=0`. The same is true on any nonconstant
arithmetic subprogression containing `t=0`, regardless of the two clocks.

Here is a direct proof that does not rely on a search cutoff. For a certified
convergent positive integer `z`, let

\[
\chi(z)=d(z)-2o(z),
\]

where `d` is its first shortcut hitting time of 1 and `o` its number of odd
steps. A legal word of length `d_i` and odd count `o_i` has slope
`3^o_i/2^d_i`. Equality of the two slopes in (2) would require

\[
d_1-d_2=4,\qquad o_1-o_2=1,\qquad
(d_1-2o_1)-(d_2-2o_2)=2.                            \tag{3}
\]

But at `t=0`, both words would end at the same ordinary value. The actual
paths `25 -> 1` and `5 -> 1` have respective `(d,o)` values `(16,7)`
and `(4,1)`, so `chi(25)=chi(5)=2`. Additivity of `chi` along any two
paths to a common endpoint therefore requires the final difference in (3)
to be zero. Padding through the `1,2` cycle changes `(d,o)` by `(2,1)`
and does not change `chi`. This is a contradiction.

This is the stopping-grade obstruction specialized to the proposed
five-lift propagator. The general affine classification is already present
in PR150 at `ef4022fa5ae43dd943ecca0b7c84d69af624c5c9`,
[`research/pointwise-closure-20261120/LOCAL_CERTIFICATE_GRADE.md`](https://github.com/GettysburgResearch/collatz/blob/ef4022fa5ae43dd943ecca0b7c84d69af624c5c9/research/pointwise-closure-20261120/LOCAL_CERTIFICATE_GRADE.md),
LC-1, building on the stopping-grade work in PR148/149; no priority for
the general invariant is claimed. Here the two ordinary endpoints are
explicitly known to converge.

The conclusion is deliberately narrow. A recursive construction may handle
this source as a base case, use different comparisons, or avoid fixed-word
identities altogether. This obstruction does not disprove five-closure.

For comparison, the exact inverse-lift calculation at a supplied unit `z`
and legal `x=(2^g z-1)/3`, with `g>=2`, is

\[
T^g(x)=z,\qquad T^g(5x)=5\,3^{g-2}z-1.              \tag{3a}
\]

After two shortcut steps the latter arm is `5*2^(g-2)z-1`; the next
`g-2` inputs are odd and give (3a). Hence this exact synchronized plan
requires unbounded multiplier indices. Likewise, for the ordinary
same-component lift `J(x)=4x+1` on odd `x`,
`5 J^a(x)-J^a(5x)=4(4^a-1)/3`. A fixed finite list of multipliers or a
fixed bounded-offset enlargement does not contain these particular return
families. This does not exclude another choice of clocks or an unbounded
state with a successful well-founded rank.

## GCL-003: reconstruction of the uniform root obligation

This deduction combines two already stated interfaces instead of treating
the large finite root certificate as an asymptotic bound. The sources are:

- main at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`,
  [`research/astra-three-routes/pass3/FINITE_RECORDS.md`](../astra-three-routes/pass3/FINITE_RECORDS.md),
  T-A3-651: every finite simple positive shortcut path has odd reciprocal
  sum at most `200` (the stronger floor-dependent bound is not needed here);
- PR148 at `55d8968d2ecbc23a91c9c4733929f34be9bf0d28`,
  [`research/focused-forward-20261120/pressure/PROOF.md`](https://github.com/GettysburgResearch/collatz/blob/55d8968d2ecbc23a91c9c4733929f34be9bf0d28/research/focused-forward-20261120/pressure/PROOF.md),
  H1 and H3: the root potential is the supremum of actual first-hit scores.
- PR150 at `ef4022fa5ae43dd943ecca0b7c84d69af624c5c9`,
  [`research/pointwise-closure-20261120/STOPPING_BURDEN.md`](https://github.com/GettysburgResearch/collatz/blob/ef4022fa5ae43dd943ecca0b7c84d69af624c5c9/research/pointwise-closure-20261120/STOPPING_BURDEN.md),
  SB5: the same constant-error equivalence already follows from its uniform
  simple-path reciprocal budget. The equivalence below is an independent
  reconstruction of that result, not a new project-level advance.

Let `m` be a positive odd ternary unit with a supplied first visit to 1 in
`h` odd steps, and let `A` be the total division exponent. Put

\[
\delta=8-5\log_2 3>0,\qquad S(m)=8h-5A,
\qquad K=\frac{1000}{3\ln2}.
\]

Then, uniformly over every such terminating source,

\[
\boxed{\quad
\delta h-5\log_2 m-K\le S(m)\le\delta h-5\log_2 m.
\quad}                                               \tag{4}
\]

The error is an absolute constant; it has no dependence on `h` or `m`.
To prove this, the first-hit shortcut path is simple. For its odd states
before 1, let `P=product(1+1/(3n_j))`. The exact product identity gives

\[
S(m)=\delta h-5\log_2 m-5\log_2 P.
\]

Using `log(1+y)<=y` and T-A3-651 gives
`0<=5 log_2 P<=5/(3 ln2) sum(1/n_j)<=K`. This proves (4). The case
`m=1,h=0` has empty product and also satisfies the bound.

Define `W(1)` by all legal inverse words on odd ternary units, with score
`8k-5A`, and include zero. Its source-pinned root formula yields the exact
equivalence

\[
\boxed{\quad W(1)<\infty
\quad\Longleftrightarrow\quad
\exists C\ \forall m\text{ in the terminating odd-unit basin},
\quad h(m)\le\frac5\delta\log_2m+C.\quad}             \tag{5}
\]

For the forward implication use the lower bound in (4) and
`S(m)<=W(1)`; the constant can be `(W(1)+K)/delta`. For the converse
use the upper bound in (4), then take the supremum of first-hit scores.
Loops at 1 have score `-2` per odd event and cannot increase the supremum.

Relative to PR148 H3 alone, the uniform reciprocal budget removes the
`log log m` error. PR150 SB5 already makes that improvement. The chosen
main-branch budget `200` gives the displayed constant `K`, while SB5 uses
its separate self-contained budget `600`; this numerical choice is not a
closing argument. Neither source nor this reconstruction proves either
side of (5). In particular, qualitative convergence alone has not supplied
this uniform logarithmic bound. Even root finiteness would still require
a separate argument for any other component.

## Relation to the semigroup theorem

Applegate and Lagarias, *The 3x+1 Semigroup*, J. Number Theory 117 (2006),
147--159, [arXiv:math/0411140v2](https://arxiv.org/abs/math/0411140v2),
Theorem 1.1, characterize the multiplicative semigroup generated by
`2` and `(2k+1)/(3k+2)`. Its products can use ratios from unrelated ordinary
sources. That theorem therefore does not justify applying multiplication
by five to an individual Collatz basin. The directed certificate here
retains the physical source and guards at every ordinary edge; its `/5`
steps remain exactly the unproved pointwise closure uses.

## What would actually finish this route

The direct five-lift plan needs a recursion that preserves a supplied
antecedent path while terminating on every positive odd unit. GCL-001 and
GCL-002 show why neither a short antecedent path nor one uniform commutator
per inverse edge supplies that recursion. The inverse-pressure alternative
needs the uniform quantitative estimate in (5), together with other-component
coverage. No argument in this investigation establishes either closing step.
