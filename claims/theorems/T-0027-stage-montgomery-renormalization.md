# T-0027 — Stage Montgomery renormalization and exact scale squaring

Claim ID: `T-0027`  
Title: One corrected 256-step stage is one canonical Montgomery tile with a squared normalized scale  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0024`, `L-0028`, `T-0025`, `T-0026`  
Scope: any tower-type schedule through one corrected phase-`-34` dyadic stage  
Related counterexample candidates: none

## Stage schedule

At scale \(m\ge8\), put

\[
B=2^m,
\qquad
d=2^{m-8},
\]

and use the corrected heights

\[
t_j=B+jd,
\qquad0\le j\le256,
\]

with

\[
t_{257}=2B+2d.
\]

Choose any phase-aligned tower-type word

\[
i_0,i_1,\ldots,i_{257}
\]

from the four phase-`-34` self-return types.

For \(0\le j<256\), let

\[
(\eta_j,\theta_j)
\]

be the connector from \((i_j,t_j)\) to \((i_{j+1},t_{j+1})\). The local residual step is

\[
\boxed{
z_{j+1}
=
\frac{3^{G_{t_j}}z_j+\theta_j-\eta_{j+1}}
{2^{K_{t_{j+2}}}}.
}
\tag{1}
\]

## Exact stage tile

Apply `L-0028` to the 256 local steps. There are uniquely determined integers

\[
A_m,
\qquad
D_m,
\qquad
C_m(i_0,\ldots,i_{257})
\]

such that the full stage acts by

\[
\boxed{
z_{256}
=
\frac{3^{A_m}z_0+C_m}{2^{D_m}}.
}
\tag{2}
\]

The exponents are independent of the tower-type word and satisfy

\[
\boxed{
A_m
=
\frac{5369}{2}\,2^m+1792,
}
\tag{3}
\]

\[
\boxed{
D_m
=
\frac{1085579}{256}\,2^m+2816.
}
\tag{4}
\]

The offset \(C_m\) is computed by the finite recurrence

\[
C^{(0)}=0,
\qquad
E^{(0)}=0,
\]

\[
\boxed{
C^{(j+1)}
=
3^{G_{t_j}}C^{(j)}
+2^{E^{(j)}}(\theta_j-\eta_{j+1}),
}
\tag{5}
\]

\[
\boxed{
E^{(j+1)}
=E^{(j)}+K_{t_{j+2}},
}
\tag{6}
\]

with

\[
C_m=C^{(256)},
\qquad
D_m=E^{(256)}.
\]

## Exact stage-domain equivalence

Define the canonical stage correction

\[
\boxed{
R_m
=
[-C_m3^{-A_m}]_{D_m},
}
\tag{7}
\]

and the stage cap

\[
\boxed{
S_m
=
\frac{C_m+3^{A_m}R_m}{2^{D_m}}.
}
\tag{8}
\]

Then a nonnegative ordinary input \(z_0\) follows **all 256 local residual connectors integrally** if and only if

\[
\boxed{
z_0=R_m+2^{D_m}Y_m}
\tag{9}
\]

for one integer \(Y_m\ge0\). Its exact stage output is

\[
\boxed{
z_{256}=S_m+3^{A_m}Y_m.}
\tag{10}
\]

Thus no intermediate integrality condition is hidden or weakened by stage compression.

## Exact scale-squaring law

The stage exponents satisfy

\[
\boxed{
A_{m+1}=2A_m-1792,
}
\tag{11}
\]

\[
\boxed{
D_{m+1}=2D_m-2816.
}
\tag{12}
\]

Define the normalized stage multiplier and radix

\[
\boxed{
\widehat N_m=3^{A_m-1792},
}
\tag{13}
\]

\[
\boxed{
\widehat R_m=2^{D_m-2816}.
}
\tag{14}
\]

Then

\[
\boxed{
\widehat N_{m+1}=\widehat N_m^2,
\qquad
\widehat R_{m+1}=\widehat R_m^2.
}
\tag{15}
\]

The removed fixed cap is exactly 256 complete negative-cycle blocks:

\[
1792=256\cdot7,
\qquad
2816=256\cdot11.
\]

Equivalently, the full-stage slope decomposes as

\[
\boxed{
\frac{3^{A_m}}{2^{D_m}}
=
\left(\frac{3^7}{2^{11}}\right)^{256}
\frac{\widehat N_m}{\widehat R_m}.
}
\tag{16}
\]

After removal of the fixed 256-cycle cap, one scale doubling is literal squaring in both the odd and binary coordinates.

## Stage-to-stage zipper

For a sequence of stage type words, continuation from stage \(m\) to stage \(m+1\) is exactly

\[
\boxed{
S_m+3^{A_m}Y_m
=
R_{m+1}+2^{D_{m+1}}Y_{m+1}.
}
\tag{17}
\]

All quantities except the ordinary quotient \(Y_m\) are finite-word computable by `T-0025` and recurrence (5).

The previous 256-step ordinary zipper has therefore compressed to one scale-level zipper equation per stage.

## Proof

`L-0028` proves (2), (5)–(10), including equivalence with all intermediate integrality conditions.

Because every tower type has

\[
G_t=7(t+1),
\qquad
K_t=11(t+1),
\]

we obtain

\[
A_m
=7\sum_{j=0}^{255}(t_j+1).
\]

The source-height sum from `T-0024` is

\[
\sum_{j=0}^{255}t_j=\frac{767}{2}B.
\]

Hence

\[
A_m
=7\left(\frac{767}{2}B+256\right)
=\frac{5369}{2}B+1792,
\]

which proves (3).

Similarly,

\[
D_m
=11\sum_{j=0}^{255}(t_{j+2}+1).
\]

The future-height sum from `T-0024` is

\[
\sum_{j=0}^{255}t_{j+2}
=\frac{98689}{256}B.
\]

Therefore

\[
D_m
=11\left(\frac{98689}{256}B+256\right)
=\frac{1085579}{256}B+2816,
\]

which proves (4).

Replacing \(B\) by \(2B\) immediately gives (11)–(12). Subtracting the fixed constants and exponentiating gives (15); equation (16) is rearrangement. Equation (17) is the canonical decomposition of the output into the next stage cylinder. ∎

## Strategic significance

The scale architecture is smaller than the 256-transition presentation suggests.

At stage boundaries, the only existential ordinary datum is \(Y_m\). The remaining components are:

- one finitely computed type word;
- one canonical stage correction \(R_m\);
- one stage cap \(S_m\);
- one odd multiplier and binary radix whose normalized parts square exactly.

This suggests a more ambitious target than bit-by-bit routing:

> Construct a scale-renormalized ordinary quotient \(Y_m\) satisfying the single zipper equation (17), rather than separately managing 256 local residuals.

The exact intermediate Collatz replay remains available through the proof-carrying expansion of the stage tile.

## Gap audit

- The stage offset \(C_m\) depends on the chosen type word and has no closed scale recurrence yet.
- Exact scale squaring of the exponents does not force the stage correction cylinders to nest around an ordinary integer.
- Equation (17) may still define only a 2-adic inverse-limit quotient.
- No finite initial \(Y_{m_0}\) or marked Collatz integer is supplied.

## Adversarial tests

`X-0014` verifies the composition recurrence, exponent formulas, scale-squaring identities, and exact replay equivalence on exhaustive small affine systems and actual finite slices of the phase-`-34` tower chain.