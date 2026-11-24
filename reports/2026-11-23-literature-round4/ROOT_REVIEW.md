# Principal review: denominator rigidity, actual finite laws, and cycle roots

Date: 23 November 2026. Reviewed parent:
`a7fd3ac9e5bff7412858df23d776bb847e9c1371`.

**Verdict: VERIFIED within the statements and boundaries below. Full
Collatz remains OPEN.** This is an independent in-session mathematical
reconstruction and integration review. Compiler execution and exact
replay are separately recorded in `LEAN_RECEIPT.json` and
`EXACT_RECEIPT.json`; neither is external peer acceptance.

## Frozen source bytes

Paths in this table are relative to `research/literature-round4-20261123/`.

| File | SHA-256 |
|---|---|
| `TRIADIC_RIGIDITY.md` | `b7f33d95c9b8caac1b1d7457189ad451220198c84f4e89f7af3ed935823fe05b` |
| `TriadicRigidity.lean` | `ab75d91329b642dd69eb6d33fd82bb376637ae0d2c8e7705fd1953e444957eb3` |
| `verify_triadic.py` | `0470da316c8e5cadb1c0b5a51452a5e9cfe2adcfb3f5b442f7cce2729fe48327` |
| `ACTUAL_LAW_RIGIDITY.md` | `a57e7aef865315ef3471a25e0fee18de4d6db75cf40455a0d658912666783e08` |
| `ActualLawRigidity.lean` | `9248f4e4041d3241038fef6a64ed502b2ab203228345c3aec3e9c4e735d432b8` |
| `CYCLE_RIGIDITY.md` | `9ab24369fe171a003ae318db808f1af78e949beeb868765673bcc632d1d78630` |
| `CycleRigidity.lean` | `e169c9914a01f1d43cf9133fbdaa5044bd080de849269437d822c10b33468d28` |
| `exact_replay.py` | `ccf0cae72418f7d8250e6cc9125a2190f100522668460e09f3e3826d97aa6791` |

## 1. Triadic classification and candidate decision

Reconstructed both predecessor cases for the pair cycle and both signed
rank branches. The indicator terms are necessary: the product is
unchanged at original coordinate 1 or dual coordinate 1. Outside the
pair cycle the corresponding marker disappears, while generic integral
product descent pays for both possible marker additions. Negative duals
are covered by the absolute-value inequality. The zero case is separate
and forces arbitrarily large powers of two to divide one fixed positive
integer. The all-time integral classification is genuinely proved in
Lean; it is not a supplied convergence hypothesis disguised as a result.

Independently derived the reduced denominator transition. At positive
exponent, an original odd input keeps the exponent; an original even
input reduces it by one, exactly, until exponent zero. Positive ordinary
orbits cannot have an all-odd tail. The first integral pair is `(2,1)`
for sources greater than 1: the other phase would already have an
integral predecessor. Earlier visits to 1 or 2 are excluded by the
unique complementary rational tail. This establishes the exact even
count in the written theorem.

For the strict clock, `3^s n+C=2^(s+b)` with `b=r+1>0` gives
`s<2b` by `9^b>8^b`. The implementation includes exactly the allowed
state clocks `0,...,3(r+1)-1`, including time zero at source 1. Its
backward equality is exact and permits unreduced inputs. Rejecting a
budget makes no assertion that the original source never converges.

Reviewed the old horizon strengthening by denominator exhaustion and
the two-step product contraction. In the adaptive zero case, finitely
many extra odd steps already contradict the available bit bound; the
final note states that finite divisibility explicitly. The linear
verifier is not a claim that short parity agreement suffices. For
example, source 1 and false candidate 10 have the first three opposite
input parities, yet fail the exact comparison with 2.

The final all-source corollary was checked independently. From the
complete affine identity, `n<=2^(r+1)`. For `N=bl(n)>=2`, this gives
`r>=N-2`, or `r>=N-1` for a nonpower of two. Since
`L>=bl(3^r)`, the monotone expression
`8N+(9r+8)L+2` is minimized at `r=N-2` and that minimum is attained
by `n=2^(N-1)`. Its numerator has absolute value at most the reduced
denominator. Thus the exact minimum is
`8N+2+(9N-10)bl(3^(N-2))`, and in particular at least
`9N^2-11N+12`. This is a cost bound for that certificate and assumes
no convergence of the other sources in the bit-length class.

**Boundary:** the rational interpretation, all-source stopping
application, finite verifier correctness argument, two-step logarithmic
bound and sharp horizon minimum remain written proofs. The eight Lean
statements establish the integral dynamics and finite count inequality.
No sufficient denominator selector for every ordinary source is supplied.

## 2. Actual finite product laws with phase collisions

Reconstructed the rotated complete carry identity with the negative
shadow sign. The telescope retains the original source and both carry
terms. Cancellation modulo powers of three fixes endpoint phases;
cancellation modulo powers of two charges the original source height.
The shadow itself is a negative rational cycle, while all finite
realizers used by the construction are positive ordinary integers.

The source cylinder has modulus `2^(A_T+1)`, with the final odd bit
included. The complete word supplies the parity at each intermediate
quotient; a reduced modulus would not establish the last exact
valuation. CRT enforces a source unit at three, and all later odd
states remain units. Distinct affine slopes give at most one bad
initial source for each pair of distinct clocks. Consequently
`T(T+1)/2+1` lifts suffice for an injective finite segment, with the
stated lower floor and strict upper bound.

The labelled de Bruijn construction gives exact product marginals
through the fixed local depth, including backward blocks after warmup.
Rotation at the maximal prefix ratio controls the full source-to-state
ratio; the finite period constant controls every interior window.
The carry bound and correction-product estimate retain the initial
floor. Sampling a whole number of phases gives collision at least
`1/d`, with ordinary diagonal `1/N`.

Independently checked how the round-three source boxes appear. Within
one phase the complete word, clock and carry quotient are fixed, but
distinct actual odd sources have different source quotients. The
cross-box mass is `1/d^2` for that phase; the sum of its individual
diagonals is `1/(dN)`. The repeated-word and cross-box terms cannot be
discarded. For `(1,1,2,2)`, the full denominator is 17 and the four
rotated carries are 73, 101, 143 and 103. They give four distinct
ternary phases from precision two onward.

The exact binary divisibility forbids keeping one positive source as
the repeating template length tends to infinity. The construction is
therefore a finite transfer obstruction, not an escaping orbit or a
counterexample to PR180's theorem about a fixed stationary time-limit
law. A next-order block marginal can coincidentally remain product;
the final checker instead chooses a depth where the iid support is
larger than the number of phases, which guarantees a nonproduct block.

**Boundary:** twelve Lean statements establish the complete carry and
shadow algebra, both divisibilities, source cost, finite phase count
and collision bound, and uniqueness of an affine coincidence. The
whole ordinary construction, CRT, de Bruijn realization and asymptotic
choice of sample sizes remain written proofs. The supplied weights are
finite uniform empirical weights, not canonical harmonic weights.

## 3. Complete cycle arithmetic and exact root-count obstruction

Expanded both block carries independently to obtain the signed cut
determinant and full transport identity. The denominator remains
`D=2^A-3^p` throughout. It is odd, so a rotation inherits full-D
divisibility by cancellation with the binary coefficient. For distinct
primitive rotations, the earlier fixed-clock carry decoder forces
distinct carries; the least carry then has a positive gap to every
other rotation. In an integral cycle each gap is a multiple of D.
This proves the exact rejection certificate for gaps between zero and D.

The suffix contraction follows already at a positive rational least
root. If a suffix has an odd bit its carry is positive; an all-even
nonempty suffix contracts directly. No integrality assumption enters
that necessary barrier. This is why treating the barrier as an extra
independent restriction on least roots fails.

Checked both complete controls: `1110010` has D=47 and a proper least
gap 14; `11011010` has D=13 and every proper least gap at least 48,
yet its least carry 319 is coprime to D. Coarse gap magnitude cannot
replace the full congruence grid. The 35/5/7 word/root/barrier counts
separate the physical least root from a coefficient barrier.

The counting obstruction is exact at every admissible fixed clock.
Every primitive rotation orbit has A words and one least root, and
the full-D zero subset is rotation-invariant. Therefore
`|W|=A|R|` and `|Z|=A|Z intersect R|`; selecting a root changes no
integral proportion. The identities also hold for rotation-invariant
weights. A fixed-clock exponential tilt is constant on the word set.
The gap gcd follows from one even transition and one odd transition;
it recovers `gcd(D,C_0)` and gives no independent arithmetic savings.

Read the primary Halbeisen–Hungerbühler carry and Lemma 9 passages.
Their classical rotation/gcd contribution is credited. The note's
comparison with Paper 87 is only a comparison with its stated
conductor window, not a root audit of the entire external manuscript.
Its window does not directly supply discrepancy at the exponentially
fine ordinary-source interval in this attempted application.

**Boundary:** five finite Lean statements establish the determinant,
transport, full divisibility propagation, least gap and suffix barrier.
Necklace counting, the gap gcd and source-window comparison remain
written. No unrestricted cycle exclusion or improved zero-fibre census
is claimed.

## 4. Execution and continuity

Root fresh compilation rebuilt the three unchanged dependencies and
three new modules, then audited all 25 public statements. All seven
commands succeeded with warnings as errors; only the ordinary three
listed Lean axioms appear. Normal and optimized Python replay both
succeeded with identical output. The receipts bind the compiled and
executed bytes. The final added triadic corollary changed only its
written note; the compiled and executable files remained unchanged.

The three source authors were assigned disjoint paths. Separate agents
reconstructed the triadic and actual-law arguments; the principal
cycle review above is independent of its author. These reviews remain
internal research evidence. The new files are additive; all 40 older
tracked Lean sources are checked against the parent bytes in the
source binding. The repository gate checks frozen structural contracts,
not the correctness of an unformalized mathematical argument.
