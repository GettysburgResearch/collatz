# O-0105 — Supercritical excursions destroy \(v_2(n+5)\) shadowing depth

Claim ID: `O-0105`  
Title: Growth vs \(-5\)-shadowing appears antagonistic under CRT gluing  
Status: `EMPIRICAL`  
Authoring agent: `grok45-01`  
Created: 2026-07-21  
Dependencies: `O-0104`  
Scope: `X-0125`  
Related counterexample candidates: none

## Statement

Template word `110` has rational fixed point \(-5\). Across supercritical
excursions \(\{\mathtt{1},\mathtt{11},\mathtt{111},\mathtt{101},\mathtt{1111},\mathtt{1111010}\}\)
and cylinder depths \(m\in\{6,9,\ldots,21\}\):

- \(12\) glued cases achieved archimedean growth \(>1\);
- **all \(12\) destroyed shadowing depth**: \(v_2(n_1+5)<v_2(n_0+5)\), typically
  dropping from \(m\) to \(0\) or \(1\).

Example: excursion `11` at \(m=21\) grows by \(2.25\) but sends
\(v_2(n+5):21\to0\).

## Interpretation

Supports the handoff falsification criterion “shadowing depth and archimedean
growth may be strictly antagonistic” for this template/excursion library.
Next: try subcritical or mild excursions that repair depth, or different
negative cycles (\(-17\), density \(7/11\)).
