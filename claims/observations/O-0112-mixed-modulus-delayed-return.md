# O-0112 — Mixed-modulus supercritical concatenations delay return, still return

Claim ID: `O-0112`  
Title: Length-48 all-odd mixed-modulus words give huge peaks then triviality  
Status: `EMPIRICAL`  
Authoring agent: `grok45-01`  
Created: 2026-07-21  
Dependencies: `O-0111`  
Scope: `X-0136`  
Related counterexample candidates: none (checked)

## Statement

Corrected beam search concatenating supercritical blocks under
\(\mathrm{mod}\,2^{L}\) with optional \(\mathrm{mod}\,3/5\) filters reached
words of length \(48\) (all ones) with affine growth \(\sim2.8\cdot10^8\).

Sample integers in the winning classes (e.g.
\(n=17169973579350015\)) achieve peak ratios \(>10^{10}\) and do **not**
hit \(\{1,2\}\) within 400 steps — but extended runs to \(10^5\) steps show
return: first drop below start around step \(180\)–\(265\), triviality by
step \(470\)–\(540\).

**No K-candidate.** The mixed-modulus ladder buys delay, not divergence.

## Interpretation

Odd moduli do not by themselves convert highway spikes into divergent
orbits in this alphabet. Residual: non-all-ones concatenations, larger
prime moduli, or a theorem bounding return after density-\(1\) odd runs.
