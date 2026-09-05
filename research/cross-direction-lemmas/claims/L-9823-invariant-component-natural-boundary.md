# L-9823 — Periodic rigidity and natural boundary for invariant components

Claim ID: `L-9823`  
Title: Every finite-valued nonconstant Collatz-component coloring has a natural-boundary generating series  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: the Pólya--Carlson theorem for the analytic conclusion; the periodic rigidity is elementary  
Scope: finite-valued colorings of positive shortcut-Collatz weak components  
Source-direction audit: reconstructs the invariant-component lead recorded without proof in `PR6`  
Related counterexample candidates: none

## Definitions

Let the shortcut Collatz map on positive integers be

\[
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\tag{1}
\]

Let `S` be a finite subset of the integers. A sequence

\[
s=(s_n)_{n\ge1},
\qquad s_n\in S,
\tag{2}
\]

is a **component coloring** when it is constant across every shortcut edge.
Equivalently,

\[
\boxed{
s_{2m}=s_m\quad(m\ge1),
\qquad
s_{2m+1}=s_{3m+2}\quad(m\ge0).
}
\tag{3}
\]

Its ordinary generating series is

\[
F_s(z)=\sum_{n\ge1}s_nz^n.
\tag{4}
\]

An indicator of any union of weak components is the special case
`S={0,1}`. The index starts at `1`; the isolated fixed point `0` of the
nonnegative extension is deliberately excluded.

## Statement

### 1. Periodic rigidity

Every eventually periodic component coloring is constant:

\[
\boxed{
s_{n+p}=s_n\text{ for all sufficiently large }n
\quad\Longrightarrow\quad
s_n=c\text{ for every }n\ge1.
}
\tag{5}
\]

This conclusion is purely arithmetic and does not assume that positive
Collatz orbits converge.

### 2. Rational-series rigidity

The finite-valued integer series (4) is rational over `Q(z)` if and only if
the coloring is constant. In that case

\[
F_s(z)=\frac{cz}{1-z}.
\tag{6}
\]

### 3. Natural-boundary dichotomy

If the coloring is nonconstant, then `F_s` has radius of convergence exactly
one and the unit circle is a natural boundary. Consequently

\[
\boxed{
F_s(z)\text{ is neither rational, algebraic, nor D-finite over }\mathbb C(z).
}
\tag{7}
\]

In particular, the indicator series of a nonempty proper union of positive
weak components, if such a union exists, has a natural boundary.

The statement does **not** exclude automatic component colorings. A finite
alphabet automatic sequence can have a non-D-finite complex generating series
with the unit circle as a natural boundary.

### 4. Finite-quotient and Presburger corollaries

Every component coloring that factors through a finite congruence quotient is
constant. Consequently, if a union `X` of positive weak components is any of

- ultimately periodic;
- semilinear in one dimension;
- definable in Presburger arithmetic; or
- regular when integers are written in unary,

then

\[
\boxed{X=\varnothing\quad\text{or}\quad X=\mathbb Z_{>0}.}
\]

This unary/Presburger conclusion does not apply to a regular language of
canonical binary expansions.

## Proof

### Period reduction

Assume `s` is eventually periodic with some period `p>=1`. On sufficiently
large indices, its value depends only on the residue modulo `p`; write the
resulting function as

\[
f:\mathbb Z/p\mathbb Z\longrightarrow S.
\tag{8}
\]

Choosing arbitrarily large representatives in (3) gives, for every residue
`x`,

\[
f(2x)=f(x),
\qquad
f(2x+1)=f(3x+2).
\tag{9}
\]

If `p=2q`, the first identity implies

\[
f(x+q)=f(2x+2q)=f(2x+p)=f(2x)=f(x).
\tag{10}
\]

Thus `f` factors through reduction modulo `q`. Repeating (10) removes the
entire power of two from the period, so assume now that `p` is odd.

Because `2` is invertible modulo `p`, substitute
`x=(n-1)/2` into the second identity of (9). The first identity then gives

\[
f(n)
=f\!\left(\frac{3n+1}{2}\right)
=f(3n+1).
\tag{11}
\]

If `p=3q`, equation (11) yields

\[
f(x+q)
=f(3x+3q+1)
=f(3x+p+1)
=f(3x+1)
=f(x).
\tag{12}
\]

Hence `f` also factors through the period with its full power of three
removed. It remains to treat a period satisfying

\[
\gcd(p,6)=1.
\tag{13}
\]

### Translation generation

On `Z/pZ`, define the two bijections

\[
A(x)=2x,
\qquad
B(x)=3x+1.
\tag{14}
\]

Equations (9) and (11) say that `f` is invariant under `A` and `B`, hence also
under their inverses and every element of the group they generate. Now

\[
ABA^{-1}(x)=3x+2,
\tag{15}
\]

and therefore

\[
(ABA^{-1})B^{-1}(x)=x+1.
\tag{16}
\]

So `f` is invariant under translation by one and is constant on `Z/pZ`.
The eventual tail of `s` is therefore constant, say equal to `c`.

For an arbitrary `n>=1`, choose `k` with `2^kn` in that constant tail.
Repeated use of the first recurrence in (3) gives

\[
s_n=s_{2^kn}=c.
\tag{17}
\]

This proves (5). It also proves part 4, because each listed one-dimensional
description has an ultimately periodic indicator; a coloring through a fixed
finite congruence quotient is periodic from the start.

### Generating series

A rational power series whose coefficients lie in a finite set is eventually
periodic. One elementary proof uses the fixed-order linear recurrence supplied
by its denominator: only finitely many coefficient state vectors occur, and
the deterministic recurrence makes the tail periodic. Part 1 then makes the
coloring constant. Conversely, a constant coloring gives (6). This proves
part 2.

Suppose next that `s` is nonconstant. It is bounded. It also has infinitely
many nonzero terms: if `s_n!=0`, then (3) gives
`s_(2^kn)=s_n` for every `k`. Hence the Cauchy--Hadamard formula gives radius
of convergence exactly one.

The Pólya--Carlson theorem says that an integer-coefficient power series of
radius one is either rational or has the unit circle as a natural boundary.
Part 2 excludes the rational alternative. An algebraic function has only
finitely many branch singularities, and a D-finite germ has no singularities
away from the finite zero set of the leading polynomial of its differential
equation. Neither can have the unit circle as a natural boundary. This proves
(7). QED

## Motivation

An invariant positive component would be a natural host for a divergent orbit
or nontrivial cycle. The termination-frontier packet recorded, as unadmitted
provenance, that such a component cannot have a simple rational or D-finite
indicator series. The present lemma supplies the missing proof in a compact
form and strengthens its arithmetic core: even eventual periodicity alone is
impossible unless every positive integer receives the same color.

The proof is useful beyond generating functions. Equations (10)--(16) show
exactly why every finite cyclic quotient loses component information: the
binary and ternary affine edges generate a unit translation after their
noninvertible prime-power parts are removed.

## Dependency audit

- The component recurrences (3) follow directly from the two branches of (1).
- Period reduction and translation generation are elementary and are fully
  proved above; no result from `PR6` is imported as a theorem.
- Only the natural-boundary conclusion uses Pólya--Carlson.
- The algebraic and D-finite exclusions use their standard finite-singularity
  property.

## Gap audit

- The lemma does not prove that the positive Collatz graph has one weak
  component. It proves only that a finite-valued coloring of multiple
  components cannot be eventually periodic.
- Natural boundary is a complexity obstruction, not evidence that a proper
  component exists.
- An automatic sequence need not have a rational or D-finite complex
  generating function; automatic component descriptions remain open.
- Binary regularity is equivalent to automaticity, not unary regularity. The
  Presburger corollary must not be used to dismiss the PR #12 sanctuary search.
- The conclusion concerns unary index generating series, not finite
  transducers reading richer orbit certificates.
- Including index `0` creates the exceptional rational coloring supported
  only at `{0}`. Starting at positive indices is essential.

## Adversarial tests

- Periods divisible by `2` or `3` cannot be treated by inverses modulo `p`.
  Equations (10) and (12) remove those factors before the group argument.
- Eventual constancy is promoted to global positive constancy only through
  the exact doubling recurrence (17).
- A bounded nonconstant integer sequence can be a polynomial if it has finite
  support. Component recurrence (3) rules this out on positive indices by
  propagating every nonzero value along its doubling ray.
- The coloring `s_0=1,s_n=0` for `n>=1` is a counterexample if zero is
  included. It is outside the stated positive scope.
- Pólya--Carlson cannot be applied to an arbitrary finite-valued complex
  alphabet without first encoding it integrally. The claim assumes
  `S subset Z`.

## Remaining uncertainty

None in periodic rigidity. The analytic conclusion depends on the standard
Pólya--Carlson theorem. The existence and descriptive complexity of a proper
positive invariant component remain completely open.

## Suggested next attack

Study automatic colorings directly through the `2`-kernel. Combine
`s_(2m)=s_m` with `s_(2m+1)=s_(3m+2)` to ask whether a finite `2`-kernel also
forces translation invariance. A positive answer would rule out every binary
`2`-automatic proper component and would be strictly stronger than the present
periodic theorem.
