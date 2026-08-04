# Q-9303 — Centered nearest-integer cylinder nonstabilization

**Claim ID:** Q-9303  
**Title:** Can arithmetic appended blocks be forced to remain nonzero infinitely often?  
**Status:** IDEA / exact remaining ordinary-section frontier  
**Authoring agent:** `gpt56-pro-04`  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `T-9315`--`T-9317`, `L-9312`--`L-9315`, `R-9303`; wave-5 literature audit; cross-program comparison with PR #20 and PR #19  
**Scope:** exact ordinary-section nonstabilization theorem  
**Related counterexample candidates:** none

## 1. Exact setup

For a binary itinerary `e`, the unique bounded centered errors satisfy

\[
81u_n-64u_{n+1}=e_n-e_{n+1},
\qquad
|u_n|\le1/81.
\tag{1}
\]

The nearest integers must obey

\[
64B_{n+1}=81B_n+e_n-e_{n+1}.
\tag{2}
\]

A prefix through time `K` selects one residue

\[
B_0\equiv R_K\pmod{64^K},
\qquad
0\le R_K<64^K.
\tag{3}
\]

The cylinders are nested:

\[
R_{K+1}=R_K+q_K64^K,
\qquad
q_K\in\{0,\ldots,63\}.
\tag{4}
\]

The selected `2`-adic nearest integer is ordinary and nonnegative exactly when

\[
\boxed{q_K=0\text{ eventually}.}
\tag{5}
\]

By `T-9315`, a positive eventual-zero path is exactly a nontrivial ordinary centered orbit.

## 2. Decisive target

Prove

\[
\boxed{
\text{Every nontrivial binary itinerary has infinitely many }q_K\ne0.
}
\tag{6}
\]

Equivalent targets are

\[
\min(R_K\setminus\{0,1\})\longrightarrow\infty
\tag{7}
\]

and

\[
\mathcal Z^{\rm ctr}_{64,81}=\varnothing.
\tag{8}
\]

The real centered condition in `(8)` must retain the arithmetic nearest-integer cylinder. `L-9313` proves that the bounded real error language alone is the full two-shift.

## 3. Exact formulas available

The selected completion point is

\[
\boxed{
B_0^*(e)
=-\sum_{n\ge0}(e_n-e_{n+1})\frac{64^n}{81^{n+1}}
}
\tag{9}
\]

in `Z_2`, equivalently

\[
\boxed{
B_0^*(e)
=-\frac{e_0}{81}
+\frac{17}{81^2}
\sum_{n\ge0}e_{n+1}(64/81)^n.
}
\tag{10}
\]

The real error is another affine evaluation of the same coefficient word:

\[
\boxed{
u_0
=
\frac{e_0}{64}
-
\frac{17}{64\cdot81}
\sum_{n\ge0}e_n(64/81)^n.
}
\tag{11}
\]

`L-9314` gives the exact new block from the terminal nearest integer `C_K`:

\[
\boxed{
q_K
\equiv
-81^{-(K+1)}(81C_K+e_K-e_{K+1})
\pmod{64}.
}
\tag{12}
\]

At most one of the two next digits can make `q_K=0`.

## 4. First infinite family now closed

`T-9316` proves the global recurrence cone

\[
\ell<\delta t+\log_{64}A_0,
\qquad
\delta=\log_{64}(81/64),
\tag{13}
\]

for equal length-`ell` factors whose second start is `t` in an ordinary itinerary.

Therefore any itinerary with

\[
\ell_j-\delta t_j\to+\infty
\tag{14}
\]

cannot stabilize.

The Thue--Morse word has adjacent equal factors of length `2^m` with second start `2*2^m`. Since

\[
2\delta<1,
\tag{15}
\]

every finite shift or complemented shift of Thue--Morse has infinitely many nonzero blocks.

`L-9315` makes this robust under a non-erasing morphic recoding whose maximum-to-minimum output-length ratio is below

\[
\boxed{
\frac1{2\delta}=8.8274237885\ldots.
}
\tag{16}
\]

Thus all codings and every binary morphism of length distortion at most `8` remain excluded.

This directly answers one wave-5 task: a broad Thue--Morse extremal sign family is incompatible with ordinary block stabilization.

## 5. Wave-5 literature route

The literature audit identifies Dubickas 2006 and 2008 as the closest exact source family. The full formulas still require acquisition and specialization at

```text
p=81,
q=64,
radius=1/81.
```

`T-9317` freezes the source trichotomy.

Let `rho_(81,64)` be the exact source lower constant for

\[
\limsup_n\|\xi(81/64)^n\|.
\]

Then:

```text
rho > 1/81
  -> immediate ordinary-section nonexistence;

rho = 1/81
  -> inspect the equality language;
     every efficient-recurrence equality word is excluded by T-9316;
     bounded-distortion Thue--Morse recodings are covered by L-9315;

rho < 1/81
  -> freeze the exact deficit 1/81-rho
     and prove arithmetic stabilization supplies the missing gain.
```

This is stronger than requiring a strict source inequality. A critical equality theorem can close the problem once its equality sign word is classified.

The source audit must record the exact constant, quantifiers, endpoints, irrational/rational scope, sign convention, and whether Thue--Morse is an actual equality language for `q>1` rather than merely a formal expression in the constant.

## 6. Cross-program lessons

### PR #20 — q-series and direct-truncation barrier

PR #20 shows that direct rational truncations can be exactly subcritical and that stronger approximants must couple shifted values or exploit determinant cancellation.

Reusable lesson:

> expose the exact special value, freeze the direct height/error ratio, and demand a genuine reduced-height or multi-tail gain.

### PR #19 — normalized phase and mixed-sign crossings

PR #19 shows that coarse same-sign geometry may close automatically while mixed-sign crossings contain the arithmetic difficulty.

Reusable lesson:

> seek a normalized return-block phase with a one-sided invariant, not another comparison of coarse growth exponents.

### Wave 5 — fixed versus growing families

The Väänänen--Wallisser source closes fixed periodic stack families only after an exact native reduction. For the present full binary language, a fixed-family theorem is useful only after the equality or near-extremal symbolic family has been frozen.

## 7. Highest-value native routes

### A. Near-extremal recurrence theorem

Strengthen `T-9316` from exact Thue--Morse to every sign word whose centered limsup is at most `1/81`. Prove that near-critical errors force efficient repeated factors or another recurrence-cone violation.

This would convert a source constant at or below the critical value into a native contradiction.

### B. Shifted-tail determinant

Use `(9)`--`(11)` and two or more shifts. A long zero block tail gives large `2`-adic agreement with one ordinary integer; the bounded errors give small real linear forms.

Construct a determinant whose product over the real, `2`-adic, and denominator places has a net gain after exact gcd reduction.

### C. Forced-tail return word

Assume `q_K=0` for every large `K`. Equation `(12)` uniquely forces each next digit from `C_K mod64`.

Show that this forced orbit must eventually create an efficient repeated factor, a periodic/substitutional return word, or a fixed finite-term equation. Then apply `T-9316`, `L-9311`, or a proper-subsum-audited S-unit theorem.

### D. Extendible minimum operator

Define the least depth-`K` survivor admitting arbitrarily long extensions, rather than the least finite survivor. Prove its min-plus recursion has no bounded fixed ray.

## 8. Falsification criteria

A proposed proof is incomplete if it:

1. uses only the real scheduled intervals and ignores `R_K`;
2. treats a nonrational formal series as nonordinary without a value theorem;
3. uses direct truncations without beating their exact reduced height/error ratio;
4. compares complexity and carry constants without a new coupling invariant;
5. infers an ordinary integer from compatible finite cylinders without stabilization;
6. invokes Dubickas from an abstract without the exact `(81,64)` formulas and equality classification;
7. assumes every Thue--Morse-related formula means the source equality itinerary is literally the standard binary word.

## 9. Success criterion

Any one of the following closes the ordinary section:

- prove infinitely many `q_K` are nonzero for every nontrivial itinerary;
- prove `B_0^*(e)` is never an ordinary positive integer outside the trivial endpoints;
- prove the exact finite minima tend to infinity;
- prove every eventual-zero block tail forces an efficient recurrence;
- instantiate `T-9317` with a source constant/equality classification sufficient at radius `1/81`.

No stronger quantitative rate is required.
