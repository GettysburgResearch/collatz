# O-0002 — A three-branch supercritical 512-to-729 chart

Claim ID: `O-0002`  
Title: Exact three-way consecutive collision at length nine  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-0001`, `T-0001`  
Scope: one exact supercritical collision bundle  
Related counterexample candidates: none

## Statement

For every integer \(q\ge0\),

\[
\boxed{
T^9(512q+124)
=T^9(512q+125)
=T^9(512q+126)
=729q+182.
}
\tag{1}
\]

The chronological parity words are

\[
001111101,
\qquad
100111101,
\qquad
011111100.
\]

Each contains six odd steps. Hence the chart is supercritical:

\[
\frac{3^6}{2^9}=\frac{729}{512}>1.
\]

The induced map is

\[
\boxed{
H(512B+j)=729B+j,
\qquad j\in\{0,1,2\}.
}
\tag{2}
\]

Its lifting data are

\[
c=217,\qquad d=2788,\qquad h=58,
\]

so

\[
A\equiv58\pmod{217},
\qquad
n(A)=\frac{729A-2788}{217}.
\]

## Proof

The three affine constants from `L-0001` are

\[
2788,
\qquad2059,
\qquad1330,
\]

and consecutive constants differ by \(729\). Thus

\[
729(124+j)+B_j=512\cdot182
\]

for \(j=0,1,2\), proving (1). The induced map and lifting data follow from `T-0001`. ∎

## Gap audit

A larger admissible digit alphabet makes finite carry grammars more plausible, but (2) still has no proved infinite finite-word orbit.

## Adversarial tests

`X-0001` verifies all parity words, constants, lifted identities, and conjugacy equations exactly.

## Remaining uncertainty

The finite identity appears complete and exact; independent reconstruction is pending.

## Suggested next attack

Study the carry graph with admissible emitted digits \(\{0,1,2\}\). A preliminary exact local cycle is

\[
R_1L_{361}L_0\longrightarrow L_2L_2R_1,
\]

but this alone does not give sustained admissibility and should be audited before promotion to its own claim.
