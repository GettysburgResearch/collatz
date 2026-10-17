# L-0040 — Eventually integral algebraic branches are polynomial

Claim ID: `L-0040`  
Title: A real algebraic function taking integer values on every sufficiently large integer is a polynomial  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-26  
Dependencies: Newton--Puiseux expansion at infinity; elementary finite differences  
Scope: real algebraic branches on a positive ray  
Related counterexample candidates: none

## Statement

Let

\[
f:(X_0,\infty)\longrightarrow\mathbb R
\]

be one real analytic branch of a function algebraic over \(\mathbb Q(X)\). Assume

\[
\boxed{f(n)\in\mathbb Z}
\qquad\text{for every sufficiently large integer }n.
\tag{1}
\]

Then there is a polynomial

\[
\boxed{p(X)\in\mathbb Q[X]}
\tag{2}
\]

such that

\[
\boxed{f(X)=p(X)}
\qquad(X>X_1)
\tag{3}
\]

for some \(X_1\). By algebraic continuation, the chosen branch is the polynomial branch wherever both are defined.

Moreover, \(p(n)\in\mathbb Z\) for every sufficiently large integer \(n\). Equivalently, after a translation of the variable it has an integer-valued Newton expansion

\[
p(N+m)=\sum_{j=0}^{d}c_j\binom mj,
\qquad c_j\in\mathbb Z.
\tag{4}
\]

## Proof

### 1. Algebraic growth and derivative decay

Newton--Puiseux expansion at infinity gives, on the selected branch, a convergent expansion of the form

\[
f(X)=\sum_{r\ge r_0}c_r X^{-r/e}
\tag{5}
\]

for one positive integer \(e\), after extracting a finite leading power. In particular there is a real number \(\rho\) such that, for every integer \(k\ge0\),

\[
\boxed{f^{(k)}(X)=O(X^{\rho-k})}
\qquad(X\to+\infty).
\tag{6}
\]

Choose an integer

\[
k>\max(\rho,0).
\tag{7}
\]

The standard integral formula for a forward difference is

\[
\Delta^k f(n)
=
\int_{[0,1]^k}
 f^{(k)}(n+t_1+\cdots+t_k)
\,dt_1\cdots dt_k.
\tag{8}
\]

Equations (6)--(8) imply

\[
\boxed{\Delta^k f(n)\longrightarrow0.}
\tag{9}
\]

### 2. Integrality forces exact vanishing

By (1), every sufficiently late forward difference \(\Delta^k f(n)\) is an integer. An integer sequence tending to zero is eventually zero. Hence

\[
\boxed{\Delta^k f(n)=0}
\qquad(n\ge N)
\tag{10}
\]

for one integer \(N\).

The elementary Newton interpolation identity now gives

\[
f(N+m)=
\sum_{j=0}^{k-1}
\Delta^j f(N)\binom mj
\qquad(m\in\mathbb Z_{\ge0}).
\tag{11}
\]

The coefficients \(\Delta^j f(N)\) are integers. Thus the right side is an integer-valued polynomial \(p(N+m)\) of degree below \(k\), proving (4) and

\[
 f(n)=p(n)
\tag{12}
\]

for every sufficiently large integer \(n\).

### 3. Infinite agreement forces algebraic identity

Put \(g=f-p\). The branch \(g\) is algebraic over \(\mathbb Q(X)\) and vanishes at infinitely many real points tending to infinity.

Let \(H(X,Y)\in\mathbb Q[X,Y]\) be an irreducible polynomial relation for \(g\). Then

\[
H(n,0)=0
\tag{13}
\]

for infinitely many integers \(n\). Hence the polynomial \(H(X,0)\) is identically zero. Therefore \(Y\) divides \(H(X,Y)\). Irreducibility forces \(H\) to be a nonzero scalar multiple of \(Y\), and consequently

\[
g=0.
\tag{14}
\]

This proves (2)--(3). ∎

## Sequence-only variant

The analytic part of the proof uses only the following condition:

> there is a fixed \(k\) for which \(\Delta^k f(n)\to0\).

Thus any eventually integer-valued section sequence with a tame interpolation satisfying that condition is eventually polynomial on the integers, even before algebraicity is invoked. Algebraicity is used only to turn equality on the integer tail into identity of the branch.

## Semialgebraic corollary

A one-variable real semialgebraic function is, after deleting finitely many points and restricting to a sufficiently late ray, a finite union of Nash branches. Each Nash branch is algebraic over \(\mathbb Q(X)\) after adjoining its defining coefficients. Therefore the same conclusion holds for an eventually integer-valued semialgebraic branch defined over \(\overline{\mathbb Q}\): it is eventually polynomial.

## Why this matters for ordinary extraction

Several proposed ordinary-extraction mechanisms seek a finite collection of nonlinear section coordinates

```text
large legal tail -> smaller legal tail
```

whose formulas are algebraic or semialgebraic and whose values are ordinary integers for every sufficiently large tail parameter.

The lemma proves that such a coordinate is not genuinely algebraic-nonlinear. On the integer tail it must already be polynomial, and exact algebraicity then makes it the same polynomial branch. In a finite expanding section graph, the polynomial degrees can subsequently be compared around graph cycles.

## Dependency audit

- Newton--Puiseux at infinity supplies only the derivative estimate (6).
- The finite-difference and infinite-zero arguments are proved here.
- No Collatz-specific theorem or computation is used.

## Gap audit

- The lemma does not apply to a function defined only on a sparse recursively generated subset of the integers.
- It does not apply to an unbounded-state pushdown or quotient machine with no fixed algebraic section formula.
- Transcendental functions can be integer-valued on the integers without being polynomials.
- The lemma is a method-boundary theorem, not an ordinary survivor or counterexample.
