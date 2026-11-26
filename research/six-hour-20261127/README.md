# Six-hour continuation: exact inverse minima and global proof boundaries

**Collatz remains open.** This packet continues PR 200 from `ad70a3b831867cb8a74d402a2a1abdc419f5a09b`. The work began at 2026-11-26 22:38:47 UTC. This is the first checkpoint of an ongoing six-hour research session, not its closing report.

The main completed addition is an exact formula for the smallest positive odd ancestor on seven ternary progressions, at every depth at least seven and with no cap on the division exponents. Its ordinary shortcut and accelerated-map statements have complete Lean proofs. The other lanes investigate cycle denominators and the distribution of mass at first exits. None supplies a universal descent selector, eliminates every possible cycle, or proves that escaping mass vanishes.

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

**First open step.** For an arbitrary fixed positive source, no theorem here forces an actual future endpoint to have an ancestor smaller than that source. A projection through \(R\) odd inverses does not license a projection through \(R+1\) without additional ternary divisibility. Extra-depth analysis is continuing separately.

## 2. Physical word changes and their limits

[Actual word compensation](pointwise/ACTUAL_WORD_COMPENSATION.md) gives the exact carry interval and congruence required for a smaller positive multiple-of-three source at the same physical and odd clocks. It constructs infinite ordinary families where several block changes succeed even though one adjacent change is obstructed. The stronger displayed family has every nonempty original physical prefix strictly above its source, while the alternative source is exactly six smaller.

[MultiBlockCompensation.lean](pointwise/MultiBlockCompensation.lean) and [OrdinaryCountedBarrier.lean](pointwise/OrdinaryCountedBarrier.lean) prove the relevant word legality, progression identities, strict-prefix claims and selected basin equivalences. They also prove an all-clock equal-odd-count obstruction for explicit convergent sources. The odd-source qualification is essential.

Two written bounds treat long runs of blocks whose affine ordering keys are monotone. [The fixed-key theorem](pointwise/MONOTONE_BLOCK_DURATION.md) gives a polynomial bound in the logarithm of the initial height. [The uniform version](pointwise/UNIFORM_KEY_CAP.md) quantifies the dependence on the key cap. A reverse-decodable dictionary obstructs freely reordering arbitrary actual words into this favorable form. Thus neither a successful infinite family nor a real affine rearrangement is a complete ordinary selector.

## 3. Quantitative cycle denominator bounds

For a cyclic odd-gap word let \(A\) be the total division count, \(p\) its odd period, \(D=2^A-3^p>0\), and \(d\) the full reduced cycle denominator. For one proper cyclic window, let \(m\) count positions whose division total differs from a common integer, and let \(h\) be the largest cyclic spacing between those exceptional positions.

For fixed \(m\le M\), [the toric argument](cycles/TORIC_CYCLE_WINDOWS.md) proves

\[
 \liminf\left(\frac{\log d}{\log D}-\frac hp\right)\ge0.
\]

With fixed \(g=\gcd(A,p)\) and \(\lambda=\liminf h/p\), the lower bound improves to \(\lceil g\lambda\rceil/g\). Coprime clocks preserve the entire leading logarithmic denominator. The argument includes mixed signs and exact clock resonance. Its substantive new step bounds the retained common factor by a specialization along prime valuations; it uses the outside-\(S\) gcd theorem of Levin and Wang.

The paper also gives positive primitive rational cycles showing why a period-independent positive exponential saving fails for **any prescribed growing allowance** of exceptions when the clock gcd may grow. These examples do not have denominator one. The elementary sparse residual and the square-root scale in the canonical small-determinant window already occur in [Paper 22/v4](https://rstation.ai/problems/collatz/papers/22/v4); they are credited prior inputs.

The full asymptotic theorem is a written proof with named external inputs. [ToricWindow.lean](cycles/ToricWindow.lean) formalizes its finite algebraic interfaces, not the external gcd theorem or the whole asymptotic proof. No bound on the number of exceptional positions is established for every possible integer cycle.

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

The [root reconstruction](../../reports/six-hour-20261127/ROOT_REVIEW_WAVE1.md), [frozen source manifest](../../reports/six-hour-20261127/WAVE1_SOURCE_MANIFEST.json), and independent review distinguish mathematical reconstruction, finite computation, formal proofs and external source inspection. The [intake inventory](../../reports/six-hour-20261127/INTAKE_SNAPSHOT.json) covers all 146 open-PR metadata records at intake; it is not a claim to have read every historical branch line by line.

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
