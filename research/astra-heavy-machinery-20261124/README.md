# Heavy machinery applied to ordinary Collatz sources

**Status: written research results and source-qualified analytic applications, with eleven new Lean-checked finite arithmetic theorems. Collatz remains OPEN.** This packet continues PR193's ordinary class-minimum construction. It connects it to higher-rank dynamics, Mahler and differential rigidity, and basin-density arguments. The analytic and topological proofs below are written mathematics; they are not claimed to have been formalized by the small accompanying Lean modules.

The scientific base is PR193 commit `d35bdfd9d0c75effda50bbb8040c136482431e24`, followed by its validation-receipt commit `4dcc03aa236fd64b7dc1c04d2574d0f56cc24f79`. Three Astra 6.2 agents worked on the three routes. The new arguments were also independently reconstructed at the file hashes recorded in the review reports.

## The strongest positive construction

On a hypothetical escaping odd orbit, let `n_i` be the least ternary-unit representative of its i-th synchronous class. The earlier packet proves that its corrected height obeys

\[
M_{i+1}=3M_i/2^{a_i},\qquad 1\le a_i\le4,
\]

and that the correction from ordinary to corrected logarithmic height is uniformly small on every sufficiently late class.

[The critical-arm theorem](ergodic/critical.md) constructs, at arbitrarily late phases, ordinary integers `z` satisfying the repository's critical mark. For every fixed ternary precision `b`, one phase `x=n_{i+j}` and one pair of integers `e,r` work for **every** unit residue `u mod 3^b`. Each corresponding `z` satisfies

\[
z\equiv u\pmod{3^b},\qquad
v_2(3z+1)=e,\qquad
U^3(z)=U^3(x),\qquad
E_3(z)-E_3(x)=r=e+c_b,
\]

\[
c_b=2\cdot3^{b+2}+5,\qquad
\bigl|2^{-r}z-x\bigr|<13.
\]

Here `U` is the next-odd Collatz map and `E_3` is the sum of the three actual halving valuations. The class phase is reached within a polynomial in `log n_i` at future-tail record windows. The critical leading strip has width of order `1/log z`. The formula provides an actual common endpoint after three odd steps, not just congruence agreement to a finite precision.

The construction's first image is approximately `3 * 2^c_b * x`. The theorem does not force its common endpoint below the original least nonconvergent input. Producing that downward comparison remains the missing implication on this route.

## Higher-rank recurrence with ordinary realizers

[The basic proof](ergodic/proof.md) first treats **every positive real bounded-clock schedule**, without an irrationality assumption. For every accuracy there is a fixed finite set of dyadic shifts such that

\[
\left(\{2^rX_j\},\{\log_2X_j\}\right)
\]

visits every prescribed rectangle within `ceil(log₂(X₀+1)) + B` phases, whenever `2^a_j X_(j+1)=3X_j` and `1≤a_j≤4`. The proof combines Furstenberg's closed-set theorem, an irrational rotation, a finite-cover argument and a rational-grid escape lemma. It also describes a terminating finite certificate search with exact linear feasibility tests over `Q + Q log₂3`.

[The quantitative refinement](ergodic/quantitative.md) applies Kravitz–Leng's quantitative ×2, ×3 theorem and Baker–Wüstholz to obtain an absolute constant `C` and

\[
B(w),R(w)\le \exp\exp\exp(w^{-C})
\]

for rectangles of side length `w`. A bounded-denominator rounding argument handles dyadic rational starting heights as well. At suitable shrinking widths, the additive time and dyadic-rank costs are `o(log X₀)`.

The exact ordinary lifting theorem E2 supplies any prescribed finite odd-gap prefix and ternary residue at **every sufficiently large prescribed dyadic rank**, with a fixed common odd-step merger horizon. E3 combines it with the recurrence theorem. It controls corrected fractional height, ordinary leading phase, low binary and ternary digits, and the actual merger. At future-tail record windows the translated packing estimate supplies a quantitative correction bound for shrinking ordinary leading arcs.

These are results about selected sources in one actual component. They do not assert Haar-distributed native time averages or positive source density for the selected witnesses. The rank and clock inequalities in the proof retain their full dependence on the requested prefix.

## A source-specific analytic criterion for excluding escape

For a fixed positive odd rational source with odd denominator, let `A_j` be the cumulative odd halving clock and set

\[
F(z)=\sum_{j\ge0}2^{A_j-j}z^j.
\]

[The two-place proof](diophantine/proof.md) establishes the equivalence

\[
\text{eventual periodicity}
\iff F\text{ rational}
\iff F\text{ D-finite}
\iff F\text{ Mahler in some integer base}.
\]

The decisive calculation makes a companion integral series singular at the real point `2/3`, while its integral coefficients give 2-adic radius at least one. Adamczewski–Bell–Smertnig's theorem on the genuine Mahler denominator rules out a Mahler equation on a nonperiodic orbit. Bell–Smertnig's theorem for D-finite series with coefficients in a finitely generated multiplicative group gives the differential implication. PR195 GS1 already proves the ordinary-source rationality/D-finiteness equivalence; this packet credits that result and extends the domain and Mahler conclusion.

The final [adelic synthesis](diophantine/ADELIC_MAHLER.md), using the latest PR195 capacity argument and Bost–Chambert-Loir's rationality theorem, proves a stronger normalization-independent statement: for **every** nonzero rational `c` and **every** integer base `k≥2`, the series `Σ 2^A_j (cz)^j` is k-Mahler exactly when the source is eventually periodic. No mean-clock limit is assumed. Meromorphic Mahler continuation at all places and positive adelic capacity handle all rational normalizations except `c=±1/2`; the physical two-place argument handles those two. A rational change of variable alone would not preserve Mahler equations.

The same argument applies to the **signed defects of the actual least representatives**, without assuming literal minimum-to-minimum edges. With bounded cumulative-clock discrepancy, the unweighted block-defect sequence is neither automatic nor D-finite. A periodic corrected clock is included; its reset sequence has to carry the nonregular behavior.

This does not construct a Mahler or differential equation for an arbitrary source. On the periodic branch, the complete ordinary cycle condition remains `2^A−3^p | C`. The packet retains that full numerical divisor. [A separate proof](diophantine/mixed-rigidity.md) shows that the natural generating table retaining both source and time satisfies no nonzero polynomial-coefficient linear PDE, even with mixed derivatives. Thus this particular source-uniform closure cannot supply the missing source-specific equation.

## Density, automatic tests, and the predecessor potential

[The general testing lemma](dynamics/AUTOMATIC_TESTS.md) proves that a bounded sequence with a Cesàro mean and sublinear total adjacent variation is asymptotically uncorrelated with every fixed automatic observable, in every integer radix. Applied using the named external fixed-target density and adjacent-merger results, it gives

\[
\#(B\cap S\cap[1,X])=\delta\,\#(S\cap[1,X])+o(X)
\]

for the ordinary basin `B` of 1, its natural density `δ`, and every fixed automatic set `S`. It would therefore suffice to give genuine convergence certificates for all but `o(X)` members of one automatic set along cutoffs on which that set occupies a positive fraction of the integers. Positive predecessor density then upgrades this to universal convergence.

The packet also records an explicit growing-register algorithm: simulate `7 * bitlength(n)` shortcut steps and accept if 1 appears. Wren's fixed-threshold clock theorem implies that this algorithm misses only a natural-density-zero subset of the **true convergers**. This does not prove that its acceptance set has density one. The analogous algorithm for visiting 5 has the same approximation guarantee, although its two true classes both have positive lower density.

[The complementary finite-state reduction](dynamics/DENSITY_RIGIDITY.md) uses Konieczny's asymptotic Cobham theorem and exact ordinary residue transport. The local Lean theorem realizes every ternary-unit row of depth `h` as one dyadic row followed by at most `6h` shortcut steps, uniformly over all high digits.

[The potential argument](dynamics/potential.md) proves a uniform-integrability estimate on every fixed antichain of targets and on every fixed-depth inverse neighborhood of one chosen representative per component. These neighborhoods may have infinitely many ordinary targets. Their allowed depth can increase slowly with the source cutoff. The remaining terms are deep comparable target visits and the separate return-from-below estimate in the cited potential approach. No countable additivity of natural density is assumed.

The fixed-target natural-density, adjacent-coalescence, and first-passage clock inputs in this section are recent external preprint/formalization results, used at the versions listed in [the source map](SOURCES.md). Their external Lean libraries were not rebuilt here. The elementary testing, transport, and potential deductions have their own stated proof boundaries.

The latest-source comparison includes concurrent PR200's existing arbitrary-base obstruction and ordinary block constructions. Combining those weighted stopping labels with the testing lemma gives [exact proportions for weighted stopping-clock residues](dynamics/WEIGHTED_CLOCKS.md): each admissible residue modulo `m` occupies `δ/m` of every fixed automatic test, where `δ` is the original convergence-basin density. Every nontrivial clock character vanishes by a two-dilation argument. The unresolved zero character is still `δ` itself.

[The joint first-passage construction](ergodic/HEAD_DIAGONAL.md) connects the ordinary lifting theorem directly to PR199's new closing criterion. For every fixed odd unit target, a positive fraction of each sufficiently high head interval has two **equal actual first-passage roots** for the head input and its four-trit truncation, with both roots reaching that target. This gives a joint diagonal lower bound. The required summable upper bound for the off-diagonal population remains open. [Latest source comparison](LATEST_CONNECTIONS.md)

## Verification and reproduction

Run only this packet's new finite formalization and controls with

```sh
python -B research/astra-heavy-machinery-20261124/check.py \
  --lean /absolute/path/to/lean \
  --out /absolute/path/outside/the/scientific/packet
```

The root replay used official Lean 4.34.1, warnings as errors, one worker per module, and an axiom query for every public theorem. It accepted only `propext`, `Classical.choice`, and `Quot.sound`. All eleven declarations passed. The driver checks source stability during the run and records source and audited-copy hashes.

All four finite-control scripts also passed in both normal and optimized Python, with identical outputs. Coverage includes 9,009 exact ordinary E2 lifts; 250 rational starts for 40 steps; 1,364 full cycle words; 260 ordinary witnesses separating source-time translates; and all 2,186 ternary-unit rows through depth seven. These are bounded arithmetic controls, not evidence of universal convergence. [Verification report](../../reports/astra-heavy-machinery-20261124/VERIFICATION.md) · [Root proof review](../../reports/astra-heavy-machinery-20261124/ROOT_REVIEW.md)

## Full-resolution obligations still open

The new machinery supplies recurrence, actual-source realization, and exact analytic or density criteria. To conclude Collatz still requires a global step: force a marked ordinary arm below the original floor; establish the source-specific regularity criterion while excluding nontrivial ordinary cycles; or certify the one-sided positive-density convergence criterion / missing potential estimate. None of those implications is asserted in this checkpoint.
