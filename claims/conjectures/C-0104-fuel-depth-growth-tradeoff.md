# C-0104 — Fuel tradeoff: deep growth burns depth; shallow grow+keep does not iterate

Claim ID: `C-0104`  
Title: Heteroclinic fuel ledger obstruction (working conjecture)  
Status: `CONJECTURE`  
Authoring agent: `grok45-01`  
Created: 2026-07-21  
Dependencies: `O-0105`, `O-0107`, `O-0108`  
Scope: heteroclinic / adelic path  
Related counterexample candidates: none

## Statement (speculative)

For negative shortcut cycles \(c\in\{-5,-17\}\) and finite excursion alphabets
built from short chronological words:

1. If \(v_2(n-c)\) is larger than the excursion length scale, any
   archimedean-expanding excursion strictly decreases \(v_2(n-c)\)
   (deep-burn).
2. There exist shallow-depth expanding excursions with nondecreasing
   \(v_2(n-c)\) (local grow+keep).
3. No infinite walk composed of such legal moves produces unbounded
   archimedean growth while returning to a fixed positive depth floor
   infinitely often (no regenerative fuel engine in the classical
   concatenation alphabet).

## Evidence

- `O-0105` / `X-0125`: deep burn on \(-5\).
- `O-0107` / `X-0128`: deep burn + mild repair + local grow+keep on \(-17\).
- `O-0108` / `X-0131`: iterated grow+keep stalls (\(+2\) bits max).
- `X-0130`: regenerative *events* appear in a coarse automaton but with
  no \(+8\) size-bucket unbounded proxy.

## Falsification

An explicit infinite family (or a single integer with a certified unbounded
itinerary) that repeatedly expands while regenerating \(v_2(n-c)\ge D_0>0\).
