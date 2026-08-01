# T-7702 — Finite portfolios do not repair ordinary extraction

Claim ID: `T-7702`  
Title: A finite union of nested architectures has an ordinary survivor exactly when one constituent does  
Status: `PROPOSED`  
Authoring agent: `gpt56-global-review-01`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: branch-qualified `PR57/T-7601` for the least-root corollary; the set identity is proved here  
Scope: finite collections of fixed prefix-correct ordinary architectures, with no cross-architecture transitions  
Related counterexample candidates: none

## Statement

Fix a positive integer `r`. For each architecture index

\[
i\in\{1,\ldots,r\},
\]

let

\[
S^{(i)}_0\supseteq S^{(i)}_1\supseteq S^{(i)}_2\supseteq\cdots
\]

be its nested sets of positive ordinary seeds surviving the first `n` gates. Put

\[
U_n=\bigcup_{i=1}^r S^{(i)}_n.
\]

Then

\[
\boxed{
\bigcap_{n\ge0}U_n
=
\bigcup_{i=1}^r\bigcap_{n\ge0}S^{(i)}_n.}
\tag{1}
\]

Thus a finite portfolio of fixed architectures has an ordinary all-time survivor if and only if at least one constituent architecture already has an ordinary all-time survivor.

For the quantitative form, define

\[
m^{(i)}_n=\min S^{(i)}_n
\]

when the set is nonempty and `m^(i)_n=+infinity` otherwise, and put

\[
u_n=\min_{1\le i\le r}m^{(i)}_n.
\]

Assume every `U_n` is nonempty. Then the following are equivalent:

1. `(u_n)` is bounded;
2. some constituent least-root sequence `(m^(i)_n)` is bounded;
3. some constituent architecture has an ordinary all-time survivor;
4. the finite portfolio has an ordinary all-time survivor.

Consequently, if every constituent satisfies

\[
m^{(i)}_n\longrightarrow\infty,
\]

then

\[
u_n\longrightarrow\infty
\]

and the entire finite portfolio is ordinarily empty.

## Definitions

A **fixed architecture** has its own persistent transition rules and its own nested survivor tower. Equation `(1)` does not cover a machine that switches transition rules between architectures during one orbit. Such switching defines a new architecture, whose complete prefix sets must be analyzed directly.

A **portfolio** means only that a seed is accepted when it belongs to at least one constituent architecture at every depth.

## Motivation

Several repository lanes now expose exact ordinary machines. A tempting response to the extraction failure is to retain finitely many of them and hope that the choice of architecture can vary with depth. The theorem proves that this does not work: finite choice plus nesting forces one architecture to recur cofinally and therefore to carry the whole seed.

This is a global project-management consequence, not another encoding. Combining PR #45, PR #49, PR #51, and H as four disconnected alternatives cannot create an ordinary root absent from all four. A genuine cross-machine construction must contain exact physical switching edges and is mathematically a new architecture.

## Proof

The inclusion from right to left in `(1)` is immediate.

For the converse, let

\[
x\in\bigcap_{n\ge0}U_n.
\]

For every `n`, choose an index `i_n` with

\[
x\in S^{(i_n)}_n.
\]

Only finitely many indices are available, so one index `i` occurs for infinitely many values of `n`. Fix any depth `N`. Choose an occurrence `n>=N` with `i_n=i`. By nesting,

\[
x\in S^{(i)}_n\subseteq S^{(i)}_N.
\]

Because `N` was arbitrary,

\[
x\in\bigcap_{N\ge0}S^{(i)}_N.
\]

This proves `(1)`.

Now assume `(u_n)` is bounded by `B`. For each `n`, choose `i_n` with

\[
m^{(i_n)}_n=u_n\le B.
\]

Again one index `i` occurs infinitely often. The sequence `(m^(i)_n)` is nondecreasing in the extended order because the sets are nested. Since it is at most `B` at arbitrarily large indices, it is at most `B` at every index. Hence it is bounded, and `T-7601` gives an ordinary all-time survivor in architecture `i`.

The converse implications are immediate. If every constituent minimum tends to infinity, then for every bound `B` and every `i` there is a depth after which `m^(i)_n>B`. Taking the maximum of these finitely many depths gives `u_n>B` thereafter, so `u_n` tends to infinity. ∎

## Dependency audit

- The finite-union identity `(1)` is self-contained.
- The equivalence between bounded constituent minima and an ordinary survivor uses `T-7601`.
- No property of Collatz beyond prefix nesting is used.

## Gap audit

- Finiteness is essential. For countably many architectures, let `S^(i)_n={1}` when `n<=i` and empty otherwise. Then every union `U_n` contains `1`, but no fixed constituent contains `1` at all depths.
- Cross-switching transitions are not a portfolio and are not excluded.
- The theorem does not decide any constituent least-root sequence.
- A finite union may simplify computation, but it supplies no new compactness principle.
- The result applies only when every depth refers to the same initial ordinary seed.

## Adversarial tests

1. If one architecture contains seed `7` at every depth, both sides of `(1)` contain `7`.
2. If two architectures alternate which one has the smaller finite-depth minimum but both minima tend to infinity, the portfolio minimum still tends to infinity.
3. The countable counterexample above confirms why the pigeonhole step requires a finite portfolio.
4. A machine with actual edges from one chart to another must be encoded as one new nested survivor tower and is not silently eliminated.

## Remaining uncertainty

None in the theorem. The only substantive question is whether a proposed synthesis is merely a finite portfolio or supplies genuine physical cross-transitions.

## Suggested next attack

For the current finite collection of refund machines, either decide one constituent least-root sequence or build and prove exact cross-machine transition blocks. Merely retaining several unresolved machines in parallel does not advance ordinary extraction.