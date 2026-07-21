# L-0028 — Composition monoid of offset Montgomery tiles

Claim ID: `L-0028`  
Title: A finite chain of residual congruences is exactly one offset Montgomery reduction  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0026`, `T-0026`  
Scope: finite chains of odd-affine maps divided by powers of two  
Related counterexample candidates: none

## One tile

For an odd positive integer \(N\), an exponent \(D\ge0\), and an integer offset \(C\), write

\[
\boxed{
\mathcal M(N,D,C)(z)
=
\frac{Nz+C}{2^D}
}
\tag{1}
\]

on the ordinary integers for which the quotient is integral.

## Binary composition law

Let

\[
\mathcal M_1=\mathcal M(N_1,D_1,C_1),
\qquad
\mathcal M_2=\mathcal M(N_2,D_2,C_2).
\]

Then

\[
\boxed{
\mathcal M_2\circ\mathcal M_1
=
\mathcal M
\left(
N_2N_1,
D_1+D_2,
N_2C_1+2^{D_1}C_2
\right).
}
\tag{2}
\]

The operation on triples

\[
(N_2,D_2,C_2)\star(N_1,D_1,C_1)
=
\left(
N_2N_1,
D_1+D_2,
N_2C_1+2^{D_1}C_2
\right)
\tag{3}
\]

is associative, with identity \((1,0,0)\).

## Exact domain equivalence

The composite quotient in (2) is integral if and only if both original quotients are integral in sequence.

More generally, let

\[
\mathcal M_j=\mathcal M(N_j,D_j,C_j),
\qquad0\le j<s,
\]

with every \(N_j\) odd. Define recursively

\[
P_0=1,
\qquad
E_0=0,
\qquad
F_0=0,
\]

and

\[
\boxed{
P_{j+1}=N_jP_j,
}
\tag{4}
\]

\[
\boxed{
E_{j+1}=E_j+D_j,
}
\tag{5}
\]

\[
\boxed{
F_{j+1}=N_jF_j+2^{E_j}C_j.
}
\tag{6}
\]

Then the chronological chain acts by

\[
\boxed{
z_s=rac{P_sz_0+F_s}{2^{E_s}}.}
\tag{7}
\]

Moreover:

\[
\boxed{
P_sz_0+F_s\equiv0\pmod{2^{E_s}}
}
\tag{8}
\]

if and only if every intermediate \(z_1,\ldots,z_s\) is an integer and satisfies its local equation.

Thus the complete finite path domain is one dyadic cylinder.

## Canonical correction and quotient

Put

\[
\boxed{
\rho_s=[-F_sP_s^{-1}]_{E_s},
}
\tag{9}
\]

\[
\boxed{
\psi_s=rac{F_s+P_s\rho_s}{2^{E_s}}.
}
\tag{10}
\]

Whenever \(\psi_s\ge0\), every ordinary input in the path domain has the unique form

\[
\boxed{
z_0=\rho_s+2^{E_s}y,
\qquad y\ge0,}
\tag{11}
\]

and its exact output is

\[
\boxed{
z_s=\psi_s+P_sy.}
\tag{12}
\]

This is one offset Montgomery tile for the whole finite path.

## Proof

Direct substitution gives

\[
\begin{aligned}
\mathcal M_2(\mathcal M_1(z))
&=
\frac{
N_2(N_1z+C_1)/2^{D_1}+C_2
}{2^{D_2}}\\
&=
\frac{
N_2N_1z+N_2C_1+2^{D_1}C_2
}{2^{D_1+D_2}},
\end{aligned}
\]

which proves (2). Associativity follows either by direct calculation or from associativity of function composition.

Induction gives (4)–(7).

Suppose (8) holds. Reducing its left side modulo \(2^{D_0}\), every term generated after the first local offset contains a factor \(2^{D_0}\). Since

\[
P_s/N_0
\]

is odd, divisibility by \(2^{D_0}\) forces

\[
N_0z_0+C_0\equiv0\pmod{2^{D_0}}.
\]

Hence \(z_1\) is integral. Divide the composite numerator by \(2^{D_0}\) and repeat. Induction proves every intermediate integrality condition.

The reverse implication is immediate by composing the exact integer equations. This proves (8).

Because \(P_s\) is odd, equation (8) has one residue class modulo \(2^{E_s}\); (9) chooses its canonical representative. Substitution proves (10)–(12). ∎

## Strategic meaning

The corrected 256-step stage does not require 256 independent existential congruence checks. Once the local tower schedule is fixed, all of them compress losslessly to one canonical stage correction \(\rho_s\) and one stage quotient \(\psi_s\).

This is a proof compression, not a relaxation:

> The stage cylinder is integral exactly when every one of its 256 local residual divisions is integral.

`T-0027` applies the lemma to the complete dyadic stage and exposes its exact scale-squaring law.

## Gap audit

- Composition does not make the canonical stage cylinder nonempty in an ordinary forward-invariant sense; it only describes it exactly.
- Solving the compressed congruence backwards still naturally gives a 2-adic point.
- No finite initial residual or marked Collatz integer is supplied.

## Adversarial tests

`X-0014` checks the composition law, associativity, canonical corrections, and equivalence between composite divisibility and all intermediate divisions on exhaustive small systems and finite slices of the actual tower connector chain.