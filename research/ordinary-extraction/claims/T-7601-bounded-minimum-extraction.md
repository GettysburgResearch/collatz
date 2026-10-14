# T-7601 — Bounded-minimum ordinary compactness

Claim ID: `T-7601`  
Title: Uniformly bounded finite witnesses are exactly the missing compactness principle for an ordinary infinite seed  
Status: `PROPOSED`  
Authoring agent: `gpt56-global-01`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: `D-7601`  
Scope: every prefix-correct family of positive ordinary seed sets  
Related counterexample candidates: none

## Statement

Let

\[
S_0\supseteq S_1\supseteq S_2\supseteq\cdots
\]

be nonempty subsets of `Z_{>0}`.  Put

\[
m_n=\min S_n.
\]

Then the following are equivalent:

1. There is one positive ordinary seed legal at every depth:

   \[
   \bigcap_{n\ge0}S_n\ne\varnothing.
   \]

2. The least finite-depth witnesses are uniformly bounded:

   \[
   \sup_n m_n<\infty.
   \]

3. The integer sequence `(m_n)` eventually stabilizes.

4. There is a finite set `F` of positive integers such that every depth has at least one witness in `F`.

Therefore, when every finite level is nonempty, exactly one of the following holds:

```text
ordinary extraction:
    m_n eventually stabilizes at one seed in every S_n;

ordinary escape:
    m_n -> infinity and the intersection is empty.
```

If a branch-specific theorem proves that every seed in the intersection has an unbounded physical Collatz orbit, then stabilization of `m_n` immediately supplies an explicit counterexample seed.  If `m_n->infinity`, the entire fixed architecture has no positive ordinary survivor.

## Definitions

`S_n` must refer to the same initial ordinary seed and the complete first `n` legality conditions.  Allowing a different coordinate system or discarding earlier gates can destroy nesting and invalidates the theorem's use.

## Motivation

This theorem identifies the exact valid replacement for the false inference

\[
\forall n\ \exists x_n
\quad\Longrightarrow\quad
\exists x\ \forall n.
\]

The replacement is a uniform ordinary bound on the finite witnesses.

## Proof or construction

Because `S_(n+1)` is contained in `S_n`, their minima satisfy

\[
m_0\le m_1\le m_2\le\cdots.
\]

If one seed `x` belongs to every `S_n`, then

\[
m_n\le x
\]

for every `n`; hence `(m_n)` is bounded.

A bounded nondecreasing sequence of positive integers is eventually constant.  Thus part 2 implies part 3.

Assume that

\[
m_n=m
\qquad(n\ge N).
\]

By definition of the minimum, `m` belongs to `S_n` for every `n>=N`.  Since the sets are nested, `S_N` is contained in every earlier `S_n`.  Hence `m` belongs to all `S_n`, proving part 1.

Parts 2 and 4 are equivalent.  A finite witness set gives the bound `max F`; conversely a uniform bound `B` allows `F={1,...,B}`.

The final dichotomy follows because a nondecreasing integer sequence that is not bounded tends to infinity. ∎

## Dependency audit

No compactness theorem, choice principle, or external result is used.  The proof is the well-ordering of positive integers plus monotonicity.

## Gap audit

- `S_n` being infinite does not help.
- Every `S_n` containing an arithmetic progression does not help.
- Existence of an inverse-limit point does not bound `m_n`.
- A sequence of different witnesses `x_n` with rapidly growing size is compatible with empty intersection.
- Conditional growth of a seed already in the intersection is not used to establish nonemptiness.
- A bounded subsequence is enough because `(m_n)` is nondecreasing; arbitrary finite witnesses need not themselves form a bounded sequence unless one selects the minima.

## Adversarial tests

1. `S_n={n,n+1,...}` has `m_n=n` and empty intersection.
2. `S_n={7,7+K_n,7+2K_n,...}` has constant minimum `7` and intersection containing `7`.
3. Nested residue classes of a noninteger `2`-adic point have nonempty infinite `S_n` but `m_n->infinity`.
4. If one depth is empty, the architecture is already excluded and the theorem is applied only up to that observation.

## Remaining uncertainty

None in the theorem.  The hard mathematical work in a live Collatz architecture is to prove boundedness or divergence of its concrete `m_n`.

## Suggested next attack

For the six-branch chart of PR `#45` / PR `#50`, stop ranking long survivors by depth alone.  Seek either:

- a uniform bound on the least allowed minimal-word root;
- a renormalization inequality forcing those least roots to infinity;
- or an inductive finite set closed under the exact decoder.

Any of these directly decides the architecture.
