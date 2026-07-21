# T-0029 — Adaptive 512-cell counter chart with robust residual expansion

Claim ID: `T-0029`  
Title: Every logarithmic connector prefix can be routed inside one scale annulus without losing two-connector growth  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0025`, `T-0028`, `T-0023`  
Scope: each fixed finite-core class of the phase-`-34` self-return towers  
Related counterexample candidates: none

## Scale annulus and counter coordinates

Fix one tower type with recovery length \(r\). Its finite-core period is

\[
P=2^{r-1}.
\]

Fix one core residue

\[
0\le\tau<P
\]

for which the finite residue \(\mu_t\) is constant whenever

\[
t\equiv\tau\pmod P.
\]

At scale \(m\), put

\[
\boxed{B=2^m,}
\qquad
\boxed{d=2^{m-9}=B/512,}
\tag{1}
\]

and assume

\[
\boxed{H=m-r-8\ge1.}
\tag{2}
\]

Then

\[
\boxed{d=P2^H.}
\tag{3}
\]

For every coarse cell

\[
0\le j<512
\]

and fine address

\[
0\le s<2^H,
\]

define the padding height

\[
\boxed{
t_{m,j}(s)
=B+jd+\tau+Ps.
}
\tag{4}
\]

Every such height lies in the \(j\)-th half-open cell

\[
[B+jd,\ B+(j+1)d),
\]

and has the fixed core residue \(\tau\pmod P\).

## Complete prefix chart in every cell

Let

\[
\Omega_{m,j}(s)
=
\omega_{t_{m,j}(s)}
\pmod{2^H}
\]

be the normalized connector prefix of `T-0028`.

Then for every cell \(j\),

\[
\boxed{
\Omega_{m,j}:
\mathbb Z/2^H\mathbb Z
\overset{\sim}{\longrightarrow}
\mathbb Z/2^H\mathbb Z
}
\tag{5}
\]

is a bijection.

Consequently, for every prescribed \(H\)-bit word \(w_j\), there is one unique fine address

\[
\boxed{s_j=s_{m,j}(w_j)}
\tag{6}
\]

such that

\[
\boxed{
\omega_{t_{m,j}(s_j)}
\equiv w_j
\pmod{2^H}.
}
\tag{7}
\]

Since connector seeds satisfy

\[
\eta\equiv-\omega_t,
\]

the same chart routes every desired \(H\)-bit connector-seed prefix.

## Monotone adaptive counter path

Choose an arbitrary desired prefix word \(w_j\) independently in each of the 512 cells, and let

\[
t_j=t_{m,j}(s_j).
\]

Then

\[
\boxed{
P\le t_{j+1}-t_j\le2d-P
}
\tag{8}
\]

for \(0\le j<511\). In particular the padding height is strictly increasing whatever prefixes are requested.

Across two consecutive connectors,

\[
\boxed{
0<t_{j+2}-t_j<4d=rac B{128}.
}
\tag{9}
\]

The same bounds hold across the scale boundary when the next annulus begins at \(2B\) with cell width \(2d\), after choosing its fine address.

## Robust two-connector expansion

For a source height \(t_j\) and the height \(t_{j+2}\) two connectors ahead, the residual-stack slope is

\[
\lambda_j
=
\frac{3^{7(t_j+1)}}{2^{11(t_{j+2}+1)}}.
\]

Every adaptive prefix sequence satisfies

\[
\boxed{\lambda_j>1.}
\tag{10}
\]

More precisely,

\[
\boxed{
\log_2\lambda_j
>
\frac{57}{6784}B.
}
\tag{11}
\]

Thus arbitrary fine-prefix routing inside the 512-cell chart is compatible with a uniform positive two-connector growth margin.

## Why 512 is the first robust adaptive dyadic chart

A general \(2^C\)-cell annulus has width

\[
d=B/2^C.
\]

Arbitrary fine-address changes give the worst-case bound

\[
t_{j+2}-t_j<4d,
\]

so robust two-connector expansion requires

\[
7\log_2 3-11>rac{44}{2^C}.
\]

The exact lower bound of `L-0025`,

\[
7\log_2 3-11>rac5{53},
\]

proves the condition for \(C=9\), since

\[
\boxed{
\frac5{53}>rac{44}{512}=rac{11}{128}.
}
\tag{12}
\]

It does not prove the condition for \(C=8\). Hence:

- 256 cells suffice for the fixed equal-jump lane of `L-0024`;
- 512 cells are the first dyadic architecture in this packet with a proof that **every adaptive fine-prefix choice** retains two-connector expansion.

## Proof

Equation (3) follows from

\[
P2^H
=2^{r-1}2^{m-r-8}
=2^{m-9}
=d.
\]

For \(0\le s<2^H\),

\[
0\le\tau+Ps
\le(P-1)+P(2^H-1)
=d-1,
\]

so (4) lies in the stated cell.

`T-0028` gives

\[
\nu_2\left(
\omega_{t_*+Ps}-\omega_{t_*+Ps'}
\right)
=
u_2(s-s'),
\]

for every fixed core class. Translating the base height to \(B+jd+\tau\) preserves the proof, so reduction modulo \(2^H\) is bijective. This proves (5)–(7).

For consecutive cells,

\[
\begin{aligned}
t_{j+1}-t_j
&=d+P(s_{j+1}-s_j).
\end{aligned}
\]

The extreme fine-address difference is \(\pm(2^H-1)\). Using \(P2^H=d\) gives (8), and summing two jumps gives (9).

Put

\[
\sigma=7\log_2 3-11.
\]

Then

\[
\begin{aligned}
\log_2\lambda_j
&=7(t_j+1)\log_2 3-11(t_{j+2}+1)\\
&=\sigma(t_j+1)-11(t_{j+2}-t_j).
\end{aligned}
\]

Since \(t_j\ge B\), equation (9) and `L-0025` give

\[
\begin{aligned}
\log_2\lambda_j
&>
\frac5{53}B-rac{44}{512}B\\
&=
\left(
\frac5{53}-rac{11}{128}
\right)B\\
&=
\frac{57}{6784}B>0.
\end{aligned}
\]

This proves (10)–(12). ∎

## Hidden coordinate system

The three quantities

\[
\boxed{(m,j,s)}
\]

are not an arbitrary bookkeeping device. For fixed tower type and core residue they are the canonical mixed-radix coordinates of every admissible padding height in the dyadic annulus:

- \(m\): leading scale bit;
- \(j\): nine-bit coarse cell address;
- \(s\): \(H=m-r-8\) fine address bits;
- \(\tau\): finite core state.

Through `T-0028`, the fine address \(s\) is isometric to the requested connector-prefix word. The padding counter therefore carries its own prefix-routing stack.

## Strategic consequence

This theorem supplies the first **adaptive**, all-prefix counter lane with a rigorous growth certificate.

At each coarse step one may:

1. compute the next desired logarithmic connector prefix from finite residual/control data;
2. invert the isometry to obtain the unique fine counter address;
3. move to that height in the next cell;
4. retain positive residual-stack expansion regardless of the chosen prefix.

The remaining missing information is the much larger ordinary residual block beyond the logarithmic prefix. That block is governed by the stage Montgomery zipper of `T-0027` and the ordinary quotient of `T-0026`.

## Gap audit

- The theorem routes \(H=O(m)\) low bits, not the full connector depth \(K=\Theta(2^m)\).
- The residual high tail must still supply the remaining linear-in-height block.
- A requested prefix must be derived from an actual ordinary residual state; naming arbitrary words is not physical closure.
- No finite marked initialization is constructed.

## Adversarial tests

`X-0014` enumerates every fine address for representative precisions and all four tower types, verifies the per-cell permutations, checks arbitrary prefix sequences, and confirms the exact jump and growth bounds.