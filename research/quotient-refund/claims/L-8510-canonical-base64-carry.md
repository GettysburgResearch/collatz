# L-8510 — The top-cell transport is a canonical base-64 multiplier with one bounded carry

**Claim ID:** `L-8510`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-23  
**Dependencies:** `L-8509`  
**Scope:** every four-cell top-boundary transition at active linear-refund heights

## Statement

Use the notation of `L-8509`. Thus

\[
\boxed{
64m'+e_k=Az+J,
}
\tag{1}

where

\[
A=3^G,
\qquad
z=d_k+64\ell,
\]

and the four paired input/output digits satisfy

\[
0\le d_k,e_k<64.
\]

Then:

### 1. Canonical quotient and remainder

\[
\boxed{
e_k=[Az+J]_{64},}
\tag{2}

\[
\boxed{
m'=\left\lfloor\frac{Az+J}{64}\right\rfloor.}
\tag{3}

In particular, for the four allowed input digits,

\[
\boxed{
e_k=[Ad_k+J]_{64}.}
\tag{4}

The paired digit map is the restriction of one affine permutation of `Z/64Z`.

### 2. Normalized carry bound

The common carry is nonnegative and satisfies

\[
\boxed{
0\le J<\frac43A.
}
\tag{5}

Consequently

\[
\boxed{
\left\lfloor\frac{Az}{64}\right\rfloor
\le m'
<
\frac{A(z+4/3)}{64}.
}
\tag{6}

### 3. Four-section transducer

For each finite physical block, the complete top-cell update has the exact machine form

```text
state data:       A=3^G, J, four allowed digits d_k;
input integer:    z=d_k+64*ell;
output digit:     e_k=(A*d_k+J) mod64;
next quotient:    floor((A*z+J)/64).
```

The multiplier and carry are common across all four target types. The target type is the section selected by the current least-significant base-64 digit.

## Proof

Equations `(2)--(4)` follow immediately from `(1)` and `0<=e_k<64`.

It remains to bound `J`. In the notation of `L-8509`,

\[
K=
\frac{
\widehat S+gA\lambda-a'
}{2^{D'}},
\qquad
J=(K-r)/3,
\]

where

\[
0<\widehat S<gA,
\qquad
0\le\lambda<2^{D'+j-6},
\]

\[
g=3\,2^{6-j},
\qquad
0\le a'<2^{D'},
\qquad
r\in\{0,1,2\}.
\]

The numerator defining `K` is greater than `-2^(D')`. Since `K` is an integer,

\[
K\ge0.
\]

Moreover

\[
g\lambda<3\,2^{D'}
\]

and, at every active height, `g<2^(D')`. Therefore

\[
\widehat S+gA\lambda-a'
<gA+3A2^{D'}
<4A2^{D'},
\]

so

\[
0\le K<4A.
\]

Because `K congruent r mod3`, the integer `J=(K-r)/3` is nonnegative and satisfies `(5)`.

Finally, `(3)` and `J>=0` give the lower bound in `(6)`, while `(5)` gives the upper bound. ∎

## Constructive meaning

The top-boundary theorem is now expressed in the same language as proof-carrying multiplier transducers:

```text
one exact integer root,
one changing odd multiplier,
one bounded normalized carry,
four legal input digits,
four forced output digits,
one full quotient retained.
```

This is substantially stronger than a modular lasso. The output quotient is the actual ordinary most-significant state needed by the next changing cylinder.

## Gap audit

- A canonical digit map at one height does not prove all-time acceptance by the later digit alphabets.
- The multiplier and carry change with the physical height and finite state.
- The four allowed digits remain a proper subset of the 64 possible digits.
- No finite initial integer is supplied.
