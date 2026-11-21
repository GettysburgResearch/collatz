# Independent review: critical likelihood tilt and the singular Green carrier

**Verdict:** the revised written arguments CT-A through CT-D are sound at
their stated scope. They do not prove an ordinary fixed-source decay
estimate, exclude an infinite ordinary trajectory, or exclude a nontrivial
positive cycle. This is a mathematical review of paper proofs, not a Lean
execution receipt.

## Exact reviewed sources

| File | SHA256 |
| --- | --- |
| `research/literature-reframe-20261122/CRITICAL_TILT.md` | `5837337aa29c6c67776a62d21accf216513b0e6da8d358870e6f5b79ebdf4e71` |
| `research/reframe-20261121/GLOBAL_MASS.md` | `212999316311aa1e6b79b764b4686828fc36b5e49e6c211f5cc6931791fb1472` |
| `research/reframe-20261121/GREEN_FRACTIONAL_MOMENTS.md` | `b54169b4ee8f2530688984d9816872eebff88cc668a34710506bbc4ad7caaf6b` |

The first draft reviewed had hash
`f56c714538b1c607431c111e7895d6ca9d1ef628f32bf66cc4df2ad5b51c1fc4`.
Review identified an opportunity to establish the exact likelihood
endpoint, and a quantifier issue between odd ordinary units and all
positive ordinary units. Both were resolved in the pinned revision above.

Primary-source interfaces independently opened were Tao's
[publisher text](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F),
particularly Proposition 1.9, Lemma 1.12, and Remark 1.13, and the
[Diaconis--Freedman author preprint](https://www.stat.berkeley.edu/~census/511.pdf),
Theorem 1 and Proposition 1. The new computations below do not require an
unproved strengthening of those sources.

## 1. Likelihood normalization and the exact CT-B boundary

The one-letter probability ratio is exactly
`(3/4^a)/(1/2^a)=3/2^a`; hence its product is the derivative `J_r`.
Both probability sequences sum to one. Their respective means, two and
four thirds, give the two opposite logarithmic drifts in CT3.
The moment identity

\[
M(s)=\sum_{a\ge1}2^{-a}(3/2^a)^s
=\frac{3^s}{2^{s+1}-1}
\]

has the correct factor and no omitted normalization. At `s=1`, its value
is one and its logarithmic derivative is
`delta=log3-(4/3)log2`. Holder's inequality therefore proves the stated
transfer when the exponential rate `c` is strictly larger than `delta`.
This assertion is about one event under two finite product laws; it does
not identify that event with an ordinary survivor set.

The initial fixed-width typical band proves failure of any threshold
strictly below `delta`. It alone did not establish failure at the exact
bound `P(E_r)<=C exp(-delta r)`. The revision now does so: for

\[
E_r^*=\{\log J_r\ge\delta r\}
=\{A_r\le4r/3\},
\]

the reverse likelihood identity gives `P(E_r*)<=exp(-delta r)`.
Under `Q`, the gaps have variance `4/9`, so the ordinary central limit
theorem gives `Q(E_r*) -> 1/2`. The lattice nature of `A_r` does not
change this limit: the standardized cutoff differs from zero by at most
one lattice spacing, which tends to zero. Thus strictness of the
threshold `c>delta` is now justified even at the endpoint.

The bounded stopping claim also checks. Every gap is at least one,
so `tau_L<=L+1`. Decomposition by the stopped finite word proves the
likelihood formula directly; bounded optional stopping is also applicable.
No unbounded-time uniform-integrability assertion is used. In fact CT-A
correctly proves that the martingale is not uniformly integrable.

## 2. Adjoint factor, composition direction, and stationary law

The relevant Haar measure is additive Haar measure restricted to
`X=Z_3^times` and normalized by its total mass. Since multiplication by
`3/2^a` has ternary absolute value `1/3`, the image of a measurable subset
of `X` has one third of its measure. Restriction and normalization do not
change that ratio. Multiplying the pressure coefficient `9/4^a` by this
Jacobian produces exactly `3/4^a`, the claimed Markov probability.

The coding order is consistent throughout. For the backward composition
`R_(a1) o ... o R_(ar)`, the constant term is
`sum_(j=1)^r 3^(j-1)/2^(A_j)`, and the remaining coefficient is
`3^r/2^(A_r)`. This tends to zero ternarily for every sequence. The
normalized tail after removing a finite prefix is itself a unit: its first
term is a ternary unit and its later terms are divisible by three. Thus
the limiting point belongs to every corresponding word domain `E_w`.

Separating the first letter proves stationarity of `pi_*Q`. Coupling two
forward chains with the same letters contracts their distance by `3^-r`.
Compactness then gives uniqueness and weak convergence. The distribution
of a finite backward composition equals that of the forward composition
because the letters are independent with the same distribution. The note
correctly confines this reversal to the random model and does not apply
it pathwise to a fixed ordinary orbit.

## 3. Green growth, singularity, and the dimension carrier

Expanding `P_2^r` gives the asserted words in precisely the same composition
order as the coding. Each domain has measure `3^-r`, even though different
domains can overlap. Neither the expansion nor the fractional-power bound
requires disjointness. The coefficient sum is finite at every depth, so
the nonnegative expansions and integrals are legitimate.

The fractional Haar estimate in CT14 is the same calculation as GF1 in
the pinned previous note. It supplies a finite positive fractional moment
of `G`, hence `G<infinity` almost everywhere for Haar measure. For a
`Q`-typical coding, its own prefix contributes

\[
F_r(\pi(a))\ge9^r/4^{A_r}.
\]

The strong law now gives the exponent
`2log3-(8/3)log2=2delta>0`. This is a statement for every point in the
image of a full-measure set of codings, so it becomes a `nu_2`-almost
everywhere statement even when the coding is not injective. The measurable
growth set can itself be used to avoid any measurability concern about
the image. Singularity follows from the disjoint full-measure conditions
`G<infinity` and `G=infinity`. It is not inferred solely from densities
tending to zero, which would be insufficient in general.

The entropy computation is
`H(q)=(8/3)log2-log3`; thus `log3-H(q)=2delta`, consistent with the
growth exponent above. The dimension argument uses a finite collection of
prefixes at each depth: there can be at most `exp(r(H+epsilon))` prefixes
whose individual probabilities are at least `exp(-r(H+epsilon))`.
Each domain is contained in a ternary ball of diameter at most `3^-r`.
For any fixed time `N` after which the probability condition always holds,
these balls cover the corresponding eventual coding image at every
`r>=N`, with vanishing total `d`-power of diameters when
`d>(H+epsilon)/log3`. Taking the countable union over `N` and then a
countable intersection as `epsilon` decreases gives a full-measure carrier
with the stated dimension upper bound. No separation condition for the
branches and no claim of exact dimension are required.

The word *carrier* matters. This is a full-measure measurable set; the
argument does not assert that the topological support excludes the dense
set of positive ordinary units.

## 4. The CT15 ordinary boundary and the resolved parity quantifier

For a positive odd integer target `t`, a legal inverse child
`(2^a t-1)/3` is a positive odd integer. Its oddness ensures that the
actual accelerated gap is exactly `a`; the ternary guard ensures that the
child remains a unit. Iterating therefore identifies the compact column
with the actual ordinary column. The first-hit/cycle bound G10 proves
its all-time Green sum finite at every such target, including periodic
targets.

This exact identification initially covered odd targets. For an even
target, ternary legality by itself does not make `a` the actual accelerated
gap: the extra two-adic factors in the target must also be removed. The
revision now handles this distinction without asserting a false column
equality. If `t=2^b u` with `u` odd, then

\[
I_a(t)=I_{a+b}(u).
\]

Sending the first exponent of a length-`r` inverse word from `a` to `a+b`
injects its legal words into those at `u`, and multiplies its coefficient
by `4^b`. Therefore `F_r(t)<=4^b F_r(u)` for `r>=1` and
`G(t)<=1+4^b(G(u)-1)<infinity`. The stated exclusion of every positive
ordinary ternary unit from the divergent Green carrier is now justified.

## 5. Real perpetuity and remaining scope

Under `P`, the negative logarithmic drift makes the positive real series
converge. Splitting its first term gives the correct affine stationary
equation. The Diaconis--Freedman hypotheses are met on the complete metric
space `[0,infinity)`: expected Lipschitz constant is one and finite,
expected displacement at zero is `1/3`, and expected log Lipschitz
constant is negative. Their theorem requires the logarithmic contraction,
not a strict inequality for the mean Lipschitz constant.

Subadditivity proves every moment below one finite with the displayed
constant. Tonelli makes the first moment infinite; `x<=1+x^theta`
then covers all larger exponents. Under `Q`, positive real terms grow
exponentially while the ternary series still converges. These different
completions need not have the same rational value, and the note makes no
such identification.

Finally, Tao's primary text uses the geometric law `2^-a` and explicitly
states finite-scale distribution hypotheses before transferring it to
ordinary sources. CT-B does not erase those hypotheses. Neither the
singular stationary measure nor its entropy carrier controls one fixed
ordinary source after its dyadic residue budget has been exhausted. The
completion interface in the note remains unproved, exactly as stated.

No Lean process was run for this review. No additional formal validation
is claimed for CT-A through CT-D or for the inherited analytic estimates.
