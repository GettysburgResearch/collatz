# LIT-KTHM-0054 — Stationary inverse-affine transported cylinders in rational base

**Status:** `KNOWN ELEMENTARY INFRASTRUCTURE / COMPLETE PROOF`  
**Created:** 2026-07-23  
**Native targets:** PR #48 `L-8210`; PR #45/PR #50 six-branch chart; centered and rational-base ordinary-marker programs  
**Literature context:** rational-base representation trees and p-adic rational-base algorithms

## Statement

Let `P>Q>=2` be coprime integers. Fix digits `a_0,a_1,...` and an exact integer path

\[
 \boxed{Qx_{n+1}=Px_n+a_n.}
\tag{1}
\]

For `s>=1`, put

\[
 C_s=\sum_{j=0}^{s-1}P^{s-1-j}Q^j a_j.
\tag{2}
\]

Then:

### 1. Exact finite-horizon identity

\[
 \boxed{Q^s x_s=P^s x_0+C_s.}
\tag{3}
\]

### 2. Unique pulled-back ordinary cylinder

Because `P` is a unit modulo `Q^s`, the first `s` digit conditions are equivalent to

\[
 \boxed{x_0\equiv\Theta_s\pmod {Q^s},
 \qquad
 \Theta_s=[-P^{-s}C_s]_{Q^s}.}
\tag{4}
\]

The residues are nested:

\[
 \boxed{\Theta_{s+1}\equiv\Theta_s\pmod {Q^s}.}
\tag{5}
\]

### 3. Transported digit recursion

There is a unique digit

\[
 d_s={\Theta_{s+1}-\Theta_s\over Q^s},
 \qquad0\le d_s<Q,
\tag{6}
\]

and the full prescribed infinite digit path selects one unique point

\[
 \Theta_\infty\in\mathbf Z_Q.
\]

The selected point is an ordinary nonnegative integer exactly when

\[
 \boxed{\Theta_s\text{ is eventually constant},}
\tag{7}
\]

or equivalently

\[
 \boxed{d_s=0\text{ for all sufficiently large }s.}
\tag{8}
\]

This is the stationary rational-base specialization of the inverse-affine transported-cylinder cocycle in PR #48 `L-8210`.

## Proof

Equation `(3)` follows by induction. For one step it is `(1)`. If it holds at `s`, then

\[
 \begin{aligned}
 Q^{s+1}x_{s+1}
 &=Q^s(Px_s+a_s)\\
 &=P(P^sx_0+C_s)+Q^sa_s\\
 &=P^{s+1}x_0+C_{s+1}.
 \end{aligned}
\]

Since `gcd(P,Q)=1`, equation `(3)` is integral at time `s` exactly when

\[
 P^sx_0+C_s\equiv0\pmod {Q^s},
\]

which has the unique solution `(4)`. The `s+1` condition implies the `s` condition, proving nesting `(5)`. Equation `(6)` is the unique mixed-radix increment between two nested least representatives.

If an ordinary nonnegative integer `x_0` satisfies every congruence, then for every sufficiently large `s` with `Q^s>x_0`, the least residue of `x_0 modulo Q^s` is exactly `x_0`; hence `Theta_s=x_0` eventually. Conversely, if `Theta_s` is eventually equal to an integer `x`, nesting shows that `x` satisfies every earlier and later cylinder. This proves `(7)--(8)`.

## Why this matters

The ordinary-marker test is not the existence of a compatible completion; compatibility always produces `Theta_infinity`. The test is whether the transported new digits eventually vanish.

For the six-branch chart of `LIT-KTHM-0053`,

\[
 (P,Q)=(3^{12},2^{19}),
\]

and the digits are restricted to six values. For PR #48/PR #49, the same theorem survives with nonstationary `P_s`, `Q_s`, and affine carries after using the full `L-8210` transport cocycle.

## Source boundary

Frougny–Klouda develop finite and eventually periodic p-adic rational-base algorithms under their own representation conventions. Those results motivate the placement of `(4)--(8)`, but they are not used to identify a separate real limit or to infer ordinary integrality automatically.

## Gap audit

- Eventual zero transported digits are a criterion, not a proof they occur.
- A finite modular lasso need not imply eventual zero most-significant support.
- In nonstationary charts, the odd multipliers and affine carries must be transported exactly as in `L-8210`.
- No counterexample is asserted.
