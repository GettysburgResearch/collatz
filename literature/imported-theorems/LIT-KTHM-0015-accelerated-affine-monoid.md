# LIT-KTHM-0015 — Accelerated Collatz affine monoid

**Verdict:** `FOLKLORE / STANDARD`, with a complete proof.  
**Maps to:** issues #8 and #9; PR #11's valuation-fuel and cycle directions.  
**Context:** the accelerated Syracuse-cycle literature uses the same affine identity; this exact compositional packaging is reconstructed here.

For an odd integer \(x\), write

\[
S(x)=\frac{3x+1}{2^{\nu_2(3x+1)}}.
\]

Let \(a_0,\ldots,a_{k-1}\ge1\), put \(A_0=C_0=0\), and define

\[
A_{j+1}=A_j+a_j,
\qquad
C_{j+1}=3C_j+2^{A_j}.
\]

## Theorem

Whenever \(x\) follows this valuation word exactly,

\[
\boxed{2^{A_k}S^k(x)=3^kx+C_k.}
\]

Hence

\[
\boxed{x\equiv-3^{-k}C_k\pmod{2^{A_k}}.}
\]

For a word \(u\), let \(M(u)=(k_u,A_u,C_u)\). Concatenation satisfies

\[
\boxed{M(uv)=
(k_u+k_v,
 A_u+A_v,
 3^{k_v}C_u+2^{A_u}C_v).}
\]

## Proof

The one-step identity is \(2^{a_j}S(y)=3y+1\). If
\(2^{A_j}S^j(x)=3^jx+C_j\), then

\[
2^{A_{j+1}}S^{j+1}(x)
=3(2^{A_j}S^j(x))+2^{A_j}
=3^{j+1}x+3C_j+2^{A_j}.
\]

Induction proves the first formula; reduction modulo \(2^{A_k}\) gives the residue. Applying the summary for \(v\) after the summary for \(u\) gives

\[
2^{A_u+A_v}S^{k_u+k_v}(x)
=3^{k_v}(3^{k_u}x+C_u)+2^{A_u}C_v,
\]

which is the composition law. ∎

## Boundary

The residue is necessary, not sufficient: every intermediate valuation must be checked. Compatible nested residues define a `2`-adic point, not automatically one ordinary positive integer.