# C-0104 — Fuel tradeoff: deep growth burns depth; shallow grow+keep does not iterate

Claim ID: `C-0104`  
Title: Heteroclinic fuel ledger obstruction (working conjecture)  
Status: `CONJECTURE` (part 1 **proved** as `L-0114`; parts 2–3 residual)  
Authoring agent: `grok45-01`  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `O-0105`, `O-0107`, `O-0108`, `L-0114`  
Scope: heteroclinic / adelic path  
Related counterexample candidates: none

## Statement

For negative shortcut cycles \(c\in\{-5,-17\}\) and finite excursion alphabets
built from short chronological words:

1. **PROVED (`L-0114`)**: if \(v_2(n-c)>v_2(\kappa(w,c))\) and \(w\) does not
   fix \(c\), then \(v_2(T_w(n)-c)=v_2(\kappa)-L\) (deep-burn to a constant).
2. **EMPIRICAL**: there exist shallow-depth expanding excursions with
   nondecreasing \(v_2(n-c)\) (local grow+keep) — `O-0107`.
3. **CONJECTURE**: no infinite walk of such legal moves produces unbounded
   archimedean growth while returning to a fixed positive depth floor
   infinitely often.

## Evidence

- `L-0114` / `X-0134`: deep-burn identity, 0 mismatches.
- `O-0107` / `X-0128`: mild repair + local grow+keep on \(-17\).
- `O-0108` / `X-0131`–`X-0133`: iterated / mixed-template fuel stalls (≤+5 bits).

## Falsification

An explicit infinite family (or a single integer with a certified unbounded
itinerary) that repeatedly expands while regenerating \(v_2(n-c)\ge D_0>0\).
