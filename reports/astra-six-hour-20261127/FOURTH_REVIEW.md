# Fourth checkpoint: precise scope of the new statements

This checkpoint continues the six-hour pass. **It does not prove Collatz.**
The earlier published checkpoint is
`b69d47f7fc0a8c6c3f227b0afcaf69b28cc92845`. Its publication and clean-checkout
validation receipts are retained in [CHECKPOINT3.json](CHECKPOINT3.json).

## The finite rational proposal

[RationalEnergy.lean](../../research/astra-six-hour-20261127/root/RationalEnergy.lean)
defines the actual odd Collatz orbit energy

\[
 E_{K,H}(y)=\sum_{k\le K}\sum_{\substack{1\le x\le H\text{ odd}\\U^kx=y}}
 x^{-3}\prod_{i<k}d(U^ix),\qquad
 d(n)=\begin{cases}1/4&n<13,\\1+1/(32n^2)&n\ge13.\end{cases}
\]

The checked conclusion is
`EnergyCriterion -> Universal`, where the criterion consists of a uniform
upper bound of 8 on all these finite sums and uniform decay for large targets.
The depth and source cutoffs are unrestricted in the decay assertion. No
instance of either premise is supplied.

The contradiction proof tracks one actual source. Failure to reach a small
odd integer forces its weight to stay at least one, so the decay premise
bounds its entire orbit. The weight then grows on this bounded set, contrary
to the uniform bound. Formal ordinary halvings and checked small odd paths
complete the implication. The accompanying written note proves a converse
without a logarithmic time hypothesis. That converse is not part of the
present formalization.

[AdaptiveGreen.lean](../../research/astra-six-hour-20261127/global/AdaptiveGreen.lean)
checks the monotonicity and exact rational inequalities for the prefix boost
`1+1/(2*max(r,13))+1/(12*max(r,13)^2)`. Its squared normalized edge factor
dominates `d(n)` whenever the representative is below the physical state.
The infinite Green construction, its rational rounding, Haar integral,
ordinary simple-path bounds, summable prebirth injection, and its equivalence
to convergence are written arguments. The missing estimate is ordinary
target decay along the forward trajectories of fixed small sources.

## Analytic arithmetic used in this pass

The new pointwise rank-pair theorem is a written deduction from two precise
analytic inputs: Lindelöf for the Riemann zeta function, in the exponential-sum
form of Ivić (2001), equation (5.1), and Robert–Sargos (2002), Theorem 1,
equation (1.6). The proof keeps the phase of the second dual rank after
separating the smooth cutoff weights. Its fourth derivative has size
`p*d/K^4`; both terms of the fourth-derivative bound are retained. This gives
the range `R <= C*p^(11/20)` and, under the ordered three-band cycle
hypotheses, the lower exponent `1000/479+11/20`.

The November 2026 RH verification record was read at the
[MIT primary page](https://math.mit.edu/~drew/grh/). RH implies the Lindelöf
input used here. The record reports checks of zeta and Dirichlet-character
statements; this checkpoint does not enlarge that scope to arbitrary Hecke
or automorphic L-functions. It does not claim to have independently rebuilt
or imported the external proof. The claimed upper irrationality exponent
three for `log(3)/log(2)` is source-qualified to Chudnovsky's November 2026
[Corollary 1.2](https://arxiv.org/html/2611.30820v1), taking two independent
positive rationals and dividing the homogeneous linear-form bound by the
rational-approximation denominator. This leaves a genuine gap between
`2.63768...` and `3` in the cycle application.

The binary bridge certificate checks three return-word products and their
frequencies using rational interval arithmetic. It brackets the critical
width of the specified fourth-energy test between `1.98534327` and
`1.98534329`. The fixed-denominator finiteness consequence also retains the
source estimate from pinned PR200 and its fixed-place Subspace input; its
onset is ineffective. Integer transfer lower bounds and log convexity
establish a limitation of every fixed even moment in the stated unweighted
equal-segment method. This is not a limitation of all possible correlated
or weighted arguments. The root replay ran both ordinary Python and `-O`,
with identical complete JSON outputs; all checks use explicit exceptions.

## Signed source limits

The Poisson clock spectrum is a written theorem retaining the named
fixed-floor passage, basin-density, and simple-prefix packing inputs. It
separates positive cycles by their actual lap contraction rates. A limit
containing the basin density of 1 does not evaluate that density as one.
The Fourier formula remains under the original geometric word law, with
its actual binary source class and total exponent.

The translated-window construction extends negative integer shadows to
signed rational shadows of denominator `3^r`; the shadow becomes an actual
negative integer after its `r`-th odd departure. This proves only a
finite-horizon obstruction. The second theorem in that note uses the p-adic
Subspace Theorem with fixed rational coefficients and powers of two to
exclude recurrent bounded signed residues at bounded gaps along an escaping
ordinary ray. It supplies arbitrarily long shadow-free blocks. It does not
prove that all other delayed windows disappear.

The two-width difference at depth `floor(8*log(R))` removes every ordinary
terminal other than 1 with an explicit power-saving error. This finite
isolation uses only deterministic lower bounds for the actual multiplier.
The further stationary first-return computation retains the inverse-density
and endpoint-gap inputs: its Mellin transform is an entire exit numerator
divided by `1-(3/4)^s`, with residue `d1/2` at zero. Singularity of the exit
law modulo the logarithmic period makes at least one nonreal lattice pole
genuine. The numerator's reciprocal moment is still unevaluated.

The separate sparse-shadow note strengthens the Subspace application. Fixed
numbers of terms with subexponentially moving coefficients have only
sublinear ternary valuation unless they cancel exactly. This yields clean
blocks avoiding exponential-width neighborhoods of nonzero ternary multiples
and signed binary representatives with any fixed digit count. In the exact
zero case, compactness of the sparse mantissa set and the irrational rotation
of an escaping ray rule out a syndetic chain. The resulting waiting bounds
are existential and retain ineffective Diophantine constants.

## Reproduction boundary

[LEAN_FOURTH.json](LEAN_FOURTH.json) records a fresh build of all 15 packet
modules with Lean 4.34.1, pinned Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`, automatic implicit parameters
disabled, and warnings treated as errors. All 130 public theorem inventories
use only `propext`, `Classical.choice`, and `Quot.sound`. The missing cached
Mathlib Field object was rebuilt from the pinned source in a temporary
overlay. None of the new infinite analytic arguments or external deep
theorems is represented by an added axiom in this Lean build; those arguments
are outside its stated scope.

The latest source intake is recorded in [THIRD_INTAKE.json](THIRD_INTAKE.json).
Earlier bulk computations were not replayed.
