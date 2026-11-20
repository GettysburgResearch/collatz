# An adaptive exclusion for a complete unbounded-rank c=3 family

**PROPOSED theorem, with a complete proof relative to the independently
verified H2 initial-interval lemma.**
Every c=3 upper certificate whose remaining odd certificate has one run of
division exponent one followed by its terminal division is excluded from
being the globally least reverse-criterion failure. The rank and the
ordinary clock of this family are unbounded. The explicit certified sources
in the c=3 binary–ternary obstruction cylinders belong to this family.

This is a source-dependent certificate transformation. It does not close
all c=3 inputs, or the full deep reverse criterion.

## C3S1. The complete single-run family

Let `a,e` be positive integers for which

`z = 2^a*(2^e+1)/3^a - 1`

is an integer and satisfies `z=41 (mod81)`. Put

`h=(4z-2)/81`, `X=128h+1=(512z-175)/81`, `Y=64h+1`.

Then `h` is positive and `h=2 (mod4)`. The upper source has exact odd
certificate

`(2,2,2,3, 1 repeated a-1 times, e+1)`.

In particular its first-hit odd rank is `a+4`, and `X` converges. Every such
`X` is excluded from being the globally least failing upper antecedent.
Equivalently, its reverse implication follows from the validity of all
eligible reverse implications with upper antecedent strictly below `X`.

### Exact lower residual and ordinary clock

The condition on `z` implies `v3(z+1)=1`. Consequently

`v3(2^e+1)=a+1`.

It follows that `e` is odd and `v3(e)=a`: for odd `e`, elementary lifting
gives `v3(2^e+1)=1+v3(e)`. In particular `e>=3^a`. Write

`q=(2^e+1)/3^a`, so `z=2^a*q-1` and `q` is positive and odd.

The first `a-1` odd division exponents of `z` are one. The next odd value
has numerator `2*(3^a*q-1)=2^(e+1)`, so its final odd division exponent is
`e+1` and its next odd value is 1. This proves the asserted upper
certificate, after the four initial gaps `(2,2,2,3)` from `X` to `z`.

For the lower source, `T^7(Y)=2z+1`. Its first `a` shortcut steps are odd
steps with division exponent one, giving

`T^a(2z+1)=2^(e+1)+1`.

If `d>=4` is even and `w` is odd, then the two ordinary steps

`T^2(2^d*w+1)=2^(d-2)*(3w)+1`

are valid. Repeating them reduces `2^(e+1)+1` to
`4*3^((e-1)/2)+1`. Finally `T^3(4P+1)=T(P)` for odd `P`. Thus, for

`P=3^((e-1)/2)`,

the exact merging formula is

`T^(a+e+9)(Y)=T(P)`, while `T^(a+e+9)(X)=1`.

The lower source is therefore in the same ordinary component as `P`.
Neither its number of steps nor its terminal pure-power exponent is bounded
independently of the source.

### Uniform least-source comparison for a>=4

Set `B=176106`, the H2 initial-interval constant. Direct substitution gives

`81*3^a*(X-B*P)`
` = 2^(a+e+9)+2^(a+9)-687*3^a-81*B*3^(a+(e-1)/2)`.

It suffices to prove positivity of the slightly smaller expression

`S(a,e)=2^(a+e+9)-687*3^a-81*B*3^(a+(e-1)/2)`.

For each fixed `a`, its positivity at one odd `e` persists for all larger
odd `e`. Writing its three terms as `P0-E-Q`, respectively, gives

`S(a,e+2)=3*S(a,e)+P0+2*E>0`.

At `a=4`, `e=3^4=81`, the exact initial difference is

`S(4,81)=5759691404070374176388879671>0`.

The comparisons at `e=3^a` also persist as `a` increases. If `e=3^a`,
the positive term multiplies by `2^(2e+1)` when `(a,e)` is replaced by
`(a+1,3e)`. The exponential negative term multiplies by `3^(e+1)`, and the
remaining negative term multiplies by 3. Since

`2^(2e+1)>3^(e+1)` for `e>=2`,

positivity is preserved. This last inequality holds at `e=2` and persists
on increasing `e`, because its two sides multiply by 4 and 3.

Thus `S(a,e)>0` for every `a>=4` and every odd `e>=3^a`, including all
the family members under consideration. Hence `B*P<X`. If `X` were the
globally least failure, H2 would put `P` in the basin, and the exact
ordinary merging formula would put `Y` there as well, a contradiction.

### The complete cases a=1,2,3

The congruence `z=41 (mod81)` is equivalent to

`2^e = 42*3^a*2^(-a)-1 (mod 3^(a+4))`.

Because 2 generates the unit group of this modulus, its complete solutions
for these three values of `a` are:

| `a` | Complete positive exponent progression |
|---:|---|
| 1 | `e=21 (mod162)` |
| 2 | `e=315 (mod486)` |
| 3 | `e=837 (mod1458)` |

For `1<=a<=3`, positivity of `S(a,e)` at every odd `e>=81` follows from

`S(3,81)=5221070572784472125193957821>0`.

Indeed `S(a,81)/2^a` decreases with `a`, so its positivity for `a=3`
implies it for `a=1,2`; the preceding increment-by-two argument then applies.
The table therefore leaves just `a=1,e=21`, with residual `P=3^10`.
That integer reaches 1 by its complete ordinary certificate: 89 shortcut
clocks, 46 odd inputs, and peak 1135052. This disposes of the exception
without a least-source estimate and completes the family proof.

## C3S2. Explicit certified sources in every requested obstruction cylinder

Let the requested ordinary word budget be any integer `H>=0`, and set

`L=H+6`, `a=L-2`, `m=2L-1=2a+3`.

Choose a positive integer `e` satisfying

`2^e = -1 + 3^(a+1)*2^(-a-1) (mod 3^m)`.                (1)

The right side is a unit. Since 2 generates all units modulo `3^m`, there
is exactly one solution class modulo `2*3^(m-1)`, and it has arbitrarily
large positive representatives. Its right side is minus one modulo
`3^(a+1)` and is not minus one modulo `3^(a+2)`. Thus every such `e` is odd
with `v3(e)=a`, and `e>=3^a`.

Define `z`, `h`, `X`, and `Y` as in C3S1, and put `N=(4z+1)/3`. The
construction gives

`z=-1 (mod 2^(L-2))`, `z=1/2 (mod3^(L+1))`,

and consequently

`N=-1 (mod2^L)`, `N=1 (mod3^L)`.

For the ternary calculation, equation (1) says

`2^a*(2^e+1)=3^(a+1)/2 (mod3^(a+L+1))`;

division by `3^a` gives `z+1=3/2 (mod3^(L+1))`, as required. The binary
calculation uses the oddness of `(2^e+1)/3^a`. These are compatible ordinary
integer congruences, not rational source substitutions.

Since `L>=6`, they imply `z=41 (mod81)`, `h=(N-1)/27=2 (mod4)`,
`162h+4=8z`, and the exact fourth valuation `c=3`. All sources are positive:
`e>=3^a` implies `2^e>3^a`, so `z>1`, and then `z=41 (mod81)` gives
`h>=2`. The entire family therefore supplies actual certified convergent
upper sources in the desired obstruction cylinders.

At the same time, C3S1 shows that none of these upper sources can be the
globally least reverse failure. Their lower companions admit the unbounded
ordinary reduction to `P=3^((e-1)/2)<X/176106`. A bounded-word obstruction
and an adaptive successful reduction on these same sources are compatible.

### Compact examples

The following are least positive solutions of (1). The source is represented
exactly by the displayed formula for `z`; there is no need to expand its
very large binary power.

| `H` | `a` | `e` | Exponent period | Residual `P` |
|---:|---:|---:|---:|---|
| 0 | 4 | 116073 | 118098 | `3^58036` |
| 1 | 5 | 380781 | 1062882 | `3^190390` |
| 2 | 6 | 2431215 | 9565938 | `3^1215607` |
| 3 | 7 | 63433935 | 86093442 | `3^31716967` |
| 4 | 8 | 633234915 | 774840978 | `3^316617457` |

The checker constructs these exponents by lifting their discrete logarithm
one ternary digit at a time. It checks larger `H` using modular arithmetic
and the proven compressed certificate, without attempting to allocate an
integer with `e` binary digits. Literal ordinary iteration on smaller
single-run family members separately audits the merging clock identity.

## Why this does not yet give a general adaptive algorithm

For an arbitrary c=3 known source, put `a=v2(z+1)`, write `z=2^a*q-1`
with `q` odd, and let

`e=v2(3^a*q-1)`, `w=(3^a*q-1)/2^e`.

The same exact algebra removes the initial run from the actual certificate:
`w` is known to converge and `T^a(2z+1)=2^(e+1)*w+1`. The lower companion
then belongs to the ordinary component of

| Parity of `e` | Remaining residual |
|---|---|
| `e` odd | `3^((e-1)/2)*w` |
| `e` even | `2*3^(e/2)*w+1` |

For `e=1`, the residual is exactly `w`, so that entire first-block case
is solved. For `w=1`, this is exactly C3S1. In the remaining cases the
residual need not be known merely because `w` is known; multiplication by
the displayed power of 3 is one of the original unresolved mechanisms.
Nor is `w` guaranteed smaller than the same least failing `X`: a long run
of exponent-one steps can make it much larger. The CRT construction gives
additional convergent sources in a cylinder, not a replacement certificate
for an arbitrary pre-existing source in that cylinder.

Accordingly, the rule above is an exact partial certificate transformation.
A proof that it always reaches a known residual or the H2 initial interval,
while preserving the same least-source guard, is still missing.

## C3S3. A concrete remaining rank-six Mersenne family

The first-block transformation already encounters a Mersenne target when
the remaining known certificate has two odd inputs. Choose

`A=340+486j`, `j>=0`, and put

`z=(2^(A+3)-11)/9`, `e=A+1=341+486j`.

Then `z` has exact odd certificate `(3,A)`. Indeed
`U(z)=(2^A-1)/3` with first division exponent 3, followed by division
exponent `A` to 1. The c=3 eligibility condition is precisely

`z=41 (mod81)` if and only if `2^(A+3)=380 (mod729)`.

The order of 2 modulo 729 is 486. The displayed congruence has the unique
solution `A=340 (mod486)`, which is even; thus the stated progression is
the complete positive exponent family for this certificate prefix.

Its convergent upper and lower companion are

`X=(2048*2^e-7207)/729`, `Y=(X+1)/2`.

The upper certificate is `(2,2,2,3,3,A)`, of exact odd rank six.
For the lower, put `R=T^7(Y)=2z+1`. Its next two odd steps are

`U(R)=(2^(A+3)-5)/3`,

`U^2(R)=2^(A+1)-1=M_e`,

with exact division exponents 1 and 2. Consequently

`T^10(Y)=M_e`.

This identifies an unbounded concrete family still requiring a successful
adaptive construction. It supplies neither a failing ordinary source nor
an impossibility theorem for such a construction.

There is also a precise limit to using only the supplied upper stopping
clock. That clock is `A+12=e+11`, at which

`T^(e+11)(X)=1`, while `T^(e+11)(Y)=(3^e-1)/2>X`.

The lower equality follows from the first `e` odd steps of `M_e`, followed
by one halving. Its strict inequality holds for every `e>=5`: after clearing
denominators, it is
`729*3^e-4096*2^e+13685>0`, and already
`729*3^5>4096*2^5`; the ratio of those two positive terms increases with
`e`. All exponents in this family satisfy `e>=341`. Thus even a short
remaining odd certificate for the upper does not guarantee that its lower
companion has descended by the same ordinary stopping clock. Additional
source-dependent work after that clock remains possible.
