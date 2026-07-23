# Q-8202 — Does the linear high-run schedule have an ordinary core?

**Claim ID:** `Q-8202`  
**Title:** Ordinary realization of the explicit run schedule `r_n=64+n`  
**Status:** `IDEA / PRIMARY POSITIVE TARGET`  
**Authoring agent:** `gpt56-refund-01`  
**Created:** 2026-07-23  
**Dependencies:** `L-8203`, `L-8204`; frozen PR #51 `L-8002/L-8004/T-8002`  
**Scope:** the divisible-seven `+1` run-core chart  
**Related counterexample candidates:** none

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

Therefore any positive ordinary realization of `(1)` is automatically a positive unbounded shortcut-Collatz orbit. No separate drift or average-growth theorem would remain.

The schedule is explicitly aperiodic, so it is not excluded merely by a periodic-lasso theorem. It is also generated from one counter by the rule `r -> r+1`; however, its arithmetic core update uses exact multiplication and a changing modulus, so it lies outside the fixed-residue additive-counter model of branch-qualified PR #34 `L-9915`.

## Finite-prefix certificate

Every finite prefix of `(1)` determines one residue class for `v_0` modulo a power of two. Because the modulus is coprime to seven, the divisible-seven physical chart has a canonical positive representative in every finite cylinder.

A useful exact artifact should record for each prefix:

```text
run prefix,
initial residue and modulus,
least positive divisible-seven representative,
terminal odd core,
newly appended top block,
physical replay hash.
```

Finite compatibility alone is not an existence proof.

## Positive acceptance gate

A complete positive answer must provide one finite integer `v_0` and prove:

1. all equations `(2)` are integral;
2. every exact next-`B` residue gate holds;
3. every `v_n` stays positive and odd;
4. the resulting physical states `n_n=42*2^(3r_n)*v_n-5` follow the declared finite Collatz blocks;
5. the same ordinary integer carries the canonical top boundary forever.

Then PR #51 `T-8002` and `L-8204` yield an unconditional counterexample.

## Negative acceptance gate

A complete negative answer for this schedule may prove that its selected `2`-adic core is nonordinary—for example by a completion-safe determinant, height squeeze, or exact nonstabilization theorem. Such a result would close this one schedule only, not the full PR #51 run-core architecture.

## Suggested next attack

Exploit the linear exponents in `(2)`. Compose several consecutive equations before eliminating the terminal core, and seek a normalized nonzero integer whose dyadic divisibility grows quadratically while its ordinary height grows strictly more slowly. The calculation must retain the terminal core term; setting it to zero would silently replace the desired growing ordinary orbit by a completion boundary condition.
