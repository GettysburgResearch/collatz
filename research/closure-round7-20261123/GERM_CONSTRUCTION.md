# Exact arithmetic transport of the actual Taylor jets

23 November 2026. Parent checkpoint:
`e4367dd2c4406c1041e66d82dfba822908747fa3`.

**Status: finite arithmetic transport proved, with a Lean-checked coefficient
core. The actual rational germ is not constructed for an arbitrary positive
source. Full Collatz remains open.**

This attack starts at the missing construction in the previous round: the
literal binary Taylor expansion of the weighted parity series. It gives an
exact denominator clock for every finite jet, an all-order prefix identity,
and a formal proof that an actual tail cannot create a new denominator
prime other than three. These are arithmetic statements about one fixed
source, rather than a replacement closure hypothesis.

## 1. The actual coefficients and their unconditional binary integrality

Use the shortcut map `T(x)=x/2` for even `x` and `(3x+1)/2` for odd `x`.
For one fixed positive ordinary integer `n`, write

\[
x_N=T^N(n),\qquad e_N=x_N\bmod 2,\qquad
p_N=\sum_{k<N}e_k,
\]
\[
B_n(z)=\sum_{k\ge0}e_k3^{-p_{k+1}}z^k,
\qquad J_n(t)=B_n(2+t)=\sum_{j\ge0}c_j(n)t^j.
\tag{1}
\]

These are the literal binary analytic functions. In particular,

\[
c_j(n)=\sum_{k\ge j}e_k\binom{k}{j}
        2^{k-j}3^{-p_{k+1}}\in\mathbb Z_2.
\tag{2}
\]

For fixed `j`, the terms tend to zero in `Q_2` at least as fast as
`2^(k-j)`. Every term is binary integral, so the sum is binary integral.
Expanding on a closed binary disc of radius less than one justifies
coefficientwise translation. The full affine orbit identity gives
`c_0(n)=-n`.

Nothing here says that `c_j(n)` is rational. This is the first remaining
construction problem, already for `j=1`.

## 2. A prefix identity at every Taylor order

Define the integer binomial-moment carries of the **actual chronological
prefix** by

\[
C_j(N)=\sum_{k<N}e_k\binom{k}{j}2^k
                      3^{p_N-p_{k+1}}.
\tag{3}
\]

The convention is `binom(k,j)=0` for `j>k`. Thus `C_0(N)` is the complete
ordinary affine carry, and

\[
C_j(N+1)=3^{e_N}C_j(N)+e_N\binom Nj2^N.
\tag{4}
\]

**R7-GERM-1 (all-order, same-source prefix identity).** For every `N,j`,

\[
\boxed{
2^j3^{p_N}c_j(n)-C_j(N)
=2^N\sum_{i=0}^j\binom{N}{j-i}2^i c_i(x_N).
}
\tag{5}
\]

This equality holds in `Q_2` without assuming rationality, density,
periodicity, or convergence of the orbit. To prove it, split (1) after
the first `N` terms:

\[
J_n(t)=\sum_{k<N}e_k3^{-p_{k+1}}(2+t)^k
       +3^{-p_N}(2+t)^N J_{x_N}(t).
\tag{6}
\]

Take the coefficient of `t^j` and multiply by `2^j3^(p_N)`. The finite
part is exactly (3), and the tail is the right side of (5).

The entire right side of (5) is divisible by `2^N` in `Z_2`. If the
initial coefficients happen to be rational, (5) consequently gives
simultaneous binary approximations by the integer carries. It does not
bound the ordinary sizes or ternary valuations of those carries.
Discarding the tail terms would discard the obstruction that must be
controlled in a Diophantine approximation argument.

## 3. Each odd step clears exactly one ternary denominator layer

The one-step version of (6) is

\[
(2+t)J_{Tx}(t)=3^eJ_x(t)-e,\qquad e=x\bmod2.
\tag{7}
\]

If `a_j=c_j(x)` and `b_j=c_j(Tx)`, its coefficient equations are

\[
2b_0=3^ea_0-e,\qquad
2b_{j+1}=3^ea_{j+1}-b_j.
\tag{8}
\]

**R7-GERM-2 (exact finite-jet denominator clock).** Suppose the first
`r+1` coefficients of the actual germ are rational numbers in `Z[1/3]`.
Let

\[
S_r(n)=\max_{0\le j\le r}
       v_3\bigl(\operatorname{den}(c_j(n))\bigr),
\tag{9}
\]

where denominators are positive and reduced. Then the corresponding
coefficients at every actual tail are still in `Z[1/3]`, and

\[
\boxed{S_r(x_N)=\max\{S_r(n)-p_N,0\}.}
\tag{10}
\]

**Proof of preservation of the coefficient ring.** The triangular
recurrence (8) first puts the rational tail coefficients in `Z[1/6]`.
Their unconditional binary integrality from (2) removes the powers of
two in their reduced denominators. Thus they are in `Z[1/3]`.

**Proof of the exact exponent.** Truncated multiplication by `2+t` is
an invertible triangular linear map over `Z_3`, with constant diagonal
entry two. Its inverse also has entries in `Z_3`. It preserves the
minimum ternary valuation of a finite coefficient vector and therefore
the maximum exponent of three in its denominators. An even step in
(7) leaves this exponent unchanged. At an odd step the vector is
multiplied by three and an ordinary integer is subtracted only from
the constant coordinate. If its maximum denominator exponent exceeds
one, the negative minimum valuation increases by exactly one; an
integer cannot cancel a term with negative valuation. If the exponent
is zero or one, every resulting coefficient is ternary integral, so
the new exponent is zero. This proves the one-step law and then (10)
by iteration. Square.

In particular, after `S_r(n)` actual odd steps, all of this finite jet
consists of ordinary integers. A positive ordinary orbit has infinitely
many odd steps: an eventually even orbit would repeatedly halve a fixed
positive integer forever. Thus the clearing time exists under the
explicit rationality and coefficient-ring hypothesis. Its ordinary
shortcut time is not bounded by (10).

The Lean module proves the sufficient clearing direction of (10)
coefficient by coefficient. The exact valuation equality is the written
argument above; it is not represented as a formal valuation theorem in
the module.

## 4. What a positive ternary radius actually supplies

Let `J3` mean the preceding round's full actual-germ hypothesis:
rational coefficients in `Z[1/3]`, with positive complex and ternary
convergence radii. Its ternary radius alone gives source-dependent
constants `A,B>=0` such that

\[
S_r(n)\le Ar+B.
\tag{11}
\]

Indeed choose any positive radius smaller than the ternary radius of
convergence. The coefficient norms times that radius to the power `j`
are bounded; taking base-three logarithms bounds the denominator
exponents linearly. Combining (10) and (11) shows that a linearly
increasing number of odd steps clears jets of increasing order.

This does **not** supply one common denominator for the whole germ.
Positive radius permits denominator exponents growing linearly with
the order. Even radius one permits sublinear unbounded growth. If a
single `3^s` cleared all coefficients, then after `s` odd steps the
whole actual germ would lie in `Z[[t]]`; this is a stronger arithmetic
hypothesis. A ternary radius strictly greater than one would imply
such a common bound, because all sufficiently high coefficients would
be ternary integral. None of these stronger properties is constructed
here for an arbitrary positive source.

The output of this mechanism is therefore precise: integer Taylor
jets appear farther along the same orbit if the initial rational
germ exists. It does not by itself compare two ordinary orbit values
or force their equality.

## 5. Every other denominator prime is exactly invariant

Fix a prime `ell` other than two and three. The prefix polynomial in
(6) is integral over `Z_(ell)`, and `(2+t)^N/3^(p_N)` is a formal unit
over that ring. Consequently, for every finite `r`,

\[
c_0(n),\ldots,c_r(n)\in\mathbb Z_{(\ell)}
\quad\Longleftrightarrow\quad
c_0(x_N),\ldots,c_r(x_N)\in\mathbb Z_{(\ell)}.
\tag{12}
\]

Here the coefficients under discussion must be rational; rationality
of one finite jet transports to the other by (8). Thus the first order
at which `ell` occurs in a reduced denominator cannot be hidden by an
actual preperiod. This holds without density or periodicity assumptions.

The formal theorem `jet_subring_iff` proves the more general one-step
version for any rational subring containing `1/2` and `1/3`. Iteration
gives (12). The companion [FINITE_JET_BOUND.md](FINITE_JET_BOUND.md)
combines this invariance with a resultant bound for a specified eventual
cycle. The finite clearing law removes the only permitted denominator
prime; the resultant detector concerns the prohibited primes. Neither
constructs the initial jet.

## 6. The direct construction attempt and its exact missing step

At first order, writing `d(x)=c_1(x)` in (8) gives

\[
2d(Tx)=3^ed(x)+Tx,
\qquad
\frac{d(Tx)}{Tx}
=\frac{3^ex}{3^ex+e}\frac{d(x)}x+\frac12.
\tag{13}
\]

The linear part retains the original Collatz multiplier. There is no
uniform complementary contraction in this recurrence. The denominator
clock shows what would happen to a triadic rational derivative; it
does not establish its rationality. Nor can one force a contradiction
by asserting positivity or nonvanishing of this derivative: the actual
convergent source `85` has `c_1(85)=0`.

At higher fixed order, (5) supplies the exact integer forms to which a
simultaneous approximation theorem would have to apply. The factors
`binom(k,j)` add moment height while the guaranteed binary precision is
still `2^N`. A proof needs an additional strict saving in the relevant
height product, or another genuinely arithmetic restriction on these
particular carries. Their ternary valuations and any binary precision
beyond (5) remain uncontrolled. We have not proved that such a saving
is impossible. Increasing the jet order with `N` also changes the
dimension, so a theorem for one fixed dimension cannot silently be
applied to that changing family.

The strongest unsupported step remains: construct rational coefficients
for the literal germ (1), starting with `c_1(n)`, and control their
denominators and analytic growth from ordinary orbit data. Equations
(5), (10), and (12) give exact constraints for that construction, not
a substitute for it.

## 7. Formal and computational boundaries

`GermConstruction.lean` has seven public theorems in namespace
`Collatz.ClosureRoundSeven.GermConstruction`:

| Theorem | Checked content |
| --- | --- |
| `binaryIntegral_int_mul` | Integer multiplication preserves an odd reduced denominator. |
| `integral_of_double` | A binary-integral rational with integral double is integral. |
| `triangular_integrality` | Binary integrality removes all apparent powers of two in finite division by `2+t`. |
| `even_step_cleared` | An even step preserves a common ternary denominator for a complete finite jet. |
| `odd_step_cleared` | An odd step removes one ternary denominator layer from a complete finite jet. |
| `odd_step_integral` | An odd step preserves an already integral finite jet. |
| `jet_subring_iff` | Finite coefficient-ring membership is equivalent before and after an actual step, when two and three are units. |

The inputs explicitly include rational coefficient sequences, the
actual triangular identities, and binary integrality where needed.
The module proves the arithmetic consequences of those equations. It
does not formalize the analytic definition (1), prove arbitrary
coefficients rational, or infer convergence from finite data.

`germ_controls.py` computes exact rational jets backwards from the
known standard tail `J_1(t)=-1/(1+4t+t^2)`. It independently checks
the literal orbit, the carry recursion and direct carry sum, every
tested instance of (5), and the exact denominator clock (10).
These are replay controls on explicitly convergent sources, including
long excursions; they are not evidence that all positive sources have
rational Taylor coefficients. Explicit checks remain active under
`python -O`.

The development module compiled with Lean 4.34.1 and mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`, with
`warningAsError=true` and `autoImplicit=false`. The packet-level report
records the independent fresh build, theorem audit, and replay totals.

## 8. Exact source refresh and imported scope

The actual-germ definitions and `J3` boundary come from PR182 at the
parent checkpoint, path
`research/profound-round6-20261123/RATIONAL_SELECTION.md`, Git blob
`54d7949ac80ec6b8286f0d03d579f9f6e0efe95f`. Its Sections 1--2 and the
actual-germ construction boundary are used here. The present finite
arithmetic proofs do not use an analytic rationality consumer.

The following upstream heads were refreshed for this attack:

| PR and exact head | Reading and scope |
| --- | --- |
| PR175 `67664c6bf555bf7f7fcec987acb79500071dce4b` | Metadata plus complete `research/lean-global-closure-20261121/risk26/README.md` and `research/lean-global-closure-20261121/risk26/triadic/FIXED_SOURCE_GLUING_BOUNDARY.md`. The source warns that distinct completions cannot be identified from an algebraic expression alone, and that the canonical fixed-source product has no strict height saving. Neither warning is promoted to a theorem excluding other constructions. |
| PR178 `398b3a04da071e96362005792417bd5cf8cc6497` | Refreshed metadata; no head advance from round six. Its analytic germ consumer is not invoked to prove (5), (10), or (12). |
| PR180 `7cfd911d35382d9d3bc988060ba88ade78a4267e` | Refreshed metadata; no head advance from round six. No neighboring route is treated as a proved universal entrance or descent theorem. |

No external literature theorem is imported into this finite arithmetic
module. The unresolved Diophantine approximation question in Section 6
is deliberately retained as an open construction step.
