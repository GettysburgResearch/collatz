# Accelerated cycle frontier at odd length 185

**Agent:** `gpt56-cycle-02`  
**Issue:** #9  
**Branch:** `agent/gpt56-cycle-02/9-factor-guided-cycle`  
**Namespace:** isolated `83xx`  
**Status:** exact finite-certificate program; no counterexample candidate

## Objective

Pursue the shortest unconditional Collatz disproof: one nontrivial positive accelerated cycle with an exact valuation word, integer fixed point, and full replay.

This packet attacks the first odd accelerated length immediately beyond the repository's length-184 frontier. It proves, conditional only on the cited 92-local-minimum theorem, that length 185 also contains no nontrivial positive cycle.

## Main result

`T-8301` classifies every possible length-185 ascent/descent skeleton with 92 local minima. Up to rotation there are exactly two:

```text
AA: 1,1,b_0,1,b_1,...,1,b_91
DD: 1,b_0,b_1,1,b_2,...,1,b_92
```

with every `b_i>=2`.

An ordered-jump identity converts all excess valuation mass into a uniquely decodable sum of dyadically separated suffix weights. Uniform multiplier bounds reduce all infinitely many excess heights to exact scans at the low heights and one reference scan at height 31. The reference failures are stable under every larger height.

Therefore no nontrivial positive accelerated Collatz cycle has odd-state length 185.

## Exact artifacts

- theorem: `claims/T-8301-no-positive-accelerated-cycle-length-185.md`
- author checker: `../../experiments/X-8301-cycle-185-decoder/run.py`
- independent checker: `../../experiments/X-8301-cycle-185-decoder/verify.py`
- frozen result: `../../experiments/X-8301-cycle-185-decoder/results/canonical.json`
- report: `../../reports/gpt56-cycle-02/2026-07-22-9-cycle-length-185.md`

## Scope boundary

This removes one exact accelerated length. It does not prove the Collatz conjecture and does not construct a cycle. The constructive next target is length 186 and, more broadly, a compressed primitive valuation circuit satisfying the complete cycle identity.
