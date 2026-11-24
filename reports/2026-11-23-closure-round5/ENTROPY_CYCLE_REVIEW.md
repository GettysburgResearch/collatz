# Independent entropy–height review and rational-certificate cross-check

Date: 23 November 2026. Reviewer: the cycle-exclusion lane, independent
of the two source authors. Local parent:
`cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`.

**Verdict: VERIFIED for the written results and finite formal statements
explicitly reviewed below. Full Collatz remains OPEN.** This report
records a mathematical reconstruction and source reading. It does not
claim an independent compiler execution or an entropy-program replay.
The root execution receipts are separate evidence.

## Reviewed source identities

The following paths are relative to `research/closure-round5-20261123/`.

| File | SHA-256 |
|---|---|
| `FIXED_SOURCE_PRESSURE.md` | `09b9cb3a1bd7daf1bc77b70e5010c8591b3d1fa7965e59a63dff6efc1dbe5c76` |
| `FixedSourcePressure.lean` | `1ca906b9fbacad0b7228ce3702c63df0e5b01b9964231b7cd2f6ed0cb812a3d6` |
| `TRIADIC_CONSTRUCTION.md` | `40fde45d454b19a97f208aef9950a2fd6fbf0fd15cef1995b37fbf5099b8b562` |
| `TriadicConstruction.lean` | `296e622d30826fe87a63f86be63b1836497705d751c7bace5699f3755e04fc23` |

Both finite Lean companions were read in full. This report reviews
their literal theorem statements and proofs semantically; compilation
is recorded by the source authors and the root in separate receipts.
No whole entropy formalization is claimed.

## 1. Actual word injection and finite normalization

Reconstructed the ordinary arithmetic directly. Two occurrences of
one length-m parity word have the same odd count and complete carry.
Subtracting their full affine identities gives

`2^m * (x_(i+m)-x_(j+m)) = 3^p * (x_i-x_j)`.

Since two and three are coprime, the original source difference is
divisible by `2^m`. If `2^m>H_N`, both positive sources lie in a
single interval shorter than that modulus, so they are equal. Actual
orbit injectivity then identifies the occurrence indices. This proof
does not assume independent words or replace the original sources by
uniform residues.

There are exactly `M=N-m+1` sampled starts, including both endpoints
of `0,...,N-m`. Every word then occurs once, giving entropy `log M`
and word-space collision `1/M`. At arbitrary precision, one residue
class has at most `floor(H_N/2^m)+1` sources, yielding the stated
maximum-atom and entropy bounds. The extra residue cell is a safe
overcount. These are word laws, not ternary endpoint laws.

The finite Lean companion defines the literal natural-number shortcut
map, endpoint and chronological parity prefix. Its branch identity is
proved from the actual remainder modulo two; induction then retains
the complete ordered carry in `parityPrefix_affine`. The equal-prefix
source congruence is derived from those identities. The height theorem
uses both original sources below the full modulus. `prefix_image_card`
counts a finite set of distinct sources, and `prefix_fiber_card_le`
injects a fixed-word fibre into the quotient cells `n / 2^m`, using
the complete carry congruence to recover a source from its quotient.
The resulting upper count is `H / 2^m + 1`. No entropy, asymptotic
limit, or unproved ordinary-orbit hypothesis is hidden in these finite
formal statements.

## 2. Finite block averaging and the remainder

Independently checked the exact factor in the key inequality. Fix
`1<=k<=m<=N` and choose a uniform m-word start `J` among M starts.
For any internal k-window offset `a` in `0,...,m-k`, its starting
positions form a subset of size M of the `N-k+1` positions used by
the full k-block empirical law. Thus the latter law is an exact
mixture of that internal law and its complementary interval law,
with coefficient

`rho=(N-m+1)/(N-k+1)`.

Concavity and nonnegative entropy give `H(Q_a)<=H(P_N,k)/rho`.
This direction is correct: a restricted law can have larger entropy,
and its mixture weight pays for that possibility.

Partition the m-word into `floor(m/k)` full k-blocks and a possible
remainder of length r<k. The remainder is a projection of the full
k-window at offset `m-k`. That comparison window may overlap the
previous block; its entropy still bounds the remainder's entropy.
Subadditivity needs no independence and no disjointness between these
comparison variables. There are exactly `ceil(m/k)` terms, giving

`H(P_N,m) <= ceil(m/k) * (N-k+1)/(N-m+1) * H(P_N,k)`.

The boundary cases k=m, k=1 and m=N cause no missing term. This
establishes the exact finite inequality used before any stationary
limit is taken.

## 3. The stationary-limit order is sound

For one infinite injective positive orbit, fixed-block empirical
limits are consistent under deletion of either endpoint: the start
intervals differ by only boundary samples. They therefore define a
stationary binary process. Entropy convergence is used only on each
fixed finite alphabet.

Distinct positive states give `H_N>=N+1`. Under a finite polynomial
height exponent beta along the chosen limit subsequence,

`m=ceil(log_2(H_N+1))`

tends to infinity, is `O(log N)`, and is eventually at most N. For
every fixed k, the exact finite inequality applies. Its endpoint
factor tends to one, and its entropy lower bound tends inferiorly
to at least `k log2/beta`. Hence every fixed limiting k-block law
has entropy at least that amount. Taking the infimum of `H_k/k`
is legitimate by stationarity and proves `h>=log2/beta`.

The stronger liminf formulation is also valid. A further subsequence
approaching a finite liminf of the height exponents retains the same
fixed-block limit. If the limiting entropy is zero and the height
ratio did not tend to infinity, there would be an infinite bounded
subsequence, contradicting the preceding positive entropy bound.
No rate of convergence of the stationary block laws is required.
The growing-m law is never identified with a growing block of the
limiting process.

The critical-density consistency check is correct. The exact orbit
product gives the displayed logarithmic identity. The correction sum
is `O(log N)`, because the original positive states are distinct and
the sum of their reciprocals is bounded by the Nth harmonic sum.
Polynomial prefix height bounds the endpoint logarithm by `O(log N)`.
Thus odd frequency tends to `log2/log3`, and binary maximum entropy
recovers the preceding `beta>=1/theta` bound. The note appropriately
does not advertise this weaker general bound as an improvement over
the existing all-visit count. Its additional restriction concerns the
actual limiting entropy, especially the zero-entropy case.

## 4. Direct entropy pressure on the actual backward odd-gap lift

Independently reconstructed the added Theorem 3 on the reversed gap
words of the same original odd orbit. Equal reversed words imply equal
forward gap words, the same complete carry, and original-source
congruence modulo `2^A`, where A is their total gap. The unrestricted
bound `A>=m` immediately supplies the nonergodic baseline
`h(eta)>=log2/beta` after the entropy passage below. No return-map
identification between two differently normalized stationary laws is
needed.

The actual logarithmic odd-map identity and distinct positive sources
give `A_M/M<=log_2(3)+o(1)`. Each fixed k-word law therefore has a
bounded expectation of its total gap, at most `k A_M/(M-k+1)`.
Truncation before the limit gives `1<=a<=log_2(3)`. The original
average can converge to the critical value while the limiting mean
loses mass; the proof correctly does not infer moment convergence.

That loss does not invalidate entropy convergence. For a positive
integer k-tuple law with expected total gap at most C, a tail of mass
delta has conditional coordinate means whose sum is at most C/delta.
Subadditivity, the geometric maximum-entropy bound and concavity of
the logarithm give tail entropy at most

`delta log(1/delta) + k delta log(e C/(k delta))`.

Above total gap R, `delta<=C/R`, so this bound tends uniformly to
zero. Entropy converges on the remaining finite set. This justifies
passing every fixed k-word entropy to the countable-alphabet limit
without assuming uniform integrability of the gap itself.

The growing-word concentration estimate is also valid with its stated
constant. For entries in `[1,R]`, the average of all internal K-window
means equals an average of K means on consecutive intervals of length
`m-K+1`. Each such interval deletes K-1 entries from the full m-word,
so its mean differs by at most `R(K-1)/m`. Jensen's inequality and
the exact empirical endpoint mixture then give equation (16), with
factor `(M-K+1)/(M-m+1)`. First let M increase with fixed K; then let
K increase. Ergodicity and bounded truncation give mean absolute
concentration. No claim of weak convergence at growing block length
is used.

Choosing a truncation whose mean exceeds `a-epsilon/2` and taking
`m=ceil(log_2(H+1)/(a-2 epsilon))` makes a proportion tending to one
of sampled words have `A>log_2 H`. Every such word is unique among
all sampled occurrences, since goodness depends only on the word.
Its empirical mass is exactly `1/(M-m+1)`, so those words alone
contribute `(1-o(1)) log(M-m+1)` to entropy. Fixed-block averaging,
the entropy convergence proved above, and then epsilon tending to
zero yield `h(eta)>=a log2/beta`. The liminf and zero-entropy
statements follow by the same further-subsequence argument already
reviewed. At critical mean this is `h(eta)>=log3/beta` on the actual
odd-clock lift. The proof explicitly supplies no collision decay
rate for the exceptional word mass.

## 5. The critical nonatomic zero-dimensional control

Reconstructed the entire symbolic control. The floor increments of
the irrational rotation by `ell=log_2(3)` are in `{1,2}`, stationary
and ergodic under Lebesgue measure, with mean ell. For the ternary
series, its residue modulo three distinguishes the first gap exactly:
the inverse powers for gaps one and two are two and one, respectively.
Multiplication by the recovered binary power, subtraction of one and
division by three recover the next digit problem. This proves the
full depth-m coding injection without an independence hypothesis.

The first m gaps have exactly m+1 interval cells, cut by the distinct
rotation breakpoints. Their words are distinct because every prefix
floor sum is nondecreasing in the starting phase and changes at its
own breakpoint. Consequently collision is exactly the sum of squared
cell lengths and at least `1/(m+1)`.

Irrational-rotation density makes the maximum cell length tend to
zero. This supplies both vanishing collision and zero atom mass.
At the same time the lower collision bound forces Renyi-2 dimension
zero; the m+1 cylinder cover even gives upper box dimension zero.
There is no false passage from finite atomic controls to a nonatomic
law. The real series identity follows by substituting
`A_i=floor(t+i ell)`, and its uniform positive term bounds prove
linear real divergence.

This control is explicitly an auxiliary symbolic law. It does not
claim ordinary realization, a fixed integer source, or the canonical
harmonic-flow law. It correctly shows that critical mean, real
divergence and nonatomicity alone do not supply a positive ternary
collision dimension.

I opened Rudolph's primary paper, *Times 2 and times 3 invariant
measures and entropy*, at the publisher PDF and checked the abstract
and introductory theorem scope. It requires invariance under both
multiplications and ergodicity for their generated semigroup; the
positive-entropy conclusion is not a theorem for an arbitrary
valuation-selected affine stationary law. The note retains this
missing hypothesis accurately.

## 6. Sparse mechanical perturbation and ordinary exclusion

The sparse repair was also reconstructed independently. Since
`ell-1>1/2`, two consecutive mechanical gaps cannot both be one.
Thus the first gap two after `ceil(2^(k/2))` is at most one position
later. For k>=4 the chosen positions are distinct. Their count before
j is `2 log_2 j+O(1)`, so changing those twos to ones multiplies the
coherent scale by a factor comparable to `j^2`.

Only `O(m log j)` fixed gap windows meet a change. In the expanded
binary script the modifications delete `O(log j)` zeroes. Binary
windows away from deletions belong to the original mechanical
language. A length-k binary factor is determined by at most k+1 gaps
and two possible starting offsets, giving at most `2(k+2)` possible
unchanged factors. Every limiting binary law is supported on this
set at each fixed k, so its entropy rate is zero.

For a purported fixed positive ordinary realizer, normalizing the
literal odd affine recurrence by the coherent scale gives exactly

`q_j = chi_j * (n + (1/3) * sum_(i<j) chi_i^(-1))`.

The reciprocal sum converges and the leading factor is comparable
to `j^2`, so the actual odd states would grow quadratically. The
gaps are at most two, hence all shortcut prefix heights would also
be polynomial. The diverging states preclude a repeated ordinary
state, which would force eventual periodicity. Applying the actual
entropy–height theorem now contradicts the zero-entropy limit.

The quantifier is one fixed ordinary source. Positive integer
realizers of each finite prefix do exist by the complete parity
cylinder and are not mistaken for one infinite realizer. The note
also credits stronger prior mechanical-approximation results and
does not claim unrestricted escape exclusion from this example.

## 7. Independent cross-check of the rational certificate

This section reviews the separately authored rational note and all
eight public statements of `TriadicConstruction.lean` semantically.
It is not a compiler receipt.

For `V=x max(1,|w|)`, the original-odd large step contracts by at
most 5/6 while x>1. A negative large numerator on an original-even
step contracts by at most 3/4. A positive large numerator on that
branch produces a numerator above 2q; the following large step then
contracts by at most 7/8. Together with one-step nonincrease, this
proves the uniform two-large-clock contraction. The x>1 guard is
necessary, and the supplied x=1 control has the stated ratio.

Each nonzero small signed value is charged by its own magnitude.
Before the first small-value repetition, each magnitude appears at
most once per sign. The exact one-sign product is `choose(2q,q)`;
the full squared charge is at most `16^q`. Zero is a distinct value
and incurs at most one factor two before repetition. This proves
the global M bound even when small and large visits interleave.

The run count is correct: with s small inputs among t inputs there
are at most s+1 large runs, so pairing within runs gives
`2P>=t-2s-1`. At `t=14L+4q+4` and `s<=2q+1`, this is at least
`14L+1`; using the weaker `P>=7L` is safe. The geometric bound then
contradicts positive integrality. At the first repeated small input
j, all earlier small input values are still distinct, so the M
bound applies to both original states being compared.

For the finite-prefix convergence certificate, the retained L tests
fit within the budget: `j<t_*` and `H=t_*+L`. Determinism of the
numerator map gives equal original parity windows, and the full
affine identity makes their source difference divisible by `2^L`.
Both sources are below that modulus, so the full pair repeats.

The added exact-candidate decision is also sound. At original state
1, all-time compatibility forces the numerator to equal 2q; this
can be checked directly from divisibility by every power of four
along the 1,2 tail. At a repeated small numerator, unequal original
states refute all-time compatibility because the entire future
numerator path repeats and would force identical infinite original
parity vectors. Equal original states produce a previously checked
compatible pair cycle and therefore certify the supplied rational.
This rejection option is why the additional L tests can be removed.
The strict state-clock budget is `14 bl(B)+60q+18`, allowing at most
one fewer ordinary transition. Rejection concerns the candidate;
it is not a statement that the original source diverges.

For mixed denominators, each positive level keeps a numerator unit
at three. A run of L0 original-odd inputs would divide a nonzero
integer of magnitude below `2^L0` by `2^L0`, so denominator exhaustion
occurs by `J<=rL0` under continued compatibility. The bounds on the
tail height give the two stated initial budgets by direct expansion.
For exact recognition, an earlier original 1 is compared with the
current rational value 2, not automatically accepted. This important
distinction is stated in the final note.

The eight formal declarations retain the literal branch equations and
correct guard conditions. The signed-value visitation, run pairing,
first-repeat selection, full parity-tail proof, exact algorithm and
mixed-denominator consumer remain written. No universal successful
candidate selector follows from these verified finite statements.

## Remaining scope

Positive parity entropy does not itself establish a ternary Renyi-2
upper bound, independent gaps, or separate times-two and times-three
invariance. The entropy theorem permits superpolynomial height in
the zero-entropy regime. The rational decision procedure recognizes
a supplied rational; it does not decide whether a suitable rational
exists. Those are still substantive unproved closing steps.
