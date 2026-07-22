# T-0029 — Adaptive 512-cell counter chart with robust residual expansion

Claim ID: `T-0029`  
Title: Every logarithmic connector prefix can be routed in a dyadic annulus while preserving two-connector growth, including scale overflow  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Last corrected: 2026-07-22  
Dependencies: `L-0025`, `T-0028`, `T-0023`  
Scope: each fixed finite-core class of the phase-`-34` self-return towers  
Related counterexample candidates: none

## Correction note

The first version correctly proved the per-cell prefix bijection and the within-annulus growth bound, but incorrectly said that the same `4d` two-step bound holds unchanged across scale overflow.

At the final source cell, arbitrary next-scale fine addresses permit a two-step jump below `5d`, not `4d`. The theorem's growth conclusion remains true because the final source height is already close to `2B`. The corrected boundary proof appears below and is checked independently by `X-0014/boundary.py`.

## Scale annulus and counter coordinates

Fix one tower type with recovery length `r`. Its finite-core period is

\[
P=2^{r-1}.
\]

Fix one residue

\[
0\le\tau<P
\]

on which the finite recovery core is constant.

At scale `m`, put

\[
\boxed{B=2^m,}
\qquad
\boxed{d=2^{m-9}=B/512,}
\]

and assume

\[
\boxed{H=m-r-8\ge1.}
\]

Then

\[
\boxed{d=P2^H.}
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
\]

Every such height lies in the half-open cell

\[
[B+jd,\ B+(j+1)d)
\]

and has the fixed core residue `tau mod P`.

## Complete prefix chart in every cell

Let

\[
\Omega_{m,j}(s)
=
\omega_{t_{m,j}(s)}\pmod{2^H}.
\]

Then, for every cell `j`,

\[
\boxed{
\Omega_{m,j}:\mathbb Z/2^H\mathbb Z
\overset{\sim}{\longrightarrow}
\mathbb Z/2^H\mathbb Z
}
\]

is a bijection.

Consequently every desired `H`-bit normalized connector prefix, and hence every desired `H`-bit connector-seed prefix, has one unique fine address inside every coarse cell.

This follows directly from the isometry of `T-0028`:

\[
\nu_2\bigl(\Omega(s)-\Omega(s')\bigr)
=
\nu_2(s-s').
\]

## Monotone adaptive path inside one annulus

Choose an arbitrary desired prefix independently in every cell and let `s_j` be its unique fine address. Put

\[
t_j=t_{m,j}(s_j).
\]

For `0 <= j < 511`,

\[
\boxed{
P\le t_{j+1}-t_j\le2d-P.
}
\]

For `0 <= j < 510`,

\[
\boxed{
0<t_{j+2}-t_j<4d=B/128.
}
\]

Thus the counter path is strictly increasing for every within-annulus prefix sequence.

## Robust within-annulus expansion

The two-connector residual multiplier from source height `t_j` to the height two connectors ahead is

\[
\lambda_j
=
\frac{3^{7(t_j+1)}}{2^{11(t_{j+2}+1)}}.
\]

Put

\[
\sigma=7\log_2 3-11.
\]

Then

\[
\log_2\lambda_j
=
\sigma(t_j+1)-11(t_{j+2}-t_j).
\]

Using

\[
\sigma>\frac5{53},
\qquad
 t_j\ge B,
\qquad
 t_{j+2}-t_j<\frac B{128},
\]

we obtain

\[
\boxed{
\log_2\lambda_j
>
\left(\frac5{53}-\frac{11}{128}\right)B
=
\frac{57}{6784}B>0.
}
\]

So arbitrary adaptive prefix routing is uniformly expanding for all two-connector windows fully inside the annulus.

## Correct scale-boundary audit

At scale `m+1`, the base and cell width are

\[
B'=2B,
\qquad
d'=2d,
\]

and the fine-address length is `H+1`.

### Source cell 510

A source in cell 510 and the point two connectors ahead in next scale cell 0 satisfy

\[
0<t_{m+1,0}-t_{m,510}<4d.
\]

The within-annulus growth estimate therefore still applies, with the stronger source lower bound `t >= 2B-2d`.

### Source cell 511

A source in the final cell and the point two connectors ahead in next scale cell 1 satisfy

\[
\boxed{
0<t_{m+1,1}-t_{m,511}<5d.
}
\]

The source itself satisfies

\[
t_{m,511}\ge2B-d.
\]

Therefore

\[
\begin{aligned}
\log_2\lambda_{m boundary}
&>
\frac5{53}(2B-d)-55d\\
&=
\left(
\frac{10}{53}-\frac{5/53+55}{512}
\right)B\\
&=
\boxed{\frac{275}{3392}B>0.}
\end{aligned}
\]

Thus arbitrary fine-address choices remain two-connector expanding across scale overflow even though the old `4d` boundary sentence was incorrect.

## Why 512 cells arise

Within one annulus, arbitrary fine-address changes cost less than four cell widths. The exact lower margin

\[
7\log_2 3-11>5/53
\]

beats

\[
44/512=11/128.
\]

At the final boundary, five cell widths are possible, but the source height is near `2B`, producing the separate positive coefficient `275/3392` above.

The theorem does not claim that 512 is minimal among every conceivable nonuniform architecture. It is the first dyadic chart developed in this packet with a complete exact proof for arbitrary per-cell fine-prefix choices and scale overflow.

## Hidden coordinate system

The coordinates

\[
(m,j,s)
\]

have a direct meaning:

- `m`: leading dyadic scale;
- `j`: nine-bit coarse cell;
- `s`: `H=m-r-8` fine address bits;
- `tau`: finite recovery-core state.

Through `T-0028`, `s` is isometric to the requested low connector-prefix word. The padding counter therefore stores its own logarithmic prefix-routing data.

## Strategic consequence

At every coarse step one may:

1. compute a desired `H`-bit connector prefix;
2. invert the finite-level isometry to obtain the unique fine address;
3. move to that ordinary padding height;
4. retain a positive two-connector multiplier, including at scale overflow.

This routes only `H=O(m)` low bits. It does not route the full connector depth `K=Theta(2^m)`, and it does not solve ordinary stage realization.

## Gap audit

- The ordinary residual carries the remaining linear-in-height correction block.
- Naming a desired prefix does not prove that it came from an actual residual state.
- The raw local expansion does not prevent the stage quotient extinction of `T-0031`.
- No finite marked initialization is constructed.

## Adversarial tests

- `X-0014/run.py` enumerates every fine address at representative precisions, verifies the per-cell permutations, within-annulus jump bounds, and growth.
- `X-0014/boundary.py` exhaustively checks 4,096 arbitrary address combinations across the two scale-boundary source cases and verifies the corrected exact growth inequalities.