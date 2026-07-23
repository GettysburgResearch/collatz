# T-8513 — A permanent refund tail prepays a linearly growing complete future cylinder

**Claim ID:** `T-8513`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-23  
**Dependencies:** `L-8507`, `T-8510`, `T-8512`  
**Scope:** every permanently refunded tail of a hypothetical infinite ordinary refund orbit

## Motivation

`T-8512` proves that the current ordinary top quotient eventually exceeds products of many future changing radices. The exact path meaning should be stated in cylinder language rather than as a literal shift register: odd multipliers pull every future condition back to one unique current residue.

This theorem identifies the rigorous object. At a late time, the current finite integer has already paid the complete exact cylinder for a linearly growing number of future connectors and still retains a positive ordinary free quotient beyond that cylinder.

## Complete pulled-back path cylinder

Let a permanent noncanonical tail begin at connector index `n`, at height

\[
t=t_n\ge5632.
\]

Fix a later index `n+r`, and put

\[
t_r=t+16r.
\]

For `h>=0`, the complete next-boundary modulus is

\[
\boxed{H_{r+h}=2^{11(t_r+16h+33)}.}
\tag{1}
\]

Fix the actual future finite-control path of the ordinary orbit for the next `s` connectors. There is one unique residue

\[
\boxed{0\le R_{r,s}<P_s(t_r),}
\tag{2}
\]

where

\[
\boxed{P_s(t_r)=\prod_{h=0}^{s-1}H_{r+h},}
\tag{3}
\]

such that the current top quotient `m_(n+r)` realizes those exact `s` future connectors if and only if

\[
\boxed{
m_{n+r}\equiv R_{r,s}\pmod {P_s(t_r)}.}
\tag{4}
\]

Writing

\[
\boxed{
m_{n+r}=R_{r,s}+P_s(t_r)U_{r,s},}
\tag{5}
\]

defines the **complete-cylinder free quotient** `U_(r,s)`.

## Theorem

### 1. Uniform prepaid horizon

For every `r>=288`, put

\[
s=\left\lfloor\frac r{288}\right\rfloor.
\]

Then

\[
\boxed{U_{r,s}\ge1.}
\tag{6}
\]

Thus, after `r` permanent-refund connectors, the current finite ordinary state has paid every exact arithmetic condition for its next `floor(r/288)` connectors and still has at least one complete free lift beyond that whole future cylinder.

### 2. Sharper late horizon

For every

\[
\boxed{r\ge100909,}
\]

put

\[
s=\left\lfloor\frac r{233}\right\rfloor.
\]

Then

\[
\boxed{U_{r,s}\ge1.}
\tag{7}
\]

Consequently

\[
\boxed{
\liminf_{r\to\infty}
\frac{
\max\{s:U_{r,s}\ge1\}
}{r}
\ge\frac1{233}.}
\tag{8}
\]

The value `233` is the first integer above the exact asymptotic reciprocal

\[
\left(-1+\frac{\sqrt{1101430}}{1045}\right)^{-1}
=232.721150\ldots .
\tag{9}
\]

## Proof

### Unique pulled-back residue

Proceed by induction on `s`.

For `s=1`, `L-8507` gives one exact current residue modulo `H_r` for the actual next transition.

Assume the first `s` transitions select one residue

\[
m=R_s+P_su
\]

and that after those transitions the exact top quotient has the affine form

\[
m^{(s)}=S_s+A_su,
\]

where `A_s` is odd. The next legal connector requires

\[
m^{(s)}\equiv\rho_s\pmod {H_{r+s}}.
\]

Because `A_s` is odd, it is invertible modulo the power of two `H_(r+s)`, so this condition selects one unique residue

\[
u\equiv v_s\pmod {H_{r+s}}.
\]

Substitution gives

\[
R_{s+1}=R_s+P_sv_s,
\qquad
P_{s+1}=P_sH_{r+s}.
\]

This proves `(2)--(4)` for every `s`. Equation `(5)` is ordinary Euclidean division.

### Uniform horizon

Since `0<=R_(r,s)<P_s`, equation `(5)` gives

\[
U_{r,s}\ge1
\quad\Longleftrightarrow\quad
m_{n+r}\ge P_s(t_r).
\tag{10}
\]

`T-8512` proves precisely this inequality for

\[
s=\left\lfloor r/288\right\rfloor,
\qquad r\ge288.
\]

This proves `(6)`.

### Sharper denominator 233

`T-8510` gives the lower bound

\[
\log_2m_{n+r}
>
175r+
\frac{
r(63t-353831)+504r(r-1)
}{665}.
\tag{11}
\]

The exact future-cylinder size is

\[
\log_2P_s(t_r)
=11s(t+16r+33)+88s(s-1).
\tag{12}
\]

Take

\[
s=\left\lfloor r/233\right\rfloor\le r/233.
\]

Using `(12)`,

\[
\log_2P_s(t_r)
\le
\frac{11r}{233}(t+16r+33)
+
\frac{88r^2}{233^2}.
\tag{13}
\]

Subtracting `(13)` from `(11)` gives the exact lower bound

\[
\boxed{
\log_2m_{n+r}-\log_2P_s(t_r)
>
\frac{r}{36102185}
\left(
32816r+1715812t-12974855475
\right).}
\tag{14}
\]

The bracket is increasing in both `r` and `t`. At the smallest permanent-refund height `t=5632`, it is positive exactly when

\[
r>\frac{3311402291}{32816}
=100908.1634\ldots .
\]

Thus `(14)` is positive for every `t>=5632` and `r>=100909`. Equation `(10)` proves `(7)`.

Finally, `1/233` is strictly below the positive root `c` of

\[
88c^2+176c=504/665,
\]

namely

\[
c=-1+\sqrt{1101430}/1045.
\]

This proves `(8)--(9)`. ∎

## Constructive significance

The result is stronger and more precise than a bit-length surplus:

```text
at time n+r,
the one current finite ordinary quotient
already satisfies the exact pulled-back cylinder
for >= floor(r/288) future physical connectors,
and retains a positive free quotient beyond it.
```

At sufficiently large `r`, the certified horizon improves to `floor(r/233)`.

This does not preload future data. The residue `R_(r,s)` is selected by the actual finite path and is present in the current ordinary integer. The theorem shows that permanent refund continually rebuilds positive top freedom even after an expanding block of future exact constraints is paid.

## Gap audit

- The theorem is conditional on an infinite ordinary path already existing.
- A positive free quotient beyond an `s`-step cylinder does not prove the next, `(s+1)`-st digit is legal.
- The horizon production rate is positive but below one connector per connector; it does not by itself close an induction from a finite prefix.
- The pulled-back mixed-radix digits are transformed path-cylinder data, not a literal unmodified queue of future residues.
- No initial integer or self-covering stack rewrite is supplied.