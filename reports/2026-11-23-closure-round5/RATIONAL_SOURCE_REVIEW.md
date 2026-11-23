# Independent source review: exact rational recognizer and companion arguments

Date: 23 November 2026. Reviewer: triadic construction lane.
Parent checkpoint: `cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`.

**Verdict: VERIFIED within the source and mathematical scope below.**
The root authored the rational recognizer and ternary-information note;
the cycle lane authored the circuit obstruction. This review independently
reconstructs those artifacts. The triadic note and module in the binding
table are this reviewer's own mathematical inputs, independently reviewed
elsewhere by root and the cycle lane. The rational replay is also authored
by this reviewer; its oracle is independent of the recognizer's decisions.
This report is not an independent review of its author's own work.

## Frozen source bindings

Paths are relative to `research/closure-round5-20261123/`.

| File | SHA-256 |
|---|---|
| `verify_rational.py` | `91e79761fe43e092e69a2be2f9224d62c4015c4b9aed8ccf77205b4bc83091b0` |
| `replay_rational.py` | `a62cf4579f4588996085f2f3d4594d6f98b6b3e8cff973ae635df98c271df887` |
| `TRIADIC_CONSTRUCTION.md` | `40fde45d454b19a97f208aef9950a2fd6fbf0fd15cef1995b37fbf5099b8b562` |
| `TriadicConstruction.lean` | `296e622d30826fe87a63f86be63b1836497705d751c7bace5699f3755e04fc23` |
| `CYCLE_EXCLUSION.md` | `53ca400b528fa55047cb78e8c056e243932256dcd3e3c7d0fa0afd129d97ebbb` |
| `TERNARY_INFORMATION.md` | `e254b24b199c94ac5832a095dc6c428eee2d8a6628dff05546bdc855287073f4` |
| `FIXED_SOURCE_PRESSURE.md` | `09b9cb3a1bd7daf1bc77b70e5010c8591b3d1fa7965e59a63dff6efc1dbe5c76` |

## 1. Exact supplied-rational recognizer

Read every branch of `verify_rational.py` against the final equations
(15a) and (20a) of the mathematical interface. No implementation mismatch
or material defect was found.

### Input normalization and budgets

The function requires integer inputs, rejects booleans, and requires a
positive ordinary source and a positive odd denominator. `Fraction`
normalizes once, so the denominator remains positive and odd. The
decomposition into `3^r*q0` is exact, with `q0` prime to three.
The zero candidate reduces to denominator one, avoiding a spurious
positive exhaustion level.

For the general method, the computed budget is exactly
`14 bl(n max(1,abs(a)))+60q+18` for the reduced candidate.
For the mixed method, the computed initial-height and denominator
parameters match (20a). Choosing the smaller of two independently proved
budgets is sound. The automatic triadic method uses the stronger
round-four strict stopping bound `3(r+1)`.

### Literal dynamics and event decisions

Python's signed remainder gives exactly the two parity residues for
negative as well as positive integers. Both numerator branch divisions
are exact because the denominator is odd. The original state remains
the unchanged positive shortcut orbit.

Parity is checked before any acceptance. At original 1, equality
`w=2*current_q` is necessary and sufficient for the complementary
all-time tail. In a fixed odd-denominator representation, compatibility
along the original `1,2` tail implies `4^h | w-2q` for every `h`;
thus `w=2q`. This reasoning is also valid at a mixed-mode intermediate
denominator, because it concerns the current rational value itself.

The small-state dictionary records the original state and clock for
each first signed numerator value. An equal original state at a repeat
gives a complete paired period, with every parity in that period already
checked. A different original state refutes all-time compatibility:
deterministic numerator evolution would give identical entire future
original parity vectors, and finite parity coding then forces the two
ordinary integers to be equal. This rejection says nothing about whether
the original source later converges.

For example, a zero numerator opposite original 3 has a repeated small
numerator at the next original state 5. The unequal original states are
already a valid reason to reject that supplied candidate, although the
ordinary source 3 itself converges. This symbolic reconstruction was also
checked in the later executable controls reported in Section 4.

### Mixed denominator exhaustion

Before exhaustion, the current denominator changes only at an odd
numerator input, equivalently an original-even input while compatibility
holds. The unreduced numerator update is divisible by three, and the
code removes exactly that factor from both numerator and denominator.
While another three remains in the denominator, the reduced numerator
stays a unit at three. Other denominator primes cannot cancel under
these steps, since multiplication by three and division by two are
units modulo the residual denominator. Thus the maintained fraction
is the exact actual rational trajectory.

Small-numerator recording is postponed until the current denominator
has no factor three. The dictionary is consequently used only with a
fixed residual denominator; an equal numerator at two different
denominators cannot trigger a false repeat. Once recording starts, the
denominator remains fixed and the general event proof applies.

### State-clock boundary and failure behavior

`range(bound)` examines precisely clocks `0,...,bound-1`. The code
takes no additional transition after the last examined state. Thus
`ordinary_steps_executed` reports the actual transition count, including
zero at the initial state.

For general and mixed modes, the mathematical accounting guarantees
a decision event within this range; exceeding it raises an explicit
error. It is not silently interpreted as a rejected candidate. For the
triadic mode, failure to reach 1 within its strict necessary stopping
bound soundly rejects the supplied triadic candidate. An earlier exact
repeat event is also a valid rational decision in that mode.

The trace records the current numerator and denominator before each
tested state. Optional tracing does not change the updates or decisions.
The implementation never equates a short matched parity prefix with
successful all-time membership.

**Scope:** the conclusions above are a source-level implementation
review. Section 4 records this lane's separately authored bounded replay,
which executes the root's recognizer against an independent oracle.
The eight mathematical core theorems were development-compiled by this
lane before implementation review; that author compile is distinct
from root's fresh independent build.

## 2. Independent reconstruction of the circuit obstruction

Recomputed the circuit formulas for `w=1^p0^h`. The complete carry is
`C=3^p-2^p`, the full positive denominator is `D=2^(p+h)-3^p`, and
`D+C=2^p(2^h-1)`. The displayed intermediate numerators have the
claimed odd parity, followed by exactly `h` even inputs. Cancelling
an odd gcd preserves these parities. The two-run mixed cyclic word is
primitive; a shorter state period would force a shorter parity period.

At `m=C/D>1`, the least nontrivial state is the first odd successor,
with gap `(m+1)/2`; every proper state on the even run is at least
`2m`. Thus the exact least carry gap is `(C+D)/2`. The full gcd is
`gcd(D,C)=gcd(D,2^h-1)`, giving the stated lower bound on the fully
reduced denominator. No prime-power cancellation is omitted.

The irrational-rotation interval is fixed after the desired floor
threshold is chosen. It admits arbitrarily large `p`, so the floor and
root gaps can exceed every fixed threshold while the reduced denominator
also grows beyond an independently prescribed threshold. The use of
fixed interval width does not require unbounded continued-fraction
partial quotients. The complete coefficient is subcritical, while each
nonempty proper prefix remains supercritical.

The ordinary-source boundary is exact. Its first `p` odd inputs force
`n=-1 mod 2^p`, hence `n>=2^p-1`. For the selected parameters the
rational fixed point is strictly smaller, so every finite ordinary
realizer has a strict complete-word descent. This does not exhibit an
ordinary integer cycle. It refutes a proposed small-gap bridge based
only on the listed coarse geometric and coefficient properties.

The note credits the classical circuit formulas. I reviewed the proof
and source-level arithmetic; I did not independently execute the long
numerical rows or audit the complete external Christoffel/high-cycle
literature in this review.

## 3. Independent reconstruction of the ternary-information theorem

The complete-carry coding is consistent, including its chronological
reversal. For fixed gap count, total binary clock and full carry, the
earlier carry decoder identifies the gap word. At a fixed ternary
residue and clock, bounding `C_m/3^m` therefore bounds the number of
possible words without a probabilistic independence assumption.

For an ergodic finite-mean gap law with mean at most `log_2(3)`, the
drift `d` is nonnegative. The prefix law `S_j=dj+o(j)` implies the
uniform maximum error over `j<=m` is `o(m)`. In the carry sum the term
`d(i-m)` is nonpositive, so the carry quotient is subexponential and
the typical clock range is linear. Both retained coordinates are
necessary for this fibre estimate.

Finite mean bounds the one-letter entropy by comparison with a
geometric law. The countable-alphabet Shannon--McMillan--Breiman
theorem can therefore be used with its finite-entropy hypothesis.
Intersecting its eventual word-mass bound with the two arithmetic
typical bounds gives the stated increasing restrictions `E_N`.
Each restricted residue ball has at most subexponentially many typical
prefixes, giving the stated uniform bound for its restricted mass.

The transfer from restricted mass to the full measure has the correct
direction. For `nu_N<=mu`, conditional expectation on the increasing
ternary residue partitions makes `nu_N(B_m)/mu(B_m)` converge to the
Radon--Nikodym density. These densities increase to one almost
everywhere, so almost every point has a positive density for some
restriction. Its full ball mass is then at most a fixed multiple of
the restricted mass. No exponential omitted-mass rate is used or
asserted.

The opposite local-dimension inequality follows because every entire
prefix cylinder maps into one ternary ball. Together the two bounds
give exact dimension `h/log(3)`. Fatou supplies the reverse entropy
liminf, while deterministic projection bounds residue entropy above
by finite block entropy. Hence the entropy rates agree and the
conditional decoding entropy is `o(m)`.

The final same-source application uses the direct odd-gap Theorem 3
of `FIXED_SOURCE_PRESSURE.md`, not a return-map identification with a
separately selected binary limit. I checked that theorem's moment,
entropy-continuity and growing-window arguments against its finite
blocking inequality (7).

The exact odd-map product and distinct positive states bound the
original average gap by `ell+o(1)`. Truncation gives the limiting
mean `1<=a<=ell`, allowing loss of first moment. A uniformly bounded
first moment nevertheless gives uniform entropy tails on every fixed
tuple alphabet: at tail mass `delta`, geometric comparison bounds
the entropy contribution by
`delta log(1/delta)+k delta log(eC/(k delta))`.
This tends uniformly to zero as the total-cost cutoff grows, so fixed
block entropies converge without assuming uniform integrability of
the gap itself.

For the ergodic improvement, the mean of `min(g,R)` over a growing
window is compared with the means over its fixed-length internal
windows. The discrepancy is at most `R(K-1)/m`. The exact endpoint
mixture controls the average deviation of those internal windows
by the fixed `K` empirical law. Taking the endpoint count to infinity
first and then `K` to infinity proves concentration by the stated
ergodicity. No growing-block convergence is assumed. Almost all
windows of length approximately `log_2(H+1)/(a-2epsilon)` then have
total gap larger than `log_2 H`. Complete ordinary-source congruence
makes each of these sampled words unique. Their entropy lower bound,
the finite blocking inequality and the fixed-block entropy passage
give `h(eta)>=a log(2)/beta`, including the stated further-subsequence
argument for a finite liminf height exponent.

For each fixed ternary precision, the exact past affine identity
identifies the endpoint residue from precisely that reversed gap
word. Its finite-depth empirical law pushes forward to the ternary
residue law; the first finitely many endpoints have vanishing weight.
This identifies the actual ternary limit with `Z_*eta` while retaining
the original source. Combining the exact-dimension theorem with the
direct entropy bound gives `dim mu>=a/(ell beta)`. The value `a=1`
is excluded at finite beta because it would force the constant gap
law and zero entropy. Critical mean `a=ell` is an explicit additional
case, not an automatic conclusion about the limiting first moment.

**Verdict and limits:** the written exact-dimension theorem and its
ergodic same-source consequence pass this reconstruction. The imported
classical ergodic theorems are used with the stated hypotheses; I did
not execute an infinite theorem or claim a Lean formalization. Exact
Shannon dimension does not imply a critical order-two collision bound,
and the note explicitly retains that gap, together with ergodicity,
height and omitted-mass-rate obligations.

## 4. Authored exact replay against an independent convergent-source oracle

Executed both commands from the repository root, each with exit code zero
and the same deterministic result dictionary:

```text
python -X utf8 -B research/closure-round5-20261123/replay_rational.py
python -O -X utf8 -B research/closure-round5-20261123/replay_rational.py
```

The checker uses explicit `require` failures rather than Python asserts.
Its oracle first follows the literal positive shortcut orbit to 1,
then reconstructs the complementary rational by exact backward
`Fraction` operations starting from 2. It does not call the recognizer
to decide the oracle value. The oracle has a 10,000-step cap; all 515
chosen sources reached 1, with largest observed stopping time 329.
This cap and source selection are finite test boundaries, not claims
about untested sources.

All three recognition strategies were compared with that exact oracle:

| Control | Observed checks |
|---|---:|
| Sources 1 through 512, plus 6171, 77031 and 837799; exact, unreduced and numerator-plus-256 candidates | 4,635 |
| Sources 1 through 40, odd denominators 1 through 15, numerators -16 through 16 | 31,680 |
| Sixty nontriadic pullbacks from proper prefixes, with residual denominators 5 and 7 | 180 |
| Two explicit repeated-small-numerator rejection cases | 6 |
| **Total candidate decisions** | **36,501** |

The decisions were 3,144 acceptances and 33,357 rejections. Event counts
were 3,965 original-one comparisons, 31,349 parity mismatches,
998 repeated-small-numerator events, and 189 specialized triadic
stopping-budget rejections. No general or mixed proved budget was
exceeded. These counts are controls on the tested implementation,
not evidence of a universal successful selector.

The pullback controls use terminal values `1/5`, `-1/7` and `11/5`.
Independent forward rational replay checks all 651 prescribed prefix
edges, even if recognition already rejects at an earlier repeated
small numerator. Across traced decisions, 2,115 exact paired edges and
360 divisions of the current denominator by three were checked.
The two explicit repeat cases preserve the repeated numerator but
change the original state, so all strategies reject them.

The checker also verifies 12 invalid-input cases, 56,432 large
single-step nonincrease samples, 23,576 compatible two-large-step
`7/8` contractions before original 1, the exact original-one
countercontrol for each odd denominator from 3 through 31, and the
central-binomial product identity and bound for denominators 1 through
64. All arithmetic uses integers or exact fractions.

No nontrivial ordinary repeated-pair acceptance was exercised: such a
positive ordinary cycle is not known. Its acceptance branch remains
covered by the mathematical and source-level argument, not by an
invented test witness. This authored execution is distinct from the
root's independent replay and final publication receipt.
