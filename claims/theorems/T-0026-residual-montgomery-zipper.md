# T-0026 — Residual Montgomery zipper criterion

Claim ID: `T-0026`  
Title: Exact normal form and counterexample criterion for the sole remaining ordinary memory channel  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0017`, `L-0026`, `T-0023`, `T-0025`  
Scope: an arbitrary phase-aligned sequence of tower connectors  
Related counterexample candidates: none

## Setup

Let

\[
E_0,E_1,E_2,\ldots
\]

be a phase-aligned sequence of exact tower instances. For the connector from \(E_n\) to \(E_{n+1}\), write

\[
(\eta_n,\theta_n)
\]

for the canonical tile of `L-0017`. Let

\[
N_n=3^{G_n}
\]

be the odd multiplier of \(E_n\), and put

\[
D_n=K_{n+2},
\qquad
C_n=\theta_n-\eta_{n+1}.
\tag{1}
\]

The exact residual equation of `T-0023` is

\[
\boxed{
N_nz_n+C_n=2^{D_n}z_{n+1}.
}
\tag{2}
\]

## Canonical Montgomery state

Define the canonical correction

\[
\boxed{
\rho_n
=
[-C_nN_n^{-1}]_{D_n},
\qquad
0\le\rho_n<2^{D_n},
}
\tag{3}
\]

and its quotient

\[
\boxed{
\psi_n
=
\frac{C_n+N_n\rho_n}{2^{D_n}}.
}
\tag{4}
\]

Whenever the schedule is one of the ordinary connector schedules constructed in the packet,

\[
\boxed{\psi_n\ge0.}
\tag{5}
\]

Then:

### 1. Exact zipper normal form

A nonnegative integer \(z_n\) satisfies the residual divisibility condition in (2) if and only if there is a unique \(y_n\ge0\) such that

\[
\boxed{
z_n=\rho_n+2^{D_n}y_n.}
\tag{6}
\]

For that decomposition,

\[
\boxed{
z_{n+1}=\psi_n+N_ny_n.}
\tag{7}
\]

### 2. Self-feeding equation

The next transition is valid exactly when

\[
\boxed{
\psi_n+N_ny_n
=
\rho_{n+1}+2^{D_{n+1}}y_{n+1}
}
\tag{8}
\]

for one nonnegative integer \(y_{n+1}\).

Thus the entire infinite arithmetic-routing problem is the ordinary-integer zipper

\[
\boxed{
\rho_n+2^{D_n}y_n
\longmapsto
\psi_n+N_ny_n
=
\rho_{n+1}+2^{D_{n+1}}y_{n+1}.
}
\tag{9}
\]

### 3. All control coefficients are finite-word computable

For the corrected 256-stage schedule, `T-0025` computes

\[
N_n,\ D_n,\ C_n,\ \rho_n,\ \psi_n
\]

from finite stage data. No coefficient in (8) is an oracle value.

### 4. Counterexample criterion

Suppose there is one explicit finite initial state

\[
(i_0,m_0,j_0,y_0,n_0)
\]

such that:

1. equations (6)–(8) hold forever under the deterministic stage schedule;
2. every \(y_n\) is nonnegative;
3. every physical tower block is replayed on the marked integer \(n_n\);
4. the residual and marked states remain above the explicit growth thresholds of `T-0023`/`T-0024`;
5. the marked orbit avoids \(1,2\).

Then \(n_0\) is a positive-integer Collatz counterexample. If the residual thresholds force unbounded marked values, the orbit diverges.

## Proof

Because \(N_n\) is odd, equation

\[
C_n+N_nx\equiv0\pmod{2^{D_n}}
\]

has one residue class. Equation (3) chooses its least nonnegative representative. Therefore (2) is integral exactly when

\[
z_n\equiv\rho_n\pmod{2^{D_n}},
\]

which is equivalent to the unique decomposition (6).

Substitution gives

\[
\begin{aligned}
N_nz_n+C_n
&=N_n\rho_n+C_n+N_n2^{D_n}y_n\\
&=2^{D_n}\psi_n+2^{D_n}N_ny_n\\
&=2^{D_n}(\psi_n+N_ny_n),
\end{aligned}
\]

proving (7). Applying the next canonical decomposition proves (8)–(9).

The compiler statement follows from `T-0025` and one finite application of the offset Montgomery formula `L-0026` to \((N_n,C_n,D_n)\).

The counterexample criterion is exact block concatenation: the marker follows its unique Collatz trajectory, every boundary is an ordinary nonnegative integer, and the infinite accepted schedule excludes the terminal cycle. ∎

## Strategic meaning

The packet previously carried two apparently infinite objects:

1. the connector inverse-prefix stack;
2. the ordinary residual tail.

`T-0025` removes the first from the existential burden. It is a deterministic finite-word computation.

The zipper variable \(y_n\) in (8) is now the only uncontrolled ordinary data channel. The central problem is no longer “generate all future connector bits.” It is:

> Find a finite self-feeding ordinary quotient whose Montgomery output lands in the next computed Montgomery correction cylinder forever.

This formulation admits three sharply distinct attacks:

- **constructive:** find a finite stack/substitution invariant for \(y_n\);
- **branching:** use tower-type or schedule choices to route the quotient into the next correction;
- **obstructive:** prove a proposed class of zipper languages cannot contain an ordinary infinite path.

## Gap audit

- The theorem is an equivalence and criterion, not an existence proof.
- The canonical correction sequence may define only a 2-adic residual when solved backwards.
- Positive slopes do not force the quotient-prefix equality (8).
- No finite \(y_0\) or marked \(n_0\) is supplied.

## Adversarial tests

`X-0012` verifies (2) on finite tower chains. `X-0013` verifies the generic Montgomery normal form and finite computation of the required correction words.