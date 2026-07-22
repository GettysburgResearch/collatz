# L-9809 — Transcendence and digit complexity of the logarithmic bulk

Claim ID: `L-9809`  
Title: The odd-base Hensel bulk limit is transcendental and has nonperiodic binary digits  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9802`; Mahler's 2-adic Hermite--Lindemann theorem as imported in `PR7/LIT-KTHM-0030`  
Scope: completed odd-base divided-power bulks and their canonical binary words  
Related counterexample candidates: none

## Definitions

We use the following standard transcendence input.

> **Mahler's 2-adic Hermite--Lindemann theorem.** If a nonzero algebraic
> `lambda` lies in the convergence disk of the 2-adic exponential, then
> `exp_2(lambda)` is transcendental.

Let `q>1` and `a>0` be odd, and put

\[
\sigma=\nu_2(q^2-1).
\]

By `L-9802`, the inverse bulks

\[
u_m=\frac{q^{-a2^m}-1}{2^{m+\sigma-1}}
\]

converge in `Z_2` to

\[
u_\infty=-\frac{a\log(q^2)}{2^\sigma}.
\tag{1}
\]

Write its canonical binary expansion as

\[
u_\infty=\sum_{j\ge0}d_j2^j,
\qquad d_j\in\{0,1\}.
\tag{2}
\]

For `n>=1`, let `p(n)` be the number of distinct length-`n` factors occurring
in the one-sided word `d_0d_1d_2...`.

## Statement

### 1. Transcendence

The normalized limit is transcendental over `Q`:

\[
\boxed{u_\infty\text{ is transcendental}.}
\tag{3}
\]

### 2. No periodic or stabilizing tail

The binary word in (2) is not eventually periodic. In particular, it is not
eventually zero, and the canonical representatives

\[
R_K=[u_\infty]_{2^K}
\tag{4}
\]

do not eventually stabilize.

### 3. Universal factor-complexity floor

For every `n>=1`,

\[
\boxed{p(n)\ge n+1.}
\tag{5}
\]

For `q=3,a=7`, this applies to the connector bulk

\[
u_\infty=-\frac78\log(9)
=-\frac74\log_2(3)
\]

identified in `PR3/O-0010` and `PR7/LIT-KTHM-0030`.

## Proof

Put

\[
\lambda=-a\log(q^2).
\]

The 2-adic logarithm valuation identity used in `L-9802` gives

\[
\nu_2(\lambda)=\nu_2(\log(q^2))=\sigma\ge3.
\]

Thus `lambda` lies in the convergence disk of `exp_2`. It is nonzero, and

\[
\exp_2(\lambda)=q^{-2a}\in\mathbb Q.
\tag{6}
\]

If `lambda` were algebraic, Mahler's theorem would make the left side of (6)
transcendental, a contradiction. Hence `lambda` is transcendental. Multiplying
by the nonzero rational `2^(-sigma)` preserves transcendence, and (1) proves
(3).

Suppose the digits in (2) were periodic from position `N` with period `h`.
Let

\[
B=\sum_{i=0}^{h-1}d_{N+i}2^i.
\]

The 2-adically convergent geometric series would give

\[
u_\infty
=\sum_{j<N}d_j2^j
+2^NB\sum_{k\ge0}2^{kh}
=\sum_{j<N}d_j2^j+\frac{2^NB}{1-2^h}
\in\mathbb Q,
\]

contradicting (3). Thus the word is not eventually periodic. Eventual
stabilization of (4) would make the digits eventually zero, so it is also
impossible.

It remains to prove (5). For any one-sided infinite binary word, factor
complexity is nondecreasing. If `p(n)<=n` for some `n`, then either only one
letter occurs, in which case the word is constant, or among the transitions

\[
p(1),p(2),\ldots,p(n)
\]

there is an index `k<n` with `p(k+1)=p(k)`. Every occurring length-`k` factor
then has a unique right extension. Iterating this deterministic extension on
the finite set of length-`k` factors makes the word eventually periodic. This
contradicts the preceding paragraph. Therefore `p(n)>=n+1` for every `n`. ∎

## Motivation

`L-9802` identifies the moving Hensel bulk as a fixed completion object, while
`L-9808` compiles any finite prefix from an ordinary dual. This lemma marks the
exact boundary between those facts:

- every finite prefix is arithmetically generable;
- the completed target is not rational, not eventually periodic, and not one
  stabilized ordinary register.

The linear factor-complexity floor is also a clean interface with the
repetition-rigidity program, although it is far weaker than a proof of high
entropy.

## Dependency audit

- `L-9802` supplies the limit (1), its integrality, and the logarithm valuation.
- Mahler's theorem is the only non-elementary input and is stated explicitly.
- The nonperiodicity and complexity conclusions are proved directly after the
  transcendence input.

## Gap audit

- Linear factor complexity does not rule out automatic, substitutive, or other
  low-complexity digit generators.
- Transcendence does not imply computational hardness or normality.
- The completed logarithm is a connector-control target, not an ordinary
  Collatz state.
- Finite forward generation remains compatible with every conclusion here.

## Adversarial tests

- An ordinary negative integer has an eventually all-one 2-adic expansion;
  the argument excludes that case as well because it excludes every eventual
  period.
- A rational 2-adic number can have a nonterminating expansion, but its digits
  are eventually periodic, exactly the possibility ruled out above.
- The proof needs `exp_2(lambda)=q^(-2a)` inside the exponential disk; the
  valuation `sigma>=3` supplies this without a branch ambiguity.

## Remaining uncertainty

The transcendence conclusion is only as independent as the imported Mahler
theorem. No claim about superlinear factor complexity is made.

## Suggested next attack

Determine whether the physical padding-counter or residual-router maps preserve
enough algebraic structure that a rational or eventually periodic address
would force an algebraic output. `L-9810` supplies this argument for the exact
exponential counter isometries.
