# Independent review: stationary collision gap and real-series drift

Date: 2026-11-23.

Reviewer: boundary/minimum lane, independent of the collision argument's author.

**Verdict: the reviewed written deductions are valid with their stated
original-source and limit-order qualifications. No Collatz closure follows.**
One source-ledger path typo was reported and corrected before this review was
bound to its final hash. No mathematical repair was required.

## Frozen material

| File | SHA-256 |
|---|---|
| `research/whole-source-20261123/COLLISION_CORE.md` | `12d5f897b830c9d4deff794c3d42f99cf330244be4eafe6a4c716fd5db353e7c` |
| `research/whole-source-20261123/lean/StationaryCollisionGap.lean` | `c3e92dce283fac5b5a0b3162b3472990aa244185c41798ee87f905feb690e0b7` |
| `research/whole-source-20261123/lean/StationaryCollisionGapAudit.lean` | `4ff553bcf294050b3caea961227027d55b46a5349c68bb3537f9fe660c6015d4` |
| `research/whole-source-20261123/reports/collision-lean-check.json` | `388448988b92173dc564226cb3419086c784e5e961a5656292c36654072cdd8b` |

The report was written after reading the complete current mathematical note,
the complete new Lean module and audit, and the fresh build receipt/log.
This review did not rerun the historical corpus or claim an independent
second compiler execution. The source hashes above match the hashes recorded
for the Lean sources in the supplied fresh-build receipt.

## 1. Exact ordinary total variation

For a retained ordinary state `q_j`, its `r`-step image is `q_(r+j)`.
Distinctness makes it impossible for another sampled root to contribute
to this same endpoint. The kernel telescopes along its unique ordinary
forward itinerary, giving exactly

`zeta_(M,r)({q_j})=v_j/((M+1)v_(r+j))`.

These masses are at most `1/(M+1)`, since `v_j` is nondecreasing. Hence
the common mass with `pi_M` is exactly their sum, proving the stated TV
identity, not merely a one-sided domination bound. At fixed `M`, letting
`r` increase makes the TV approach the displayed `epsilon_M`, so the
supremum assertion is also correct. Cesaro convergence of `v_j/C` to one
proves uniformity over all finite choices `r=r_M`.

Pushforward contracts TV. Therefore the shared subsequential ternary weak
limits are justified at every fixed modulus without a rate assumption.
The note does not subtract this unquantified TV error from an exponentially
small finite-resolution collision lower bound.

## 2. Stationary lift, entropy deficit, and endpoint projection

The bounded expected total gap makes each fixed-length countable word
alphabet tight. A diagonal subsequence preserves all its probability mass.
Deleting either end of a window changes only a bounded number of sampled
endpoints, so the limiting block laws are consistent and stationary. Passing
bounded truncated costs first gives mean at most `log_2(3)`; it does not
assume uniform integrability of the gap sizes.

The reversal of the gap word in the coding formula is correct. Two steps,
for example, give the ternary residue `2^(-g_j)+3*2^(-g_j-g_(j-1))`.
The omitted early endpoints have vanishing mass at each fixed precision.
Thus the already selected ordinary time limit is the ternary factor of
the stationary gap law on the same subsequence.

The entropy cap follows from the finite cross entropy with the geometric
reference law. This also licenses all countable Shannon entropies used in
the proof. A finite-block deficit persists by stationarity and subadditivity.
If every finite block has maximum entropy, the displayed relative-entropy
formula forces the exact geometric product law, including its mean. Its
collision rate is `log(2*ell-1)`, strictly below its Shannon rate `Phi(ell)`.
This equality case is handled rather than omitted. Projecting word masses
to endpoint residues can only increase collisions. The process-dependent
strict upper Renyi-2 dimension bound consequently follows without asserting
existence of a Renyi rate.

The finite-window continuation also handles its countable-alphabet issue.
For fixed block length, a uniformly bounded first moment of total gap controls
entropy tails by comparison with `exp(-t*cost)`: first choose `t` small,
then the finite cutoff large. The block-interval mixture and its length
factor are retained. This supports the stated growing-resolution conclusion
in the deficit case; it does not supply that conclusion in the equality case.

## 3. No uniform strict gap and the type-class construction

The nonuniformity claim is correctly restricted to stationary positive-gap
processes, rather than claimed for actual Collatz factors. To make the rate
check explicit, fix a finite type class `W` of length `N` and concatenate
independent uniform blocks, with a uniform phase. This is stationary and has
the stated mean. A length-`m` word contains at least `m/N-2` complete blocks;
conditional on a phase, any one such word has mass at most
`|W|^(-m/N+2)`. The same upper bound holds after mixing phases and bounds
the collision sum from above. For a lower bound, force two samples to have
the same specified phase and all blocks intersecting the window equal.
This costs at most a constant number of additional blocks and a phase factor
independent of `m`. Both bounds give collision exponent `log|W|/N`.

Finite-support distributions of mean below `ell` can approximate the
mean-`ell` geometric entropy. Rational type approximations and finite-type
counting therefore make those exponents approach `Phi(ell)` from below.
Every fixed process still has a strict gap. The note correctly declines to
claim this sharpness survives the noninjective ternary coding.

## 4. Stationary finite real series: sign and integrability

Section 9 was checked independently. The positive real series identity is

`R=2^(-G_1)(1+3 R o S)`.

Taking logarithms gives exactly the sign in (24): the positive correction
appears on the same side as `G_1 log 2-log 3`. From `R>=2^(-G_1)`,

`log(1+1/(3R)) <= G_1 log 2 + log(4/3)`.

The correction is therefore integrable under the finite mean-gap premise.
The logarithmic coboundary is integrable by the identity, even if `log R`
itself is not. Clipping `log R` to `[-N,N]` preserves stationarity of its
marginal, gives zero expectation to the clipped difference, and bounds its
absolute value by that of the integrable unclipped difference. Dominated
convergence proves zero mean for the coboundary. The remaining positive
correction then forces strictly larger mean gap than `log_2(3)`. No
ergodicity, independence, or hidden logarithmic-moment hypothesis is needed.

The sufficient real-tightness condition is also correctly phrased. The
consistent real partial sums are increasing on the stationary sequence
space. Uniform tightness in their length makes their limit finite almost
surely. Fixed-precision ternary convergence does not establish this uniform
real tightness. The note keeps that missing link explicit and does not
identify it with the differently normalized real inverse-boundary law.

## 5. Lean scope and the remaining proof obligation

The four public Lean declarations prove the sequence blocking inequality,
the all-length deficit with its quotient floor, its eventual positive gap,
and the deficit-or-rigidity case split. All entropy, coding, source-extraction,
and rigidity inputs are theorem parameters in this generic module; none is
introduced as a global axiom. The source matches this claimed scope.

The reviewed fresh receipt records Lean 4.34.1, warnings as errors, successful
new module and audit builds, and only `propext`, `Classical.choice`, and
`Quot.sound` in the four audited declarations. The real-series theorem and
the actual probability identifications remain written arguments.

The first unproved closing alternative is still either a critical same-limit
collision upper bound with a subexponential loss, or uniform real tightness
for the very same stationary gap-series partial sums. The pressure density
comparison grows at fixed precision and cannot furnish the former by an
exchange of limits. The new strict lower bound sharpens these targets; it
does not prove either one.
