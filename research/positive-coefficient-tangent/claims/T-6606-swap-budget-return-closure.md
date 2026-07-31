# T-6606 — a mechanical swap budget forces a long repeated factor

**Claim ID:** `T-6606`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** `T-6604`, `T-6605`; elementary finite-word counting  
**Scope:** finite first-coefficient-crossing words  

## 1. Finite-word recurrence lemma

Let `w=w(j)` be the upper mechanical first-crossing extremizer from `T-6605`, and let `v` be any first-crossing word of the same length and weight.

Put

\[
I=\mathcal I(v),
\]

the exact monotone adjacent-swap distance from `v` to `w`.

For every factor length `1<=L<=j`, let `p_v(L)` be the number of distinct length-`L` factors occurring in `v`. Then

\[
\boxed{
p_v(L)\le L+2+2IL.}
\tag{1}
\]

Consequently, if

\[
\boxed{2L(I+1)<j-1,}
\tag{2}
\]

then some length-`L` factor occurs at least twice in `v`.

## 2. Proof of the complexity bound

The first `j-1` symbols of `w` are a prefix of one Sturmian upper-mechanical word. Hence every length-`L` factor of `w` not meeting its forced final zero belongs to a Sturmian language and contributes at most `L+1` possibilities. There is at most one additional factor meeting the final position. Therefore

\[
\boxed{p_w(L)\le L+2.}
\tag{3}
\]

A sequence of `I` adjacent swaps changes two symbols per swap. Thus the Hamming distance between `v` and `w` is at most

\[
H(v,w)\le2I.
\tag{4}
\]

A mismatch position belongs to at most `L` length-`L` windows. Therefore at most `HL<=2IL` starting windows of `v` meet a mismatch. Every other factor occurrence is identical to the corresponding factor of `w`.

The clean factors contribute at most `p_w(L)<=L+2` distinct words, while the exceptional windows contribute at most `2IL` further distinct words. This proves `(1)`.

The word `v` has `j-L+1` factor starts. If `(2)` holds, then

\[
j-L+1>L+2+2IL\ge p_v(L),
\]

so two starts carry the same factor. ∎

## 3. Canonical length extracted from the swap budget

Define

\[
\boxed{
L_*(j,I)
=
\left\lfloor{j-2\over2(I+1)}\right\rfloor.}
\tag{5}
\]

Whenever `L_*>=1`, condition `(2)` holds with `L=L_*`. Thus every first-crossing word at swap distance `I` contains a repeated factor of length at least

\[
{j-2\over2(I+1)}-1.
\]

In particular:

```text
I=O(1)       -> a repeated factor of linear size;
I=o(j)       -> a repeated factor whose length tends to infinity;
I=j^theta    -> a repeated factor of order j^(1-theta), for theta<1.
```

## 4. Closed exact certificate with `T-6604/T-6605`

Use the notation of `T-6605`. Suppose a positive ordinary integer `n` follows `v` and does not descend at its first coefficient crossing.

Put

\[
C={3^q\over2^j},
\qquad
B=B(v),
\qquad
\mathfrak M=E(w)-n(1-C)\ge0.
\tag{6}
\]

`T-6605` gives

\[
I
\le
{4\,3^B\over C}\mathfrak M.
\]

Define the integer budget

\[
\boxed{
K
=
\left\lfloor
{4\,3^B\over C}\mathfrak M
\right\rfloor,}
\tag{7}
\]

and the forced return length

\[
\boxed{
L_K
=
\left\lfloor{j-2\over2(K+1)}\right\rfloor.}
\tag{8}
\]

Then `I<=K`, so if `L_K>=1`, the word `v` contains a repeated factor of length `L_K`.

If the two physical states at those occurrences are distinct, `T-6604` forces

\[
\boxed{
2^{L_K}+1
<
3^B\left({j\over\lambda}+{j\over2}\right),
\qquad
\lambda=j\log2-q\log3.}
\tag{9}
\]

Therefore the reverse inequality

\[
\boxed{
2^{L_K}+1
\ge
3^B\left({j\over\lambda}+{j\over2}\right)}
\tag{10}
\]

is a complete exact contradiction unless the segment already contains a repeated physical state and hence a positive cycle.

No asymptotic theorem or Baker constant is needed for `(10)`.

## 5. Canonical first-crossing decision rule

For a first-crossing word `v`, take

\[
n=r^+(v),
\]

the least positive parity-cylinder representative. Compute exactly:

1. its endpoint `y^+(v)`;
2. the proper-prefix bank `B(v)`;
3. the mechanical remainder `E(w)`;
4. the margin
   \[
   \mathfrak M=E(w)-r^+(v)(1-C);
   \]
5. `K` and `L_K` from `(7)--(8)`;
6. the two sides of `(10)` using a directed interval for `lambda`.

Then:

- if `y^+(v)<r^+(v)`, the target is already proved;
- if the margin is negative, no word of the same `(j,q)` can avoid descent;
- if `(10)` holds and no physical state repeats, the canonical target is proved;
- otherwise the word is forced into the explicitly recorded high-bank / large-swap / ultra-small-gap residual class.

This is a proof-producing consumer for the remaining delayed-crossing lane.

## 6. Asymptotic closure criterion

For a family with lengths `j_r`, suppose

\[
K_r=o\!\left(
{j_r\over
 B_r+\log(j_r/\lambda_r)}
\right).
\tag{11}
\]

Then

\[
L_{K_r}
\gg {j_r\over K_r+1},
\]

and the left side of `(9)` grows faster than its right side. Hence, outside the positive-cycle alternative, no such family can contain canonical target failures for all large `r`.

Thus a surviving non-cycle family must satisfy the quantitative lower-pressure alternative

\[
\boxed{
K_r
\not=o\!\left(
{j_r\over
 B_r+\log(j_r/\lambda_r)}
\right).}
\tag{12}
\]

In words: the mechanical remainder margin, amplified by `3^B`, must support almost linearly many swap units relative to the available recurrence scale.

## 7. What remains

The delayed-crossing blocker is now reduced to three explicit possibilities:

```text
positive physical cycle;
coefficient bank large enough to destroy the dyadic return;
mechanical swap budget large enough to make every forced return too short,
combined with an exceptionally small lambda.
```

The next analytic target is to show that a canonical first-crossing residue cannot simultaneously sustain the last two quantities.

## 8. Gap audit

- The factor-complexity estimate is deliberately coarse but exact.
- A large swap budget can make `L_K` trivial.
- Equation `(10)` needs a directed lower bound for the specific logarithmic gap.
- A repeated physical state is not discarded; it is handed to the positive-cycle/full-denominator lane.
- The theorem does not close every first crossing and does not prove Collatz.
