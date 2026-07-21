# Open problems

Last updated: 2026-07-21  
Active packet: issue `#2`

## Q-0001 — Finite-word regeneration

Status: `IDEA` / central open target  
Dependencies: `T-0001`

For at least one supercritical induced map

\[
H(MB+j)=NB+j,
\qquad j\in D,
\]

construct one finite positive integer \(A_0\) in the required lifting congruence class such that every iterate \(H^t(A_0)\) has least base-\(M\) digit in \(D\).

A valid solution must establish infinite behavior by finite induction or another ordinary-integer argument. An inverse-limit or radix-adic object is not enough.

## Q-0002 — Collision-bundle growth

Status: `IDEA`  
Dependencies: `X-0001`

Are the widths of supercritical consecutive collision bundles unbounded as \(L\to\infty\)? More modestly, construct an infinite explicit family whose widths or carry-grammar quality can be controlled analytically.

A larger alphabet may make closure easier, but width alone is not the optimization objective. Relevant secondary quantities include:

- expansion ratio \(N/M\);
- lifting modulus \(N-M\);
- short cycles in the carry graph;
- emitted admissible-digit density;
- compatibility with other charts.

## Q-0003 — Carry grammar for the width-three chart

Status: `IDEA`  
Dependencies: `O-0002`

For

\[
H(512B+j)=729B+j,
\qquad j\in\{0,1,2\},
\]

classify short carry cycles and determine whether they combine into a finite regenerative grammar.

A preliminary exact local rewrite is

\[
R_1L_{361}L_0\to L_2L_2R_1.
\]

This is not yet a promoted claim because the emitted digits do not automatically sustain more than the next induced step.

## Q-0004 — Multi-chart transition groupoid

Status: `IDEA`  
Dependencies: `O-0001`, `O-0002`, `O-0003`

Construct exact finite bridges among different collision charts. A successful cycle may let one chart repair the inadmissible boundary produced by another while retaining net expansion.

Required data for a bridge:

- source lifting coordinate and congruence class;
- finite Collatz word realizing the transition;
- target chart and congruence class;
- effect on the finite stack parameter;
- positivity and uniformity in every free parameter.

## Q-0005 — Finite versus adic closure criterion

Status: `IDEA`

Develop a theorem that distinguishes:

1. nested compatible admissible residue classes defining an element of \(\mathbb Z_M\); and
2. a family that contains one ordinary nonnegative integer with an infinite admissible forward orbit.

A useful theorem should be directly applicable to finite substitution grammars and should expose exactly when the high-order boundary stabilizes finitely.

## Q-0006 — Independent verification

Status: `IDEA`

Reconstruct the first contribution without relying on its author's confidence:

- check parity-word orientation;
- check every affine constant;
- check the lifting congruences;
- check the derivation of `H`;
- check the carry-cycle direction;
- rerun `X-0001` independently;
- identify the first unsupported inference, if any.
