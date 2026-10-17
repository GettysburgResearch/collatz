# T-0028 — Padding-counter isometry for the connector-prefix space

Claim ID: `T-0028`  
Title: Each phase-`-34` tower counter is a lossless binary address tape for normalized connector prefixes  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0016`, `L-0019`, `L-0022`  
Scope: one fixed finite-core class of each phase-`-34` self-return tower type  
Related counterexample candidates: none

## Setup

Fix one of the four phase-`-34` self-return tower types. Let \(r\) be its synchronized recovery length. Its exact finite-core period from `L-0016` is

\[
\boxed{P=2^{r-1}.}
\tag{1}
\]

Choose one base height \(t_*\). Along the arithmetic progression

\[
\boxed{t(s)=t_*+Ps,}
\qquad s\in\mathbb Z_{≥0},
\tag{2}
\]

the finite residue \(\mu_t\) is constant; write it as \(\mu_*\).

Put

\[
\boxed{
\Omega(s)
=
\frac{
\mu_*+3^{-g_*-7Ps}
}{2^{r+1}}
\in\mathbb Z_2,
}
\tag{3}
\]

where

\[
g_*=g_0+7t_*.
\]

This is the normalized connector prefix \(\omega_{t(s)}\) of `L-0019`/`L-0022`.

## Exact isometry

For all distinct nonnegative integers \(s,s'\),

\[
\boxed{
\nu_2\bigl(\Omega(s)-\Omega(s')\bigr)
=
\nu_2(s-s').
}
\tag{4}
\]

Consequently \(\Omega\) extends uniquely by continuity to an isometry

\[
\boxed{
\Omega:\mathbb Z_2\longrightarrow\mathbb Z_2.
}
\tag{5}
\]

It is bijective.

## Finite-level bijection

For every \(H\ge1\), reduction modulo \(2^H\) gives a permutation

\[
\boxed{
\Omega_H:
\mathbb Z/2^H\mathbb Z
\overset{\sim}{\longrightarrow}
\mathbb Z/2^H\mathbb Z.
}
\tag{6}
\]

Thus for every desired binary word

\[
w\in\{0,1,\ldots,2^H-1\},
\]

there is a unique counter address

\[
\boxed{
s_H(w)\in[0,2^H)}
\tag{7}
\]

such that

\[
\boxed{
\Omega(s_H(w))
\equiv w
\pmod{2^H}.
}
\tag{8}
\]

Since a connector seed has low prefix

\[
\eta\equiv-\Omega(s)\pmod{2^H},
\]

the counter can generate **every** requested \(H\)-bit connector prefix.

## One-bit forward lift

Suppose

\[
s_H\in[0,2^H)
\]

satisfies

\[
\Omega(s_H)\equiv w_H\pmod{2^H}.
\]

Let \(w_{H+1}\) be either extension of \(w_H\) by one new high bit. Then exactly one of

\[
\boxed{s_H}
\qquad\text{or}\qquad
\boxed{s_H+2^H}
\tag{9}
\]

satisfies

\[
\boxed{
\Omega(s_{H+1})
\equiv w_{H+1}
\pmod{2^{H+1}}.
}
\tag{10}
\]

Thus a counter word matching \(H\) connector bits is extended to \(H+1\) bits by appending exactly one ordinary binary counter bit.

More generally, adding a multiple of \(2^{H+1}\) does not change the first \(H+1\) bits. Hence the actual padding height

\[
t=t_*+Ps
\]

can always be chosen arbitrarily large while retaining the requested prefix.

## Proof

For \(n=s-s'\ne0\), equation (3) gives

\[
\Omega(s)-\Omega(s')
=
\frac{
3^{-g_*-7Ps'}
\left(3^{-7Pn}-1\right)
}{2^{r+1}}.
\]

The leading power of three is a 2-adic unit. Since

\[
P=2^{r-1},
\]

the 2-adic lifting-the-exponent formula gives

\[
\begin{aligned}
\nu_2(3^{7Pn}-1)
&=
\nu_2(3-1)+\nu_2(3+1)+\nu_2(7Pn)-1\\
&=
1+2+(r-1)+\nu_2(n)-1\\
&=
r+1+\nu_2(n).
\end{aligned}
\]

Division by \(2^{r+1}\) proves (4).

Equation (4) shows that reduction modulo \(2^H\) is injective on the \(2^H\) residue classes of \(s\). The codomain also has \(2^H\) elements, so the map is bijective, proving (6)–(8).

The two lifts of one class modulo \(2^H\) are exactly \(s_H\) and \(s_H+2^H\). Their images agree modulo \(2^H\), while (4) says their difference has valuation exactly \(H\). Hence their \((H+1)\)-st bits are opposite, proving (9)–(10).

Compatibility of the finite-level permutations defines a bijective isometry of \(\mathbb Z_2\), proving (5). ∎

## Explicit four-type data

The four tower types have

| source mismatch index | recovery `r` | core period `P=2^(r-1)` |
|---:|---:|---:|
| 5 | 5 | 16 |
| 6 | 4 | 8 |
| 7 | 3 | 4 |
| 8 | 2 | 2 |

The cancellation in the proof is exact for every row:

\[
\nu_2(7P)=r-1.
\]

This is why all four maps have unit Lipschitz constant and full finite-level coverage despite their different recovery depths.

## Strategic consequence

Earlier results correctly showed that fixed-period counter control cannot supply growing connector precision. The present theorem identifies the nonlinear replacement:

> The unbounded padding counter itself is a perfect binary stack, isometrically conjugate to the normalized connector-prefix space.

This has three consequences.

1. **No prefix scarcity.** Every finite desired connector word has one exact counter address.
2. **Forward bit append.** If the desired word is generated one bit at a time, the counter address is generated one bit at a time.
3. **Growth freedom.** Extra higher counter bits may be used to increase the padding height without changing the already certified prefix.

The remaining physical problem is to couple this address lift to the ordinary residual zipper of `T-0026`: the Collatz output must generate the counter-addressed cylinder, not merely permit us to name it.

## Gap audit

- The theorem chooses a padding address for a requested prefix; it does not prove that a given ordinary residual outputs that prefix.
- The inverse isometry is an arithmetic routing map, not yet a local Collatz rewrite.
- Nested counter addresses are dynamic ordinary states, but they do not by themselves initialize one marked Collatz orbit.

## Adversarial tests

`X-0014` verifies exact valuation preservation, all finite-level permutations through representative precisions, and the one-bit lift rule for all four tower types.