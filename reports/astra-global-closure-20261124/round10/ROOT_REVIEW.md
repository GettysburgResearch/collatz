# Root reconstruction and evidence boundary

25 November 2026. **VERIFIED within the scopes below; universal Collatz remains
OPEN.** This report covers the round-ten scientific sources frozen in
[SOURCE_HASHES.json](SOURCE_HASHES.json). It does not upgrade unreviewed
statements elsewhere in any cited pull request.

## Ordinary tower route

I reconstructed the common-denominator proof rather than infer it from
finite controls. With `2H≤r`, the elementary size comparison forces the
competing source to have ternary exponent at least `H`. Both scaled affine
constants are then equal modulo `3^H` and lie in `[0,3^H)`, so they agree as
integers. Coprimality of the base with six gives `w|b`, the lower-base bound
gives `b=w`, and exact powers of two force equal clocks. The constructive
direction retains `d≤r` before forming the positive ordinary lower power.

I also checked the limitation on a freely supplied power of two. An even
endpoint can be such a power without consuming the source clock. The
specific example `T(87381)=2^17` refutes the unrestricted extension. The
all-odd cylinder instead has odd endpoints through clock `H`, so all those
source halvings must be removed within the original clock budget. The
review and theorem state that qualification explicitly.

The two-run descent retains the additive terms in its strict size
inequality. For `m=H+1`, `e=5H+2`, `r=2H`, the stronger budget
`2*3^(m+r)≤2^(m+e)` pays those terms. The CRT construction supplies one
class of `a` modulo `3^(r+1)*2^(e+1)`, with odd positive base `w`,
`w=1 mod 3` and odd positive endpoint `b`. The first entry into the free-two
reservoir is at `H+1`; the actual smaller integer is reached at `6H+3`.
No minimum claim about the latter clock is used. The all-clock 15/5 example
shows why a universal equal-constant replacement would be false.

The final Lean assembly supplies the precise minimum application:
`0<b<w` gives `Good b` from `FirstTower.smaller` at exponent zero, and
the actual path pulls goodness back to the purported bad tower. For the
prefix maximality theorem, `f≤r` ensures the extra odd count can be removed
from the ternary exponent. These are closed scoped deductions. The final
universal theorem still takes `FrontierMerger` as an explicit parameter.
The parameter is the prior PR192 condition, already proved equivalent to
ordinary convergence; no new proof of it appears here.

[Tower peer review](rows/CLOSURE_REVIEW.md) ·
[Final consumer peer review](arithmetic/REVIEW_FINAL.md)

## Ordered cycle gaps and every nonzero rank shift

I checked the lifted recurrence before reducing the rank modulo the period.
Both the input cut and the possible additional output cut are accounted for.
The middle of a common word is constrained by the product of its past
ternary modulus and future binary modulus on that same integer gap. The
chosen word length makes this product exceed every possible gap difference.

The geometric proxy increases by at least `st/p²` per rank, with absolute
error at most `2p`. Thus a repeated integer gap has multiplicity at most
`1+4p³/(st)`. The `p/(log p)²` range in the first argument makes deletion
of cut-hitting windows cost `o(p)`. The exact entropy comparison has a small
but strictly positive margin: its first exponent after division by `p` is
less than `-0.00084`. The proof retains constants and logarithmic factors;
it claims a sufficiently large onset rather than a usable small period.

The extension charges cut labels within an explicit probability assignment
to finite codes. It assumes no probabilistic behavior of the physical
cycle. For larger rank offsets the gaps are all distinct, so the `p` codes
are distinct. AM–GM gives the necessary average code length, contradicted
by `5.12*(42/521+1/10)=60224/65125<1` under the sparse hypothesis.
Ten cyclic ranks and the Hamming triangle inequality then handle every
shift of order at least ten.

For the remaining orders, a normalized exponent and its band-change bit
uniquely determine the physical exponent. The physical word determines an
actual terminal site modulo a power of three greater than the whole height
range. This gives a separate temporal entropy bound `E_h>p/20`.
I verified the exact constant `20^640<19^608*3^125`. Each nonmonochromatic
coset of a shift of order `d` consumes at least two mismatches and has `d`
members. Every such coset meets the `b=2` arc. Edges between monochromatic
cosets cannot decrease the band there, so all temporal decreases touch the
nonmonochromatic set. Unit increases and decreases balance around the cycle,
giving `E_h≤2dE_t`. This completes `E_t>p/747` for every nonzero shift.

The source height inequalities are indispensable. PR200's `479/1000`
strip count has its ordinary minimum/excursion assumptions. Wu–Wang's
Theorem 1 has linear-form exponent `4.1163051+epsilon`; the cycle product
introduces an extra factor of the period, giving the stated `5.12` upper
height exponent. I checked the published theorem statement and its
specialization. Neither its analytic proof nor the full PR200 certificate
was re-executed in this pass.

The symbolic coloring construction retains physical edge legality but not
ordinary cycle integrality. It prevents this necessary mismatch bound from
being misrepresented as an exclusion of every physical word. The complete
denominator and the separate first-crossing branch are still unresolved.
[Independent original-gap review](rows/ARITHMETIC_REVIEW.md) ·
[Independent final extension review](rows/EXTENDED_SHIFTS_REVIEW.md)

## Literal exact rows

I reconstructed the off-center floor from the qualified central floor F.
The local floors apply at every supplied intermediate ordinary endpoint.
The full path recovers its fixed gap cuts and all intermediate clock
choices; distinct clock vectors cannot charge the same source twice.
Every block has multiplier at most one half, preserving the doubled
offset budget. The square-root factors cancel to the single global factor
up to an exponential loss in the number of blocks.

The moving-barrier upper counts original integers. For fixed first-entry
clock, odd count and landing value, the possible original values occupy a
short interval derived from the actual affine product. Summation over these
fibers transfers a complete-grid bound without resampling the selected
landing distribution. Good prefixes force timely first entries inductively.
The centered errors sum over geometrically decreasing log heights, giving
the claimed square-root error. The barrier and exception parameter obey
the stated range restrictions.

For a nontrivial fixed cyclic terminal, every counted path is its first-hit
segment followed by full laps. The shell parameter determines the lap
count up to a bounded error. The positive defect `2p-A` is the same
quantity in the lower clock displacement and the upper early-entry test.
The off-cycle predecessor is chosen above the largest cycle site.
Consequently the two bounds concern the same `q`, the same residual shell
and the same normalization; both have cost `exp(-Theta(k²/b))` in the
stated range. The trivial odd cycle has zero defect and a different lower
bound. No contradiction follows from this distinction.

The escaping-ray statement likewise retains the supplied ray and its finite
first-gate set. The all-terminal late-suffix conclusion is not asserted for
the smaller terminal window of PR207 without its additional restriction.
F remains source-qualified. The finite simple-path bound S was reconstructed
from its resident proof; the full analytic proof behind F was not.
[Independent row review](arithmetic/REVIEW_ROWS.md)

A final primary-literature comparison checked Idris Ali Shaik's
[Polylogarithmic Descent for Almost All Collatz Orbits in Natural Density](https://shaikidris.github.io/polylog/paper/),
manuscript v4.0.2 dated 4 October 2026. Its Theorem 1.1 and Corollary 1.2
already give polylogarithmic descent in natural density, centered clocks,
and separately prescribed height bounds. Its Sections 4–6 explicitly
count later first passages among original sources. Those mechanisms and
the leading clock constant are therefore not claimed as original here.
The current proof adapts the repository's specified entrance argument to a
variable exponential barrier and then applies it to the exact row shell.
No fixed-target or pointwise conclusion is imported from an almost-all
statement, and the external paper's reported Lean development was not
recompiled in this pass.

## Executed checks and limits

The root's final fresh project-cache build passed all seven modules with
warnings treated as errors: four new modules and three byte-identical
dependencies. All 65 selected transitive inventories, including 28 from
the new modules, use at most `propext`, `Classical.choice` and `Quot.sound`.
The final source hashes were unchanged throughout the build. Mathlib and
package oleans were reused at the recorded revision; the toolchain was not
rebuilt. [Execution receipt](lean/receipt.json)

The root replayed all three finite checkers both normally and with Python
optimization. Each pair produced identical output, with explicit checks
that remain active under optimization. The recorded ranges include 688
short-cone cases, 30 CRT examples, 270 complete rows, 870 cut unions,
690 offset compositions, 50,867 schedule corners and 14,880 rank windows.
Rational cycle controls are explicitly denominator-cleared controls, not
ordinary counterexamples. [Finite receipts](controls/control-replay.json)

An all-state remote readback before publication again found 166 PRs, through
PR207, with no changed heads relative to this pass's intake. The owned PR195
head was still `51e2c43a60950e446eabe782c5b1cb1d0ae11bab`, open and draft.
Publication and complete-checkout integrity receipts are separate from the
mathematical and Lean evidence. No such integrity check proves Collatz.
