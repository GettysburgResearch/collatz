# L-0002 — Nine-column carry cycle and finite-horizon stack amplifier

Claim ID: `L-0002`  
Title: A regenerative carry block for the 64-to-81 collision chart  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `O-0001`, `NOTATION.md`  
Scope: finite words and a finite, parameterized number of induced-map steps  
Related counterexample candidates: none

## Statement

Work with the partial map from `O-0001`,

\[
H(64B+j)=81B+j,
\qquad j\in\{0,1\}.
\]

Let

\[
L_d(x)=64x+d,
\qquad
R_c(x)=81x+c.
\]

Define the low-order-first nine-digit block

\[
W=
L_{15}L_{29}L_{43}L_{57}L_7L_{22}L_{36}L_{50}L_0.
\]

Then the exact mixed-radix rewrite is

\[
\boxed{
R_1W\longrightarrow L_0^9R_1.
}
\tag{1}
\]

Consequently, for every integer \(m\ge0\) and every nonnegative integer high-order context \(x\), define

\[
S_m(x)=L_1W^m(x).
\]

Then

\[
\boxed{
S_m(x)
=64^{9m+1}x+\frac{64^{9m+1}+17}{81}
}
\tag{2}
\]

and the next \(9m+1\) applications of \(H\) are all defined, with

\[
\boxed{
H^{9m+1}(S_m(x))
=81^{9m}(81x+1).
}
\tag{3}
\]

This is a finite-horizon amplification theorem. It does not assert that the right-hand side regenerates another \(S_{m'}(x')\).

## Definitions

The word orientation and normalization rule

\[
R_cL_d\to L_rR_q,
\qquad81d+c=64q+r,
\]

are fixed in `NOTATION.md`.

## Motivation

A counterexample requires a finite word whose admissibility regenerates indefinitely. Equation (3) shows that a fixed nine-column carry block can guarantee an arbitrarily long, exactly controlled future segment while transporting an arbitrary finite high-order context. The remaining problem is closure, not local simulation.

## Proof

### The carry cycle

For an emitted digit zero, the normalization equation is

\[
81d+c=64q.
\tag{4}
\]

Since

\[
64^{-1}\equiv19\pmod{81},
\]

we have

\[
q\equiv19c\pmod{81}.
\]

Starting from \(c=1\), multiplication by \(19\) modulo \(81\) gives the nine-cycle

\[
1\to19\to37\to55\to73\to10\to28\to46\to64\to1.
\]

For each transition, solving (4) gives the input digits

\[
15,29,43,57,7,22,36,50,0.
\]

Therefore normalization emits nine zeros and returns to carry one, proving (1).

### Value of one block

Write

\[
W(x)=64^9x+w.
\]

The numerical equality corresponding to (1) is

\[
81W(x)+1=64^9(81x+1).
\]

Comparing constants gives

\[
w=\frac{64^9-1}{81}.
\]

Thus

\[
W^m(x)
=64^{9m}x+\frac{64^{9m}-1}{81}.
\]

Applying \(L_1\) gives

\[
\begin{aligned}
S_m(x)
&=64W^m(x)+1\\
&=64^{9m+1}x+\frac{64(64^{9m}-1)+81}{81}\\
&=64^{9m+1}x+\frac{64^{9m+1}+17}{81},
\end{aligned}
\]

which proves (2).

### Forced future steps

Because the least base-64 digit of \(S_m(x)\) is one, the first induced step is defined. It replaces the leading \(L_1\) by \(R_1\). Applying (1) through all \(m\) copies of \(W\) gives

\[
H(S_m(x))=64^{9m}(81x+1).
\tag{5}
\]

The right side has exactly the displayed block of \(9m\) low base-64 zeros, possibly followed by additional zeros depending on \(x\). Every such zero is admissible. Each zero-step removes one factor of \(64\) and introduces one factor of \(81\). After \(9m\) further steps, (5) becomes

\[
81^{9m}(81x+1),
\]

proving (3). ∎

## Dependency audit

- `O-0001` supplies the induced map \(H\).
- The proof uses only the exact two-radix normalization identity.
- No claim about the behavior after the guaranteed \(9m+1\) steps is used.

## Gap audit

- The lemma gives arbitrarily long finite admissible trajectories, not one infinite trajectory.
- Letting \(m\to\infty\) would create an infinite base-64 word, not automatically an ordinary integer.
- The free context \(x\) must be selected by a separate finite closure theorem.
- To lift into the original Collatz chart, one must additionally choose \(S_m(x)\equiv6\pmod{17}\). Such an \(x\) exists in a unique residue class modulo 17 because the coefficient of \(x\) in (2) is invertible modulo 17, but this does not solve regeneration.

## Adversarial tests

`X-0001` verifies the nine carry transitions, equation (2), and equation (3) for \(0\le m\le4\) and several high-order contexts.

## Remaining uncertainty

The finite lemma appears complete. It has not been independently reconstructed.

## Suggested next attack

Solve a finite regeneration equation or construct a cycle of several word schemas. The target must take the output of (3) into a larger finite word of a recognized schema without passing to an infinite radix-adic tail.
