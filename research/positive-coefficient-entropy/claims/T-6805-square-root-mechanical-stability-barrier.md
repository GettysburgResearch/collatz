# T-6805 — Any infinite noncyclic CST obstruction must leave the mechanical extremizer by at least square-root scale

**Claim ID:** `T-6805`  
**Status:** **PROPOSED / SOURCE-QUALIFIED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6806`, `T-6803`  
**Scope:** sequences of coefficient-first-crossing words

## 1. Statement

Let `w_j` be coefficient-first-crossing words of lengths `j->infinity`. Let `u_j` be their upper mechanical reference words and let

\[
K_j=K(w_j)
\]

be the exact adjacent-swap area from `L-6806`.

Assume:

1. the canonical orbit of each `w_j` contains no repeated state;
2. each canonical member is non-descending at the first coefficient crossing:
   \[
   s_{w_j}\ge r_{w_j};
   \]
3. the standard effective two-logarithm lower bound used in `T-6803`.

Then

\[
\boxed{K_j\ne o(\sqrt j).}
\tag{1}
\]

Equivalently, there is no infinite family of noncyclic CST obstructions whose swap area from the maximum-remainder mechanical word is sub-square-root.

## 2. Proof

Suppose for contradiction that

\[
K_j=o(\sqrt j).
\tag{2}
\]

Choose

\[
L_j=\lfloor\sqrt j\rfloor.
\tag{3}
\]

By `L-6806`,

\[
B_{w_j}<1+K_j=o(L_j),
\tag{4}
\]

and

\[
p_{w_j}(L_j)
\le
L_j+1+2K_jL_j.
\tag{5}
\]

Equation `(2)` gives

\[
K_jL_j=o(j),
\]

so `(5)` implies

\[
p_{w_j}(L_j)=o(j).
\tag{6}
\]

There are `j-L_j` factor starting positions in the proper prefix. Hence

\[
M_{w_j}(L_j)
=
\left\lceil
\frac{j-L_j}{p_{w_j}(L_j)}
\right\rceil
\longrightarrow\infty,
\tag{7}
\]

and in particular `M_{w_j}(L_j)>=2` eventually.

Also

\[
L_j/\log j\to\infty.
\tag{8}
\]

Thus the hypotheses `(13)`–`(15)` of `T-6803` hold. Since the canonical orbit has no repeated state, `T-6803` yields

\[
s_{w_j}<r_{w_j}
\]

for all sufficiently large `j`, contradicting assumption 2. This proves `(1)`. ∎

## 3. Interpretation

The maximum affine remainder is attained by the upper mechanical word. A hypothetical late first-crossing paradoxical word cannot be a small combinatorial repair of that extremizer.

It must accumulate at least square-root-scale prefix displacement in the precise sense that the total area

\[
K_j
=
\sum_{m<j}
\bigl(S_m-\lceil\alpha m\rceil\bigr)
\]

cannot be `o(sqrt(j))`.

This is stronger than saying that the word is not literally mechanical or Sturmian. It excludes every perturbation obtainable by a sub-square-root number of rightward adjacent repairs, even though the ambient word length tends to infinity.

## 4. Connection to the remaining stability theorem

`L-6806` gives the exact endpoint gain of one repair:

\[
\frac{3^t}{2^{h+2}}.
\]

To close the complete first-crossing lane, one would like the opposite estimate:

```text
retaining enough affine remainder to avoid descent
    -> K_j is small.
```

`T-6805` proves that every actual infinite obstruction must violate such a small-repair conclusion at least at square-root scale. A successful stability theorem must therefore either:

- force `K_j=o(sqrt(j))`, yielding an immediate contradiction; or
- control much rougher perturbations by a stronger factor/source argument.

## 5. Repeated-state alternative

If the canonical orbit repeats a state, determinism creates a positive periodic orbit. That is not treated as a harmless proof exception: it is a nontrivial positive-cycle certificate unless the repeated orbit is the trivial `1 <-> 2` cycle.

Thus the complete conclusion is:

\[
\boxed{
\begin{array}{c}
\text{an infinite family of first-crossing non-descent words}\
\text{with }K_j=o(\sqrt j)
\end{array}
\Longrightarrow
\text{a positive cycle occurs in one canonical prefix}.}
\tag{9}
\]

Subject to independent review and the imported two-logarithm bound, low-swap aperiodic obstructions are excluded.

## 6. Gap audit

- The theorem does not prove a uniform numerical lower bound `K_j>=c sqrt(j)`.
- Families with `K_j` comparable to or larger than `sqrt(j)` remain open.
- The two-logarithm source dependence is inherited from `T-6803`.
- A positive-cycle alternative must be handled by the separate cycle funnel.
- No proof of CST or Collatz is claimed.