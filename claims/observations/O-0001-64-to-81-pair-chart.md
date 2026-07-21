# O-0001 — A two-branch supercritical 64-to-81 chart

Claim ID: `O-0001`  
Title: Exact adjacent collision at length six  
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
T^6(64q+14)=T^6(64q+15)=81q+20.
}
\tag{1}
\]

The chronological parity words are respectively

\[
011101,
\qquad
111100.
\]

Both contain four odd steps, so the affine multiplier is

\[
\frac{3^4}{2^6}=\frac{81}{64}>1.
\]

Applying `T-0001` gives

\[
M=64,\,N=81,\,c=17,\,d=146,\,h=6
\]

and the induced partial map

\[
\boxed{
H(64B+j)=81B+j,
\qquad j\in\{0,1\}.
}
\tag{2}
\]

The ordinary-integer lifting class is

\[
A\equiv6\pmod{17},
\]

with

\[
n(A)=\frac{81A-146}{17}.
\]

## Proof

By `L-0001`, the affine constants for the two words are

\[
B(011101)=146,
\qquad
B(111100)=65.
\]

Therefore

\[
\begin{aligned}
T^6(64q+14)
&=\frac{81(64q+14)+146}{64}
=81q+20,\\
T^6(64q+15)
&=\frac{81(64q+15)+65}{64}
=81q+20.
\end{aligned}
\]

The remaining statements are the substitution

\[
L=6,\ a=4,\ r=14,\ s=20,\ m=2
\]

into `T-0001`. ∎

## Gap audit

This chart is locally expanding, but no infinite admissible orbit of (2) is proved here. A sequence of longer finite prefixes or an element of \(\mathbb Z_{64}\) would not by itself provide a finite positive integer.

## Adversarial tests

`X-0001` verifies the two parity words, both affine constants, identity (1) for several values of \(q\), and the conjugacy equations.

## Remaining uncertainty

The finite identity appears complete and exact; independent reconstruction is pending.

## Suggested next attack

Use the mixed-radix carry transducer from `L-0002`, or compare this chart with the larger alphabets in `O-0002` and `O-0003`.
