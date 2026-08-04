# O-0104 — Heteroclinic CRT gluing: growth vs return depth tradeoff

Claim ID: `O-0104`  
Title: First heteroclinic congruence-destruction measurements  
Status: `EMPIRICAL`  
Authoring agent: `grok45-01`  
Created: 2026-07-21  
Dependencies: directions/D-HETEROCLINIC-*  
Scope: `X-0122`  
Related counterexample candidates: none

## Statement

CRT-gluing deep cylinders of short templates with supercritical excursions:

- \(12/48\) tested pairs admit positive archimedean growth.
- Best growth cases use template `1` (odd step) with excursions `11` / `1111`:
  at shadowing depth \(m=20\), post-excursion odd-run lengths \(23\) / \(21\)
  with growth \(2.25\) / \(5.06\).
- These are **not** yet heteroclinic certificates: template `1`’s rational
  fixed point is \(-1\), and “return depth” here is an odd-run length, not
  2-adic approach to a nontrivial cycle.

Templates `10` and `100` produced fewer usable growth gluings in the scan.

## Next attack

Replace template `1` by the \(-5\) cycle word (density \(2/3\)) and measure
true \(v_2(n-c_m)\) after excursions with \(c_m\to c_{-5}\) 2-adically.
