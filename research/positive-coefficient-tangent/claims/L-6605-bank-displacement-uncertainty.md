# L-6605 — bank–displacement uncertainty for every acyclic first-crossing failure

**Claim ID:** `L-6605`  
**Status:** **PROPOSED / SOURCE-DEPENDENT**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** `T-6604`, `T-6606`; Rhin's bound as recorded in `L-6604`  
**Scope:** every acyclic canonical first-crossing target failure  

## 1. Statement

Let `v` be a first-coefficient-crossing word of length `j`. Put

\[
I=\mathcal I(v)
\]

for its exact integrated adjacent-swap distance from the upper mechanical extremizer, and

\[
B=\max_{0\le t<j}(q_t-\alpha t),
\qquad
\alpha={\log2\over\log3}.
\]

Assume the least positive parity-cylinder representative does not descend at the crossing and the represented segment contains no repeated physical state.

Then

\[
\boxed{
B>
\alpha
\left\lfloor{j-2\over2(I+1)}\right\rfloor
-14.3\log_3j
-\log_3(3/2).}
\tag{1}
\]

In particular,

\[
\boxed{
(I+1)
\left(
B+\alpha+14.3\log_3j+\log_3(3/2)
\right)
>
{\alpha(j-2)\over2}.}
\tag{2}
\]

Equation `(2)` is the bank–displacement uncertainty principle.

## 2. Proof

`T-6606` forces a repeated factor of length

\[
L_*=\left\lfloor{j-2\over2(I+1)}\right\rfloor.
\]

By the no-cycle hypothesis, its two physical source states are distinct.

Rhin's lower bound, specialized in `L-6604`, and the return inequality of `T-6604` give

\[
2^{L_*}+1
<
3^B\left(j^{14.3}+{j\over2}\right)
\le
{3\over2}3^Bj^{14.3}.
\]

Since `2^(L_*)<2^(L_*)+1`, taking logarithms to base three gives

\[
\alpha L_*
<
B+14.3\log_3j+\log_3(3/2),
\]

which is `(1)`.

Using

\[
L_*
\ge
{j-2\over2(I+1)}-1
\]

in `(1)` and rearranging gives `(2)`. ∎

## 3. Quantitative alternatives

### Small bank forces almost-linear displacement

For any explicit upper bound `B<=b`, equation `(2)` gives

\[
\boxed{
I+1
>
{\alpha(j-2)
 \over
 2\left(b+\alpha+14.3\log_3j+\log_3(3/2)\right)}.}
\tag{3}
\]

Thus a bounded bank requires

\[
I=\Omega\!\left({j\over\log j}\right),
\]

and a bank of order `log j` still requires an almost-linear number of displacement units.

### Small displacement forces a large bank

For any explicit upper bound `I<=s`, equation `(1)` gives

\[
\boxed{
B>
\alpha
\left\lfloor{j-2\over2(s+1)}\right\rfloor
-14.3\log_3j
-\log_3(3/2).}
\tag{4}
\]

Thus fixed or polylogarithmic displacement forces a coefficient bank growing essentially linearly in `j`.

### Balanced frontier

Optimizing the two factors in `(2)` yields the square-root frontier of `T-6610/L-6604`:

\[
I,B=\Omega(\sqrt j)
\]

up to logarithmic corrections whenever neither quantity dominates the other.

## 4. Asymptotic product form

For any family with

\[
I_j=o(j/\log j),
\]

equation `(2)` gives

\[
\boxed{
\liminf_{j\to\infty}
{I_jB_j\over j}
\ge{\alpha\over2}.}
\tag{5}
\]

Indeed, the terms involving `I_j log j/j` vanish and `I_j/(I_j+1)` tends to one unless `I_j` stays bounded, which is already excluded by `(2)`.

If `I_j` is not `o(j/log j)`, then the displacement is already almost linear. Thus every surviving family satisfies one of:

```text
I_j is at least order j/log j;

or

I_j * B_j is at least (alpha/2-o(1))*j.
```

## 5. Interaction with the full-denominator window

`T-6609` shows that every target failure must hit one of fewer than `j/2` full-denominator residue levels.

`L-6605` proves that a word reaching such a level cannot be simultaneously close to mechanical and low-bank. Its displacement support and its coefficient corridor must jointly carry linear-scale information.

This rules out a broad class of sparse repair architectures even when their individual edit positions are adaptive.

## 6. Gap audit

- Large-bank, large-displacement words remain open.
- The logarithmic exponent `13.3` is inherited from the quoted Rhin theorem.
- The inequality does not control the modular distribution of the displacement numerator inside the short dangerous window.
- A repeated physical state is the positive-cycle alternative, not part of this lemma.
- No CST or Collatz proof is claimed.
