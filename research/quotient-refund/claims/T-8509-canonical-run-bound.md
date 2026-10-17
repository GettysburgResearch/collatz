# T-8509 — Canonical lift runs are uniformly bounded and eventually have length at most 233

**Claim ID:** `T-8509`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-23  
**Dependencies:** `L-8506`, `L-8507`, `T-8507`; the exact integer inequality `3^665>2^1054`  
**Scope:** every hypothetical infinite ordinary orbit of the intrinsic core decoder

## Statement

Let

\[
(t_n,\gamma_n,i_n,C_n),
\qquad
t_n=t_0+16n,
\]

be an ordinary orbit of `T-8507`. At each step write the complete top-boundary quotient in the form supplied by `L-8507`:

\[
m_n=\rho_n+H_n\ell_n,
\qquad
H_n=2^{11(t_n+33)},
\qquad
\ell_n\ge0.
\]

Call step `n` **canonical** when `ell_n=0`.

### General run inequality

Suppose

\[
\ell_n=\ell_{n+1}=\cdots=\ell_{n+r}=0
\tag{1}
\]

for some `r>=1`. Thus both endpoint states and every state between them use their canonical top-boundary representative. Put `t=t_n`. Then necessarily

\[
\boxed{
\frac{
r(63t-121080)+504r(r-1)
}{665}
<
22(t+16r)+559.
}
\tag{2}
\]

### Uniform canonical-run bound

For every `t>=3760`, inequality `(2)` fails at `r=470`. Consequently:

\[
\boxed{
\text{no ordinary path has 471 consecutive canonical lifts}
}
\tag{3}
\]

once it reaches height `3760`.

Equivalently, every hypothetical infinite ordinary refund path has a noncanonical, genuinely refunded top lift at least once in every `471` consecutive connectors. In particular:

\[
\boxed{
\liminf_{N\to\infty}
\frac{
\#\{0\le n<N:\ell_n\ge1\}
}{N}
\ge\frac1{471}.
}
\tag{4}
\]

### Asymptotic strengthening

For every multiple of `16` with

\[
\boxed{t\ge1{,}140{,}416,}
\]

inequality `(2)` already fails at `r=233`. Therefore no such late orbit segment has `234` consecutive canonical lifts, and every hypothetical infinite path satisfies the stronger asymptotic density bound

\[
\boxed{
\liminf_{N\to\infty}
\frac{
\#\{0\le n<N:\ell_n\ge1\}
}{N}
\ge\frac1{234}.
}
\tag{5}
\]

Combined with `T-8508`, every noncanonical event occurring from height `3776` satisfies

\[
m_{n+1}>2m_n.
\]

Thus the canonical exception cannot absorb the linear refund architecture. Any infinite path must regenerate and spend a genuine ordinary top quotient with positive lower frequency.

## Proof

### Canonical states have only linear height

At a canonical state, `L-8506` and `L-8507` give

\[
C=\widehat R+Qm,
\qquad
0\le\widehat R<Q,
\qquad
0\le m<H,
\]

where

\[
Q=3\,2^{D+6},
\qquad
D=11(t+17)-i,
\qquad
H=2^{11(t+33)}.
\]

Since `3<4` and `1+H<2H`,

\[
C<Q(1+H)
<2^{D+8}2^{11(t+33)+1}.
\]

Using `D<=11(t+17)=11t+187`, one obtains the uniform canonical cap

\[
\boxed{
\log_2 C<22t+559.
}
\tag{6}
\]

### Every legal core step has increasing linear gain

Let the next type at height `t` be `j`. The exact core recurrence is

\[
C^+=\frac{3^GC+1}{2^{D+j}}
>
\frac{3^G}{2^{D+j}}C,
\]

with

\[
G=7(t+1)+\gamma-\beta_i\ge7t+5,
\]

and

\[
D+j=11(t+17)-i+j\le11t+190.
\]

The exact comparison

\[
3^{665}>2^{1054}
\]

therefore gives

\[
\boxed{
\log_2\frac{C^+}{C}
>
\frac{63t-121080}{665}.
}
\tag{7}
\]

Indeed

\[
1054(7t+5)-665(11t+190)=63t-121080.
\]

### Summation across a canonical run

Under `(1)`, the endpoint state `n+r` is canonical, so `(6)` applies there. Summing `(7)` over the `r` transitions from `n` to `n+r`, using

\[
t_{n+s}=t+16s,
\]

gives

\[
\log_2 C_{n+r}
>
\log_2 C_n
+
\frac{
r(63t-121080)+504r(r-1)
}{665}.
\tag{8}
\]

Since `C_n>=1`, the first term on the right is nonnegative. The canonical endpoint cap is

\[
\log_2 C_{n+r}
<22(t+16r)+559.
\tag{9}
\]

Combining `(8)--(9)` proves the necessary inequality `(2)`.

### The uniform number 471

At `r=470` and `t=3760`, the numerator obtained after moving the right side of `(2)` to the left is

\[
\begin{aligned}
&470(63\cdot3760-121080)
+504\cdot470\cdot469\\
&\qquad
-665\bigl(22(3760+16\cdot470)+559\bigr)\\
&=\boxed{124585}>0.
\end{aligned}
\]

Thus `(2)` fails. For fixed `r=470`, the left-minus-right expression has coefficient

\[
63\cdot470-665\cdot22=14980>0
\]

in `t`, so the contradiction only strengthens for every `t>=3760`.

Condition `(1)` with `r=470` is exactly a string of `471` consecutive canonical lifts. This proves `(3)`. Partitioning a late orbit into consecutive blocks of length `471` proves `(4)`.

### The eventual number 234

For `r=233`, the coefficient of `t` in the same left-minus-right expression is

\[
63\cdot233-665\cdot22=49>0.
\]

At the first multiple of sixteen above the exact crossing point,

\[
t=1{,}140{,}416,
\]

the expression equals

\[
\boxed{593}>0.
\]

Hence `(2)` fails there and at every greater height. Condition `(1)` with `r=233` is a string of `234` consecutive canonical lifts. The late orbit may therefore be partitioned into blocks of length `234`, each containing a noncanonical event, which proves `(5)`. ∎

## Eureka consequence

The two apparent escape modes are not symmetric:

```text
noncanonical lift:
  exact multiplicative refund, eventually more than doubling;

canonical lift:
  an absolute O(t)-bit core cap.
```

But the exact Syracuse recurrence accumulates `Omega(r*t+r^2)` bits across a run. The quadratic growth and linear cap are incompatible. Therefore an infinite ordinary orbit must repeatedly regenerate a genuinely free top boundary; it cannot hide forever in least representatives.

## Gap audit

- Positive density of refunded steps does not prove that any finite initial core reaches the required residues.
- Canonical steps may still occur, and the theorem does not control the size change of the top quotient across them.
- The constants `471` and `234` are rigorous bounds, not claimed optimal.
- The theorem is conditional on the existence of an infinite ordinary core orbit; it does not construct one.
