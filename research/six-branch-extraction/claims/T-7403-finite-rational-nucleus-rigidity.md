# T-7403 — Finite rational-section nucleus rigidity

Claim ID: `T-7403`  
Title: Every finite rational-function self-section of the complete six-branch tree is the original forward map  
Status: `PROPOSED`  
Authoring agent: `gpt56-extraction-01`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: `D-7401`, `T-7402`  
Scope: finite-control rational-function section coordinates carrying the complete six-branch subtree  
Related counterexample candidates: none

## Statement

Use the exact six-branch system of `D-7401`:

\[
Qk'=Pk+c_i-r_j,
\qquad 0\le i,j\le5,
\tag{1}
\]

where

\[
P=3^{12},\qquad Q=2^{19},\qquad P>Q.
\]

For every ordered pair `i -> j`, let `kappa_(ij)` be the unique residue in
`{0,...,Q-1}` for which the right side of `(1)` is divisible by `Q`, and put

\[
\lambda_{ij}={P\kappa_{ij}+c_i-r_j\over Q}.
\tag{2}
\]

Thus every exact child tail has the parametrization

\[
k=\kappa_{ij}+Qt,
\qquad
k'=\lambda_{ij}+Pt,
\qquad t\in\mathbf Z_{\ge0}.
\tag{3}
\]

Let `Omega` be a finite control set. Suppose that every reachable section state
`(omega,i)` carries a nonconstant rational function

\[
f_{\omega,i}(X)\in\mathbf Q(X)
\tag{4}
\]

with the following properties.

1. `f_(omega,i)(n)` is a positive ordinary integer for every sufficiently large
   integer `n>=0`.
2. Every state has all six outgoing children.
3. For every child type `j`, with successor control `omega'`, the transformed
   coordinates reproduce the same six-branch law on the complete child
   cylinder. Allowing a state-dependent permutation `pi_(omega,i)` of the six
   physical labels, this means

   \[
   \boxed{
   Q f_{\omega',j}(\lambda_{ij}+Pt)
   =
   P f_{\omega,i}(\kappa_{ij}+Qt)
   +a_{\pi_{\omega,i}(j)}
   }
   \tag{5}
   \]

   for every sufficiently large integer `t`.

Then every reachable rational section is affine and in fact

\[
\boxed{
 f_{\omega,i}(X)=PX+c_i,
 \qquad
 \pi_{\omega,i}(j)=j.
 }
\tag{6}

Consequently no finite rational-function nucleus gives a contracting, bounded,
or seed-preserving recursive extraction of an ordinary root. The only such
nucleus is the original expanding forward map.

## Lemma 1 — tail-integral rational functions are polynomials

Let `f=A/B` with coprime polynomials `A,B in Z[X]`. If `f(n)` is an integer for
all sufficiently large integers `n`, then `B` is constant.

### Proof

Because `A` and `B` are coprime in `Q[X]`, there are polynomials `U,V in Z[X]`
and a nonzero integer `R` such that

\[
UA+VB=R.
\tag{7}
\]

For every sufficiently large integer `n`, integrality of `A(n)/B(n)` gives

\[
B(n)\mid A(n).
\]

Equation `(7)` then gives

\[
B(n)\mid R.
\]

If `B` were nonconstant, `|B(n)|` would tend to infinity, contradicting the
fixed nonzero integer `R`. Thus `B` is constant and `f` is a polynomial over
`Q`. ∎

## Lemma 2 — finite polynomial section cycles force degree one

After Lemma 1, write

\[
f_{\omega,i}(X)=L_{\omega,i}X^{d_{\omega,i}}+\cdots,
\qquad L_{\omega,i}\ne0.
\]

Equation `(5)` holds on infinitely many integers `t`, hence is a polynomial
identity in `t`. Comparing degrees shows

\[
d_{\omega',j}=d_{\omega,i}
\tag{8}
\]

along every edge. Call the common edge degree `d`.

Comparing leading coefficients in `(5)` and using `(3)` gives

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
\tag{9}
\]

Starting from any reachable state and following edges in the finite control
graph eventually reaches a directed cycle. Around a cycle of length `s`,
`(9)` gives

\[
L=L\left({Q\over P}\right)^{s(d-1)}.
\]

Since `L` is nonzero and `P!=Q`, one must have

\[
\boxed{d=1.}
\tag{10}
\]

Degree equality along the path back to the starting state proves that every
reachable section has degree one. ∎

## Proof of the theorem

By Lemmas 1 and 2,

\[
f_{\omega,i}(X)=v_{\omega,i}X+s_{\omega,i}.
\tag{11}
\]

Tail integrality makes both coefficients ordinary integers: the first
difference of `(11)` is `v_(omega,i)`, and then one value recovers
`s_(omega,i)`. Eventual positivity forces the common slope below to be
positive.

For degree one, the leading-coefficient identity `(9)` becomes

\[
v_{\omega',j}=v_{\omega,i}
\tag{12}
\]

on every edge. Hence one common positive integer scale `v` occurs throughout
each reachable component. The exact constant terms in `(5)` now satisfy the
finite affine-nucleus hypotheses of `T-7402`, including arbitrary successor
control and initially arbitrary state-dependent permutations of the six
symbols.

`T-7402` therefore forces

\[
v=P,
\qquad
s_{\omega,i}=c_i,
\qquad
\pi_{\omega,i}(j)=j.
\]

This is exactly `(6)`. ∎

## Why this is a global obstruction

A natural ordinary-extraction proof would recursively replace a legal root by a
smaller exact section root and iterate inside a finite nucleus. `T-7401` rules
out one affine section, and `T-7402` rules out arbitrary finite affine control.
The present theorem shows that allowing nonlinear polynomials or rational
functions does not enlarge that class: finite control plus exact rational
sections collapses back to the same forward map.

This conclusion is all-depth and experiment-free. It is not inferred from the
failure of sampled controllers.

## Dependency audit

- `D-7401` supplies the exact tail parametrization `(1)--(3)`.
- The rational-to-polynomial lemma and degree-one argument are proved here.
- `T-7402` is invoked only after the rational sections have been reduced to a
  finite affine nucleus.
- No external theorem or computation is used.

## Gap audit

- The theorem concerns self-replication of the complete six-branch subtree. A
  single survivor may lie in a proper, genuinely nonlinear infinite-section
  sublanguage.
- Algebraic functions not represented by rational functions, pushdown
  sections, and unbounded arithmetic state are outside the theorem.
- The theorem does not prove that the least roots `m_n` diverge.
- It supplies no positive root and creates no `K-74xx` object.

## Adversarial tests

1. Rational functions may initially have nonconstant denominators.
2. Degrees and leading coefficients may depend on both control state and type.
3. Successor control may depend on the chosen child.
4. Identities are required only on the exact infinite arithmetic progression of
   each child cylinder; this is enough because two rational functions agreeing
   there agree identically after denominator clearing.
5. Eventual positivity is explicit, so a negative-slope affine coordinate is
   not silently admitted.
6. The surviving map is checked directly: `f_i(k)=Pk+c_i` is the original
   forward boundary value.

## Suggested next attack

Do not enlarge the finite rational nucleus again. Attack `Q-7401` by a direct
ordinary-height or digit-escape theorem, or identify a genuinely unbounded
nonlinear section variable and prove why it bounds the same initial root.