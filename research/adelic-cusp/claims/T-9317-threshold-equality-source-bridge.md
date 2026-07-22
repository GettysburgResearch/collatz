# T-9317 — Threshold/equality source bridge for centered rational powers

**Claim ID:** T-9317  
**Title:** A sharp nearest-integer lower bound at the critical radius closes the ordinary section even in the Thue--Morse equality case  
**Status:** PROPOSED / CONDITIONAL  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `T-9315`, `T-9316`  
**Scope:** exact source-to-native interface for Dubickas-type nearest-integer theorems  
**Related counterexample candidates:** none

## 1. Native critical radius

Put

\[
\beta=\frac{81}{64},
\qquad
r_*=\frac1{81}.
\tag{1}
\]

By `T-9315`, the nontrivial ordinary section is nonempty exactly when there is a real number `xi>0` such that

\[
\left\|\xi\beta^n\right\|
\le r_*
\qquad(n\ge0).
\tag{2}
\]

Every positive orbit satisfying `(2)` actually lies strictly inside the strip at every finite time, but its limit superior may equal `r_*`.

## 2. Abstract source hypotheses

Let `rho` be a nonnegative constant. Suppose an external nearest-integer theorem supplies:

### Lower-bound hypothesis

For every `xi>0` in the theorem's stated scope,

\[
\boxed{
\limsup_{n\to\infty}
\left\|\xi\beta^n\right\|
\ge\rho.
}
\tag{3}
\]

### Equality-language hypothesis

If

\[
\limsup_{n\to\infty}
\left\|\xi\beta^n\right\|
=\rho
\tag{4}
\]

and all powers remain in the corresponding closed extremal strip, then the sign itinerary of the nearest-integer errors belongs to a class `E_rho`.

Assume every itinerary in `E_rho` satisfies the efficient-recurrence condition of `T-9316`:

\[
\ell_j-\delta t_j\longrightarrow+\infty,
\qquad
\delta=\log_{64}(81/64),
\tag{5}
\]

for some sequence of equal factors.

## 3. Conditional closure theorem

Under the hypotheses above, either of the following is sufficient to exclude the nontrivial ordinary section:

1. 
   \[
   \boxed{\rho>1/81;}
   \tag{6}
   \]
2. 
   \[
   \boxed{
   \rho=1/81
   \quad\text{and the equality-language hypothesis holds.}
   }
   \tag{7}
   \]

### Proof

Suppose a nontrivial ordinary survivor exists. By `T-9315`, it gives `xi>0` satisfying `(2)`. Hence

\[
\limsup_n\|\xi\beta^n\|
\le1/81.
\tag{8}
\]

If `(6)` holds, equations `(3)` and `(8)` contradict one another.

If `(7)` holds, `(3)` and `(8)` force equality:

\[
\limsup_n\|\xi\beta^n\|=1/81.
\tag{9}
\]

The equality-language hypothesis places the sign itinerary in `E_rho`. Condition `(5)` and `T-9316` then exclude an ordinary positive lift, again a contradiction. QED.

## 4. Thue--Morse specialization

A particularly useful equality classification is

\[
\mathcal E_\rho
\subseteq
\left\{
\sigma^s\tau,
\sigma^s\overline\tau:
 s\ge0
\right\},
\tag{10}
\]

where `tau` is the Thue--Morse word.

`T-9316` proves that every itinerary in `(10)` has infinitely many nonzero appended nearest-integer blocks. Therefore an exact source theorem with lower constant

\[
\boxed{\rho\ge1/81}
\tag{11}
\]

would be enough provided its equality classification is `(10)` or any broader class satisfying efficient recurrence.

This sharpens the wave-5 literature task. A strict lower bound is sufficient but is not necessary: a critical equality bound plus a native recurrence obstruction also closes the ordinary section.

## 5. Quantitative deficit when the source constant is smaller

If the exact specialization gives

\[
\rho<1/81,
\tag{12}
\]

then the external theorem alone leaves the explicit deficit

\[
\boxed{
\Delta_{\rm src}
=
\frac1{81}-\rho>0.
}
\tag{13}
\]

The native problem is then no longer vague. One must show that arithmetic stabilization of the appended blocks improves the source lower bound by more than `Delta_src`, or that every near-extremal sign word has an efficient recurrence excluded by `T-9316`.

## 6. Exact source-acquisition checklist

Before this conditional theorem can be instantiated with Dubickas 2006 or 2008, a source audit must freeze:

1. the exact formula for `rho_(p,q)`;
2. whether `(3)` covers every nonzero real `xi`, only irrational `xi`, or another scope;
3. the precise use of `limsup`, large limit points, or two-interval containment;
4. all closed/open endpoint conventions;
5. the equality or extremal sign-word classification;
6. whether the Thue--Morse word appears as an actual equality language for `q>1`, or only for the integer-base subcase;
7. the exact translation of the source sign convention into the native digits `e_n` and blocks `q_K`.

No abstract, citation snippet, or analogy is sufficient for these obligations.

## 7. Dependency audit

- `T-9315` supplies the exact ordinary-section/centered-power equivalence.
- `T-9316` excludes every efficient-recurrence equality language, including shifted/complemented Thue--Morse.
- The threshold argument is elementary comparison of limit superiors.
- No uninspected external theorem is asserted to satisfy the hypotheses.

## 8. Gap audit

- `T-9317` is conditional: the Dubickas constants and equality cases have not yet been fully sourced and specialized in the repository.
- The 2006 abstract says the constants are explicit and Thue--Morse-related, but does not expose the formulas or prove that the rational `(81,64)` equality language is `(10)`.
- The 2008 two-interval theorem uses a different target geometry unless an exact source reduction is supplied.
- A source constant below `1/81` does not refute the centered program; it quantifies the remaining native gain.

## 9. Suggested next attack

Acquire the full 2006 and 2008 source texts. Populate the checklist in Section 6, evaluate every constant with exact rational or certified algebraic arithmetic, and then apply the trichotomy:

```text
rho > 1/81  -> immediate nonexistence;
rho = 1/81 -> equality-language audit + T-9316;
rho < 1/81 -> freeze the exact deficit and attack it through q_K.
```
