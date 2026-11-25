# Round thirteen: actual-source synchronization and its pointwise limits

**Status: PROPOSED written theorems, verified finite Lean kernels, and one separately source-qualified density refinement. Collatz remains OPEN.** This pass constructs ordinary mergers for every finite family of prescribed earlier parents inside every parameter progression. It also proves that this particular synchronized architecture misses infinitely many actual indices. The trace construction removes external renewal and pair-absorption assumptions from a lower count at selected thin original-source bands. The cycle and critical-record arguments impose further arithmetic structure without excluding the surviving ordinary cases.

Three GPT-6.2 Astra agents were explicitly run at ultra effort, with coordinator reconstruction and independent cross-reviews. The intake inventoried all 169 PRs and pinned the newly changed proof packets. That is metadata coverage of the whole repository's PR history, not a claim to have independently verified every historical proof. Late changes to PR200 and PR201 were read separately before publication. [Intake and boundaries](../../../reports/astra-global-closure-20261124/round13/INTAKE.md)

Use the shortcut map `T(n)=n/2` on even positive integers and `T(n)=(3n+1)/2` on odd ones. An ordinary statement below always concerns actual positive integers. Rational controls are labeled explicitly.

## 1. Any finite collection of earlier parents merges on a subprogression

For the difficult three-odd upper-certificate family put

$$
 j_m=11+162m,\qquad Z_m=(2^{j_m+7}-271)/81,\qquad x_m=3^{j_m}-1.
$$

The lower arm reaches `x_m` after `7+j_m` ordinary steps; `3Z_m` reaches one at that same numerical clock by a different physical word.

**Unconditional written result.** Fix any finite set of offsets `F` containing zero, and any arithmetic progression of `m`. There is a subprogression on which, for every sufficiently large `m`, all the positive parents `Z_(m-i)`, `i in F`, reach a common ordinary endpoint. Their original clocks need not agree. Each smaller parent's triple retains its own upper hit.

The new mechanism is deterministic control of one binary parameter. Let `J=max F`, `n=3^(11+162(m-J))`, and write the post-peak starts as `3^(162(J-i))n-1`. At each finite binary precision, this power of three runs through every residue `n=3 mod 8`. Fix the bits demanded by the original parameter progression. The physical continuations have forms `3^p w+B`. A signed two-form steering procedure first removes a grade difference, then contracts the remaining equal-grade disparity to zero. Earlier equalities persist. The extension corresponds to an actual subprogression of the same ordinary exponent, and odd-modulus conditions are retained by CRT.

A finite-family clock bound is

$$ H\le C^{|F|}(v+162J+4), $$

where `2^v` is the binary part of the original progression modulus and `C` is absolute. Consequently every interval of `N` sufficiently large indices contains at least `N^(1-o(1))` indices that merge with all their previous `floor(c log log N)` parents, for some absolute `c>0`. This quantitative conclusion needs no probabilistic pair-tail input.

**Pointwise obstruction, also unconditional written mathematics.** Define two indices to be related when their post-peak paths meet at the same clock and their initial exponents plus odd counts agree. Every equivalence class is finite, whether the reference path is nonperiodic or eventually periodic. The proof uses the shifted correction product

$$
 D'_h(x)=\frac{2^h(T^h x+1)}{3^{P_h(x)}(x+1)}
 =\prod_{\substack{j<h\\T^j x\ \mathrm{even}}}
       \left(1+\frac1{T^j x+1}\right).
$$

A simple-path reciprocal bound forces a bounded even gate for a nonperiodic reference; equal-clock meetings force identical visit times at a shared gate. In the periodic case a cycle phase supplies a bounded integer invariant. Thus infinitely many actual class-minimum indices have no earlier merger of this synchronized, grade-compensated form. Successful subprogressions, however abundant, do not establish the missing statement at each fixed source.

[Finite-family proof, interval bound and all-depth obstruction](trace/FINITE_FAMILY.md) · [Deterministic steering](trace/STEERING.md)

## 2. Explicit ordinary mergers checked by Lean

The constructive family includes concrete simultaneous comparisons to `Z_(m-1)` and `Z_(m-3)`. For every `L>=0`, an explicitly decidable residue class modulo `2^(2325+2L)` gives an actual common endpoint for `Z_m,Z_(m-1),Z_(m-3)`. The full clocks differ by 162 and 486. A two-parent companion gives one class modulo `2^(1705+2L)`. The two unions are disjoint and have combined parameter density

$$ \frac43(2^{-1705}+2^{-2325}). $$

The proof follows the original parents through their Mersenne peaks, three positive physical prefix representatives, additional full laps, and a common lifted tower certificate. The signed rational centers are only discovery data. Lean computes the positive representatives and proves the ordinary lift identities.

The four audited public theorems are `three_peaks`, `three_parents`, `upper_hit`, and `excludes_least`. They prove the physical statements under the exact displayed arithmetic gate. Existence of each full exponent progression is a written LTE and finite-ring argument. The least-defect corollary uses a smaller parent's independently proved upper hit; it does not assume convergence of the starting lower arm.

[Explicit progressions and proof](arithmetic/README.md) · [Compiled physical theorem](arithmetic/PostPeakMerger.lean)

A separate [density-one refinement](arithmetic/DENSITY.md) uses PR146's frozen, source-qualified oriented absorption tail. Under that input, every interval of `N` indices has at most `O(N(1+J)/sqrt(log N))` failures for a block of `J` prescribed earlier parents. Its analytic tail is not independently proved in this pass. None of the unconditional results above assumes it.

## 3. An actual-row source floor without renewal

Fix an odd unit `a` that does not reach one, let `q_i=U^i(a)` for the odd accelerated map, and let `A_i` be the true accumulated gap clock. The surplus

$$ L_i=2i-A_i $$

has upward jumps at most one and satisfies `L_i >= log_2(5/4)i-log_2 a`. It therefore attains every nonnegative integer. This permits actual suffix indices to be selected by the clock instead of requiring uniform distribution of an unconditioned terminal.

For prefix grade `k`, binary precision `h`, and ternary precision `J` with `h+J<=k/10`, select a central pre-pad word and retain its complete carry. Its source satisfies

$$
 3^k x=a2^S-D_w,\qquad D_w=2^H+3C_w,
$$

where `D_w` is independent of the long pad. A full period of `2^S mod 3^(k+J)` assigns every retained word to exactly one original-source phase. A square-root offset estimate and the ordinary mixed-residue lattice cap then give, at many selected actual balanced rows, at least

$$ c\,W/(2^h3^J\sqrt{k}) $$

positive unit sources in a width-`W` interval immediately below `a2^S/3^k`, in the prescribed mixed residue class. Here `k` is comparable to `log b`, the width is polynomial in row index `b`, and the center is exponential in `b`. The selected row may change with the prescribed cell.

The deterministic synchronization theorem supplies a binary cylinder making every start in a consecutive block of length `M` have the same endpoint and odd count at a clock at most `C M^A`. Attaching this cylinder produces disjoint nonconvergent blocks inside the same original band without external inputs F or S. One choice gives growing block length comparable to a positive power of `log k` and covered population at least `cW/k^(3/2)`.

Two precise controls limit a proposed upper-bound contradiction. First, known convergent ordinary gates reproduce the same finite-scale concentration at arbitrarily large scales when the gate varies. Second, the union of all these polynomial-width, exponentially remote bands for a fixed gate has finite reciprocal mass. Even arbitrarily long filled blocks are consistent with logarithmic density zero and with descent to that fixed gate. Tao's logarithmic-density orbit-minimum theorem supplies no opposing bound inside these bands. The upper estimate at one fixed escaping gate remains unproved.

[Complete count, blocks, convergent controls and harmonic-mass bound](trace/README.md) · [Finite Lean identities](trace/AttainedClock.lean)

## 4. Cycle factors must resist reversal, but rational controls survive

For the bounded least-tripling-disagreement cycle branch, write the rank polynomial as `C=H Q`, where `H=gcd(C,C*)` removes all factors matched by reversal. Physical edge monotonicity and a positive convolution imply

$$
 \deg Q+2\sum_{\substack{\text{conjugate root pairs of }Q\\0<\theta<\pi/2}}
       (\lceil\pi/\theta\rceil-2)>p/40.
$$

An explicit sine multiplier makes each troublesome quadratic coefficientwise nonnegative. Positivity of `C` bounds a root's distance from one by a constant times its angle; the nonzero integer `G(1)` and Smyth's Mahler-measure bound then show that an unmatched nonreciprocal irreducible factor has degree at least `c log p`. If all unmatched roots stay a fixed angle from the positive real ray, the bound strengthens to `c_theta p/log p`. This need not be the factor carrying the large determinant divisor from round twelve.

A separate distribution theorem evaluates every divisor of the complete determinant `D=2^h-3^p`. For the uniform finite population of legal positive rational cycles with the ordered bands, minimum anchor and physical height ceiling,

$$
 \mathbb E\log\gcd(D,F(u))
 =\sum_{\ell^e\mid D}\frac{\log\ell}{\ell^e}
     +O(p e^{-c\sqrt p}).
$$

Here the sum is over prime powers with multiplicity. Large cancellation is exponentially rare, including among unrestricted rank words of high degree, but no distribution claim is made after conditioning on the least-disagreement basin or ordinary denominator one.

An exact 41-phase rational cycle demonstrates the difficulty. Its primitive degree-40 rank polynomial is irreducible and absorbs `9,378,571`. It passes every one of the 1,681 one-lap inverse-clock comparisons on its fixed numerator lattice and attains all 39 applicable central multiple-of-three optima. Its reduced denominator is `44,835,377,399`. It is not an ordinary counterexample.

[Pointwise proof and control](cycle/README.md) · [Full-divisor distribution](cycle/DISTRIBUTION.md) · [Six finite Lean kernels](cycle/RankCharacter.lean)

## 5. The Subspace Theorem restricts critical limits without making them rational

We reconstructed PR210's rational classification and its genuine three-place Subspace Theorem argument. The product of forms at infinity, 2 and 3 cancels both clock monomials in a periodic approximation, leaving a small error controlled by its unreduced numerator. Under the stated repetitions and clock balance, a nonperiodic critical script has a transcendental ternary coordinate.

An explicit example uses gaps `floor(j log_2 3)-floor((j-1)log_2 3)`. A repeated local-switch construction gives a compact set consisting entirely of transcendental critical coordinates, of exact ternary Hausdorff dimension

$$ \frac{(2-\log_2 3)\log2}{2\log3}>0. $$

Every finite prefix has a positive ordinary realization. The sources vary with depth. No argument here places this set on one fixed escaping orbit, or rules out such an occurrence. The explicit construction explains why compactness and criticality alone cannot be promoted to finite rational confinement.

The previously uncompiled PR210 candidate was adapted without changing its theorem statements: narrow imports, three algebra tactic changes and two linter fixes. All 13 selected declarations now compile. The full-domain theorem still assumes `RecordLock` and `CycleExclusion`.

[Reconstructed argument and singleton control](critical/README.md) · [Explicit transcendental compact family](critical/TRANSCENDENTAL_FAMILY.md) · [Compiled finite candidate](critical/CriticalRecordRigidity.lean)

## Verification and the unresolved universal step

The root rebuilt **14 project modules in an empty project object directory**, including ten unchanged dependencies and four current modules. **119 selected transitive axiom inventories passed, 36 in the current modules.** Only `propext`, `Classical.choice`, and `Quot.sound` appeared. Strict flags include warnings-as-errors and disabled automatic implicit variables. Pinned Mathlib/package binaries and the compiler were reused.

Four exact control programs ran in normal and optimized Python with identical output and no Python assertion statements. The controls include literal ordinary blocks at a common balanced row, finite-family exponent inversion and CRT lifts, the complete 41-phase inverse-window census, and changing ordinary realizations of mechanical critical prefixes. The analytic and all-depth arguments remain written mathematics; these finite checks do not formalize them.

[Root review](../../../reports/astra-global-closure-20261124/round13/ROOT_REVIEW.md) · [Lean receipt](../../../reports/astra-global-closure-20261124/round13/lean/receipt.json) · [Control receipt](../../../reports/astra-global-closure-20261124/round13/controls/control-replay.json) · [Source ledger](SOURCES.json)

The retained [FinalProposal.lean](../round11/formal/FinalProposal.lean) still requires `remaining : FrontierMerger`. The new work has not discharged it. A complete proof must handle each surviving ordinary first failure, permitting mechanisms outside the synchronized augmented merger classes, or separately exclude both full-denominator cycles and escape at their actual sources. Ensemble rarity, successful subprogressions and transcendence of a limiting coordinate do not supply that pointwise conclusion.

Reproduce the finite proof and control runs from a complete checkout:

    python -B research/astra-global-closure-20261124/round13/check_lean.py \
      --lean /absolute/path/to/lean \
      --mathlib /absolute/path/to/mathlib4 \
      --report-dir /absolute/path/to/lean-reports
    python -B research/astra-global-closure-20261124/round13/check_controls.py \
      --report-dir /absolute/path/to/control-reports
    python -X utf8 -B tools/validate.py --receipt /outside/checkout/validation.json
