# T-9608 — A 1,024-block mechanical repair full shift has no positive cycle

**Claim ID:** `T-9608`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-26  
**Dependencies:** `L-8402`, `L-9608`; exact base-library audit `X-9612`  
**Scope:** every finite word over one explicit 1,024-block equal-summary repair alphabet, at every repetition length  
**Related counterexample candidates:** none

## 1. Primitive mechanical base block

Take the lower mechanical valuation word of slope `19/30`:

```text
w = 1 2 1 2 2 1 2 2 1 2 1 2 2 1 2
    2 1 2 2 1 2 1 2 2 1 2 2 1 2 2.
```

It has

\[
k=30,
\qquad
A=49,
\qquad
P=3^{30}=205891132094649,
\qquad
Q=2^{49}=562949953421312,
\tag{1}
\]

and positive-drift block denominator

\[
\boxed{
D=Q-P=357058821326663.}
\tag{2}
\]

Its affine numerator is

\[
C_w=2542081306853405.
\tag{3}
\]

## 2. Ten independent fixed-boundary swaps

Use the ten pairwise disjoint adjacent positions

```text
0, 2, 4, 7, 9, 12, 15, 18, 20, 23
```

with zero-based indexing. At each selected position, independently exchange the two unequal adjacent valuations.

By the exact adjacent-swap formula of `L-8402`, the signed numerator changes are

```text
 +45,753,584,909,922
 +40,669,853,253,264
 -36,150,980,669,568
 -42,845,606,719,488
 -38,084,983,750,656
 -45,137,758,519,296
 -53,496,602,689,536
 -63,403,380,965,376
 -56,358,560,858,112
 -66,795,331,387,392.
```

Disjointness makes the corrections additive. Hence the `2^10=1024` replacement combinations form one equal-summary block alphabet

\[
\mathcal L=\{B_0,\ldots,B_{1023}\}
\tag{4}
\]

with pairwise distinct constants.

The exact diameter is

\[
\begin{aligned}
W
&=\sum_{j=1}^{10}|\Delta_j|\\
&=488696643722610\\
&<562949953421312=Q.
\end{aligned}
\tag{5}
\]

Thus the entire 1,024-letter alphabet lies on the rigid side of `L-9608`.

The extreme constants are

\[
C_{\min}=2139808101293981,
\qquad
C_{\max}=2628504745016591.
\tag{6}
\]

## 3. Exact base audit

`X-9612` independently reconstructs all 1,024 words and constants using direct accelerated-numerator evaluation. It verifies:

```text
variants:                    1,024
pairwise distinct constants: 1,024
constant span:               488,696,643,722,610
single-block D-divisor hits: 0
```

Equivalently,

\[
D\nmid C_{B_s}
\qquad(0\le s<1024).
\tag{7}
\]

The exact variant/residue transcript has SHA-256

```text
d21492c18b71f2dbb4869357f746c3a04b44818e9f008dfaba67070494fbc95a
```

and the residues range from

```text
116,668,550,076
```

to

```text
356,882,772,173,939.
```

The finite audit is load-bearing only for the 1,024 base blocks. The all-length conclusion below is mathematical and is not extrapolated from a repetition scan.

## 4. All-repetition theorem

Let `R>=1`, and choose an arbitrary block at each aligned position:

\[
\mathbf s=(s_0,\ldots,s_{R-1})
\in\{0,\ldots,1023\}^R.
\]

The resulting accelerated word has denominator

\[
Q^R-P^R.
\]

If it satisfied the full cycle divisibility condition, `L-9608` and `(5)` would force

\[
C_{B_{s_0}}=\cdots=C_{B_{s_{R-1}}}.
\]

The constants are pairwise distinct, so

\[
s_0=\cdots=s_{R-1}=s
\]

for one base variant `B_s`. Its composite numerator is then

\[
C_{B_s}\frac{Q^R-P^R}{Q-P}.
\]

Therefore

\[
Q^R-P^R
\mid
C_{B_s}\frac{Q^R-P^R}{Q-P}
\quad\Longleftrightarrow\quad
Q-P\mid C_{B_s},
\]

which is impossible by `(7)`.

Hence

\[
\boxed{
\text{no word over }\mathcal L,
\text{ of any positive block length, is a positive-cycle divisor hit.}}
\tag{8}
\]

In particular, the theorem excludes all

\[
1024^R
\]

ordered block words simultaneously for every `R>=1`.

## 5. Why this changes the compiler boundary

`T-9607` left open the possibility that a three-or-more-block equal-summary alphabet could evade the binary Christoffel all-or-none sieve. `T-9608` closes a much larger class:

```text
one primitive mechanical block
 + ten independent exact local swaps
 -> 1,024 distinct repaired blocks
 -> arbitrary full-shift concatenation
 -> every repetition length
 -> no complete denominator hit.
```

The obstruction is not a missing prime factor and not a bounded search. The entire library fits inside one dyadic numerator cell of width `Q`, so the base-`Q` carry forced by complete denominator divisibility must be identically zero. A viable equal-summary cycle circuit must therefore cross at least one of the following boundaries:

1. numerator diameter at least `2^A`;
2. scale-varying block summaries;
3. overlapping/nonaligned repairs that are not captured by one fixed block library;
4. a surviving single block that already passes the complete denominator.

## 6. Gap audit

- The theorem excludes one explicit infinite grammar, not every mechanical repair architecture.
- The ten swaps are aligned inside each length-30 block; genuinely cross-boundary or scale-varying repairs remain open.
- No positive cycle, divergent seed, or `K-####` object is produced.
- The theorem is stronger than a finite repetition census but does not resolve arbitrary numerator-diameter-at-least-`Q` libraries.