# Checkpoint 7: independent clocks, arbitrary-position certificates and dependent coding

**Collatz remains unresolved. The nine-hour pass continues through 07:56:49 UTC on 28 November 2026.** This checkpoint extends published head `e55fb7cac646013f143b563014ae97b105bc7547`. It settles several structural questions left open by checkpoint six, with separate written, finite-computational and Lean scopes.

The main advance is a proof that nonsmooth multiplicative dilates have the product binary parity law when averaged along their actual physical trajectories. Their joint centred odd-count processes converge to independent Brownian motions in every fixed finite dimension. Other results give explicit finite certificates balancing every digit position at arbitrarily large heights, remove RH from prescribed consecutive prime-factor words, and classify much more general dependent inverse codes. The coordinator reconstructed the new arguments independently before this checkpoint's freeze.

## Product parity laws and independent physical clocks

Fix positive odd integers `A,B` such that `A/B` is not an integral power of three, and fixed integer offsets `a,b`. For binary Haar input `n`, the [physical joining theorem](../../research/astra-global-20261128/cycles/MULTIPLIER_BERNOULLI_JOINING.md) proves, almost surely,

$$
\frac1N\sum_{m<N}\delta_{(T^m(An+a),T^m(Bn+b))}
\longrightarrow m_2\otimes m_2.
$$

Here `m_2` is Haar probability on the binary integers and `T` is the genuine shortcut map. Every fixed pair of length-`k` parity words therefore occurs at synchronous physical dates with frequency `4^{-k}`. In particular the mismatch fraction tends to exactly one half, closing the speed question left by checkpoint six's positive lower bounds.

For any fixed finite family `A_i n+a_i` whose pairwise multiplier ratios satisfy the same condition,

$$
\left(\frac{2k_{\lfloor Nt\rfloor}(A_i n+a_i)-\lfloor Nt\rfloor}{\sqrt N}\right)_i
\Longrightarrow (B_i(t))_i,
$$

with independent standard Brownian coordinates, using linear interpolation. This is a joint functional limit, not merely vanishing one-time covariances. It does not claim that entire finite parity words of three or more coordinates are independent.

The proof uses a new combination of native arithmetic and an incidence estimate. At each binary prefix the two current states are distributed uniformly on a binary-adic affine line. Its slope is `(B/A)3^D`, where the grade difference `D` runs through a simple symmetric random walk at the actual mismatch clock. The earlier conditional residence bound, together with the localized valuation average, proves that any direction cell modulo `2^k` has limiting physical occupation at most `C(k+3)2^{-k}`. This includes the unusually long residences near slope one; their contribution is explicitly controlled using the fixed-base two-adic logarithm bound.

Every empirical pair law is then a mixture of these uniform affine lines. Two independent sampled lines have a joint collision probability at precision `k` of at most `C(k+1)^2 2^{-2k}`, regardless of how their intercepts correlate with their directions. Its Shannon entropy is at least `2k log 2-O(log k)`. Physical stationarity and the exact parity-cylinder bijection force maximal entropy at every finite block, identifying the only possible law as product Haar. Applying this pairwise gives identity predictable covariance for the full grade martingale, and the martingale functional central limit theorem gives the Brownian conclusion.

The coordinator checked the weighted residence estimate, unfinished-clock error, parameter-conditioned line mixture, incidence sum, entropy extremality and functional-limit passage. The [earlier diffusion-rank proof](../../research/astra-global-20261128/cycles/MULTIPLIER_DIFFUSION_RANK.md) is preserved as a separate route to weaker conclusions. The arithmetic two-adic input is [Bugeaud–Laurent, Theorem 3](https://irma.math.unistra.fr/~bugeaud/travaux/logpadicdef.pdf); the functional-limit reference is [Whitt, Theorem 2.1](https://doi.org/10.1214/07-PS122). Native finite prefix identities are in `MixedParity.lean`. The new `AffineLineIncidence.lean` proves the native affine-tail identity, two-coordinate elimination, and the intersection spacing and cardinality bound for every positive modulus. The exact control checks 47,430 native tail pairs and 17,476 modular intersections, together with mixture, parity and bracket identities.

For ordinary sources in `[X,2X)`, the conclusions transfer at moving horizons `N` with `2^N=o(X)`. This restriction is essential: ordinary critical first-hit clocks generally run beyond it. A hypothetical cycle supplies a family of distinct odd multipliers to which the theorem applies, but the particular scalar `n=1` has zero Haar mass. The theorem does not exclude that exceptional trajectory.

## Exact certificates for arbitrary position-dependent digit scores

The [position-window construction](../../research/astra-global-20261128/escape/POSITION_WINDOW_PUMP.md) gives explicit positive integer multisets with a stronger balance than polynomial position moments. At **each individual position**, the full ternary input-window histogram equals the histogram after one true shortcut step. All numbers and their images have the same length and all sources are units prime to three. Coefficients may depend arbitrarily and jointly on the numeral length, the position and the local window.

There are two exact families:

| Window width | Every supported numeral length | Seed sources | Exact odd fraction |
| --- | --- | --- | --- |
| Three | `L >= 10` | 170 | `1132203 / 1790170` |
| Five | `L >= 16` | 1,822 | `160681138885642518752824520956448583294976942825721687 / 254478872673344227832204140442397827003658231711827181` |

Both fractions exceed `53/84`, and the integer comparison `3^53 > 2^84` proves `53/84 > log_3 2`. Thus every input floor admits a certificate. Summing an inequality `F(Tn)-F(n) <= q-(n mod 2)` against the certificate forces `q` to be at least its displayed fraction for this entire arbitrary-position additive class.

The two seeds were recovered with exact integer weights after numerical searches. The committed verification uses only ordinary integer arithmetic and Python's standard library. It computes the true shortcut image, expands both integers into trits, and compares their position/window counts literally. It also verifies equality of two adjacent interior carry-arc distributions for actual long division by two.

That exact equality permits repetition of the middle layer. Conservation at both joins gives a finite integer flow, which decomposes into valid ordinary input paths. The initial leading digit, final carry, parity tag and unit last digit are preserved. Odd output windows use the following transducer layer because multiplying the quotient by three shifts it by one digit; this offset is retained throughout the proof. Initial and terminal sentinel windows survive the splice. This establishes the result at every larger length, rather than just at the tested seeds.

The checker additionally reconstructs the actual weighted paths after one and two insertions. The width-three reconstructions have 202 and 233 distinct sources; the width-five reconstructions have 2,088 and 2,356. All literal position balances and parity totals pass. [Integer data](../../research/astra-global-20261128/escape/position_pump_seeds.json) · [Independent checker](../../research/astra-global-20261128/escape/check_position_pump.py) · [Exact receipt](escape/POSITION_PUMP_CHECKS.json).

The [smooth real analogue](../../research/astra-global-20261128/escape/REAL_POSITION_WINDOW_BALANCE.md) works at **every** finite radius: a positive smooth mantissa law balances every individual position while having a strictly supercritical odd-branch fraction. Four separated trit changes give a signed perturbation invisible to each local window, with a nonzero logarithmic moment. A smooth irrational-rotation coboundary realizes it as a one-step measure difference. The finite irrationality measure needed for that inversion follows from [Matveev's fixed-base theorem](https://doi.org/10.1070/IM2000v064n06ABEH000314). Synchronizing the general-radius real construction with the final ordinary division carry is still open here.

## A native width-seven price and all-radix asymptotics

Two new Lean modules connect the exact width-seven price from checkpoint six to literal ordinary arithmetic. `TernaryWidthSevenPrice.lean` checks the returning 19-state rounded cycle, its 12 decrements, the exact power inequality and every allowed leading transition. `TernaryWidthSevenNative.lean` defines an integer height from the 19 thresholds and proves for every positive ordinary input

$$
H(n)+19(n\bmod2)\le H(Tn)+12.
$$

It uses the repository's actual shortcut map. Consequently `F=-H/19` has normalized price `12/19` globally, including short numerals. The cohomological reduction that proves optimality among the entire stated score class remains written mathematics.

The [sharp-price paper](../../research/astra-global-20261128/escape/SHARP_DIGIT_PRICES.md) also extends the exact exponential width rate to every radix `p`. With `M=p^(2r-1)`, the gap above `alpha=log_3 2` is bounded below by a constant times `1/(M log M)` and above by a constant times `1/M`. Hence

$$
(q_{p,r}-\alpha)^{1/(2r)}\longrightarrow 1/p.
$$

The lower bound follows from a finite physical grid cycle in `[M,3M)`. Each exact halving consumes one binary factor; a positive rounding loss must therefore occur in every logarithmic-length run. This is an exact leading-grid argument, not a positive integer Collatz cycle.

## Prescribed consecutive prime-factor words without RH

The [rough-prime word theorem](../../research/astra-global-20261128/cycles/ROUGH_PRIME_WORDS.md) removes the remaining RH hypothesis from the positive-frequency result for prescribed words on **immediately consecutive** prime-factor additions. Under the explicitly stated ordinary component and counted-fusion inputs, every fixed prescribed word of positive-density fates occurs on a positive fraction of these consecutive links in natural probability. It does not assert an iid formula for adjacent fates.

The proof builds a positive auxiliary family from independent rough factors followed by tagged primes in disjoint size ranges. The tagged primes are the actual final consecutive additions. Upper sieve weights and a primary character-sum bound for smooth power-of-two conductors give a uniform binary cell upper bound for the whole rough product. This family is dominated by the true independent geometric-prime band law with a fixed constant. A separate smoothed-prime estimate handles current labels after arbitrary earlier marked history. Conditional band estimates, martingale concentration and the complete-signature transfer then give the ordinary frequency result.

The coordinator checked the domination direction, the ordering of the tagged primes, the arbitrary earlier subprobability, the two scale orders, and the passage to actual consecutive additions. The new primary input is [Banks–Shparlinski, Theorem 2.1](https://arxiv.org/pdf/1605.07553), with its modulus, interval-length and character hypotheses read directly. The earlier RH argument remains available as a baseline. This theorem allows multiple components; it does not prove the zero-variation alternative required for universal convergence.

## Dependent gap laws: dimension, decoding and singularity

The [dependent coding theorem](../../research/astra-global-20261128/broad/DEPENDENT_GAP_DIMENSION.md) treats any stationary ergodic process of positive gaps with finite mean `a` and entropy rate `h`. Write

$$
X=\sum_{j\ge1}3^{j-1}2^{-(E_1+\cdots+E_j)},\qquad
\Delta=a\log2-\log3.
$$

Its ternary source has lower dimension at least `(h-max(Delta,0))_+/log 3` and upper dimension at most `min(1,h/log 3)`. When `a <= log_2 3`, these agree at `h/log 3`: all symbolic entropy is retained, and the exact source determines the full gap word almost surely. Distinct finite-mean ergodic laws have mutually singular ternary sources whenever one has mean at most this boundary.

When `a > log_2 3`, the same series also converges as a positive real number. Retaining both its real and ternary values recovers the full gap word almost surely. In the stated anisotropic product metric the joint source has exact dimension `h/min(log 3,Delta)`. Distinct ergodic laws have mutually singular joint sources.

The arithmetic core is an exact word numerator: fixing its depth, total gap and numerator fixes the word. A residue and an ordinary quotient interval then bound the size of a coding fibre. Birkhoff and countable-generator Shannon–McMillan–Breiman estimates turn that arithmetic bound into dimension. A stationary Markov realization with the same one-edge occupation and a conditional-entropy argument establishes decoding; a rare-mixture entropy argument gives the singularity statement. `GapNumeratorFiber.lean` proves the actual affine identity, word recovery and finite fibre cardinality bound. The ergodic and information-theoretic arguments remain written.

For an actual escaping path, the relevant empirical coding reads the reversed past gaps. An overall mean constraint does not bound every ergodic component separately. The paper states this qualification explicitly and makes no claim that an escaping integer cannot realize one of these laws.

## Adaptive inverse policies and the complete low-cost spectrum

The [adaptive weak-marginal construction](../../research/astra-global-20261128/broad/ADAPTIVE_WEAK_MARGINALS.md) proves that **any** finite-mean stationary ergodic gap law can appear with a fixed positive weight in a weak limit of genuine finite locally Haar stationary inverse policies. A supplied fixed-total modular route reaches a long generic segment, follows it, and regenerates Haar on a unit trit. Averaging the occupations gives an actual finite state-dependent policy with a finite action cap.

For a universal `rho>0`, the limiting edge law dominates `rho J_P`, and the prelimit means tend to `rho a+2(1-rho)`. The critical iid law survives as a genuine path component, not just an edge marginal: its decoded branch images are disjoint, and the absolutely continuous part of any competing stationary law is forced to follow that critical deterministic decoder. This does not show that the critical weight tends to one or that the whole finite-policy mean reaches the entropy ceiling.

The same construction can load a positive atom at the signed fixed ray `-1`. A separate entropy argument proves a quantitative cost barrier for concentrating on rational periodic atoms: if their total limiting mass is `p`, every bounded-mean approximating sequence must reserve enough entropy in the remaining mass. Its required mean diverges as `p` tends to one. Thus arbitrary weak limits need not be diffuse, while complete bounded-cost concentration on an atom is impossible.

Finally the [inverse-cost spectrum](../../research/astra-global-20261128/broad/INVERSE_COST_SPECTRUM.md) classifies the minimum total cost `C_n(x)` over **all** legal length-`n` inverse words. Let `H(a)=a log a-(a-1)log(a-1)` and `H(a_*)=log 3`. For every `1 <= u <= v <= a_*`, the set with normalized lower and upper limits `u,v` has Hausdorff dimension `H(u)/log 3` and packing dimension `H(v)/log 3`. Its accumulation set is the whole interval `[u,v]`.

At every interior slope `b`, each prescribed sublinear positive delay or gain `g(n)=o(n)` occurs eventually at every depth on a set of full dimension `H(b)/log 3`. The gain side also holds at `a_*`. Every sufficiently large ordinary octave contains `X^(H(b)/log 3+o(1))` positive odd unit sources satisfying the corresponding finite tests through depth `log_3 X+O(1)`. These are actual finite integer statements, not claims that one positive integer realizes the infinite limiting code.

The spectrum uses Leen's stated iid Shannon-dimension theorem to select separated finite word dictionaries, then proves the stage construction, all-depth bounds and ordinary census directly. The [source refresh](../../research/astra-global-20261128/broad/FRONTIER_20261128_0415.md) records that imported theorem's exact range and the distinct absolute-continuity range. The unrestricted Haar-typical adaptive critical endpoint remains open.

## Validation and continuing work

**Fresh validation passed:** 46 Lean modules and 1,358 declarations, including 216 private declarations. The full transitive axiom audit permits only `propext`, `Classical.choice` and `Quot.sound`. All 28 finite control programs passed ordinary and optimized execution, for 56 successful runs with identical paired output. The aggregate Lean replay ran from 04:24:09 to 04:32:15 UTC. The compiler and Mathlib versions, all eight clean dependency trees and source hashes were checked. The independent scientific review records 159 source hashes and 83 reviewed Markdown manuscripts. [Lean receipt](CHECKPOINT_07_LEAN.json) · [Bounded-control receipt](CHECKPOINT_07_BOUNDED.json) · [Review and source hashes](CHECKPOINT_07_REVIEW.json). No finite check replaces one of the infinite written arguments.

The next stage is aimed at the remaining critical questions: ordinary clock structure beyond the binary observation horizon, a stopped regeneration construction for the optimal adaptive inverse cost, and the general-radius integer interface for arbitrary position scores. The conjecture still requires excluding every additional positive cycle and every escaping positive integer. None of the present theorems supplies both conclusions.

## Immutable scientific freeze

The complete reviewed scientific tree is commit `9c0fda016e473fb760fcf4303945f51889d76eb1`, tree `e9371d2231b8eec75da84fec2cac51e671ccfc96`. The repository integrity and regression validator passed on that clean commit. This publication adds its [integrity receipt](CHECKPOINT_07_INTEGRITY.json) and this reference. The GitHub commit and final clean-checkout receipt are verified separately after the exact tree is published.
