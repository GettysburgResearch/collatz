# T-8306 — The full critical Farey-tree sibling-swap grammar contains no integral cycle

Claim ID: `T-8306`  
Status: `PROPOSED / COMPUTER-ASSISTED EXACT THEOREM`  
Authoring agent: `gpt56-cycle-02`  
Created: 2026-07-23  
Dependencies: `L-8308`; exact experiment `X-8306`; paired-chart expansion `L-8304`  
Scope: every word in the recursive Farey sibling-swap grammar rooted at the lower critical mechanical run word  
Related counterexample candidates: none

## 1. Frozen critical root

Use the run fraction

\[
{p\over q}
=
{236\,838\,463\,643
 \over
 267\,629\,447\,755}
\tag{1}
\]

and the hierarchical grammar `G(p,q)` of `L-8308`. Every word has the same run counts and therefore expands through `L-8304` to an accelerated valuation word with

```text
k = 3,149,971,404,836,
A = 4,992,586,555,009,
D = 2^A-3^k > 0.
```

The fully expanded Farey parse has

```text
267,629,447,755 leaves,
267,629,447,754 internal occurrences.
```

At every internal occurrence, its two recursively repaired children may remain in Farey order or reverse. Choices at distinct occurrences are independent.

## 2. Exact ordinary decision at 314 bits

Set

\[
M=2^{314}.
\tag{2}
\]

`L-8308` gives two complete compilers.

### Modular side

The recursive affine-set compiler produces exactly

\[
\mathcal C_M
=
\{C_w\pmod M:w\in G(p,q)\}.
\tag{3}
\]

Since `D` is odd, the possible ordinary quotient classes are

\[
\mathcal Q_M
=
\{cD^{-1}\pmod M:c\in\mathcal C_M\}.
\tag{4}
\]

### Real side

The directed Farey envelope produces a rigorous interval

\[
J_{\rm Farey}
\tag{5}
\]

containing every real fixed point `C_w/D` in the grammar. Exact outward rounding certifies

\[
\boxed{
0<\inf J_{\rm Farey}
\le\sup J_{\rm Farey}<2^{314}.}
\tag{6}
\]

It also certifies that `J_Farey` contains ordinary integers, so the conclusion below is not a vacuous sign or size exclusion.

## 3. Empty intersection theorem

`X-8306` computes `(3)` and `(5)` by independent exact recursive circuits and verifies

\[
\boxed{
\mathcal Q_M
\cap
(\mathbf Z\cap J_{\rm Farey})
=\varnothing.}
\tag{7}
\]

Because every possible ordinary fixed point lies in `(5)` and must satisfy `(4)`, equation `(7)` proves

\[
\boxed{
D\nmid C_w
\quad
\text{for every }w\in G(p,q).}
\tag{8}
\]

Consequently the full hierarchical Farey sibling-swap grammar contains no positive accelerated Collatz cycle.

## 4. Proof-carrying computation

The author implementation uses memoized recursion. The verifier uses an independently constructed bottom-up Farey DAG. Both perform:

1. exact Farey-parent reconstruction from `pb-qa=1`;
2. small explicit Christoffel orientation checks;
3. exact modular set composition at `2^314`;
4. directed real translation-envelope composition;
5. the ordinary quotient intersection test `(7)`.

Replay:

```bash
python3 -B experiments/X-8306-farey-tree-grammar/run.py \
  --check-results \
  experiments/X-8306-farey-tree-grammar/results/canonical.json

python3 -B experiments/X-8306-farey-tree-grammar/verify.py \
  experiments/X-8306-farey-tree-grammar/results/canonical.json
```

## 5. Relation to earlier waves

- `O-8301` and `O-8302` rejected individual repaired words.
- `T-8303` excluded the first-80 disjoint grammar.
- `T-8304` excluded the complete canonical greedy matching with more than thirty billion independent sites.
- `T-8306` now permits recursive block reversal at every Farey scale and internal occurrence.

The obstruction remains strikingly low-coordinate: the entire ordinary quotient set is already separated from the real room modulo `2^314`.

## 6. Honest boundary

The theorem does **not** exclude:

- arbitrary permutations of the fixed run multiset;
- arbitrary fixed-weight binary run words;
- grammars that change `(A,k)` or combine neighboring critical convergents;
- general positive Collatz cycles;
- an infinite ordinary path in the negative-three/six-branch chart;
- the Collatz conjecture or its negation.

No `K-83xx` identifier is assigned.

## 7. Constructive next move

The first surviving cycle grammar must alter the low ordinary quotient digits that the fixed-shape Farey tree cannot reach. The most promising exact extensions are:

1. controlled shape changes between adjacent upper convergents;
2. block gadgets with at least seven non-2 valuations and a different first dyadic repair spectrum;
3. multi-shape quotient-target synthesis carrying `C-ND` directly.

Any exact zero residual receives immediate full valuation and shortcut-Collatz replay.
