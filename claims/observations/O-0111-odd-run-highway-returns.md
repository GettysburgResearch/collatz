# O-0111 — Odd-run highways spike then return to the trivial cycle

Claim ID: `O-0111`  
Title: Nested odd-run CRT ladders produce large peaks, not divergence  
Status: `EMPIRICAL`  
Authoring agent: `grok45-01`  
Created: 2026-07-21  
Dependencies: none  
Scope: `X-0135`  
Related counterexample candidates: none

## Statement

For odd-run words \(1^k\) with \(k\le19\), sample lifts, nested CRT ladders
through \(k=13\), and evergreen \(k=20\) seeds:

- highway growth matches \((3/2)^k\) as expected;
- peak ratios reach \(>10^5\) (evergreen \(>8\cdot10^4\));
- **every** scanned trajectory hit the trivial cycle \(\{1,2\}\) within the
  horizon (no 300-step post-highway survivors).

## Interpretation

Odd-run highways are real archimedean engines but, alone, appear to feed
back into the trivial basin. Next: interleave highways with odd-modulus
constraints (`X-0136`) or prove a post-highway return bound.
