# L-8505 — Primitive refund cores satisfy one exact Syracuse equation

**Claim ID:** `L-8505`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Dependencies:** `L-8504`, `T-8505` local signature calculation  
**Scope:** every pair of consecutive legal connectors after the first boundary

## Setup

Let an infinite or finite legal path have types `i_n`, heights

\[
t_n=t_0+16n,
\]

and boundary words `W_n`. Write

```text
b_i=2^i 3^(beta_i),
beta=(2,3,2,1).
```

For `n>=1`, define the primitive prime-to-six core

\[
\boxed{
C_n=
\frac{W_n}{2^{i_n}3^{\beta_{i_{n-1}}}}.}
\tag{1}
\]

By `T-8505`, `C_n` is a positive integer coprime to six and exceeds one.

Put

\[
\boxed{
L_n=11(t_n+17)+i_{n+1}-i_n,}
\tag{2}
\]

\[
\boxed{
G_n=7(t_n+1)+\beta_{i_{n-1}}-\beta_{i_n}.}
\tag{3}
\]

Both exponents are positive.

## Exact core recurrence

Every legal local connector satisfies

\[
\boxed{
2^{L_n}C_{n+1}=3^{G_n}C_n+1.}
\tag{4}
\]

Since `C_(n+1)` is odd,

\[
\boxed{
\nu_2(3^{G_n}C_n+1)=L_n.}
\tag{5}
\]

Since `C_n` is coprime to three, equation `(4)` also gives

\[
\boxed{
\gcd(C_n,C_{n+1})=1.}
\tag{6}
\]

Thus the entire moving connector, after exact signature removal, is one generalized accelerated Syracuse step with affine constant exactly one.

## Proof

The local scaled-tail equation is

\[
2^{11(t_n+17)}W_{n+1}
=3^{7(t_n+1)}W_n+b_{i_n}.
\tag{7}
\]

Use

\[
W_n=2^{i_n}3^{\beta_{i_{n-1}}}C_n,
\]

\[
W_{n+1}=2^{i_{n+1}}3^{\beta_{i_n}}C_{n+1},
\]

\[
b_{i_n}=2^{i_n}3^{\beta_{i_n}}.
\]

Substitution in `(7)` and division by the common factor

\[
2^{i_n}3^{\beta_{i_n}}
\]

gives exactly `(4)` with the exponents `(2)--(3)`.

The core `C_(n+1)` is odd by construction, so the displayed power of two is exact, proving `(5)`. Any common divisor of `C_n` and `C_(n+1)` divides the right side of `(4)` and its first term, hence divides one. This proves `(6)`. ∎

## Intrinsic physical form

By `L-8504`,

\[
n_n+34
=2^{11t_n+5+i_n}3^{\beta_{i_{n-1}}}C_n.
\tag{8}
\]

Therefore `C_n` is exactly the prime-to-six core of the physical shifted boundary value. The exponents `L_n,G_n` are recoverable from the consecutive physical valuation signatures. No symbolic directive is needed to state or verify `(4)`.

## Constructive meaning

`Q-8501` may equivalently be viewed as the search for one finite physical integer whose intrinsic prime-to-six core continues to satisfy the exact valuation demand `(5)` at every scale. The connector problem is not merely a large mixed-radix congruence: it is an explicit nonautonomous Syracuse recurrence with a fixed `+1` toll and bounded signature corrections.
