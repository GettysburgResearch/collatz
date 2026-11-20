# Independent review of the valuation-one transport packet

**VERIFIED at the narrow V1--V5 claim level. Full five closure remains
OPEN.** This review reconstructs the ordinary identities, joint endpoint
fiber estimate, and residual-family calculation. It does not turn the
uncovered energy into a finite quantity.

## Frozen inputs and scope

The reviewed worktree files have SHA256:

- `VALUATION_ONE_TRANSPORT.md`:
  `a47dd19445db7cf9f8e3e4522686161b39679866e0701f8ac05ecbda292f3422`;
- `check_valuation_one_transport.py`:
  `3f7d137c73790daceb122a1f05a94dfe9b1202bfc742586c12ea7f7c4b29cc2f`.

The prior ladder dependency was read from the complete checkout at
PR166 `5996b9f525ca50978bc34f423192c36a87765bf3`, paths
`research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md`
and `LADDER_RENEWAL.md`. In particular its physical A-block identity,
source-cylinder partition, `q<=x/7` bound, and initial-domain density
`1/24` are correctly used.

The PR146 comparison is source-qualified to
`fd991063721e9c157d318e40bb20131762f7d750`,
`research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`.
The verdict applies to the frozen packet, not automatically to a later
repository head or a revised note.

During review, the independent refresh found PR167
`e83cc8b35ad614c616df7c00318cc9645a174c34`,
`research/least-failure-closure-20261121/EXPANDED_FIVE_RENEWAL.md`,
ER1--ER3. It already includes V1's B-block and a stronger renewal on
a larger domain. The author has now explicitly credited that source,
as well as PR168 and PR169, and describes V1--V3 as independent
rederivations and a smaller-domain cross-check. This is the correct
comparison to the refreshed sources; the review does not assert those
transport families are new.

## V1 and V2: physical transport and compiler

**VERIFIED.** The four source odd positions `0,1,2,3` have affine
correction `65`, while the target positions `0,1,3,8` have correction
`325=5*65`. With total clock `b+3` and four odd inputs on both arms,
the full target numerator is exactly five times the source numerator.
For `b>=6`, every target exponent is positive. Full numerator
divisibility modulo `3^4` implies each successive inverse division by
three is integral; this follows by reducing modulo three, dividing by
three, and repeating. The integer inverse outputs are odd and positive.

No target intermediate value can be one: starting from `5q>=5`, an
inverse output one would require `2^a u=4` with odd `u>1`. On the
source side the last inverse is at least `21q`, and the three inverse
valuation-one steps decrease to a source still greater than `q`.
These facts justify the first-hit statements used in composition.

The two-way cylinder description follows from `81x+65=0 mod512`.
Its unique residue is `271`, which also gives `x=7 mod8` and hence
the exact first three valuations one. The fourth valuation is at
least six. The endpoint is automatically a ternary unit. The height
bound follows from `6(81x+65)<=512x` for every such `x>=271`.

The B-cylinder is disjoint from all A-cylinders by its first valuation.
Its relative density among odd ternary units is `1/256`; adding the
source-qualified A density gives `35/768`. This counts initial blocks,
not complete supported source certificates. The compiler's parsing is
unambiguous, its finite termination uses only the supplied word length,
and appending the actual edge `5->1` adds exactly one odd input and
four shortcut steps. Unsupported valid words remain unresolved.

For the closed family, `2^31=65 mod243` and `2^54=82 mod243` give
`x_k=2k mod3` in addition to the required divisibility modulo 81.
The first-hit words stated in V2 follow directly from the B identity.

## V3: the uniform subcritical coefficient

**VERIFIED.** Set `s=21/25`. For a fixed odd ternary-unit endpoint `q`,
the complete A-source fiber for run length `r` occupies one exponent
progression of period `2*3^r`, while the B fiber has period54.
Positive affine correction implies that consecutive sources grow by
at least the corresponding power of two. Deleting nonunit sources
only reduces the sum. Distinct blocks do not double-count a source.

The following coupling is essential and valid:

- If `q!=7 mod27`, an A-block of length `r>=2` cannot have `b=4`.
  Integrality would imply `4q=1 mod3^(r+1)`, hence `q=7 mod27`.
  Thus `b>=5` and
  `x_b>=(52/5)(4/3)^r q` for `q>=5`.
- If `q=7 mod27`, then `q=7` has zero defect because both 7 and 35
  reach 1. Every remaining odd endpoint is at least 61. Thus all A
  fibers satisfy `x_b>=(324/61)(4/3)^r q`.
  In the same endpoint class, B-integrality gives
  `2^(b+3)=17 mod27`. Since 2 has order 18 and `2^15=17 mod27`,
  `b=12 mod18`; in particular `b>=12`.

The full normalized fiber sums, using the packet's exact power
inequalities, are bounded respectively by

\[
\frac{32}{155}+\frac{512}{1085}+\frac8{31}
=\frac{1016}{1085}
\]

and

\[
\frac{3144}{3317}+\frac1{128}
=\frac{405749}{424576}<1.
\]

The first coefficient is strictly smaller than the second. The B
height estimate in the second case is
`y_b>=(32755/81)q`; raising the claimed power comparisons to 25
checks them by strict integer inequalities. Its period54 geometric
sum is bounded by `(1/129)/(1-1/129)=1/128`.

The cutoffs are carried correctly: A endpoints satisfy `q<=x/7` and
B endpoints `q<=x/6`, so all endpoint terms from sources at most `X`
lie in `E(X/6)`. The finite-cutoff inequality is therefore

\[
E(X)\le R(X)+\frac{405749}{424576}E(X/6).
\]

Subtracting a multiple of the finite sum `E(X)` before taking
monotone limits gives the factor `424576/18827`. No infinite
quantity is subtracted. No convergence of an arbitrary endpoint is
assumed, and finiteness of the complement remains unproved.

## V4: the unresolved rank-two family

**VERIFIED.** For `z_k=(2^(6k+5)-5)/9`, the actual source word is
`(1,6k+4)`. Two shortcut steps on its multiplied companion give
`-5+5*2^(6k+3)`. The three-step block

\[
-5+2^e c\longmapsto-5+9\cdot2^{e-3}c
\]

has exactly two odd inputs whenever `e>=4` and `c` is positive odd.
Applying it `2k` times gives `40*81^k-5`. Three further shortcut
steps give `5(3^(4k+2)-1)`, whose exact two-adic valuation is three;
three halvings give the claimed odd endpoint `w_k>=5`.

The total clock is `6k+8`, and the odd count is `4k+4`. Every earlier
value is greater than one. Since the endpoint is odd and at least 5,
an eventual first hit needs at least one further odd input. This
proves the stated lower bound `4k+5` without asserting that all such
endpoints converge. The compiler correctly excludes the source's
initial valuation pattern.

## V5: the one-then-threes decoder and two-antecedent form

**VERIFIED.** Summing the geometric correction gives, for the source
word `(1,3 repeated r times,b)`,

\[
5B=3^{r+2}+2^{3r+4}.
\]

With `p=r+2`, each of the `p-1` decoder steps subtracts its leading
power of three and divides by exactly two: the remaining parenthesis
is odd. The final residual is `3+2^(2r+3)>1`, whereas a correction
with exactly `p` positions must terminate at one. This proves that
every word in the stated family fails the homogeneous same-resource
test, independently of the terminal exponent `b`. It does not exclude
later prefixes with additional general letters or transformations
which change the target resources.

The two-antecedent reformulation is also exact. If the first exponent
of an odd unit `q` is one, then `u=(3q+1)/2` is odd, `u=2 mod3`,
and `u!=5 mod9`. Those conditions also give the converse ordinary
unit `q=(2u-1)/3`. Its multiplied arm satisfies `T(5q)=5u-2`.
Therefore the proposed implication from convergence of `q` and
`5U(q)` to convergence of `5q` is exactly the stated restricted
implication from convergence of `u` and `5u` to convergence of
`5u-2`. The review proves the equivalence, not that implication.

## Execution evidence and limits

The reviewer separately executed the frozen author checker with
`python -X utf8 -B` and with `python -OO -X utf8 -B`; both completed
successfully. Their JSON outputs are saved as
`witness-cross-review-normal.json` and
`witness-cross-review-optimized.json` in the review directory. They
are byte-identical to the author's supplied report. These are
independent executions of the author program, not a second independent
implementation. The independent part of this review is the proof
reconstruction above.

No correction is required at this frozen hash. The closest unsupported
closure step is still a bound on the residual energy, or a total
ordinary transport from every residual failure into the covered
initial-block domain. Neither V1--V5 nor the bounded replay proves it.
