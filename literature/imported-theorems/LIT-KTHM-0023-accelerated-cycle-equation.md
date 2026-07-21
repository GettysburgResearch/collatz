# LIT-KTHM-0023 — Exact accelerated-cycle equation

**Verdict:** `KNOWN — EXACT` in the classical cycle literature; complete derivation supplied.  
**Maps to:** issue #9 and PR #11's exact cycle direction.  
**Sources:** Eliahou's cycle-length bounds and Simons–de Weger's theoretical/computational cycle analysis use this affine cycle framework.

Let an accelerated odd orbit have valuations \(a_i=\nu_2(3n_i+1)\), \(0\le i<k\). Put

\[
A=\sum_{i=0}^{k-1}a_i,
\qquad
A_j=\sum_{i=0}^{j-1}a_i.
\]

## Theorem

If \(n_k=n_0\), then

\[
\boxed{
(2^A-3^k)n_0
=
\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}.
}
\tag{1}
\]

A proposed word yields a positive cycle exactly when the right side is divisible by \(2^A-3^k>0\), the quotient is a positive odd integer, and direct replay gives each prescribed valuation and returns to the start.

## Proof

`LIT-KTHM-0015` gives

\[
2^A S^k(n_0)=3^kn_0+C_k.
\]

Unrolling \(C_{j+1}=3C_j+2^{A_j}\) yields

\[
C_k=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}.
\]

Set \(S^k(n_0)=n_0\) and rearrange to obtain (1). Conversely, divisibility reconstructs a candidate start, but exact replay is required because the affine equation alone does not force the intermediate valuations. ∎

## Boundary

- Real growth inequalities do not replace integrality.
- The accelerated-step count is not automatically the local-minimum count used in every published cycle bound.
- A compressed solver must expand enough structure to check the parameter of the theorem it cites.