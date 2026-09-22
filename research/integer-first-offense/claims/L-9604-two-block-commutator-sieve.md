# L-9604 — Two-block cycle words have a commutator divisibility sieve

**Claim ID:** `L-9604`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-22  
**Dependencies:** elementary affine-block algebra; compatible with PR #34 `L-9904` and `L-9906`  
**Scope:** a negative-drift accelerated block repeated `m` times followed by a positive-drift block repeated `n` times

## 1. Two affine blocks

Let accelerated valuation blocks `u,v` have affine summaries

\[
F_u(x)={px+c\over q},
\qquad
F_v(x)={rx+d\over s},
\tag{1}
\]

where

\[
p=3^{k_u},\quad q=2^{A_u},\quad
r=3^{k_v},\quad s=2^{A_v},\quad c,d>0.
\]

Assume

\[
p>q
\qquad\text{and}\qquad
s>r.
\tag{2}
\]

Thus `u` has the negative rational fixed point

\[
z={c\over q-p}<0,
\]

while `v` has the positive rational fixed point

\[
\xi={d\over s-r}>0.
\]

Define the oriented affine commutator

\[
\boxed{
\Omega(u,v)=(q-p)d-(s-r)c.}
\tag{3}
\]

Blocks of opposite drift sign cannot have `Omega=0`: equality would give the same finite fixed point with opposite signs.

## 2. Powers and the mixed denominator

For `m,n>=1`, consider the chronological word

\[
u^m v^n.
\]

Put

\[
G_m={p^m-q^m\over p-q}>0
\tag{4}
\]

and

\[
D_{m,n}=q^m s^n-p^m r^n.
\tag{5}
\]

The positive-cycle regime is `D_(m,n)>0`.

The fixed point of the composite satisfies

\[
\boxed{
x_{m,n}-\xi
=-{r^nG_m\Omega(u,v)\over(s-r)D_{m,n}}.}
\tag{6}
\]

## 3. Necessary commutator divisibility

If `u^m v^n` is a positive accelerated cycle certificate, then `x_(m,n)` is an integer. Multiplying `(6)` by `(s-r)D_(m,n)` shows

\[
D_{m,n}\mid r^nG_m\Omega(u,v).
\]

Moreover

\[
\gcd(D_{m,n},r)=1,
\]

because modulo the odd power `r`, the first term `q^m s^n` is a power of two and hence a unit. Therefore

\[
\boxed{
D_{m,n}\mid G_m\Omega(u,v).}
\tag{7}
\]

This is a strong necessary sieve: the mixed denominator must divide an integer that is independent of the repetition count `n` of the contracting block.

A surviving row must still pass the exact standard numerator divisibility test. Equation `(7)` is used only to eliminate rows, never as a sufficient cycle certificate.

## 4. Terminal size elimination

For fixed `u,v,m`, once `D_(m,n)>0`, the sequence is strictly increasing in `n`:

\[
\begin{aligned}
D_{m,n+1}
&=sD_{m,n}+p^mr^n(s-r)\\
&>D_{m,n}.
\end{aligned}
\tag{8}

Consequently, as soon as

\[
\boxed{
D_{m,n}>|G_m\Omega(u,v)|,}
\tag{9}
\]

no present or later `n` can satisfy `(7)`. Every fixed pair `(u,v,m)` therefore has a finite, explicitly terminated search over **all** positive-drift repetition counts `n`.

## 5. Negative three-cycle specialization

Take

\[
u=(1,2),
\qquad
(p,q,c)=(9,8,5),
\qquad z=-5.
\]

For a contracting block `v` with summary `(r,s,d)`, equation `(3)` becomes

\[
\boxed{
\Omega(u,v)=-d-5(s-r).}
\tag{10}
\]

The sieve is therefore

\[
\boxed{
8^ms^n-9^mr^n
\mid
(9^m-8^m)\bigl(d+5(s-r)\bigr).}
\tag{11}
\]

The right side contains only one negative-cycle geometric factor and one fixed block commutator.

## 6. Exact finite packet

`X-9604` enumerates every primitive contracting valuation word `v` with

```text
1 <= length(v) <= 5
1 <= each valuation <= 6
2^A(v) > 3^k(v)
v != (2)
```

There are `9,237` such blocks. For each one it checks

```text
1 <= m <= 1,000
all n in the positive-drift regime,
terminated only by the proved size bound (9).
```

The exact census contains

```text
761,934 reduced divisibility rows,
9,237,000 terminal size eliminations,
0 exact cycle hits.
```

Thus no nontrivial positive cycle of the form

\[
(1,2)^m v^n
\]

occurs in the frozen block library and `m` range.

## 7. Strategic consequence

A two-block compressed grammar can be searched without expanding either repeated block:

```text
block summaries
  -> fixed-point commutator
  -> one n-independent divisibility bound
  -> monotone terminal cutoff
  -> full numerator test on survivors.
```

The theorem also explains why choosing two blocks with an almost common fixed point is attractive: a small commutator makes `(7)` even harder to satisfy, while exact zero commutator collapses to powers of one primitive block rather than creating a new cycle.

## 8. Gap audit

- The experiment freezes one negative block and a bounded contracting-block library.
- More than two macro-block types are not covered.
- The theorem supplies a necessary sieve, not a sufficient certificate.
- Large contracting words with scale-dependent commutator remain open.
- No nontrivial cycle, divergent seed, or Collatz counterexample is claimed.
