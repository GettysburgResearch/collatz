# Coordinator reconstruction and evidence boundaries

Review date: 2026-11-25. Source identities for this submitted packet are fixed in `SOURCE_HASHES.json` and the final Lean receipt. The verdicts here attach to those files and the explicitly named claims, not later edits or whole external PRs.

## TD116 and TU116: VERIFIED within the stated finite scope

The ordinary shortcut endpoint bound counts odd inputs, not odd outputs. For a fixed exponent, multiplication by an odd power of three preserves distinct residues modulo a power of two. Physical parity coding is bijective. Thus exact binomial coefficients count the parity vectors in a complete block even though the actual orbit endpoints depend on the ordinary quotient. The endpoint estimate is uniform over every allowed quotient because the base is at least the block modulus.

On the step-six ray the initial bit is forced odd. The first shortcut maps successive base indices with odd stride `3^(r+2)`, so the remaining 1023 bits still give every parity vector once. When the starting residue is 1 or 5 modulo 6, every base is odd and prime to 3. This addresses the eligible base population in the frozen smooth-core reduction, instead of deriving its existence statement merely from even bases.

The simultaneous estimate is a union bound. No independence of different exponent tests is used. The numerical certificate computes the two finite tail sums using an exact binomial recurrence proved equal to the mathematical sums. The Lean numerical proof uses `decide +kernel`. The density conclusions follow from the generic cardinality inequalities and the numerical bounds, while named corollaries expose ordinary positive endpoints. The full 116-exponent population and the eligible 116-exponent population are both covered by the kernel calculation. The sharper 65-exponent percentages are also checked by independent exact Python calculations.

The consumer `first_bad_requires_exception` is a conditional statement about a hypothetical least failure. A small exceptional population does not prove the chosen least base is outside it. The explicit long-prefix ordinary family demonstrates why the finite deadline is not universal. Its all-parameter construction is written mathematics and sixteen finite lifts are checked by the Python control.

## EC1024: VERIFIED as an exact finite-clock equivalence

For h shortcuts, the exact affine expansion is `2^h*T^h(n) = 3^q*n + C`, with a nonnegative additive offset. The uniform upper bound `C <= 3^h` in `affine_sandwich` is sufficient. At h=1024 and `n=3^r*w`, the two exact comparisons `3^646*2^1024 + 3^1024 < 2^2048` and `2^1024 < 3^647` prove descent for `q+r <= 646` and exclude it for `q+r >= 647`, respectively. The first comparison uses the smallest permitted base and then scales its positive margin to every larger base. The second needs only the nonnegative offset. Thus `exact_clock_1024` handles both directions, all nonnegative ranks, and the boundary base. It proves no all-time convergence statement. The fixed-source reviewer independently rebuilt and challenged this final module.

## TM32: VERIFIED, without a prescribed-exponent inference

The residue classes 23 modulo 32 and 59 modulo 128 give literal neighboring ternary mergers at clocks five and seven. The power-of-three action on odd residues modulo 128 supplies one such class in every 32-exponent window. The finite residue table and its lift are in Lean. This is a statement about some adjacent pair on the fixed ordinary tower. It does not identify the hypothetical first bad exponent as one of the useful upper endpoints.

## PG and physical clocks: VERIFIED with explicit approximation hypotheses

For positive odd inputs, telescoping the logarithms of the actual odd-map recurrence gives an ideal irrational rotation plus a nonnegative accumulated correction bounded by the number of observations divided by the floor. A reduced Dirichlet approximant permutes a rational grid; the construction leaves room for the signed approximation error and the positive physical correction. The matched indices are distinct times. They need not be distinct values on a cycle.

The finite polynomial specialization explicitly consumes a lower bound on the approximant denominator. Lean does not derive that hypothesis from the external logarithmic-form papers. The source includes the embedding of each odd iterate into the ordinary shortcut orbit at the sum of the actual valuations. A bound on the number of odd observations is not silently relabeled as the same number of shortcut steps.

## CW and BX: VERIFIED AS WRITTEN ARGUMENTS, external deductions SOURCE-QUALIFIED

I reconstructed the counting argument independently of its author's summary. A fixed finite bin of initial logarithmic heights gives common allowable intervals for every cumulative clock. For interval length between one and two, the proportion of positions allowing a second integer is bounded by its length minus one. The rational-grid proof is uniform in the translated initial phase: in a block of length q the error relative to a translated rational grid is at most 1/q, independent of the block's absolute index. First taking the long path length to infinity at fixed q, and then taking arbitrarily large approximants, establishes the required upper frequency.

Counting all independent integer choices only overcounts legal paths. Successive clock differences fix the gap word and its affine carry. The terminal, rather than the initial state, is fixed modulo `3^k`; the interval width is smaller than this modulus. A cycle's k-step map permutes its distinct phases even when k is larger than the period. These observations give the upper period exponent in CW. The terminal-uniqueness arithmetic is included in Lean; the uniform entropy argument is not.

The exact product around a lap gives a positive nonzero form `A log 2 - p log 3` at most `p/(3m)` and `p <= A <= 2p`. A homogeneous form bound of exponent kappa gives `m = O(p^(kappa+1))`. This contradicts CW only when the fixed band parameter is strictly below `2*3^(1/(kappa+1))`. The asymptotic statement supplies no numerical minimum cutoff and leaves wider cycles possible.

For BX, a repeated state before exiting the band would generate one of the sufficiently large narrow cycles already excluded. All states before exit are therefore distinct; length-k windows supply distinct terminals to the same finite count. At the first exit after j odd steps, positivity of the terminal and the product identity give `2^S <= n*(3+1/n)^j <= n*4^j`, hence `S <= 2j + log_2 n`. This controls the shortcut clock even when the final division gap is large. The argument does not choose the direction of exit.

Both the coordinator and the machinery reviewer checked these quantifiers. The resulting threshold is a partial restriction, not a proof that no nontrivial cycles exist. No assertion of priority over the entire published literature is made.

## PE and the symbolic obstruction: VERIFIED in separate scopes

The physical cylinder difference is exactly `2^(L-j)*3^(odd_count_j)*k`. Taking k=1 proves that every cut's stated divisor is sharp at once. All normalized cuts share the same quotient; multiplying them does not create independent source information. The Lean rank-one identity expresses this. It does not exclude nonlinear auxiliary constructions or a different analytic argument.

For the return criterion, matching h-bit windows places the two actual states in the same residue class modulo `2^h`. The stated height condition puts both states below that modulus, forcing equality. It applies to the same ordinary integer at both times.

I separately reconstructed the written masked-word argument. The equality constraints form a forest when the lag is divisible by three and force free bits to one otherwise. The probability bound `2^(-floor(h/3))`, the union bound with threshold `ceil(72+(t+d)/24)`, and the two exact affine-displacement estimates yield a positive-measure symbolic family passing every stated magnitude test. The construction neither proves congruence of those rational heights nor supplies a single ordinary integer realizing the infinite word. Finite ordinary realization with changing seeds is not all-time ordinary realization.

## Primary external sources and what was checked

| Source | Input used and evidence ceiling |
|---|---|
| [Alpöge announcement](https://alpo.ge/remark.pdf) and [MIT verification](https://math.mit.edu/~drew/grh/) | Read the announced RH/Dirichlet-GRH scope, theta-lift mechanism, and reported independent verification. No external rebuild and no GRH-to-Collatz theorem is claimed. |
| [Wu and Wang, JNT 142 (2014), Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007) | Read the publisher's statement for `p + q1 log 2 + q2 log 3` with exponent `4.1163051 + epsilon`; setting the constant coefficient to zero yields the required homogeneous estimate. The input is not an irrationality exponent for log 3 alone. |
| [Chudnovsky, October preprint](https://arxiv.org/abs/2610.28079) and [November preprint, Corollary 1.2 / Appendix A](https://arxiv.org/html/2611.30820v1) | Read the homogeneous `n + epsilon` bound, use n=2 with the multiplicatively independent rationals 2 and 3, and distinguish the reported external Lean audit from a build performed here. Its ineffective onset remains ineffective in BX and the cycle-width result. |
| [Dubickas, squares in Sturmian words](https://archive.numdam.org/articles/10.1051/ita/2009005/) | External word-combinatorial input for the written Sturmian corollary. The local arithmetic echo implication is formalized; the word theorem is not redeveloped here. |

## Frozen project comparisons

PR 192, commit `a0d7c6e36c378bbb6c826002039aef486bbe0383`, `research/astra-universal-closure-20261124/global/SmoothCore.lean`: the smaller-base merger and least smooth-core target guide the new descent result. The target remains open.

PR 173, commit `fa0c9e2a2851e6324391e39c17afcb5913185aec`, `research/lean-shell-cover/ForwardSection.lean`: the arithmetic lane credits its prior actual-orbit logarithmic identity and reduced-approximation work. That prior packet already gives shrinking sections. The present finite theorem adds a whole grid of matched times and a floor-dependent polynomial specialization; it does not supply downward movement at a mark.

PR 197, commit `b27a6fe31a487adf5615e173329ad009b975a3cd`, `research/ayh-resource-reset-20261124/closing-proposal/README.md`: bounded reverse return is distinguished from the still-open higher-rank progression.

PR 205, commit `32d722c5d5597846da5dad842c8ea15742abc176`, `research/astra-fixed-target-closure-20261124/ordinary/HEIGHT_STRIP.md`: the excursion/period restriction does not contradict the lower period exponent allowed by the new logarithmic-form input.

PR 206, commit `b2b56b94175174a680a296478f16c619a8828972`, `research/clock-itineraries/OrbitAttack.md`: its explicit all-cycle odd-width restriction and the present asymptotic width restriction have different quantifiers. The larger asymptotic threshold is not an all-minima replacement for its finite bound.

These are scoped comparisons. The intake list and reading of a proposal do not independently verify all of its mathematics or every file at its head.
