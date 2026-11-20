# Independent review of the ternary stationary boundary

**Verdict: VERIFIED at the stated elementary claims TM1--TM5;
VERIFIED AS A SOURCE-QUALIFIED CONSEQUENCE at TM6.** This is internal
agent review, not human referee acceptance or formal verification. No
ordinary approximation theorem or Collatz proof is verified here.

Reviewed source: `TERNARY_STATIONARY_BOUNDARY.md`, SHA256
`543c0bd7a72d5dec598898850a49a257a9ef3b55cd1fff8741d8699fbad57a7c`.
The source was read in full. The independent checker uses rational Gaussian
elimination, not the author's cyclic stationary recursion.
The review verdict covers TM1--TM6. The added TM7 was contributed by
this reviewer and requires a different author's independent review;
its authorship is not counted as an independent confirmation here.

## Claim reconstruction

**TM1.** A common length-`N` coin word has slope `3^j/2^N`, where `j`
is its count of `F_1` moves. Thus `j>=s` really does synchronize every
pair of states modulo `3^s`. At `N=4s`, applying the elementary Markov
inequality to `3^-J` at threshold `3^{-(s-1)}` gives precisely
`(16/27)^s/3`. Stationary existence is finite-state compactness;
the same coupling proves uniqueness. Multiples of three lose all their
mass unless every coin is zero. Multiplication by two cycles through
all finite ternary units, so the remaining closed class is irreducible.
These facts establish the stated support, consistency and normalization.

**TM2.** For `pi(A)<=1/2`, the `4s`-step exit probability from a point
of `A` is at least `1/2-16/81=49/162`. Under the stationary initial
law, every path ending outside `A` after starting inside it has at
least one outward crossing. Its probability is therefore at most
`4s` times the stationary one-step outward flow. This yields the stated
cut constant `49/(648s)`. Inward and outward flow are equal without a
reversibility assumption. Integrating the cut inequality over the real
level sets produces exactly the coefficient `648s/49` in the pairwise
oscillation inequality. The source correctly restricts the coarea claim
to real labels and uses the stationary, rather than uniform, weight.

**TM3.** The ordinary comparison has no replacement of a fixed source
by an independent parity sequence. Oddness of the conductor guarantees
that periodic source weights see the two source parities equally.
For even sources, stationarity gives `pi(2m)<=2pi(m)`, so the cutoff
`m<=X/2` contributes at most `delta`. For odd sources, the actual
image is injective and lies below `3X/2+O(1)`; its incoming stationary
weight gives `pi(n)<=2pi(Tn)`, hence at most `3delta`. Adding the
source error produces `5delta`. No division by a stationary weight
occurs, so the zero weights on multiples of three cause no gap. The
upper-limit argument handles the bounded change in the cutoff by using
that changed cutoff in the same defining limsup.

**TM4.** The sum of incoming odd-branch weights is the marginal at the
unique residue modulo `3^(s-1)`, which proves recursion (5). The unit
cycle then gives (6) by a finite geometric sum. After multiplying by
`3^s`, the branch density factors are exactly `1/2` and `3/2`.
Their squared diagonal integrals are `R_s/4` and `3R_(s-1)/4`, and
the cross coefficient is `3/2`. Rearranging proves
`R_s-R_(s-1)=2I_s`. Positivity on `2,8 mod9` verifies strict increase
for `s>=2`; the first level is direct. The all-one word gives the lower
atom bound, and summing only one parity of geometric weights gives the
upper atom bound. The bounds are not statements of uniform Haar density.

**TM5.** The proposed contradiction for an `L^2` density is sound.
The pointwise stationary equation makes its positive support invariant
under multiplication by two modulo Haar-null sets. The inclusion becomes
equality because multiplication by two preserves Haar measure. Finite
unit quotients are single cycles; conditional expectations therefore prove
ergodicity on the units. A nonzero nonnegative density must consequently
be positive almost everywhere on that whole unit set. Squaring the
stationary equation gives diagonal coefficient `1/4+3/4=1`, so its
nonnegative cross integral would have to vanish. Both factors are
positive almost everywhere on `2,8 mod9`, a positive-measure set.
Cauchy--Schwarz makes the integral finite under the assumed `L^2`
hypothesis; hence the required vanishing is impossible.

The final implication from bounded `R_s` to an `L^2` stationary
density also retains the necessary hypothesis: consistency makes the
step densities a martingale, so their squared distance is
`R_t-R_s`. Boundedness would make them `L^2` Cauchy and preserve
every cylinder integral. Thus `R_s` diverges. This argument neither
requires nor proves the imported `L^1` assertion.

**TM6.** I independently opened the published Cambridge article by
Terence Tao, *Almost all orbits of the Collatz map attain almost bounded
values*, DOI [10.1017/fmp.2022.8](https://doi.org/10.1017/fmp.2022.8).
The normalization and stationary process in Remark 1.13 agree after the
geometric waiting-time regrouping. Equation (1.23) gives consistency;
Proposition 1.14 and its oscillation definition (1.27) give the claimed
`L^1` Cauchy estimate for these step densities. Therefore the inference
to an `L^1` density is valid, and combining it with TM5 gives
`L^1\L^2`. This review checks that use of the published theorem; it
does not reconstruct Tao's complete Fourier argument. The article's
modulo-nine distribution also agrees exactly with the independent linear
system below. No claim of new priority for the stationary measure is made.

**TM7 contribution, separate from the independent verdict.** This reviewer
supplied the bounded-error comparison by splitting `g_s=g_m+(g_s-g_m)`.
For `0<=e<=1`, the periodic remainder is bounded by its full `L^1`
average regardless of the ordinary error's residue distribution.
The finite bound `g_m<=2^m` and the imported fine-scale estimate give
`delta_s(e)<=2^m delta_H(e)+C_A m^-A`, uniformly in the conductor.
Choosing `m` proportional to `log(1/delta_H)` gives the uniform
inverse-logarithmic modulus and the stated stretched-exponential
consequence. The same estimate holds at finite cutoffs divisible by the
fine modulus. This positive transfer does not construct the required
approximation or prove pointwise minority mass. A separate root review
should cover TM7 before it is described as independently reconstructed.

## Independent finite execution

`review_ternary_independent.py` was executed in normal and optimized
Python. Both executions returned `PASS` with identical report bytes:
SHA256 `774963d2c6d2f22d36bf0ebd68d30804f617618cbb104bf68e6433f7db2a0410`.
Actual commands and execution intervals are recorded in
`ternary-independent-execution.json`; the result is
`ternary-independent-report.json`.

The independent algorithm solves `pi K=pi` and `sum pi=1` as rational
linear equations on each unit class for moduli `3,9,27,81`. It then
checks full stationarity including zero-weight states, projective
consistency, the norm identity, the atom bounds and the binomial bound.
All 520 subsets of the full state spaces modulo 3 and 9 are checked
against the conductance constant. The first square norms are

\[
R_1=5/3,\quad R_2=15/7,\quad
R_3=177005/67963,\quad
R_4=6626070796594781675/2159281421340253987.
\]

These finite computations do not establish the infinite `L^2`
contradiction or the imported fine-scale mixing theorem; their purpose
is to check the normalization, coefficients and finite algorithm by
a different construction.

## Remaining boundary

No defect was found in the reviewed mathematical statements. The
closing ordinary source estimate remains absent: quotient mixing does
not control the weighted approximation error of an actual component
indicator. The `3x-1` conjugacy and its distinct positive cycles correctly
demonstrate this distinction. Later wording or neighboring claims are
outside this hash-specific verdict. The elementary finite checks were
first run against the pre-TM7 source hash
`55fde4bbef8dfe02c40c48572475791082aa2a160ccd71b07ce5091595238caf`;
TM1--TM6 are unchanged in the revised note. The execution receipt retains
that original hash honestly, while this written review identifies the
revised full note and its separate TM7 authorship.
