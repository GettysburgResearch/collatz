# Complete visitor clocks, finite-state cycle counts, and local energy obstructions

**PROPOSED research; Collatz remains open.** The earlier finite selectors
now yield ordinary protection against complete smaller orbits on growing
families of targets. A general finite-state counting argument gives a
global cycle census. A separate obstruction rules out several broad
classes of one-edge escape certificates. These are written proofs with
finite controls and explicitly limited kernel consumers.

## Removing the visitor clock bound on a growing target family

Put `s=284051/829440>1/3` and `s₀=1041139/4147200>1/4`.
The [all-clock scaled-target theorem](descent/postpeak/allclock/SCALED_TARGETS.md)
proves that at least `(s−o(1))X` integers `n∈[X,2X)` have no smaller
positive visitor to **any** integral target

\[
 Y=2^\delta(3/2)^j(n+1)-1,
 \qquad j,\delta\ge0,\qquad 2^\delta(3/2)^j\le X^{1/50}.
\]

At least `(s₀−o(1))X` protected starts are multiples of three. Both
proportions are normalized by the whole shell. The conclusion includes
all `j,δ≤(log₂X)/80` simultaneously and allows every finite visitor
clock. It does not assert a simultaneous result for all scales at a
single fixed integer.

The new finite-size form of Weaver 177's long-arrival estimate is

\[
              |E_J(Y)|\ll Y2^{-J/25}+Y^{49/50}.
\]

Here `E_J(Y)` consists of targets at most `Y` reached after time `J`
from a positive source at most `Y`, with all intervening states at least
that source. The proof uses ordinary orbit-image compression and an
entropy tail, and does not assume termination. If a protected source
still has a smaller visitor, choose the target's least positive ancestor.
Its first arrival stays above that ancestor, so this estimate applies.
The affine target map is injective for each scale pair. Taking
`K=floor((3/5)log₂X)` and summing the `O(log²X)` possible pairs costs
`o(X)`; the two relevant exponents are `249/250` and `2499/2500`.

## An all-clock classification after a long odd ascent

For the original physical word `O^H w`, write `t=|w|`, let `f` and `q`
be its odd and even counts, and set `C_w=A_w−3^f`, where
`2^t T_w(x)=3^f x+A_w`. Call `w` maximal if no word of the same length
and signed offset has more odd letters.

The [postpeak theorem](descent/postpeak/allclock/POSTPEAK_VISITORS.md)
classifies the two cases when `H≥600` and `t≤H/100`:

- Every nonmaximal word has an explicit positive smaller visitor at its
  endpoint for every source in its native dyadic cylinder.
- Every maximal word protects more than one third of that cylinder
  against every smaller positive visitor through the entire original
  segment, with arbitrary visitor time. More than one quarter of the
  whole cylinder consists of protected multiples of three.

The density statement first fixes `H,w`. The note also proves a uniform
finite-shell version: for all sufficiently large `X`, the same strict
fractions hold in each such cylinder inside `[X,2X)`, simultaneously
for `600≤H≤(log₂X)/100` and `t≤H/100`.

A stronger symbolic statement gives protection at least

\[
        s-5\,6^t4^q2^{-\lfloor H/12\rfloor}
        \quad\text{when }H\ge12(t+2),
\]

with `s₀` replacing `s` for the zero class. Stop a competitor's reverse
path at the `H+f`-th odd inverse. If this suffix has few even steps,
the signed trap forces its integer shadow to end at `−1`; equal-offset
maximality then sends it to the same common-scale protection set.
The number of long-even suffixes is bounded by their signed origins,
and the squared-gain stopping estimate makes their remaining mass
summable. Finite reverse deadlines transfer to actual sources before
the long-arrival estimate removes the deadline. This order avoids
assigning an ordinary natural density to an arbitrary ternary closed
set without proof.

There are at least `binom(t,floor(t/2))` maximal words: equal weights
have distinct signed offsets, by the native parity bijection. Hence
the protected fraction conditional on the first `H` odd letters is
at least one third times `2^(−t)binom(t,floor(t/2))` in the stated range.
The next bit is not separately conditioned to be even.

Weaver 178's stronger pure-ascent proportion is credited. The new
classification covers the postpeak language and its ordinary all-clock
transfer. It shows why a universal smaller-merger claim restricted to
these segments cannot follow from merely raising the visitor budget.
A later merger beyond the segment remains possible.

## Finite-state words and a census across all positive cycles

The [general language theorem](cycles/phase7/FINITE_STATE.md) applies
to a primitive right-resolving finite parity graph with a positive
critical tilt `z>1`, stationary odd frequency `p*=log₃2`, and entropy
`h∈(0,1)`. If an ordinary set is forward invariant, is accepted by this
graph, and has uniformly bounded fixed-time multiplicity, then every
interval of length `X` contains `O(X^(h−γ))` of its states for some
fixed `γ>0`.

The union of all accepted cycles has multiplicity one. Each individual
divergent orbit also has multiplicity one. A union of arbitrary divergent
orbits need not satisfy the hypothesis. The proof obtains canonical
source concentration from Markov bridges, discarding exponentially rare
local types before conditioning and paying their probabilities explicitly.
It then uses the high-count and shorter-image recurrence.

The [avoidance applications](cycles/phase7/AVOIDANCE_LANGUAGES.md) give
strict savings below critical exponents approximately `0.702879` for
omitting `101` and `0.359194` for omitting `111`. These correspond to
avoiding odd residues one and seven modulo eight. The symbolic entropy
models are credited to prior work; the ordinary estimates retain their
bounded-multiplicity premise.

For the [global census](cycles/phase7/PERIOD_CENSUS.md), write
`g_C=n_C ln2−u_C ln3>0` for a cycle's logarithmic gap. If the union of
its distinct odd states through `X` has size `O(X^h)`, then

\[
 \sum_{m_C\ge M}g_C=O(M^{h-1}),\quad
 \#\{C:g_C\ge t\}=O(t^{-h}),\quad
 \sum_C g_C^a<\infty\quad(a>h).
\]

This counts cycles with multiplicity even when several share one period
vector. The minima split at `1/t` proves the middle bound. A lattice
count in the strip `0<np*−u≤t`, `n≤N`, then gives:

| Quantity | Bound | Additional input |
|---|---|---|
| Distinct reduced slopes `u/n` | `O(N^(h/(1+h)))` | None |
| Distinct vectors with `gcd(n,u)≤G` | `O(N^(h/(1+h))+G)` | None |
| All distinct vectors after discarding at most one rational ray | `O(N^(h/(1+h)))` | None |
| All distinct vectors | `O(N^(h(μ−1)/(μh+1)))` | `||bp*||≫b^(1−μ)`, `μ≥2+h` |
| All cycles, including repeated vectors | `O(N^((μ−1)h))` | Same irrationality bound |

In the two-dimensional case the lattice hull contains at most `2Nt+1`
nonzero vectors. In the one-dimensional case all vectors are multiples
of one primitive ray; the irrationality bound controls that ray.

An elementary unrestricted cycle-state argument supplies every
`h>h*=H₂(log₃2)=0.9499555271…`, below one. Thus the reduced-slope
exponent is `0.4871677913…+ε` without a numerical verification floor
or a quantitative irrationality measure. Classical Rhin gives the
unrestricted full-vector exponent `0.8662982135…+ε`. The separately
quoted Chudnovsky input `μ≤3` gives `0.4935004926…+ε`; under the same
input the dimer and avoid-seven cycle counts, including multiplicity,
are respectively `O(N^0.641704)` and `O(N^0.718389)`.

The strict finite-state bound also supplies a convergent unrestricted
fractional gap moment at exponent `h*`. Earlier Papers 186 and 217
already aggregate cycle gaps, and Paper 145 gives stronger results
inside some narrow-height classes. Those precedents are distinguished
from this census. Sparse possible periods still permit an exceptional
cycle of an unbounded period.

The [joint backward-mask estimate](cycles/phase7/REVERSE_MASK.md)
retains both a real source interval and an actual ternary predecessor
condition, including the finite canonical carry. The [iteration audit](cycles/phase7/BOOTSTRAP.md)
identifies why the current bounds cannot simply be reapplied until the
exponent becomes negative: actual-source conditioning changes the word
law, later masks can repeat already determined information, and the
specific even-moment Fourier certificate has a square-root support floor.

## Limits of local one-edge energy functions

A positive `u(n)=o(n²)` satisfying `u(Tn)≥w(n)u(n)`, with `w=1/4`
on even inputs and `9/4` on odd inputs, would exclude escape by the
main repository's finite simple-path reciprocal bound. The
[finite-place obstruction](rigidity/phase8/ADELIC_HEIGHT_OBSTRUCTION.md)
considers the explicit representation

\[
 u(n)=n^2\exp[-g(\log_2 n)-P(n)-E(n)].
\]

Here `g` is nonnegative and nondecreasing, `E` decays by a positive
power of `log n`, and `P` belongs to the stated finite-prime classes:
regular bounded local terms, finite-precision logarithmic potentials
of signed measures, or full algebraic-center potentials with the
specified height moment. If `g` is unbounded, the violating ordinary
vertices have upper counting exponent one. In particular the inequality
cannot hold outside a set of size `O(X^(1−ε))` for any fixed `ε>0`.

The proof samples genuine positive CRT lifts of a stationary finite-place
law, biases only a short initial parity block to obtain positive real
growth, and supplies independent fair tail bits to avoid a proposed
power-sparse failure set. Stationarity compares the two local expectations;
the geometric-scale recurrence then forces `g` bounded, a contradiction.
Bounded `g` cannot make this representation subquadratic either, because
the sampled local potentials have uniformly bounded expected magnitude.

For locally constant corrections and finitely many fixed logarithmic
centers, with the stated harmonic error condition, the
[stronger obstruction](rigidity/phase8/PERIODIC_PLACE_VIOLATIONS.md)
forces positive upper natural density of violations. An expanding
rational periodic point gives a true arithmetic progression on which
the local terms cancel. Weighted sums of radial increases then telescope.

These conclusions do not impose the representation on arbitrary
arithmetic functions. [GeometricScales.lean](rigidity/phase8/GeometricScales.lean)
formalizes only the finite recurrence and its boundedness consumer.
The finite-place comparisons and density theorems remain written proofs.

## Verification and unresolved obligations

See [checkpoint seven evidence](../../reports/astra-reciprocal-rigidity-20261127/checkpoint7/README.md).
The root reconstructed all arguments above. The cycle and rigidity lanes
independently reviewed the all-clock, Markov-bridge, mask, and census
proofs. Exact controls retain their finite scope.

An all-clock protected initial segment can merge later. A sparse cycle
census can contain a cycle. A local-potential obstruction leaves genuinely
nonlocal arithmetic certificates open. No statement here forces the
future of every fixed ordinary source to reach one.
