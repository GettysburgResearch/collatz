# L-0115 — 3-adic valuation ledger for affine Collatz blocks

Claim ID: `L-0115`  
Title: \(v_3(T_w(n)-c)=v_3(\kappa+3^a(n-c))\) (ultrametric cases)  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`, `L-0114`  
Scope: 3-adic hybrid path (`D-ADIC3-*`)  
Related counterexample candidates: none

## Statement

Let \(c\in\mathbb Z\), \(w\) a chronological word of length \(L\) with \(a\) ones,
\(B=B(w)\), and

\[
\kappa(w,c)=3^a c+B-c\,2^L,\qquad
T_w(n)=\frac{3^a n+B}{2^L}
\]

for integers \(n\) following \(w\). As in `L-0114`,

\[
2^L\bigl(T_w(n)-c\bigr)=\kappa+3^a(n-c).
\]

Since \(v_3(2^L)=0\),

\[
\boxed{v_3\bigl(T_w(n)-c\bigr)=v_3\bigl(\kappa+3^a(n-c)\bigr).}
\]

Write \(d=v_3(n-c)\), \(v_n=d+a=v_3(3^a(n-c))\), and
\(v_\kappa=v_3(\kappa)\) when \(\kappa\neq0\). By the ultrametric inequality:

1. If \(\kappa=0\), then \(v_3(T_w(n)-c)=d+a\).
2. If \(\kappa\neq0\) and \(v_\kappa < v_n\), then \(v_3(T_w(n)-c)=v_\kappa\).
3. If \(\kappa\neq0\) and \(v_n < v_\kappa\), then \(v_3(T_w(n)-c)=v_n=d+a\).
4. If \(\kappa\neq0\) and \(v_n=v_\kappa\), then
   \(v_3(T_w(n)-c)\ge v_\kappa\), with equality unless the leading digits cancel.

## Contrast with `L-0114`

| | 2-adic | 3-adic |
|---|---|---|
| Divide by \(2^L\) | subtracts \(L\) | invisible (unit) |
| \(\kappa=0\) hold | depth \(-L\) | depth \(+a\) |
| Dominant \(\kappa\) | collapse to \(v_2(\kappa)-L\) | collapse to \(v_3(\kappa)\) |

## Proof

Immediate from the affine identity, \(v_3(2)=0\), \(v_3(3^a)=a\), and the
ultrametric inequality.

## Empirical check

`X-0139` (corrected case split): mismatches \(=0\) on the scanned library.

## Consequence

Template holds on a negative cycle regenerate 3-adic depth (\(+a\)) but burn
2-adic depth (\(-L\) by `L-0114`). Finite 2-adic bank ⇒ finitely many holds ⇒
bounded archimedean boost from pure holds. 3-adic regeneration does not refund
2-adic fuel.
