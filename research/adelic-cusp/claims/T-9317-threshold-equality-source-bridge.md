# T-9317 — Threshold/equality source bridge for centered rational powers

**Claim ID:** T-9317  
**Title:** A sharp nearest-integer lower bound at the critical radius closes the ordinary section even in a classified equality case  
**Status:** PROPOSED / CONDITIONAL  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `T-9315`, `T-9316`, `L-9315`, `L-9316`  
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

Every positive orbit satisfying `(2)` lies strictly inside the strip at every finite time, although its limit superior may equal `r_*`.

## 2. Abstract source hypotheses

Let `rho` be a nonnegative constant. Suppose an external nearest-integer theorem supplies:

### Lower-bound hypothesis

For every `xi>0` in the theorem's exact stated scope,

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

Assume every itinerary in `E_rho` is excluded from ordinary stabilization by at least one of the following native interfaces:

1. the efficient-recurrence condition of `T-9316`;
2. a bounded-distortion morphic presentation covered by `L-9315`;
3. a deterministic sequential presentation covered by `L-9316`.

The first condition can be written as

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

The equality-language hypothesis places the sign itinerary in `E_rho`, and the native classification assumption excludes an ordinary positive lift. QED.

## 4. Thue--Morse and encoded Thue--Morse specializations

Let `tau` be the Thue--Morse word.

### Literal equality language

If

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

then `T-9316` excludes every equality itinerary.

### Morphic equality language

If every equality itinerary is a finite shift of a non-erasing morphic image of `tau`, with output lengths in `[a,b]`, then `L-9315` excludes it whenever

\[
\boxed{
\frac ba
<
\frac1{2\log_{64}(81/64)}
=8.8274237885\ldots.
}
\tag{11}
\]

### Sequential equality language

If every equality itinerary is produced from a shifted/complemented Thue--Morse input by a deterministic non-erasing sequential transducer with `Q` states and output lengths in `[a,b]`, then `L-9316` excludes it whenever

\[
\boxed{
\frac ba
<
\frac1{(2Q+1)\log_{64}(81/64)}.
}
\tag{12}
\]

In particular, every deterministic letter-to-letter convention with at most eight states is excluded.

Thus an exact source theorem with lower constant

\[
\boxed{\rho\ge1/81}
\tag{13}
\]

would be enough provided its equality language is covered by one of these native classifications.

A strict lower bound is sufficient but is not necessary: a critical equality bound plus a finite symbolic presentation can also close the ordinary section.

## 5. Quantitative deficit when the source constant is smaller

If the exact specialization gives

\[
\rho<1/81,
\tag{14}
\]

then the external theorem alone leaves the explicit deficit

\[
\boxed{
\Delta_{\rm src}
=
\frac1{81}-\rho>0.
}
\tag{15}
\]

The native problem is then no longer vague. One must show that arithmetic stabilization of the appended blocks improves the source lower bound by more than `Delta_src`, or that every near-extremal sign word enters a recurrence class excluded by `T-9316`, `L-9315`, or `L-9316`.

## 6. Exact source-acquisition checklist

Before this conditional theorem can be instantiated with Dubickas 2006 or 2008, a source audit must freeze:

1. the exact formula for `rho_(p,q)`;
2. whether `(3)` covers every nonzero real `xi`, only irrational `xi`, or another scope;
3. the precise use of `limsup`, large limit points, or two-interval containment;
4. all closed/open endpoint conventions;
5. the equality or extremal sign-word classification;
6. whether Thue--Morse appears as an actual equality language for `q>1`, or only in the integer-base subcase or constant formula;
7. whether the source convention is a coding, a morphism, a sequential transducer, or a more general relation;
8. the exact translation into native digits `e_n`, terminal states `C_K`, and blocks `q_K`.

No abstract, citation snippet, or analogy is sufficient for these obligations.

## 7. Dependency audit

- `T-9315` supplies the exact ordinary-section/centered-power equivalence.
- `T-9316` excludes literal efficient-recurrence equality languages.
- `L-9315` and `L-9316` transfer that exclusion through bounded morphic and sequential presentations.
- The threshold argument is elementary comparison of limit superiors.
- No uninspected external theorem is asserted to satisfy the hypotheses.

## 8. Gap audit

- `T-9317` is conditional: the Dubickas constants and equality cases have not yet been fully sourced and specialized in the repository.
- The 2006 abstract says the constants are explicit and Thue--Morse-related, but does not expose the formulas or prove that the rational `(81,64)` equality language has any presentation covered above.
- The 2008 two-interval theorem uses a different target geometry unless an exact source reduction is supplied.
- A source constant below `1/81` does not refute the centered program; it quantifies the remaining native gain.

## 9. Suggested next attack

Acquire the full 2006 and 2008 source texts. Populate the checklist in Section 6, evaluate every constant with exact rational or certified algebraic arithmetic, and then apply:

```text
rho > 1/81
  -> immediate nonexistence;

rho = 1/81
  -> equality-language presentation
     -> T-9316 / L-9315 / L-9316;

rho < 1/81
  -> freeze the exact deficit
     -> attack it through q_K or a shifted-tail determinant.
```
