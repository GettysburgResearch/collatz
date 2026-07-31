# L-6504 — Every ordinary Lane-A orbit has a zero-rate two-boundary cusp subsequence

**Claim ID:** `L-6504`  
**Status:** `PROPOSED / SOURCE-DEPENDENT`  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Dependencies:** `T-6506`; elementary parity-cylinder source/end duality  
**Scope:** positive ordinary nonperiodic all-prefix-supercritical trajectories  
**Related candidates:** none

## 1. Canonical source and endpoint representatives

For a parity word `w` of length `k` and weight `q`, write

\[
2^k T^k(x)=3^q x+A_w.
\tag{1}
\]

The word selects:

- one canonical positive source representative
  \[
  r(w)\in\{1,\ldots,2^k\};
  \]
- one canonical positive endpoint representative
  \[
  s(w)\in\{1,\ldots,3^q\}.
  \]

Every ordinary lift has the exact paired form

\[
\boxed{
 x=r(w)+2^k t,
 \qquad
 T^k(x)=s(w)+3^q t,
}
\tag{2}
\]

with the same integer `t` after the canonical conventions are aligned.

## 2. Statement

Let `n` be a positive ordinary integer with an infinite nonperiodic orbit, and assume

\[
D_k=q_k-\alpha k\ge0
\qquad(k\ge1),
\qquad
\alpha={\log2\over\log3}.
\tag{3}
\]

Then there is a sequence `k_j -> infinity` such that, for the actual prefix word `w_j`,

\[
\boxed{D_{k_j}=o(k_j),}
\tag{4}
\]

\[
\boxed{r(w_j)=n,}
\tag{5}
\]

\[
\boxed{s(w_j)=T^{k_j}(n),}
\tag{6}
\]

and both canonical boundary heights have zero exponential rate:

\[
\boxed{
{\log r(w_j)\over k_j}\longrightarrow0,
\qquad
{\log s(w_j)\over q_{k_j}}\longrightarrow0.}
\tag{7}
\]

Equivalently,

\[
r(w_j)=\exp(o(k_j)),
\qquad
s(w_j)=\exp(o(q_{k_j})).
\tag{8}
\]

Thus a hypothetical ordinary Lane-A orbit occupies the simultaneous zero-rate corner of the exact `2`-adic source / `3`-adic endpoint rectangle.

## 3. Proof

`T-6506` supplies a sequence `k_j` with `(4)` and

\[
\log T^{k_j}(n)=o(k_j).
\tag{9}
\]

For every sufficiently large `j`,

\[
2^{k_j}>n.
\]

The actual integer `n` lies in the source cylinder of `w_j`, and its least positive residue modulo `2^(k_j)` is therefore exactly `n`. This proves `(5)`.

Also

\[
q_{k_j}=\alpha k_j+D_{k_j}
=\alpha k_j+o(k_j),
\tag{10}
\]

so

\[
3^{q_{k_j}}=\exp((\log2)k_j+o(k_j)).
\]

Equation `(9)` implies

\[
T^{k_j}(n)<3^{q_{k_j}}
\]

for all sufficiently large `j`. The actual endpoint is in the endpoint residue class selected by `w_j`; being positive and smaller than the endpoint modulus, it is the canonical representative. This proves `(6)`.

The first limit in `(7)` is immediate from `(5)`. The second follows from `(6)`, `(9)`, and `(10)`.

## 4. Exact interpretation

For a generic symbolic word, either canonical boundary may occupy a positive fraction of its ambient modulus. An ordinary Lane-A orbit forces both to collapse simultaneously along a subsequence:

```text
source modulus:   2^k,
source height:    fixed n;

endpoint modulus: 3^q,
endpoint height:  exp(o(k)).
```

The source collapse is ordinary stabilization. The endpoint collapse is a consequence of the source-qualified critical-density theorem plus the exact polynomial correction product.

## 5. Relation to the latest exponent-code literature

Kramer's 2026 exponent-code framework records a `2`-adic start rate, a `3`-adic endpoint rate, and real drift. Its theorem that a fixed positive integer has asymptotically vanishing canonical residue rates is consistent with `(7)`.

The present lemma identifies the precise all-prefix-supercritical subsequence on which both rates vanish while the real drift remains nonnegative.

Kramer's finite experiments report positive tradeoff rates for searched critical codes, but no theorem there excludes the zero-rate corner. This file does not promote the diagnostic to a proof.

## 6. Gap audit

- No lower bound preventing simultaneous zero boundary rates is currently proved.
- Counting or entropy alone cannot exclude one nested ordinary path.
- A `2`-adic completion with small finite representatives at each isolated depth is not automatically one fixed ordinary source; equation `(5)` is the load-bearing ordinary fact here.
- The theorem does not prove that the endpoint values remain small at every time, only on a subsequence.

## 7. Exact closing target

A theorem of the following form would eliminate Lane A:

> There exists `epsilon>0` such that every sufficiently long all-prefix-supercritical parity word satisfies
> \[
> \max\left\{
> {\log r(w)\over k},
> {\log s(w)\over q(w)}
> \right\}\ge\epsilon.
> \]

Even a weaker lower bound tending to zero more slowly than the rates in `(7)` could suffice.

No such canonical-boundary uncertainty theorem is presently established in the repository or in the inspected literature.
