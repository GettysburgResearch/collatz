# Six-hour continuation: exact inverse minima and global proof boundaries

**Collatz remains open.** This packet continues PR 200 from `ad70a3b831867cb8a74d402a2a1abdc419f5a09b`. The work began at 2026-11-26 22:38:47 UTC. This is the fifth checkpoint of an ongoing six-hour research session.

**Latest results:** [Ordinary safe suffixes and strict cycle-rank convexity](FIFTH_CHECKPOINT.md). The actual ordinary map has a Lean-proved safe-suffix equivalence with an explicit bit-length bound. A written strict-convexity theorem makes height-one rank gaps unique and strengthens valuation-mismatch bounds without a population estimate. Separate arguments cover all positive valuations in a three-grade strip, finite physical residence and variable-denominator physical occupation. The fresh formal build has 28 local modules and 275 audited declarations; the aggregate finite replay covers 62 programs. The [fifth root review](../../reports/six-hour-20261127/ROOT_REVIEW_WAVE5.md) records the precise scopes, independent reconstructions and earlier-source qualifications.

The [fourth checkpoint](FOURTH_CHECKPOINT.md) retains the exact one-variable fifth-moment certificate, which crosses the cubic source-counting threshold and yields source-qualified fixed-denominator finiteness for binary cycles through real discrepancy `2+1/100000`. Its full fifth grid was separately rebuilt with integer arithmetic. The [fourth root review](../../reports/six-hour-20261127/ROOT_REVIEW_WAVE4.md) preserves that computation's scope.

The [third checkpoint](THIRD_CHECKPOINT.md) retains moving-phase complexity, sliding-stack bounds on one ordinary source, reflected-grade sparsity, and the earlier narrow binary-cycle results. Its [root review](../../reports/six-hour-20261127/ROOT_REVIEW_WAVE3.md) records the distinct earlier corrections and verification scope.

The main completed addition is an exact formula for the smallest positive odd ancestor on seven ternary progressions, at every depth at least seven and with no cap on the division exponents. Its ordinary shortcut and accelerated-map statements have complete Lean proofs. The second checkpoint adds genuine positive endpoint reductions, exact additional-budget classifications, simultaneous rational-anchor escape, and cycle constructions that test proposed structural implications. None supplies a universal descent selector, eliminates every possible cycle, or proves that escaping mass vanishes.

The [second root review](../../reports/six-hour-20261127/ROOT_REVIEW_WAVE2.md) records independent reconstructions and three preserved corrections. Fresh reviewers separately checked the [inverse extensions](../../reports/six-hour-20261127/INVERSE_WAVE2_INDEPENDENT_REVIEW.md), [anchor theorem](../../reports/six-hour-20261127/ADAPTIVE_ANCHOR_REVIEW.md), and [five cycle papers](../../reports/six-hour-20261127/CYCLE_WAVE2_INDEPENDENT_REVIEW.md). That checkpoint had 17 local modules and 160 audited declarations. Written and external theorem scopes remain explicit.

## 1. Exact ordinary inverse minima

Let

\[
 U(n)=\frac{3n+1}{2^{v_2(3n+1)}}\qquad(n>0\text{ odd}),
\]

and let \(M_R(X)\) be the smallest positive odd \(y\) for which \(U^j(y)=X\) at some \(0\le j\le R\). The division exponent at each step is unrestricted. Choose a row from

| \(t\) | \(a\) | \(h\) |
|---:|---:|---:|
| 17 | 0 | 0 |
| 25 | 1 | 1 |
| 37 | 2 | 2 |
| 55 | 3 | 3 |
| 41 | 4 | 5 |
| 61 | 5 | 6 |
| 91 | 6 | 7 |

For every \(R\ge7\) and integer \(z\ge1\), put

\[
 k=\left\lfloor\frac{R-a}{7}\right\rfloor,\quad
 p=7k+a,\quad H=11k+h.
\]

Then

\[
 \boxed{M_R(2\cdot3^Rz-t)=2^{H+1}3^{R-p}z-17.}
\]

The written proof also identifies the unique attaining inverse history. The formal `IsLeast` theorem proves the minimum and its attainment; it does not separately package history uniqueness.

For example, at \(R=7,t=17,z=1\), the smallest odd source reaching 4357 within seven odd departures is 4079. The assertion covers every larger depth and every positive cofactor as well. It is not an extrapolation from this example or from the finite enumeration.

The proof projects any competitor to the reflected map \(S(n)=n/2\) for even \(n\), \((3n-1)/2\) for odd \(n\). A finite integer potential, with 22 overrides and a closed trap of 34 states, bounds **all** reflected paths reaching the marked cycle. A polynomial tail inequality proves the potential inequality beyond the finite table. The signed cycle then supplies the unique optimal start and the exact positive lift. The natural-number proof keeps the available ternary rank in every projection step.

- [Statement, integer certificate and proof](pointwise/NEGATIVE17_EXACT_MINIMA.md).
- [Reflected potential and all-clock bound](pointwise/ReflectedCycleMinimum.lean).
- [Ordinary shortcut minimum](pointwise/SevenPhaseMinimum.lean), `SevenPhaseMinimum.exact_minimum`.
- [Usual accelerated-map minimum](pointwise/SevenPhaseOddMap.lean), `SevenPhaseOddMap.exact_accelerated_minimum`.
- [Independent mathematical review](../../reports/six-hour-20261127/INVERSE_MINIMUM_REVIEW.md), pinned to the written proof and its original checker.

**Prior scope.** Weaver's [Paper 108/v1](https://rstation.ai/problems/collatz/papers/108/v1) proves eventual finite terminal dictionaries for negative-cycle anchors and leaves the relevant optimizer unenumerated. [Paper 21/v3](https://rstation.ai/problems/collatz/papers/21/v3) supplies the classical cycle and its affine lifts. [Paper 178/v1](https://rstation.ai/problems/collatz/papers/178/v1) treats the negative-five barrier. This packet supplies the closed winner at all seven phases and every \(R\ge7\), including its full formal ordinary interpretation. The literature comparison is specific, not an exhaustive priority claim.

### What extra departures change

[The additional-budget theorem](pointwise/EXTRA_BUDGET.md) proves composition through the principal minimum for up to three extra odd departures and gives an effective finite terminal dictionary for every supplied extra budget. [The fourth-extra classification](pointwise/FOURTH_EXTRA_CLASSIFICATION.md) locates the unique bypass: at matching depth and \(n\equiv60\pmod{81}\), the smaller source is \((64n-33)/81\). This expression has a prior in Paper 1; the classification here concerns the complete seven-phase family.

For every ordinary target, the formal [positive budget bound](pointwise/PositiveBudget.lean) gives

\[
 M_{R+s}(X)+1\ge(2/3)^s\bigl(M_R(X)+1\bigr).
\]

If \(3^s\mid M_R(X)+1\), an actual all-one inverse path attains equality. [PositiveApplications.lean](pointwise/PositiveApplications.lean) proves this as an `IsLeast` theorem on the seven progressions. On the opposite class, at matching depth with \(3^s\mid n\), the [written overhead theorem](pointwise/ORDINARY_OVERHEAD_SPECTRUM.md) proves \(M_{R+s+2}(X)=n\) for every \(s\ge1\). It gives an exact finite positive-root test for any further overhead, and complete all-\(s\) classifications through six additional departures. Its independent controls realize every successful small-overhead tuple on every marked phase.

[Positive anchor projection](pointwise/ADAPTIVE_POSITIVE_ANCHORS.md) applies beyond these particular progressions: a bounded ancestor query at \(X=a+2\cdot3^Rz\) reduces to actual forward paths at the smaller positive anchor \(a\), from the explicit pool \(w\le\lfloor Na/X\rfloor\). The [two-way transport](pointwise/PositiveAnchorProjection.lean) and complete cutoff iff are formal. The source-side seven-phase refinements and spectrum classifications are written proofs. [Fixed-source delay](pointwise/FIXED_SOURCE_DELAY.md) and [stopping-time transfer](pointwise/STOPPING_TIME_TRANSFER.md) retain the distinction between a supplied orbit and changing constructed cofactors.

**First open step.** For an arbitrary fixed positive source, no theorem here forces an actual future endpoint to have an ancestor smaller than that source. A projection through \(R\) odd inverses still does not license a signed projection through \(R+1\) without additional ternary divisibility.

## 2. Physical word changes and their limits

[Actual word compensation](pointwise/ACTUAL_WORD_COMPENSATION.md) gives the exact carry interval and congruence required for a smaller positive multiple-of-three source at the same physical and odd clocks. It constructs infinite ordinary families where several block changes succeed even though one adjacent change is obstructed. The stronger displayed family has every nonempty original physical prefix strictly above its source, while the alternative source is exactly six smaller.

[MultiBlockCompensation.lean](pointwise/MultiBlockCompensation.lean) and [OrdinaryCountedBarrier.lean](pointwise/OrdinaryCountedBarrier.lean) prove the relevant word legality, progression identities, strict-prefix claims and selected basin equivalences. They also prove an all-clock equal-odd-count obstruction for explicit convergent sources. The odd-source qualification is essential.

Two written bounds treat long runs of blocks whose affine ordering keys are monotone. [The fixed-key theorem](pointwise/MONOTONE_BLOCK_DURATION.md) gives a polynomial bound in the logarithm of the initial height. [The uniform version](pointwise/UNIFORM_KEY_CAP.md) quantifies the dependence on the key cap. A reverse-decodable dictionary obstructs freely reordering arbitrary actual words into this favorable form. Thus neither a successful infinite family nor a real affine rearrangement is a complete ordinary selector.

### Simultaneous rational-anchor escape

At a positive ordinary state \(x\), score a reduced anchor \(p/q\) by \(v_3(x+p/q)\). [The rational-anchor theorem](pointwise/ADAPTIVE_TERNARY_ANCHORS.md) gives a clock simultaneously shallow relative to every positive rational of height at most \(H\), within an explicit initial or late dyadic window. It combines an exact adjacent transport identity with Yu's published logarithmic-form bound. For \(H\) polynomial in the late clock \(J\), the depth is \(O((\log J)^2)\). [The fixed-source packing theorem](pointwise/FIXED_SOURCE_ANCHOR_ESCAPE.md) gives sharper explicit constants for the seven marked integer anchors.

[The signed path compiler](pointwise/ALL_SIGNED_ANCHOR_COMPILER.md) permits arbitrary signs and even denominators. With Weaver's adaptive dictionary theorem it gives \(\gg\log N\log\log N\) simultaneous shallow clocks for sublinear-sized polynomial-height signed families on a fixed nonperiodic orbit. A separate elementary height split extends the prefix count to *all positive rationals* of every supplied height. That latter count can occur early in the prefix; it is not a count on every late interval. The [rational displacement](pointwise/RationalAnchorDiscrepancy.lean), [word-code kernel](pointwise/AnchorPathCode.lean), and [marked interval packing](pointwise/TernaryAnchorEscape.lean) are formal. Yu, graph compilation and the analytic complexity deductions are written with explicit external inputs.

## 3. Quantitative cycle denominator bounds

For a cyclic odd-gap word let \(A\) be the total division count, \(p\) its odd period, \(D=2^A-3^p>0\), and \(d\) the full reduced cycle denominator. For one proper cyclic window, let \(m\) count positions whose division total differs from a common integer, and let \(h\) be the largest cyclic spacing between those exceptional positions.

For fixed \(m\le M\), [the toric argument](cycles/TORIC_CYCLE_WINDOWS.md) proves

\[
 \liminf\left(\frac{\log d}{\log D}-\frac hp\right)\ge0.
\]

With fixed \(g=\gcd(A,p)\) and \(\lambda=\liminf h/p\), the lower bound improves to \(\lceil g\lambda\rceil/g\). Coprime clocks preserve the entire leading logarithmic denominator. The argument includes mixed signs and exact clock resonance. Its substantive new step bounds the retained common factor by a specialization along prime valuations; it uses the outside-\(S\) gcd theorem of Levin and Wang.

The paper also gives positive primitive rational cycles showing why a period-independent positive exponential saving fails for **any prescribed growing allowance** of exceptions when the clock gcd may grow. These examples do not have denominator one. The elementary sparse residual and the square-root scale in the canonical small-determinant window already occur in [Paper 22/v4](https://rstation.ai/problems/collatz/papers/22/v4); they are credited prior inputs.

The full asymptotic theorem is a written proof with named external inputs. [ToricWindow.lean](cycles/ToricWindow.lean) formalizes its finite algebraic interfaces, not the external gcd theorem or the whole asymptotic proof. No bound on the number of exceptional positions is established for every possible integer cycle.

### Moving defects, actual clocks and full-denominator counterfamilies

[Moving cluster denominators](cycles/MOVING_CLUSTER_DENOMINATORS.md) allows a fixed number of sublinear rectangles containing unboundedly many raw terms, using Grieve--Wang's outside-place theorem. [Ordinary clock shadows](cycles/ORDINARY_CLOCK_SHADOWS.md) gives a separate elementary finite approach: two-ended integer separation and a circle-mesh estimate force bounded-order near-resonance when a clean interval is macroscopic. [The fixed-source profile](cycles/FIXED_SOURCE_CLOCK_PROFILE.md) treats actual finite prefixes without identifying their artificial cyclic closure with an ordinary cycle. Under its additional low-defect and genuine-match hypotheses it forces exponential endpoint growth; in the stated initial-overlap case it also excludes the complete small-anchor range at that matched ternary depth.

Two explicit rational-cycle constructions identify limitations of the unrestricted structural proposals:

- [Four resonant defects](cycles/RESONANT_DENOMINATOR_INTERVAL.md) allow the full denominator fraction \(\log d/\log D\) to approach every real number in \([1/2,2/3]\), while the sparse residual gcd fraction remains \(2/3\).
- [Dense defects at every lag](cycles/DENSE_SUBEXPONENTIAL_DENOMINATORS.md) coexist with subexponential full denominator, binary gaps, discrepancy width below two and uniformly quadratic phase heights. A positive density of defects occurs at every proper lag. These cycles have growing clock gcd; the prior integer phase-order theorem already excludes denominator one in that narrow sector.

The full constructions and limiting arguments are written proofs. [ClockShadow.lean](cycles/ClockShadow.lean), [ClockMesh.lean](cycles/ClockMesh.lean) and [ResonantPulse.lean](cycles/ResonantPulse.lean) check their finite separation, mesh and root-of-unity interfaces. Complete integer-factor controls retain shared prime powers and distinguish the full phase denominator from the auxiliary residual gcd.

## 4. First-exit mass, entropy and recurrence

These notes use the physical shortcut map and the product \(3n/(3n+1)\) at odd departures. Their normalizations and external dependencies are stated individually.

| Result | Consequence and boundary |
|---|---|
| [Early gate background](gates/EARLY_GATE_BACKGROUND.md) | Computes the positive **unnormalized** mass outside the thin late-exit sieve from the defective ascending ladder law of the fair parity walk. This background has zero normalized harmonic mass. |
| [Odd-grade and square-weight leakage](gates/GRADE_GATE_LEAKAGE.md) | Gives the subcritical weight laws and the explicitly grade-truncated critical square-weight coefficient. It does not estimate the entire retained deep-label charge. |
| [Adaptive-window posterior](gates/ADAPTIVE_WINDOW_POSTERIOR.md) | Under the pinned escaping-charge inputs, late suffix laws concentrate even when distance bands are chosen adaptively. An all-scale pair-capacity inequality locates the entropy deficit. |
| [Balanced source blocks](gates/BALANCED_GATE_BLOCKS.md) | Macroscopic gate laws have asymptotically fair fixed initial parity blocks. Within synchronized blocks, their source digits and affine carries cancel exactly, with full mutual information; independent affine convolution would be invalid. |
| [Grade recurrence](gates/GRADE_RECURRENCE.md) | A density-weighted reversible walk on a hypothetical escaping component is null recurrent in the symmetric case. Directed escape remains compatible with that recurrence. |

The elementary affine and dyadic identities are formalized in [GateDyadicMoment.lean](gates/GateDyadicMoment.lean) and [GateMergeCarry.lean](gates/GateMergeCarry.lean). External coalescence, basin-density and escape-current developments are source-inspected inputs, not developments rebuilt by this packet. The missing global estimate remains a subsequence on which the retained harmonic gate mass is \(o(\log X)\), or another proved mechanism excluding each fixed escaping source.

## 5. Evidence and replay

The [first root reconstruction](../../reports/six-hour-20261127/ROOT_REVIEW_WAVE1.md), [second reconstruction](../../reports/six-hour-20261127/ROOT_REVIEW_WAVE2.md), [first source manifest](../../reports/six-hour-20261127/WAVE1_SOURCE_MANIFEST.json), [second source manifest](../../reports/six-hour-20261127/WAVE2_SOURCE_MANIFEST.json), and independent reviews distinguish mathematical reconstruction, finite computation, formal proofs and external source inspection. The [intake inventory](../../reports/six-hour-20261127/INTAKE_SNAPSHOT.json) covers all 146 open-PR metadata records at intake; the [later source snapshot](../../reports/six-hour-20261127/LATE_INTAKE_SNAPSHOT.json) pins subsequent selected advances. Neither is a claim to have read every historical branch line by line.

The replay uses Lean commit `5045d0056413266e57c625dcd7c365b10e377c52` and Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`. It rebuilds every local module in import order in a fresh directory, enables warnings-as-errors and disables automatic implicit variables, and audits every local theorem, including private lemmas. Only `propext`, `Classical.choice` and `Quot.sound` are allowed. Two missing external dependency objects are rebuilt from unchanged pinned sources; the remaining pinned Mathlib object cache is reused.

```bash
python -B research/six-hour-20261127/replay_lean.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/pinned/mathlib4 \
  --receipt /absolute/path/outside/repo/lean-receipt.json
python -B research/six-hour-20261127/replay_controls.py
python -O -B research/six-hour-20261127/replay_controls.py
```

The controls replay both Python modes and compare complete output bytes with the frozen JSON. They cover the finite gate computations, 26,792 cyclic-window cases, ordinary compensation families, 420 inverse-minimum cases, and a separately implemented 644-case inverse enumeration. These finite counts support diagnostics and independently check examples; the all-depth minimum follows from the mathematical proof and Lean theorem.

Publication additionally requires `python -X utf8 -B tools/validate.py --receipt /outside/path/checkout.json` in a clean, complete checkout. Repository integrity is a different check from mathematical validity.
