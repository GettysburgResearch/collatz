# Checkpoint 3: affine families, local witnesses, and the fixed escape spine

This is an interim checkpoint in the requested 12:31:15–21:31:15 UTC pass.
It does not close the pass or claim a complete proof. The coordinator read
and reconstructed the four arguments below. Exact finite controls are in
[CHECKPOINT_03_EVIDENCE.json](CHECKPOINT_03_EVIDENCE.json). No additional
analytic theorem was formalized in Lean for this checkpoint.

## 1. Arbitrary sparse affine families

Author commit `d2624544`; coordinator integration `879ec47f`.
[MIXED_AFFINE_FAMILIES.md](../../research/astra-global-pursuit-20261128/dynamics/MIXED_AFFINE_FAMILIES.md)
extends the previous block proof to arms `3^Q_i x+c_i`, with repeated grades
and an arbitrary real centering parameter. The event is simultaneous equality
of endpoints and effective odd grades under one Haar binary anchor.

The signed residual update is exact. At a fixed grade the residuals still
have integer spacing, irrespective of the real center, so the same packing
estimate absorbs the number of large-residual labels into a fractional
moment drift. The remaining forcing term is the number of represented grades.
Each individual arm has a binomial added-grade marginal; a union bound needs
no independence between arms. This bounds the expected grade range by its
initial width plus the smaller of the time and the square root of time times
logarithmic family size. Sorting the remaining grades makes the scalar-pair
grade costs telescope. Signed offsets cancel exactly after normalization.

The resulting tail numerator is
`1+K+min(L,sqrt(L A))`, with `L=1+log(2+V)`,
`A=1+log(2M)`, and `V=sum(1+|c_i-3^Q_i beta|^alpha)`.
For times preceding the compression stage this numerator is at least a
constant times `sqrt(L)`, so the stated bound also covers those times by the
trivial probability bound. The imported scalar absorption estimate remains
the substantive external input already identified in checkpoint 1.

The ordinary consumer includes every start in every interval
`[2^a 3^b n,2^a 3^b(n+1))`, for `0<=a,b<=h`, at once. The first `a`
ordinary steps produce the affine label `3^(b+k)n+T^a(r)`; this identity
remains valid when the offset exceeds `2^a`. The total number of arms and
their offsets are exponential in `h`, so the tail becomes `O((1+h)/sqrt(t))`.
Counting complete binary periods adds `2^t/X` for an anchor interval of
length `X`. Different original starts may arrive at the common integer at
different dates, since their preparatory lengths differ. This is not a
claim of synchrony at the original common clock.

Normal and optimized exact replays agreed on 4,590 signed updates, 1,781
normalized cancellations, 72 complete-period binomial marginals, and
137,592 ordinary interval lifts. These checks verify the finite identities,
not the imported infinite-time tail.

## 2. A pointwise tripling witness

Author commit `ea3d46b4`; coordinator integration `bcf37dff`.
[LOCAL_TRIPLING_WITNESS.md](../../research/astra-global-pursuit-20261128/arithmetic/LOCAL_TRIPLING_WITNESS.md)
starts with one specified adjacent change of an invariant binary coloring.
It produces an odd tripling failure from a bounded list of dyadic boundary
addresses and explicit chains of powers of three.

The persistent child is unique because the two exterior colors differ.
The address cannot contain `100`: the corresponding two consecutive
integers have the same third shortcut iterate. Six initial left choices
give six plus-germ phases. Removing powers of two and three changes the
plus-germ exponent by `h+2v`; one phase makes `2^k a` equal to one modulo
nine. The resulting lower pixel `(2^k a-1)/3` is an odd multiple of three
whose two colors are exactly the original unlike colors. Two consecutive
right choices give the minus-germ construction, with exponent shift `h+v`
and a residue choice modulo three. In the remaining address the successive
odd endpoints cycle through all three residues modulo three within the
claimed bounded depth.

For each produced witness its six-free anchor is recovered from one of the
witness itself, `3P+1`, or `P+1`. This gives the claimed logarithmic-square
fiber count. The final higher-denominator statement is also scoped
correctly: it classifies zero offset at the *first integral entrance*, not
every eventual equality of colors. A negative offset that will reach zero
is increasing while negative; an even step followed by an odd step rises
above `-1/4`. Hence before the last odd departure only the two displayed
words are possible.

Priority has been explicitly corrected. Papers 227 and 228 already give
stronger global directed supplies and tripling sufficiency. The local
decoder does not establish a needed directed implication. Its 2,050 ordinary
controls use the visit-to-five label, which has one exceptional departure;
they are concrete checks of the formulas on the tested instances, not an
example of a globally invariant nonconstant coloring. The 59,048 rational
phase controls are exact. Both runs agree under Python optimization.

## 3. A nearest-representative moment for unweighted escape

Author commit `67bbe79b`; coordinator integration `befa23dd`.
[REAL_SHIFTED_HARMONIC_FLUX.md](../../research/astra-global-pursuit-20261128/wild/REAL_SHIFTED_HARMONIC_FLUX.md)
uses the joint stationary real and ternary coordinates. The odd representative
is chosen strictly above the real coordinate, rather than above zero.
With exponent `u=k^(-1/5)`, its normalized singular moment has limit
`(log 3)/2 + (log(4/3))/2 * d_escape`, where `d_escape` is the actual
ordinary relative odd escape density.

The coordinator checked the finite-part argument against the existing
single-scale pole theorem and Weaver 176/v1. At fixed conductor and exponent
the difference from the periodic ternary profile divided by the integer is
absolutely summable. Therefore changing the forward cutoff to its inverse
cutoff has the same arithmetic flux as in Weaver's original calculation.
The additional killing factor is `1-c(y)^u`; its uniform first-order
expansion is valid since `-log c(y)` is bounded. Summing with the same
exponent held fixed, then using the joint limit from checkpoint 2, gives
the unweighted escape coefficient. Weaver's earlier pure ternary statistic
has a survival-weighted coefficient and is credited separately.

For each sample the representatives after the first lie between two explicit
harmonic bounds. Their total difference is bounded by a logarithm of the
first representative divided by the conductor, integrable uniformly by the
stationary fractional real moment. This justifies the uniform `O(1)`
remainder after taking expectations and removing the cutoff. The first
singular term is integrable at each fixed positive exponent; the stated
concentration estimate or monotone convergence after subtracting the
dominated tail proves this without assuming the desired limiting bound.

The 18 CRT means and 2,240 rational tail sandwiches replayed exactly in
normal and optimized Python. They do not evaluate the stationary moment.
No uniform upper bound by `(log 3)/2` has been proved.

## 4. One fixed ordinary escape root, with its complete inverse spectrum

Author commit `bd75438d`; coordinator integration `d4670a87`.
[ESCAPE_GAIN_SPECTRUM.md](../../research/astra-global-pursuit-20261128/dynamics/ESCAPE_GAIN_SPECTRUM.md)
gives a deterministic structure theorem conditional on an escaping positive
component. It does not select a different source at successive deadlines.

The elementary uniform reciprocal bound follows by applying a logarithmic
number of shortcut steps to all states below `Y`. High-odd-count words are
entropy-sparse; every remaining endpoint lies in an interval of a smaller
power of `Y`. On a nonperiodic orbit this iterate is injective, so dyadic
summation bounds the sum of reciprocal visited states uniformly. The
multiplicative correction defining the amplitude is therefore finite.

Amplitudes exceed the corresponding ordinary integer. Every bounded
amplitude cutoff consequently contains finitely many ordinary sources.
A minimizing amplitude is attained, and its source wins the incoming gain
competition at every future endpoint. The next distinct amplitude supplies
a uniform relative gap. For any fixed source in the component, all members
of each finite amplitude cutoff eventually reach its path. The normalized
gain spectrum and its ordinary-source multiplicities then stabilize exactly;
the maximizing clock is the physical clock plus one fixed integer. This is
stronger than extracting a compatible infinite symbolic path from a series
of unrelated finite maxima.

At each odd departure the skipped even sibling has a predecessor cone
disjoint from every other such sibling cone. Maximizing sources for these
cones form an ordinary forward antichain. Reciprocal powers give summability
of sibling gain ratios to any power greater than one without a density
input. First-power summability additionally uses the explicitly cited
uniform predecessor floor of Wren 10/v3, whose stated input is joint mixing.
The coordinator read that primary statement, including its coverage of
all positive ternary units, and checked that the chosen unit remains on
the relevant sibling path before it joins the spine.

No positive comparison between a high normalized gain spike and its doubled
sibling is established. Such a comparison would exclude escape, but it
would not by itself exclude nonstandard bounded cycles. The Haar maximum-
gain tail and the worst-root inverse-frequency theorem do not supply this
comparison; the note records their quantifier mismatch explicitly.

## Evidence and remaining scope

All three finite checkers use explicit exceptions rather than removable
Python assertions for their validation gates. No new Lean compilation is
claimed here. The thirteen displayed roots from the preceding checkpoints
remain the locally compiled formal portion. Analytic and density inputs
from outside sources remain source-qualified written inputs; reported
external Lean has not been rebuilt by this team.

The next research work continues on actual global implications and possible
new mechanisms. This checkpoint preserves these arguments while that work
is active.
