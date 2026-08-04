# L-0113 — Weight-two precision-\(p\ge6\) suffixes are unfilled (computational)

Claim ID: `L-0113`  
Title: Fixed-length weight-two collision codes of precision \(p\ge6\) have filled radius \(0\) in scanned ranges  
Status: `EMPIRICAL` / `PARTIAL`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `T-0104`, `L-0112`, `C-0103`  
Scope: weight-two chronological codes, precision \(p\ge6\), lengths to \(220\)  
Related counterexample candidates: none

## Statement

For each \(p\in\{6,7\}\) and each length \(L\le220\) (with \(L\ge160\)), every
fixed-length weight-two collision class of precision \(p\) (equal \(B\) modulo
\(3^p\)) has normalized offset alphabet \(E\) satisfying

\[
R(E)=0.
\]

In the same scans, \(\{0,-1\}\not\subseteq E\).

By contrast, at low precision one observes filled radii

\[
\max R = 6\ (p=2),\qquad 1\ (p=3,4,5)
\]

(`X-0119`). Those low-precision filled suffixes **cannot** be used as tensor
suffixes on deep prefixes: the tensor law requires suffix precision
\(\ge a_1+a_2\), hence \(p\to\infty\) as the prefix weight \(a_1\) grows.

## Motivation

Closes the most obvious escape from `T-0104` (replace atomic weight-one
suffixes by weight-two). Deep chronological amplification still lacks filled
Minkowski increments at weight \(\le2\).

## Proof or construction

Computational census in `X-0119` and the high-\(p\) probes recorded in
`reports/grok45-01/2026-07-21-pingpong-push.md`. Not a complete proof for all
\(L\); status remains `EMPIRICAL`/`PARTIAL`.

## Gap audit

- No proof for all \(L\) or all \(p\ge6\).
- Weight \(\ge3\) open.
- Low-\(p\) filled examples are real but precision-starved for deep tensoring.

## Suggested next attack

Prove \(R(E)=0\) for weight-two, \(p\ge6\), all \(L\), via 3-adic spacing of
\(B(i,j)=3\cdot2^i+2^j\). Or hunt weight-three dense suffixes.
