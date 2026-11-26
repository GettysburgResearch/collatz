# Final coordinator review: actual arithmetic and the surviving obstructions

**Scope:** reconstruction of the named written arguments, together with
separately executed finite checks. This supplements the earlier
[ROOT_REVIEW.md](ROOT_REVIEW.md); it does not turn the complete repository
or every auxiliary appendix into an audited proof. Collatz remains open.
The three research lanes were GPT-6.2 Astra agents. Their independent
reviews are other-agent reconstructions, not outside expert endorsements.

The source manifest binds the delivered bytes. Hashes below identify the
versions the coordinator actually read. The compiler receipts establish
only their listed finite statements. None of the infinite arguments in
this report has a complete Lean formalization in this packet.

## 1. The actual shifted-cofactor theorem

Reconstructed `renewal/SHIFTED_COFACTORS.md`, SHA-256
`1bc18fa536bac5133648b0ee1ef27696decd7abacb9aed7a38908a58197d23e6`.
Separate reconstructions are in the operator and adelic directories.

The short-return identity is an integer identity at every prime,
including 2, 3 and primes dividing the fixed denominator. If two visits
to a shifted prime-power class are sufficiently close in native time,
their common divisor exceeds the absolute value of the return integer.
Its vanishing makes the indicated affine word a genuine periodic return
of the rational phase. Backward dyadic integrality supplies the literal
parity word; affine equality alone would not justify that interpretation.

The important quantifier is a *single* prime pool per complete prefix,
with bounded cardinality. Its primes may depend on the full prefix.
Within one logarithmic-height band, high divisibility creates only a
bounded number of periodic groups. The random translation of the
multiplicative bands in log height bounds the sum of entrance charges.
The coordinator checked the deterministic selection from that average,
the subdivision at a fixed multiple of band height, and the negligible
short pieces as the actual source goes to infinity.

The fixed-source periodic-window theorem is then used with fixed library,
fixed interval count and fixed auxiliary places. No Subspace Theorem
constant is claimed uniform in the moving prime pool. Summing the
length bound gives lower native fraction `log₃ 2`, with limits taken in
the stated order. Nonperiodic phases yield singleton groups and fraction
one. These are necessary properties of an assumed escape, not an
assertion that any escape exists or that a time-dependent pool may be
chosen separately at every clock.

The coordinator also reconstructed `renewal/CYCLE_COFACTORS.md`,
`aaef2037495e50a1b8e34a0f3efd75e180da0e232e6e407d967681cc044d5c71`.
The inherited finite simple-path bound gives reciprocal odd-state sum
`O(μ^(−1/40))` on one primitive lap. Repeating only `floor(μ^(1/80))`
laps makes the total reciprocal error tend to zero. The integer carry
bound gives initial log height `O(L)`, negligible compared with the
repeated length. The local varying-window statement in adelic Theorem A
therefore applies uniformly on the needed subwindows. Repetition does
not misuse the distinct-state bound: that bound is applied to one lap
before multiplying its resulting estimate by the number of laps.
The result concerns a sequence of distinct cycles with minima tending
to infinity, not exclusion of one unknown finite cycle.

The coordinator reread the finite-path input T-A3-651 in
`research/astra-three-routes/pass3/FINITE_RECORDS.md`: low total odd-gap
valuation is counted by one residue per composition; high valuation
has distinct smaller odd endpoints. Discarding the final `q` odd states
handles the finite boundary. The supplied constants yield
`5 X^(39/40)` and its reciprocal integral. This is an inherited written
argument, not a newly executed formal theorem.

## 2. Nonlinear polynomial values: a finite elementary proof

Reconstructed `renewal/POLYNOMIAL_COFACTORS.md`,
`726cd84a3663023bd48f4eb2ae71f675f1132f3b4962b47f050286ba3ad0327b`,
also independently reviewed in `adelic/REVIEW_POLYNOMIAL_COFACTORS.md`.

For irreducible `f` of degree at least two and a return
`x ↦ (3ᵇx+C)/2ˡ`, the two integral polynomials are `f(X)` and
`2^(ld) f((3ᵇX+C)/2ˡ)`. A zero resultant would force their shared
irreducible factor to be all of `f`. The affine map would permute every
distinct conjugate root. Some positive power would fix two distinct
points, impossible because its positive slope is never 1. This argument
also covers the all-even and all-odd words.

The integral Sylvester adjugate expresses the resultant as an integral
combination of the two polynomials. Evaluating at the source therefore
retains the shared prime divisor even at 2; no inversion of the
denominator is used. The coefficient bound is exponential in the native
return length with constant depending only on `f`.

The coordinator checked the entire counting step: remove one maximum
valuation for each selected prime, integrate the remaining `N/u` tails
only between `Q/(2r)` and `Q`, and separately count values above `Q`.
This produces `r log(2r)`, not `r²`. Distinct positive states make the
low-height exceptional set at most `sqrt(N)+O_f(1)`, uniformly in the
starting source. Factorization handles polynomials with no rational
roots, retaining fixed content and multiplicities. The rank-coset
bound selects at most `r` coordinate primes from the span of sampled
ratios; it does not bound the support of arbitrary group generators.

The source explicitly credits Weaver's paper 138 for the return-tail,
coordinate-prime and weak summation method. The coordinator opened that
primary manuscript and the Stacks Project's Sylvester-map description.
The nonlinear nonvanishing resultant is the additional input here.
No exhaustive novelty search is claimed.

## 3. Mandatory log-height and growing prime pools

Reconstructed `operator/ROUGH_LOG_GATES.md`,
`119009343083c886caa5e465c08c9bcce47aa13dff76772ca0afa25d697e1a7a`,
and the final `operator/GROWING_PRIME_POOLS.md`,
`fdde266803da529be1a6ebe48afb38bcfafba0f438a72990b8502a6cd990a42d`.
The renewal lane independently checked these arguments. The final edit
to the growing-pool statement makes the same-pool prefix quantifier
explicit; the coordinator read that final text.

The coefficient-record endpoint is marked by its incoming positive
logarithmic overshoot. All records below a chosen logarithmic height
`H` together cost at most `H+O(1)`. Above it, the exact return integer
gives short-gap groups at each selected prime. Two genuine coefficient
records within such a group force the returned rational phase to be a
negative signed record-cycle phase, since the actual multiplier between
the records exceeds one. Interior marks then have the stated incoming
and outgoing labels and paired local congruences. Only boundedly many
end marks per group must be discarded at fixed precision.

For bounded pools the total unprotected roof is `O(sqrt(N))`. Repeating
the weak-tail summation with a pool of size `r` and optimizing `H` gives
`O(1+sqrt(N r log(2r)))`. The estimate is on an actual single source,
before division by its running peak. The support conclusion therefore
requires `r log(2r)=o(A_N²/N)`; it is not automatic on slowly growing
escapes. The numerical-record transfer uses a bounded total-variation
discrepancy for arbitrary marks at the same physical times, and charges
all additional numerical-only records. It does not assert a uniform
component-summed rate for the global exit current.

For nonperiodic shifts, the same prime-tail estimate gives an absolute
finite bound on every simple native segment. A state of an assumed
escaping orbit is nonperiodic under that hypothesis. The argument does
not silently assume that an arbitrary positive integer is nonperiodic.

## 4. Exit-gate geometry and the compulsory clock

The earlier review covers `operator/EXIT_GATES.md`. The coordinator
additionally reconstructed the following frozen arguments:

| File | SHA-256 |
|---|---|
| `operator/GATE_ARITHMETIC.md` | `0c2c0e70ec194484a806158ce7ae046ed26ba32b7bd99c39c66e01620e19198d` |
| `renewal/GATE_PROXIMITY.md` | `3a8df7c90b246382843b115c5e628c6468a719844d02903c6421b50f688181d3` |
| `operator/GATE_LOWER.md` | `51c7131e3afbcb7d67bcf28a1bb2e7c0fb844ff8929d1023e8b49a451da7b433` |
| `operator/GATE_SUSPENSION.md` | `aa703d7a73d3e51341c37f1a614613813749b03eee31b89c051b679cf7454609` |
| `operator/REGULAR_OCCUPATION.md` | `016949d85c512c229043fbe7be50188deb140b84c15d01cc72315845e720ba43` |

A heavy gate has a contribution from a bounded source after truncating
the Dirichlet tail. Its long backward prefix is coefficient-critical;
the first subcritical prefix plus the logarithmic-form lower bound
gives the stronger ternary proximity exponent. The true critical sieve
then has the stated ballot-count size. The leakage computation retains
all short backward histories and gives the separate regimes at, below
and above `s=2`. Lower bounds survive deletion of every power-thin set
through `s=2`; above 2 the extra lower-pressure proof concerns total
flux, not flux outside the sieve. That distinction is retained.

The total lower-pressure construction selects literal admissible
reverse words and a terminal representative in a short annulus. Their
prefix slope bound places every preceding state below the cutoff, so
the exit is genuine. Different word/representative pairs cannot count
the same source twice. Under the tilted geometric law a fixed initial
buffer leaves positive probability of staying above the barrier.

The compulsory clock follows from the exact monotone discrepancy
between coefficient log records and numerical log records. Its
increments have summable total discrepancy. Normalization by total
positive roof leaves mass one even if odd-time occupation vanishes.
Weighted edge laws are not automatically invariant counting measures.
The circle identity is an average across each roof interval, not a
claim of stationarity of terminal phases.

On the regular sector, finite-time suspension invariance yields a
probability-preserving flow; division by the roof gives a sigma-finite
conservative base measure. The coordinator checked the exhaustion away
from zero roof, the absence of influx into this sector, and recurrence
used to classify atoms. An atom in either local coordinate forces a
finite genuine negative rational cycle with agreeing coordinates.
The regular sector can have zero mass, and its nonatomic part remains.

The indented blank line in `GATE_ARITHMETIC.md` is deliberately retained
so its reviewed source hash is not changed merely for whitespace.

## 5. Conditional fibers and exact countermodels

Reconstructed `renewal/ENTROPY_FIBERS.md`,
`53d3416b6ec5f1ce95cdabbe7e7c7186c0eb0bff0c164e6fe3d43fa3af7cfd29`.
For finite-mean ergodic record flow, future labels determine the dyadic
coordinate and past labels the ternary coordinate. The conditional
dimension `h/(L log 3)` retains the finite label entropy and carry-overlap
arguments. The restriction-to-measures step uses a positive local
Radon–Nikodym derivative, rather than asserting injective ternary coding.
No lower bound `h>0` is proved for an ordinary escape.

Reconstructed `renewal/LOG_HEIGHT_MODEL.md`,
`bf13ef7aac53937df40c8ad7dda1e486ddb9c5d63a019b9eedb595cc4b820d0e`.
One model has bounded positive roofs, unbounded labels, vanishing
odd-time flow, irrational dyadic start, and a single unequal rational
pair in its log-height occupation. A second has diagonal atomic
occupation but rare off-diagonal cluster points. The latter prevents
turning an all-cluster-set exclusion into positive occupation outside
the diagonal. Neither has a single positive ordinary realization.
The explicit family reaching a power of two supplies arbitrarily long
matching finite windows in the known basin. Those sources change.

## 6. Order, its counterexample, and surviving rational cycles

Reconstructed `adelic/ORDER_REVERSALS.md`,
`f3f219255ba0587203cffe12a689c087c1c19722db02f7e92858f7985c49ac34`;
`adelic/CONTRACTING_REVERSAL.md`,
`aaa8a8384ed0790b502531dbd9562fb46b6f71df87f8eb00c9dc7e91e5a8e60c`;
and `adelic/DYADIC_CYCLE_ORDER.md`,
`75d634920ffef0d37f7589833d85ecbebe0044b9e36e0d33f96deab8f3c7b915`.

The fixed-grade classification includes wrap pairs in the sorted residue
class. The exceptional small grades are kernel-decided in the finite
Lean file; propagation uses genuine residue classes and common affine
slopes. The coordinator's independent search found the contracting
counterexample at `859,860`, clock 46, grade 29. Its terminal values
`890,866` both exceed both sources, but the paths have earlier descents.
No first-descent assertion is refuted or assumed.

The unequal-clock argument for a primitive cycle, with its least native
period and distinct odd phases, sorts all dyadic lifts of those phases.
An adjacent periodic swap removes one affine inversion, preserves mean
displacement and changes the number of quotient cycles by one. The
sorted translation has `gcd(N,p)` cycles, giving the lower bound and
parity. The integer interval condition rules out depth-one and
depth-two inversions. It supplies no upper bound excluding the coprime
sector.

Finally reconstructed the analytic part of
`adelic/DYADIC_CYCLE_CONTROLS.md`,
`c8e0a110a8ccdec8b933887bc5f37316029d2c918e7adff8e96709758df4ae5f`.
For `δ=N−p log₂3≤1/p` and coprime `N,p`, the displacement of two
normalized perturbation arcs from the `qN/p` grid is at most
`(p−1)δ/p`. Their circle distance is therefore at least `1/p²`.
The convergent families already in `CYCLE_INDEX.md` satisfy that
hypothesis. Thus a large family of rational cycles passes even the
strongest disjoint-arc version of this test.

The same note's two new numerical overlap tables were executed by the
adelic agent and independently recomputed by the operator agent. The
small case was checked with full rational numerators; both lanes used
outward intervals with coincident lower/upper counts for the large one.
The coordinator inspected the method but did **not** rerun these extra
pair tables. They are not counted among the nine root-replayed control
programs. The underlying full native fixtures were already root-replayed.

## 7. Annular transplantation and a source-qualified distribution rate

Reconstructed `operator/ANNULAR_TRANSPLANT.md`,
`910c93932d200fb1c1514088c008f8f76285962616c919a7a9fd9fdb2fc3b09f`.
The odd inverse congruence and a fixed arithmetic progression of binary
scalings retain the required ternary class. A finite irrational-rotation
net places the result in any prescribed relative annulus. Bounded
multiplicity preserves the predecessor lower count. This gives a
sufficient exceptional-set target, not the required estimate itself.

Reconstructed the finite argument in `adelic/LEVEL_FRONTS.md`,
`e1eaca725e3fddf110313ef0e4729b0f58178aa03373a27dc28361e1a9587386`.
The finite total-variation comparison with translation of the full
landing-label distribution is valid. Its asymptotic `1/sqrt(log)`
rate imports Leen's unrefereed adjacent-fusion theorem. The original
Zenodo retrieval failed; the coordinator read primary manuscripts
124 and 13 stating that input, but did not audit the original proof.
The finite table version is separate from the source-qualified rate.

## 8. Executed formal scope and remaining obligations

The original replay covered 53 unique declarations in ten source files.
The trapping replay rebuilt eleven files with 60 declarations. The
order replay rebuilt its dependency and the four new declarations.
Their union is **64 unique declarations in twelve exact source files**.
Every successful final run used warnings as errors, fresh output, stable
source bytes and printed axiom inspection. Only `propext`,
`Classical.choice`, and `Quot.sound` appeared. The intermediate failed
trapping edit was corrected before the successful exact-source replay;
it is not presented as a successful formal result.

The nine root-replayed finite scripts each matched the full recorded
JSON in ordinary and optimized Python, with identical output bytes.
The separate gate and order receipts supplement the first seven-script
receipt. These eighteen executions certify neither the infinite
analytic theorems nor universal convergence.

[FINAL_PROPOSAL.md](../../research/unconventional-20261126/FINAL_PROPOSAL.md)
states the exact checked equivalence and the two missing mathematical
conclusions: finite trapping for every positive source and uniqueness
of the positive cycle. In the analytic route the sharp missing estimate
is vanishing weighted current on the explicit thin critical gate sieve.
In the cycle route it is exclusion of the denominator-one row except for
words on the known positive cycle.
Neither conclusion follows from the restrictions reviewed here.
