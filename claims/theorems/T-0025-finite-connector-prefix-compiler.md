# T-0025 — Uniform finite-word compiler for the 256-stage connector control

Claim ID: `T-0025`  
Title: The frontier, inverse-prefix, cap, and odometer tracks are generated from one finite stage state  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-0022`--`L-0027`, `O-0009`, `O-0010`  
Scope: connector-control data for the corrected phase-`-34` 256-step stage  
Related counterexample candidates: none

## Statement

Fix one initial dyadic scale \(m_0\ge8\). Let

\[
Q_m=11\left(2^m+2^{m-8}+1\right)
\]

and let

\[
\boxed{x_m=[3^{-7\cdot2^m}]_{Q_m}.}
\tag{1}
\]

From the finite initial state

\[
\boxed{(m_0,x_{m_0})}
\tag{2}
\]

there is a uniform deterministic finite-integer algorithm that, for every \(m\ge m_0\), produces:

1. the exact first-target inverse prefix \(x_m\) to precision \(Q_m\);
2. the full Newton workspace \(\widetilde x_m\) to precision \(2Q_m\);
3. every normalized source prefix needed at all 256 positions of stage \(m\);
4. every canonical connector seed among the four source and target tower types;
5. every bounded connector cap;
6. the periodic rational-frontier state from `O-0009`;
7. the eight-bit odometer state;
8. the finite quadratic/logarithmic bulk prefix from `L-0023` and `O-0010`;
9. the next finite stage state \((m+1,x_{m+1})\).

No bit of an infinite 2-adic word is part of the initial data.

## Explicit compiler

At stage \(m\), put

\[
B=2^m,
\qquad
d=2^{m-8},
\qquad
N_m=3^{7B}.
\]

### A. Lift the stage-start inverse to full workspace precision

Compute

\[
\boxed{
\widetilde x_m
\equiv
x_m(2-N_mx_m)
\pmod{2^{2Q_m}}.
}
\tag{3}
\]

Then

\[
\boxed{
N_m\widetilde x_m
\equiv1
\pmod{2^{2Q_m}}.
}
\tag{4}
\]

The full workspace is necessary: the target depths of later connectors exceed \(Q_m\), although all remain below \(2Q_m\).

### B. Generate every within-stage inverse power

Compute the finite odd unit

\[
\boxed{
a_m=[3^{-7d}]_{2Q_m}.}
\tag{5}
\]

For

\[
t_{m,j}=B+jd,
\qquad0\le j\le256,
\]

we have, at every requested precision \(K\le2Q_m\),

\[
\boxed{
3^{-7t_{m,j}}
\equiv
\widetilde x_ma_m^j
\pmod{2^K}.
}
\tag{6}
\]

Multiplication by the fixed unit \(3^{-7}\) gives \(3^{-G_{t_{m,j}}}\). The finite tower anchors then give every connector seed and cap through equations (16)–(17) of `L-0027`.

### C. Advance the scale

The next base is

\[
N_{m+1}=N_m^2.
\]

Since \(\widetilde x_m^2\) is an inverse of \(N_{m+1}\) modulo \(2^{2Q_m}\), define

\[
\boxed{
x_{m+1}
=[\widetilde x_m^2]_{Q_{m+1}}.}
\tag{7}
\]

The precision identity

\[
\boxed{Q_{m+1}=2Q_m-11}
\tag{8}
\]

shows that this supplies the full next prefix with exactly eleven spare Newton bits.

## Consequence: the state-space reduction

The previous candidate state was written

\[
(i,m,j,W,z,n),
\]

with an apparently independent unbounded connector word \(W\).

The theorem shows that \(W\) is a **derived proof track**. It is generated from \(m\), finite tower control, \(x_m\), and the temporary finite workspace \(\widetilde x_m\). It is not an independent choice and need not be preloaded from a completion point.

The load-bearing candidate state may therefore be reduced conceptually to

\[
\boxed{(i,m,j,z,n)}
\tag{9}
\]

plus deterministic finite arithmetic workspace, where:

- \(i\) is finite tower type;
- \(m\) is the unbounded scale;
- \(j\) is the eight-bit odometer;
- \(z\) is the ordinary residual high tail;
- \(n\) is the explicitly marked ordinary Collatz integer.

All connector-control words are checkable outputs of the compiler.

## Proof

`L-0027` proves the exact exponent schedule, full Newton lift, stage-depth bound, within-stage inverse factorization, connector formula, and next-stage transition.

For each tower type, the finite recovery residue is periodic with period dividing sixteen. The stage jump \(d=2^{m-8}\) is divisible by those periods for all sufficiently large \(m\); the finitely many smaller scales can be incorporated into the initial state.

`O-0009` supplies the rational frontier; `O-0010` identifies the moving bulk; `L-0024` supplies the finite odometer. Every operation—addition, multiplication, squaring, modular reduction by a power of two, and exact division after a proved congruence—acts on finite ordinary words. Induction on \(m\) proves the claim.

## What this resolves

The connector-control side of `Q-0020` no longer has a finite-versus-adic ambiguity:

- the required finite prefix is exact;
- every deeper within-stage prefix comes from the same finite Newton workspace;
- the next stage prefix is computed from the current stage state;
- precision nearly doubles at each scale;
- no left-infinite input is invoked;
- every cap and carry has a direct finite certificate.

The 2-adic logarithm in `O-0010` describes the limiting object, but the compiler never needs that limit as data.

## What remains

The theorem does **not** show that the physical residual \(z\) lies in the computed cylinders. The exact residual update remains

\[
z_{j+1}
=
\frac{3^{G_j}z_j+\theta_j-\eta_{j+1}}
{2^{K_{j+2}}}.
\]

The remaining construction must prove, from one finite \(z_0\), that:

1. every displayed division is integral;
2. every residual stays nonnegative and above the required threshold;
3. the residual reaches the next computed stage cylinder;
4. the marked ordinary integer replays every Collatz block.

Thus the sole uncontrolled infinite channel is now the ordinary residual/marker pair, not the connector stack.

## Gap audit

- A uniform arithmetic algorithm is not automatically a finite-state transducer; it uses growing finite work tapes.
- Computed residues do not imply physical membership in those residues.
- The theorem supplies no initial residual and no counterexample integer.

## Adversarial tests

`X-0013` reconstructs the compiler independently. It checks the full Newton workspace, the deepest within-stage connectors, the exact eleven-bit slack, all source/target connector formulas, and agreement with direct modular inversion.