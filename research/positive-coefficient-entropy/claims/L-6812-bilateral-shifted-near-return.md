# L-6812 — Bilateral shifted-denominator identity and the one-third displacement window

**Claim ID:** `L-6812`  
**Status:** **PROPOSED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6803`; exact shortcut-Collatz affine expansion  
**Scope:** canonical non-descending coefficient-first-crossing words

## 1. Setup

Let `w` be coefficient-first-crossing of length `j` and weight `q`.  Put

\[
P=2^j,
\qquad
Q=3^q,
\qquad
D=P-Q>0,
\]

and write

\[
T_w(x)={Qx+A_w\over P}.
\]

Let

\[
(r,s)
\]

be the canonical source--endpoint pair from `L-6803`.  Assume that it does
not descend, and put

\[
\boxed{d=s-r\ge0.}
\tag{1}
\]

## 2. Bilateral exact identity

The canonical affine equation is

\[
P(r+d)=Qr+A_w.
\]

Rearranging in source coordinates gives

\[
\boxed{
A_w=Dr+Pd,}
\tag{2}
\]

while substituting `s=r+d` gives the endpoint form

\[
\boxed{
A_w=Ds+Qd.}
\tag{3}
\]

Consequently

\[
\boxed{
 r={A_w-Pd\over D},
\qquad
 s={A_w-Qd\over D}.}
\tag{4}
\]

The two complete-denominator congruences are equivalent:

\[
\boxed{
D\mid A_w-Pd
\iff
D\mid A_w-Qd,}
\tag{5}
\]

because `P congruent Q (mod D)`.

Thus one must retain the coordinate convention:

```text
quotient of A_w-Pd by D = canonical source;
quotient of A_w-Qd by D = canonical endpoint.
```

The congruence may use either shift, but the exact integer quotient changes by
`d`.

## 3. Sharpened normalized-remainder bound

Put

\[
\alpha={\log2\over\log3},
\qquad
D_m=q_m-\alpha m.
\]

The exact normalized remainder is

\[
\boxed{
{A_w\over P}
=
{1\over2}
\sum_{m=1}^{j}
 v_{m-1}3^{D_j-D_m}.}
\tag{6}
\]

The final crossing bit is even.  Hence every nonzero summand in `(6)` comes
from an odd step ending at a proper time `m<j`.

At such a time,

\[
D_m
=D_{m-1}+1-\alpha
\ge1-\alpha,
\tag{7}
\]

while first crossing gives

\[
D_j<0.
\tag{8}
\]

Therefore every nonzero summand in `(6)` is strictly smaller than

\[
{1\over2}3^{-(1-\alpha)}
={1\over2}3^{\alpha-1}
={1\over3},
\tag{9}
\]

because `3^alpha=2`.  There are exactly `q` odd steps, so

\[
\boxed{
0<{A_w\over P}<{q\over3}.}
\tag{10}
\]

This improves the earlier universal `q/2` ceiling.

## 4. One-third displacement window

Equation `(2)` and `r>=1` give

\[
Pd<A_w.
\]

Together with `(10)`,

\[
\boxed{
0\le d<{A_w\over P}<{q\over3}<{\alpha j\over3}<{j\over3}.}
\tag{11}
\]

Thus every acyclic canonical first-crossing obstruction is an exact ordinary
near-return

\[
\boxed{
T^j(r)=r+d,
\qquad
1\le d<q/3,}
\tag{12}
\]

while `d=0` is precisely the positive-cycle level.

For one fixed word, the complete displacement search is therefore

\[
\boxed{
 d\in\mathbf Z,
\qquad
0\le d<q/3,}
\tag{13}
\]

not the older interval `0<=d<j/2`.

## 5. Prime-power form

Let `Q_s` be any prime-power divisor of `D`.  Equation `(5)` gives the local
condition

\[
\boxed{
A_w\equiv Qd=3^q d\pmod {Q_s}.}
\tag{14}
\]

This is the form used by the excess-path compiler in `L-6809`.  After the
local paths reconstruct the word, the ordinary source must still be computed
from

\[
r=(A_w-Pd)/D,
\]

and checked in the canonical positive range.

## 6. Cross-branch coordinate audit

A shifted-denominator formula is sometimes written as

\[
A_w=nD+dQ.
\]

By `(3)`, this formula uses

\[
n=s,
\]

the **endpoint**, not the source.  If `n` is intended to denote the source,
the correct identity is

\[
\boxed{A_w=nD+dP.}
\tag{15}
\]

Confusing the two leaves the modular congruence unchanged but shifts the
physical candidate by `d`.  It therefore affects positivity, replay, and any
candidate interpretation.

## 7. Consequences

The delayed-crossing and cycle lanes share the one exact family

\[
\boxed{
A_w=Dr+Pd=Ds+Qd,
\qquad
0\le d<q/3.}
\tag{16}
\]

- `d=0`: exact positive cycle;
- `d>0`: exact acyclic CST near-return;
- every complete prime-power factor must reconstruct the same `d`;
- the source and endpoint quotients must not be interchanged.

## 8. Gap audit

- The one-third window still grows linearly with `j`.
- Divisibility by proper factors does not imply the complete equation.
- The sharpened range does not prove that the displacement residue misses the
  interval.
- `d=0` retains the nontrivial positive-cycle alternative.
- No proof of CST, either boxed statement, or Collatz is claimed.
