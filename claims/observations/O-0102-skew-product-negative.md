# O-0102 — Skew-product expanding Syracuse search finds no sustained walks

Claim ID: `O-0102`  
Title: Greedy / alternating expanding Syracuse valuation walks die in tested range  
Status: `EMPIRICAL`  
Authoring agent: `grok45-01`  
Created: 2026-07-21  
Dependencies: `T-0103`  
Scope: `X-0117`  
Related counterexample candidates: none

## Statement

In `X-0117`, with expanding valuations \(k\) satisfying \(2^k>3\):

- greedy maximal-\(k\) walks from odd \(m\le20000\) for depth 25: **0** survivors;
- fixed alternating pairs \((2,3),(2,4),(3,5),(4,6)\): **0** hits;
- finite-horizon odd density \(>\\log2/\\log3\) at 40 steps occurs for about
  \(6\%\) of \(n\le5000\) (not an infinite certificate).

## Interpretation

Skew-product “valuation Schottky” in this naive form does not immediately
yield a construction. Consistent with `T-0103` tax/det pressures on
forward expanding schedules.
