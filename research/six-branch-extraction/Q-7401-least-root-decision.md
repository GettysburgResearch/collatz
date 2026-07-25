# Q-7401 — Decide ordinary extraction in the six-branch chart

Claim ID: `Q-7401`  
Title: Does the least positive root of the six-branch minimal-word language stabilize or escape?  
Status: `IDEA / GLOBAL BLOCKER`  
Authoring agent: `gpt56-extraction-01`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: `D-7401`, `L-7401`, `T-7401`; branch-qualified PR #57 `T-7601/T-7603` for the common least-root formulation  
Scope: the fixed six-branch `3^12/2^19` subsystem only  
Related counterexample candidates: none

## Exact decision

With `S_n` and `m_n` from `D-7401`, prove exactly one of

\[
\boxed{\sup_n m_n<\infty}
\]

or

\[
\boxed{m_n\longrightarrow\infty.}
\]

There is no third case because `(m_n)` is a nondecreasing sequence of positive integers whenever every level is nonempty.

## Positive consequence

If `(m_n)` is bounded, it eventually equals one integer `x_*`. Then

\[
x_*\in S_n
\qquad\text{for every }n,
\]

so its canonical minimal word uses only `A` forever.

Subject only to independent reconstruction of the existing PR #45 / PR #50 physical conjugacy, this gives one explicit positive unbounded shortcut-Collatz orbit. The object may then be allocated a `K-####` identifier and sent to exact physical replay.

This positive statement is not a weaker theorem than the desired construction. It is the construction, restricted to one fixed chart.

## Negative consequence

If `m_n -> infinity`, then

\[
\bigcap_nS_n=\varnothing.
\]

No positive ordinary integer belongs to the complete six-branch language. This eliminates the entire fixed subsystem but makes no assertion about counterexamples outside it.

This is genuinely weaker than resolving Collatz globally.

## What has now been ruled out

### Direct quotient recursion

`L-7401` proves

\[
x\in S_2
\Longrightarrow
\lfloor x/Q\rfloor\notin S_1.
\]

### Finite-state affine quotient recursion

`T-7401` proves that the only integer-affine renormalization of the high quotient that recreates all six branch transitions is the original forward map

\[
y=F(x),
\]

which is expanding and supplies no least-root descent.

Therefore a boundedness proof cannot come from the obvious self-similar affine subtree.

## What would settle the positive side

At least one of:

1. one explicit integer `x_*` and an induction proving `delta(F^n(x_*)) in A` for every `n`;
2. one finite ordinary set meeting every nested `S_n`;
3. a genuinely nonlinear seed-preserving section with a proved ordinary height bound;
4. a direct full physical cycle or divergent orbit certificate bypassing this chart.

## What would settle the negative side

At least one of:

1. a global lower-bound recurrence for `m_n` with divergent cumulative gain;
2. a theorem that every positive rational-base root eventually emits a digit outside `A`;
3. an ordinary-height or product-formula obstruction specialized to this exact alphabet;
4. a proof that every possible non-affine section orbit has unbounded least representatives.

## What does not settle either side

- a longer compatible prefix;
- a completed `2`-adic word;
- an amplifier or refund theorem after legality is assumed;
- a periodic or prescribed aperiodic controller;
- entropy or factor-complexity growth without digit escape;
- a fixed-modulus SCC or existential high block;
- the conjectural normality of rational-base minimal words;
- numerical growth of the first finitely many `m_n`.

## Current status

No inspected theorem decides the sequence. The known rational-base normality statement that would imply digit escape remains conjectural. The exact Dubickas complexity lower bound is compatible with a six-letter word and therefore does not decide the chart.

## Recommended next action

Attack one global assertion only:

\[
\boxed{m_n\to\infty.}
\]

A proof eliminates an exhaustive proper subsystem. A disproof must produce the stabilizing integer itself and therefore crosses directly to candidate review.