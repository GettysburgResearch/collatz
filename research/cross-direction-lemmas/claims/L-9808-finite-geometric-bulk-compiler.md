# L-9808 — Finite geometric compiler for inverse Hensel bulk

Claim ID: `L-9808`  
Title: Every inverse-power bulk prefix is an explicit finite polynomial in its positive ordinary dual  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: standard 2-adic LTE; `L-9802` for the inverse-bulk normalization  
Scope: odd-base divided powers and the ordinary bulk generator of `PR3/T-0030`  
Related counterexample candidates: none

## Definitions

Let `q>1` and `a>0` be odd, and put

\[
\sigma=\nu_2(q^2-1),
\qquad
e_m=m+\sigma-1
\qquad(m\ge1).
\tag{1}
\]

Define the positive ordinary bulk, inverse bulk, and unnormalized power by

\[
A_m=q^{a2^m},
\qquad
V_m=\frac{A_m-1}{2^{e_m}}\in\mathbb Z,
\qquad
u_m=\frac{A_m^{-1}-1}{2^{e_m}}\in\mathbb Z_2.
\tag{2}
\]

For an integer `L>=1`, define the finite geometric compiler

\[
P_{m,L}
=-V_m\sum_{j=0}^{L-1}(-2^{e_m}V_m)^j
\in\mathbb Z.
\tag{3}
\]

## Statement

For every `m,L>=1`:

### 1. Common quadratic dynamics

Both `V_m` and `u_m` are odd, and each obeys

\[
\boxed{
X_{m+1}=X_m+2^{m+\sigma-2}X_m^2.
}
\tag{4}
\]

Thus the positive ordinary word and its inverse 2-adic dual evolve under the
same integral polynomial.

### 2. Exact duality and finite compilation

One has

\[
\boxed{u_m=-A_m^{-1}V_m}
\tag{5}
\]

and the compiler error is exactly

\[
\boxed{
u_m-P_{m,L}
=(-1)^{L+1}2^{Le_m}V_m^{L+1}A_m^{-1}.
}
\tag{6}
\]

In particular,

\[
\boxed{\nu_2(u_m-P_{m,L})=Le_m.}
\tag{7}
\]

### 3. Exact precision cost

For a requested precision `Q>=1`, set

\[
L_Q=\left\lceil\frac{Q}{e_m}\right\rceil.
\tag{8}
\]

Then

\[
\boxed{
P_{m,L_Q}\equiv u_m\pmod{2^Q}.
}
\tag{9}
\]

Within the truncation family (3), this depth is minimal: with the convention
`P_(m,0)=0`,

\[
P_{m,L_Q-1}\not\equiv u_m\pmod{2^Q}.
\tag{10}
\]

### 4. Append-only compiler law

Increasing the compiler depth by one appends one exact correction:

\[
\boxed{
P_{m,L+1}-P_{m,L}
=(-1)^{L+1}2^{Le_m}V_m^{L+1},
}
\tag{11}
\]

whose valuation is exactly `Le_m`. Hence the ordinary polynomials
`P_(m,1),P_(m,2),...` form a nested, certified prefix stream for `u_m`.

For `q=3` and `a=7`, one has `sigma=3`, `e_m=m+2`, and `V_m` is exactly the
ordinary generator in `PR3/T-0030`.

## Proof

The even-exponent LTE identity gives

\[
\nu_2(A_m-1)=m+\sigma-1=e_m,
\]

so `V_m` is a positive odd integer. Multiplication by the odd unit `A_m^-1`
shows that `u_m` is odd as well.

Since `A_(m+1)=A_m^2` and `e_(m+1)=e_m+1`, writing

\[
A_m=1+2^{e_m}V_m
\]

and squaring proves (4) for `V_m`. Applying the same calculation to
`A_m^-1=1+2^{e_m}u_m` proves (4) for `u_m`.

The identity

\[
A_m^{-1}-1=-A_m^{-1}(A_m-1)
\]

proves (5). Put `x=2^(e_m)V_m`, so `A_m=1+x`. The finite geometric identity

\[
\frac1{1+x}
=\sum_{j=0}^{L-1}(-x)^j+\frac{(-x)^L}{1+x}
\]

gives

\[
-\frac{V_m}{1+x}
=P_{m,L}
+(-1)^{L+1}\frac{2^{Le_m}V_m^{L+1}}{A_m}.
\]

Together with (5), this is (6). Both `V_m` and `A_m` are odd, so its valuation
is exactly `Le_m`, proving (7).

Equations (9)--(10) now follow from

\[
(L_Q-1)e_m<Q\le L_Qe_m,
\]

with the case `L_Q=1` using that `u_m` is odd and `P_(m,0)=0`. Finally, the
new `j=L` summand in (3) is exactly the right-hand side of (11). ∎

## Motivation

`PR3/T-0030` replaces a completed 2-adic bulk by a positive ordinary generator,
but still invokes a finite inverse compiler. This lemma makes that compiler a
single explicit polynomial and gives its exact precision cost. It therefore
separates two questions cleanly:

- generating the required inverse prefix is finite ordinary arithmetic;
- routing that prefix into the physical residual cylinder remains a distinct
  Collatz constraint.

## Dependency audit

- LTE is used only to prove the exact odd normalization in (2).
- `L-9802` supplies the same inverse normalization and independently checks the
  quadratic recurrence; the proof above rederives both facts.
- No connector-router or counterexample claim is used.

## Gap audit

- The polynomial may have depth `Theta(Q/m)` at scale `m`; this is a finite
  compiler, not a bounded-memory local rule.
- Congruence to `u_m` does not place the result in a physical residual cylinder.
- The bit-length surplus of `V_m` does not by itself implement the arithmetic
  multiplications in a Collatz rewrite system.
- Nothing here supplies one marked ordinary initialization.

## Adversarial tests

- At `L=1`, `P_(m,1)=-V_m` and (6) becomes
  `u_m+V_m=2^(e_m)V_m^2/A_m`, so the first error valuation is exactly `e_m`.
- At `L=2`, the next correction has the opposite sign and the error valuation
  doubles to `2e_m`.
- The word “minimal” in (10) is restricted to the geometric family (3); no
  circuit or algorithmic lower bound is claimed.

## Remaining uncertainty

None in the algebraic compiler. Its physical realizability inside the
connector grammar is open.

## Suggested next attack

Normalize the residual Montgomery zipper so that multiplication by `V_m` and
the append law (11) become explicit finite-state or counter updates. The first
useful target is not the whole precision `Q`, but one additional correction
block of length `e_m` per physical stage.
