# L-0030 — Canonical cap bound for positive offset-Montgomery chains

Claim ID: `L-0030`  
Title: Every canonical finite connector chain has output cap below three times its odd multiplier  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0028`  
Scope: finite chains of odd-affine maps divided by nontrivial powers of two  
Related counterexample candidates: none

## Setup

Let

\[
f_j(x)=\frac{N_jx+C_j}{q_j},
\qquad 0\le j<s,
\tag{1}
\]

where

\[
N_j\in\mathbb Z_{>0}\text{ is odd},
\qquad
q_j=2^{d_j}\ge2,
\tag{2}
\]

and the offset lies in the canonical connector window

\[
\boxed{-q_j<C_j<N_j.}
\tag{3}
\]

Put

\[
N=\prod_{j=0}^{s-1}N_j,
\qquad
Q=\prod_{j=0}^{s-1}q_j.
\tag{4}
\]

By `L-0028`, chronological composition has the form

\[
f_{s-1}\circ\cdots\circ f_0(x)
=\frac{Nx+C}{Q}
\tag{5}
\]

for one integer offset \(C\), and composite divisibility is equivalent to integrality of every local quotient.

Let

\[
\boxed{R=[-CN^{-1}]_Q,}
\qquad 0\le R<Q,
\tag{6}
\]

be the canonical correction, and put

\[
\boxed{S=\frac{NR+C}{Q}.}
\tag{7}
\]

## Statement

### 1. Positivity is automatic

Every intermediate value obtained by replaying the chain from \(R\) is a nonnegative integer. In particular,

\[
\boxed{S\ge0.}
\tag{8}
\]

### 2. Universal cap bound

The final canonical cap satisfies

\[
\boxed{S+1<3N,}
\tag{9}
\]

and therefore

\[
\boxed{0\le S<3N.}
\tag{10}
\]

The constant is independent of:

- the number of bits in the individual moduli;
- the signs of the offsets;
- the canonical correction \(R\);
- and the length \(s\) of the chain.

### 3. Quotient form

Every nonnegative input in the complete path cylinder is uniquely

\[
\boxed{x=R+QY,\qquad Y\ge0,}
\tag{11}
\]

and its output is

\[
\boxed{f_{s-1}\circ\cdots\circ f_0(x)=S+NY.}
\tag{12}
\]

Thus a long exact connector chain leaves only one unrestricted ordinary quotient \(Y\), while its canonical additive cap is uniformly smaller than \(3N\).

## Proof

### Nonnegativity

Let \(x_j\ge0\) be an integral input to one local map. From (3),

\[
N_jx_j+C_j>-q_j.
\]

The numerator is divisible by \(q_j\). No negative multiple of \(q_j\) lies strictly above \(-q_j\), so

\[
x_{j+1}=\frac{N_jx_j+C_j}{q_j}\ge0.
\]

The canonical correction \(R\) is nonnegative, and `L-0028` converts composite divisibility into every local divisibility condition. Induction proves nonnegativity of all intermediate values and of \(S\).

### Cap estimate

Write

\[
w_j=x_j+1,
\qquad
\lambda_j=\frac{N_j}{q_j}.
\]

The upper half of (3) gives

\[
\begin{aligned}
w_{j+1}
&=\frac{N_jx_j+C_j+q_j}{q_j}\\
&<\frac{N_jx_j+N_j+q_j}{q_j}\\
&=\lambda_jw_j+1.
\end{aligned}
\tag{13}
\]

Iterating (13) yields

\[
w_s
<
\left(\prod_{j=0}^{s-1}\lambda_j\right)w_0
+
\sum_{k=0}^{s-1}
\prod_{j=k+1}^{s-1}\lambda_j.
\tag{14}
\]

Since \(0\le R<Q\),

\[
w_0=R+1\le Q.
\]

Hence the first term in (14) is at most

\[
\frac NQ Q=N.
\tag{15}
\]

A suffix containing \(\ell\) local maps has denominator at least \(2^\ell\), while its numerator product is at most the complete product \(N\). Therefore

\[
\prod_{j=k+1}^{s-1}\lambda_j
\le
\frac{N}{2^{s-1-k}}.
\tag{16}
\]

Summing the geometric series gives

\[
\sum_{k=0}^{s-1}
\prod_{j=k+1}^{s-1}\lambda_j
<2N.
\tag{17}
\]

Equations (14)--(17) prove

\[
w_s=S+1<3N.
\]

Finally, (11)--(12) are the canonical correction and quotient formulas of `L-0028`. ∎

## Application to the phase-34 tower system

For one local residual connector in `T-0026`,

\[
N_j=3^{G_j},
\qquad
q_j=2^{K_{j+2}},
\qquad
C_j=\theta_j-\eta_{j+1}.
\]

`L-0017` gives

\[
0\le\theta_j<N_j,
\qquad
0\le\eta_{j+1}<q_j,
\]

so (3) holds exactly. The lemma therefore applies to every finite phase-aligned tower path, including the complete corrected stage of `T-0027`.

## Interpretation

The large negative local offsets cannot create a large negative or positive canonical cap. Dyadic divisibility and the canonical connector rectangles force a much stronger global fact:

> after an arbitrary finite exact path, the additive output cap is less than three copies of the complete odd multiplier.

This is the archimedean estimate needed to import the completion-height and carry-extinction viewpoint developed independently in PR #16, PR #19, and PR #33 into the supercritical stage zipper of this packet.

## Gap audit

- The lemma is finite and does not decide whether successive canonical caps equal successive corrections.
- The unrestricted quotient \(Y\) may be enormous.
- The bound controls the cap, not the full output \(S+NY\).
- Ordinary realization of an infinite directive still requires the quotient to satisfy every later cylinder.

## Adversarial tests

`X-0015` exhaustively checks the theorem on 69,904 small chains, verifies local nonnegativity and exact replay, and reconstructs one complete 256-transition phase-34 stage at scale \(m=8\).