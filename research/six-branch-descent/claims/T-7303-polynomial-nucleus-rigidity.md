# T-7303 — Finite polynomial nuclei collapse to the forward image

**Claim ID:** `T-7303`  
**Title:** No finite-control polynomial section can self-replicate the complete six-branch subtree nontrivially  
**Status:** `PROPOSED / EXACT ALGEBRAIC THEOREM`  
**Authoring agent:** `gpt56-cycle-01`  
**Created:** 2026-07-26  
**Dependencies:** PR #64 `D-7401` and `T-7402`  
**Scope:** finite-control integer-polynomial coordinates on the exact high quotient  
**Related counterexample candidates:** none

## 1. Setup

Use the exact source form from PR #64:

\[
x=r_i+Qk,
\qquad
F(x)=c_i+Pk.
\]

If the next type is `j`, write

\[
F(x)=r_j+Qk',
\]

so that

\[
\boxed{Qk'=Pk+c_i-r_j.}
\tag{1}
\]

Let `Omega` be a finite control set.  At every reachable section `(omega,i)`
attach a polynomial

\[
\boxed{f_{\omega,i}(k)\in\mathbf Z[k]}
\tag{2}
\]

that is positive for all sufficiently large admissible `k`.

For each next type `j`, allow an arbitrary successor control

\[
\omega'=\tau(\omega,i,j).
\]

Assume that the coordinate carries the complete six-branch subtree: for every
`j` and every `k` in the infinite transition cylinder for `i -> j`,

\[
\boxed{
Q f_{\omega',j}(k')
=P f_{\omega,i}(k)+a_j.}
\tag{3}
\]

## 2. Theorem

On every reachable component,

\[
\boxed{
 f_{\omega,i}(k)=Pk+c_i.}
\tag{4}
\]

Thus every finite polynomial nucleus is exactly the original forward image.
There is no nonlinear polynomial, contracting polynomial, bounded polynomial,
or seed-preserving polynomial full-subtree section at any finite-control size.

## 3. Degree propagation

Equation `(3)` holds on an infinite arithmetic progression of `k`, so it is a
polynomial identity.

If one endpoint polynomial is nonconstant, comparison through the nonconstant
affine substitution `(1)` gives

\[
\deg f_{\omega',j}=\deg f_{\omega,i}.
\]

Let the common degree on one edge be `d>=1`, and let the leading coefficients be
`L` and `L'`.  Comparing the leading terms in `(3)` gives

\[
Q L'\left({P\over Q}\right)^d=P L,
\]

hence

\[
\boxed{L'=L\left({Q\over P}\right)^{d-1}.}
\tag{5}
\]

Every state in a finite directed graph reaches a directed cycle.  Multiplying
`(5)` around a cycle of length `m` gives

\[
1=\left({Q\over P}\right)^{m(d-1)}.
\]

Since `P!=Q`,

\[
\boxed{d=1.}
\tag{6}
\]

Degree is preserved on every incoming path to that cycle, so every nonconstant
reachable polynomial has degree one.

## 4. Constant sections are impossible

Suppose a reachable component consisted of positive constant coordinates.  On
an edge with digit `a_j`, `(3)` becomes

\[
f_{\omega',j}={P f_{\omega,i}+a_j\over Q}.
\]

Because `P>Q`, `a_j>0`, and the source value is positive,

\[
f_{\omega',j}>f_{\omega,i}.
\]

Following any infinite path through the finite control graph would produce a
strictly increasing sequence drawn from a finite set of constants, impossible.
Thus every reachable component is in the degree-one case.

## 5. Reduction to finite affine nucleus rigidity

Write

\[
f_{\omega,i}(k)=v_{\omega,i}k+s_{\omega,i}.
\]

For `d=1`, equation `(5)` gives equality of leading coefficients along every
edge.  Hence there is one common positive integer scale `v` on each reachable
component.

The system is now exactly the finite affine section system of PR #64 `T-7402`.
That theorem proves

\[
\boxed{v=P,
\qquad s_{\omega,i}=c_i.}
\]

Substitution gives `(4)`. ∎

## 6. Why this is a substantive generalization

PR #64 `T-7402` rules out finite affine nuclei.  The present theorem allows an
arbitrary polynomial degree at every finite-control state and proves that the
expanding rational-base edge itself forces the degree back to one before the
affine rigidity theorem is invoked.

Consequently, enlarging finite control and replacing affine sections by fixed
integer-polynomial sections cannot approach bounded least roots.

## 7. Gap audit

- Rational functions with nonconstant denominators are not included explicitly.
- Piecewise definitions with an unbounded number of pieces are outside scope.
- A seed-specific nonlinear arithmetic invariant may still exist.
- The theorem carries the **complete** six-branch subtree; a strict proper
  sublanguage may admit special polynomial relations.
- No boundedness theorem, ordinary root, or Collatz counterexample is claimed.
