# Independent review of the finite cycle-prime detector

23 November 2026. Reviewer lane: `ordinary_descent7`.

## Frozen sources and verdict

Parent PR182 head:
`e4367dd2c4406c1041e66d82dfba822908747fa3`.

| Source | Exact Git blob | Review boundary |
|---|---|---|
| `research/closure-round7-20261123/FINITE_JET_BOUND.md` | `f0fec15024a3d43bb02e07b2abdb61440fe79ded` | R7-DET-1 through R7-DET-4 and their written proofs |
| `research/closure-round7-20261123/detector_controls.py` | `31b3bef9fbbb6053c1741468957a996d9a003a3c` | Source inspection of exact arithmetic, literal realization, and finite-case scope |

**VERIFIED at the stated written-mathematics scope.** No correction was
identified in the four detector claims. The result retains a supplied
actual eventual cycle, a supplied cycle word or cycle-complexity bound,
and the arithmetic hypotheses on the actual coefficients. It does not
prove eventual periodicity, supply a universal period bound, construct
the ordinary-source germ, or prove Collatz.

This review does not claim a Lean formalization of the resultant,
algebraic-root valuation, or pole-evaluation arguments. It uses the
explicitly pinned earlier irreducibility, noncancellation, and ordinary
cycle-arithmetic dependencies at their separately stated evidence levels.
The verdict is bound to the source blobs above and does not extend
automatically to later edits.

## R7-DET-1: the finite resultant certificate

The full rational function is retained as
`C_w(z)/(3^p-z^A)`, and the monic reduced-clock polynomial is
`F(z)=z^u-3^v`, with `gcd(u,v)=1`. Given the pinned earlier
irreducibility and noncancellation result, the norm
`R=Res(F,C_w)` is an actual nonzero integer, even when the full
numerical cycle denominator has cancellations.

For a prime `ell` dividing `F(2)`, the roots `alpha_i` of `F` are
integral units at `ell`. Their translated roots `beta_i=alpha_i-2`
have nonnegative valuation, and the sum of those valuations is exactly
`v_ell(F(2))`. Therefore a root with valuation at least
`v_ell(F(2))/u` exists. Each numerator value `C_w(alpha_i)` is
integral; the valuation of any one of these values is at most the
valuation of their complete nonzero product `R`. Neither step drops
a denominator factor or assumes that the chosen extension is unramified.
The valuation is normalized by `v_ell(ell)=1`, so fractional extension
valuations cause no issue.

If the first `N` actual Taylor coefficients are integral at `ell`,
their finite truncation is an integral polynomial. Subtracting the
denominator times this polynomial from the numerator gives an integral
polynomial whose first `N` coefficients vanish. Its divisibility by
`t^N` is a polynomial statement. Evaluating it at the actual translated
root gives the stated lower bound on the numerator valuation. No
convergence of an infinite Taylor series at its pole is used.

The resulting inequality is `N*d_ell <= u*b_ell`. Taking
`N=floor(u*b_ell/d_ell)+1` gives a nonintegral coefficient among
indices `0,...,N-1`, so the claimed bound on the first forbidden order
has the correct indexing. The case `b_ell=0` correctly forces a
forbidden constant coefficient.

## R7-DET-2: the explicit number of coefficients

All complex roots of `F` have modulus `r=3^(p/A)`, and the positive
coefficient numerator obeys

`|Res(F,C_w)| <= C_w(r)^u`.

There are exactly `p` nonzero chronological carry terms. Each has
coefficient at most `3^(p-1)` and degree strictly less than `A`,
so `C_w(r) < p*3^(2p-1)`. The further bound
`p*3^(2p-1) < 5^(2p-1)` holds for every integer `p>=1`:
the initial ratio is `3/5`, and its next-to-current ratio is at most
`18/25`. Since every reduced-clock prime is at least five,
`b_ell < u*(2p-1)`. The first-forbidden-order bound then yields

`delta_ell < u^2*(2p-1)`.

Thus the displayed `M` is a count of coefficients, indexed through
`M-1`, as claimed. This argument provides a bound in supplied cycle
parameters and does not establish a universal bound on those parameters.

## R7-DET-3: exact prefix invariance

The full actual prefix identity has an additive polynomial with
denominators only powers of three, and multiplier
`(2+t)^h/3^s`. At a prime other than two and three, the additive
polynomial is integral and the multiplier is a unit of the integral
formal power-series ring. Its inverse is integral as well. Applying
this identity modulo `t^(K+1)` proves integrality equivalence for
every finite initial jet in both directions. The earliest forbidden
order is therefore exactly invariant, rather than only bounded after
transport.

For the direct norm check, the complete prefixed numerator evaluated
at a root of `F` is `alpha^h*C_w(alpha)`. The norm of `alpha` is a
signed power of three, so its contribution is a unit at the selected
prime. The resultant valuation is unchanged; no hidden preperiod
height is introduced. The assertion is properly scoped to rational
coefficients, with actual eventual periodicity supplying that property
in the application.

## R7-DET-4: the ordinary conditional conclusion

The ordinary conclusion assumes that the one positive ordinary source
is already eventually periodic. The pinned prior ordinary cycle-product
and exceptional-clock argument gives a genuine prime outside two and
three for every nonstandard positive ordinary cycle. The finite detector
and exact prefix invariance then contradict initial coefficients in
`Z[1/3]` over the stated range. This proves that such a supplied
eventually periodic ordinary source reaches one under the stated finite
arithmetic hypothesis. It makes no transfer from arbitrary rational
cycles to ordinary cycles and does not assert the hypothesis for every
ordinary source.

## Control implementation review

The source code was read independently; this review does not claim an
additional execution of `detector_controls.py`. The integrating agent
records actual execution receipts separately.

The configured cases are 15 selected positive rational cycle words,
including standard-cycle repetitions and three explicit delayed-prime
words. Each cycle is followed through its entire literal itinerary with
exact `Fraction` arithmetic, and the actual parity and exact return are
checked. There is no ordinary nonstandard-cycle assertion or all-word
census.

The resultant implementation takes the determinant of multiplication
by the full numerator in the integer quotient by `z^u-3^v`.
Reduction modulo this monic polynomial preserves the norm. The
fraction-free elimination checks exact division and handles pivot row
swaps; dimensions at most six are also compared with the independent
permutation expansion. Larger configured matrices do not receive that
second determinant check, which is an appropriate finite-coverage
distinction.

The Taylor routine translates the complete numerator and denominator
exactly and solves their coefficient convolution over `Fraction`.
The selected count exceeds every exact resultant-order bound in that
case. Each detected first forbidden coefficient is checked both against
its full-valuation bound and against the explicit period-only count.

Every preperiod is built by actual inverse branches, checked positive,
and then replayed forward for its literal parity and correct endpoint.
The direct full prefixed rational-function Taylor calculation is compared
against independent triangular coefficient transport. The first
forbidden order and the resultant prime valuation are both compared
before and after the prefix. Checks use explicit `require` calls,
so Python optimization does not disable them.

The implementation is an appropriate exact bounded control for the
general written theorem. It does not substitute computation for the
all-period valuation proof or the missing all-source construction.
