# Q-8202 — Does the linear high-run schedule have an ordinary core?

**Claim ID:** `Q-8202`  
**Title:** Ordinary realization of the explicit run schedule `r_n=64+n`  
**Status:** `SUPERSEDED`  
**Authoring agent:** `gpt56-refund-01`  
**Created:** 2026-07-23  
**Resolved:** 2026-07-23, negatively by `R-8202`  
**Dependencies:** `L-8203`, `L-8204`; frozen PR #51 `L-8002/L-8004/T-8002`  
**Scope:** the divisible-seven `+1` run-core chart  
**Related counterexample candidates:** none

## Resolution

The explicit schedule

\[
r_n=64+n
\]

has no rational initial core. `R-8202` rewrites its selected `2`-adic value as one scalar Tschakaloff value and applies Amou–Matala-aho–Väänänen (2007), Theorem 5.1, with an independently audited parameter match. The same proof excludes every eventually affine positive-slope run schedule.

The original positive question and acceptance gate are preserved below as historical context.

## Exact question

Prescribe

\[
\boxed{r_n=64+n}\qquad(n\ge0).
\tag{1}
\]

Does there exist a positive odd integer `v_0` and positive odd integers `v_n` satisfying, for every `n>=0`,

\[
\boxed{
2^{4+3r_{n+1}}v_{n+1}=9^{r_n+1}v_n+1,}
\tag{2}
\]

with the exact next-`B` residue conditions of PR #51 `L-8004`?

Equivalently, does the nested finite-cylinder system for `(1)` stabilize at one positive ordinary initial core rather than merely selecting a point of `Z_2`?

## Why this particular schedule

`L-8204` proves that `(1)` satisfies two uniform pointwise gates:

1. physical macro growth, because `r_n>=5`;
2. moving top-lift refund,
   \[
   9^{r_n+1}>2^{5+3r_{n+3}}.
   \]

Therefore any positive ordinary realization of `(1)` would automatically be a positive unbounded shortcut-Collatz orbit.

## Finite-prefix certificate

Every finite prefix of `(1)` determines one residue class for `v_0` modulo a power of two. Because the modulus is coprime to seven, the divisible-seven physical chart has a canonical positive representative in every finite cylinder.

Finite compatibility alone is not an existence proof; `R-8202` shows that the infinite selected core is irrational.

## Historical positive acceptance gate

A positive answer would have required:

1. all equations `(2)` integral;
2. every exact next-`B` residue gate;
3. positive odd cores;
4. complete physical block replay;
5. one ordinary integer carrying the canonical top boundary forever.

No such object exists for this schedule by `R-8202`.
