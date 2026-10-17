# T-9418 — Withdrawn unbounded-gap irrationality claim

Claim ID: `T-9418`  
Title: The attempted deduction from unbounded gaps to irrationality conflated real and `2`-adic limits  
Status: `WITHDRAWN — INVALID PROOF; STATEMENT OPEN`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Withdrawn: 2026-07-22  
Dependencies audited: `L-9416`  
Scope: method correction for binary `64/81` series  
Related counterexample candidates: none

## Withdrawn statement

The previous version claimed that a binary `64/81` series with infinite support
and unbounded gaps could not have a rational `2`-adic value.

That conclusion is **not proved**.

## First invalid inference

Let

```text
Y_(j,N)=sum_(k=j)^N (64/81)^[h_k-h_j].                (1)
```

These rational partial sums converge in both `R` and `Q_2`, but generally to
two different completion values:

```text
Y_j^(infinity)=lim_N Y_(j,N) in R,
Y_j^(2)       =lim_N Y_(j,N) in Q_2.                  (2)
```

`L-9416` concerns the rationality and reduced denominators of `Y_j^(2)`.
The geometric estimate

```text
1<Y_j^(infinity)<=1/(1-64/81)                         (3)
```

concerns `Y_j^(infinity)`.

The withdrawn proof silently identified the two values and applied (3) to the
rational `2`-adic tail. No such identification was established.

A rational sequence can converge to different rational limits in the two
completions. For example,

```text
x_N=2^N/(1+2^N)
```

tends to `1` in `R` and to `0` in `Q_2`.

## What remains valid

`L-9416` is valid after its completion convention is made explicit:

```text
rational 2-adic one-tail
 -> every later reduced denominator divides the initial denominator.        (4)
```

But (4) does not bound the ordinary numerators of those rational values. Hence
it does not give a finite rational state set or a real limit-point
contradiction.

## Current status of the mathematical statement

No counterexample to the withdrawn statement is supplied here. The statement
may still be true, but its proof requires a new cross-completion height
argument: an ordinary numerator bound, a trapped normalization, or a nonzero
integer whose `2`-adic divisibility outruns its archimedean height.

## Dependency audit

- The invalid step is wholly downstream of `L-9416`.
- No earlier Padé, repetition, demand-tree, or source-dependent theorem is
  affected.
- `T-9419`, `T-9420`, and `T-9421` depended on the same completion conflation and
  are withdrawn separately.

## Process lesson

Whenever one rational sequence is evaluated in two completions, the repository
must name the completion-specific limits separately. Equality may be used only
for a finite expression or after eventual periodicity/rational-function
representation has already been proved independently.

## Suggested next attack

Use the exact denominator chain only as one coordinate in a genuine
completion-height argument. Do not infer archimedean boundedness from positive
real partial sums of the same formal series.
