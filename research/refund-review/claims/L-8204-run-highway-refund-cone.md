# L-8204 — Exact refund cone for the negative-three-cycle run highway

**Claim ID:** `L-8204`  
**Title:** A three-runs-ahead inequality makes every coherent PR #51 top lift double  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-refund-01`  
**Created:** 2026-07-23  
**Dependencies:** `L-8203`; frozen PR #51 `L-8002/T-8002`  
**Scope:** coherent ordinary maximal-run paths in the normalized negative-three-cycle chart  
**Related counterexample candidates:** none

## Setup

Let

\[
r_0,r_1,r_2,\ldots
\]

be the maximal-run sequence of a coherent PR #51 chart path. In the quotient coordinates of `L-8002`, the transition from state

\[
(r_n,r_{n+1},k_n)
\]

toward the prospective run `r_(n+2)` has

\[
k_n
=
\rho_n+M_{r_{n+2}}\ell_n,
\tag{1}
\]

\[
k_{n+1}
=
\sigma_n+9^{r_n+1}\ell_n,
\tag{2}
\]

where

\[
M_s=2^{4+3s},
\qquad
\sigma_n\ge0.
\tag{3}
\]

Coherence with the next prospective run `r_(n+3)` means

\[
k_{n+1}
=
\rho_{n+1}
+
M_{r_{n+3}}\ell_{n+1},
\tag{4}
\]

with

\[
0\le\rho_{n+1}<M_{r_{n+3}}.
\tag{5}
\]

## Refund-cone theorem

If

\[
\boxed{
9^{r_n+1}
>
2M_{r_{n+3}}
=
2^{5+3r_{n+3}}}
\tag{6}
\]

and

\[
\ell_n\ge1,
\]

then

\[
\boxed{\ell_{n+1}\ge2\ell_n.}
\tag{7}
\]

### Proof

Equations `(2)` and `(4)` give

\[
M_{r_{n+3}}\ell_{n+1}
=
\sigma_n+9^{r_n+1}\ell_n-\rho_{n+1}.
\]

Use `(3)`, `(5)`, and `(6)` exactly as in `T-8201`:

\[
M_{r_{n+3}}\ell_{n+1}
>
(2\ell_n-1)M_{r_{n+3}}+1.
\]

The left side is an integral multiple of the modulus, so `(7)` follows.

## Physical-growth cone

PR #51 `T-8002` independently proves that the physical macro boundary grows whenever

\[
\boxed{r_n\ge5.}
\tag{8}
\]

Thus a complete positive certificate may be separated into three exact gates:

1. **physical highway**
   \[
   r_n\ge5;
   \]
2. **top-boundary refund**
   \[
   9^{r_n+1}>2^{5+3r_{n+3}};
   \]
3. **ordinary coherence**
   every required quotient congruence is realized by the same finite initial core.

Gates 1 and 2 imply all required growth. Gate 3 is the only existence problem.

## Explicit aperiodic target schedule

The schedule

\[
\boxed{r_n=64+n}
\qquad(n\ge0)
\tag{9}
\]

is nonperiodic and satisfies both growth gates.

Indeed, `r_n>=64>5`. Also

\[
r_{n+3}=r_n+3.
\]

The exact inequalities

\[
3^{53}>2^{84},
\qquad
3^{12}>2^{19}
\]

give

\[
3^{65}>2^{103}.
\]

Squaring yields

\[
9^{65}=3^{130}>2^{206}.
\]

At `r_n=64`,

\[
5+3r_{n+3}
=
5+3\cdot67
=
206,
\]

so `(6)` holds strictly. Advancing `n` multiplies the left side by `9` and the right side by `8`, hence the inequality persists.

Therefore `(9)` defines a particularly simple, explicitly aperiodic, high-run and top-refunding source language.

## What remains for the schedule

For the prescribed sequence `(9)`, every finite prefix has infinitely many positive ordinary representatives by the exact run cylinders. The infinite sequence selects one compatible `2`-adic initial core.

The unresolved statement is:

\[
\boxed{
\text{is that selected core one positive ordinary integer?}}
\]

A positive answer, with exact replay, is an unconditional Collatz counterexample. This claim does not assert that answer.

## Gap audit

- The relevant future run in `(6)` is `r_(n+3)`, not `r_(n+2)`.
- An explicit aperiodic schedule is not an explicit ordinary orbit.
- Top-lift doubling does not imply the nested initial residues stabilize.
- The schedule `(9)` may be excluded by a future completion-height or value-theory theorem.
- No finite search is used as the existence argument.

## Verification

`X-8202` reconstructs 386,176 exact coherent refund-cone lift cases in its finite audit grid and checks the first 501 inequalities of the schedule `(9)` using integer arithmetic.
