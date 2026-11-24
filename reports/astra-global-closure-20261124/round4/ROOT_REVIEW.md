# Controller reconstruction and verification boundary

**Verdict: the new written deductions pass the controller's reconstruction at the exact scientific bytes below. Collatz remains open.** This is an additional review after the three specialist streams exchanged their work. It is not a declaration that every cited research theorem has been independently established or formalized.

| Scientific source under `research/astra-global-closure-20261124/round4/` | SHA-256 |
| --- | --- |
| `ordinary/README.md` | `dc57012b30256c4439e8dcd8c6a73f4f6a9c331f5a7a8ea6b1cacaaf9cad5dc7` |
| `arithmetic/README.md` | `f0d6a529de3e549bcb21ab6a0484f8ba39524fc07d6986e7e369a94b990dc241` |
| `arithmetic/CYCLOTOMIC_DEGREE.md` | `c9926f783775101f2765ccbe8bf0a8d3e422d92cf9287331a2aca4f522c103e4` |
| `head/README.md` | `d442ceb155a590df54cb2d790c4159e0394fa5c5b6434467efdbc7a624c8f85a` |
| `controller/KilledClock.lean` | `15a0bf212393a067b974e4f2d8c25b2fe5ca7601add74e11b0da43cf77f45254` |

All five Lean source hashes, the compiler, runtime library, runner, logs and axiom inventories are in [the fresh joint receipt](lean/receipt.json). The other four Lean sources were read in full. The author and reviewer builds are additional evidence; the controller ran its own joint replay.

## Original translated sources

The divisor argument uses diameter, not absolute height. For a large divisor, the first partial prime product above the diameter is itself a divisor of that integer. Two integers assigned the same crossing pair cannot fit in the set. The finite Rankin bound then needs only the actual divisor product's logarithm. Splitting the prime factors at `J/log J` gives the stated error without a prime number theorem.

In the Collatz application, a covered row divides the product of its actual pairwise carries. The projection of one fixed word onto that row has positive slope and is injective. A long total division clock consumes at most `s` odd inputs in the first `K` physical bits; there is one source residue for each word. The first multiplier crossing uses disjoint finite cylinders and a Bernoulli likelihood ratio, before any source selection. Consequently all three terms in (3) count the original interval uniformly over its translation. No estimate of a restarted endpoint distribution is used.

The quarter-logarithmic parameter choices leave strictly positive gaps in all three exponents. For the explicit `1/16` horizon the two limiting exponents are below `4/5`; the stated exact integer comparisons suffice. In the sublogarithmic case the condition `(1+beta)(1-sigma)<1` makes the Rankin correction subpower. The endpoint exponent follows by first taking the limiting upper exponent, then decreasing sigma. These are written asymptotic steps.

I checked the Krasikov–Lagarias statement in its original source and the loss from stripping powers of two. The target is fixed before the asymptotic limit. I also read PR193's finite synchronized image proof: one representative per terminal value remains distinct at every earlier common odd clock, so the residual-clock induction applies. Dividing the number of good original sources by the number of possible endpoints proves the final paragraph, with an interval-dependent endpoint. These two applications do not imply a hit or descent for one prescribed orbit.

## Complete denominator and local nonvanishing

The main denominator proof retains `g = gcd(S,C)` as an integer. The period identities hold in the full quotient ring; they do not require a field or an invertible `t-1`. The residue-order argument shows that every prime of `S` is at least the slot prime `N`. The small constant term of the quadratic period is therefore a unit, proving the exact undamaged gcd statement including all valuations.

At a cut outside the interiors of the altered intervals, the old and new maps have identical interval slopes. Their carry differences therefore add with exactly the displayed powers of `Q` and `P`, even when the internal cell weights change. Simultaneous approximation supplies one nonzero `u<N`, all signed exponents of magnitude less than `N/K`, and a valid modular root after raising by the inverse of `u mod N`.

The quadratic resultant cannot vanish. A common characteristic-zero root would contain a square root of `-N`. The binomial's reduction at `N` is squarefree because `N` divides none of its exponent or coefficients. The power-basis ring of each minimal factor has reduced reduction. Scaling a putative square root to minimum coefficient valuation zero and reducing its square first forces the numerator, then the denominator, to be divisible by `N`. This contradiction works even if the binomial is reducible or the template difference is divisible by `N`.

For the degree extension, the carry sum's degree is the multiplier-orbit size of its off-zero coefficients. The reduced exponent polynomial has zero constant coefficient, so the only possible multiple of the prime cyclotomic polynomial is zero. This proves the stabilizer calculation and the nonrationality hypothesis. In the local nonvanishing step, all binomial roots lift into a finite unramified extension. The translated cyclotomic polynomial is Eisenstein over that extension; a nonconstant-off-zero carry sum cannot belong to it. This rules out each conjugate factor, giving a nonzero integer resultant divisible by the whole `g`.

The root-modulus bound includes the leading coefficient `P` of the binomial. The degree and coefficient norm losses give precisely the two displayed estimates. In the undamaged many-template case, Parseval subtracts the constant coefficient in frequency space, each algebraic conjugate occurs the same number of times, and the variance is bounded by one quarter of the carry spread squared. The maximal physical carry is `2^(L-p)(3^p-2^p)`, less than `2^((2-log_3 2)L)`. Reflection and `log N=o(L)` then give the `log_3 2 / 2` lower exponent.

I checked the high-distance example against PR188's eight-cell family. Whole-slot and within-slot rotations use different counts; both have a positive mismatch fraction. Changing a bit destroys at most two mismatches for any fixed rotation. The block fixed-point lower bound propagates across the closed affine concatenation by convexity and then through its internal prefixes by the discrepancy bound. These are positive rational cycles. No inference that arbitrary integer cycles have this description is made.

## Directed head localization

The actual phase labels are permuted by one common shortcut clock. Applying the same high-lift normalization to every arm preserves three-label distinctness. The finite menu is fixed before row growth and before the original source chooses a detour. T3 therefore bounds the selected error by the unconditional finite-menu error at that same source.

In the adjacent-child recurrence, each vertical edge is charged at most twice and a parent adjacency occurs at exactly one carry. The normalization consequently has coefficient `1/81`. The finite bank of even or odd powers of two sends every phase to an interior patch. All its paths have fixed length, bounded source multiplicity, and positive patch margin after finitely many rows. Extra final rows contribute only a constant.

For the directed part, the score is a vertex difference on any two-label subset. Its comparison-square error is supported on the three-label exception. Summation cancels the horizontal terms. The log-circle row shift from doubling depends on the coordinate but not on the row, so only endpoint terms remain. The Fourier multiplier `1 + exp(2 pi i m log_81 2)` is nonzero at every fixed integer mode. The proof uses one fixed polynomial after choosing its approximation accuracy; it does not require a uniform small-divisor estimate. The approximation error is `epsilon V_N` and can be absorbed into the unsigned patch estimate.

The theorem is conditional on T3 as pinned, and the Collatz equivalence separately uses M. The reviewer correctly required the optional `GOODPROFILE` paragraph to retain P, the signed-level estimate and its original head domain; the final reviewed bytes do so. A first-passage phase requires the actual shortcut-clock parity, not merely the landing pair or the odd-count difference. The selected directed series is still unbounded by the available arguments.

## Executed evidence and limits

The fresh controller build passed all five modules and all 28 selected axiom queries with warnings as errors. Mathlib and package objects were reused; there are no local project imports in these modules. Only the three standard axioms occurred. The controller also ran the four exact control scripts in both normal and optimized Python, matched all eight outputs against the recorded JSON, and verified unchanged script hashes. [Lean receipt](lean/receipt.json) · [Finite-control receipt](controls-replay.json)

An initial attempt to compile PR201's original `KilledMoment.lean` using its umbrella `import Mathlib` was canceled during the long import/build; it gives no verdict on that source. The portable adaptation in this packet is the source actually compiled, with explicit imports and the finite common-clock additions. Its external stochastic hypotheses remain explicit.

The latest intake reviews and the controller's PR193 comparison have separate pins. In particular, the conditional PR202 block corollary follows by deleting at most one disjoint block per exceptional source; the ambient power saving beats the near-linear block count. Its weaker `0.84-o(1)` form uses the published predecessor theorem and a bounded-multiplicity unit conversion, retaining S/R and optional D. The analytic sources of those inputs were not rebuilt. [Latest intake](LATEST_INTAKE.md)

Complete-checkout integrity is a separate publication gate and supplies no additional mathematical theorem. Earlier frozen files are preserved. This review certifies the stated deductions at their hypotheses, not unrestricted convergence, an assumed rank upper bound, or independent sampling of a deterministic head pair.
