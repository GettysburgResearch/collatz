# Dubickas `(81,64)` specialization pre-audit

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Date:** 2026-07-22  
**Status:** SOURCE FORMULA UNVERIFIED / conditional exact evaluation  
**Related native claims:** `T-9316`, `T-9317`, `Q-9303`

## 1. Why this file is a pre-audit

The wave-5 literature review correctly requests the full 2006 and 2008 Dubickas formulas, specialized at

```text
p=81,
q=64,
critical centered radius=1/81.
```

The repository currently has:

- the verified bibliographic records and abstracts;
- the statement that the 2006 constants are explicit in `p,q` and Thue--Morse-related;
- the reported `3/2` large-limit endpoint `0.238117...`;
- a secondary-source quotation of the integer-base Thue--Morse function.

It does **not** yet have the full 2006 theorem text or its exact rational-base equality classification. Therefore no formula below is imported as a theorem.

## 2. Candidate Thue--Morse normalization

Define

\[
\boxed{
P(x)=\prod_{j\ge0}(1-x^{2^j})
}
\tag{1}
\]

and

\[
\boxed{
E(x)=\frac{1-(1-x)P(x)}{2x}.
}
\tag{2}
\]

For an integer base `a`, a later primary-source discussion quotes Dubickas's extremal lower constant as

\[
\frac1aE(1/a).
\tag{3}
\]

Moreover, the published `3/2` decimal is numerically

\[
\frac13E(2/3)
=
0.2381175584\ldots,
\tag{4}
\]

matching the abstract's endpoint `0.238117...`.

These two checks strongly suggest the candidate rational normalization

\[
\boxed{
\rho_{p,q}^{\rm cand}
=
\frac1pE(q/p).
}
\tag{5}
\]

They do not prove that `(5)` is the exact theorem statement for every rational `p/q`, nor that its extremal word classification extends from `q=1` to `q>1`.

## 3. Conditional exact evaluation at `(81,64)`

Set

\[
x=64/81.
\tag{6}
\]

If `(5)` is the source constant, then

\[
\rho_{81,64}^{\rm cand}
=
\frac1{81}E(64/81).
\tag{7}
\]

A seven-factor product, with an exact geometric bound on the omitted factors, gives the certified interval

\[
\boxed{
0.6275202709455016010
<
E(64/81)
<
0.6275202709455020263.
}
\tag{8}
\]

Consequently,

\[
\boxed{
0.00774716383883335309
<
\rho_{81,64}^{\rm cand}
<
0.00774716383883335835.
}
\tag{9}
\]

The native critical radius is

\[
1/81=0.012345679012345679\ldots,
\tag{10}
\]

so the conditional deficit is

\[
\boxed{
0.00459851517351232066
<
\frac1{81}-\rho_{81,64}^{\rm cand}
<
0.00459851517351232592.
}
\tag{11}
\]

Thus, if `(5)` is indeed the 2006 large-limit constant, its strict inequality alone cannot close the ordinary section.

## 4. Exact certification of `(8)`

Let

\[
P_7(x)=\prod_{j=0}^{6}(1-x^{2^j}),
\qquad
y=x^{128}.
\tag{12}
\]

For `0<x<1`,

\[
\sum_{j\ge7}x^{2^j}
\le
\frac{y}{1-y}.
\tag{13}
\]

The elementary product inequality

\[
\prod_i(1-a_i)
\ge
1-\sum_i a_i
\tag{14}
\]

for nonnegative `a_i` gives

\[
P_7(x)
\left(1-\frac{y}{1-y}\right)
\le
P(x)
\le
P_7(x).
\tag{15}
\]

Substituting the two exact rational endpoints of `(15)` into `(2)` gives `(8)`--`(11)`. No floating-point inference is needed; the decimals are outward renderings of exact fractions.

A much coarser comparison already proves the direction. Since `P(x)>0` and `x=64/81>1/2`,

\[
E(x)<\frac1{2x}=\frac{81}{128}<1,
\tag{16}
\]

so the candidate constant in `(7)` is strictly below `1/81`.

## 5. Consequence for the proof strategy

If the full source confirms `(5)`, the trichotomy in `T-9317` lands in the third case:

```text
rho_(81,64) < 1/81.
```

The external large-limit theorem would quantify the baseline but would not prove nonexistence.

The remaining native task would be to recover the deficit `(11)` from arithmetic stabilization. Plausible ways are:

1. prove that an eventual-zero appended block tail cannot remain near the source extremal language;
2. show every near-extremal source word has efficient repeated factors and apply `T-9316`;
3. use two or more shifted tails to build an adelic determinant whose gain is absent from the one-orbit source bound;
4. exploit the 2008 two-interval geometry rather than only the scalar large-limit constant.

## 6. Thue--Morse equality bridge

Even though the likely scalar constant is subcritical, `T-9316` remains useful.

If a sharper scheduled/two-interval theorem reaches the native threshold and identifies a shifted or complemented Thue--Morse equality word, that equality path cannot stabilize:

\[
\boxed{
q_K\ne0
\quad\text{for infinitely many }K.
}
\tag{17}
\]

Thus source equality classification must be retained, not discarded after extracting one number.

## 7. Acquisition checklist

Before replacing `rho_cand` by a verified source constant, obtain and record:

1. the full 2006 theorem statement and notation;
2. the exact formulas for both large and small limit constants;
3. whether `(5)` is exact for `q>1`;
4. the quantifier on `xi` and any rational/irrational exceptions;
5. the exact equality/best-possible statement;
6. the Thue--Morse sign convention;
7. the full 2008 two-interval inequalities for general `p,q`;
8. a source-to-native translation into `e_n`, `C_K`, and `q_K`.

Until then, this file is a conditional calculation, not a theorem import.

## 8. Status boundary

- Equations `(8)`--`(16)` are exact conditional arithmetic once `(5)` is assumed.
- Formula `(5)` is not marked verified from the full 2006 source.
- No Dubickas theorem is claimed to close the ordinary section.
- No positive centered parameter, ordinary survivor, or Collatz resolution is claimed.
