# Q-9302 — Two-place room-cusp decay

**Claim ID:** Q-9302  
**Title:** Can a short CRT frequency orbit sample enough of the stationary two-place spectral mass to close the room discrepancy?  
**Status:** IDEA  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `T-9304`, `L-9306`; branch-qualified room-position interface for the final survivor transfer  
**Scope:** newest issue-#4 room/Cantor EQ frontier  
**Related counterexample candidates:** none

## Statement

For `n,j >= 1`, put

\[
Q=64^n81^j,
\qquad
u=(81^j)^{-1}\pmod{64^n},
\qquad
v=(64^n)^{-1}\pmod{81^j}.
\]

For `H<Q`, define the restricted two-place discrepancy sum

\[
\boxed{
\mathcal D_{n,j}(H)
=
\sum_{1\le h\le H}
\frac1h
\left|
\widehat\mu\!\left(\frac{hu}{64^n}\right)
\widehat\nu\!\left(\frac{hv}{81^j}\right)
\right|.
} \tag{1}
\]

The open target is to identify a room-relevant family

\[
(n_k,j_k,H_k),
\qquad
n_k+j_k\longrightarrow\infty,
\]

for which

\[
\boxed{
\mathcal D_{n_k,j_k}(H_k)\longrightarrow0.
} \tag{2}
\]

More ambitiously, prove a quantitative estimate uniform whenever

\[
H\le Q^{\delta}
\]

for some fixed `delta>0`, or in the exact frequency regime required by the issue-#4 room recursion.

If the branch-qualified position-rigidity bijection has displacement at most `D_j` joint-modulus slots, `T-9304` gives the weighted transfer error

\[
\sum_{h\le H}
\frac1h
\left|
\frac{S_{n+j}(h)}{2^{n+j}}-G_{n,j}(h)
\right|
\le
\boxed{
\frac{2\pi D_jH}{Q}.
} \tag{3}
\]

Thus `(2)` plus

\[
\boxed{
D_jH/Q\longrightarrow0
} \tag{4}
\]

would transfer two-place cusp decay to the actual deeper survivor coefficients, conditional on that position interface.

## Definitions

The map underlying `(1)` is the short orbit

\[
\boxed{
h\longmapsto
(hu\pmod{64^n},
 hv\pmod{81^j}),
\qquad1\le h\le H.
} \tag{5}
\]

Over the complete range `h mod Q`, this map is a bijection onto the product dual group, and `L-9306` factors every absolute moment. Over a short interval, it is a thin arithmetic diagonal whose discrepancy is the whole problem.

The phrase *room-relevant* refers to parameter choices for which the issue-#4 product-rigidity/room recursion compares the actual depth-`n+j` survivor positions with the CRT product at the interval scale being counted.

## Motivation

The newest issue-#4 work shows that the finite survivor set has an exact core/Cantor product structure up to a controlled real displacement. `D-9303` through `L-9306` identify the fixed local measures and prove that global spectral correlation vanishes completely.

Therefore the residual difficulty is sharply localized:

> A low-height integer interval does not sample the product dual group independently. It follows one coupled CRT orbit determined by the inverse pair `(u,v)`.

A theorem for `(5)` would directly engage the room process rather than returning to the earlier one-place worst-frequency wall.

## Proposed proof routes

### Route A — restricted-orbit large sieve

Prove a large-sieve inequality adapted to the graph

\[
\{(hu,hv):1\le h\le H\}
\]

against the product spectral weights

\[
|\widehat\mu(a/64^n)|^2
|\widehat\nu(b/81^j)|^2.
\]

The complete second moment is exactly `2^(-(n+j))` by `L-9306`. The missing ingredient is a nonconcentration estimate showing that a short graph cannot pass through a disproportionate amount of this mass.

### Route B — two-place phase-energy inequality

Write both factors as cosine products. Seek a deterministic inequality

\[
|G_{n,j}(h)|
\le
\exp\bigl(-c(\mathcal E_2(h)+\mathcal E_3(h))\bigr),
\]

then prove that every low-height `h` has logarithmic **combined** phase energy. A resonance lost at the `2`-adic place may be forced, by the product formula and the CRT inverse relation, to generate loss at the `3`-adic place.

This route is the two-place version of `L-9303` and may succeed even when either local energy alone is small.

### Route C — solenoid renewal

View `(u,v)` as a finite reduction of one rational orbit in the dual `{2,3}` solenoid. Prove a renewal or shrinking-target theorem for the first `H` multiples of that orbit, with constants uniform in `n,j`.

The theorem must be arithmetic and quantitative. Generic unique ergodicity after taking `H` comparable to the full period is not enough.

### Route D — room recursion plus positivity

Use the issue-#4 room transition law directly. Instead of bounding `(1)` termwise, derive cancellation or entropy growth across room digits. The stationary measures identify the local transition kernels; positivity of the counting recursion may allow a transfer-operator proof that avoids absolute Fourier sums altogether.

## What would count as progress

1. A power-saving upper bound for `(1)` in any nontrivial family with `H` growing polynomially.
2. A restricted `L^2` theorem showing
   \[
   \sum_{h\le H}|G_{n,j}(h)|^2
   \le H^{1-\epsilon}+o(H)
   \]
   in a room-relevant range.
3. A combined phase-energy lower bound for every `h<=H`.
4. A proof that large joint coefficients force a structured subprogression whose mass contradicts one local block theorem.
5. A rigorous obstruction showing that a proposed range of `(2)` is impossible because of exact self-similar copies; this would still sharpen the route.

## What would falsify the motivating mechanism

- An explicit infinite parameter family with `D_jH/Q -> 0` but `D_(n,j)(H)` bounded below away from zero due to coherent local resonances.
- A proof that every short orbit `(5)` can remain trapped in high spectral mass despite the full-group moment law.
- A room displacement necessarily too large for `(4)` in every frequency range where `(2)` could be proved.

Any such result would refute this particular two-place Fourier transfer, not EQ or Collatz.

## Dependency audit

- `T-9304` supplies the pointwise two-place coefficient and conditional position transfer.
- `L-9306` supplies exact full-group moment factorization.
- The target `(2)` is open and is not used as a premise elsewhere.
- The final implication to actual survivor positions is conditional on the branch-qualified room-position theorem.
- No external large-sieve, mixing, or renewal theorem is asserted to apply.

## Gap audit

- Full-group moment factorization does not imply restricted-orbit sampling.
- The orbit length `H` may be much shorter than either local period.
- The two local coefficient arrays are highly singular and self-similar.
- A weighted Fourier sum may still be the wrong proof template below the fair window; issue #4's copy barrier remains relevant.
- Equation `(3)` controls coefficient transfer, not directly interval counts; the appropriate discrepancy lemma must still be supplied.
- Parameters `n,j,H` must be matched exactly to the live room recursion before any claimed quantitative consequence.

## Adversarial tests

1. At `H=Q-1`, the orbit is essentially the full product group and `L-9306` applies; this is too long for the target.
2. At `H=1`, a single resonant coefficient can be large; no decay should be expected without growing `H` or local energy.
3. Frequencies divisible by powers of `64` or `81` create exact local self-similarity and must be separated before any uniform estimate.
4. If `D_jH` is comparable to `Q`, the position-transfer error `(3)` is order one and the route correctly fails.
5. Any theorem proved only after averaging the starting point of the interval does not automatically control the initial segment required by `(1)`.

## Remaining uncertainty

The correct room-relevant scaling of `n,j,H` should be frozen jointly with issue #4's current recursion notation. The most promising analytic object is the combined phase energy, but it may still be defeated by exact copy frequencies.

## Suggested next attack

Derive the exact two local phase recurrences for the same numerator `h` and eliminate `h` between them. Search for a product-formula inequality showing that simultaneous low energy forces a large power of `2` or `3` to divide `h`. For polynomial-height `h`, logarithmically many simultaneous resonances would then be impossible.