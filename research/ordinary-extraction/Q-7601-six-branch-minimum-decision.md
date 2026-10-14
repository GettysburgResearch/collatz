# Q-7601 — Decide the six-branch least-root sequence

Claim ID: `Q-7601`  
Title: Is the least positive root of the six-digit rational-base language bounded or divergent?  
Status: `IDEA / GLOBAL BLOCKER`  
Authoring agent: `gpt56-global-01`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: `T-7603`  
Scope: the exact PR `#45` / PR `#50` six-branch chart only  
Related counterexample candidates: none

## Statement

With the notation of `T-7603`, decide exactly one of:

\[
\boxed{\sup_n m_n<\infty}
\]

or

\[
\boxed{m_n\longrightarrow\infty.}
\]

Because `(m_n)` is a nondecreasing integer sequence, there is no third case.

## Why this target is legitimate

A bounded sequence stabilizes at one explicit positive integer whose restricted minimal word is legal forever.  Subject to the branch-qualified physical conjugacy and exact replay, this supplies a `K`-candidate.

Divergence proves that no positive ordinary integer lies in the complete six-digit language.  This eliminates the entire fixed six-branch architecture but says nothing about other Collatz counterexamples.

The problem is therefore an exhaustive decision for one fixed subsystem.  It is not a reformulation of all Collatz behavior.

## What would count as a positive proof

At least one of:

1. one explicit `x_*` with an all-time induction proving every digit lies in `A`;
2. a finite set `F` meeting every `S_n`, followed by `T-7601`;
3. a seed-preserving recursive embedding that proves `x_*` belongs to every finite language;
4. a nonlinear arithmetic invariant that is closed under the canonical ceiling map and contained in the six allowed digit cells.

## What would count as a negative proof

At least one of:

1. a recurrence `m_(n+k)>=m_n+c_n` with cumulative growth to infinity;
2. an eventual forbidden-digit theorem for every positive integer root;
3. a ranking or completion-height invariant proving all ordinary roots exit;
4. a source theorem specialized exactly to `(P,Q,A)` that forces digit escape.

## What does not count

- another long finite prefix;
- a compatible `2`-adic word;
- an eventually periodic or prescribed aperiodic controller;
- factor-complexity lower bounds without digit escape;
- a finite-state graph with existential high digits;
- conditional growth after all-time legality;
- a numerical trend in `m_n` without a uniform theorem.

## Current status

No boundedness proof, divergence proof, explicit forever-defined root, or exact digit-escape theorem is present in the inspected repository state.  The normality prediction is conjectural.
