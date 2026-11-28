# Checkpoint thirteen: local landing laws, fixed-numerator complexity and critical tower synchronization

**Status:** independently reconstructed proposed written theorems, exact finite controls, and the separately stated fresh Lean kernels. This review is restricted to the source fingerprints in `source-manifest.json`. It does not certify neighboring revisions or settle ordinary Collatz convergence.

The main extension in this checkpoint is a landing law uniform over every exponentially large interval of starting numerators, even when the interval is translated arbitrarily far along the positive real axis. A second line gives the exact critical synchronization profile for powers of three and the second moment of their actual endpoint multiplicities. A third explains why a fixed ordinary numerator cannot have a landing word described by only a bounded number of cheap repeated pieces. These statements address different quantifiers and are kept separate.

## 1. A fixed numerator requires substantial word complexity

`FIXED_NUMERATOR_LANDING_COMPLEXITY.md` concerns an actual positive reduced source `m/(q 3^n)`, with `q` prime to six, through its first clearing of all ternary denominator factors. Let `T` be that native date. If its complete word is a concatenation of a fixed number `K` of powered templates of total template length `B=o(T)`, then, under the stated fixed-prime or small-denominator hypotheses,

\[
                         \log_2 m\ge n-o(n).
\]

In particular a fixed numerator cannot satisfy that description hypothesis as `n` grows. This is a complexity obstruction for an actual entire landing word. It does not assert that every landing word has such a description.

The coordinator reconstructed the exact centered block identity, including positive, zero and negative block centers. After the centers are written over their full rational denominators, the endpoint equation becomes a fixed-dimensional relation among pure powers and the landing numerator. The archimedean small form has the required saving when the asserted numerator lower bound fails. At two and the allowed denominator primes, the other forms pay for the exact denominators. The product formula retains the common binary denominator. Dividing out a primitive common factor can only improve the required inequality. A succession of rational subspace relations eliminates pure coordinates while preserving the same small form; it cannot terminate in the alleged nonzero tiny value. The argument permits a vanishing endpoint coefficient in an intermediate relation.

There is also an effective statement with arbitrary `K` and arbitrary `q`. With `H=1+B+log(2mq)`,

\[
                n\le T\le H[C\log(2+n/H)]^K.
\]

The coordinator checked the two-logarithm specialization of Yu's original theorem, including the last-exponent minimum condition, the small auxiliary parameter and the field containing the required third root of unity at the prime two. Multiplicative independence is not an unstated hypothesis of the version used. Every block supplies a nonzero integer of the form `a+3^h c`, with its coefficients charged to `H` and the previous clock. Iterating the resulting valuation bound proves the display. The treatment of a zero block center and the ordinary all-even background were checked separately.

For fixed `m,q`, the number `E` of individual even dates is therefore at least `(1-o(1)) log n / log log n`. Conversely, for each fixed `E`, the smallest numerator with exactly `E` even dates before first landing has `log_2 m_E(n)/n -> 1`. Exact dyadic cylinders give the matching construction. The note also records a relative lower-tail formula in the range where the dyadic modulus remains smaller than the ternary source grid; this is not extended past that range.

The finite control replays 872 true complete landing words, 1,659 centered powered pieces, 2,001 prescribed fast cylinders and the complete 19,682-source small-height grid. Its rational replay is independent of the centered integer formulas. These calculations test the identities and constructions, not the Subspace Theorem or the infinite valuation estimate.

## 2. Endpoint cofactors and the translated lattice count

`COPRIME_ENDPOINT_PRODUCTS.md` keeps the entire remaining denominator `Q=q 3^h` and the outside-S parts of both endpoint numerators. For a fixed number of intervening odd levels it proves

\[
                  Q\ll_\varepsilon
                  [b_S(u)b_S(v)]^{1+\varepsilon}.
\]

There is no separate numerator-height bound in this assertion. For a general native interval, its exact duration is retained in the additional binary cost. With controlled total binary height, the product has logarithm at least `log Q-o(n)`. When the original outside-S numerator is subexponential, every positive-level date after the first odd departure has almost its full possible outside-S cofactor, rather than merely all but a small fraction of marked levels.

The coordinator checked the elementary reduction from the rational Subspace Theorem to the fixed-S primitive three-term estimate. Applied to the exact endpoint identity, its common divisor is split into the S part and the outside-S part before cancellation. The latter occurs cubically in the three-term product; the surviving quotient is bounded by the product of the two endpoint cofactors. This is the reason arbitrary common numerator factors do not invalidate the conclusion. The fixed-grade time estimate is then substituted without discarding its logarithmic cofactor cost.

The useful dual consequence is a bound for a nonzero relation `a+2^s b=Qk`, with `Q` a power of three. The proof preserves the two-, three-, and outside-S parts of the common divisor. The case `k=0` is explicitly separate. This lemma supplies the short-dual obstruction needed in `LOCAL_INTEGER_LANDING.md`.

For any fixed `theta>0`, take any interval of `M>=3^(theta n)` consecutive numerators inside the complete grid and sample its ternary units. The proposed local theorem is

\[
                   T=2n+O_{A,\theta}(\sqrt{n\log n})
\]

outside probability `O_(A,theta)(n^(-A))`, uniformly in the interval's position. It also proves the stated exponential lower-deviation tail and stronger-than-fixed-stretched-exponential upper-deviation tail. The onset from the fixed-S theorem is ineffective. A single specified numerator and subexponential source intervals are outside the theorem's scope.

The delicate regime is where the entire source interval is shorter than the remaining ternary modulus. At every fixed native date, remaining height and integer floor, candidate states are points in a translated two-dimensional lattice of covolume `Q`, inside a rectangle of side lengths `Q/2^l` and `M`. A nonzero short dual vector would give the preceding three-term relation with product too small by a fixed exponential factor. Zero-coordinate and zero-quotient cases are excluded directly. A product of two squared sinc functions has Fourier support precisely small enough that only the zero dual coefficient remains. Its periodization bounds the number of candidate points in **every translate** by `8M/2^l`. The coordinator checked the support, integral, box majorant and locally uniform periodization; no equidistribution assumption for a translated thin rectangle is substituted for this argument.

This gives an unconditional bound for every fixed date/height/floor and every collection of future bit words. Union bounds first control high excursions, then the odd counts in successively shorter blocks. Only after those bounds hold simultaneously are the blocks chosen from the actual orbit. The last `O(log n)` levels are paid for with the elementary quadratic worst-case landing bound. This order avoids treating bits after an orbit-selected stopping time as independent fair bits.

The exact control compares 1,758 small dual rectangles exhaustively, identifies 58 genuine nonzero-quotient dual obstructions, excludes twelve obstructed boxes rather than claiming the bound there, and checks 132 dual-free boxes and 72 small-modulus boxes. Its 8,501 signed endpoint comparisons include 4,733 nontrivial common divisors. Large-modulus continued-fraction examples are labeled finite diagnostics.

## 3. Arbitrarily high real translates: time and final height share the cost

`TRANSLATED_LANDING_INTERVALS.md` extends the local source theorem to an interval of `3^(theta n)` through `3^n` positive numerators anywhere on the number line. Write the actual source as `x_0=X+y_0`, with `0<y_0<=1`, and let `N` be its first integer value. The strongest joint statement is

\[
       T+\log_2N=\max\{2n,\log_2m\}
                          +O_{A,\theta}(\sqrt{n\log n})
\]

with the same arbitrary polynomial confidence, uniformly over the real translate. Both observables refer to the same actual first landing. The separate time bound has the additional term `[log_2(X+1)-(2-log_2 3)n]_+`. Below that critical height by a fixed exponential margin, the landing integer is polynomial in `n` on the same good event.

The proof follows the affine contribution `3^g 2^(-t)X` of the common translate and its positive residual `y_t`. The residual is updated using the **actual source's parity bits**; it is not assumed to be an independent Collatz orbit. At fixed date and remaining height the translating contribution is known, so a bounded residual allows only a bounded number of true integer floors, regardless of how high the translate is. The translated lattice bound already covers those floors. The same good event therefore brings the actual path to `O(log n)` remaining levels near time `2n`, while controlling the residual.

Above one, each odd native step multiplies the state by at most two and each even step divides it by two. Thus the remaining duration plus the logarithm of its endpoint is bounded by the incoming logarithm plus twice the remaining odd grade. If the path first crosses below one, that crossing lies above one half and the subsequent small-height clock is charged explicitly. This proves the upper joint bound. The exact nonnegative carry identity gives `2^T N>=m`, and the lower time estimate gives the other half of its maximum.

The high-translate obstruction uses one common real translation for polynomially many sources. On the ordinary complete grid, pigeonhole a common height-one date and numerator among the typical sources. Add a suitable multiple of `2^t` to every selected initial real value. This preserves all the first `t` actual bits, while a congruence forces the new height-one numerator to be divisible by `2^D`. Those true sources then take at least `D` consecutive even steps before landing. The translate has logarithm `D+O(n)`. It rules out a smaller coefficient on the unrestricted height correction at arbitrary polynomial confidence; it does not construct one fixed divergent ordinary source.

The exact translated control checks 430 actual sources, 6,061 rational residual dates and 632 above-one time-plus-height inequalities. Four common-translate examples check 67,780 actual coast dates. In the largest example, 243 of the 13,122 unit sources share a true height-one visit and then take 257 consecutive even dates under one shared translation. Both later landing and large terminal-integer regimes are present.

## 4. Powers of three synchronize on a square-root exponent scale

`TERNARY_TOWER_SYNCHRONIZATION.md` considers either actual tower `c+M 3^n` or `c+M 3^(-n)`, for fixed integer `c` and positive integer `M`. Let `t=floor(log_2 N)` and average over any `N` consecutive exponent starts. The adjacent nonmerger fraction is `(kappa(c,M)+o(1))/sqrt(t)`, uniformly over the interval origin, with strictly positive explicitly described capacity constant. A block of `o(sqrt(t))` consecutive exponents therefore coalesces by the common deadline with density one. Endpoints a distance much greater than `sqrt(t)` apart agree with density tending to zero.

The coordinator checked the exact two cosets traced by the powers of three modulo powers of two, their period and the residual Haar entrance after a fixed depth. At least one of the two cosets is live, which proves positivity of the capacity average. To handle a sample whose length is only comparable to the full residue period, use the shorter deadline `t-O(log t)` first, then bound the newly absorbed fraction with the full period. Numerical coincidences before canonical slope equality are isolated and cost only `O(t)` exceptional exponent starts. This distinction matters for the actual rational paths in the statement.

For the positive descending tower, a block that merges before it clears its denominator has identical actual first integer landing time and value. The adjacent asymptotic consequently forces arbitrarily large positive landing-time jumps and common-landing plateaux of order `sqrt(log N)`. None of these distributional conclusions applies automatically to a specified ordinary integer numerator.

`DISTINCT_TOWER_ENDPOINTS.md` initially bounds the number of different date-`t` values between fixed positive multiples of `N/sqrt(t)`. Its first lower bound comes from the binomial distribution of the actual odd grade on the two cosets; members with the same grade cannot have the same endpoint after the exceptional small exponents are removed. The later fibre-energy argument below improves that lower constant, while preserving this earlier independently useful proof.

The tower control checks 17,600 actual Fraction endpoint pairs, 400 complete residue periods, 344,784 partial exponent visits and 212 full common-landing blocks. It explicitly includes 172 unequal-slope physical coincidences rather than excluding them by assumption.

## 5. The exact critical profile and actual fibre second moment

For gaps `k/sqrt(t)->lambda>0`, `CRITICAL_TOWER_ENDPOINT_PROFILE.md` gives actual endpoint agreement fraction

\[
                         \operatorname{erfc}(\lambda).
\]

This is a new moving-initial-level deduction from Leen's cited written process results. The coordinator read the original uniform fixed-test occupation theorem, exact odd and even holding formulas, cap-error estimate, raw first-return moment and uniform remaining-absorption estimate. The fixed-state tail alone would not justify the moving-state limit.

The embedded mixed-direction walk begins at height approximately `lambda sqrt(t)`. At a deterministic direction cutoff or its first hit of zero, its physical clock is twice its direction count plus `o_P(t)`. To prove this uniformly, divide the killed epoch process into deterministic finite blocks. The uniform expected occupation theorem controls each conditional expected reward, and bounded block martingale differences give a weak law for every fixed capped holding bias. A discrete Poisson corrector pays for the uncapped valuation tail. Its increments grow only like a squared logarithm, its endpoints are negligible by the walk maximal inequality, and visits to the boundary have a uniformly geometric tail. Centered odd and even holdings then have the required variance bounds. The reflection principle supplies the Brownian hitting profile at the rescaled cutoff. The raw return moment and the remaining-absorption bound make the later zero-level excursions negligible on this time scale.

The finite coset entrance changes the initial level by only a bounded amount and keeps the normalized offset bounded. The two-deadline period argument transfers the resulting Haar statement to actual consecutive tower exponents uniformly in their origin. The normalized offset formula, time cutoff conventions and possible terminal half-epoch were checked explicitly.

`CRITICAL_TOWER_FAMILIES.md` obtains two carefully separated extensions. Every predetermined set of `o(sqrt(t))` marks spanning a critical block has the same limiting all-mark agreement probability. For the entire consecutive block, conditioned on agreement of its outer endpoints, the number of missing interior members is tight; its limiting upper tail is `O(H^(-2/3))`. An exact whole-block limiting success probability is not inferred. The displayed five-source example at native date sixteen has matching outer values and two missing interiors, so that distinction is physically necessary.

The proof uses adjusted grades rather than an assumed ordering of real states. Once the two outer grades meet, every interior grade has already met at least one of them. Each such first crossing has a uniformly controlled later absorption delay. These bounds are used unconditionally, without conditioning on selected crossings or successful outer fusion. An early/late split, Markov's inequality and optimization of the split give the stated tightness exponent.

For the actual endpoint multiplicities `m_y`, the same note proves

\[
                  \frac{\sum_y m_y^2}{N\sqrt t}\longrightarrow
                                      \frac2{\sqrt\pi}.
\]

Compact critical lags contribute the integral of `erfc`, and the two-arm grade bound pays the Gaussian tail. The finitely many potentially exceptional low exponents contribute only `O(t^2)` pairs in total: every high-exponent part of an endpoint fibre has diameter at most `t`. This prevents an erroneous exceptional cost at every one of the `N` possible lags. Cauchy--Schwarz gives at least `(sqrt(pi)/2-o(1)) N/sqrt(t)` distinct numerical endpoints.

The exact critical control verifies 198 reflection identities, 138 clipped holding means, 2,211 intermediate adjusted-grade crossings, 253,560 high exponent visits and 362,296 equal ordered endpoint pairs. Independent Fraction evaluations check the symbolic endpoint labels. The asymptotic clock, profile and integration remain written proofs.

## 6. Connected landing semantics and full-denominator zero propagation in Lean

`ordinary/TernaryLanding.lean` adds six connected public roots for the actual odd-denominator numerator recursion. They prove the exact consumed grade, full native prefix carry, existence of a positive terminal numerator at displayed ternary height zero, preservation of ternary-unit numerators at every positive level, equality with the evaluated rational word, and preservation of all actual bits under a complete dyadic numerator translation. The termination proof uses strong induction on the positive numerator inside induction on the remaining height. Thus it supplies a real finite landing object, not a conditional endpoint identity alone.

For `q=1` and a ternary-unit initial numerator, the positive-level unit property rules out an earlier integer state. For general odd `q`, the formal recursion clears the displayed power of three and ends over `q`; its hypotheses do not silently assert a unit residual denominator. The separate word-value root connects the integer recursion to the existing affine rational evaluation. The dyadic translation root changes the terminal numerator by exactly the chosen integer while preserving the complete word, as required by the high-translate construction. None of the six roots formalizes the local lattice count or an asymptotic probability theorem.

`cycles/FullDenominatorPairZero.lean` proves two public roots. In a transitive native recurrence, one zero of an integer comparison scaled by a complete denominator forces that entire denominator to divide every comparison. Coprimality with two is the exact cancellation hypothesis. After division, the comparison is integer valued with forcing between minus two and two. Any nonzero sign persists, so transitivity back to the given zero forces all comparisons to vanish.

The roots expose the full modulus, exact recurrence, winding exponents and transitivity hypothesis. They do not assume a spatial ordering or discard a denominator factor. The actual dyadic chart, its realization and the sparse-recurrence exclusion used in the forthcoming cycle application remain written work. This local formal kernel is independently meaningful with its stated hypotheses.

Fresh compilation with Lean 4.34.1 and the pinned Mathlib source is recorded separately for both new modules. Separate imported-root audits retain the standard axiom boundary `propext`, `Classical.choice` and `Quot.sound`. The landing replay also rebuilds and audits its thirteen existing affine dependency roots; they are not counted again. Cached third-party objects are reused; no cold Mathlib rebuild or independent LeanChecker run is claimed. The eight new roots raise the cumulative published inventory to **79 distinct central roots, or 80 including the separately rebuilt motif specialization**.

## Verification and outstanding questions

The five finite programs were rerun centrally in normal and optimized Python with identical output and stable source hashes. Receipts preserve both runs and their exact inputs. Clean-checkout repository validation is a separate publication gate and does not certify the mathematics. The source-qualified analytic inputs and their actual roles are recorded above.

The local source law still leaves every specified exceptional numerator open. The tower law concerns averages over exponent intervals, even when its conclusions describe genuine integer landing values. Fixed numerator complexity supplies an obstruction to cheap descriptions, not a universal description. The worst-case logarithmic landing clock, control of unrestricted ordinary paired revisits, ordinary cycle exclusion and convergence of every positive integer remain unresolved.
