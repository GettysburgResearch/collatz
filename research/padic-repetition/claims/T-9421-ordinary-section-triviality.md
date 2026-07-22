# T-9421 — Withdrawn ordinary-section triviality claim

Claim ID: `T-9421`  
Title: The attempted negative resolution of M1 depended on the withdrawn rationality-periodicity classification  
Status: `WITHDRAWN — INVALID PROOF; M1 REMAINS OPEN`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Withdrawn: 2026-07-22  
Dependencies audited: `D-9401`, withdrawn `T-9420`  
Scope: the full binary `64 -> 81` ordinary section  
Related counterexample candidates: issue #4 M1; no `K-####` candidate

## Withdrawn statement

The previous version claimed

```text
Phi({0,1}^N) intersect Z_(>=0)={0,1}.                 (1)
```

That conclusion is **not proved**. Issue #4's M1 question remains open.

## Why the proof fails

The endpoint argument would be correct **after** eventual periodicity had been
proved: an eventually periodic series is one rational-function expression, so
its real and `2`-adic evaluations represent the same rational number; the real
value then lies in `[0,1]`.

But the required implication

```text
Phi(epsilon) rational in Q_2
 -> epsilon eventually periodic                       (2)
```

was the withdrawn `T-9420`. Its proof used a compact real bound on separate
real tail limits to bound rational `2`-adic tail numerators. That completion
identification is invalid.

Therefore the real endpoint classification cannot be applied to an arbitrary
ordinary `2`-adic code.

## What remains valid

- `Phi(000...)=0` and `Phi(111...)=1`.
- Among **eventually periodic** codes, the only nonnegative ordinary integer
  values are `0` and `1`; this follows from the shared rational geometric
  expression and the real interval bound.
- `T-9412`--`T-9417` exclude their stated periodic and eventually periodic
  stack families.
- M1 may still contain a genuinely nonperiodic ordinary point.

## Dependency audit

The withdrawal changes no earlier theorem. It only removes a downstream claim
whose sole load-bearing premise was withdrawn `T-9420`.

## Process lesson

A conclusion as strong as M1 emptiness must retain the ordinary-height or
nearest-integer coordinate throughout the proof. A rational `Q_2` value cannot
be bounded by the positive real series with the same coefficients unless a
finite rational-function representation has already been established.

## Suggested next attack

Return to the exact M1 equivalents that keep ordinary height visible:

```text
- PR #16 appended nearest-integer block nonstabilization;
- divergence of exact finite survivor minima;
- completion-height determinants coupling real companions and 2-adic tails.
```

No negative M1 verdict should be recorded without one of these missing steps.
