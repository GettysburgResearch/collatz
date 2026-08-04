# L-0026 — Offset Montgomery lifting for connector tiles

Claim ID: `L-0026`  
Title: Exact precision extension by feeding a connector quotient back as the next correction numerator  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0017`, `L-0022`  
Scope: odd-modulus mixed-radix connector equations  
Related counterexample candidates: none

## Statement

Let

\[
N\ge1
\]

be odd, let \(C\in\mathbb Z\), and suppose integers

\[
k\ge1,
\qquad
0\le \eta_k<2^k,
\qquad
\theta_k\ge0
\]

satisfy the exact connector equation

\[
\boxed{
C+N\eta_k=2^k\theta_k.
}
\tag{1}
\]

For an additional precision block \(s\ge1\), define the unique correction digit

\[
\boxed{
d_s
\equiv
-\theta_kN^{-1}
\pmod{2^s},
\qquad
0\le d_s<2^s,
}
\tag{2}
\]

and put

\[
\boxed{
\phi_{k,s}
=
\frac{\theta_k+Nd_s}{2^s}.
}
\tag{3}
\]

Then:

### 1. Exact precision lift

The extended correction

\[
\boxed{
\eta_{k+s}=\eta_k+2^kd_s
}
\tag{4}
\]

is the unique integer in \([0,2^{k+s})\) satisfying

\[
\boxed{
C+N\eta_{k+s}=2^{k+s}\phi_{k,s}.
}
\tag{5}
\]

Moreover

\[
\boxed{\phi_{k,s}\ge0.}
\tag{6}
\]

Thus a valid \(k\)-bit connector is extended by appending the finite \(s\)-bit word \(d_s\) at its high end.

### 2. High-tail preservation

For every ordinary integer \(z\ge0\),

\[
\boxed{
C+N\bigl(\eta_{k+s}+2^{k+s}z\bigr)
=
2^{k+s}\bigl(\phi_{k,s}+Nz\bigr).
}
\tag{7}
\]

The still-higher ordinary tail \(z\) is preserved exactly.

### 3. Newton–Hensel inversion as a special case

Take

\[
C=-1,
\qquad
\eta_k=x_k,
\qquad
Nx_k\equiv1\pmod{2^k}.
\]

With \(s=k\), equation (4) gives the inverse of \(N\) modulo \(2^{2k}\). It is equivalently

\[
\boxed{
x_{2k}
\equiv
x_k(2-Nx_k)
\pmod{2^{2k}}.
}
\tag{8}
\]

Thus the familiar Newton inverse-doubling rule is exactly the self-composition of the mixed-radix connector tile.

### 4. Offset Montgomery interpretation

Equation (1) is an offset Montgomery reduction with binary radix \(R=2^k\):

\[
\eta_k
\equiv
-CN^{-1}\pmod R,
\qquad
\theta_k=\frac{C+N\eta_k}{R}.
\]

The quotient \(\theta_k\) is not discarded. It is precisely the numerator whose next Montgomery correction \(d_s\) creates the additional precision block.

## Proof

Because \(N\) is odd, it is invertible modulo \(2^s\), so (2) has one residue class and the chosen representative is unique.

Equation (2) gives

\[
\theta_k+Nd_s\equiv0\pmod{2^s},
\]

so (3) is an integer. Since both terms in its numerator are nonnegative, \(\phi_{k,s}\ge0\).

Now substitute (4) into the left side of (5):

\[
\begin{aligned}
C+N\eta_{k+s}
&=C+N\eta_k+2^kNd_s\\
&=2^k\theta_k+2^kNd_s\\
&=2^k(\theta_k+Nd_s)\\
&=2^{k+s}\phi_{k,s}.
\end{aligned}
\]

The bounds

\[
0\le\eta_k<2^k,
\qquad
0\le d_s<2^s
\]

imply

\[
0\le\eta_k+2^kd_s<2^{k+s}.
\]

Uniqueness follows because the congruence

\[
C+Nx\equiv0\pmod{2^{k+s}}
\]

has one solution modulo \(2^{k+s}\).

Adding \(N2^{k+s}z\) to (5) proves (7).

For the Newton specialization, write

\[
Nx_k=1+2^ke_k.
\]

The appended block is

\[
d_k\equiv-e_kx_k\pmod{2^k},
\]

so

\[
x_k+2^kd_k
\equiv
x_k-2^ke_kx_k
=x_k(2-Nx_k)
\pmod{2^{2k}},
\]

which proves (8). ∎

## Application to the Collatz connector stack

A connector from one tower instance to another has

\[
C=B-\bar A,
\qquad
N=3^G,
\qquad
C+N\eta=2^{\bar K}\theta.
\]

Hence every canonical connector is an offset Montgomery reduction. Its finite quotient \(\theta\) is an exact precision-lifting state, not an unexplained carry artifact.

This removes one false dichotomy from the packet:

> Higher connector precision does not require consulting a pre-existing infinite 2-adic word. For one frozen congruence, it is generated from finite correction and quotient words by (2)–(5).

The remaining difficulty is dynamic: in the Collatz tower the modulus exponent, offset, and next physical residual all move between stages. `L-0027` and `T-0025` handle the moving connector-prefix modulus; the ordinary residual still requires a forward-invariant routing theorem.

## Gap audit

- The lemma extends one frozen odd-modulus congruence; it does not by itself synchronize a changing sequence of tower offsets.
- A finite arithmetic compiler for correction words does not prove that one ordinary Collatz residual contains those words at the required times.
- Newton lifting solves prefix computation, not the marked-orbit initialization problem.

## Adversarial tests

`X-0013` exhaustively checks small odd moduli, signed offsets, initial precisions, and extension lengths. It compares the lifted word with direct inversion modulo \(2^{k+s}\) and verifies the exact high-tail identity.