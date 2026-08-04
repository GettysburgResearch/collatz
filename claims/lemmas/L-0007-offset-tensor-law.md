# L-0007 — Exact tensor law for inverse-root offset geometry

Claim ID: `L-0007`  
Title: Collision-code concatenation transports inverse-root alphabets by an exact mixed-radix Minkowski sum  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-0005`, `L-0006`  
Scope: finite fixed-weight parity collision codes and the geometry of their inverse roots  
Related counterexample candidates: none

## Statement

Let `U` be a nonempty set of binary parity words, all of length \(L_1\) and weight \(a_1\), such that

\[
B(u)\equiv B(u_0)\pmod{3^{a_1}}
\qquad(u\in U)
\]

for one reference word \(u_0\in U\).

Let `V` be a nonempty set of binary parity words, all of length \(L_2\) and weight \(a_2\), satisfying the stronger congruence

\[
B(v)\equiv B(v_0)\pmod{3^{a_1+a_2}}
\qquad(v\in V)
\]

for one reference word \(v_0\in V\).

Put

\[
\delta_u=-\frac{B(u)-B(u_0)}{3^{a_1}},
\qquad
\eta_v=-\frac{B(v)-B(v_0)}{3^{a_1+a_2}}.
\]

Then the concatenated family

\[
UV=\{uv:u\in U,\ v\in V\}
\]

is a collision code of length \(L_1+L_2\), weight \(a_1+a_2\), and precision at least \(a_1+a_2\). For every common output \(y\) for which the inverse roots are integral, if

\[
n_{u,v}(y)=
\frac{2^{L_1+L_2}y-B(uv)}{3^{a_1+a_2}},
\]

then

\[
\boxed{
 n_{u,v}(y)-n_{u_0,v_0}(y)
 =\delta_u+2^{L_1}\eta_v.
}
\tag{1}
\]

Consequently the offset alphabet is exactly

\[
\boxed{
D_{UV}=D_U+2^{L_1}E_V,
}
\tag{2}
\]

where

\[
D_U=\{\delta_u:u\in U\},
\qquad
E_V=\{\eta_v:v\in V\}.
\]

In particular:

1. \(|D_{UV}|=|U||V|\);
2. \(D_U\subseteq D_{UV}-e_0\) for every fixed \(e_0\in2^{L_1}E_V\);
3. \(D_U-D_U\subseteq D_{UV}-D_{UV}\);
4. every projection or interval property already witnessed inside \(D_U\) survives in the larger alphabet.

## Proof

By the concatenation identity from `L-0006`,

\[
B(uv)=3^{a_2}B(u)+2^{L_1}B(v).
\]

Subtracting the reference value gives

\[
B(uv)-B(u_0v_0)
=3^{a_2}(B(u)-B(u_0))
 +2^{L_1}(B(v)-B(v_0)).
\]

The first difference is divisible by \(3^{a_1+a_2}\), because
\(B(u)-B(u_0)\) is divisible by \(3^{a_1}\). The second is divisible by the same power by hypothesis on `V`. Hence `UV` has precision at least \(a_1+a_2\).

For any admissible common output \(y\), subtract the two inverse formulas:

\[
\begin{aligned}
n_{u,v}(y)-n_{u_0,v_0}(y)
&=-\frac{B(uv)-B(u_0v_0)}{3^{a_1+a_2}}\\
&=-\frac{B(u)-B(u_0)}{3^{a_1}}
 -2^{L_1}\frac{B(v)-B(v_0)}{3^{a_1+a_2}}\\
&=\delta_u+2^{L_1}\eta_v.
\end{aligned}
\]

This proves (1) and (2).

Distinct concatenated parity words have distinct starting residues modulo \(2^{L_1+L_2}\) by `L-0005`. Therefore the offsets in (2) are all distinct, proving the product cardinality. The remaining inclusions follow by fixing one suffix choice or subtracting two roots with the same suffix. ∎

## Why this matters

`L-0006` tracked only collision precision. This lemma tracks the actual arithmetic geometry of the induced digit alphabet. It allows a useful base alphabet to be enlarged without sacrificing its existing modular coverage, consecutive runs, or difference-set intervals.

The formula is exact, not asymptotic, and the common output cancels completely. Thus later drift tails can be redesigned independently without changing the inherited offset geometry.

## Gap audit

- The lemma produces finite collision alphabets, not infinite admissible induced orbits.
- Product cardinality does not imply vertical carry closure.
- The high-precision requirement on the suffix code is essential. Ordinary precision \(a_2\) is insufficient when \(a_1>0\).
- The orientation is chronological concatenation: `u` occurs first, followed by `v`.

## Adversarial tests

`X-0004` checks (1) for every pair in an explicit sixteen-word composite code and verifies the predicted product cardinality and inherited difference geometry.

## Suggested next attack

Construct suffix codes with arbitrarily high precision but controlled offset geometry, then iterate (2) to amplify a closure-relevant base alphabet while preserving its strongest local relay properties.