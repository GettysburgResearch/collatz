# Q-9303 — Centered nearest-integer cylinder nonstabilization

**Claim ID:** Q-9303  
**Title:** Can the centered error path force infinitely many nonzero nearest-integer cylinder blocks?  
**Status:** IDEA  
**Authoring agent:** `gpt56-pro-04`  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `T-9315`, `L-9312`, `L-9313`, `R-9303`; cross-program comparison with PR #20 and PR #19  
**Scope:** exact remaining ordinary-section theorem  
**Related counterexample candidates:** none

## 1. Exact setup

For a binary itinerary `epsilon`, define the unique centered errors

\[
81u_n-64u_{n+1}
=
\varepsilon_n-\varepsilon_{n+1},
\qquad
|u_n|\le1/81.
\]

The nearest integers must satisfy

\[
64B_{n+1}
=81B_n+\varepsilon_n-\varepsilon_{n+1}.
\]

A prefix through time `K` selects one residue

\[
B_0\equiv R_K\pmod{64^K},
\qquad
0\le R_K<64^K.
\]

The cylinders are nested, so

\[
R_{K+1}=R_K+q_K64^K,
\qquad
q_K\in\{0,\ldots,63\}.
\]

The selected `2`-adic nearest integer is ordinary and nonnegative exactly when

\[
\boxed{q_K=0\text{ eventually}.}
\]

By `T-9315`, the ordinary section is nontrivial exactly when a nontrivial itinerary has this eventual-zero property with a positive starting integer.

## 2. Decisive target

Prove

\[
\boxed{
\text{Every nontrivial binary itinerary has infinitely many }q_K\ne0.
}
\]

It is enough to prove this only for itineraries compatible with the survivor chart, because arbitrary binary itineraries already define formal `2`-adic points.

## 3. Why the real schedule does not solve it

`L-9313` proves that every binary itinerary has one bounded centered-error path. Therefore:

- real interval cylinders never disappear merely because the itinerary is complicated;
- the four-phase `3/2` schedule has full symbolic support;
- entropy or total interval length cannot prove nonstabilization by itself.

The new theorem must couple the bounded real errors to the unbounded base-64 precision of `R_K`.

## 4. Exact formulas available

The selected completion point is

\[
\boxed{
B_0^*(\varepsilon)
=-\sum_{n\ge0}
(\varepsilon_n-\varepsilon_{n+1})
\frac{64^n}{81^{n+1}}
}
\]

in `Z_2`, or equivalently

\[
\boxed{
B_0^*(\varepsilon)
=-\frac{\varepsilon_0}{81}
+\frac{17}{81^2}
\sum_{n\ge0}
\varepsilon_{n+1}(64/81)^n.
}
\]

The real error coordinate is

\[
\boxed{
u_0
=
\frac{\varepsilon_0}{64}
-
\frac{17}{64\cdot81}
\sum_{n\ge0}
\varepsilon_n(64/81)^n.
}
\]

The same itinerary therefore generates two affine evaluations of one coefficient series:

1. a bounded real centered error;
2. a `2`-adic nearest-integer cylinder point.

A successful argument must exploit this shared coefficient sequence without identifying the real and `2`-adic sums.

## 5. Cross-program lessons

### PR #20 — active cylinders and partial theta

PR #20 proves that prescribed stack directives also select one `2`-adic point, ordinary exactly when appended cylinder blocks eventually vanish. It further shows that direct rational truncations have subcritical approximation exponent and develops S-adic transfer polynomials to seek stronger determinant approximants.

For the full binary ordinary-section problem, raw S-adic structure is unavailable. The reusable lesson is instead:

> expose the exact special value, freeze the direct truncation barrier, and seek a new approximant or invariant that couples several shifted values.

### PR #19 — phase and mixed-sign crossing

The H-frontier isolates a normalized phase in `[0,1)` and shows same-sign concatenations are stable; only mixed-sign crossings carry new difficulty. The centered errors here already encode sign changes exactly through `q_K`'s driving digit difference.

The reusable lesson is:

> find a normalized phase whose update under concatenation or return blocks has a one-sided invariant, rather than comparing coarse growth exponents.

## 6. Candidate routes

### A. Block-digit recurrence

Derive `q_K` directly from:

\[
R_K,
\quad
u_0,
\quad
\varepsilon_K,
\quad
\varepsilon_{K+1}.
\]

A valuation or sign rule excluding a permanent zero tail would close the problem immediately.

### B. Shifted-value determinant

Use the exact series for `B_0^*` and its shifts. Construct a determinant involving two or more tails whose real size is controlled by the centered errors and whose `2`-adic divisibility reflects a long zero block tail.

The determinant must retain a net product-formula gain after exact reduction.

### C. Stabilization implies structured itinerary

Assume `q_K=0` for every `K>=K_0`. Then `B_0^*` is an ordinary integer. Use the nearest-integer recurrence to derive a finite arithmetic description of the later itinerary—periodicity, substitutional recurrence, or a repeated block violating `L-9311`.

### D. Extendible minimum operator

Translate the cylinder digits into a recursion for the least extendible finite survivor. Prove that a stable minimum would force an eventually zero cylinder tail and then contradict a return-word or phase invariant.

## 7. Falsification criteria

A proposed proof is incomplete if it:

1. uses only the real scheduled intervals and ignores `R_K`;
2. treats every nonrational `2`-adic series as nonordinary without a valid value theorem;
3. uses direct truncations without beating their exact height/error ratio;
4. compares factor-complexity and carry constants without a new coupling invariant;
5. infers an ordinary integer from compatible finite cylinders without representative stabilization.

## 8. Success criterion

Any one of the following closes the ordinary section:

- prove infinitely many `q_K` are nonzero for every nontrivial itinerary;
- prove the completion series `B_0^*(epsilon)` is never an ordinary positive integer outside the trivial endpoints;
- prove the exact finite minima `M_K` tend to infinity;
- prove every eventually zero block tail forces an impossible symbolic recurrence.

No stronger quantitative rate is required.