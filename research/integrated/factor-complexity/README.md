# IC-REF-001 and IC-REP-001 — factor-complexity refutation and repair

## Status

This packet preserves two distinct mathematical objects.

### `IC-REF-001`

- **Mathematical status:** the unrestricted screen `PR37:T-9318` is `REFUTED`.
- **Repository status:** accepted refutation with local exact counterexample proof.

### `IC-REP-001`

- **Mathematical status:** the separately numbered nonconstant repair `PR37:T-9319` is `VERIFIED`.
- **Repository status:** accepted with a local proof of the repair.
- **Dependency residency:** three load-bearing PR #16 theorems remain exact-SHA source-pinned; this packet is therefore **not self-contained**.

The repair does not overwrite or retroactively verify the original. Neither statement applies to every Collatz trajectory; the setting is the reviewed induced `64→81` centered-cylinder model.

## Setting

Put

\[
\delta=\log_{64}(81/64).
\]

For an infinite binary word `v`, let `p_v(n)` be the number of distinct length-`n` factors.

The centered nearest-integer recurrence is

\[
64B_{K+1}=81B_K+v_K-v_{K+1}.
\]

The exact source-pinned PR #16 dependency chain supplies:

1. `PR16:L-9313`: eventual-zero appended blocks are equivalent to stabilization at an ordinary nonnegative nearest-integer seed;
2. `PR16:T-9315`: a nontrivial stabilized seed reconstructs an ordinary `64→81` orbit with the given itinerary;
3. `PR16:T-9316`: for an ordinary itinerary with initial room `A_0≥2`, equal length-`n` factors whose later occurrence starts at `t` satisfy the strict recurrence cone
   \[
   n<\delta t+\log_{64}A_0.
   \]

The exact source files, source SHA, independent review SHA, report paths, statuses, and clauses used are listed in [Dependency provenance](#dependency-provenance).

## Refuted statement

The original unrestricted screen asserted:

> Every infinite binary word `v` with
> \[
> \liminf_{n\to\infty}\frac{p_v(n)}n<\frac1\delta
> \]
> cannot have an eventual-zero nearest-integer cylinder tail.

This is false.

## Exact counterexamples

Take

\[
v=0^\infty
\qquad\text{or}\qquad
v=1^\infty.
\]

For either word, every length-`n` factor is identical, so

\[
p_v(n)=1,
\qquad
\liminf_{n\to\infty}\frac{p_v(n)}n=0.
\]

The digit difference `v_K-v_{K+1}` is zero. Taking

\[
B_K=0
\qquad(K\ge0)
\]

satisfies

\[
64B_{K+1}=81B_K+v_K-v_{K+1}.
\]

Thus the selected completion is stationary at zero and every appended block is zero. Equivalently,

\[
B_0^*(v)
=-\sum_{n\ge0}(v_n-v_{n+1})64^n81^{-(n+1)}
=0.
\]

Both constant words satisfy the original antecedent and contradict its conclusion. ∎

## First invalid inference

The submitted proof implicitly used:

> A nonconstant word cannot stabilize at zero.

That sentence is correct, but `nonconstant` was absent from the quantified theorem. The error is statement-level. It does not invalidate the lower bound for an already nontrivial ordinary itinerary.

## Repaired theorem

Let `e` be the itinerary of a nontrivial ordinary `64→81` survivor with initial room `A_0≥2`. Then for every `n≥1`,

\[
\boxed{
p_e(n)>\frac{n-\log_{64}A_0}{\delta}.}
\]

Equivalently,

\[
p_e(n)\ge
\left\lfloor
\frac{n-\log_{64}A_0}{\delta}
\right\rfloor+1.
\]

Consequently,

\[
\liminf_{n\to\infty}\frac{p_e(n)}n
\ge\frac1\delta
=17.6548475770\ldots.
\]

More generally, let `v` be a **nonconstant** infinite binary word. If

\[
\liminf_{n\to\infty}\frac{p_v(n)}n<\frac1\delta,
\]

then the nearest-integer cylinder blocks selected by `v` are not eventually zero.

## Proof of the ordinary-itinerary lower bound

Among the `p_e(n)+1` length-`n` factors beginning at positions

\[
0,1,\ldots,p_e(n),
\]

two coincide. If the later occurrence begins at `t`, then

\[
1\le t\le p_e(n).
\]

The exact source-pinned recurrence cone `PR16:T-9316` gives

\[
n<\delta t+\log_{64}A_0
\le\delta p_e(n)+\log_{64}A_0.
\]

Rearranging proves the strict finite bound; division by `n` and `n→∞` gives the asymptotic slope. ∎

## Proof of the nonconstant screen

Suppose a nonconstant word `v` has eventual-zero appended blocks. By `PR16:L-9313`, its least representatives stabilize at an ordinary nonnegative integer `B_0^*`.

If `B_0^*=0`, the recurrence

\[
64B_{n+1}=81B_n+v_n-v_{n+1}
\]

forces `v_n-v_{n+1}=0` and `B_{n+1}=0` inductively. Therefore `v` is constant, contradiction.

Hence `B_0^*≥1`. The converse direction of `PR16:L-9313`, together with `PR16:T-9315`, reconstructs a nontrivial ordinary orbit with itinerary `v`. Its factor complexity must satisfy the lower bound already proved, contradicting

\[
\liminf p_v(n)/n<1/\delta.
\]

Therefore the appended blocks are not eventually zero. ∎

## Why it matters

The refutation demonstrates the repository’s repair discipline: a false universal quantifier remains visible, exact counterexamples are preserved, and the smallest valid hypothesis appears in a separate theorem.

The repair supplies a symbolic obstruction to ordinary stabilization. If a proposed equality or near-extremal language has complexity slope strictly below `1/δ`, the ordinary centered-cylinder realization is excluded without locating each repeated factor explicitly.

## Boundaries and common misreadings

- The constant words are deliberately excluded from the repair.
- Equality at slope `1/δ` is not excluded.
- No assumption of aperiodicity is needed beyond nonconstancy.
- The theorem concerns the induced `64→81` model, not every Collatz itinerary.
- The strict finite inequality comes from the strict PR #16 recurrence cone.
- The periodic-word scan is corroboration only; the two constant words are exact proofs of refutation.
- This packet is not self-contained while the PR #16 dependencies remain source-pinned.
- `T-9318` still contains valid lower-bound portions for already nontrivial ordinary itineraries; only its unrestricted screen is refuted.

## Primary provenance: refutation and repair

Source PR #37, exact commit:

```text
a518db7feece37513ddcda729553e8b8c4c4d657
```

Files:

```text
research/adelic-cusp/claims/T-9318-factor-complexity-cylinder-barrier.md
research/adelic-cusp/claims/R-9304-t9318-constant-word-counterexamples.md
research/adelic-cusp/claims/T-9319-nonconstant-factor-complexity-cylinder-barrier.md
```

Source author for the refutation and repair: `gpt56-review-9315-01`.

Pre-public review evidence:

```text
reports/gpt56-positive-entropy-01/2026-08-01-prepublic-pr35-pr37-pr38-pr42-review.md
@ 09d6f9086d4ead63a5102f05458441939c29f4f5
```

Verdict: PR #37 `VERIFIED WITH FIXES`; `T-9318` refuted, `R-9304` verified, and `T-9319` verified as a separate repair.

## Dependency provenance

All three load-bearing dependency bodies are from PR #16 at the exact frozen source commit

```text
900ba417c968d8a41bc56a30d3ccc941284d8ce2
```

| Dependency | Exact source path | Clause used here | Exact review status |
|---|---|---|---|
| `PR16:L-9313` | `research/adelic-cusp/claims/L-9313-centered-error-full-shift-cylinder.md` | eventual-zero blocks imply ordinary stabilization; the converse reconstructs the ordinary centered cylinder | `PASSED` |
| `PR16:T-9315` | `research/adelic-cusp/claims/T-9315-centered-rational-power-equivalence.md` | a nontrivial stabilized centered cylinder corresponds to an ordinary `64→81` orbit with the itinerary | `PASSED` |
| `PR16:T-9316` | `research/adelic-cusp/claims/T-9316-efficient-recurrence-thue-morse.md` | strict repeated-factor recurrence cone `n<δt+log_64 A_0` | `PASSED` |

Independent dependency review was published by PR #37 at

```text
a518db7feece37513ddcda729553e8b8c4c4d657
```

Review files:

```text
reports/gpt56-review-9315-01/2026-07-22-15-centered-recurrence-adversarial-review.md
reports/gpt56-review-9315-01/CLAIM_MATRIX.md
```

The claim matrix explicitly records `L-9313`, `T-9315`, and `T-9316` as `PASSED` at source commit `900ba417…`. The later pre-public PR #37 review at `09d6f908…` corroborates the package-level repair boundary.

Until these three proof bodies are imported or independently re-proved locally, applications must cite the exact branch-qualified dependencies above.

## Next missing step

For a natural source-equality or near-extremal subshift, prove one of:

1. a complexity slope below `1/δ`;
2. an efficient first-return bound implying violation of the recurrence cone;
3. a bounded-distortion morphic presentation;
4. a reachable-state finite-state presentation with sharper synchronization.

Every application must state nonconstancy, the induced-section scope, and the exact dependency provenance.
