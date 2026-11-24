# Independent review: actual CRT scalar approximation and carry freedom

23 November 2026. Reviewer lane: `pressure_construction8`.
Published parent: `6352608dd6c04735e1f8bd86fef4ebc97b1aeacb`.

**Verdict: VERIFIED for the written R9-A1--R9-A4, the stated coupled
coordinate cancellation, and the inspected literature boundaries.
No theorem correction was required; the source added an explicit
formal-series clarification during review.**

These are the exact new source versions reviewed under
`research/scalar-rigidity-round9-20261123/`:

| Path | Git blob |
| --- | --- |
| `ARITHMETIC_RIGIDITY.md` | `2c872eb9818be062e9444fde91555ba4e1e7230f` |
| `arithmetic_controls.py` | `1fbfd59b7fdc8de5d0b37d7d0514de590356431a` |
| `ArithmeticRigidity.lean` | `3776250063a2c3faae330574c400b160fdf992b6` |

The publication receipt supplies the containing commit. The real scalar
input remains the parent's reviewed R8-G1, blob
`540110f09cf68e3309fd83fea9c7ae497536ded4`. This review does not
upgrade finite realization into one ordinary infinite realization.

The source was first reconstructed at blob
`6e8dd3fd13c5d08084b430b53188af8dcb3ec135`. Its final version adds
only the explicit paragraph after (5) distinguishing the formal
symbolic identity from convergent evaluation for actual carries.
That paragraph was inspected and agrees with Section 1 below.

## 1. Exact carry normal form and its convergence domain

After ternary denominators have cleared, the fractional part has a
finite tripling orbit. Subtracting the unique representative p_i in
`(1/2,3/2]` from the actual scalar gives a nonnegative integer k_i.
The strict lower endpoint makes this valid even at fractional part
one half. Since `3p_i-p_(i+1)` is an integer strictly between zero
and four, its canonical charge b_i belongs to `{1,2,3}`.

The exact recurrence gives
`g_i=b_i+3k_i-k_(i+1)`. Its finite discounted telescoping identity is
`sum_(i<N)g_i/3^(i+1)=p_0+k_0-(p_N+k_N)/3^N`.
The converse's stated boundary condition is therefore sufficient for
the discounted value, without ordinary realization. For actual sources,
the scalar bound and `q_i<=2^i q_0` make k_i grow at most linearly.

The generating-series identity
`z(G-B)=(3z-1)K+k_0` is also correct coefficient by coefficient.
Its scope should be read precisely: in the unrestricted symbolic
converse, `k_N/3^N -> 0` does not itself ensure convergence of
`K(1/3)`, so that version uses the formal identity and the finite
telescoping limit. For actual linearly bounded carries, K does converge
at one third and literal evaluation is justified. No zero times an
undefined divergent series is needed for R9-A1.

## 2. The bounded automatic symbolic example

Both possible blocks, `(2,1)` and `(1,4)`, contribute `7/9` before
the common next-block discount of `1/9`. The infinite value is thus
`(7/9)/(1-1/9)=7/8` for every binary symbol sequence. Direct transport
gives intermediate charge `5/8+s_j` and returns to `7/8` at every
block endpoint. All raw gaps remain positive and at most four.

The indicator of positive powers of two is a binary automatic
sequence. Its infinitely many ones have unbounded gaps, so it cannot
be eventually periodic. The even subsequence of the proposed raw
gaps recovers that indicator; the raw gaps consequently are not
eventually periodic either. This verifies R9-A2's exact symbolic
counterexample without treating it as an actual infinite ordinary
trajectory.

## 3. Full ordinary cylinder, including every intermediate quotient

For a supplied positive-gap word of length N, the full affine equation
is `2^A_N v=3^N q+C_N`. Its final quotient is odd exactly when

`3^N q+C_N = 2^A_N mod 2^(A_N+1)`.

The coefficient `3^N` is invertible modulo this binary modulus, so
there is exactly one source residue. It is odd because C_N is odd
and A_N>=1. This proves the necessary complete terminal condition.

For sufficiency, split at any internal k<N. The suffix carry is odd,
and the complete final congruence reduces to

`3^(N-k)(3^k q+C_k) = 2^A_k mod 2^(A_k+1)`.

Multiplication by the inverse odd factor retains the same right side.
Every internal quotient is therefore an odd integer. All are positive
because the source and affine constants are positive. Consecutive
quotient equations recover every literal gap. The proof retains the
ordinary quotients rather than checking only total divisibility.

An arbitrary positive odd modulus M is coprime to the complete binary
modulus. CRT gives one combined residue below `M*2^(A_N+1)` and it
cannot be zero, since it is odd. Residues divisible by three and
M=1 are allowed; no unit-source restriction is silently introduced.

The endpoint estimate is independently recovered from

`C_N/2^A_N <= sum_(j<N) 3^(N-1-j)/2^(N-j) = (3/2)^N-1`.

Combining it with the strict source bound gives
`v<(2M+1)3^N`. The absence of the supplied gaps from this endpoint
bound is legitimate: their cost has already been paid in the source
modulus and source bit length. This verifies R9-A3.

## 4. Both actual approximation constants

For n binary blocks the symbolic tail is `7/8`, the total binary
clock is exactly `3n+2 sum s_j`, and the actual scalar error is
`9^(-n)(h(v)-7/8)`. The endpoint estimate with N=2n implies

`h(v)<(4n+bl(M)+4)/3`.

Together with `h(v)>1/2`, this gives the strict error bound
`(32n+8bl(M)+11)/(24*9^n)`. The corresponding source bit length is
at most `3n+2 sum s_j+bl(M)+1`, hence at most `5n+bl(M)+1`.

For a general supplied real target x>=1/2, the proposed normalized
ternary digits have discounted sum x after the initial integer part
is placed in the first gap. All gaps remain positive. Their first-N
clock is at most `3N+3floor(x-1/2)` and the symbolic tail lies in
`[1/2,3/2]`.

The actual endpoint gives the strict tail upper bound
`h(v)<(2N+bl(M)+4)/3`. That upper bound minus one half is at least
one, so it bounds both possible signs of the difference from the
symbolic tail. Multiplication by `3^(-N)` yields exactly

`(4N+2bl(M)+5)/(6*3^N)`.

This includes x=1/2, half-integer targets with zero ternary remainder,
and arbitrarily large integer parts. The closure assertion in every
odd congruence class follows. It does not assert that the same source
works for all N, or that every real or rational target is actually
attained.

## 5. Coupled algebraic coordinate and literature hypotheses

The algebraic radical coordinate is defined in one fixed field after
the residual denominator has been fixed. Its recurrence is exactly
`2^g y'=y^3`. Substituting this into the proposed coupled equation and
cancelling the nonzero y' gives the ordinary edge equation back.
Thus the displayed relation imposes no additional restriction on the
integer carries. No finite prime support has been proved for the
ordinary factors q_i.

I independently opened the primary
[Adamczewski--Bugeaud paper](https://annals.math.princeton.edu/wp-content/uploads/annals-v165-n2-p04.pdf)
and inspected Condition (*) and Theorems 5 and 5A. Theorem 5 includes
the base-field alternative for bounded integer coefficients. Theorem
5A requires the genuine expansion and a Pisot base. The source note's
distinction between those inputs and redundant raw gap coefficients
is correct; no actual-orbit automaticity premise has been supplied.

I also opened the primary
[Corvaja--Zannier paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2F6BB76838F610EB90B204764335ABCA/S0010437X02000258a.pdf/div-class-title-some-new-applications-of-the-subspace-theorem-div.pdf)
and inspected Theorems 1, 3, and 4. Theorem 4 retains a fixed tuple
dimension, explicit height bounds, and its distinguished-term
nonvanishing-subsum requirement. The stated coupled identity does not
establish these inputs. This is a hypothesis audit, not a new proof
of those external number-theoretic theorems or a rejection of every
possible later application.

The seven inspected Lean theorem statements concern finite block
charges, finite concatenation, tail differences, and algebraic
cancellation. They preserve the claimed finite scope. Compilation
and declaration-dependency auditing are recorded by the executing
parent; this review does not claim an independent compiler run.

## 6. Executed independent checks

The frozen `arithmetic_controls.py` returned PASS normally and under
`python -O`, each with 26,856 exact checks. Its domain comprised 490
target approximation cases, 130 binary carry cases, and 6,384 literal
ordinary odd transitions. These controls use unconditional scalar
enclosures and do not assume a terminating tail.

A separate literal-map replay exhausted every positive odd residue
below the complete binary modulus for all 39 words of length one
through three with gaps in `{1,2,3}`. It checked 2,954 representatives.
In every word's whole residue domain, exactly the displayed cylinder
residue had that actual gap word. This independently verifies both
directions and uniqueness on that finite domain.

An additional 75 boundary cases used targets
`1/2,3/2,5/2,201/2,1/2+1/59049`, lengths `1,4,12`, and congruences
`(M,a)=(1,0),(3,0),(5,4),(9,8),(101,100)`. Independent division by
two replay confirmed the literal gaps, prescribed residues, source
height, endpoint height, and the full rational enclosure bound in
each case. All checks passed.

**Remaining global step:** obtain a restriction on the actual carries
of one fixed positive ordinary source that survives these redundant
digit identities and changing-source approximation theorems. Neither
the density result nor the algebraic renaming establishes its scalar's
arithmetic type or its convergence.
