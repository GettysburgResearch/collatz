# Independent reconstruction and research boundary

24 November 2026. Repository: GettysburgResearch/collatz. The branch starts at main
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. See `SOURCE_HEADS.json` for the twenty
freshly queried source PR heads. A head inventory is not a proof review of every
file at those heads. This report records the particular arguments reconstructed
in this investigation. It does not upgrade neighboring results or later commits.

Three separately tasked GPT-6.2 Astra agents worked on stationary/carry analysis,
cycle arithmetic, and formal verification. The root reconstructed their new
arguments and the interfaces below. Separate instances of the same model can
share an error; the recorded proofs, exact controls, source changes and compiler
receipts are the evidence. No human referee or independent Lean kernel is claimed.

## Bounded births and ordinary occupation

**Verdict: independently reconstructed written proof**, conditional only on the
specified actual-scalar theorem and, for the stated corollary on canonical prefix
growth, the specified whole-orbit correction-product bound. The finite new Lean
cores have their own narrower execution record.

The stationary agent first counted positive carry prefixes on runs of canonical
digit one. The root then strengthened the count by retaining the allowed size of
a carry immediately after zero. Both mathematics agents independently checked the
stronger transfer estimate. For `0<x<1/2`, put
`D=(1-x)/(1-2x)`, `f(0)=1`, `f(c)=D*x^c` for positive `c`, and `lambda=1+D*x`.
The total of `f` is exactly `D`. At a positive current carry one may enlarge the
next-carry range to all nonnegative integers. At zero the three actual digits
permit only `{0}`, `{0,1}`, or `{0,1,2}`. This gives the respective operator
factors `1`, `lambda`, and at most `lambda^2`. Positivity of every operator
justifies iteration; `f(c)>=x^c` supplies the terminal weight. No independent
randomness assumption is involved.

For the entropy estimate the window contains **m+1** carries. The last carry has
bounded mean because the window is sampled from an actual injective prefix, and
the summed logarithmic potential bounds the sum of all carries. The cancellation
at `-log x=2 log lambda` uses the actual mean of `2*carry+canonical digit`. It
does not replace the ordinary empirical law by a product law. The extension to
all window lengths is a separate use of the entropy of the finite sample index
above logarithmic resolution. It is not a new rate theorem for an arbitrary
stationary weak limit.

For occupation below X the root independently recovered the complete terminal
carry from the total binary clock, initial phase, and the **first m** carries.
The weighted count must therefore be applied to m vertices and m-1 edges. It is
bounded by `D*lambda^(B-m)`, since the omitted final digit has nonnegative cost.
The scalar bound at the actual endpoint gives the first-m carry budget and
cancels B from the exponent. The other bound is the unrestricted positive
composition count. Splitting at `A/m=23/20` makes both bounds strictly smaller
than `X^0.6799`, before absorbing the logarithmic number of clocks into `X^0.68`.

The high-clock lane needs injectivity of `U` on the entire invariant set S. It
counts distinct sources by distinct endpoints below X/2. A predecessor basin
does not inherit this premise. The dyadic source congruence and ternary endpoint
congruence serve different steps of the proof and have not been interchanged.

The root additionally combined the entropy height bound with PR182 R12-1 at
`cbec52dde5bed390a693310dd04e911033ba0cc9`,
`research/phase-packing-round12-20261124/README.md`, section 2. That pointwise
comparison removes the extra factor N in the older drawup-to-height estimate.
For zero canonical factor entropy, the necessary polynomial exponent for the
canonical prefix maximum is consequently at least `3.49822161875...`, rather
than only `2.49822161875...`. The special critical-mean branch of R12-2 already
has a stronger superpolynomial conclusion and retains that credit.

## Top cyclotomic component

**Verdict: independently reconstructed written theorem with the stated classical
irreducibility input.** The source interface is PR191 TCP-4, not a blanket
verification of that PR or of a full numerical denominator saving.

The root checked the grouping of odd-position indices modulo b. Each row has
coefficients `2^(d_(i+jb)-a*j)`, and adjoining a root of the top polynomial gives
the cyclotomic field as a subfield. For odd g, the order discriminant is odd
because `X^g-1` is squarefree modulo two. The integral valuation at a prime above
two then shows that every monic factor degree of `X^b-2^a/w` is divisible by b.
This proves the required extension degree without assuming the conclusion about
the itinerary.

For a prime-power g, divisibility of a degree-below-g row by its cyclotomic
polynomial repeats its coefficient block. Equality of the powers of two is
exactly the positional translation by `A/ell`. Conversely an ell-fold word
repetition supplies that translation. For powers of two, the rational binomial
criterion leaves precisely the exceptional case `g=4` with even b. The root
opened and checked Theorem 1 of Koley--Reddy, arXiv:2006.03787v1, including the
exception `4|n` and a negative four times a rational fourth power. The source is
linked in the proof; it is an external algebraic theorem, not a new Lean result.

The mixed-prime construction was checked by its three coefficient rows. Two
distinct prime divisors give two indicator cosets with incompatible nontrivial
periods. All rows vanish at each primitive g-th root, while their common period
cannot be shorter than g blocks. Thus an entire top factor can cancel in a
primitive word. Each five-step block is contracting; its exact fixed-center
interval and the first two gaps at block zero exclude an integer boundary.
The explicit g=4 example cancels only one of the two quartics. These are literal
positive rational cycles, not proposed integer counterexamples.

The result classifies which clock gcds guarantee nonvanishing for **every**
primitive candidate word. It does not say that all words at a remaining gcd
have zero determinant. Nonvanishing alone does not bound the determinant below
the numerical factor, and cancellation of one factor does not cancel the full
cycle denominator.

## Latest phase-packing round

At PR182 `cbec52dde5bed390a693310dd04e911033ba0cc9`, the root reconstructed
`research/phase-packing-round12-20261124/README.md`, R12-1--R12-3.

For R12-1, the local carry inequality at exponent `log_3(4)` is exact at
`next=3*current+2`. In the decreasing-carry case its proof follows from
`current+1<=2^current` and `log_3(4)<=2`. The full actual multiplicative
correction is bounded by the pinned whole-orbit sparsity result. Combining the
local telescoping inequality with that product gives the pointwise canonical
prefix lower bound at every clock of the same orbit.

For R12-2, summing m+1 carry costs over all past windows costs at most m+1 times
the total cost. The low-cost window count uses one ordinary endpoint per ternary
residue only because the chosen precision exceeds the height threshold. The
remaining fraction is bounded by Markov's inequality. The canonical complexity
and mean hypotheses are retained; no universal complexity upper bound follows.

For R12-3, the guarded normalized state satisfies a genuine affine comparison
with the periodic canonical trajectory. Contractivity makes the burn-in finite.
The cubic guard converts the bounded normalized state into a bounded integer
state. A repeated integer state then provides a literal cycle whose rational
scalar can be compared exactly with the propagated candidate. Rejection before
burn-in remains a sound branch. This is a decision for supplied rational
candidates with **contracting** eventual phase. It does not decide arbitrary
low phases or scalar membership in general. The bounded graph control excludes
only cycles wholly confined to the stated interval.

## Binary substitution extension

**Verdict: independently reconstructed written proof**, with a second frozen
cross-review. The root checked PR190 MPS-1--MPS-6 at `ba58227c5a047ff3859a148a5fdaac4fd1451e4c` and the new
extension in `MAHLER_EXTENSION.md`. For a reducible binary substitution, the
incidence matrix is triangular after renaming letters. The faster pure-image
case supplies a positive dominant eigenvector directly, so the original
nonvanishing argument applies without primitivity. When the mixed coordinate
dominates, the root checked the auxiliary-polynomial dimension count over
`Q(Y)` and the order of limits: choose its degree first, then let the iteration
grow. Its unrestricted Y degree costs only `o(V_n)` in height. All X-coefficient
polynomials evaluate integrally, controlling the infinite tail.

When one letter is fixed, the root separately reconstructed the zero-clock
recurrence and its digit-multiplicative normalization. An algebraic solution of
`H(z)=P(z)H(z^a)` has a rational power, by the constant coefficient of its monic
minimal polynomial. Pulling the divisor back through the power map forces all
orders to be divisible by that power; hence H itself is rational over the
algebraic closure. Rationality and `f_(a*n)=f_n` force the finite set of
exponential bases to be permuted by powering: cardinality rules out hidden
cancellation when bases collide. The resulting polynomials are constant.
Positivity of the digit weights then forces every weight to be one, making the
original binary word periodic, a contradiction.

This argument proves formal transcendence at the required specialization before
the physical auxiliary-polynomial argument. It does not equate a real root used
for formal normalization with a 2-adic analytic limit. The diagonal and
imprimitive binary cases are accounted for; excluding the identity substitution
is essential. The theorem does not cover arbitrary binary codings of larger
substitution alphabets.

## Inverse tree and shadow classification

The root checked the full finite invariant relation against the table: division
by three loses one ternary digit, so the input uses a lift modulo 81 and the
output is constrained modulo 27. Since every next carry lies in [6,16], every
actual inverse edge has gap in [4,50] and strictly increases the positive source.
All scalar identities are finite extensions of the known value at one. The
probability argument for the lower source count uses costs, not actual
multipliers, with a finite stopping cut; its endpoints are distinct by
determinism of the forward map. The stated exponent does not refute the numeric
0.68 upper bound for a general basin; it refutes the endpoint injection used in
this particular proof.

For the eight shadows the root solved both coefficient equations directly.
The four slopes below one all have denominator 83 and the same integer offset
after writing the map as `lambda*(q+7)-5`. Only the slopes 60/83 and 61/83 beat
the intermediate ordinary-state floor for every positive q. Full odd endpoint
parity forces each of the two prescribed gaps. An infinite image cannot hit
one because neither permitted target block is the all-two block. The comparison
still applies only to the minimum within the specified tail.

## Earlier stationary theorem and attribution

PR189 S1 at `a0be70b1ffa075cbc50755ac76036108c028d120` rederives the strict
stationary collision-gap theorem already present in PR180 at
`7cfd911d35382d9d3bc988060ba88ade78a4267e`,
`research/whole-source-20261123/COLLISION_CORE.md`, sections 3--4. Its novelty
description must be corrected. PR189 explicitly states the weaker sufficient
contrary hypothesis using upper, rather than lower, collision dimension; that
is an immediate corollary of PR180's own strict upper-dimension conclusion.
The separate stationary review identifies the exact finite-window and equality
case scopes. The new birth-constrained bounds are distinct from this duplicate.

## The attempted closing steps still fail

For escape, the new estimates force a low-complexity hypothetical orbit to attain
large heights and large canonical coefficients. They provide no opposing bound
for an arbitrary ordinary source and no proof that its scalar is rational or
its canonical factor complexity is subexponential. Finite congruence witnesses
may change with the horizon; they cannot supply one all-time positive source.

For cycles, the top-component classification supplies a nonzero component in
specified cases and explicit primitive cancellation examples in the others.
It supplies neither a universal strict numerical gcd saving nor a complete
smaller-source construction. The exact affine-shadow and inverse-tree studies
record why two natural attempts to bridge these gaps do not close them.

These are remaining mathematical steps, not missing finite test coverage.
The repository continues to have no proof of full Collatz and no verified
positive counterexample.
