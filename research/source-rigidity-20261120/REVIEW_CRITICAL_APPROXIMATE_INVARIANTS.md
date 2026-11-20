# Independent review of the critical ordinary-operator annex

**Verdict: VERIFIED at CA1–CA3 and the named finite checker scope.**
No Collatz resolution or nonconstant exact invariant is established.
This review is an independent reconstruction of the frozen arguments and
code below. It does not extend to later bytes or to unquoted source claims.

## Frozen files

Author directory:
`/workspace/scratch/46eba7b29f50/agent-root-remains/`.

| File | Bytes | SHA-256 |
|---|---:|---|
| `CRITICAL_APPROXIMATE_INVARIANTS.md` | 8,588 | `5dfeaaaa239f2ecb62741e1eb6925a3b9e19731f923c785c72c6c06bf6f6fee3` |
| `check_critical_cutoffs.py` | 5,863 | `889d0ab549595b54bc95a2312e09fa4d558acf982432ac33c86c35adcb984f42` |
| `critical-cutoffs-report.json` | 10,503 | `16d790a0b827048c955753b262f9c1043de5a49a95881c4f6553ba291287ded5` |

The cutoff definition in the companion `ENDPOINT_CAPACITY.md`, frozen at
`0e4479eefbb7f27f2cabca82c2414a7c9fab4d6c2c2788235ad6e997a0d1e65d`,
is also reproduced explicitly in the reviewed annex. Nothing about a
nontrivial Collatz component is imported from that construction.

## CA1: harmonic mass and tripling defect

Every positive integer has the unique form `2^a m`, with `m` odd. Summing
the geometric fiber gives

\[
\sum_{n\ge1}\frac{b_M(n)}n
=2\sum_{\substack{m\le M\\m\text{ odd}}}\frac1m.
\]

The tripling defect is negative exactly when `M/3<o(n)<=M`, so the same
calculation gives the stated absolute defect. The odd harmonic sum is
`(1/2)log M+O(1)`. Subtracting the two endpoints of the annulus gives
the limit `log 3` for the full dyadic defect. The support of `b_M` is
infinite but its harmonic norm is finite for each fixed `M`; that fact is
correctly used before normalization.

**CA1: VERIFIED.**

## CA2: the actual Collatz branch and the valuation tail

Even inputs have no defect because `b_M(2n)=b_M(n)`. At an odd input the
odd part of `T(n)` is exactly `U(n)`, so the crossing description uses the
actual map with its additive term, not its homogeneous approximation.

The outward crossing interval lies inside `(M/3,M]`. For its odd harmonic
sum, retaining the first term and comparing the later terms to the
preceding length-two integral gives at most `1+(log 3)/2<2`.

For an odd endpoint `t` prime to three, the legal exponents in
`x=(2^a t-1)/3` form exactly one positive parity class. Consecutive
predecessors obey `x_next=4x+1`. Once the first crossing predecessor
`x_0>M` is selected, all remaining crossing sources are

\[
x_j=4^j x_0+\frac{4^j-1}{3}.
\]

The bound `sum_j 1/x_j <=4/(3x_0)<4/(3M)` therefore covers the entire
infinite fiber. There are at most `(M+1)/2` possible odd endpoints. The
resulting inward bound is at most `4/3`; with the outward bound this
indeed proves the conservative strict bound `Delta_T(M)<4` for every
positive `M`. Multiples of three have no odd predecessors and introduce
no missing fiber.

For exact valuation `a`, the condition
`3n+1 = 2^a mod 2^{a+1}` selects one odd residue modulo `2^{a+1}`.
The displayed crossing intervals are correct: `a=1` gives outward
crossings, and `a>=2` gives inward crossings. For fixed `a`, the density
of that one residue class and an elementary harmonic Riemann sum yield

\[
2^{-a-1}|\log(3/2^a)|.
\]

The limit is not summed without a tail estimate. If `a>=A>=3`, the first
admissible crossing predecessor satisfies both `x_0>M` and
`x_0>=2^{A-1}t/3`. Consequently its entire fiber is bounded by

\[
\frac43\min\left(\frac1M,\frac6{2^A t}\right).
\]

Summing over all integers `1<=t<=M` is a valid overcount. With
`K=ceil(6M/2^A)`, for fixed `A` and sufficiently large `M` one has
`K<=M`, and

\[
\frac43\left[\frac KM+
 \frac6{2^A}\sum_{t=K+1}^M\frac1t\right]
\le\frac8{2^A}\left(1+\log\frac{2^A}{6}\right)
 +\frac4{3M}.
\]

This proves a uniform **upper-limit** tail as `M` tends to infinity.
That is exactly what the fixed-valuation limiting argument requires;
no claim that the same displayed bound holds for every small `M` is
needed. The tail tends to zero as `A` tends to infinity.

Finally,

\[
\sum_{a\ge2}2^{-a-1}=\frac14,
\qquad
\sum_{a\ge2}a2^{-a-1}=\frac34,
\]

so the valuation sum is `(log 2)/2`. The constants, parity, additive
term, and order of limiting operations are all correct.

**CA2: VERIFIED.**

## CA3: bounded operators, joint residuals, and essential spectrum

The specified space is `X_p=l^p(N_{>0},1/n)`, for `p=1,2`.
The composition operators act on this full space. The note does not
incorrectly assert that `K_T` preserves the smaller exactly
doubling-invariant subspace.

For multiplication by `j`, changing variables gives operator norm to
the power `p` equal to `j`. For `T`, an endpoint `t` has the even
preimage `2t` and, exactly when `t=2 mod 3`, the positive odd preimage
`(2t-1)/3`. Relative to endpoint weight `1/t`, their total weight is

\[
\frac12+1_{t\equiv2\ (3)}\frac{3t}{2t-1}.
\]

Its maximum is `5/2`, achieved at `t=2`, whose preimages are `1` and
`4`. Thus `||K_T||_{X_p}^p=5/2`; no factor of two is missing.

The normalized vectors `v_{M,p}=b_M/L_M^{1/p}` have norm one.
Since the unnormalized functions are Boolean, the `p`-th power of an
absolute pointwise defect equals that defect. This gives both residual
identities exactly. Their rates are `1/log M` for the `p`-th powers and
`(log M)^{-1/p}` for the norms. Exact doubling invariance is retained.

On `X_2`, the sequence is weakly null: coordinates tend to zero,
the norms stay one, and finite-support vectors are dense. For every
fixed complex linear combination of the three operators with
coefficients summing to one, the residual tends to zero. A Fredholm
operator `L-I` would have a bounded left parametrix modulo compact
operators. Applying it to this weakly null sequence would force the
unit vectors to converge in norm to zero, a contradiction. This proves
the stated essential approximate spectral point on `X_2`.

The review does not infer weak nullity on `X_1`, nor an exact fixed
vector, nor failure of any specific-vector transport estimate.

**CA3: VERIFIED.**

## Checker review and actual replay

The checker explicitly enumerates every outward crossing and every odd
endpoint `t<=M` with an inward fiber. The starting exponent parity is
correct (`a=2` for `t=1 mod 3`, `a=1` for `t=2 mod 3`). It advances to
the first predecessor above the cutoff, then replays six exact legal
fiber terms.

If `x` is the first omitted term, its remaining infinite sum is enclosed by

\[
\frac4{3x+1}\le
\sum_{j\ge0}\frac1{4^j x+(4^j-1)/3}
\le\frac4{3x}.
\]

Indeed its exact denominator is
`[4^j(3x+1)-1]/3`, which lies between `4^j x` and
`4^j(x+1/3)`. Summing the resulting geometric bounds proves the
enclosure. Thus the report intervals cover **all original sources**
at each named `M`, not only the literal prefix.

The separate literal evaluation uses `T` directly through the stated
source cutoff and matches the corresponding finite fiber contribution.
The floor/ceiling conversion to scale `10^12` rounds outward. The
normalized residual enclosure divides by the exact positive norm.
The exact dyadic coefficient checks include their complete analytic
tails: `2^{-(A+1)}` for the mass and `(A+2)2^{-(A+1)}` for the first
moment. They therefore check the two coefficients used in the limiting
constant without numerical logarithms.

I ran the frozen checker independently in normal Python and obtained a
byte-identical copy of the pinned report. Its scope is 12 cutoffs
`1,2,3,4,7,16,31,64,127,256,511,1024`, 53,248 literal source checks,
1,026 valuation-domain checks, 684 full inward fibers, and 4,104 exact
fiber terms before analytic tails. The seven negative controls include
actual noninvariance, the norm-attaining preimage pair, even-input
invariance, valuation-one outward crossings, and exclusion of ternary
multiple endpoints. The gates use explicit `require`, not `assert`.
The author also reports identical normal and `-OO` output; this review's
own executed replay was the normal mode.

## Limits of the verdict

The written proof establishes a critical stability obstruction for the
specified ordinary operators on the specified harmonic spaces.
The executable controls do not establish the infinite limiting or
Fredholm arguments; those were reconstructed above. All cutoff
functions fail exact Collatz invariance, including at known convergent
ordinary inputs. This result cannot be promoted to an invariant
separating component, a divergent orbit, or a nontrivial cycle.

The remaining positive task is still an argument that uses exact
ordinary invariance or another source-persistent arithmetic condition.
Approximate invariance in these harmonic norms is insufficient.
