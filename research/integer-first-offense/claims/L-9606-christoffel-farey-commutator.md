# L-9606 — Farey-neighbor Christoffel blocks have a pure two-prime commutator

**Claim ID:** `L-9606`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** elementary accelerated affine-word algebra  
**Scope:** lower rational mechanical valuation words over the alphabet `{1,2}`

## 1. Mechanical valuation words

For coprime integers

\[
0\le p\le q,
\qquad q\ge1,
\]

define the lower mechanical valuation word

\[
\mathcal C_{p/q}=(a_0,\ldots,a_{q-1}),
\qquad
 a_j=1+\left\lfloor{(j+1)p\over q}\right\rfloor
       -\left\lfloor{jp\over q}\right\rfloor.
\tag{1}
\]

It has length `q`, exactly `p` letters equal to `2`, and total valuation

\[
A(\mathcal C_{p/q})=p+q.
\tag{2}
\]

For an arbitrary nonempty valuation word `w`, write

\[
k_w=|w|,
\qquad
A_w=\sum_{a\in w}a,
\tag{3}
\]

and

\[
C_w=\sum_{j=0}^{k_w-1}3^{k_w-1-j}2^{A_{w,j}},
\qquad
A_{w,j}=\sum_{i<j}a_i.
\tag{4}
\]

Chronological concatenation obeys

\[
\boxed{
C_{uv}=3^{k_v}C_u+2^{A_u}C_v.}
\tag{5}
\]

Define the oriented affine commutator

\[
\boxed{
\Omega(u,v)=C_{uv}-C_{vu}.}
\tag{6}
\]

Equivalently,

\[
\Omega(u,v)
=(2^{A_u}-3^{k_u})C_v
 -(2^{A_v}-3^{k_v})C_u.
\tag{7}
\]

## 2. Stern–Brocot commutator recursion

For all nonempty words `u,v`,

\[
\boxed{
\Omega(u,uv)=2^{A_u}\Omega(u,v),}
\tag{8}
\]

and

\[
\boxed{
\Omega(uv,v)=3^{k_v}\Omega(u,v).}
\tag{9}
\]

### Proof

Apply `(5)` repeatedly. First,

\[
\begin{aligned}
C_{u(uv)}
 &=3^{k_u+k_v}C_u+2^{A_u}C_{uv},\\
C_{(uv)u}
 &=3^{k_u}C_{uv}+2^{A_u+A_v}C_u.
\end{aligned}
\]

Substitution of `C_(uv)` from `(5)` and cancellation gives

\[
C_{u(uv)}-C_{(uv)u}
=2^{A_u}(C_{uv}-C_{vu}),
\]

which is `(8)`. The same calculation on the other side gives

\[
C_{(uv)v}-C_{v(uv)}
=3^{k_v}(C_{uv}-C_{vu}),
\]

which is `(9)`. ∎

## 3. Exact Farey-neighbor formula

Let

\[
{p\over q}<{r\over s},
\qquad
rq-ps=1,
\tag{10}
\]

with both fractions reduced and contained in `[0,1]`. Put

\[
u=\mathcal C_{p/q},
\qquad
v=\mathcal C_{r/s}.
\]

Then

\[
\boxed{
\Omega(u,v)
=-2^{r+s-1}3^{q-1}.}
\tag{11}
\]

For the reverse orientation, if `rq-ps=-1`, then

\[
\boxed{
\Omega(u,v)
=2^{p+q-1}3^{s-1}.}
\tag{12}
\]

Thus the commutator of two Farey-neighbor Christoffel valuation blocks is one signed `{2,3}`-unit, with coefficient exactly one.

### Proof

The base Farey pair is

\[
{0\over1}<{1\over1},
\]

whose words are `(1)` and `(2)`. Directly,

\[
\Omega((1),(2))=(3+2)-(3+4)=-2,
\]

which is `(11)` at the base.

Every ordered Farey-neighbor pair is generated from the base by the two Stern–Brocot moves

\[
(u,v)\longmapsto(u,uv),
\qquad
(u,v)\longmapsto(uv,v).
\tag{13}
\]

Under the first move, the right fraction changes from `r/s` to

\[
{p+r\over q+s}.
\]

Formula `(11)` therefore gains the factor

\[
2^{p+q}=2^{A_u},
\]

exactly as in `(8)`. Under the second move, the left denominator changes from `q` to `q+s`, so `(11)` gains the factor

\[
3^s=3^{k_v},
\]

exactly as in `(9)`. Induction proves `(11)` for every ordered neighbor pair. Swapping `u,v` changes the sign and exchanges the two displayed exponent roles, giving `(12)`. ∎

## 4. Contextual pure-unit replacement

Let `x,y` be arbitrary valuation words, possibly empty. The two fixed-boundary replacements

\[
xuvy
\qquad\hbox{and}\qquad
xvuy
\]

have the same length and total valuation, and

\[
\boxed{
C_{xuvy}-C_{xvuy}
=3^{k_y}2^{A_x}\Omega(u,v).}
\tag{14}
\]

Consequently every contextual swap of Farey-neighbor Christoffel blocks changes the full accelerated numerator by one signed `{2,3}`-unit.

### Proof

In the difference of the two applications of `(5)`, the suffix contribution `C_y` cancels because `uv` and `vu` have the same summary exponents. Removing the common suffix contributes `3^(k_y)`. Removing the common prefix contributes `2^(A_x)`. The remaining difference is exactly `(6)`. ∎

## 5. Why this is useful constructively

PR #45's mechanical-word compiler and local-replacement program require exact numerator atoms at scales far beyond expanded-word enumeration. Equation `(14)` supplies such atoms recursively:

```text
Farey tree node
  -> its two standard parents
  -> swap the parent order in any fixed context
  -> exact signed 2^a 3^b numerator change.
```

The atom is known in closed form from the two parent fractions and the context exponents. No word expansion, numerical approximation, or partial denominator factorization is involved.

This does not by itself solve the full-denominator equation. It converts a hierarchical Christoffel replacement circuit into an exact signed `{2,3}`-unit equation, which is the appropriate finite object for CRT, quotient-digit, or S-unit synthesis.

## Gap audit

- The formula concerns the numerator change; an arbitrary collection of swaps need not span the full denominator.
- Contextual swaps must still be arranged so the compressed derivation is unambiguous and the final word is primitive.
- Passing selected prime-power components is not complete cycle divisibility.
- No nontrivial positive cycle or divergent orbit is claimed.

## Verification

`X-9610` checks `(11)`–`(14)` with exact integers on every ordered Farey-neighbor pair with both denominators at most `100`, together with thousands of independent contextual replacements.