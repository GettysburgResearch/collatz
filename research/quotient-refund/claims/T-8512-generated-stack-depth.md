# T-8512 — Permanent refund creates linearly growing raw radix capacity

**Claim ID:** `T-8512`  
**Status:** `SUPERSEDED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-23  
**Corrected:** 2026-07-23  
**Superseded by:** `T-8513`; independently diagnosed and repaired by PR #48 `R-8203` / `L-8210`  
**Dependencies:** `T-8510`, `T-8511`  
**Scope:** numerical size of the top quotient on a permanent-refund tail

## Correction note

The numerical inequalities in the original submission are correct. The original identification of the **plain Euclidean mixed-radix digits of `m`** with later legality residues is false.

One transition is

```text
m_n      = rho_n + H_n*ell_n,
m_(n+1) = sigma_n + A_n*ell_n.
```

The next legal cylinder is imposed on

```text
sigma_n + A_n*ell_n mod H_(n+1),
```

not on the plain digit

```text
ell_n mod H_(n+1).
```

Therefore the raw expansion below measures radix **capacity**, not directly readable future-cylinder content. This first invalid interpretation was independently identified in PR #48 `R-8203`.

`T-8513` supplies the corrected native theorem by pulling every later condition back through the intervening odd affine maps. PR #48 `L-8210` gives the equivalent transported-stack cocycle and records the alternate convention that omits the already-paid current cylinder, producing a one-level index shift.

The original mathematical size proof is retained below in narrowed form.

## Raw mixed-radix capacity

Let a permanent noncanonical tail begin at connector index `n`, at height

\[
t=t_n\ge5632,
\]

with positive top quotient `m_n`. At a later index `n+r`, put

\[
t_r=t+16r.
\]

The future complete top-boundary radices are

\[
\boxed{
H_{r+h}=2^{11(t_r+16h+33)},
\qquad h\ge0.}
\tag{1}
\]

For `s>=0`, put

\[
\boxed{
P_s(t_r)=\prod_{h=0}^{s-1}H_{r+h}.}
\tag{2}
\]

Define the **raw radix capacity** of `m_(n+r)` to be the largest `s` for which

\[
\boxed{m_{n+r}\ge P_s(t_r).}
\tag{3}
\]

This is an ordinary size property. It makes no claim that the plain Euclidean digits are the transported legality digits.

## Valid numerical theorem

### Uniform capacity

For every `r>=288`,

\[
\boxed{
m_{n+r}
>
P_{\lfloor r/288\rfloor}(t_r).}
\tag{4}
\]

### Sharper late capacity

For every

\[
\boxed{r\ge100909,}
\]

\[
\boxed{
m_{n+r}
>
P_{\lfloor r/233\rfloor}(t_r).}
\tag{5}
\]

Thus the raw capacity grows linearly, with asymptotic lower rate at least `1/233`.

## Proof

`T-8510` gives

\[
\boxed{
\log_2m_{n+r}
>
175r+
\frac{
r(63t-353831)+504r(r-1)
}{665}.}
\tag{6}
\]

From `(1)--(2)`,

\[
\boxed{
\log_2P_s(t_r)
=11s(t+16r+33)+88s(s-1).}
\tag{7}
\]

For

\[
s=\left\lfloor r/288\right\rfloor,
\]

subtracting the upper bound obtained from `(7)` from `(6)` gives

\[
\boxed{
\begin{aligned}
\log_2m_{n+r}-\log_2P_s(t_r)
>{}&r\left(
\frac{1547}{27360}t
+
\frac{143531}{984960}r\\
&\qquad-
\frac{4584925}{12768}
\right).
\end{aligned}}
\tag{8}
\]

The bracket is increasing in `t,r` and at `t=5632,r=288` equals

\[
\frac{84263}{63840}>0.
\]

This proves `(4)`.

For

\[
s=\left\lfloor r/233\right\rfloor,
\]

the exact corresponding difference is positive for all `t>=5632,r>=100909`; in the simplified form used by `T-8513`,

\[
\boxed{
\log_2m_{n+r}-\log_2P_s(t_r)
>
\frac{r}{36102185}
\left(
32816r+1715812t-12974855475
\right).}
\tag{9}
\]

The bracket is positive at the stated endpoint and increases thereafter, proving `(5)`. ∎

## Correct physical interpretation

The retained size theorem implies that the current top quotient is large enough to contain many future radices. It does **not** identify their plain digits with legality data.

Two corrected interpretations are now available:

1. `T-8513` counts a complete pulled-back path cylinder **including the current already-selected connector**. Its bounds are `floor(r/288)` uniformly and `floor(r/233)` late.
2. PR #48 `L-8210` places the transported stack on the free lift after removing the current radix. Under that convention the corresponding bounds lose one level:
   ```text
   floor(r/288)-1,
   floor(r/233)-1.
   ```

The two conventions are consistent.

## Gap audit

- Raw capacity is not routing content.
- The numerical theorem is conditional on a hypothetical permanent-refund orbit.
- The transported digits require the inverse-affine cocycle of `T-8513` / PR #48 `L-8210`.
- Neither the raw capacity nor the repaired stack constructs an infinite ordinary path.
- No `K-85xx` candidate is produced.