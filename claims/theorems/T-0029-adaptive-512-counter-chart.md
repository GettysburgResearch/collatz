# T-0029 — Adaptive 512-cell counter chart with robust residual expansion

Claim ID: `T-0029`  
Title: Every logarithmic connector prefix can be routed inside one scale annulus without losing two-connector growth  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-0025`, `T-0028`, `T-0023`  
Scope: each fixed finite-core class of the phase-`-34` self-return towers  
Related counterexample candidates: none

## Scale annulus and counter coordinates

Fix one tower type with recovery length \(r\). Its finite-core period is

\[
P=2^{r-1}.
\]

Fix a core residue

\[
0\le\tau<P
\]

for which \(\mu_t\) is constant whenever

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

define

\[
\boxed{
t_{m,j}(s)=B+jd+\tau+Ps.
}
\tag{4}
\]

Every such height lies in

\[
[B+jd,\ B+(j+1)d)
\]

and has the fixed core residue \(\tau\pmod P\).

## Complete prefix chart in every cell

Let

\[
\Omega_{m,j}(s)
=
\omega_{t_{m,j}(s)}
\pmod{2^H}.
\]

For every cell \(j\),

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

Consequently every prescribed \(H\)-bit word \(w_j\) has one unique fine address \(s_j\) satisfying

\[
\boxed{
\omega_{t_{m,j}(s_j)}
\equiv w_j
\pmod{2^H}.
}
\tag{6}
\]

Since connector seeds satisfy

\[
\eta\equiv-\omega_t,
\]

the same chart routes every desired \(H\)-bit connector-seed prefix.

## Monotone adaptive counter path inside one annulus

Choose an arbitrary desired prefix independently in each cell, and put

\[
t_j=t_{m,j}(s_j).
\]

For \(0\le j<511\),

\[
\boxed{
P\le t_{j+1}-t_j\le2d-P.
}
\tag{7}
\]

Hence the padding height is strictly increasing regardless of the requested prefixes. For \(0\le j<510\),

\[
\boxed{
0<t_{j+2}-t_j<4d=B/128.
}
\tag{8}
\]

## Scale-boundary bounds

The next scale starts at \(2B\) and has cell width \(2d\). Arbitrary fine addresses therefore give:

- a last-old-cell to first-new-cell jump smaller than \(3d\);
- a within-new-scale jump smaller than \(4d\).

Accordingly:

- from the second-last old cell across the boundary, two jumps total less than \(5d\), while the source height is at least \(2B-2d\);
- from the last old cell across the boundary and into the second new cell, two jumps total less than \(7d\), while the source height is at least \(2B-d\).

These boundary bounds are weaker than (8) as raw jump bounds, but the source height is almost \(2B\), so the same positive growth estimate remains valid.

## Robust two-connector expansion

For any source height \(t\) and the height \(t^{++}\) two connectors ahead, put

\[
\lambda
=
\frac{3^{7(t+1)}}{2^{11(t^{++}+1)}}.
\]

Every adaptive prefix sequence, including transitions across scale boundaries, satisfies

\[
\boxed{\lambda>1.}
\tag{9}
\]

Inside a single annulus we have the explicit lower bound

\[
\boxed{
\log_2\lambda
>
\frac{57}{6784}B.
}
\tag{10}
\]

The boundary cases have larger positive lower bounds:

\[
\frac{2195}{27136}B
\]

for a source in the second-last old cell, and

\[
\frac{1034}{27136}B
\]

for a source in the last old cell.

## Why 512 is the first robust adaptive dyadic chart

A general \(2^C\)-cell annulus has width

\[
d=B/2^C.
\]

Inside one scale, arbitrary fine-address changes give

\[
t^{++}-t<4d.
\]

A uniform proof of two-connector expansion therefore asks for

\[
7\log_2 3-11>
\frac{44}{2^C}.
\]

`L-0025` proves

\[
7\log_2 3-11>
\frac5{53}.
\]

For \(C=9\),

\[
\boxed{
\frac5{53}>
\frac{44}{512}
=
\frac{11}{128}.
}
\tag{11}
\]

The same imported lower bound does not prove the adaptive condition at \(C=8\). Hence:

- 256 cells suffice for the fixed equal-jump lane of `L-0024`;
- 512 cells are the first dyadic architecture in this packet with a proof that every adaptive fine-prefix choice retains two-connector expansion.

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
\nu_2(s-s')
\]

for every fixed core class. Translating the base height to \(B+jd+\tau\) preserves the proof, so reduction modulo \(2^H\) is bijective. This proves (5)–(6).

For consecutive cells,

\[
t_{j+1}-t_j
=d+P(s_{j+1}-s_j).
\]

The extreme fine-address difference is \(\pm(2^H-1)\). Using \(P2^H=d\) gives (7), and summing two jumps gives (8). The boundary bounds follow directly from the half-open cell intervals.

Put

\[
\sigma=7\log_2 3-11.
\]

Then

\[
\log_2\lambda
=
\sigma(t+1)-11(t^{++}-t).
\]

Inside one annulus, \(t\ge B\) and (8) give

\[
\begin{aligned}
\log_2\lambda
&>
\frac5{53}B-
\frac{44}{512}B\\
&=
\frac{57}{6784}B>0.
\end{aligned}
\]

For the second-last-cell boundary case,

\[
t\ge2B-2d,
\qquad
t^{++}-t<5d,
\]

so

\[
\log_2\lambda
>
\left(
\frac5{53}\frac{1022}{512}
-
\frac{55}{512}
\right)B
=
\frac{2195}{27136}B>0.
\]

For the last-cell boundary case,

\[
t\ge2B-d,
\qquad
t^{++}-t<7d,
\]

so

\[
\log_2\lambda
>
\left(
\frac5{53}\frac{1023}{512}
-
\frac{77}{512}
\right)B
=
\frac{1034}{27136}B>0.
\]

All later cases are ordinary within-annulus cases at the doubled scale. This proves (9)–(11). ∎

## Hidden coordinate system

For fixed tower type and core residue, the tuple

\[
\boxed{(m,j,s,\tau)}
\]

is the canonical mixed-radix coordinate of every admissible padding height in the dyadic annulus:

- \(m\): leading scale;
- \(j\): nine-bit coarse cell;
- \(s\): \(H=m-r-8\) fine address bits;
- \(\tau\): finite core state.

Through `T-0028`, \(s\) is isometric to the requested connector-prefix word. The padding counter therefore carries its own prefix-routing stack.

## Strategic consequence

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

`X-0014` enumerates every fine address for representative precisions and all four tower types, verifies the per-cell permutations, checks arbitrary prefix sequences within and across scales, and confirms the exact jump and growth bounds.