# T-0025 — Uniform finite-word compiler for the 256-stage connector control

Claim ID: `T-0025`  
Title: The frontier, inverse-prefix, cap, and odometer tracks are generated from one finite stage state  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
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
x_m=[3^{-7\cdot2^m}]_{Q_m}.
\]

From the finite initial state

\[
\boxed{(m_0,x_{m_0})}
\tag{1}
\]

there is a uniform deterministic finite-integer algorithm that, for every \(m\ge m_0\), produces:

1. the exact inverse prefix \(x_m\) to precision \(Q_m\);
2. every normalized source prefix \(\omega_{m,j}\) for
   \[
   0\le j\le256;
   \]
3. every canonical connector seed \(\eta_{m,j}^{i\to k}\) among the four source and target tower types;
4. every bounded connector cap \(\theta_{m,j}^{i\to k}\);
5. the periodic rational-frontier state from `O-0009`;
6. the eight-bit odometer state \(j\);
7. the finite quadratic bulk prefix from `L-0023` and `O-0010`;
8. the next finite stage state \((m+1,x_{m+1})\).

No bit of an infinite 2-adic word is part of the initial data.

## Explicit compiler

At stage \(m\):

### A. Generate all within-stage inverse powers

Put

\[
B=2^m,
\qquad
d=2^{m-8}.
\]

From \(x_m=3^{-7B}\pmod{2^{Q_m}}\), compute the finite unit

\[
a_m=3^{-7d}\pmod{2^{Q_m}}.
\]

Then

\[
\boxed{
3^{-7(B+jd)}
\equiv
x_ma_m^j
\pmod{2^{Q_m}}
}
\tag{2}
\]

for \(0\le j\le256\).

The four periodic core residues \(\mu\), finite source constants, and target anchors turn (2) into the exact \(\omega\), \(\eta\), and \(\theta\) values by `L-0022` and equation (12) of `L-0027`.

### B. Advance the scale

Square the modulus base:

\[
N_{m+1}=N_m^2,
\qquad
N_m=3^{7B}.
\]

Apply the Newton rule of `L-0027`:

\[
y_m=x_m^2\pmod{2^{Q_m}},
\]

\[
\widehat y_m
\equiv
y_m(2-N_m^2y_m)
\pmod{2^{2Q_m}},
\]

\[
\boxed{
x_{m+1}=[\widehat y_m]_{Q_{m+1}}.}
\tag{3}
\]

Because

\[
Q_{m+1}=2Q_m-11,
\]

this produces the full next precision with eleven spare Newton bits.

## Consequence: the state-space reduction

The previous candidate state was written

\[
(i,m,j,W,z,n),
\]

with an apparently independent unbounded connector word \(W\).

The theorem shows that \(W\) is a **derived proof track**. It is generated from \(m\), finite tower control, and the finite Newton prefix \(x_m\). It is not an independent choice and need not be preloaded from a completion point.

The load-bearing candidate state may therefore be reduced conceptually to

\[
\boxed{(i,m,j,z,n)}
\tag{4}
\]

plus deterministic finite arithmetic workspace, where:

- \(i\) is finite tower type;
- \(m\) is the unbounded scale;
- \(j\) is the eight-bit odometer;
- \(z\) is the ordinary residual high tail;
- \(n\) is the explicitly marked ordinary Collatz integer.

All connector-control words are checkable outputs of the compiler.

## Proof

`L-0027` proves the exact stage precision, Newton transition, and connector formula at the stage boundary. Equation (2) is finite modular exponentiation of one odd unit and gives every within-stage source inverse.

For each tower type, the finite recovery residue is periodic with period dividing sixteen. The stage jump \(d=2^{m-8}\) is divisible by those periods for all sufficiently large \(m\), while the finitely many smaller scales can be incorporated into the initial state. The remaining anchors and caps are finite formulas in the tower data.

`O-0009` supplies the rational frontier; `O-0010` identifies the moving bulk; `L-0024` supplies the finite odometer. Every operation—addition, multiplication, squaring, modular reduction by a power of two, and exact division after a proved congruence—acts on finite ordinary words. Induction on \(m\) proves the claim.

## What this resolves

The connector-control side of `Q-0020` no longer has a finite-versus-adic ambiguity:

- the required finite prefix is exact;
- the next prefix is computed from the current finite prefix;
- precision nearly doubles at each stage;
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

`X-0013` reconstructs the compiler independently. It checks Newton generation, the exact eleven-bit slack, all sixteen boundary connector seeds, within-stage inverse powers, and agreement with direct modular inversion.