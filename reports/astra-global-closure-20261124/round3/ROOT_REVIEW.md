# Root mathematical review of the third continuation

The root reconstructed the following arguments independently of their authors. These are mathematical reviews at the listed bytes, not human peer review or a claim that the analytic arguments have been fully formalized. The separate kernel receipt records actual compiler execution. No complete Collatz proof results.

## Original-source divisor count — VERIFIED as written

Source: `research/astra-global-closure-20261124/round3/analytic/README.md`, SHA-256 `5353daa4bb3ba75ce34d510f76c366866a35df05a0561bcb28abdf9943d3fbdf`.

For a fixed division word, a covered row divides the product of the positive pair carries. This follows by truncating each competing prime valuation at the row's valuation, then applying the exact affine identity to every pair. Adjacent carries equal one. Each divisor determines at most one original source, since the fixed row's affine map has nonzero slope. The union runs over every possible word and row; it does not resample endpoints or assume an independent choice of a row.

The physical product bound gives total division exponent at most `floor(log2 X)+2(t-1)`. Positive compositions with that budget are counted by the displayed binomial coefficient. Every carry is at most `12^t X`; removing an adjacent factor leaves at most `t-2` nontrivial factors. The elementary small-prime/large-prime proof of the maximal divisor estimate is uniform, and its exponent is `o(log X)` when `t=o(log log X)`. The special case `t=2` has product one and is handled separately. This verifies the claimed subpower count, including its growing-window quantifier.

The floor-weighted carry estimate gives the separate deterministic power drop. The inequality `4^(j-i) q_i <= 4^(t-1) x` follows from `q_i <= 2^i x`. This estimate retains the original source and does not impose a cap on a single division exponent. The three-state classification follows from the two adjacent gcds being one; the manuscript explicitly treats the small sources in its exclusion of `x | U^2(x)`.

The fixed-target section conclusion subtracts a subpower exceptional count from the positive exponent in PR199 Theorem A at the same cutoff. It is conditional on exactly that theorem's external inputs. The unconditional divisor count is independent of them. The terminating-prefix construction uses a unit congruence modulo `3^t`; the full-word congruence implies every suffix integrality condition, and positive large lifts give all the stated actual valuations. It correctly blocks an inference from large short-window rank to nonconvergence.

The valuation/gcd basis was found in the primary literature during review and is credited explicitly. The packet does not claim a new general rank criterion or an improvement to the stronger whole-prefix rank results in Papers 137–138.

## Two-light ordinary descent — VERIFIED at the theorem boundary

Source: `research/astra-global-closure-20261124/round3/descent/TwoLight.lean`, SHA-256 `fdddc3ede29502691ea2a27354abdd8b09faee98fc0f338bb3b970c9cf141964`.

The theorem assumes one infinite sequence of raw positive ordinary boundary equations and odd boundary values, together with its two Boolean language restrictions. Those equations supply actual shortcut paths. A two-light checkpoint clears the denominator of `F(q)=(183q+1)/128`. The three returns have matching source/target clocks and odd counts, and their carry balances are exact. The induction proving that the comparison never reaches one accounts both for a hit before the next checkpoint and a hit after it.

At a three-light initial phase, `1024 | q+7` gives the single positive odd source `(183q+1)/256`, strictly below both original odd heights. At the other phases, the next paid boundary after zero, one or two light blocks is itself smaller and remains on the same bad input. This is an original-floor assertion. It does not follow merely from entry into the language at some later, larger height. The cycle agent additionally rebuilt the complete two-file local import closure and checked this source independently; see `cycles/REVIEW_TWO_LIGHT.md`.

The root's separate exact check reconstructs the three coefficient identities and twelve literal ordinary lifts. Its `LLPPP` example shows why appending an arbitrary third paid block is not a valid return for this same chart. The example is a finite failed extension, not a counterexample to Collatz.

## Full cycle denominator and transport cost — VERIFIED as written

Source: `research/astra-global-closure-20261124/round3/cycles/README.md`, SHA-256 `0c52480edc174b1cd6addc893797652638e10af7c142e99934264841527b2c75`.

The signed edge flux from adjacent circular swaps has unit jumps and total absolute mass at most the number of swaps. Its range costs at least half its square: the two crossings of every integer level give the stated charge, with no assumption on the locations or signs of the swaps. This bounds cyclic count discrepancy by `1+sqrt(2K)`. For coprime clocks the inverse-weight shift changes exactly two reference bits; for noncoprime clocks a proper period of the mechanical reference changes none. Primitivity ensures a positive mismatch count for the actual cycle in both cases.

The manuscript reconstructs the intrinsic bound from PR188, retaining the complete reduced denominator and the strict nonzero physical difference at a matching run. Substitution gives the finite inequality before any transcendence estimate. The cited two-logarithm lower bound supplies only the uniform logarithmic remainder. The resulting `Omega(A^(2/3))` and disjoint-swap `Omega(A/log A)` restrictions concern physical binary swaps. They do not exclude words of large transport cost.

For the signed rotation product, the local mixed-pair factors have the same sign on numerator and denominator. Multiplying the nonzero signed differences around a closed lap cancels them exactly. The counts of odd-odd and the two directed mixed cases are consistent. The dyadic valuation budget is also explained by the lengths of the subsequent matching runs, so it is not counted as an additional independent entropy restriction. The all-prime product remains an exact identity on actual values.

The new `CyclicFlux.lean` formalizes the quadratic range estimate via the potential `x*abs(x)`. The attachment of that walk to arbitrary swaps and the real asymptotic argument remain written mathematics.

## Congruence-preserving carry construction — VERIFIED, on the modified map

Source: `research/astra-global-closure-20261124/round3/cycles/CONGRUENCE_MODEL.md`, SHA-256 `98eb973ab20fb1fcc4dc5736a3bd145d944ae3229bd0a54b7d96591d0b8af3a7`.

The near-critical clocks can be chosen with the clock gap coprime to the prescribed modulus; reduction by their gcd preserves this property. The geometric-series calculation proves the already-known balanced full-denominator statement. Rounding the ideal orbit in the prescribed residue classes incurs at most `7Q/2` error per carry, leaving strictly positive bounded odd carries. The ideal-level spacing eventually exceeds the rounding scale, so all cycle states are distinct. Disjoint height intervals define one autonomous map. The separate diagonal variant retains density-zero exceptional inputs and eventual agreement modulo every fixed modulus.

Both constructions alter the literal carry at every exceptional cycle. Neither supplies an ordinary `+1` cycle. The fixed-modulus bounded alphabet and the growing-modulus diagonal variant are correctly distinguished.

## Authorship and remaining boundary

The root authored `controller/DivisorCount.lean`; its independent review is `cycles/REVIEW_DIVISOR_COUNT.md`, rather than this self-review. The two additional descent modules and their language restrictions are reviewed separately by the analytic agent. The combined build receipt identifies the exact modules, source hashes, cache boundary and selected transitive axiom reports.

The open steps are still ordinary and pointwise: cover a hypothetical least nonconverger from its original floor, or bound its fixed-target ancestor population more strongly than the lower count, and exclude high-complexity cycle words. Source density, congruence agreement and arbitrary finite realizations do not establish these implications.
