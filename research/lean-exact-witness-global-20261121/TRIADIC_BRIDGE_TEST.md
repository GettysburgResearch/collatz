# Testing the signed-shadow bridge against the new triadic certificate

Date: 23 November 2026. **Written exact bridge test. Full target closure
remains OPEN.** No frozen checkpoint file is changed by this addendum.

## 1. New source and the precise construction target

The refreshed source is PR178 at
`4e204f54136c79cf8c9393b34e3330594f99ae0a`, specifically
`research/global-closure-20261123/duality/TRIADIC_RANK.md`, Sections 2,
4, and 5. Its overview and complete-denominator attempt were also read:

- `research/global-closure-20261123/README.md`;
- `research/global-closure-20261123/cycles/INTEGRAL_MAHLER_CLOSURE_ATTEMPT.md`.

The source gives an all-time convergence implication for a supplied
triadic complementary-parity candidate, and a written finite sufficient
certificate. The theorem and its Lean module are source-qualified here;
they were not rebuilt in this bridge test.

Precisely, the source defines

\[
 \operatorname{bl}(u)=\min\{L\ge1:u<2^L\}\quad(u\ge0),
\]

and, for an ordinary starting value `n>0`, signed numerator `a`, and
denominator exponent `r>=0`,

\[
 N=\operatorname{bl}(n),\quad
 B=\max(1,|a|,3^r),\quad L=\operatorname{bl}(B),\quad
 H=8N+(9r+8)L+2.                         \tag{TB1}
\]

If `e_i` are the actual original shortcut parity bits, put

\[
 b_i=\sum_{j<i}(1-e_j),\quad D_0=0,\quad
 D_{i+1}=3^{1-e_i}D_i+(1-e_i)2^i.
\]

The source's sufficient condition is

\[
 2^H\mid 3^{b_H}a+3^rD_H.               \tag{TB2}
\]

Its unproved universal step is to construct such a candidate at its
own height-dependent horizon. The present test checks one natural
construction suggested by our signed normalizer, without assuming the
universal step or the new closing theorem itself.

## 2. A genuine triadic dual of the signed normalizer

Use the six-step family TE14--TE16 in
[`TARGET_ENTRY_CONTINUATION.md`](TARGET_ENTRY_CONTINUATION.md). Write

\[
 b=341+486h\quad(h\ge0),\qquad
 x=\frac{2^{b+11}-7207}{729},\qquad
 y=\frac{x+1}{2}=\frac{2^{b+10}-3239}{729}.
                                                        \tag{TB3}
\]

The complete source word is `[2,2,2,3,3,b-1]`, and `x=257 mod 512`.
Its signed shadow is the fixed rational value

\[
 z=-3239/729,\qquad y-z=2^{b+10}/729.      \tag{TB4}
\]

The shadow reaches `-2` at shortcut clock 9 and `-1` at clock 10.
Unlike a generic signed endpoint, this endpoint allows an exact
triadic complementary candidate to be written down. The two rational
trajectories below have opposite parities at every displayed clock:

| Clock | Signed shadow | Its complementary candidate |
|---:|---:|---:|
| 0 | `-3239/729` | `-734/81` |
| 1 | `-1498/243` | `-367/81` |
| 2 | `-749/243` | `-170/27` |
| 3 | `-334/81` | `-85/27` |
| 4 | `-167/81` | `-38/9` |
| 5 | `-70/27` | `-19/9` |
| 6 | `-35/27` | `-8/3` |
| 7 | `-13/9` | `-4/3` |
| 8 | `-5/3` | `-2/3` |
| 9 | `-2` | `-1/3` |
| 10 | `-1` | `0` |

Every edge follows directly from the shortcut branches, with parity
defined using the odd denominator. Thereafter the pair `(-1,0)` is
fixed and remains complementary. Thus `-734/81` is a genuine all-time
triadic complementary candidate for the signed shadow. Equivalently,
starting with the pair `(-2,-1/3)` and pulling the right coordinate
backward through the first nine shadow branches gives that value.
No rationality conjecture is needed for this particular candidate.

## 3. Exact finite agreement with the positive target

For two odd-denominator rationals with the same parity, the difference
of their next shortcut values is either their previous difference
divided by two or three times that difference divided by two. Its
binary valuation therefore decreases by exactly one.

Equation (TB4) has exact binary valuation `b+10`. Hence `y` and `z`
have the same parity at clocks `0,...,b+9` and different parities at
clock `b+10`. Their respective evolutions need not be identified
after that first disagreement.

Consequently, the candidate `-734/81` has opposite parity to the
actual target `y` for exactly the first `b+10` clocks and fails at
clock `b+10`. The actual formulas in the source family also show this
directly: `T^10(y)=2^b-1`, its next `b` starting states are odd, and
`T^(b+10)(y)=3^b-1` is even, while the candidate has been zero since
clock 10.

There is an exact endpoint-congruence consequence. Force the candidate
through the complementary word of `y`, even after that disagreement.
At clock `b+10`, its current value is zero and the prescribed next
branch is odd, producing `1/2`. Every later forced branch increases
its reduced binary denominator exponent by one: its numerator is odd
and multiplication by three plus an even denominator cannot change
that. Therefore, for every `J>b+10`,

\[
 v_2\!\left(3^{b_J}(-734)+81D_J\right)=b+10.   \tag{TB5}
\]

This verifies the failure of longer endpoint congruences directly,
without an infinite-parity or convergence assumption.

## 4. The candidate does not meet its own height budget

For `b>=341`, the expression in (TB3) satisfies
`2^b<y<2^(b+1)`: the lower inequality follows from
`295*2^b>3239`, and the upper one from `1024<2*729`.
Thus the precise data for this candidate are

\[
 N=b+1,\quad a=-734,\quad r=4,\quad B=734,\quad L=10.
\]

Its horizon in (TB1) is therefore

\[
 H=8(b+1)+(9\cdot4+8)10+2=8b+450>b+10.    \tag{TB6}
\]

Equation (TB5) proves that (TB2) fails at this horizon for every member
of the complete-source family. This is a structural all-parameter
control, not a search through a finite list of candidates.

## 5. What this selects for the next attack

Our signed normalizer is a **same-parity** shadow of the positive target.
PR178's new terminating pair needs **opposite parity**. The shadow's
triadic denominator, and the finite padding theorem which funds its
normalization, do not by themselves change that orientation. Even
when the shadow has a completely explicit triadic complementary dual,
as above, its agreement can expire before the required height budget.

This test refutes only the displayed natural shadow-to-dual bridge.
It does not refute a different candidate, a different padded shadow,
or the universal source-dependent construction in PR178. The numerical
factor in its sufficient horizon is also not claimed optimal.

The new rank makes a precise next global target available: derive an
opposite-parity candidate whose binary agreement exceeds its own
numerator and ternary-denominator height cost. Funding the existing
same-parity normalizer is a finite step toward studying that question,
but does not supply the required bound.

The refreshed cycle file does not change the arithmetic cycle target:
its minimal triangular isogeny degree is exactly
`(2^A-3^p)/gcd(2^A-3^p,C)`. Excluding degree one is the same full
numerical cancellation still missing in the carry and fiber routes;
the torus normalization itself does not give a degree lower bound.
