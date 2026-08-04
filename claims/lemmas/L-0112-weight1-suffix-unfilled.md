# L-0112 — Weight-one high-precision suffixes have unfilled offset alphabets

Claim ID: `L-0112`  
Title: Precision \(p\ge2\) weight-one collision classes have filled difference radius \(0\)  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `T-0104`, `C-0103`  
Scope: weight-one chronological parity collision codes  
Related counterexample candidates: none (obstruction)

## Statement

Let \(p\ge2\). Consider any finite set \(J\) of bit-positions such that the
weight-one words \(e_j\) (single \(1\) at position \(j\)) form a collision code
of precision \(p\), i.e.

\[
2^{j}\equiv2^{j_0}\pmod{3^p}\qquad(j\in J)
\]

for a reference \(j_0\in J\). Let \(E\) be the corresponding normalized offset
alphabet (integers \((2^{j_0}-2^j)/3^p\)). Then

\[
\boxed{R(E)=0,}
\]

i.e. \([-1,1]\not\subseteq E-E\) beyond the trivial \(\{0\}\) — equivalently,
\(E\) is not a translate of a filled interval of length \(\ge1\). In particular
\(E\) cannot supply a filled Minkowski increment at suffix scale.

(Empirical strengthening from `X-0118`: the same holds for all scanned
classes with \(2\le p\le8\), and \(\max|E|=4\) in those scans.)

## Proof sketch

The multiplicative order of \(2\) modulo \(3^p\) is \(\varphi(3^p)=2\cdot3^{p-1}\)
for \(p\ge1\). Hence each admissible residue class for \(2^j\) is hit by an
arithmetic progression of positions with difference \(d=2\cdot3^{p-1}\). The
associated offsets are

\[
\frac{2^{j_0}-2^{j_0+kd}}{3^p}
=2^{j_0}\frac{1-2^{kd}}{3^p},
\qquad k\in\mathbb Z.
\]

For \(p\ge2\), the smallest nonzero absolute offset arising from \(k=\pm1\)
already has absolute value

\[
\frac{2^{j_0}(2^d-1)}{3^p}
\ge\frac{2^d-1}{3^p}
=\frac{2^{2\cdot3^{p-1}}-1}{3^p}\ge\frac{2^6-1}{9}>1
\]

(and vastly larger for \(p>2\)). Therefore \(1\notin E-E\), so \(R(E)=0\).

(The atomic two-point code is the case \(|J|=2\), already covered.)

## Motivation

Partial confirmation of `C-0103` and fuel for strengthening `T-0104` beyond
purely atomic suffixes: **all** weight-one precision-\(p\ge2\) suffixes are
unfilled.

## Gap audit

- Weight \(\ge2\) suffixes remain open (the heart of residual `C-0103`).
- Uses the standard order of \(2\) mod \(3^p\); elementary LTE/order proof can
  be inlined if required by a verifier.

## Adversarial tests

`X-0118`: for \(p=2..8\), every rich class has \(R_{\mathrm{filled}}=0\);
only \(p=1\) yields \(R=1\).

## Suggested next attack

Weight-two precision-\(p\) collision codes: enumerate small \(p\) and compute
\(R(E)\).
