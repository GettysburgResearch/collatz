# Coordinator review: ordinary arithmetic continuation

**Status: Collatz remains open.** This report records the coordinator's
reconstruction of the mathematical arguments, the scope of the independent
reviews, and the checks actually executed for the continuation of commit
`a30402b7849c437edf245974d9f436d1f105e08e`. It is not a formalization of the
whole written packet and makes no literature-priority claim.

The scientific entry point is
[the packet README](../../../research/high-variance-closure-20261124/ordinary-arithmetic/README.md).
The source and runtime provenance is in
[SOURCES.json](../../../research/high-variance-closure-20261124/ordinary-arithmetic/SOURCES.json).
The final byte identities are recorded in [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json).

## 1. What is actually formalized and executed

I executed the packet's replay runner against Lean 4.34.1, compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with Mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`. It copied the project sources into
an empty temporary directory and compiled them in dependency order, with
`-j1 -DwarningAsError=true -DautoImplicit=false`. It did not reuse project
`.olean` files. The pinned prebuilt Mathlib and package runtime was used.

| Module | Public declarations audited | Scope |
| --- | ---: | --- |
| `QuarterShift` | 5 | Rebuilt dependency: physical identities and the finite base below 20 |
| `BiasedParity` | 5 | Rebuilt dependency: high-prefix bounds and the earlier real-series criterion |
| `DyadicCompanion` | 4 | New: numerator-height decrease, a small-value visit, the finite forbidden-class check, and impossibility of an all-time positive integral companion above the physical floor |
| `ResetAncestor` | 4 | New: unique parent, exact ancestor toll, prescribed delayed merger, and at least one nonperiodic branch |
| `PeriodicBoundary` | 3 | New: all-state reachability in the canonical affine-pair process, its exact lift, and aligned numerator identities |

All **11 new** and **10 dependency** audits passed. The printed axiom sets
contain only subsets of `propext`, `Classical.choice`, and `Quot.sound`.
There is no admitted proof, custom axiom, or native-decision axiom in these
audited declarations. This is a statement about the declarations and
dependency closure in the receipt, not a claim that every file elsewhere
in the repository was Lean-compiled.

Four exact finite controls also completed in normal and optimized Python,
with identical paired outputs. The eight executions cover:

- finite dyadic prefixes, incorrect triadic candidates, small integral
  companions, and the concrete ordinary oscillation examples;
- exact selector/CRT/ancestor identities in the synthetic reset family;
- rational seed cycles, the actual fixed-root cross-level merger, all
  admissible exponent residues for the `1011` bound, and the terminal
  three-source fixture;
- the two-step negative-center kernel inequalities, finite Green moments,
  and the missing-pole obstruction fixtures.

The controls are diagnostic finite arithmetic. In particular, the reset
control does not instantiate an entire infinite wrapped cutoff bank, and
the finite prefix/candidate tests do not prove universal arithmetic
membership. The full command, actual stdout, exit codes, source hashes,
and axiom lists are in [REPLAY.json](REPLAY.json). It records success.

## 2. The dyadic companion and the exact arithmetic gap

I reconstructed the finite telescoping and shift identities for

\[
 A_i=2^{i+P_i}/3^i,\qquad B_k=\sum_{i<k}e_iA_i,\qquad
 D(n)=\sum_{i\ge0}e_iA_i\in\mathbb Z_2.
\]

The valuation of each term tends to infinity, so the dyadic definition
does not require physical convergence. The finite identities are

\[
 2B_k=3A_k-3+\sum_{i<k}A_i,
 \qquad D(n)=B_k+A_kD(T^k n).
\]

The physical parity is recoverable from the companion: it is even at an
even source, while at an odd source it is 1 modulo 4. The two exact
companion updates are `3d/2` and `3(d-1)/4`. Thus, if `D(n)` is rational,
all subsequent reduced denominators divide its initial odd denominator.
The dyadic integrality is what permits this denominator assertion; it is
not an ordinary-real convergence assumption.

If the physical source never reaches 1, the checked finite base gives
`x_i>=20`. The earlier high-prefix theorem gives
`A_k^5 >= (256/243)^k/n^3`, and the telescoping identity then makes `B_k`
unbounded in the real ordering. A rational initial companion therefore
eventually becomes negative. On that tail, put `w_i=-D(x_i)/3>0`.
The coupled real updates are

\[
 (x,w)\mapsto(x/2,3w/2),\qquad
 (x,w)\mapsto((3x+1)/2,(3w+1)/4).
\]

The height `x^2 w^3` decreases by the factor `27/32` in the even branch.
For `x>=20,w>=64`, the odd factor is at most
`26750481097/26843545600<1`. I checked the exact rational constants.

If the orbit is not eventually periodic, its physical states are distinct
and tend to infinity. Equal companion values at two states would force
all subsequent parity bits to agree. The usual finite parity congruence
then makes the two ordinary states equal modulo every power of two, hence
equal. Thus the positive tail values `w_i` are also distinct; bounded
denominators imply that they tend to infinity. The two coordinates must
eventually stay in the contracting region, which is impossible. This
proves the written implication from rational companion to eventual
periodicity. Conversely, a periodic tail makes the dyadic series a
geometric rational series with ratio `2^(l+p)/3^l != 1`.

The stronger assumption `D(n) in Z[1/3]` loses one power of three in its
denominator per update and eventually produces an integral companion
divisible by three. On a nonhitting orbit this gives a positive integral
`w`. The new Lean theorem excludes an all-time such path above 20. Its
small-value step checks every integer 2 through 63 reaches the forbidden
class 3 modulo 4 within 17 steps. The remaining value 1 forces every
physical step to be odd, hence `2^k` divides the fixed positive integer
`x_0+1` for every `k`, a contradiction. The reverse implication starts at
`D(1)=9` and propagates backwards through the finite physical prefix.

This establishes the two written classifications

\[
 D(n)\in\mathbb Q\iff n\text{ is eventually periodic},\qquad
 D(n)\in\mathbb Z[1/3]\iff n\text{ reaches }1.
\]

The Lean integer consumer does not formalize the dyadic construction or
either complete equivalence. Neither the written argument nor its Lean
kernel proves universal rationality or universal `Z[1/3]` membership.
[SERIES_REVIEW.md](SERIES_REVIEW.md) contains the independent reconstruction.

### Effective separation from one incorrect candidate

For `a=A/3^h`, the proof sets
`N=5+h+ceil(log2(n+1))+ceil(log2(|A|+2))` and obtains

\[
 D(n)\ne a\implies v_2(D(n)-a)\le10^6N.
\]

I reconstructed the coarse constants, including the loss of at most two
bits per trial update. Agreement beyond `10^6 N` keeps the trial dynamics
legal through `430000 N` clocks. After `h+1` updates the trial is integral
and divisible by three. Unless the physical path already enters the
checked base, the high-prefix estimate makes the trial negative by clock
`160 N`; the associated initial joint height is at most `2^(805 N)`.
The exact inequality `2*theta^256<1` forces entry to a small physical or
companion value within a further `206080 N` clocks. A small companion
other than 1 fails within 17 steps. Value 1 cannot support the remaining
all-odd physical segment because it would force more divisibility of
`x+1` than its height allows.

The remaining physical values below 20 reach 1 within 31 steps. Their
companions have denominator at most `3^31<2^50` and absolute value below
`2^20`. The nonzero terminal rational difference therefore has binary
valuation at most `t+3N+71`; transporting it to the initial state gives
at most `3*(210000N)+3N+71<10^6N`. This supplies the contradiction.

The result decides equality with one specified triadic rational by a
finite prefix. It supplies no bound on a successful candidate's height.
The text's quadratic-irrational example explains why a comparable
separation property alone cannot establish rationality.

I also checked the infinite binary-section rank argument. At positive
ordinary sources, dyadic difference quotients tend to zero because the
number of odd steps tends to infinity. At zero, the quotients along
`2^j*3^p` have fixed nonzero dyadic norm. Evaluating a putative finite
linear dependence at the least-index singular center isolates that
coefficient. This excludes a finite linear binary-digit representation;
it excludes neither arbitrary algorithms nor a different arithmetic
construction.

## 3. Deterministic merger across boundary levels

The written all-cylinder statement is stronger than a computation on
small offsets. For arms `u,3^s u+D`, refining a binary residue class lets
one prescribe the next anchor parity, since its slope in the remaining
quotient is odd. At positive grade, even offsets can be halved, zero can
be made nonzero, and an odd offset reduces the grade. At grade zero the
two-step operations on odd offsets of magnitude greater than one give
`(3D-1)/4` or `-(3D+1)/4`, strictly reducing the absolute value. The unit
offsets have explicit three-bit absorbing words. The Lean reachability
proof quantifies over every canonical state; the interpretation as a
refining physical cylinder is written mathematics.

For a persistent oriented boundary with rational address `alpha`, the
ordinary endpoints at level `i` are dyadic lifts of the signed rational
seeds. Up to their native clock the identity is

\[
 T^u(n_i+e)=2^{i-u}3^p\alpha+T^u(x_i+e).
\]

If one left seed and one right seed have eventually periodic futures
with positive odd counts per period, their dyadic levels can be chosen
on different progressions so that their odd-grade increments agree.
The resulting endpoints are fixed affine arms along `3^(Ch)`, for an
even positive `C`. The elementary valuation formula for `3^C` makes
this parameter fill every refinement of one open binary ball. It
therefore enters the finite merger cylinder for an actual pair from
the same original ordinary root. No independent resampling or
probability statement occurs in this step.

For the address repeating `1011`, the rational cycles have odd
frequencies `1/3` and `3/5` and are disjoint. At left level `8+36h` and
right level `8+20h`, both ordinary endpoints have odd grade `5+12h`
and differ by three. Their common parameter satisfies

\[
 5u_h-4=3^{12h+4}(15n+11).
\]

The root-17 control uses `h=6`, giving levels 224 and 128 and a merger
ten added clocks later. Unlike the pure-triadic case discussed below,
`1011` is allowed by the previous even-zero-gap forbidden-word test.

### Why the 9,209 bound is a uniform finite-word certificate

Modulo `2^16`, `u_0=243n+179` runs over all residues, and the exponent
update is the permutation
`u -> (3^12*(5u-4)+4)/5`. A preceding four-bit word different from
`1011` implies `v_2(15n+11)<4`, hence excludes exactly the 4,096
residues with `5u-4=0 mod 16`.

The executed control covers the other 61,440 residues in 32 complete
permutation cycles. A hit means equal endpoints **and equal odd
counts** for `u,u+3` within 16 clocks. Since all source parity bits
in that window are fixed modulo `2^16`, the two affine endpoint slopes
also agree. A hit therefore certifies every positive lift of its
residue, not just the small representative.

The longest cyclic run of failed exponent parameters is 1,023, so a
hit occurs with `h<=1023` from any permitted starting point. The
larger native level is at most `8+36*1023=36836=4*9209`. A finite
prefix consisting of a different four-bit block followed by 9,209
copies of `1011` thus already forces the contradicting pair of
component colors. The added physical merger clocks require no extra
dyadic address bits after those ordinary sources have been fixed.
This is an exact Python certificate, not a Lean theorem about 9,209.

There is no contradiction with the early-clock obstruction. The two
adjacent endpoints at the **same** sufficiently high level cannot meet
through any two clocks at most `(1+delta)i`, for fixed `delta<4/15`.
Their native leading grades have a linear discrepancy. The only
non-elementary input in this delay estimate is the fixed-base
two-logarithm consequence of Gouillon's Corollary 2.3: a nonzero
linear form with coefficients `O(i)` has a polynomial lower bound,
which contradicts the required exponentially small upper bound.
The cross-level alignment and periodic-ray exclusion do not use
Gouillon. I read the primary paper and checked this exact use.

The pure `3^d` denominator exclusion for `d>=2` is explicitly credited
as overlapping prior work: the old forbidden word `100` already
excludes those addresses. Rational seeds with zero odd-grade cycles,
and arbitrary aperiodic boundary addresses, are outside the new
criterion. Rationality of an address is not by itself a proof that
its positive rational seed orbit is periodic.

### Terminal extension and its missing center

For each fixed positive `b`, every infinite arithmetic progression
of nonnegative exponents contains a subprogression on which

\[
 2^k b-1,\quad 2^{2k}b+1,\quad 2^{2k+1}b+1
\]

share a future. Their native endpoints are `u=3^k b-1`, `u+2`, and
`2u+3`. Restrict to an even-stride exponent progression. First use
the gap-two merger ball, then refine the remaining progression to
merge `2u` and `2u+3`; `2u` itself maps to `u`. Both previous
congruence conditions are preserved. This yields a common future
of the three original positive sources, with possibly different
physical clocks.

The concrete `b=5,k=51` fixture reaches the same integer at clocks
72, 123, and 124. I added that fixture to the public control before
the successful root replay. The independent reviewer also executed
the original three starts directly. Two eventual punctured-side
colors cannot differ under this result, but neither side has been
shown to share the center `b`'s own component.
[BOUNDARY_REVIEW.md](BOUNDARY_REVIEW.md) records the final reviewed
prose and the terminal addendum.

## 4. The reset counterfamily, repair, and remaining loss

I reconstructed the quantifiers in the counterfamily: it applies
to every allowed cutoff bank `B_j>=2^(j^2)` and every positive
summable choice of weights for which the earlier `G` is finite.
It does not posit one orbit that escapes.

At `x=8 mod 18`, the child `z=x/2` is 1 modulo 3 and has the unique
physical parent `x`. The cheaper ordinary ancestor
`m=(4x-5)/9` makes two odd steps to `x`, with `m+2<=z`. These
identities force the ancestor minimum to inherit its price and
give `b_*(x)=b_*(z)` at the marked edge. The Lean module checks
these finite ancestor and delayed-collision mechanisms.

The construction of arbitrarily large marked edges requires the
additional written selector and cutoff argument. The selector
accepts `7*3^a+C` uniformly for `1<=C<=sqrt(s)` once large; the
other tested powers of two are separated by the elementary
integer lower bound on their logarithmic phase difference.
Writing `C_j=min_{h>=j} B_h/3^h`, the quadratic lower growth forces
infinitely many large increments in `log(C_j)`. At these indices,
the two CRT-selected starts lie in `[B_j,10B_j)`, and the next
cutoff level cannot wrap across them. The separated starts then
give the exact marker profile: `J=j-i` before the exit and no
mark through the next `j` clocks. The two distinct branches
coalesce one clock after the prescribed common halving prefix.
Since a deterministic map is injective on its periodic points,
at least one whole chosen prefix is nonperiodic.

Consequently there are actual edges with `J(x)=1`, equal complete
ancestor toll, and `t_1(Tx)>=j+1`. The exact debit of the previous
score is

\[
 4(W_2-w_1t_1(Tx))\le4W_2-4w_1(j+1)\longrightarrow-\infty.
\]

This closes the proposed universal reset inequality negatively.
Bounded signed ancestor charges cannot pay the unbounded refill
on those unique-parent edges either.

The signed repair is a substantive second attempt. With
`v(x)=1/((K+log(x+1))*log(K+log(x+1)))`, the charge
`c=v*(1-3*1_M)` has a positive lower budget on every finite actual
path: `sum c >= .1 sum v-C_0`. The proof assigns disjoint windows
of length `4h` to the marked positions; at most `h` places are
marked and the large-`K` weight variation is at most `6/5`.
The endpoint errors have a uniform bound.

The resulting ancestor infimum is finite, proper, attained, and
computable with the canonical bank. It pays at least `2v` at
every marked edge, including periodic sources. It can lose `v`
at an unmarked edge, and actual unmarked edges attain that loss.
Although `v=o(1/log x)`, its sum diverges on every infinite
positive trajectory by the elementary exponential upper bound
on physical height. Thus paying the resets does not complete
global descent. [RESET_EXIT_REVIEW.md](RESET_EXIT_REVIEW.md)
independently reconstructs both the counterfamily and this repair.

The accompanying origin-count theorem uses the already pinned
strict-power occupation estimate only on a single hypothetical
escaping orbit. Every strict improvement over the inherited
ancestor price has a new minimizing origin. Short incoming paths
land on that same sparse orbit. For long paths, the exact full
carry identity forces a high odd count; the binomial entropy
bound then gives a strict power saving in the number of possible
origins. The number of discounts is sublinear in the intrinsic
budget. Their magnitudes are not controlled, so this is not an
unpaid-loss summability argument in disguise.

## 5. Ordinary oscillation and the negative-integer attempt

I reconstructed the ordinary residue-lifting calculation for the
near-neutral rational cycle and the expansion factor. Monks's
Theorem 1.1 supplies arbitrarily large basin-of-one endpoints in
the required translated progression. The resulting starting
integers themselves converge and have actual forward endpoints
arbitrarily close in relative size, in the same prescribed residue
class, with arbitrarily large series multiplier. Thus the claimed
local smooth supersolution estimate fails on ordinary convergent
inputs, not only on dyadic or rational surrogate states. I read
the primary Monks paper and checked that the use is the
arithmetic-progression sufficiency theorem, with no assumption
that all starting integers converge.

The consecutive-source construction uses the paired arms
`3^k t-1,t`, a fractional-moment bound on random parameter
prefixes, and the source-qualified almost-sure affine-merger
result at PR146's pinned commit. After a finite merger and a
small-tail cutoff, the ordinary lift to a common power-of-two
endpoint is exact. This gives convergent consecutive integers
whose real series values tend respectively to infinity and 3.
I checked the finite lifting and tail estimate; the full
probability proof is retained as the named prior input, not
reported as newly Lean-verified or independently re-proved in
this packet. That qualification is explicit in `SOURCES.json`.

The coordinator's separate negative-integer Green kernel supplies
a finite potential at every positive ordinary input without any
Collatz assumption. With the exact affine function
`f(h)=h+32/13`, the two-step inequalities are
`K^2 f <= (76/81)f` and `Kf <= (10/9)f`, giving total first moment
at most `1539/13` from the initial center 1. The four exact
residue rows were checked algebraically and by the control.

The intended supersolution fails for a structural reason. A
nonzero nonnegative measure on negative integer centers, with
finite first height moment, cannot satisfy the required positive
source inequality. An atom whose odd pullback is a nonintegral
rational pole gives ordinary lifts on which the normalized
right side stays positive and the normalized left side tends
to zero. Finite first moment supplies the domination needed for
this limit. If every atom lies in the remaining class 1 modulo
3, its even pullback lies in a forbidden residue class and gives
the same contradiction. Constants or any `o(n)` additive repair
also vanish in this normalization. The argument is specific to
the discrete finite-first-moment class; diffuse measures and
rational centers are not excluded.
[NEGATIVE_KERNEL_REVIEW.md](NEGATIVE_KERNEL_REVIEW.md) is the
independent mathematical review.

## 6. Provenance, source edits, and publication scope

The three research streams were run by GPT-6.2 Astra agents with
separate assignments; their principal arguments were sent to
different agents for mathematical reconstruction. Reviews are
evidence of scrutiny, not substitutes for kernel checking.

The scientific prose and Lean files were copied from the final
reviewed drafts. The coordinator wrote the README, sources,
negative-kernel note/control, replay runner, this review, and
manifest. The boundary control received one additional terminal
fixture before the root replay. The boundary reviewer pins its
own earlier control bytes; `REPLAY.json` pins the final public
control with that additional fixture. The README received the
reviewer's clarifications distinguishing an orbit that is not
eventually periodic from a merely transient source and allowing
early entry to the physical base in the candidate argument. The
coordinator also clarified that the delay concerns adjacent
endpoints at the same level. These do not change a proof source.

The current-repository intake is frozen at the heads in
`SOURCES.json`, with the exact read scopes stated there. Those
other PRs are context, not automatically imported theorems.
Monks and Gouillon are the only new primary literature inputs.
Brofferio and Furstenberg were read as motivation; their
probabilistic results or conjectures do not close the ordinary
source gap here.

`PREVIOUS_PR182_DESCRIPTION.json` preserves the exact previous
57,806-character PR description in its `body` field, before
replacing that long description with a concise current one.
The JSON archive retains the original Markdown line-break
whitespace. It is earlier status history, not new mathematics.

The final repository integrity validation and remote byte
readback will be recorded in the updated PR description against
the published commit. A self-containing commit receipt is not
claimed here. This packet's embedded execution receipt verifies
the listed source bytes and the stated declarations and finite
controls.

The central missing conclusions remain explicit: universal
`D(n) in Z[1/3]`, exclusion of all surviving boundary addresses
and center-side separations, or a finite nonnegative score that
pays every actual loss. This checkpoint proves none of those
universal assertions.
