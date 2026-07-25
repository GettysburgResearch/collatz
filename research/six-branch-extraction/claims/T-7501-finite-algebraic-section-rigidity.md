# T-7501 — Finite algebraic-section rigidity

Claim ID: `T-7501`  
Title: Every finite algebraic or semialgebraic exact self-section of the complete six-branch tree is the original forward map  
Status: `PROPOSED`  
Authoring agent: `gpt56-breakthrough-01`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: `D-7401`, `T-7402`; the elementary Newton–Puiseux consequence proved below  
Scope: finite-control algebraic branches defined on an ordinary tail and carrying the complete labeled six-branch subtree  
Related counterexample candidates: none

## Statement

Use the exact quotient transition of `D-7401`:

\[
Qk'=Pk+c_i-r_j,
\qquad
P=3^{12}>Q=2^{19},
\qquad 0\le i,j\le5.
\tag{1}
\]

For every ordered pair `i -> j`, write the exact child cylinder as

\[
k=\kappa_{ij}+Qt,
\qquad
k'=\lambda_{ij}+Pt,
\qquad t\in\mathbf Z_{\ge0}.
\tag{2}
\]

Let `Omega` be finite.  For every reachable state `(omega,i)`, let

\[
f_{\omega,i}
\]

be one single-valued algebraic branch over `Q(X)`, real analytic on some ray
`(R_(omega,i),infinity)`, such that

\[
f_{\omega,i}(n)\in\mathbf Z_{>0}
\]

for every sufficiently large integer `n`.

Assume that every state carries all six children.  For every child type `j`, let
`omega'=tau(omega,i,j)` be the successor control state, and permit an initially
arbitrary permutation `pi_(omega,i)` of the six physical labels.  Require the
exact section identity

\[
\boxed{
Q f_{\omega',j}(\lambda_{ij}+Pt)
=
P f_{\omega,i}(\kappa_{ij}+Qt)
+a_{\pi_{\omega,i}(j)}}
\tag{3}
\]

for every sufficiently large integer `t`.

Then every branch is an ordinary affine polynomial and, on every reachable
component,

\[
\boxed{
f_{\omega,i}(X)=PX+c_i,
\qquad
\pi_{\omega,i}(j)=j.}
\tag{4}
\]

Consequently:

1. finite control plus radicals, algebraic curves, algebraic power series,
   piecewise-algebraic formulas, or any other tail algebraic coordinate does
   not produce a contracting ordinary self-section;
2. every finite semialgebraic exact self-section also collapses to `(4)`;
3. the only finite algebraic nucleus carrying the complete six-branch tree is
   the original expanding forward boundary map.

This is an all-depth architecture theorem.  It does not assume or extrapolate
from a finite search.

## Lemma 1 — an algebraic branch integral on a full tail is a polynomial

Let `f` be a single-valued algebraic branch over `Q(X)`, real analytic for all
sufficiently large positive real `X`.  If

\[
f(n)\in\mathbf Z
\]

for every sufficiently large integer `n`, then

\[
\boxed{f\in\mathbf Q[X].}
\tag{5}
\]

### Proof

At infinity an algebraic branch has a convergent Newton–Puiseux expansion on a
sufficiently narrow sector containing the positive ray:

\[
f(X)=\sum_{m\le M} c_m X^{m/e},
\tag{6}
\]

for some positive integer `e`; the exponents are bounded above and tend to
`-infinity`.  Put

\[
\rho=M/e.
\]

Choose an integer `d>rho`.  The `d`-th forward difference is

\[
\Delta^d f(n)
=
\sum_{h=0}^{d}(-1)^{d-h}{d\choose h}f(n+h).
\tag{7}
\]

For one power `X^alpha`, standard finite-difference cancellation gives

\[
\Delta^d X^\alpha=O(X^{\alpha-d}).
\tag{8}
\]

The Puiseux expansion converges normally on a tail of the positive ray, so it
may be differenced term by term there.  The leading exponent in `(7)` is at
most `rho-d<0`.  Hence

\[
\boxed{\Delta^d f(n)\longrightarrow0.}
\tag{9}
\]

Every value in `(7)` is an integer.  Therefore

\[
\Delta^d f(n)=0
\]

for all sufficiently large integers `n`.

Discrete summation now gives a polynomial `p in Q[X]`, of degree at most
`d-1`, for which

\[
f(n)=p(n)
\]

at every sufficiently large integer.  Explicitly, after one late index `N`,

\[
p(X)=\sum_{r=0}^{d-1}\Delta^r f(N){X-N\choose r}.
\tag{10}
\]

The algebraic branch `f-p` has infinitely many zeros tending to infinity.  If
it were nonzero, its own Puiseux expansion at infinity would have a first
nonzero term and could not vanish at every sufficiently large integer.
Therefore `f-p` is identically zero on the tail branch.  Algebraic continuation
gives `(5)`. ∎

## Lemma 2 — finite algebraic section cycles force degree one

Apply Lemma 1 state by state.  Write

\[
f_{\omega,i}(X)
=L_{\omega,i}X^{d_{\omega,i}}+\cdots,
\qquad L_{\omega,i}\ne0.
\tag{11}
\]

Equation `(3)` holds at infinitely many integers `t`, and both sides are now
polynomials.  It is therefore a polynomial identity.

Comparison of degrees on an edge gives

\[
d_{\omega',j}=d_{\omega,i}.
\tag{12}
\]

Comparison of leading coefficients, using `(2)`, gives

\[
Q L_{\omega',j}P^d
=
P L_{\omega,i}Q^d,
\]

or

\[
\boxed{
L_{\omega',j}
=
L_{\omega,i}\left({Q\over P}\right)^{d-1}.}
\tag{13}
\]

Every infinite path in the finite reachable control graph enters a directed
cycle.  Around a cycle of length `s`, `(13)` gives

\[
L=L\left({Q\over P}\right)^{s(d-1)}.
\]

The functions are nonconstant, `L` is nonzero, and `P!=Q`.  Hence

\[
\boxed{d=1.}
\tag{14}
\]

Degree equality propagates this conclusion back along every reachable path. ∎

## Proof of the theorem

By Lemmas 1 and 2,

\[
f_{\omega,i}(X)=v_{\omega,i}X+s_{\omega,i}.
\tag{15}
\]

Because `(15)` is an integer at every sufficiently large integer, its first
difference `v_(omega,i)` is an integer, and then one value shows that
`s_(omega,i)` is an integer.  Eventual positivity and nonconstancy force the
reachable slope to be positive.

For degree one, `(13)` says that the slope is constant on every edge.  Thus one
common positive integer scale occurs on each reachable component.  The exact
constant terms in `(3)` now satisfy precisely the arbitrary-finite-control
affine-nucleus hypotheses of `T-7402`, including state-dependent successor
control and initially arbitrary output-label permutations.

`T-7402` forces

\[
v=P,
\qquad
s_{\omega,i}=c_i,
\qquad
\pi_{\omega,i}(j)=j.
\]

This is `(4)`. ∎

## Semialgebraic corollary

Let the section coordinates instead be arbitrary semialgebraic functions on a
positive real tail, integer-valued at every sufficiently large integer.
A univariate semialgebraic graph has only finitely many cells.  On its final
unbounded cell it is a single continuous algebraic branch: its one-dimensional
semialgebraic graph is contained in an algebraic curve, and after the finitely
many branch and singular points are removed one branch remains.

Finite control absorbs the finitely many initial cells.  Lemma 1 therefore
applies on the final cell, and the preceding proof gives `(4)`.

Hence no finite semialgebraic piecewise rule—polynomial, rational, radical,
finite case split, or finite composition of such operations—can provide the
missing ordinary descent while preserving the complete six-branch language.

## Why this is stronger than rational rigidity

`T-7403` closes rational functions by a Bézout denominator argument.  The
present theorem also permits genuinely algebraic, nonrational branches before
tail integrality is imposed.  Tail integrality itself destroys every fractional
Puiseux term: a sufficiently high finite difference tends to zero but remains
an integer, so the branch must become polynomial.

Thus adding a square root, an algebraic implicit equation, or finitely many
algebraic sheets cannot evade the degree-one cycle obstruction.

## Relationship to ordinary extraction

The theorem eliminates a complete proof architecture:

```text
finite control
+ one exact algebraic ordinary coordinate per state
+ recursive reproduction of all six child cylinders
=> no nontrivial descent; only the forward map survives.
```

A successful positive proof cannot arise by enlarging the current finite
rational nucleus to a finite algebraic or semialgebraic one.  It must instead
supply at least one of:

- genuinely unbounded section information;
- a non-semialgebraic global arithmetic invariant;
- a direct height theorem proving `m_n -> infinity`;
- or one explicit all-time root.

The theorem does **not** say that every imaginable nonlinear invariant fails.
It says exactly that the entire finite algebraic bounded-memory class fails.

## Dependency audit

- `D-7401` supplies the exact child parametrization.
- The algebraic-tail-to-polynomial lemma is proved in this file from the
  Newton–Puiseux expansion at infinity and elementary finite differences.
- The degree cycle argument is reconstructed explicitly.
- `T-7402` is used only after every algebraic branch has been reduced to an
  affine integer coordinate.
- No finite computation is used.

## Gap audit

- The complete-subtree hypothesis is essential.  A single survivor could lie
  in a proper sublanguage with no six-way recursive self-copy.
- A coordinate that changes through infinitely many algebraic branches is
  unbounded-state and lies outside finite control.
- Arbitrary transcendental functions and pushdown or tape-like sections are
  not covered.
- The theorem does not decide whether the concrete least roots `m_n` diverge.
- No positive root or `K-75xx` object is produced.

## Adversarial tests

1. Algebraic branches may depend on both finite control state and current type.
2. Different states may begin with different Puiseux exponents and leading
   coefficients; edge identities and finite cycles force one common degree.
3. Successor control may depend on the chosen child.
4. Identities need hold only on the exact infinite child progression; after
   polynomial reduction, infinitely many values force polynomial identity.
5. Eventual, rather than all-input, integrality is sufficient.
6. Finitely many singularities and case boundaries are harmless because the
   theorem works on a common late tail.
7. The surviving map `PX+c_i` is checked directly and is expanding.

## Remaining uncertainty

The ordinary least-root decision remains open:

\[
\sup_n m_n<\infty
\quad\text{or}\quad
m_n\to\infty.
\]

The result sharply identifies the next acceptable positive mechanism: it must
be genuinely unbounded-state or prove a global ordinary-height statement, not
merely replace rational formulas by algebraic ones.

## Suggested next attack

Do not enlarge the finite tame-function hierarchy again.  Attack the actual
transported high boundary with an unbounded invariant, or prove direct digit
escape.  Any such invariant must be shown to bound the same initial ordinary
root; otherwise it is another completion ghost.
