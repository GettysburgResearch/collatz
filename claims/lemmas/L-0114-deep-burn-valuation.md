# L-0114 — Deep 2-adic shadowing collapses under non-fixing excursions

Claim ID: `L-0114`  
Title: \(v_2(T_w(n)-c)=v_2(\kappa(w,c))-L\) whenever \(v_2(n-c)>v_2(\kappa)\)  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`  
Scope: heteroclinic / valuation-fuel path; elevates `C-0104`(1)  
Related counterexample candidates: none (obstruction)

## Statement

Let \(c\in\mathbb Z\) and let \(w\) be a chronological parity word of length \(L\)
with \(a\) ones and Collatz constant \(B=B(w)\). Write

\[
T_w(n)=\frac{3^a n+B}{2^L}
\]

for every integer \(n\) that follows \(w\), and define the **obstruction constant**

\[
\kappa(w,c)\;:=\;3^a c+B-c\,2^L.
\]

Then for every such \(n\),

\[
2^L\bigl(T_w(n)-c\bigr)=\kappa(w,c)+3^a(n-c).
\]

Consequently:

1. If \(\kappa(w,c)=0\) (i.e. \(w\) fixes \(c\)), then
   \[
   v_2\bigl(T_w(n)-c\bigr)=v_2(n-c)-L.
   \]
2. If \(\kappa(w,c)\neq0\) and \(v_2(n-c)>v_2(\kappa(w,c))\), then
   \[
   \boxed{v_2\bigl(T_w(n)-c\bigr)=v_2(\kappa(w,c))-L.}
   \]
   In particular the post-image depth is **independent of** how deep the
   pre-image shadow was: all deeper fuel is burned down to the constant
   \(v_2(\kappa)-L\).
3. If \(v_2(\kappa(w,c))<L\), then **no** integer \(n\) following \(w\) can
   satisfy \(v_2(n-c)>v_2(\kappa(w,c))\). (Otherwise the identity would force
   \(v_2(2^L(T_w(n)-c))=v_2(\kappa)<L\), contradicting integrality of
   \(T_w(n)-c\).)

## Proof

The affine identity is immediate from the definition of \(T_w\) and \(\kappa\).
For (1), \(\kappa=0\) yields \(2^L(T_w(n)-c)=3^a(n-c)\); since \(3^a\) is odd,
valuations subtract \(L\).

For (2), the two summands on the right have valuations \(v_2(\kappa)\) and
\(v_2(n-c)+v_2(3^a)=v_2(n-c)\). The hypothesis makes the first strictly
smaller, so the sum has valuation \(v_2(\kappa)\). Dividing by \(2^L\)
subtracts \(L\).

For (3): if \(v_2(n-c)>v_2(\kappa)\), then (2) would give
\(v_2(T_w(n)-c)=v_2(\kappa)-L<0\), impossible for nonzero
\(T_w(n)-c\in\mathbb Z\). If \(T_w(n)=c\), the left side of the identity
vanishes, so \(\kappa=-3^a(n-c)\) and \(v_2(\kappa)=v_2(n-c)\), contradicting
the strict inequality. Hence no such \(n\) exists.

## Empirical check

`X-0134` confirms (2) for \(c\in\{-5,-17\}\) and expanding words
`1`,`11`,`111` at depths \(10\) and \(20\): predicted depths match exactly
(e.g. \(c=-17\), \(w=\mathtt{1}\): \(\kappa=-16\), \(v_2(\kappa)-L=3\)).

Mild words with \(v_2(\kappa)<L\) (e.g. \(w=\mathtt{0}\) at \(c=-17\):
\(\kappa=17\), \(v_2=0<1\)) admit no deep pre-images, matching (3) and
explaining why mild repair in `O-0107` occurs only at shallow depth.

## Consequences for fuel path

- Deep-burn half of `C-0104` is now a lemma, not a conjecture.
- Regenerative fuel engines cannot rely on “banked” deep \(v_2(n-c)\) through
  non-fixing excursions: depth collapses to \(v_2(\kappa)-L\).
- Residual fuel search must use shallow grow+keep, chart switches with
  \(\kappa=0\) holds, or abandon single-template valuation fuel.

## Dependency audit

- Uses only the affine block formula from `D-0101` and 2-adic valuations.
- Does not depend on unmerged external claims.
