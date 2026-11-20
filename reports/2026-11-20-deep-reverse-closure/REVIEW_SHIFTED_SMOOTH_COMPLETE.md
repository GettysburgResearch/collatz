# Independent reconstruction of the complete shifted-smooth graph

Reviewer: `/root/deep_reverse_proof`.
The mathematical object reviewed is `SHIFTED_SMOOTH_COMPLETE.md`
at SHA-256
`34117cfda702fddc423976ccf649ad1414c37772c4a146c63eeec30d5ec85ccb`.
The adjacent author checker was identified at SHA-256
`682d02113a3181167f4f0b1ee3600ce42ae3d23c8eadaa5af1785b59b58c4410`,
but was not imported or used to derive the independent replay.

## Verdict

**VERIFIED as a source-qualified deduction from the displayed explicit
Lagarias inequality (L), at the claims CS1--CS3 only.** The finite
complement and exact algebra were independently reconstructed. This is
an AI mathematical review, not a proof-assistant execution or human
referee acceptance. No claim about convergence after leaving the class,
or about full Collatz, follows.

The quoted external estimate is retained as an external dependency.
The primary paper fetch in this reviewer session was unavailable; the
author and root report having read the exact primary lemma. This
review independently verifies the deduction conditional on the stated
bound and does not claim to have independently re-proved that bound.

## Reconstruction

For a boundary state `N_k=2*3^(k-1)-1`, one has
`3N_k+1=2(3^k-1)`. Thus, if `b=v2(3^k-1)`, the actual division
exponent in the odd map is `b+1`, while its endpoint is
`(3^k-1)/2^b`. This distinction is correctly retained.

If the endpoint is in the shifted class, its shift yields
`3^k+2^b-1=2^B*3^t`, with `B>=b+1`. For `k>=128`, the elementary
valuation formula gives `2^b<=4k<3^k`; consequently
`t=v3(2^b-1)<k`. Also `B<2k`. The positive logarithmic difference is
then

`0 < B log 2 -(k-t) log 3 < 4k/3^k`.

Using (L) with denominator `q=B`, not with denominator `k`, gives
the lower bound `log 3/(1200 B^13.3)`. Weakening it to
`1/[1200(2k)^14]` is legitimate and makes the remaining cutoff an
integer comparison. The exact comparison at 128 and the exact
inequality `129^15<3*128^15` prove the necessary opposite inequality
for every larger index. There is no appeal to a merely asymptotic
irrationality measure or an unspecified effective threshold.

The independently computed complete complement `1<=k<128` contains
only `(k,N_k,U(N_k))=(1,1,1),(2,5,1),(4,53,5)`. These include both
the cycle and the two terminating edges. All other indices are
excluded by either the finite complement or the uniform argument.

For `n+1=2^s*3^t`, the `s-1` valuation-one steps retain `s+t` and
reach `N_(s+t)`. The following step is precisely the boundary step.
Hence for index outside `{1,2,4}` the first exit is at odd clock
`s`, while the other three indices enumerate exactly
`{1,3,5,15,23,35,53}`. Thus CS2 follows for all initial exponents,
including unbounded ones, conditional on CS1.

For CS3, a defect edge with both endpoints in the class can start
only at `1`, `5`, or `53`. On a simple prefix the first cannot be
an outgoing edge, and the other two occur at most once. All remaining
defects touch an outside occurrence, each of which has at most two
incident edges. This proves `D_N<=2C_N+2`. On a never-convergent orbit
none of the three starts can occur, so `D_N<=2C_N` holds even for
periodic orbits and repeated occurrences.

For a general positive odd state, write `n+1=2^s q`, `q` odd.
There are exactly `s-1` valuation-one steps followed by one defect,
so the next defect finishes after exactly `s` odd transitions.
Combining `s<=log_2(n+1)` with the actual shifted-height envelope
gives `R_(i+1)<=log_2(3) R_i+h_0`. Solving this recurrence and using
the strict inequality `N<R_(D_N+1)` gives the displayed floor bound
also when the logarithm is an integer. The indexing and the strict
endpoint are correct.

## Independent finite execution

`check_shifted_smooth_review.py` was written without author imports.
It passed in normal and `-OO` Python modes with identical reports:

* 127 complete boundary indices;
* 8,128 source/index pairs checking exact exits or the seven-state basin;
* 24,688 simple-prefix incidence inequalities;
* 13,274 exact integer defect-clock inequalities.

The clock control uses the exact form
`2^R_(i+1)<=3^R_i*(n_0+1)`, avoiding floating logarithms.
The complement-table digest is
`dae95039b21160cc3dc852ce159583b1c9dcc950c5824e507bcdf783ef7a7b4b`.
The reviewer implementation SHA-256 is
`93a739f9b46daacb67324e7ce4a74e328206d924f35855074752676a45b123e5`.

The finite checks verify the complement and examples. The written
all-size argument, with its explicit external input, supplies the
unbounded quantifier. In particular no inference from a bounded
census to all large indices is used.
