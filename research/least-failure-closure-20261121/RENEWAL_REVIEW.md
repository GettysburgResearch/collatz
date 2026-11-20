# Independent review of the expanded renewal and density budget

**Disposition: VERIFIED at the narrow written-claim level below; no
mathematical gap found.** These remain proposed research statements.
The reviewer is the primary AI agent, separate from the energy author.
This is not external peer acceptance, a formal proof, or a finite-energy
bound for a hypothetical nonconstant Collatz invariant.

## Frozen targets

| Artifact | SHA-256 |
| --- | --- |
| `EXPANDED_FIVE_RENEWAL.md`, ER1–ER4 | `3589ca1bcf2533bc7cbd427feb0d8f830cc077c3a6e90d2a7abd6eeef3ffd70b` |
| `DENSITY_CONGESTION.md`, DC1–DC3 | `51849fd915649590157d5eac7c7336ac2f06f9d3673f306ab3def32b76a842da` |
| `check_expanded_renewal.py` | `4edb327ad20391e4124db1146eddde96d7c033ed014b9ea172bcf05c92f29ad6` |
| `expanded-renewal-report.json` and optimized companion | `0269c59ed42793d9ebc918d0a0ace065a8df3dabdecde78b47006cfb953bb2f3` |
| Independent `check_renewal_review.py` | `923a36f93af1bf2065e172a25e4ed1d06cbef9641df2d519f42382abf257afe7` |
| Both `renewal-review-report` files | `fa38464b1522d5b2c50c2aaa60f000cc022071f1ec1dbe5183582c293b9403ce` |

The reviewer read the complete written proofs and author checker, and
independently reconstructed the formulas below. The independent finite
checker imports no author code. Normal and `-OO` execution both passed
and produced identical complete reports.

## ER1: actual blocks, domain, and height

The three source corrections are `65,73,121`; the target corrections
are exactly five times these. All target terminal exponents are positive
under the stated guards. Full inverse numerator divisibility recursively
proves each intermediate division by three integral. Every resulting
state is positive and odd, which makes the actual division exponents
exact. This justifies physical paths, not only a rational endpoint identity.

The reviewer independently reconstructed the arbitrary-exponent HT3
classification and the three cylinders. The cylinders are pairwise
disjoint, begin with valuation one, and avoid the old ladder, which
begins with valuation two. Their endpoint-height estimate `q<=x/3` is
valid even at the least positive source in each class. Adding their
relative odd-source masses `1/256,1/128,1/512` to the old ladder's
`1/24` gives `85/1536`. Natural density uses the old ladder's controlled
infinite tail; the argument is not applied to a general countable cover.

## ER2: the full infinite inverse fibers

For a fixed endpoint `q`, the old ladder's inverse exponents form one
class modulo `2*3^r`. The positive correction means each later source is
at least the corresponding power of two times the first source. The
resulting geometric denominator therefore bounds the full infinite fiber.

The common residue `c=q mod81` fixes the relevant least exponents for
`r=1,2,3`. Replacing `q` by its least positive odd representative at least
5 enlarges every ratio. For `r>=3`, the exact identity

\[
x_b=1+(4/3)^r(2^bq-4)/3
\]

gives the geometric tail in `r`, while every exponent period is at least
54. The three new families also have period 54. Thus all six positive
pieces must be added at the same endpoint residue before taking a maximum.
No independence between families or source-unit exclusion is presumed.

The separate review checker reconstructed all 54 coefficient rows with
`fractions.Fraction`. For exponent `21/25`, it enclosed each power on a
`10^12` grid, independently of the author's `10^9` grid, using exact
25th-power integer comparisons. It verified coefficients below `5/8`,
`91/100`, and, after adding the high-valuation fiber, `7/8` on every
residue. No floating-point rounding supports these inequalities.

## ER3–ER4: cutoffs, charges, and finite limits

Every covered source has an actual endpoint below `X/3`, and ordinary
invariance gives exactly `e(x)=e(q)`. Grouping nonnegative terms is valid
without assuming finite total energy. Subtraction is performed at finite
cutoffs, where every term is finite, before taking monotone limits. This
proves the stated equivalence of full and uncovered energy finiteness.

For every first valuation `a>=3`, two literal shortcut steps from `5x`
give `5*2^(a-2)q-1`. The other endpoint `5*2^(a-2)q` has label `f(5q)`.
The triangle inequality yields the exact adjacent charge in ER4. Its
source weights, multiplicities, and cutoffs are retained in `J(X)`.

These high-valuation sources are disjoint from the entire old and new
transport domain, whose first valuation is one or two. Their first legal
inverse exponent is 3 or 4 according to `q mod3`, with period two; the
same positive-correction argument bounds their full fiber. Also `q<=x/2`.
The zero-defect endpoint `q=1` may be omitted from the transported `e(q)`
sum, but its adjacent charges remain in `J`. All these conventions agree
with the written inequality.

One wording correction was requested and incorporated before the frozen
hash: declaring the adjacent charge zero **for every ordinary invariant
label** would assert the corresponding convergence transfer. For one
fixed constant label it says nothing about convergence. No such universal
zero-charge theorem is claimed.

The first unresolved assertion is finiteness of the remaining all-source
energy. The harmonic rigidity consequence in PR163 also retains its
separate PD input; the subcritical consequence retains its predecessor
moment input. The elementary renewal inequalities neither assume nor
establish these global interfaces.

## DC1–DC3: density and the architecture limitation

A word with `p` odd inputs and shortcut clock `L` has one source residue
modulo `2^(L+1)`, of relative odd-source mass `2^(-L)`. Integrality fixes
one unit endpoint residue modulo `3^p`; exactly two of its three lifts
modulo `3^(p+1)` have a ternary-unit source. The legal endpoint fraction
is consequently `3^(-p)`. Positivity removes only finitely many endpoints.

The asymptotic inverse ratio is `3^p/2^L`. For a finite family, multiplying
each exact residue fraction by its limiting ratio proves the mean-kernel
formula. At exponent one the mean is exactly the sum of binary cylinder
masses. The independent checker enumerated all ternary lifts for 11
specified words and verified this exact normalization, rather than
approximating an empirical mean.

For an infinite family, every finite partial sum inherits a hypothesized
uniform positive column bound. Taking the supremum of these finite means
is legitimate by nonnegativity; no unproved interchange of infinite
averages is used. A uniform endpoint contraction yields the stronger
subcritical factor stated in DC3.

The final qualification is essential and correct: a countable union of
binary cylinders can contain every positive ordinary integer yet have
arbitrarily small Haar mass. The proof constructs such a cover directly.
Therefore the mean identity rules out the stated strict uniform kernel
bound for a Haar-full cover, not for every all-ordinary-source compiler.
Nor does it prohibit estimates exploiting the support of an actual
invariant label's defects.

## What the verification establishes

The written reconstruction supports the universal formulas and their
quantifiers. Exact finite checks certify the numerical constants, residue
normalizations, and selected physical controls. The checks are not a
proof of Evertse's theorem, a census proving Collatz, or a bound on the
uncovered energy. No accepted baseline status is changed by this review.
