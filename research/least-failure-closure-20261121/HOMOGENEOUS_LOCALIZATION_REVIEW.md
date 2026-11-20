# Independent review of homogeneous localization

**Disposition: no gap found in LC1--LC4 at the frozen hashes below.**
The paired-prefix equivalence is valid for complete homogeneous transports,
and the explicit infinite family has the stated first-hit resources.
These results constrain this certificate architecture; they do not exclude
physical five-closure or general adaptive certificate transfer.

## Frozen scope and replay

| Artifact | SHA-256 |
|---|---|
| `HOMOGENEOUS_LOCALIZATION.md` | `90ad2bba3c3ee9a7c22b3369ac1b3dcc2b1d1cc536e8d670368cd0579219c775` |
| `check_homogeneous_localization.py` | `7e0bb2f9441cbe5883e3bd825920fa2a0719c15d9f8d04b75476f8bfbf4c3601` |
| Normal and `-OO` reports | `2c7d2f0ca68288918ef097c12d128fcdfb3af3519906dffe41956280e94e22de` |
| HT1--HT2 source, `HOMOGENEOUS_FIVE_TRANSPORT.md` | `f2872fad5c04e3aba9219f4b54576ef438d2922d7dcad9b0a8423974c4d2c31b` |

Both checker modes were independently rerun. Their complete reports are
byte-identical to each other and to the frozen author report. Source
inspection confirms that the checks use explicit failures, not Python
assertions. Fixture searches have a finite 10,000-odd-step budget and
are followed by literal ordinary shortcut replay; they are not a universal
convergence search.

## LC1: cancellation and the first-hit boundary

The two supplied prefixes consume exactly the same shortcut clock `L`
and odd count `p`. Determinism forces any complete homogeneous target
path to begin with that actual target prefix. Its endpoint `5q` is odd,
so the cut is an accelerated-word boundary; subtracting the prefix leaves
exactly the clock and odd count of the source suffix. This proves necessity.
Concatenation proves sufficiency, and HT1 uniqueness identifies the result.
No dictionary factorization is assumed, so allowing blocks to cross this
boundary cannot evade the argument.

The source condition that 1 has not appeared before the prefix endpoint
is essential to identifying the concatenation with the first-hit source
certificate. It is stated explicitly. When `q=1`, its suffix is empty,
and the supplied target prefix already ends at 5; the empty target suffix
is the correct recognized result. Appending the actual exponent-four
edge `5->1` then finishes the target witness.

A positive shortcut orbit that has reached 1 stays in `{1,2}`. Thus an
actual target prefix ending at `5q>=5`, or a complete homogeneous target
path ending at 5, cannot have an earlier hit of 1. The first-hit claim
therefore does not assume an unproved target minimality property.

## LC2: the prescribed-endpoint lift

The PR146 prefix has clock 71 and 37 odd inputs on each arm. Appending
`b` halvings to the even endpoints `2^b q` and `2^b 5q` preserves that
odd count and gives common clock `71+b`, as required by LC1.

For `k>=0`, parity-prefix lifting changes every earlier seed state by a
nonnegative amount. The seed endpoint is greater than 1, so its ordinary
prefix has no earlier hit of 1. During the appended halvings, 1 can first
appear only at the final source endpoint when `q=1`. Hence the source
first-hit hypothesis holds for the stated lifts, including that endpoint
case. Refining the binary or ternary source progressions does not change
this path argument.

Independent replay confirms the four table entries:
`v` has rank/clock `(78,144)`, `5v` has `(67,129)`, `a` has
`(115,215)`, and `5a` has `(104,200)`. Their failure of homogeneous
recognition is correctly distinguished from convergence: all four
ordinary first-hit certificates are actually replayed.

## LC3: universal algebra for the infinite family

The recurrence

\[
x_1=49,\qquad x_{j+1}=64x_j+49
\]

proves positivity, odd integrality, `x_j=49 mod64`, and `x_j=j mod3`
for every `j>=1`. Thus the odd ternary-unit members are exactly those
with `3` not dividing `j`.

The two first odd successors are, respectively,

\[
U(x_j)=\frac{7\,2^{6j-2}-1}{3},\qquad
U(5x_j)=\frac{35\,2^{6j-5}-1}{3}.
\]

They are positive odd integers. Direct substitution gives first
exponents 2 and 5 and then exponents `6j-2` and `6j-5`, landing at
7 and 35. These last exponents are positive even at `j=1`. The
intermediate states are at least 37 and 23, so neither prefix has an
early visit to 1.

The remaining literal odd paths are

\[
7\to11\to17\to13\to5\to1,
\qquad 35\to53\to5\to1.
\]

Their words are `(1,1,2,3,4)` and `(1,5,4)`. Consequently the complete
source word has exactly seven odd inputs and clock `6j+11`, while its
multiple by five has exactly five odd inputs and clock `6j+10`.
These are first-hit resources for all `j`, not a pattern inferred from
the ten finite family controls.

The source-7 suffix cannot be homogeneously recognizable: success would
give the first-hit target-35 resources `(6,15)` by HT2, whereas its
actual first-hit resources are `(3,10)`. LC1 propagates this failure to
every member of the family. This is compatible with both arms being
explicitly convergent and with the initial two-input ladder being legal.

## Scope

The note does not infer that a sufficient residue class is physically
unsolvable, that five-closure fails, or that independently certified
terminal families are unavailable. Its conclusion is exactly that the
homogeneous recognizer's status is unchanged by the supplied paired
prefix. Different clocks, different odd counts, other endpoints, and
independent endpoint certificates remain outside this restriction.
