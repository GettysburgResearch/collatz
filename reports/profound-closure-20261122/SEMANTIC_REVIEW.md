# Coordinating semantic review

The review concerns the new packet, not a new proof audit of the entire
repository. Exact reviewed file hashes are in `root-review-pins.json`.
Independent agent reviews of the two-exponent exclusion and both analytic
notes are also included here. Compiler and exact-certificate execution
are separate evidence, with their own receipts.

## Independent power blocks

The written proof correctly excludes the case `D_i*x_i-C_i=0` before
charging a repeated block against a bit budget. Such a used block closes
the actual deterministic orbit, so arbitrary fixed-block padding cannot
create a new cycle. Integrality of a binary affine composition detects
the full parity word: after the first wrong branch, the numerator remains
odd over a growing power of two. Consequently the signed divisibility
condition is physical, not just a rational fixed-point equation.

The rotation argument uses a minimum partial multiplier over block
boundaries, and every rotated suffix multiplier is at most one. The
translation bound is independent of every exponent. Matveev's Corollary
2.3 was checked in the primary PDF with field degree one, two logarithms,
height bounds 1 and 2, and constant `2^33`. Combining its multiplier gap
with the finite bit budget gives the claimed cutoff. The full external
Matveev proof is not audited or formalized here; the Lean source-height
premise stays explicit. The generic finite enumeration is not represented
as an executed computation.

## The complete two-exponent exclusion

The necessary equation retains both the whole denominator and its positive
integer cofactor. The simple ratio argument eliminates the entire cone
`n>=m`. In the remaining cone, the coarse Matveev cutoff and Legendre
reduction retain the greatest-common-divisor scaling: a reduced convergent
is tested at the least positive scale making both original exponents
integral, and larger scales only worsen the decisive inequality.

The rational logarithm intervals include their positive series tails.
The exact verifier checks a consecutive continued-fraction cover through
a denominator beyond the required cutoff. It does not inspect an
arbitrarily selected list of good approximants. An independent researcher
reconstructed the written proof and ran its 32-convergent certificate and
eight corruption controls. The full logarithmic closure is not claimed
as a Lean theorem; the physical arithmetic interface and the entire
`n>=m` cone are formalized.

## Complement budgets and actual suffixes

The complement identity preserves the actual positive target and handles
both parities. The auxiliary negative-sign map is not assumed to converge.
Instead the pair consisting of the remaining even-step budget and the
valuation of `d-1` gives a terminating finite task, with the value one
handled explicitly. The lower bound `d>=2^p` prevents that early stop
before the required budget is earned; the explicit height recursion gives
the stated clock bound.

The supplied all-one prefix is a genuine guard. The final rank handoff
uses the same literal suffix from the original complete source witness,
strictly removes grade-two entries, and applies the interval premise once.
The arbitrary-gap transport equation is total arithmetic semantics, not
a proof that a paid prefix is always reached. The unit-complement
overshoot is a checked obstruction to that stronger reading. The Python
checker now uses explicit exceptions throughout, so optimization cannot
remove its proof checks; semantic corruption controls cover the block
chain, endpoints, clock, and payment claim.

## Finite inverse bounds and small ancestors

The floor enters as `omega<=q/b`, not as `omega<=1` at an arbitrary target.
The source-qualified full-clock counting estimate already sums the
inverse prefix and its clock tail. The new argument telescopes at one
fixed target, making at most `s/m` block comparisons, and accumulates the
quadratic error with the correct factor `m^(-A-1)`.

Only prefix endpoints through the stated horizon use the ancestor floor.
The suffix density is bounded by its unconditional finite-residue L1
norm. This validates the finite-floor localization. Substituting
`b=exp((log q)^gamma)` and choosing a fixed mixing exponent with
`gamma*(A+1)>2B+2` forces a genuinely smaller unit ancestor, at depth at
most the finite certificate depth (plus one for the obstacle comparison).
The smaller integer's forward orbit reaches the target; this is not a
claim that the target's own forward orbit descends to that integer.

The finite obstacle index and the stopped contact convention `tau<L` are
preserved. No infinite-horizon interchange or fixed-orbit random-law
substitution occurs. The analytic results depend on Tao's published
marginal theorem and the explicitly pinned written counting/comparison
results in PR180; the contact corollary additionally uses PR176. Those
repository analytic inputs have not been promoted to Lean theorems. The
four-theorem Lean module verifies the algebraic telescope and its finite
hypothesis version.

## Coverage

No argument supplies a universal bound on cycle-word power complexity,
successful-prefix coverage for the entire carry dispatcher, or a fixed
polylogarithmic depth for every necessary large canonical certificate.
These are mathematical hypotheses still to prove, not unverified finite
tests that a larger run would silently discharge. The new packet does not
claim a full Collatz proof or a new proof of GRH.
