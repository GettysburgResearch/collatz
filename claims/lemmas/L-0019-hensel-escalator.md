# L-0019 — Hensel escalator for normalized connector prefixes

Claim ID: `L-0019`  
Title: Exact nonlinear padding jumps that preserve and extend the normalized tower stack prefix  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Dependencies: `L-0016`, `L-0017`, `L-0018`  
Scope: one padded tower type with odd cycle odd-count  
Related counterexample candidates: none

## Statement

Use one tower type from `L-0016`, with

\[
g_t=g_0+at,
\]

where \(a\) is odd, and with fixed recovery depth \(r\).

In the 2-adic integers define

\[
\zeta_t=3^{-g_t}\in\mathbb Z_2.
\tag{1}
\]

Let \(\mu_t\) be the canonical finite recovery residue

\[
\mu_t\equiv-\zeta_t\pmod{2^{r+1}},
\qquad
0\le\mu_t<2^{r+1},
\tag{2}
\]

and define the **normalized connector tail**

\[
\boxed{
\omega_t=
\frac{\mu_t+\zeta_t}{2^{r+1}}
\in\mathbb Z_2.
}
\tag{3}
\]

Then:

### 1. Exact Hensel jump

For every requested prefix precision \(H\ge1\), put

\[
\boxed{
\Delta_H=2^{H+r-1}.
}
\tag{4}
\]

Then

\[
\boxed{
\mu_{t+\Delta_H}=\mu_t
}
\tag{5}
\]

and

\[
\boxed{
\omega_{t+\Delta_H}
\equiv
\omega_t
\pmod{2^H}.
}
\tag{6}
\]

Thus the first \(H\) LSD-first bits of the normalized stack survive unchanged when the counter advances by the exact order-sized jump \(\Delta_H\).

### 2. Low connector prefix is target-independent

For the tower output block, `L-0016` gives

\[
B_t=3^b\frac{3^{g_t}\mu_t+1}{2^{r+1}},
\qquad
G_t=g_t+b.
\tag{7}
\]

Consider a connector from this output to any later tower input

\[
\bar A+2^{\bar K}h'
\]

whose binary anchor satisfies

\[
2^H\mid\bar A
\tag{8}
\]

and whose depth satisfies \(\bar K\ge H\). Let \(\eta\) be the canonical connector seed from `L-0017`:

\[
B_t+3^{G_t}\eta
\equiv
\bar A
\pmod{2^{\bar K}}.
\tag{9}
\]

Then its low \(H\) bits are

\[
\boxed{
\eta\equiv-\omega_t\pmod{2^H}.
}
\tag{10}
\]

They do not depend on the target tower type or target height once the target anchor is divisible by \(2^H\).

### 3. Append-only normalized lane

Choose precisions \(H_0<H_1<\cdots\) and counters recursively by

\[
t_{n+1}=t_n+2^{H_n+r-1}.
\tag{11}
\]

Then

\[
\omega_{t_{n+1}}\equiv\omega_{t_n}\pmod{2^{H_n}}.
\tag{12}
\]

The finite words

\[
\omega_{t_n}\bmod2^{H_n}
\]

therefore form a nested LSD-first prefix sequence. At this normalized level, the stack can be updated by appending higher bits rather than rewriting its established lower prefix.

This is the first exact nonlinear counter schedule in the packet that bypasses the fixed-affine obstruction of `T-0021`.

## Proof

By `L-0018`, because \(a\) is odd,

\[
\operatorname{ord}_{2^J}(3^a)=2^{J-2}
\]

for every \(J\ge3\). Take

\[
J=H+r+1.
\]

Then

\[
\Delta_H=2^{J-2}
\]

and hence

\[
3^{a\Delta_H}\equiv1\pmod{2^{H+r+1}}.
\tag{13}
\]

Therefore

\[
\zeta_{t+\Delta_H}
=3^{-g_t-a\Delta_H}
\equiv3^{-g_t}
=\zeta_t
\pmod{2^{H+r+1}}.
\tag{14}
\]

Reduction modulo \(2^{r+1}\) makes the defining residues in (2) equal, proving (5). Subtracting the two versions of (3) and using (14),

\[
\omega_{t+\Delta_H}-\omega_t
=
\frac{\zeta_{t+\Delta_H}-\zeta_t}{2^{r+1}}
\equiv0\pmod{2^H},
\]

which proves (6).

For the connector prefix, reduce (9) modulo \(2^H\). Hypothesis (8) gives

\[
3^{G_t}\eta\equiv-B_t\pmod{2^H}.
\]

Since \(3^{G_t}\) is odd,

\[
\eta\equiv-B_t3^{-G_t}\pmod{2^H}.
\tag{15}
\]

But

\[
\begin{aligned}
B_t3^{-G_t}
&=
3^b\frac{3^{g_t}\mu_t+1}{2^{r+1}}
3^{-g_t-b}\\
&=
\frac{\mu_t+3^{-g_t}}{2^{r+1}}\\
&=\omega_t.
\end{aligned}
\]

Substitution into (15) proves (10). Part 3 is repeated application of part 1. ∎

## Interpretation

`L-0018` says a fixed period cannot preserve inverse-power prefixes at growing precision. The exact multiplicative order supplies the minimal nonlinear repair:

\[
\text{requested precision }H
\quad\Longrightarrow\quad
\text{counter jump }2^{H+r-1}.
\]

The price is enormous counter growth. The benefit is exact append-only nesting of the normalized connector prefix.

This suggests a revised stack state:

\[
(i,t,W,n),
\]

where \(W\) is a finite LSD-first word representing a prefix of \(-\omega_t\), rather than a fixed finite residue label.

## What this does not prove

The nested words in (12) naturally converge to a 2-adic object. That alone is not an ordinary finite marker.

A valid counterexample construction must still prove that the **forward emitted connector output** generates the added high bits from one finite initial stack. Preloading the entire nested limit would repeat the original adic error.

## Dependency audit

- `L-0018` supplies the exact multiplicative order.
- `L-0016` supplies \(\mu_t,B_t,G_t\).
- `L-0017` supplies the connector seed equation.
- No compactness claim is used to infer an ordinary integer.

## Gap audit

- The jump \(\Delta_H\) is exponential in the precision and has not been coupled to the next physical marker value.
- Target-independent low bits do not determine the full connector seed.
- Nested prefixes remain a completion object until a finite forward stack-regeneration rule is proved.

## Adversarial tests

`X-0012` checks (5)--(6) for all four self-return tower types at phase \(-34\), across a range of requested precisions, and verifies the low-prefix identity (10) directly modulo powers of two.

## Suggested next attack

Search for a connector macro whose output tail contains the next Hensel prefix plus a transformed copy of the existing finite stack. A successful rule would turn the append-only normalized lane into a forward-generating ordinary stack rather than a preloaded 2-adic address.