# T-8511 — Multiplicative quotient refund is absorbing once it dominates the following cylinder

**Claim ID:** `T-8511`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-23  
**Dependencies:** elementary integer arithmetic  
**Scope:** changing-modulus ordinary quotient maps, including `L-8507` and PR #51 `L-8002`

## General setup

For each step `n`, suppose an exact ordinary transition is written

\[
\boxed{
x_n=\rho_n+Q_nu_n
\longmapsto
x_{n+1}=\sigma_n+A_nu_n,}
\tag{1}
\]

where

\[
Q_n,A_n\in\mathbf Z_{>0},
\qquad
0\le\rho_n<Q_n,
\qquad
\sigma_n\ge0,
\qquad
u_n\in\mathbf Z_{\ge0}.
\]

Assume the next legal step has the corresponding exact decomposition

\[
\boxed{
x_{n+1}=\rho_{n+1}+Q_{n+1}u_{n+1},}
\tag{2}
\]

with

\[
0\le\rho_{n+1}<Q_{n+1}.
\]

Call the step canonical when `u_n=0` and refunded when `u_n>=1`.

## Theorem

For every integer `q>=0`, if

\[
\boxed{A_n>2^qQ_{n+1},}
\tag{3}
\]

then every refunded legal transition satisfies

\[
\boxed{u_{n+1}\ge2^qu_n.}
\tag{4}
\]

In particular:

1. if `A_n>Q_(n+1)`, the refunded region is forward invariant;
2. if `A_n>2Q_(n+1)`, the free quotient at least doubles;
3. if `A_n>4Q_(n+1)`, it grows by at least a factor four;
4. along any tail on which `(3)` holds with exponents `q_n`,
   \[
   \boxed{
   u_{n+r}\ge
   2^{q_n+\cdots+q_{n+r-1}}u_n.}
   \tag{5}
   \]

If, additionally, canonical runs have a finite uniform bound on that tail, then every infinite ordinary orbit eventually enters the refunded region and remains there forever.

## Proof

Equate `(1)` and `(2)`:

\[
Q_{n+1}u_{n+1}
=A_nu_n+\sigma_n-\rho_{n+1}.
\]

Using `sigma_n>=0` and `rho_(n+1)<Q_(n+1)`, condition `(3)` gives

\[
u_{n+1}>2^qu_n-1.
\]

The left side is an integer, proving `(4)`. Iteration proves `(5)`.

If canonical runs have bounded length, an infinite orbit must eventually take a refunded step. Forward invariance under the case `q=0` keeps every later step refunded. ∎

## Phase-34 specialization

For `L-8507`,

\[
Q_n=H_{t_n}=2^{11(t_n+33)},
\]

\[
A_n=3^{G_n},
\]

and

\[
Q_{n+1}=H_{t_n+16}=2^{11(t_n+49)}.
\]

`T-8510` proves

\[
A_n>2^{q(t_n)}Q_{n+1},
\qquad
q(t)=\left\lfloor\frac{63t-353166}{665}\right\rfloor.
\]

At `t>=5632`, `q(t)>=2`. `T-8509` supplies the canonical-run bound, so every hypothetical infinite phase-34 path is eventually permanently refunded.

## Negative-three-cycle specialization

PR #51 `L-8002` has

\[
\boxed{
k=\rho_{r,s,t}+2^{4+3t}\ell
\longmapsto
k^+=\sigma_{r,s,t}+9^{r+1}\ell.}
\tag{6}

If the following complete run cylinder has modulus

\[
Q_{\rm next}=2^{4+3v},
\]

then any legal refunded step satisfying

\[
\boxed{
9^{r+1}>2^q2^{4+3v}
}
\tag{7}

obeys

\[
\boxed{
\ell^+\ge2^q\ell.}
\tag{8}

Thus a high-run invariant for PR #51 should control not only the pointwise physical condition `r>=5`, but also the explicit two-run cone `(7)`. Inside any forward-invariant cone where `q>=0`, a single nonzero lift becomes absorbing; inside `q>=1` or `q>=2`, it is multiplicatively refunded.

## Constructive significance

The common positive architecture is now exact:

```text
changing dyadic cylinder,
ordinary free quotient,
odd multiplicative transport,
nonnegative canonical carry,
following-cylinder domination,
absorbing refunded region.
```

This theorem separates two genuinely different tasks:

1. **growth/absorption**, supplied by `(3)`;
2. **first ordinary entry**, the remaining exact top-boundary existence problem.

## Gap audit

- Domination of the following modulus does not construct the first refunded ordinary state.
- A branchwise cone condition must be proved invariant before it can be iterated.
- The theorem assumes exact ordinary decompositions, not completion-level residues.
- Canonical-run boundedness is a separate hypothesis in the abstract form.
