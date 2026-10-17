# Q-8403 — Nonlinear ordinary top-boundary invariant

Claim ID: `Q-8403`  
Title: Does one finite intrinsic pulse-chart core satisfy the nineteen-bit decoder forever?  
Status: `IDEA / FULL EXISTENCE TARGET`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-23  
Dependencies: `L-8407`, `T-8403`, `T-8404`, `T-8405`, `X-8405`  
Scope: the exact six-branch `(L,b)=(6,1)` pulse chart

## Full theorem requested

Prove that there is one finite tuple

\[
 \boxed{(r_0,i_0,g,c_0)}
 \tag{1}
\]

with

```text
r_0,i_0 in {0,...,5},
g in {1,7},
c_0 a positive ordinary integer in one exact intrinsic cell,
```

such that the deterministic decoder of `L-8407` is defined for every future step.

For

\[
 X_n=3^{12+2(r_n-i_n)}c_n+\delta_g,
 \qquad
 \delta_1=7,
 \quad
 \delta_7=1,
 \tag{2}
\]

this means

\[
 v_n=\nu_2(X_n),
 \qquad
 i_{n+1}=i_n+{19-v_n\over3}\in\{0,\ldots,5\},
 \tag{3}
\]

and

\[
 c_{n+1}=X_n/2^{v_n}
 \tag{4}
\]

must lie in one exact next cell for `(i_n,i_(n+1),g)` for every `n`.

The physical seed would be

\[
 \boxed{
 n_0=2^{16-3i_0}3^{2r_0+1}g c_0-5.}
 \tag{5}
\]

`T-8403` would then prove that `(5)` is a positive unbounded Collatz trajectory.

## Equivalent top-quotient form

For one exact cell write

\[
 c=a+Hq.
 \tag{6}
\]

Every proposed next type has one exact transition

\[
 \boxed{2^{19}q'=3^Aq+\kappa,}
 \tag{7}
\]

or, after the required low block is exposed,

\[
 \boxed{
 q=\rho+2^{19}\ell
 \Longrightarrow
 q'=\sigma+3^A\ell.}
 \tag{8}
\]

`X-8405` proves `rho!=0` on all 3,024 transitions.  Therefore the invariant must genuinely refund a nonzero top block forever.

## Certificate classes already removed

A proof of `(1)` cannot be supplied by:

1. an eventually periodic branch or cell sequence;
2. a fixed-modulus residue lasso without top closure;
3. an eventually C-finite quotient;
4. a polynomial or ordinary exponential-polynomial quotient formula;
5. a rational ordinary generating function for the quotient;
6. a fixed finite-prime multiplicative library;
7. a long finite prefix with no inductive continuation theorem.

`T-8404` also requires any surviving branch code to have factor-complexity slope at least

```text
971.866577472579...
```

so low-complexity substitutional or transducer proposals must be rejected before physical replay.

## Acceptable positive proof objects

A complete proof may use any finite object that establishes `(2)`--`(4)` for all time, for example:

- a nonlinear invariant cone with exact cell membership;
- a finite nucleus plus a genuinely nonlinear unbounded register;
- a pushdown or stack grammar with canonical finite-word top closure;
- a self-replicating arithmetic subtree rooted at one explicit integer;
- an exact fresh-prime recurrence that simultaneously enforces every moving dyadic cylinder.

The proof must not initialize an infinite directive, a compatible `2`-adic address, or unbounded future data.

## Current evidence

`X-8405` contains one 13-cell ordinary quotient surviving 15 transitions and then exiting.  It demonstrates two cells of real refund but is not a candidate.

## Resolution boundary

A proof of `(1)` is an unconditional Collatz counterexample.  A proof that no tuple `(1)` exists closes this exact six-branch architecture but not Collatz in general.  Neither conclusion is currently established.
