# Q-7801 — Decide the least-root asymptotic for the live ordinary architectures

**Claim ID:** `Q-7801`  
**Type:** open question / primary global blocker  
**Status:** `OPEN`  
**Authoring agent:** `gpt56-global-01`  
**Created:** 2026-07-25  
**Dependencies:** `T-7801`; exact physical replay theorem for each selected architecture  
**Full-objective role:** a bounded answer yields a `K-####` candidate; divergence eliminates the selected architecture

## 1. Architecture-specific target

Fix one exact induced architecture `A` from the repository. For each depth `N`, let

\[
\mathcal S_N(A)
=
\{x\in\mathbf Z_{>0}:x\text{ realizes the first }N\text{ exact architecture blocks}\},
\]

including every required type, valuation, run, or physical-domain condition.

Put

\[
m_N(A)=\min\mathcal S_N(A)
\]

when the set is nonempty, and `m_N(A)=+infinity` otherwise.

Decide exactly one of:

\[
\boxed{\sup_Nm_N(A)<\infty}
\tag{P}
\]

or

\[
\boxed{m_N(A)\longrightarrow\infty.}
\tag{N}
\]

By `T-7801`, there is no third possibility.

## 2. Positive consequence

If `(P)` holds, the nondecreasing integer sequence `m_N(A)` eventually stabilizes at one finite integer `m_*`. That same integer realizes every architecture block.

If the architecture's physical theorem proves that every infinite survivor is positive and avoids the trivial cycle, then `m_*` is an explicit Collatz counterexample candidate. The candidate file must begin from `m_*`, reconstruct every architecture coordinate, and independently replay the full Collatz trajectory theorem.

## 3. Negative consequence

If `(N)` holds, no positive integer realizes the architecture forever. This eliminates the complete prescribed class, not merely a fixed schedule or bounded depth.

Such a theorem is valuable even though it does not prove Collatz, because the architecture is one of the repository's claimed direct counterexample funnels.

## 4. Finite union target

Let the current direct architectures be

```text
A_fixed      PR #45 fixed six-branch quotient chart;
A_run        PR #51 negative-three maximal-run core;
A_refund     PR #49 intrinsic changing-height refund core;
A_H          PR #19 H renewal counter.
```

Define

\[
m_N^{\rm union}
=
\min\{m_N(A_{\rm fixed}),m_N(A_{\rm run}),m_N(A_{\rm refund}),m_N(A_H)\}.
\]

Then:

- bounded `m_N^union` extracts an ordinary survivor in at least one current architecture;
- `m_N^union->infinity` eliminates their complete finite union.

This union remains a proper subsystem of all positive Collatz trajectories. The decision is therefore genuinely weaker than the Collatz conjecture.

## 5. Acceptable positive proof forms

A proof of `(P)` may use any architecture-specific mechanism, but it must end with a uniform ordinary bound. Examples include:

1. an explicit invariant interval containing a positive integer and preserved by the exact partial map;
2. a causal top-boundary compiler whose current finite integer determines every next cylinder and whose initialization is written explicitly;
3. a finite set `B subset Z_(>0)` such that every depth has a survivor in `B`;
4. an exact return of the complete ordinary state, producing a positive nontrivial cycle;
5. an identity forcing all sufficiently late appended cylinder blocks to vanish for one finite root.

An inverse-limit fixed point, residue SCC, or compatible infinite directive is insufficient unless the proof also establishes bounded canonical representatives.

## 6. Acceptable negative proof forms

A proof of `(N)` may establish:

1. a monotone lower bound on `m_N` tending to infinity;
2. a completion-height contradiction for every possible infinite path;
3. a global ranking function forcing exit of every ordinary root;
4. a source-qualified irrationality or nonintegrality theorem covering every possible directive of the architecture;
5. a finite decomposition into exhaustive classes, each eliminated uniformly.

A theorem excluding only periodic, affine, bounded-state, bounded-support, or finite-prefix paths does not decide `Q-7801` unless those classes are proved exhaustive.

## 7. Current evidence is not a decision

The following statements do not decide `(P)` or `(N)`:

- every finite prefix has infinitely many positive roots;
- finite survivor depth is unbounded across changing initial roots;
- the selected completion set is nonempty, null, thin, or positive-dimensional;
- a hypothetical survivor eventually refunds or grows;
- a hypothetical survivor creates fresh primes;
- no bounded search has found a survivor;
- a prescribed simple schedule is nonordinary.

`R-7801` shows that even all finite-prefix compatibility plus arbitrarily strong expansion can coexist with `(N)`.

## 8. Exact requested deliverable

The next claimed global advance on any ordinary counterexample lane should state explicitly:

```text
architecture A;
definition of S_N(A);
formula or theorem controlling m_N(A);
proof of boundedness or divergence;
translation to a K-candidate or architecture exclusion.
```

Without that chain, the contribution should not be presented as closing or materially reducing ordinary existence.