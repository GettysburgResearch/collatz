# Actual pressure maxima and arithmetic classes of the discounted scalar

23 November 2026. Parent: `3954c775ba74e1f40776ff38cb4282698d4a334a`.

**Status: PROPOSED elementary written deductions, exact finite controls,
and a source-qualified actual escape-pressure input. Collatz remains OPEN.**

The same ordinary pressure maximum from the earlier source construction
has a much sharper scalar restriction than a bound on its average gap.
Its actual discounted scalar lies strictly below the explicit series
`H*` in Section 6. Separately, a finite modular phase calculation
excludes whole classes of rational scalar denominators, including every
residual power of two except one phase at denominator eight. These
deductions use the actual scalar and actual positive ordinary states.
They do not construct rationality of that scalar, or the missing mass
comparison between moving ordinary predecessor basins.

## 1. Map, scalar, and frozen dependencies

For a positive odd ordinary integer q, write

\[
q_i=U^i(q),\qquad g_i=v_2(3q_i+1),\qquad
2^{g_i}q_{i+1}=3q_i+1,\qquad A_j=\sum_{i<j}g_i.
\]

Retain the actual real scalar from the companion `GERM_BRIDGE.md`,
R8-G1--R8-G2:

\[
h(q)=\sum_{i\ge0}\frac{g_i}{3^{i+1}},\qquad
\frac12<h(q)\le1+\frac{\log_2q}{3},\qquad
h(Uq)=3h(q)-g_0.                                      \tag{1}
\]

That note is frozen for this deduction at Git blob
`540110f09cf68e3309fd83fea9c7ae497536ded4`. Its real construction,
strict lower endpoint, and triadic criterion are independently
reconstructed in the companion review. In particular, strictness at
one half is essential below: equality would force every actual gap to
be one, making `2^j` divide the fixed positive integer `q+1` for every j.

The pressure input is PR182, full head
`3954c775ba74e1f40776ff38cb4282698d4a334a`, path
`research/closure-round2-20261123/SOURCE_CLOSURE.md`, selection theorem
(1)--(3) and forward coefficient inequality (6), Git blob
`9346c3b93fbd2e336a4e1c2e80d7b92ff5f34162`. That source in turn
pins the positive escaping-orbit correction product to PR177,
`6de3e304bb49a93a6c5ef0e5563137e75c7defb4`, path
`research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md`,
HE18--HE24e, blob `314fce3965adf36775fac9b5f2097c0181e830de`.
We retain that source qualification. No product is asserted on a
periodic component.

The phase theorems in Sections 2--5 require only (1), not the escaping
product. Section 6 explicitly assumes the actual escaping component
and its source-qualified product. No source or probability law is
changed between a premise and its conclusion.

## 2. A finite phase calculation that keeps the ordinary floor

Suppose the actual scalar is rational in lowest terms,

\[
h(q)=\frac{a}{3^r d},\qquad (d,3)=1.
\]

After r actual odd steps, its fractional part has denominator d and
numerator congruent to a modulo d. Its future fractional parts run
around the finite tripling orbit

\[
f_i=\left\{\frac{3^ia}{d}\right\},\qquad 0\le i<L.
\]

For d=1 this is the one-state orbit with fraction zero. Define m(f) to
be the unique representative of f modulo the integers in `(1/2,3/2]`:

\[
m(f)=
\begin{cases}
f+1,&0\le f\le1/2,\\
f,&1/2<f<1.
\end{cases}                                             \tag{2}
\]

Thus `m(0)=1` and `m(1/2)=3/2`. The actual scalar on this tail is
`h(q_(r+i))=m(f_i)+k_i` with an integer `k_i>=0`. Put

\[
S=\sum_{i=0}^{L-1}m(f_i),\qquad \mu=S/L.
\]

The canonical charges `b_i=3m(f_i)-m(f_(i+1))` are integers in
`{1,2,3}`; the open lower endpoint and closed upper endpoint in (2)
give `0<b_i<4`. Therefore

\[
2S=\sum_{i=0}^{L-1}b_i\in\mathbb Z_{>0}.                \tag{3}
\]

**R8-P1 (finite phase criterion).** Let Q be a positive odd integer
such that every positive odd ordinary integer at most Q reaches one.
If

\[
\boxed{(3+1/(Q+2))^L<2^{2S},}                           \tag{4}
\]

then any actual source with the displayed rational scalar reaches one.
Consequently, when d>1, that reduced scalar denominator and numerator
phase cannot occur at any positive ordinary source.

**Proof.** Define the actual positive potential

\[
W_i=q_i/2^{h(q_i)}.
\]

The complete ordinary equation and (1) give, without an omitted carry,

\[
\frac{W_{i+1}}{W_i}
=\frac{3+1/q_i}{4^{h(q_i)}},\qquad
W_i\ge\frac12q_i^{2/3}\ge\frac12.                       \tag{5}
\]

If the orbit never meets the verified finite set of odd integers at
most Q, every state is at least Q+2. On each complete phase block after
r, its scalar sum is at least S, so

\[
W_{r+(j+1)L}\le
\frac{(3+1/(Q+2))^L}{2^{2S}}W_{r+jL}.
\]

Condition (4) would force this subsequence to zero, contradicting (5).
The orbit therefore enters the finite convergent set and reaches one.
Conversely, an actual finite prefix followed by the standard tail at
one gives a scalar in `Z[1/3]`; hence a reduced residual denominator
d>1 is impossible. All computations in (4) are rational because of
(3).

With Q=1 this is the unconditional exact test

\[
10^L<3^L2^{2S}.                                         \tag{6}
\]

In particular every phase with mean at least `7/8` passes: the needed
strict comparison follows from `10^4=10000<10368=3^4*2^7`.
For a phase with mean greater than `log_4(3)`, a large enough Q always
satisfies (4), but its finite convergence premise must still be supplied.
The argument does not silently replace that premise by the conjecture.

### A small completely checked floor improves the test

The literal ordinary trajectories of all odd sources at most 31 are
replayed to one by `pressure_controls.py`. This is a finite convergence
certificate, not a statistical sample or an orbit-height assumption.
It makes Q=31 available in R8-P1. Since

\[
100^5=10\,000\,000\,000
<10\,018\,660\,608=2^8 33^5,
\]

**every phase with mean at least `4/5` passes this verified finite-floor
test**. Complete modular enumeration gives, in addition to the families
proved below:

| Complete residual denominator d | Number of tripling orbits | Smallest lift mean |
| --- | ---: | ---: |
| 11 | 2 | 4/5 |
| 26 | 4 | 5/6 |
| 35 | 2 | 5/6 |
| 46 | 2 | 19/22 |
| 52 | 4 | 5/6 |
| 85 | 4 | 13/16 |
| 109 | 4 | 23/27 |

Thus none of these complete residual denominators occurs in an actual
scalar. The script checks every reduced numerator class in each row,
and (4) directly, without floating point thresholds. This table does
not assert closure for denominators outside its listed finite set.

## 3. Complementary phases give infinite denominator families

**R8-P2 (minus-one family).** If `d>2` and `3^k=-1 mod d` for some
positive k, every phase at residual denominator d has mean one and
therefore is excluded by (6).

Indeed the orbit pairs each fraction f with `1-f`. Because the
numerator is reduced and d>2, neither endpoint zero nor one half
occurs. Formula (2) gives `m(f)+m(1-f)=2`, so each full orbit has mean
one. The case d=2 is even stronger: its sole lift is `3/2`, and it is
excluded as well.

For example all powers `5^j`, `7^j`, and `17^j`, j>=1, satisfy the
condition. Start with the explicit negative-one exponents 2, 3, and 8
modulo 5, 7, and 17. If p is odd and `x=-1 mod p^j`, the binomial
expansion gives `x^p=-1 mod p^(j+1)`. Thus the exponents
`2*5^(j-1)`, `3*7^(j-1)`, and `8*17^(j-1)` lift the three examples.
Their doubles also satisfy the condition; `4*7^j` does too because
its displayed exponent is odd. This does not make arbitrary products
of excluded denominators excluded: their negative-one exponents can
be incompatible.

## 4. Complete classification for residual powers of two

**R8-P3.** For a reduced residual denominator `d=2^k`, the finite phase
test excludes every case except the tripling orbit `{5,7}` modulo 8.
More explicitly:

| d | Reduced numerator orbit(s) | Lift mean | Conclusion |
| --- | --- | ---: | --- |
| 1 | 0 | 1 | The allowed triadic case; convergence follows |
| 2 | 1 | 3/2 | Excluded |
| 4 | 1,3 | 1 | Excluded |
| 8 | 1,3 | 5/4 | Excluded |
| 8 | 5,7 | 3/4 | Remains unresolved by this criterion |
| 2^k, k>=4 | Two orbits | 1−2/d and 1+2/d | Both excluded |

Here is an all-k proof of the final row. For t>=1,

\[
v_2(3^{2^t}-1)=t+2.                                    \tag{7}
\]

The initial case is `3^2-1=8`. Squaring increases the valuation by
one, since `3^(2^t)=1 mod 8` makes the new factor `3^(2^t)+1` have
valuation one. It follows that the order of 3 modulo `2^k`, k>=3,
is `2^(k-2)`: the displayed exponent works, and every smaller divisor
of that power of two fails by (7).

Powers of 3 are congruent to 1 or 3 modulo 8. There are exactly
`2^(k-2)` such odd residues modulo `2^k`, so they are the whole subgroup
generated by 3. The other coset consists of residues congruent to 5 or
7 modulo 8. Write `d=8t`, with t even when k>=4. In the first coset,
the residues are `8b+1,8b+3`, `0<=b<t`, whose sum is `8t^2-4t`.
The second coset has sum `8t^2+4t`. Dividing by the orbit size `2t`
and then by d gives fractional means `1/2−2/d` and `1/2+2/d`.

Translation by d/2 preserves each coset, because d/2 is divisible by
8, and pairs its lower-half and upper-half residues. Thus exactly
half of its lifts in (2) add one. The lift means are consequently
`1−2/d` and `1+2/d`, as claimed. At d>=16 both are at least 7/8.
Equivalently, with `L=d/4`, the worst block factor in (6) is

\[
2(5/6)^L\le2(5/6)^4=625/648<1.                          \tag{8}
\]

At d=8 translation by d/2 does not preserve these cosets, which is
why it must be handled separately. The unresolved pair has minimum
lifts `5/8,7/8` and canonical gaps 1,2. These are realized by the
negative ordinary cycle `-5 -> -7 -> -5`. That is not a positive
ordinary realization. Actual positive sources in this phase may also
have positive integer carries k_i in Section 2; the calculation has
not eliminated those carries.

Consequently, if the actual scalar belongs to `Z[1/6]`, it is either
triadic and the source converges, or its reduced residual denominator
is exactly 8 and, after the powers of three are cleared, its reduced
numerator is 5 or 7 modulo 8. The latter alternative is still OPEN.

## 5. A uniform family for high odd prime powers

**R8-P4.** Let p>=5 be a prime, let `t=ord_p(3)`, and put

\[
w=v_p(3^t-1).
\]

Every complete residual denominator `d=p^k` with `k>w` is excluded.

**Proof of the group assertion.** Write `3^t=1+p^w u`, with p not
dividing u. For an exponent coprime to p the geometric-sum identity
preserves valuation w. Raising to the p-th power increases the
valuation by exactly one: the leading binomial term has valuation
w+1 and every later term has strictly larger valuation, since p is
odd. Induction therefore gives

\[
v_p(3^{tv}-1)=w+v_p(v),\qquad
\operatorname{ord}_{p^k}(3)=t p^{\max(k-w,0)}.            \tag{9}
\]

The necessity of t dividing an exponent follows by reduction modulo p.
When `k>w`, put `D=p^w`, `M=p^(k-w)`. Each tripling orbit modulo
`DM` maps onto one orbit of length t modulo D. Its length is tM by
(9), so above each of its base residues it contains all M possible
lifts. This uses the entire finite residue fiber.

**Proof of the mean assertion.** For a base fraction `f=a/D`, the
fractions in that full fiber are `(b+f)/M`, `0<=b<M`. The number M is
odd, and f is not one half. If `f<1/2`, exactly `(M+1)/2` of these
fractions are below one half; if `f>1/2`, exactly `(M-1)/2` are.
Their fractional mean is `1/2+(f-1/2)/M`. Adding the appropriate
proportion of ones from (2) shows that the fiber's lift mean is

\[
1+\frac{m(f)-1}{M}.
\]

Consequently a complete orbit has mean

\[
\boxed{\mu_k=1+\frac{\mu_w-1}{p^{k-w}}
>1-\frac1{2p^{k-w}}\ge\frac9{10}>\frac78.}              \tag{10}
\]

R8-P1 with Q=1 finishes the exclusion. The strict inequality uses
`m(f)>1/2` at every base residue. This proves the whole family; it is
not extrapolated from a modular sample.

For example, `ord_11(3)=5` and `3^5-1=2*11^2`, so all residual
denominators `11^k`, k>=3, are excluded. The finite-floor table also
excludes 11 itself. The exponent k=2 is not settled by this family;
modulo 121 there is a phase of mean `3/5`. Also `ord_13(3)=3` and
`3^3-1=2*13`, so all residual denominators `13^k`, k>=2, are excluded.
These statements concern complete residual denominators. An arbitrary
denominator merely containing one of these prime powers is not
excluded by factoring it and applying this theorem to that factor.

## 6. A sharper bound at the same ordinary pressure maximum

Now assume an actual escaping component E of positive odd unit
integers. Retain the pinned source's positive correction product and
its ordinary weight

\[
\Lambda(n)=\prod_{j\ge0}\frac{3U^j(n)}{3U^j(n)+1},\qquad
r(n)=\Lambda(n)/n.
\]

The source proves a component-uniform constant `delta>0` with
`delta/n<=r(n)<=1/n`, the complete edge identity

\[
2^{g(n)}r(n)=3r(Un),                                    \tag{11}
\]

and attainment of a maximum at one positive ordinary `m in E`.
The same m is retained in every statement below.

### The discounted logarithmic identity

Put `ell_i=log_2 r(U^i q)` and `alpha=log_2 3`. Equation (11) gives
`g_i=alpha+ell_(i+1)-ell_i`. The actual growth inequality

\[
q_i+1\le(3/2)^i(q+1)
\]

and the uniform lower bound for r give `|ell_i|=O(i+1)`. Thus the
discounted logarithmic series and its summation-by-parts boundary term
are justified. Explicitly,

\[
h(q)=\frac\alpha2-\frac{\ell_0}{3}
       +\frac23\sum_{i\ge1}\frac{\ell_i}{3^i}.           \tag{12}
\]

At the actual maximum m this becomes

\[
\frac\alpha2-h(m)
=\frac23\sum_{i\ge1}\frac1{3^i}
       \log_2\frac{r(m)}{r(U^im)}\ge0.                  \tag{13}
\]

This is a same-source identity between actual pressure and the actual
scalar, with no entrance-law identification.

### Every prefix clock gives a sharper scalar ceiling

**R8-P5 (pressure-clock ceiling).** At that same m,

\[
\boxed{\frac12<h(m)<H_*:=
\frac23\sum_{j\ge1}\frac{\lfloor j\log_2 3\rfloor}{3^j}
<\frac{152}{243}.}                                     \tag{14}
\]

Numerically `H*=0.6253443474333885...`; the decimal is explanatory.
The exact series and the final rational bound are the statements used.

For every nonempty actual prefix the source already proves
`2^(A_j)<3^j`. Therefore `A_j<=floor(j alpha)`. The actual scalar
summation-by-parts identity from R8-G1 gives

\[
h(m)=\frac23\sum_{j\ge1}\frac{A_j}{3^j}\le H_*.
\]

Strictness follows within the same escape hypothesis. Escape makes
`U^j(m)` tend to infinity, and hence `r(U^j(m))<=1/U^j(m)` tends to
zero. Telescoping (11) shows

\[
A_j-j\alpha=\log_2\frac{r(U^jm)}{r(m)}\longrightarrow-\infty.
\]

It is therefore impossible that every A_j equal `floor(j alpha)`;
one positive-weight term in the preceding sum is strictly smaller.
This clock proof does not depend on the logarithmic series in (12).

For a fully rational upper bound after J terms, use `alpha<8/5`,
which follows from `3^5=243<256=2^8`, and the exact tail sum. Then

\[
H_*<\frac23\sum_{j=1}^{J}
\frac{\lfloor j\alpha\rfloor}{3^j}
+\frac{(2J+3)8}{30\,3^J}.                              \tag{15}
\]

The first six exact clocks are `1,3,4,6,7,9`. The corresponding bounds
from (15) are:

| J | Rational upper bound |
| ---: | ---: |
| 1 | 2/3 |
| 2 | 88/135 |
| 3 | 256/405 |
| 4 | 764/1215 |
| 5 | 2282/3645 |
| 6 | 152/243 |

The control script computes each floor as `(3^j).bit_length()-1`,
so there is no logarithmic rounding decision. At J=20 the bound is
`32706613742/52301766015`.

The small remaining interval above `5/8` does not prove exclusion:
`5/8 < H*` and the unresolved denominator-eight phase survives this
ceiling. For example the seventh floor clock is 11, whereas the
alternating 1,2 clock has cumulative value 10 there. A pressure maximum
whose scalar is triadic would already contradict the escape assumption;
the work here does not manufacture that arithmetic condition.

If the scalar at m has denominator exactly 8, with no power of three
left to clear, (14) leaves only `h(m)=5/8` among that denominator's
allowed values. This conclusion does not extend unchanged to
`h(m)=a/(3^r*8)` with r>0: clearing those powers of three moves to
`U^r(m)`, which has not been selected as the pressure maximum. The
maximum-root ceiling must not be reapplied there without a new argument.

## 7. Evidence and first unsupported step

`pressure_controls.py` uses exact integers and fractions throughout.
It replays the finite ordinary floor, exhausts the modular phases in
the finite table, checks powers of two through exponent 12, checks
explicit odd-prime-power fiber identities, and computes the rational
pressure-clock bounds. Its checks remain active under `python -O`.
Those runs corroborate the finite cases; the all-exponent claims are
the written arguments above. This note does not add a Lean theorem
claiming construction of the actual real scalar's arithmetic type.

The source-qualified pressure input is only asserted on actual escape.
The phase criterion itself applies to every positive ordinary source
whose actual scalar has the specified rational representation. Neither
one supplies a successful representation for every source. The
ordinary-selector companion investigates actual long low-scalar visits
and retains their full carry cost; it does not supply an all-time
positive realization of the denominator-eight phase.

**First unsupported step:** construct arithmetic rigidity of the
unchanged source's actual scalar, or exclude the surviving low phases
and irrational values using actual positive ordinary dynamics. A
construction of positive full predecessor mass for moving sibling
roots, with a paid comparison back to the original source, is also
still missing. Closeness of the pressure ceiling to 5/8, exclusions of
individual denominator classes, and finite rational approximations
do not close either gap.
