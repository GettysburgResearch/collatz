# L-9802 — Dyadic logarithmic bulk lift

Claim ID: `L-9802`  
Title: Dyadic inverse powers form an exact quadratic lift with a normalized logarithmic limit  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01-a`  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: standard 2-adic LTE and logarithm facts  
Scope: odd-base inverse-power Hensel lanes  
Related counterexample candidates: none

## Statement

Let `q>1` and `a>0` be odd. Put

\[
\sigma=\nu_2(q^2-1)
=\nu_2(q-1)+\nu_2(q+1)\ge3.
\tag{1}
\]

For `m>=1`, define in `Z_2`

\[
y_m=q^{-a2^m},
\qquad
u_m=\frac{y_m-1}{2^{m+\sigma-1}}.
\tag{2}
\]

Then `u_m` is odd and

\[
\boxed{u_{m+1}=u_m+2^{m+\sigma-2}u_m^2},
\qquad
\boxed{\nu_2(u_{m+1}-u_m)=m+\sigma-2}.
\tag{3}
\]

It converges to the explicit odd 2-adic unit

\[
\boxed{u_\infty=-\frac{a\log(q^2)}{2^\sigma}},
\qquad
\boxed{\nu_2(u_\infty-u_m)=m+\sigma-2}.
\tag{4}
\]

There is also an exact odometer form. Fix `g_0,t,r>=0`, and set

\[
g_s=g_0+as,
\quad \zeta_s=q^{-g_s},
\quad
\mu_s=[-\zeta_s]_{2^{r+1}},
\quad
\omega_s=\frac{\mu_s+\zeta_s}{2^{r+1}},
\tag{5}
\]

where the bracket is the canonical residue in `[0,2^(r+1))`. Choose `H>=1`
so that

\[
d=H+r+2-\sigma\ge1,
\qquad \Delta_H=2^d.
\tag{6}
\]

For every nonzero integer `j` with `t + j Delta_H >= 0`,

\[
\mu_{t+j\Delta_H}=\mu_t,
\qquad
\boxed{
\nu_2(\omega_{t+j\Delta_H}-\omega_t)=H+\nu_2(j)}.
\tag{7}
\]

For `q=3`, `a=7`, and `sigma=3`, this specializes to

\[
u_m=\frac{3^{-7\cdot2^m}-1}{2^{m+2}},
\quad
u_{m+1}=u_m+2^{m+1}u_m^2,
\quad
u_\infty=-\frac{7\log9}{8},
\tag{8}
\]

with `nu_2(u_infinity - u_m) = m + 1`. This independently recovers and strengthens
the algebraic core of `PR3/L-0019`, `PR3/L-0023`, and the odometer calculation
used by `PR3/L-0024`.

## Definitions

The logarithm is the convergent 2-adic series

\[
\log(1+z)=\sum_{n\ge1}(-1)^{n+1}\frac{z^n}{n}
\qquad(z\in4\mathbb Z_2).
\]

We use the standard facts

\[
\lim_{n\to\infty}\frac{x^{2^n}-1}{2^n}=\log x
\quad(x\in1+8\mathbb Z_2)
\tag{9}
\]

and `nu_2(log x)=nu_2(x-1)` for `x in 1+4 Z_2`.

## Proof

For the even exponent `a2^m`, 2-adic LTE gives

\[
\nu_2(q^{a2^m}-1)
=\nu_2(q-1)+\nu_2(q+1)+m-1
=m+\sigma-1.
\tag{10}
\]

Multiplication by the odd unit `q^(-a2^m)` preserves valuation, so `u_m` is
integral and odd. Since `y_(m+1) = y_m^2`, write

\[
y_m=1+2^{m+\sigma-1}u_m.
\]

Squaring and factoring the next normalization gives

\[
\begin{aligned}
y_{m+1}
&=1+2^{m+\sigma}u_m+2^{2m+2\sigma-2}u_m^2\\
&=1+2^{m+\sigma}
  (u_m+2^{m+\sigma-2}u_m^2),
\end{aligned}
\]

which proves the recurrence. Oddness makes its difference valuation exact.

For the limit, put `x=q^(-2a) in 1+8 Z_2`. Equation (9), with `n=m-1`,
gives

\[
u_m
=2^{-\sigma}\frac{x^{2^{m-1}}-1}{2^{m-1}}
\longrightarrow
2^{-\sigma}\log x
=-\frac{a\log(q^2)}{2^\sigma}.
\]

The logarithm valuation fact and (1) make this limit odd. Also

\[
u_\infty-u_m=\sum_{n=m}^\infty(u_{n+1}-u_n).
\]

The summands have strictly increasing valuations beginning at
`m+sigma-2`; the ultrametric inequality is sharp at the unique first term.
This proves the exact error valuation in (4).

Finally, for negative `j`, multiplication by the odd unit
`q^(a|j|Delta_H)` shows
`nu_2(q^(-a|j|Delta_H)-1)=nu_2(q^(a|j|Delta_H)-1)`. Thus positive-exponent
LTE applies for either sign of `j`, and (6) gives

\[
\begin{aligned}
\nu_2(q^{aj\Delta_H}-1)
&=\sigma+\nu_2(j\Delta_H)-1\\
&=H+r+1+\nu_2(j).
\end{aligned}
\tag{11}
\]

The same valuation holds for
`zeta_(t+j Delta_H) - zeta_t`. It is at least `r+1`, so the canonical `mu`
residues agree. Division by `2^(r+1)` proves (7). ∎

## Motivation

The collision/Hensel stack's moving bulk is not arbitrary: it is a canonical
sequence of finite-precision approximations to one normalized 2-adic
logarithm. The recurrence propagates existing digits, while (4) identifies the
position of the next genuinely new digit.

## Dependency audit

- Equation (10) is standard `p=2` LTE.
- Equation (9) and logarithm valuation preservation are standard and stated
  explicitly above.
- No PR #3 claim is used; its labels are only specializations.

## Gap audit

- The logarithmic limit is a completion object, not a finite ordinary stack.
- Same-precision recurrence does not generate a longer prefix for free.
- Odometer control does not prove integrality of the residual recurrence.
- The condition `d>=1` in (6) is essential for the even-exponent LTE formula.

## Adversarial tests

- For `q=3`, (3) is exactly the recurrence in `PR3/L-0023`.
- Taking `j=2^s` in (7) raises agreement by exactly `s`, not merely at least
  `s`.
- If `a` is even, the chosen normalization need not make `u_m` odd.
- Noncanonical choices of `mu_s` can destroy their equality in (7).

## Remaining uncertainty

None in the abstract calculation. Applying it to a counterexample still needs
the finite forward router and ordinary initialization absent from PR #3.

## Suggested next attack

Express the next non-stabilized bit of `u_infinity` in the finite residual
state of one 256-transition stage, without treating the logarithmic limit as
an oracle.
