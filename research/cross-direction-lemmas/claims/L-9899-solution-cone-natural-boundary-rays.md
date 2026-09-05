# L-9899 -- Extreme solution-cone rays have a rational/natural-boundary dichotomy

Claim ID: `L-9899`
Title: Analytic continuation of the distinguished component ray is equivalent to the Collatz conjecture
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: `gpt56-synthesis-01-p`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: the standard Polya--Carlson theorem for the natural-boundary conclusion; source directions Issue #24/T-9702 and local L-9823 are rederived below
Scope: the nonnegative fixed cone of the shortcut Collatz pullback on `ell^infinity(N_0)`
Related counterexample candidates: none

## Setup

Let

\[
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2
\end{cases}
\qquad(n\in\mathbb N_0)
\tag{1}
\]

be the shortcut Collatz map, with `T(0)=0`.  Let `G` be its functional
graph, and let `mathcal C` denote the weak components of `G`.  On real
bounded sequences define

\[
(Fa)_n=a_{T(n)},
\qquad
K=\{a\in\ell^\infty(\mathbb N_0):Fa=a, a_n\ge0\}.
\tag{2}
\]

For a component `C`, write `1_C` for its indicator and

\[
f_C(z)=\sum_{n\in C}z^n
\qquad(|z|<1).
\tag{3}
\]

The component of `1` is denoted by `C_1`.  The singleton `{0}` is always a
component, and every other component is contained in the positive integers.

An extreme ray of `K` is called **rational**, respectively
**natural-boundary**, when the generating series of one (equivalently every)
nonzero spanning vector is rational, respectively has the unit circle as a
natural boundary.

## Statement 1 -- independent extreme-ray classification

The fixed cone is exactly the cone of nonnegative component-constant
sequences:

\[
\boxed{
K=\left\{\sum_{C\in\mathcal C}c_C1_C:
0\le c_C\le M\text{ for some }M<\infty\right\}.
}
\tag{4}
\]

The sum in (4) is pointwise: exactly one term is nonzero at each coordinate.
Its extreme rays are precisely

\[
\boxed{\mathbb R_{\ge0}1_C\qquad(C\in\mathcal C).}
\tag{5}
\]

This statement does not assume that the collection of components is finite.

## Statement 2 -- analytic classification of every extreme ray

The zero-component ray has

\[
f_{\{0\}}(z)=1.
\tag{6}
\]

For every positive component `C`, exactly one of the following alternatives
holds:

\[
\begin{array}{ll}
\text{full positive component:}
&C=\mathbb Z_{>0},\quad f_C(z)=\dfrac{z}{1-z};\\[6pt]
\text{proper positive component:}
&\partial\mathbb D\text{ is a natural boundary of }f_C.
\end{array}
\tag{7}
\]

In the second alternative `f_C` is neither rational, algebraic, nor
D-finite over `C(z)`.

## Statement 3 -- exact analytic equivalents of Collatz

The following are equivalent.

1. Every positive integer reaches the cycle `{1,2}`.
2. `C_1=Z_{>0}`.
3. `f_{C_1}(z)=z/(1-z)`.
4. `f_{C_1}` analytically continues through some nonempty open arc of the
   unit circle.
5. `K` has a rational extreme ray other than the isolated ray
   `R_{>=0}1_{\{0\}}`.
6. No extreme ray of `K` has a natural-boundary generating series.

Equivalently, the rational extreme-ray count has the sharp dichotomy

\[
\boxed{
\#\{\text{rational extreme rays of }K\}
=
\begin{cases}
2,&\text{if Collatz holds},\\
1,&\text{if Collatz fails}.
\end{cases}}
\tag{8}
\]

If Collatz fails, every positive component ray -- including the distinguished
`C_1` ray -- has a natural boundary.  The theorem does not distinguish
whether an extra component contains a nontrivial cycle or a divergent orbit.

## Proof

### Step 1 -- weak components are grand orbits

For a map with one outgoing edge at every vertex, two vertices lie in the
same weak component exactly when their forward orbits meet.  In the present
notation,

\[
m\sim n
\quad\Longleftrightarrow\quad
T^j(m)=T^k(n)\text{ for some }j,k\ge0.
\tag{9}
\]

Indeed, the relation on the right is an equivalence relation containing every
edge pair `(n,T(n))`, so it contains weak connectivity.  Conversely, equality
of two forward iterates gives an undirected path through their common image.

If `Fa=a`, then `a_n=a_{T^j(n)}` for every `j`.  Equation (9) therefore makes
`a` constant on every weak component.  The converse is immediate because
`n` and `T(n)` lie in the same component.  This proves the description (4).

### Step 2 -- extreme rays

For every component `C`, the indicator `1_C` lies in `K`.  Suppose

\[
1_C=u+v,
\qquad u,v\in K.
\tag{10}
\]

Both `u` and `v` are component-constant.  On `C` they therefore have constant
values `alpha,beta>=0` with `alpha+beta=1`; on every other component their
two nonnegative values sum to zero.  Hence

\[
u=\alpha1_C,
\qquad
v=(1-\alpha)1_C,
\tag{11}
\]

so `R_{>=0}1_C` is extreme.

Conversely, let `a` in `K` be nonzero and have positive values on two
distinct components `C` and `D`.  Splitting off the `C` coefficient in (4)
gives

\[
a=c_C1_C+\bigl(a-c_C1_C\bigr),
\tag{12}
\]

where both summands lie in `K`, are nonzero, and neither is proportional to
`a`.  Thus `a` does not span an extreme ray.  A vector supported on exactly
one component is a positive scalar multiple of its indicator.  This proves
(5).

### Step 3 -- every positive component is infinite

First, `T^{-1}(0)={0}`, so `{0}` is an isolated weak component.  If
`C!=\{0\}` and `n in C`, then `n>=1` and

\[
T^k(2^kn)=n
\qquad(k\ge0).
\tag{13}
\]

Consequently `2^kn in C` for every `k`; in particular `C` is infinite and
the series `f_C` has radius of convergence exactly one.

### Step 4 -- periodic rigidity for component indicators

We prove the arithmetic input rather than importing it.  Let

\[
s_n=1_C(n)\qquad(n\ge1)
\tag{14}
\]

for a positive component `C`.  Constancy across Collatz edges gives

\[
s_{2m}=s_m\quad(m\ge1),
\qquad
s_{2m+1}=s_{3m+2}\quad(m\ge0).
\tag{15}
\]

Assume that `s` is eventually periodic with period `p`.  On sufficiently
large representatives, its tail defines a function

\[
h:\mathbb Z/p\mathbb Z\longrightarrow\{0,1\}
\tag{16}
\]

satisfying

\[
h(2x)=h(x),
\qquad
h(2x+1)=h(3x+2).
\tag{17}
\]

If `p=2q`, then

\[
h(x+q)=h(2x+2q)=h(2x)=h(x),
\tag{18}
\]

so the period loses one factor of two.  Repeat until the period is odd.  Now
substitute `x=(y-1)/2` in the second identity of (17) and use the first:

\[
h(y)=h(3y+1).
\tag{19}
\]

If the remaining period is `p=3q`, equation (19) gives

\[
h(x+q)=h(3x+3q+1)=h(3x+1)=h(x),
\tag{20}
\]

so all factors of three can also be removed.  We may therefore assume
`gcd(p,6)=1`.

On `Z/pZ`, let

\[
A(x)=2x,
\qquad
B(x)=3x+1.
\tag{21}
\]

They are bijections, and (17),(19) make `h` invariant under `A`, `B`, and
their inverses.  Their affine commutator produces translation by one:

\[
(ABA^{-1})B^{-1}(x)=x+1.
\tag{22}
\]

Thus `h` is constant.  The original sequence is eventually constant; for any
fixed `n>=1`, choose `k` so that `2^kn` lies in that tail.  Equation (15)
then gives

\[
s_n=s_{2^kn},
\tag{23}
\]

so `s` is constant on all positive indices.  Since `C` is nonempty, this
constant is one and

\[
C=\mathbb Z_{>0}.
\tag{24}
\]

We have proved the sharp rigidity statement

\[
\boxed{
1_C\text{ is eventually periodic on }\mathbb Z_{>0}
\quad\Longleftrightarrow\quad
C=\mathbb Z_{>0}.
}
\tag{25}
\]

### Step 5 -- Polya--Carlson

A rational power series whose coefficients lie in a finite set is eventually
periodic: its denominator supplies a fixed finite-state linear recurrence.
Hence (25) shows that the series of a proper positive component is not
rational.

Its coefficients are integers and its radius is one by Step 3.  The
Polya--Carlson theorem now gives the alternative: it is rational or the unit
circle is a natural boundary.  The rational branch has just been excluded,
which proves (7).  A function algebraic over `C(z)` has only finitely many
branch singularities, and a D-finite germ has singularities only among the
finitely many zeros of the leading polynomial of its differential equation.
Neither can have every point of the unit circle as a barrier to continuation.

### Step 6 -- equivalences

By (9), a positive integer is in `C_1` exactly when some iterate reaches the
cycle `{1,2}`.  Thus Statements 1 and 2 of the equivalence list agree.
Statement 2 is equivalent to Statement 3 by (3).

The rational function `z/(1-z)` continues through every unit-circle arc not
containing `1`, whereas the alternative in (7) continues through none.  This
proves the equivalence with Statement 4.

By the extreme-ray classification, every nonzero non-isolated ray is the ray
of a positive component.  The analytic dichotomy (7) therefore proves the
equivalence with Statements 5 and 6 and the count (8).  QED

## Source-direction audit

- The solution-cone packet on the head of issue #24's source branch states the
  component/extreme-ray classification as its unreviewed `T-9702`.  Steps 1
  and 2 above independently reconstruct the needed result; no confidence
  label or proof step is imported.
- `L-9823` in this packet proves periodic rigidity for arbitrary finite-valued
  component colorings.  Step 4 repeats the indicator case in full so that the
  bridge is self-contained.
- The new content is the synthesis (7)--(8): every positive extreme ray is
  analytically classified, and continuation of the distinguished `C_1` ray
  is an exact Collatz equivalent.
- Only the natural-boundary conclusion invokes the external
  Polya--Carlson theorem.  The extreme-ray and eventual-periodicity parts are
  elementary.

## Gap and scope audit

- This is an equivalent reformulation, not a proof that `f_{C_1}` continues
  across an arc.  Establishing such continuation remains as hard as proving
  that every positive integer belongs to `C_1`.
- Natural-boundary behavior separates the conjectural two-component graph
  from every graph with an extra positive component.  It does **not** separate
  a nontrivial-cycle component from a cycle-free divergent component.
- The theorem concerns extreme rays, whose coefficients are binary.  It does
  not classify generating series of arbitrary points of `K`, whose component
  coefficients may take infinitely many values and need not satisfy the
  integer-coefficient hypothesis of Polya--Carlson.
- The index `0` is exceptional.  Its indicator is the polynomial `1`; omitting
  it would make the rational-ray count in (8) wrong.
- A natural boundary is compatible with automatic coefficient sequences.
  Nothing here excludes binary-automatic proper components or a regular
  sanctuary language.

## Adversarial checks

- The radius-one claim uses infinitely many actual members `2^kn` of each
  positive component, not an unproved density assertion.
- Inverting the affine maps modulo `p` occurs only after every factor of `2`
  and `3` has been removed from the period.
- Eventual tail constancy is promoted to all positive indices only through
  the exact doubling identity in (15).
- Failure of Collatz makes `C_1` proper because another positive component
  exists; it does not merely assert that some unnamed component is proper.
- Scaling a ray multiplies its generating series by a nonzero constant, which
  preserves rationality and the natural-boundary property.

## Suggested next attack

The distinguished ray criterion reduces the analytic program to a concrete
question: prove or refute continuation of `f_{C_1}` through one specified arc.
Any proposed transfer-operator or weighted-Hilbert argument should therefore
produce an actual boundary regularity estimate for this binary series, rather
than only a spectral statement about an ambient space.
