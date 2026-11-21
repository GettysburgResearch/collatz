# Independent internal semantic reviews

These reviews were performed by separate collaborating agents against the
listed proof-source bytes. They are focused internal checks, not external
peer review. The root separately inspected the constructions, checked the
source pins, and ran the final combined Lean replay. All four final sources
passed that replay and its 53-theorem audit.

## ExponentCoverage

Reviewer: `band_route`. Verdict: **VERIFIED** at SHA-256
`339a866a08aaba64660c984a0b17834e89a98d3bfd6b2230b63e2a9995536718`.

The review reconstructed the phase budget, the bound `r <= 2^h` from a
supplied certificate, and the order of quantifiers: one arbitrarily large
chosen `q` serves every permitted certificate and every exponent in the
common interval. It checked the exponential coefficient budget
`C = 2^(H+1)`, the transfer from `C*y<n` and `n<=C^120` to
`y^120<n^119`, and the exact ten-q out of twelve-q exponent count. The return
index is a positive actual iterate of the marked return map; it need not be
the first return. The note correctly retains the selected-scale gap and
the short-certificate gap, including `r^21<n`. No universal convergence
claim follows from this family alone.

## MergerDispatch

Reviewer: `lean_architecture`. Verdict: **PASS** at final SHA-256
`cd34962cee9831194a95c19c13c948b14fbc3c7f4be232841cff924ff4a5720d`.

The review checked the actual forward clocks, factorization guards, parity
and positivity conditions, strict endpoint comparisons, and the basin
transfer used for a least counterexample. It confirmed that the proposed
odd-gap partner is already an earlier forward iterate. The restriction to
`{2,3,5,7}` concerns the original no-descent source. It cannot be reapplied
to all later states using the original source floor. The explanatory
finite-clock sieve and the distinction between a necessary cover and exact
eight-step survivors were also checked. One docstring incorrectly covered
an even-gap endpoint at `b=0`; it was corrected to the theorem's actual
guard before the final fresh replay. No proof statement changed.

## AnalyticCoupling

Reviewer: `band_route`. Verdict: **VERIFIED** at SHA-256
`5e0938034cf795ad65993d1ca384ebba4f967bb3267283b5166c08c4ea6f16a4`.

The review reconstructed the reciprocal finite-set induction, exact
height/valuation cocycle, Fourier telescoping bound, nearest-integer
character-gap bound, and nonnegative-kernel count. The distinctness
hypothesis covers only indices below `N`; the endpoint at `N` may repeat.
Small values are counted by injectivity into a finite value set, not by an
unproved escape-time bound. The reviewer independently replayed the exact
integer arithmetic at `n=2^601-1`, including all seven earlier failed
markedness tests and the larger-than-source first marked offset. The note
does not identify temporal orbit counts with spatial source counts or
phase equidistribution with residue independence.

## TemporalDensity

Reviewer: `lean_architecture`. Verdict: **PASS** at SHA-256
`3f78622671aaed9ee29f59c1edcadc4d5545487a873e31c6bf156b5e272bc2f6`.

The review checked the choices `K=floor(log2(N)/16384)` and `B=8192*K`,
the elementary power comparisons and the use of `pi<=4`, the zero-parameter
cases, and the final constant 196608. The finite-prefix, globally injective,
and unbounded-orbit statements retain their distinct hypotheses. The
estimate does not exclude repeated periodic orbits or create a quantitative
escape rate. The large constant is explicit and conservative rather than
a useful small-horizon cutoff.

## Separation of evidence

The successful development checks were followed by a fresh combined run
of all seven continuation/vendor modules and the audit. Seven unchanged
baseline modules were reused only after checking their earlier actual
successful receipt and source/artifact hashes. See [LEAN_RECEIPT.json](LEAN_RECEIPT.json)
for that complete evidence. Failed intermediate development probes and
resource-contention timeouts are not counted as successful proof checks.
