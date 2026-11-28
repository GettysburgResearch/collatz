# Twelfth coordinating review: effective landing clocks and source quantifiers

Date: 2026-11-28. Branch: `research/astra-critical-rigidity-20261128`.

## Status and principal result

The coordinating lane independently reconstructed the seven new written notes, read all seven exact programs and replayed each with normal and optimized Python. The three public roots in `IntegerMinorConcentration.lean` were freshly compiled and then imported into a separate axiom audit. These are different evidence levels: the determinant kernel is formalized; the complete asymptotic theorems remain **proposed written theorems**, with finite controls for their actual arithmetic realizations.

The main new bound concerns the entire finite source grid, not a typical source. If `J(N)` is the greatest first integer landing time of the positive shortcut map from a reduced fraction `M/3^N` in the unit interval, then

\[
 J(N)\ll N^2\frac{\log\log\log N}{\log\log N}
\]

has an effective constant and effective onset. The proof uses elementary integer determinants and a coefficient-uniform valuation count. It does not invoke the Subspace Theorem or an irrationality measure. The earlier qualitative `J(N)=o(N^2)` result used ineffective Diophantine input. The important open scale is still `O(N log N)`, and the unrestricted ordinary paired-clock problem is not settled by the present effective estimate.

## 1. Distinct valuation levels with unrestricted coefficient heights

`POWER_VALUATION_LEVELS.md` proves an effective bound for the number of **distinct finite valuations** of a sum of at most `r` powers of a fixed integer base, with exponents between zero and `T`. The coefficients are arbitrary elements of the local field and may change with `T`. With a prime not dividing the base, the bound is

\[
 \exp(Cr^2)(T+1)^{1-\delta_r},\qquad
 \delta_r^{-1}=(r-1)!\sum_{i=0}^{r-1}\frac1{i!}.
\]

The coordinator checked why no coefficient-height condition is hidden in this assertion. Scaling the whole form normalizes the smallest coefficient valuation to zero and only translates the set being counted. Dividing each row by its first power changes neither its valuation nor its coefficient valuations. After boxing the relative exponents, all row entries are bounded ordinary integers. The values below the determinant cutoff are counted **once globally**, not once in every box.

If the rows above that cutoff had full rational rank, their integer adjugate would force the determinant to have more prime divisibility than its ordinary absolute value permits, because one normalized coefficient is a local unit. A column basis of the remaining rational row space expresses the same form using fewer original powers. The new coefficients are again unrestricted local numbers, so the induction applies. The recurrence balances the number of boxes with the smaller-rank exponent. Its constants grow at most exponentially in `r^2`; the factorial formula and the lower bound `delta_r >= 1/r!` were checked explicitly.

This theorem does not bound the largest individual valuation. A single coefficient can make that arbitrarily large. Counting the levels, uniformly over coefficients, is precisely what the landing application needs.

## 2. A common exceptional set for every starting numerator

`EFFECTIVE_WORST_LANDING.md` keeps the actual reduced numerator through the whole positive descent. At remaining denominator level `h`, it changes by halving on an even date and by averaging with `3^(h-1)` on an odd date. Thus it stays positive, at most `3^N`, and prime to three before landing. A packet of `k` consecutive odd departures, including its final even coast or ending at landing, satisfies the exact integer equation

\[
 u+\sum_{i=1}^k3^{h-i}2^{t_i}=2^d v,\qquad t_1=0.
\]

The proof forms a finite matrix from **all actual packets of duration at least `2N`, across all numerators at the fixed height**. The starting height and the other odd dates are boxed with side comparable to `N/k`. Each pure column becomes a bounded integer product of a power of two and a power of three, times a coefficient fixed on that box. A nonzero minor of a rational column basis supplies Cramer denominators. Multiplying through by that minor creates a common integer congruence; its other coefficients may be arbitrarily large.

For every bordered minor involving the actual numerator column, the dyadic modulus divides that minor times the chosen Cramer determinant. The columnwise size bound is strictly smaller than the modulus. The coordinator checked the factorial cost, the `3^N` numerator column, both determinant factors and the box constants. Therefore all bordered minors vanish. The actual numerator belongs to the rational span of the pure columns, even in the case where there are too few rows to form a bordered minor. Its ternary valuation zero now identifies the starting height with a distinct valuation of a short sum of powers of two. The preceding lemma bounds the number of possible starting levels.

This yields one exceptional set `E_(N,k)` of size at most `exp(Ck^2)(N+1)^(1-delta_k)` for the entire source grid. A single positive descent can use any level only once. Charging short packets, exceptional packets and the two boundary pieces gives

\[
 J(N)\le 2N^2/k+CkN+kN\exp(Ck^2)(N+1)^{1-\delta_k}.
\]

Taking `k` comparable to `log log N / log log log N` gives the stated effective bound. This argument also works uniformly for the enlarged collection of odd ternary-unit numerators at most `3^N` at any initial level at most `N`, even if their real value exceeds one. That extension is used in the next note.

The exact program replays 58,968 physical sources and 2,213,730 numerator transports. It checks 1,761 distinct long packets, 1,041 bordered-divisibility instances, six nontrivial individually certified boxes and 81,858 finite valuation rows. The small physical samples do not reach the asymptotic box-size regime. A separate explicitly synthetic fixture exercises three distinct levels in a rank-deficient box; it is not reported as a physical Collatz packet. The written proof supplies the infinite estimate.

## 3. Formal determinant scope

The new Lean module proves three public roots:

- An integer row congruence implies that its modulus divides the determinant times every selected coefficient.
- Separate bounds on each column give the corresponding factorial-times-product bound for the determinant, directly from the Leibniz formula.
- If one coefficient is nonzero and this scaled bound is below the modulus, the determinant is zero.

The root hypotheses expose every modulus, column bound and scaling factor. There is no global coefficient-height restriction. The proof uses the integer adjugate and exact divisibility; the signed-unit terms in the Leibniz formula are dealt with internally. The packet selection, rational Cramer basis, valuation induction and asymptotic optimization remain written. The local-field version of the first valuation argument is also written rather than silently identified with the integer Lean root.

The fresh build and separate imported-root audit both succeeded with Lean 4.34.1 and Mathlib source `d13f23b723b8a846827a245b89c10fc7d3f11612`. Only `propext`, `Classical.choice` and `Quot.sound` occur in the public-root axiom closure. Pinned cached dependency objects were reused; this was not a cold Mathlib rebuild or an independent LeanChecker run. The cumulative inventory is **71 distinct central public roots, or 72 including the separately rebuilt motif specialization**.

## 4. Ordinary pairs: the cost of revisiting a descending level

`EFFECTIVE_PAIRED_RUNS.md` applies the common exceptional-level set to actual unmatched positive ordinary inputs `s,3s`. Its hypotheses are quantities read from their finite parity words: `R` is the number of single-arm runs and simultaneous-odd pieces, and `V` is the largest number of descending visits to one slope gap. For `N=G+2`, the effective bound is

\[
 L\ll N^2/k+(R+1)kN+
       VkN\exp(Ck^2)(N+1)^{1-\delta_k}.
\]

The coordinator checked both physical orientations. The first joint odd date makes both states ternary units and fixes the initial nonzero translation. Higher-slope motion obeys the outward scalar recurrence and costs its grade plus a boundary term. Negative descending translations are controlled by the existing physical potential. On a positive descending segment the passive arm is actually even, so the moving arm's parity is precisely the translation numerator's parity; the comparison with a pure-three scalar descent is exact. A switch can truncate a true scalar packet but cannot lengthen it. Zero-gap coasts and incomplete final packets are charged separately.

Each exceptional descending level can be charged at most `V` times. This is the missing multiplicity factor in a direct attempt to apply the scalar bound to arbitrary pairs. The note gives effective subquadratic bounds under explicit growing bounds on `R` and `V`, and shows why an unrestricted effective modulus would already imply an effective superlinear lower bound for `ord_(2^ell-3)(3)`. That latter step remains open. The controls cover 1,024 ordinary sources, 7,320 packet partitions, both descending arms, 872 sign transitions, and both complete and truncated packets. Repeated counts across several packet choices are labeled as such.

## 5. Typical grids and coherent sources have different laws

`TYPICAL_INTEGER_LANDING.md` proves, for each fixed `A>0`, that all but `O_A(3^n n^(-A))` unit numerators have first integer landing time

\[
 \tau(n,M)=2n+O_A(\sqrt{n\log(2+n)}).
\]

The coordinator checked the unconditional residue-fiber estimate at each fixed date, remaining height and real-value floor. The proof never assumes that the bits after a stopping time are independently sampled. It bounds all relevant fixed triples first and then applies those estimates to the actual path. An excursion bound controls the range of real values; parity concentration on successively shorter remaining-height blocks gives the square-root error. The last small height is paid for using a uniform worst-case landing bound. The elementary quadratic bound suffices for the displayed typical law, while the older qualitative improvement strengthens one fixed-deviation tail. The finite controls cover every source up to height nine and include an independent Fraction replay and residue tables where the dyadic classes exceed the remaining ternary modulus.

Summability also gives the same limit two for Haar-almost every **single coherent ternary unit**, without requiring independence between heights. This should not be read as a result for one specified positive ordinary numerator.

`COHERENT_LANDING_SPECTRUM.md` supplies the complementary topological statement. If `Lambda=limsup J(n)/n`, the complete grid cluster set is `[1,Lambda]`, with `Lambda>=3`. A residual set of coherent ternary units has that same cluster set, and on a residual set every member of a prescribed countable collection of shift-stable scales sees the full worst-case limsup.

The key transplantation prepends actual positive inverse dates while keeping the entire old landing word. At any fixed ternary precision the new numerator runs through all unit classes in a bounded number of inverse dates, using the exact order of two modulo a power of three. The bounded changes in height and clock preserve normalized limits. The inverse branch and its two-gap/four-gap estimate are explicitly credited to Weaver, Paper 19/v2, section 9.1, equations B9–B10. The new uses are the exact fixed-cylinder transplantation and the coherent cluster-spectrum conclusions.

The coordinator checked both directions needed to fill the interval: the unit-interval inverse gives upward crossings from all-odd fast examples, while an alternative genuine inverse extension with average cost at most five halves per grade gives downward crossings from high records. The two ranges overlap. At full height, reaching one fixed ordinary numerator requires a discrete-logarithm congruence whose necessary cost can be exponential over the grid; no such lower bound is claimed for the maximizing entries, and that congruence is not asserted sufficient. The controls replay 6,136 entire transplanted landing words and 52,416 unit-interval inverse dates.

## 6. Two barriers to insufficient arithmetic shortcuts

`SHORT_CLOCK_FACTOR_ERASURE.md` constructs primitive physical calendars whose complete denominator loses selected shorter clock factors while retaining asymptotically full native denominator exponent. The exact quotient and its possible residual common divisor are retained; divisibility of the full denominator is not confused with equality. A growing least-common-multiple construction erases every prescribed initial collection of short factors at once. On the other hand, a fixed number of narrow clusters of shifts cannot perform the required cancellation: the separated-support moving-arc theorem forces only a subexponential common factor. The coordinator read the full pinned source at commit `505d3fe782922904e86477990cc5d41e9110edda`, including the moving coefficient and subsequence hypotheses, and checked its original Grieve–Wang outside-S input. That obstruction is source-qualified and does not yield a small multiplicative order of the remaining denominator. The controls replay 48 primitive words, 12,096 true rational dates and 144 shorter-clock tests, including nontrivial residual overlap.

`DESCENT_COFACTOR_OBSTRUCTION.md` shows why large nonsmooth marked numerators alone cannot force a short native clock. A constructive CRT argument realizes any supplied finite parity word, under an explicit source-precision budget, with every marked numerator carrying almost its full outside-P cofactor. For pure-three sources this produces long local prefixes while consuming only a small fraction of all denominator levels. For complete prescribed descents it permits a moving power-of-five residual denominator, whose large bit cost is stated. Neither construction is a counterexample to the pure-three worst-case theorem or to a fixed ordinary-input assertion.

The coordinator checked the dyadic parity cylinder, the separate prime avoidance conditions, the bounded representative inside `[Q/2,Q]`, preservation of the complete reduced denominator and the real lower bound at every mark. Two separately authored exact constructors passed: the author's control covers 114 sources and 930 marks; the coordinating constructor exhausts all words of lengths one through eight and adds long sparse and full moving-denominator cases, totaling 516 sources, 5,765 independent Fraction steps and 1,864 marked cofactor tests.

## Verification boundary and next obligations

All seven normal/optimized control pairs have byte-identical outputs, explicit active guards and stable source fingerprints in their receipts. The source manifest pins the reviewed notes, programs, author controls and the Lean runner. Repository integrity is separately validated in a clean complete checkout before publication; that check is not mathematical certification.

The recent logarithm theorem is still undergoing its separate fresh authored-source build and is not an input to any new theorem in this checkpoint. The remaining decisive obligations are the `O(n log n)` worst-case landing bound, an unrestricted bound on the number of effective descending revisits, a fixed ordinary-source bridge beyond measure/category statements, and full ordinary cycle exclusion. None is claimed complete here.
