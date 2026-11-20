# Independent review of the homogeneous five compiler

## Reviewed bytes and disposition

The reviewed proof is `HOMOGENEOUS_FIVE_TRANSPORT.md`, SHA-256
`f2872fad5c04e3aba9219f4b54576ef438d2922d7dcad9b0a8423974c4d2c31b`.
Its checker is `check_homogeneous_five_transport.py`, SHA-256
`304e290bb3c0215d1cd5fe2f4f290c4ed8f3ef629912106f0c936105ab59fd97`.

**Disposition:** no mathematical defect found in HT1--HT5 at their
stated ordinary domains and architecture scope. The complete compiler
recognizes same-odd-count, same-clock transports to the prescribed
five-times endpoint. Full forward-five closure remains open.

The energy author previously coordinated with the compiler author on
the three four-input words and independently reconstructed those words
for the expanded renewal. This review extends to the entire frozen
proof. It is not a claim of separate discovery of the three families.

## HT1: unique decoding and actual ordinary legality

For a fixed number of odd inputs, subtracting the leading power of three
leaves a positive power of two times an odd integer. The binary valuation
therefore forces the first gap. Dividing reduces the term count by one;
induction gives uniqueness and reversing the steps gives existence.
The one-term case requires correction exactly one. The strict final
position condition ensures a positive final exponent, rather than a
zero-length last accelerated edge. Uniqueness is for the supplied odd
count, not a claim across different counts.

I reconstructed the integrality argument explicitly. If

\[
2^Lq-B=3^p x,
\]

the last correction term is `2^(L-a_p)`. Reduction modulo three
forces `2^a_p q-1` to be divisible by three. Writing its quotient as
`y` leaves

\[
2^{L-a_p}y-B_{\mathrm{prefix}}=3^{p-1}x.
\]

Induction forces every remaining inverse step. Each integral inverse
`(2^a v-1)/3`, with `a>=1` and positive odd `v`, is positive odd.
Consequently the requested exponents are exact. Applying this to
correction `5B` and endpoint `5q` constructs a path starting at the
specified integer `5x`. No residue lift replaces the supplied endpoint.

Necessity follows by subtracting five times the source affine identity
from the target identity. Both arms must have the same given odd count
and clock for this subtraction to yield correction `5B`. Those hypotheses
are explicit in the theorem and retained throughout the review.

## HT2: the precise maximality statement

A successful complete source certificate ending at 1 produces a target
prefix ending at 5. It cannot have hit 1 earlier, since the accelerated
positive orbit of 1 remains 1. Appending the actual exponent-four edge
`5->1` gives exactly one more odd input and four more shortcut clocks.
The source 1 is separately treated by its empty certificate.

Every concatenation of homogeneous blocks along a supplied finite
certificate gives one transport with its total count and clock. HT1
must recognize it. Even an adaptive infinite dictionary consumes only
finitely many nonempty blocks on that finite certificate. This proves
maximality for the named architecture; it does not address transformations
that alter the total clock, odd count, or target endpoint. In particular
it does not make an unresolved valid certificate malformed.

## HT3: arbitrary-exponent classification

I rederived the exclusions without bounding the intervening exponents.
At three inputs the required remaining power of two is divisible by
five, which is impossible. At four inputs `(1,c,d,b)`, the first target
gap is forced to be one and the remaining equation is

\[
2^u(3+2^v)=5[18+2^c(3+2^d)].
\]

For `c>=2`, valuation forces `u=1`. If `c>=3`, the resulting right
side for `2^v` is two modulo four and larger than two. At `c=2`,
the cases `d=1,2` have odd parts 23 and 7; every `d>=3` has odd part
`9+5*2^(d-2)>1`. Thus no such case survives.

For `c=1`, the cases `d=1,2` give `(u,v)=(2,5),(5,1)`.
For `d>=3`, `u=3` and `2^v=12+5*2^(d-2)`. Only `d=4` succeeds;
`d=3` gives 22 and every `d>=5` has an odd factor greater than one.
Matching the final positive gap gives exactly the thresholds `b>=6,4,4`.
The one- and two-input exclusions also hold as stated. This checks the
complete classification over arbitrary positive intervening exponents.

## HT4: whole cylinders, positivity, and endpoint bounds

For every nonnegative integer lift `t`, direct forward calculation gives:

| Source | First three odd states after the source | Next numerator |
| --- | --- | --- |
| `271+512t` | `407+768t`, `611+1152t`, `917+1728t` | `64(43+81t)` |
| `135+256t` | `203+384t`, `305+576t`, `229+432t` | `16(43+81t)` |
| `87+1024t` | `131+1536t`, `197+2304t`, `37+432t` | `16(7+81t)` |

The first three divisions are exact on every lift. Stripping the entire
last binary valuation gives the ordinary odd endpoint. Matching full
corrections `65,73,121` with `325,365,605` verifies the two arms and
their equal clocks. The endpoint bound reduces in the middle row to
`13x>=219`, valid at its least positive source 135; the other rows give
it immediately. The ternary source guard is exactly exclusion of
`2^Lq-B=0 mod243`; the endpoint itself is automatically a ternary unit.

The three relative cylinder masses sum to `7/512` among odd ternary
units. Their first valuation words ensure disjointness from one another
and the prior ladder. The `q=1` families meet the exact modulus-81
conditions at clocks `31,30,26 mod54`; HT1 gives actual first-hit target
certificates after appending the final edge. The least-failure descent
uses the actual smaller endpoint, not an arbitrary congruent integer.

## HT5 and the examples defining the boundary

The literal pair starting at `(7,35)` reaches `(2,1)` at clock ten
and `(1,2)` at clock eleven. These two pairs alternate forever; none
of the first eleven rows has ratio five. This proves exclusion for every
positive clock, including any padded source certificate. Both starts
converge, so their invariant-label five defect is zero. The example
therefore excludes universal first-block coverage but does not refute
a renewal estimate restricted to nonzero defects.

The other unresolved example, 17, has word `(2,3,4)` and correction
53. Decoding 265 forces gap eight and then fails. Its target 85 has
actual one-letter certificate `(8)` and never visits 5. The example
correctly distinguishes failure of this architecture from failure of
target convergence.

## Executed controls and their limits

The author checker was run normally and under `-OO`. Both reruns agree
byte for byte with the supplied report, SHA-256
`e1ea543ff91648e8e59e04b354400bd05a046b0d68553af658c9b0455a489a8d`.

The separate `check_transport_review.py` imports no author checker.
It independently follows literal paired trajectories for all odd starts
through 2047 and their first eight odd prefixes. Across 8,192 prefixes,
the algebraic criterion agrees exactly with equal target clock, odd
count, endpoint, and target exponents: 95 accepted, 8,097 unresolved.
The accepted controls include 65 unit-source and 30 nonunit-source
prefixes. Its affine coefficient checks establish the three cylinder
identities in the table for every nonnegative lift. It also reconstructs
the finite pair leading to the exact period-two tail at source 7.
Normal and optimized reports agree byte for byte.

These finite controls test implementation, clocks and ordinary domains.
The arguments above, not the sampled starts, establish decoder uniqueness,
arbitrary-exponent classification, concatenation maximality and the
all-time exclusion after the identified terminal cycle. No test or
review finding is promoted to a full Collatz proof.
