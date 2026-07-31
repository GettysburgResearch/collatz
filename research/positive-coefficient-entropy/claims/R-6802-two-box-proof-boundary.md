# R-6802 — Proof-boundary correction for the two boxed targets

**Claim ID:** `R-6802`  
**Classification:** `METHOD / STATEMENT CORRECTION`  
**Status:** **PROPOSED** pending independent review  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31

## 1. Literal Box 2 has one trivial equality

The word

```text
10
```

is coefficient-first-crossing and has

\[
A_w=1,
\qquad
2^j-3^q=1,
\qquad
r^+(w)=1.
\]

Therefore

\[
r^+(w)=\frac{A_w}{2^j-3^q},
\]

not strict inequality. This is the trivial shortcut cycle `1 -> 2 -> 1`.

The corrected strict statement is

\[
\boxed{
r^+(w)>
\frac{A_w}{2^j-3^q}
\quad
\text{for every coefficient-first-crossing word with }r^+(w)\ge2.}
\tag{1}
\]

By `L-6803`, `(1)` is exactly

\[
\boxed{s_w<r_w.}
\tag{2}
\]

## 2. Box 2 is the coefficient-stopping-time conjecture

For the canonical source `r_w`, the first coefficient crossing occurs at time `j`. Equation `(2)` says that the actual endpoint is already below the start at precisely that time.

Thus `(1)` is not a new technical lemma left over after PR #76. It is the smallest-cylinder formulation of Terras's Coefficient Stopping Time conjecture:

```text
actual stopping time
=
coefficient stopping time
for every n>=2.
```

PR #76 proves a strong least-counterexample restriction and excludes the first forced Farey candidate. It does not prove the universal CST statement.

## 3. Box 1 is a separate global statement

Box 1 says

\[
\boxed{
\text{every positive integer has finite coefficient stopping time}.}
\tag{3}
\]

Equivalently, the nested minimum sequence

\[
m_N^{sup}
\]

escapes to infinity.

`T-6709` and the present entropy packet classify what an assumed ordinary counterexample to `(3)` must do:

- its orbit tends to `+infinity`;
- its logarithmic surplus is unbounded;
- under `T-6802`, the surplus has at least logarithmic record pressure;
- by `L-6805`, its source residue stabilizes while both normalized source and endpoint coordinates tend to the canonical corner.

None of those necessary properties contradicts ordinary existence.

## 4. The two statements are stronger than merely restating one another

The logical route is:

```text
Box 1:
    every n has some coefficient-subcritical prefix;

corrected Box 2 / CST:
    the first such prefix already descends below n;

well-ordering:
    repeated descent reaches 1.
```

Together the boxes imply Collatz. Neither current repository theorem closes either box globally.

The universal corrected Box 2 is stronger than what is strictly needed in a least-counterexample proof: it suffices to exclude first-crossing paradoxical words satisfying the full no-descent and verified-floor conditions of PR #76.

## 5. Correction to the record-growth narrative

`L-6804` proves immediately that any all-time coefficient-supercritical positive orbit satisfies

\[
X_N\ge n+N.
\]

Therefore the `N^{0.0358...}` record corollary stated in `T-6802` is not a meaningful strengthening. The genuinely new proposed content of `T-6802` is the coefficient-surplus lower bound

\[
B_N\ge(\kappa_*-o(1))\log_2N,
\]

not its weaker physical-record corollary.

No theorem body is silently rewritten by this correction.

## 6. What a real completion must prove

The exact unresolved interfaces are now:

### Supercritical lane

Show that no nested supercritical word sequence can have canonical sources eventually equal to one positive integer, even though the canonical endpoints satisfy the explicit corner estimate in `L-6805`.

### First-crossing lane

Show directly that

\[
\Delta_w=s_w-r_w<0
\]

for every nontrivial least-counterexample-admissible first-crossing word. Estimating `r_w` and `A_w/(2^j-3^q)` separately is equivalent to estimating this one displacement by `L-6803`.

## 7. Nonclaim

This correction does not prove either boxed statement or the Collatz conjecture. It prevents three false progress signals:

1. treating the trivial `10` equality as a strict theorem;
2. presenting CST itself as a nearly completed algebraic inequality;
3. presenting sublinear polynomial records as stronger than the automatic linear record floor.