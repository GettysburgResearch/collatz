# T-0004 — Exact run-length skeleton of an induced radix orbit

Claim ID: `T-0004`  
Title: Equivalence between infinite digit-preserving radix orbits and infinite `S`-unit carry chains  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0001`; applications to Collatz use `T-0002`  
Scope: maximal constant-digit phases of every induced collision chart  
Related counterexample candidates: none

## Statement

Let \(1<M<N\) be coprime, let
\(D\subseteq\{0,1,\ldots,M-1\}\), and consider

\[
H_D(MB+d)=NB+d,
\qquad d\in D.
\tag{1}
\]

For a nonzero integer \(z\), define the base-\(M\) divisibility depth

\[
\operatorname{ord}_M(z)
=\max\{u\ge0:M^u\mid z\}.
\tag{2}
\]

Let \(A\ge M\) be admissible and put

\[
d=A\bmod M\in D,
\qquad
u=\operatorname{ord}_M(A-d),
\qquad
C=\frac{A-d}{M^u}.
\tag{3}
\]

Then \(u\ge1\), \(C>0\), and \(M\nmid C\). The following hold.

### 1. Exact phase transfer

For every \(0\le t\le u\),

\[
\boxed{
H_D^t(A)=d+N^tM^{u-t}C.
}
\tag{4}
\]

In particular, the least base-\(M\) digit remains exactly \(d\) for the first
\(u\) induced steps.

At the phase boundary,

\[
A^+=H_D^u(A)=d+N^uC.
\tag{5}
\]

Its least digit

\[
e=A^+\bmod M
\tag{6}
\]

satisfies \(e\ne d\). The orbit continues precisely when \(e\in D\).

### 2. Skeleton transition

If \(e\in D\), define

\[
v=\operatorname{ord}_M(A^+-e),
\qquad
C^+=\frac{A^+-e}{M^v}.
\tag{7}
\]

Then \(v\ge1\), \(C^+>0\), \(M\nmid C^+\), and the transition between
maximal phases is exactly

\[
\boxed{
d+N^uC=e+M^vC^+.
}
\tag{8}
\]

Equivalently,

\[
\boxed{
C^+=\frac{N^uC+d-e}{M^v}
}
\tag{9}
\]

with the exact congruence

\[
\boxed{
N^uC\equiv e-d\pmod{M^v}.
}
\tag{10}
\]

### 3. Infinite-chain equivalence

An ordinary integer \(A_0\ge M\) has an infinite admissible orbit if and only
if its dynamics can be decomposed into an infinite chain of positive integers

\[
(d_k,u_k,C_k)_{k\ge0}
\]

such that

- \(d_k\in D\);
- \(u_k\ge1\);
- \(C_k>0\) and \(M\nmid C_k\);
- \(d_{k+1}\ne d_k\);
- for every \(k\),

\[
\boxed{
d_k+N^{u_k}C_k
=d_{k+1}+M^{u_{k+1}}C_{k+1};
}
\tag{11}
\]

- and

\[
A_0=d_0+M^{u_0}C_0.
\tag{12}
\]

For a Collatz collision chart, one adds the lifting congruence and positivity
condition from `T-0002` to (12).

## Definitions

A **phase** is a maximal consecutive run during which the least base-\(M\)
digit of the induced state is constant. Equation (11) is called the
**run-length skeleton** or **`S`-unit carry chain** of the orbit.

## Motivation

Individual carry blocks obscure the global state. The skeleton theorem strips
away every forced run and retains only the genuinely nonlinear events: a digit
change, a power of \(M\) created by cancellation, and the updated cofactor.
The counterexample problem becomes an exact infinite chain of exponential
congruences rather than an unstructured search through enormous integers.

This formulation also clarifies what a regenerative grammar must control. It
must update not only a visible digit block but the triple
\((d_k,u_k,C_k)\), with enough cancellation in (10) to create the next power
of \(M\).

## Proof

From (3),

\[
A=d+M^uC.
\]

For \(t<u\), the second term in

\[
d+N^tM^{u-t}C
\]

is divisible by \(M\), so the least digit is \(d\) and the next application
of (1) is defined. One step replaces one factor \(M\) by one factor \(N\).
Induction proves (4).

At \(t=u\), (5) holds. If \(e=d\), then

\[
M\mid A^+-d=N^uC.
\]

Coprimality of \(M\) and \(N\) would imply \(M\mid C\), contradicting the
maximality in (3). Therefore \(e\ne d\).

If \(e\notin D\), the partial map stops. If \(e\in D\), then each
induced step from a state at least \(M\) increases that state by
\((N-M)\lfloor A/M\rfloor>0\). Hence \(A^+\ge M\), and because
\(0\le e<M\), the difference \(A^+-e\) is a positive multiple of \(M\).
Thus (7) is well-defined and gives all stated divisibility properties.
Substitution gives (8)--(10).

Starting from an infinite admissible orbit and repeatedly taking maximal
phases produces an infinite chain satisfying (11). No phase can be infinite:
(4) reaches the nondivisible cofactor after the finite depth \(u_k\), forcing
a digit change.

Conversely, suppose a chain satisfying the displayed conditions is given.
Equation (4) supplies exactly \(u_k\) admissible steps from

\[
d_k+M^{u_k}C_k
\]

to

\[
d_k+N^{u_k}C_k.
\]

Equation (11) identifies that endpoint with the start of the next phase.
Concatenating all phases gives an infinite admissible orbit beginning at
(12). ∎

## Dependency audit

- The theorem uses only the exact induced map (1) and coprimality.
- `T-0002` supplies the separate lift from an induced orbit to Collatz.
- No assumption about periodicity, randomness, or average parity is used.

## Gap audit

- The skeleton is an equivalence, not an existence proof.
- Solving each finite congruence (10) independently may still produce only an
  adic inverse-limit object.
- A successful construction must keep every \(C_k\) an ordinary positive
  integer and must prove the chain continues uniformly.
- Periodic choices of digits and phase lengths are not automatically valid;
  the cofactors carry essential information.

## Adversarial tests

`X-0002` decomposes exact finite induced trajectories into maximal phases,
checks (4) at every intermediate state, and reconstructs the original
trajectory from (11).

## Remaining uncertainty

The equivalence appears complete but has not been independently reviewed.

## Suggested next attack

Search for parameterized solutions of (11), not isolated starting values. The
most promising target is a finite family of cofactor schemas closed under
(9), with an aperiodic but finitely generated schedule of exponents
\(u_k\). Multi-chart work can be incorporated by allowing \((M,N,D)\) to
change at designated skeleton transitions.
