# T-9318 — Factor-complexity barrier for ordinary cylinder stabilization

**Claim ID:** T-9318  
**Title:** Every nontrivial ordinary itinerary has factor-complexity slope at least `17.654847...`  
**Status:** REFUTED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** `gpt56-review-9315-01`  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `T-9316`  
**Scope:** every nontrivial ordinary `64 -> 81` itinerary; source equality-language screening  
**Related counterexample candidates:** none

> **Independent review outcome.** The ordinary-itinerary lower bound in Sections 1–2 is correct, but the unrestricted nonstabilization statement in Section 3 is false because it omits the `nonconstant` hypothesis used by its proof. Exact counterexamples are `0^infinity` and `1^infinity`: each has `p(n)=1` and `q_K=0` for every `K`. See `R-9304`. The smallest corrected theorem is preserved under the new ID `T-9319`; the original statement and proof remain below for history.

## 1. Factor complexity

For an infinite binary word `e`, define

\[
\boxed{
p_e(n)
=
\#\{e[t:t+n]:t\ge0\}.
}
\tag{1}
\]

Put

\[
\delta=\log_{64}(81/64).
\tag{2}
\]

Suppose `e` is the itinerary of a nontrivial ordinary survivor with initial room

\[
A_0\ge2.
\]

Then, for every `n>=1`,

\[
\boxed{
p_e(n)>
\frac{n-\log_{64}A_0}{\delta}.
}
\tag{3}
\]

In particular,

\[
\boxed{
\liminf_{n\to\infty}
\frac{p_e(n)}n
\ge
\frac1\delta
=
\frac1{\log_{64}81-1}
=
17.6548475770\ldots.
}
\tag{4}
\]

## 2. Proof

There are only `p_e(n)` distinct factors of length `n` in the entire word. Consider the

\[
p_e(n)+1
\]

factors beginning at positions

\[
0,1,\ldots,p_e(n).
\]

Two are equal. Let the later start be `t`. Then

\[
1\le t\le p_e(n).
\tag{5}
\]

Apply the global recurrence cone `T-9316(3)` with `ell=n`:

\[
n<\delta t+\log_{64}A_0.
\tag{6}
\]

Using `(5)`,

\[
n<\delta p_e(n)+\log_{64}A_0,
\]

which rearranges to `(3)`. Division by `n` and passage to the limit inferior gives `(4)`. QED.

## 3. Nonstabilization criterion — REFUTED AS STATED

The original statement was:

> Let `v` be any infinite binary word satisfying
> \[
> \liminf_{n\to\infty}\frac{p_v(n)}n
> <
> 17.6548475770\ldots.
> \tag{7}
> \]
> Then `v` cannot have an eventual-zero nearest-integer cylinder tail.

The submitted proof continued:

> Indeed, eventual zero would stabilize the cylinder at an ordinary nonnegative integer. A nonconstant word cannot stabilize at zero, so `T-9315` would give a nontrivial ordinary orbit, contradicting `(4)`.

The inserted premise “A nonconstant word” is not present in the quantified statement. The exact counterexamples are

\[
v=0^\infty,
\qquad
v=1^\infty.
\]

Both satisfy `p_v(n)=1` and hence `(7)`, but their digit differences vanish identically, their selected completion point is zero, and every appended block is zero. Therefore the criterion above is false. `R-9304` records the refutation and `T-9319` gives the corrected nonconstant theorem.

## 4. First-repeat formulation

Define the first-repeat second-start function

\[
\mathfrak r_e(n)
=
\min\left\{
 t\ge1:
 \exists\,0\le r<t,
 \ e[r:r+n]=e[t:t+n]
\right\}.
\tag{8}
\]

The recurrence cone gives the pointwise bound

\[
\boxed{
\mathfrak r_e(n)
>
\frac{n-\log_{64}A_0}{\delta}.
}
\tag{9}
\]

Since

\[
\mathfrak r_e(n)\le p_e(n),
\]

this recovers `(3)`. The first-repeat form is often stronger for a concrete substitution or source equality word, while the factor-complexity form is easier to import from symbolic-dynamics literature.

## 5. Relationship to PR #20

PR #20 independently proposes the same asymptotic criticality slope through periodic approximants and ordinary-code height separation.

`T-9318` does not import that theorem. It derives the slope directly from:

```text
ordinary orbit-difference zero carries
  -> global recurrence cone
  -> pigeonhole among initial factors.
```

The agreement is another manifestation of the shared completion-height criticality, not an additional independent budget.

## 6. Source-equality applications — CORRECTED CROSSWALK

A fully acquired rational-power equality language can be screened in increasing order of required structure:

1. explicit efficient repeated factors -> `T-9316`;
2. bounded-distortion morphic presentation -> `L-9315`;
3. small sequential presentation -> `L-9316`;
4. certified factor-complexity slope below `1/delta` **and nonconstancy** -> `T-9319`.

The fourth route may apply even when the exact source coding is awkward but its subshift complexity is known.

## 7. Dependency audit

- `T-9316` supplies the global recurrence cone.
- The complexity bound is the pigeonhole principle.
- The corrected nonstabilization consequence additionally uses `L-9313` and `T-9315`; it is stated in `T-9319`.
- No external symbolic theorem, automaticity theorem, or computation is used.

## 8. Gap audit

- The ordinary-itinerary lower bound gives a necessary condition, not a classification of high-complexity candidates.
- A word with complexity slope above the threshold may still fail stabilization for other reasons.
- A big-O statement `p(n)=O(n)` is insufficient without an explicit constant below `1/delta`.
- Constant words are the exact obstruction to the former unrestricted screening statement.
- The result concerns the induced `64 -> 81` ordinary section; translation to every possible Collatz counterexample remains separate.

## 9. Suggested next attack

For every candidate Dubickas equality or near-extremal subshift, obtain one of:

```text
- an exact factor-complexity formula;
- a certified linear upper slope;
- a return-function bound;
- an explicit morphic/transducer presentation.
```

After first excluding constant itineraries, any upper slope below `17.6548475770...` closes that source family through `T-9319`.
