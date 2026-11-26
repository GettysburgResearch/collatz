# First-wave independent reconstruction

**First checkpoint; no universal Collatz proof is asserted.** This report records the root review of the first six-hour continuation wave. The start was 2026-11-26 22:38:47 UTC. The publication base is PR200 at `ad70a3b831867cb8a74d402a2a1abdc419f5a09b`. The [source manifest](WAVE1_SOURCE_MANIFEST.json) fixes the integrated bytes. A later edit requires a new review boundary. The six-hour session continues after this checkpoint.

## Intake

The [intake snapshot](INTAKE_SNAPSHOT.json) records all 146 open pull requests returned by the two API pages at intake. This is a complete metadata inventory, not a line-by-line review of all historical branches. The five newly advanced source heads selected for scientific intake were:

| PR | Frozen head | Main new interface inspected |
| --- | --- | --- |
| 192 | `ed7a6fe30b8602407f77855ceb74ce0489ce9c10` | Finite-place defects in the regulator proposals |
| 193 | `25f5462e2c43feea65760884f7ea8f53576fbc18` | Dyadic splitting, clipped energy, and signed escape statistic |
| 195 | `51d97cbe17054415acaf95e422801a3532545033` | New ordinary merger/word interfaces; assigned to pointwise worker |
| 197 | `1f0f496fbea37792439feada6106eaaff596bcd1` | Conditional renormalized-real subspace-theorem obstruction |
| 201 | `21bed7ac2b1b1bb4baf0f6cabd53f8b9dd11b58a` | Native and odd-depth gate sieves, finite trapping, dyadic cycle order |

## Gate leakage: reconstructed written arguments

The root independently checked the following steps of the frozen `EARLY_GATE_BACKGROUND.md` and `GRADE_GATE_LEAKAGE.md`, now in `research/six-hour-20261127/gates/`. Their final hashes are `0951adb46c8b6520588c8b4601ba114c3a4e495b501014564cca338894acd3cf` and `ed4786792aa2049225e7c1ff17a8ba6c4bbc26f4b521ff8637ea1afa2180fcd9`.

1. A full ordinary shell `[2^m,2^(m+1))` contains each actual parity word of length `m` exactly once. For a shorter prefix the multiplicities are equal. Extending the last incomplete shell is used only for a nonnegative upper bound.
2. For clocks at most the shell rank, the exact moment is `lambda(t)^j`, where `lambda(t)=(1+3^t)/2^(1+t)`. For longer clocks, only the already sampled first `m` letters are randomized; the remaining multiplier is bounded deterministically by `(3/2)^(K-m)`. This fixes the otherwise invalid incomplete-period argument beyond `log_2 X`.
3. The resulting exponent is `t*log_2(3/2)*(c-1)+log_2 lambda(t)`. Its derivative at zero is negative precisely for `c<log(3)/(2 log(3/2))`. The separate affine-intercept error is `o(X)` in this range.
4. Fixed-clock Riemann sums use the real source variable `u=x/X`, with intensity `du/u`; the killing product tends uniformly to one on the sources that exit at those fixed clocks. Summing the successive defective ascending ladder laws gives the claimed overshoot density. The fixed-clock mass at any `o(X)` set of gate labels vanishes, while every sufficiently late gate lies in the native sieve.
5. At odd grade at most `ceil(log_3 X)`, the ternary endpoint progression has at most a constant times `X/3^q` representatives, including its endpoint error. This justifies the normalized `s<2` geometric tail estimate. The choice `max(0,s-1)<t<1` is available exactly in the stated subcritical range.
6. For the square-weight calculation, the exact endpoint interval is determined by every inverse prefix being positive and below `X`. Its Riemann error, weighted by the Bernoulli-3/4 word mass, sums to `O(1)` through the explicit grade cutoff. The remaining main term is an ordinary stopped Cesaro average; geometric waiting times give the required uniform integrability.

These checks do **not** prove that the harmonic weight on the retained deep labels is `o(log X)`. The new limit computes a positive unnormalized background, whose normalized mass tends to zero. It is consistent with a remaining nonzero escaping charge.

## Monotone block duration: VERIFIED written argument at a frozen hash

Draft source: `MONOTONE_BLOCK_DURATION.md`, SHA256 `514c2352e0c6ddf181eea277c5b92b42e72cdb8d942f78c21641a37363ded868`.

The root independently reconstructed the affine exchange formula, injectivity of the block key from its 2-adic valuation, and the repeated-block marker identity. Distinct boundaries ensure the marker is nonzero, so its divisibility by the full run clock bounds the run length. The contracting low-key interval is handled separately. In a fixed narrow key bin, irrational-rotation counting gives one eligible descent exponent per large ascent exponent and a small coefficient in the harmonic type count. Monotonicity permits each type only one run. Summing logarithmic run growth and absorbing the small coefficient bounds the final block index by a fixed power of the initial logarithmic height; physical clocks satisfy the same type of bound.

The theorem concerns every supplied ordinary segment satisfying its monotone-key condition. It does not show that a hypothetical escaping segment can be reordered legally into that form. The reverse-decoding dictionary in the companion packet directly obstructs that implication.

## Cycle denominator theorem: VERIFIED with the stated external inputs

The root directly read Levin--Wang, Theorem 1.13(1), at [the primary journal source](https://doi.org/10.1515/crelle-2019-0033). It bounds the outside-`S` gcd of coprime polynomial values on rational `S`-unit tuples outside finitely many proper translated algebraic subgroups. The outside-`S` version has no extra nonvanishing-at-the-origin hypothesis.

For `TORIC_CYCLE_WINDOWS.md`, final hash `8ac0504105e0c5912a0d8820c1a3af06a50dc7185053d18675c0bdc5f39ee246`, the root reconstructed minimal connected-coset descent, factorization of the positive binomial in a primitive torus character, and the valuation specialization. The specialization uses the valuation of the coordinate ratio to a fixed reference point. It therefore stays on the translated torus and produces the raw ternary exponents up to fixed reference shifts. A retained common factor of degree `j` contributes a segment of width `j(p-p0)/q`. Nonzero Laurent widths add under multiplication. This bounds the retained degree even with cancellations in the original signed residual, and hence bounds the complete gcd rather than selected factors.

The norm divisibility `q|tA0` and `q|tp0` quantizes irreducible-factor degrees; the resulting divisor divides the gcd of the actual two clocks. The complementary factor gives the matching height bound for rational accumulation slopes of the sparse residual gcd. Transfer of an exact slope to the original numerator retains the stated nonzero sublinear determinant hypothesis. Exact resonance is included in the denominator lower bound, but not silently inserted into that slope-transfer statement. The switch constructions and their fixed-sparsity sharp limit were checked separately from ordinary integrality. A fresh worker's [independent review](TORIC_INDEPENDENT_REVIEW.md) reconstructs the whole frozen argument, including all-prime-power transfer and the sharpness families.

The additional elementary bound is also reconstructed. Rotate the exceptional cyclic window positions into `[0,R]`, where `R=p-h` and `h` is their largest cyclic spacing. After clearing powers of three and removing the common power of two, the first residual term is odd and all later terms are even: their valuations are `min(E_i+u,E_(i+v))`, a strictly increasing sequence. Thus the residual is nonzero even in the mixed resonant case. If `theta=A/p` and `W` is the cyclic clock-discrepancy range, each normalized term is at most `2^(theta*i+W+abs(u-theta*v))*3^(R-i)`. Summation gives the printed exact denominator lower bound with the minimum of the term count and geometric factor `1/(1-3/2^theta)`. Its square-root canonical consequence is credited prior work.

**Prior-work correction during intake.** The root opened the current primary [Paper 22 v4](https://rstation.ai/problems/collatz/papers/22/v4), including its sparse residual, minimal-coset argument, and Theorem 5A. Its oddness proof and square-root consequence substantially precede the corresponding reconstructions above. They are checked prior inputs, not new cycle exclusions. The final packet contains the explicit comparison and quantitative retained-factor extension. Separately, [Paper 178 v1, section 5](https://rstation.ai/problems/collatz/papers/178/v1) already supplies the negative-five root/gain mechanism; the packet credits it. Neither discovery is a global proof.

## Exact seven-phase minima: written proof and complete local Lean theorem

The root reconstructed the displacement projection through the stated ternary rank, the complete reflected potential argument, the phase calibration, the ordinary positive lift and the strict margin against every off-cycle reflected start. The 34-element closed trap excludes all odd reflected starts below 21 except 17. The modified potential has 22 overrides and a uniform polynomial tail beyond 244. The product inequality holds at every physical time. The remaining same-cycle competitors are ordered strictly by their lap counts. These steps concern all genuine positive odd competitors at the supplied budget, not a capped search.

The frozen written proof is `1d036bb16dd0623a95d09124d8e88ec06d071a8981ba5d126ff92eaa175fed60`. A fresh independent worker reconstructed it without importing the author's checker; the [separate review](INVERSE_MINIMUM_REVIEW.md) describes both mathematical checks and its different enumeration. Its verdict is pinned to the written source, not extended to later Lean files by implication.

The root read the complete formal definitions and main statements. `Ancestor` requires a positive odd ordinary source, an actual iterate of the shortcut and its recursively counted odd departures. `project` builds a strictly positive reflected source by a natural-number displacement, and `dual_transport` proves every parity and endpoint equality. `exact_minimum` proves `IsLeast`, including attainment. The accelerated interface defines the usual odd part with the exact factorization exponent, proves correspondence of the two clocks, and obtains the same `IsLeast` statement for genuine accelerated iterates.

The final formal sources are `ReflectedCycleMinimum.lean` at `9e78964fec3ea9cc549f08291d2b1bc3bbdcbdb283364b38d6aa53ab78d4e3a6`, `SevenPhaseMinimum.lean` at `db030a2c0a3e065c7cfab0905ed227d7df1828764f9a36fad7683a87b1517511`, and `SevenPhaseOddMap.lean` at `283b522e648cb64a20de903bc9cc16e3393a1ebfe0326e56070f4b3c20c233c6`. The superseding minimum hash adds audits of all private lemmas without changing the proof body. Its result is a complete formal minimum theorem on the stated seven progressions, not a formal proof of Collatz. Written uniqueness of the attaining history has not been separately packaged as a formal theorem.

## Other pointwise and gate reconstructions

The root checked the actual-word carry interval, the two infinite multiple-block examples and their positive integer parity interpretation. The stronger family's every nonempty physical prefix is strictly above its start, although its competing source is six smaller. The reverse-unique terminal congruence dictionary prevents treating arbitrary affine reorderings as legal positive paths. For monotone keys, the nonzero repeated-block marker, the irrational-rotation harmonic type count and the absorption of the small-bin term prove the stated duration bound. The uniform addendum's continued-fraction counting and repeated logarithmic-height bounds give its explicit dependence on the key cap. These are conditional structural bounds on supplied ordinary segments, not an exhaustive selector.

For `ADAPTIVE_WINDOW_POSTERIOR.md`, the root checked the common-suffix atom using the order of fixed-bottom, fixed-anchor and large-gate limits. The random-dyadic-grid proof bounds the sum of all fair-pair capacities by entropy. This covers adaptively selected bands as well. The separate finite harmonic-row estimate uses an injective ordinary source map, an inclusive source residue class and a geometric-clock tail; it does not infer independence of conditional inverse words.

For `BALANCED_GATE_BLOCKS.md`, the root directly read the pinned `GaoShortcutBridge.lean` and the relevant `Martas.lean` statement/proof portions. This is source inspection, not a replay of that external development. Equal native arrival clocks and odd counts give exact equal gate weights within each usable block. The periodic exceptional-set bound survives harmonic weighting. The affine carries are exactly anticorrelated with the source digits. High entropy at early clocks and a nearly deterministic late suffix are therefore consistent.

For `GRADE_RECURRENCE.md`, the root checked the density flow, well-defined signed grade, direction-word normal form, cancellation of forward/backward steps, binomial grade transition and the fixed-grade bridge maximum. The symmetric return law and effective slab resistance concern the specifically weighted reversible network. Neither entails recurrence of the directed ordinary trajectory or an invariant probability measure on its states.

## Executed checkpoint checks

The root independently rebuilt all eight local Lean modules, with 97 local theorem audits, in fresh temporary object directories. The version pins, flags, every source hash and every axiom report are in [LEAN_WAVE1_RECEIPT.json](LEAN_WAVE1_RECEIPT.json). All audits used only `propext`, `Classical.choice` and `Quot.sound`. Two missing Mathlib dependency objects were rebuilt from unchanged pinned source; the other pinned external objects were reused.

All five finite-control programs were executed in normal and optimized Python. Their complete output bytes agree with each other and with the retained results. The [control receipt](CONTROLS_WAVE1_RECEIPT.json) includes hashes. The separate 644-case audit preserves path multiplicities and uses an inclusive height cap instead of the author's recursive minimum pruning. Both enumeration methods permit all exponent branches that can attain or improve the tested bound. Counts are finite evidence; no all-depth conclusion is inferred from them.

## Literature interface inspected

OpenAI/math was pinned at `3344da59991ed94f9ba711217b29c1d760badfa6`. The root read result 148's introduction, pair-capacity lemma, and disjoint-window proof from their TeX source. The useful mechanism is choosing a later entropy band after earlier fine endpoints are known, then summing disjoint gains without a uniform endpoint rate. Its application there uses independent conditional tails averaging to one self-similar law. No such stationary conditional-tail identity has been established for a fixed escaping ordinary Collatz path. This is an attempted interface, not an imported Collatz theorem or a review of the whole external manuscript.
