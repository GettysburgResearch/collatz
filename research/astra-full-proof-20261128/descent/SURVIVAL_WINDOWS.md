# Removing every landing width below half a future minimum

Let \(N\ge1\) be an integer, let \(R\ge1\) be an integer, and put
\(W_j(x)=2^{-C_j(x)}\) with \(C_j\) as in [the clock note](CLOCK_HEIGHT_MARK.md).
This note proves a uniform estimate on a portion of the true signed
native-versus-rational comparison. The estimate allows a full path
barrier, including all ordinary states after the entrance. The
[wide-interval argument](INTERMEDIATE_FLOOR_WIDTHS.md) controls the other
tail on a calibrated source scale. Intermediate widths remain open.

## An exact comparison at each denominator

Let \(P_r\) be the expectation of \(W_R\) for the positive source
\(u/3^r\) with \(1\le u\le N3^r\). The observable can also carry any
factor \(0\le H(x)\le1\) defined intrinsically from this rational source
and its trajectory, the same at every denominator. For the \(r\)-th
rung \(1\le r\le R\), generate \(r\) independent even-run lengths
\(e_i\ge0\) with \(\Pr(e_i=e)=2^{-e-1}\). A run followed by an odd
step acts by \(z\mapsto a_i z+1/2\) with \(a_i=3/2^{e_i+1}\).
Write \(A_r x+B_r\) for their composed map, \(B_0=0\), \(A_0=1\),
and \(Y=NA_r\). Then
\[
 P_{r-1}-P_r=\mathbb E_{\rm words}\sum_{B_r<y\le B_r+Y}
 (3\mathbf1_{y\equiv2\ (3)}-1)
 \frac{y-B_r}{Yy}\ W_{R-r}(y)H((y-B_r)/A_r),                    \tag{1}
\]
where \(y\) ranges over ordinary integers. The rational source with
this word and endpoint is uniquely \((y-B_r)/A_r\). Its numerator at
level \(r\) is an integer divisible by three exactly when
\(y\equiv2\bmod3\). The unmarked rung has factor \(1/Y\); here the
first \(r\) departures contribute exactly \(W_r=(y-B_r)/y\).
Multiplicativity gives (1). The countable sum over words is
absolutely convergent since its unmarked positive source mass is one.
The same proof works with \(W_\infty(y)=\lim_jW_j(y)\) in place of the
remaining finite product and the corresponding entire-path weight at
the source. The integral-weight estimate
\[
       0\le (y-B_r)/(Yy)\le 1/y                                  \tag{2}
\]
is uniform in the landing width. [Unmarked stopping-word bijection](../parity/MODERATE_DENOMINATOR_LADDER.md)

## Uniform sum over microscopic widths

For \(0<\varepsilon<1/8\), the total absolute contribution to (1)
from \(Y\le\varepsilon\), **summed over all** \(r\le R\), satisfies
\[
             O\bigl(\varepsilon(1+|\log\varepsilon|)^3\bigr).       \tag{3}
\]
The constant is independent of \(N,R,H\) and of the suffix marks.
Here and below \(\log\) denotes the natural logarithm. We give the
uniform occupation argument since a bound per rung costs a factor
that diverges with the source scale.

Fix \(0<\alpha<1\), and put
\(\rho=\mathbb E a_i^\alpha=3^\alpha/(2^{1+\alpha}-1)<1\).
Strict inequality follows from strict concavity in the expectation
and \(\mathbb E a_i=1\). For every translated interval \(I\) of length
one,
\[
 \sum_{p\ge0}\mathbb E[(1+B_p^\alpha)
                    \mathbf1_{\{\log A_p\in I\}}]\le C_\alpha.    \tag{4}
\]
For the unweighted term start at the first entry into \(I\). A return
at lag \(l\) then has probability at most
\(\Pr(\log A_l\ge-1)\le e^\alpha\rho^l\), independently of the first
entry location. Sum the lags. For the weighted term expand \(B_p\)
into one half the sum of the last \(j\) slope products,
\(0\le j<p\), and use subadditivity of the \(\alpha\)-power. Conditional
on the last \(j\) slopes, sum the translated unweighted strip bound
on the preceding \(p-j\) slopes. Integration of the last product costs
\(\rho^j\). Summation over \(j\) proves (4).

Let \(Z\) have the stationary law for the real post-odd random affine
map above. Its construction as the convergent backward positive
perpetuity gives \(\mathbb E Z^\alpha<\infty\) by the same geometric
series. It has the law of \((3U+1)/2\) for the stationary fair-clock
shortcut state \(U\). Indeed the stationary fair state is distributed
as \(2^{-e}Z\), where \(e\) is the independent number of even steps
since the preceding odd one. Weaver's real anti-concentration estimate
(Q7) consequently gives
\(\sup_x\Pr(|Z-x|\le h)\ll h\log(e/h)\) for small \(h>0\). In particular
\[
 \mathbb E\sum_{y\ge1}y^{-1}\mathbf1_{|Z-y|\le c h}
                \ll_c h(1+|\log h|)^2.                            \tag{5}
\]
For \(y\le1/h\), sum the uniform estimate against \(1/y\).
For larger \(y\) the weight is at most \(h\), and the intervals have
bounded overlap. [Weaver, equation (Q7), version 2](https://rstation.ai/problems/collatz/papers/19)

Partition the widths into strips \(h/e<Y\le h\) with \(h=e^{-j}\)
and \(j\ge0\). For large \(j\) set \(L=\lceil C_\alpha(j+1)\rceil\).
For \(r<L\) couple \(B_r\) to \(B_r+A_rZ'\) with independent stationary
\(Z'\). The latter has law \(Z\). Restrict \(Z'\le M\) for a constant
\(M\) having positive probability. Since \(A_r=Y/N\le h\),
\(B_r<y\le B_r+Y\) implies \(|B_r+A_rZ'-y|\le (1+M)h\) there.
Independence and (5) bound the sum over these \(r\) by
\(O(Lh(1+j)^2)\), including the weights (2).

For \(r\ge L\), split into \(p=r-L\) preceding runs and an independent
suffix of length \(L\) with slope \(A'\) and intercept \(B'\). Compare
\(B_r=B'+A'B_p\) with \(Z_L=B'+A'Z'\), which has law \(Z\).
Conditional on the suffix and \(Z'\), the width strip restricts
\(\log A_p\) to a single translated interval of length one. If
\(A'(B_p+Z')\le h\) then the sum over \(p\) is at most
\(C_\alpha\sum_y y^{-1}\mathbf1_{|Z_L-y|\le2h}\) by (4). Its
expectation is \(O(h(1+j)^2)\). Otherwise there is at most one integer
in the original interval and its reciprocal is at most one. Use
\(\mathbf1_{A'(B_p+Z')>h}\le h^{-\alpha}(A')^\alpha(B_p^\alpha+(Z')^\alpha)\)
and (4) on the same strip. This contributes at most
\(C_\alpha h^{-\alpha}\rho^L(1+\mathbb E (Z')^\alpha)\), which is
\(O(h^2)\) by the choice of \(C_\alpha\). Hence the entire strip costs
\(O(e^{-j}(1+j)^3)\). Summing over \(j\ge\lfloor|\log\varepsilon|\rfloor\)
proves (3), with the bounded range of small \(j\) absorbed by (4).

## Applying an entire future floor

For an ordinary integer \(a\ge2\) put
\[
 E_a=\{y\ge1: T^i y\ge a\text{ for every }i\ge0\}.
\]
Use in (1) the mark requiring every state of the original path to be
at least \(a\), including the rational prefix and the ordinary future.
An escaping-future mark may be added. Whenever the summand survives,
its ordinary endpoint \(y\) belongs to \(E_a\). No backward invariance
of \(E_a\) is assumed. For fixed \(0<\theta<0.0500\), the external
uniform first-landing estimate gives
\[
 \#(E_a\cap[1,X])\ll_\theta X a^{-\theta},\qquad
 \sum_{y\in E_a} y^{-1-\alpha}\ll_{\alpha,\theta}a^{-\alpha-\theta}.
                                                                    \tag{6}
\]
Use its barrier \(a-1\) and partial summation from \(a\).
[Wren, Theorem 4 and its formal-status statement](https://rstation.ai/problems/collatz/papers/55)

Fix \(1-\theta<\alpha<1\). For \(a^{-3}<Y\le a/2\) divide into
\(O(1+\log a)\) unit logarithmic strips, allowing shorter end strips.
For each \(y\in E_a\), its occurrence forces \(B_r\ge y-Y\ge y/2\).
The weighted strip bound (4), applied at \(\log Y=\log N+\log A_r\),
then bounds the summed contribution over \(r\) by \(O_\alpha(y^{-1-\alpha})\)
for that integer and strip. Using (3) on \(Y\le a^{-3}\) and (6) on
all larger strips yields the uniform total
\[
 \sum_{r\le R}\bigl[\text{absolute contribution in (1) with }Y\le a/2\bigr]
 \ll_{\alpha,\theta} a^{-3}(1+\log a)^3
             +(1+\log a)a^{-\alpha-\theta}=o(1/a).                 \tag{7}
\]
This inequality holds for the original signed comparison with true
physical future acceptance. It bounds each absolute summand before
any cancellation. The asymptotic in (7) concerns \(a\to\infty\).

Suppose an ordinary trajectory escapes. Its odd tail has arbitrarily
large future minima \(a\) prime to three. At every such \(a\), Weaver's
native first-landing theorem supplies \(\gg N/a\) ordinary sources
whose whole path has minimum \(a\) and escapes. Their survival is
bounded below by the simple-orbit reciprocal estimate. Thus
\(P_0\gg1/a\) for this marked source test, for sufficiently large
\(N=2^k\) at fixed \(a\). Taking \(R=\lfloor r_*+vg\rfloor\) as in the
clock note gives \(P_R\to0\), even if every rational source is included.
Taking \(k\) large at each supplied \(a\), (7) forces a positive net
contribution \(\gg 1/a\) to (1) from widths \(Y>a/2\). The mark can
also specify exact global minimum \(a\), since every marked ordinary
suffix still lies in \(E_a\). Proving a uniform \(o(1/a)\) *signed*
upper on these remaining widths would exclude escape. This argument
makes no claim that its fixed-exponent test excludes a nonstandard
cycle. [Native first-landing bound and its quantifiers](ENTRANCE_COMPARISON.md)

## Retaining nonstandard cycles at fixed exponent

Let \(D(x)\) be the first date at which a trajectory visits a previously
visited state. Set it to infinity when no such date exists. Define
\(\widetilde W_R(x)\) by multiplying the same positive survival factors
as \(W_R\) through date \(\min(D(x),\sigma_R(x))\). In the version
that tests all fates, use the finite mark \(\mathbf1_{\{\tau_1>\sigma_R\}}\)
that one has yet to be visited by the evaluation date. In the floor
version require that all states stay at least \(a\) in the entire future. This repeat rule and these marks refer to the
actual reduced rational source at every rung.

Every bad ordinary source contributes at least a fixed positive amount
to \(\widetilde W_R\), uniformly in \(R\). The segment through the first
repeat has distinct departure states. The published simple-path
reciprocal bound applies to all such states, since every bad state is
above the cited finite verification floor. This includes the transient
and the first lap of any additional cycle.
[Weaver, distinct-segment estimate (23) and its finite verification input](https://rstation.ai/problems/collatz/papers/175)

In the full rational law with denominator \(3^R\), write
\(s=\min(R,v_3(u))\). Before its first \(R-s\) odd departures the
reduced rational denominator decreases exactly once per odd departure.
The intervening even steps strictly decrease the positive state. Thus
no state repeats before integrality. Every omitted departure before
\(\sigma_R\) is ordinary and there are at most \(s\). Consequently
\[
                 W_R\le\widetilde W_R\le(4/3)^s W_R.                \tag{8}
\]
The full rational benchmark in fact has an elementary rate. Write
\(D_0=2-\lambda,\ R=r_*+h\) and assume \(\sqrt k\ll h=o(k)\). Then
\[
                  \mathbb E_{\rm rat}\widetilde W_R
                        \ll \exp(-c h^2/k).                         \tag{8a}
\]
Put \(d=\lfloor r_*+h/4\rfloor\) and \(t=\lfloor 2r_*+h\rfloor\).
The first \(t\) genuine parity bits are within total variation
\(2^t/(N3^R)=O(2^{-(\lambda-1)h})\) of fair independent bits: each word
has one initial numerator class modulo \(2^t\). On the fair bits let
\(S_d\) be the binary date of the \(d\)-th odd, a sum of \(d\)
independent mean-two geometric variables. With complementary
probability \(O(\exp(-c h^2/k))\), one has
\[
 S_d\le t,\qquad S_d-k-\lambda d\ge D_0h/8.
\]
Indeed \(t-2d=h/2+O(1)\) and \(2d-k-\lambda d=D_0h/4+O(1)\);
use the two geometric Chernoff tails. These events up to date \(t\)
transfer under the coupling. For every such true source \(0<x\le N\),
its \(d\)-th post-odd intercept \(B_d\ge1/2\), so
\[
 W_R\le W_d=\frac{3^d2^{-S_d}x}{3^d2^{-S_d}x+B_d}
                  \le 2N3^d2^{-S_d}\le2\cdot2^{-D_0h/8}.
\]
No independence of the source size and its parities has been used.
Under uniform numerators, \(\Pr(s\ge l)\le3^{-l}\) for \(1\le l\le R\).
Outside \(s>\eta h\), (8) costs at most \((4/3)^{\eta h}\). Fix
\(\eta>0\) small enough that \(\eta\log_2(4/3)<D_0/8\). The exponential
bound on the good event, and the bound \(\widetilde W_R\le1\) on its
complement, prove (8a). This proof uses only true initial numerator
precision and the first \(d\) completed odd departures. The full joint
concentration (3) in the clock note is a separate stronger conclusion
about the actual \(R\)-th endpoint. [Related genuine-numerator coupling for rational floors](../mass/ABSORBING_RATIONAL_FLOOR.md)

On the ordinary finite mark every bad source still contributes at
least a positive constant. Therefore vanishing of the *one*
native-minus-rational finite test in liminf would rule out both types
of positive exceptional orbit by fixed-target positive predecessor
density. The rational side of this comparison satisfies (8a).

A weaker-rate native comparison needs only an elementary finite path
bound. The at most \(R\) odd departure states up to the first repeat
on a bad orbit are distinct odd integers at least three. Ordered by
size, their \(j\)-th value is at least \(2j+1\) for \(j\ge1\). Hence
\[
 -\log\widetilde W_R\le\tfrac13\sum_{j=1}^R(2j+1)^{-1}
              \le\tfrac16\log(2R+1).
\]
The last inequality integrates the decreasing function \((2x+1)^{-1}\)
from zero to \(R\). Consequently a zero liminf of
\(R^{1/6}\mathbb E_{\rm ord}[\widetilde W_R\mathbf1_{\tau_1>\sigma_R}]\)
already implies universal convergence using positive predecessor density,
without the external uniform simple-path estimate. At \(h=vk^{3/5}\)
(8a) remains negligible under the same normalization. The stronger
unscaled native comparison above retains the external simple-path input.

The small-width estimate (7) extends to this repeat rule, uniformly
in \(N,R\) as \(a\to\infty\). For each candidate endpoint \(y\) and
word \(w\) at rung \(r\), put \(s=s(w,y)=\min(r,v_3(2^t y-C_w))\),
where \(A_r=3^r/2^t,\ B_r=C_w/2^t\). Set \(s=r\) if that formal
numerator is zero. Only positive numerators appear in (1). On a
source satisfying the whole floor, its repeat-stopped product
obeys \(\widetilde W_R\le W_r q^s\), \(q=1+1/(3a)\), because at
most \(s\) ordinary prefix tolls can be lost, each at input at least
\(a\). Regardless of any dependence of the stopping rule across the
rung, the absolute contribution is consequently at most
\(2q^s/y\) per valid marked endpoint. The exact signed sum uses
\(Y^{-1}\widetilde W_R((y-B_r)/A_r)H((y-B_r)/A_r)\) in place of the
product after the signed trit in (1).

For each fixed \(p>1\) with \(q^p<3/2\), uniformly over the integer
\(y\), source size and translated unit log-width strip \(I\),
\[
        \sum_{r\ge1}\mathbb E[q^{ps(w,y)}
                     \mathbf1_{\{\log Y\in I\}}]\le C_{q,p}.     \tag{9}
\]
The condition \(s\ge l\) for \(r\ge l\) is precisely the integrality
of the last \(l\) inverse odd-ending steps from \(y\). Once an inverse
has a proper ternary denominator each preceding inverse increases its
reduced denominator. The first inverse is integral only at
\(y\equiv2\bmod3\). To make its integer predecessor
\(2^e(2y-1)/3\) again congruent to two requires one prescribed parity
of \(e\), or is impossible. Each succeeding such test has conditional
probability at most \(2/3\) under its fresh geometric run. Hence the
last \(l\) runs satisfy the event with probability at most
\((2/3)^{l-1}\), uniformly in \(y\). Conditional on these runs, the
sum over earlier prefix lengths is bounded by the unweighted part of
(4). Expand the increasing geometric weight over \(l\le s\) and sum
\(\sum_lq^{pl}(2/3)^{l-1}\). This proves (9).

Put \(d=1-1/p\). In a strip \(h/e<Y\le h\) the proof of (3) at each
single integer gives
\(\sum_r\Pr(\text{strip},B_r<y\le B_r+Y)\ll (1+|\log h|)^2 h\)
uniformly in \(y\), by using (Q7) itself instead of (5). Hölder's
inequality with (9) raises this bound to the power \(d\) when the
summand carries \(q^s\). Sum against \(1/y\) up to \(1/h\). For
\(y>1/h\) use \(B_r\ge y/2\), (4), and the same Hölder bound, giving
\(O(y^{-\alpha d})\) before the reciprocal weight. The entire strip
costs \(O((1+|\log h|)^3h^{\alpha d})\) for small \(h\). Thus widths
\(Y\le a^{-C}\) cost \(o(1/a)\) for any fixed \(C>1/(\alpha d)\).
On each remaining strip up to \(a/2\), every marked \(y\in E_a\) has
\(B_r\ge y/2\), giving a total \(O(\sum_{E_a}y^{-1-\alpha d})\)
as before. Fix \(\alpha<1\) and \(p\) large enough that
\(\alpha d+\theta>1\), then take \(a\) sufficiently large that
\((1+1/(3a))^p\) is bounded strictly below \(3/2\). This proves the
uniform \(o(1/a)\) estimate over *all* widths \(Y\le a/2\), also with
the repeat-stopped all-fates mark. At any family of bad future minima
\(a\to\infty\), native landing and (8) again put a net \(\gg1/a\) on
the remaining widths. A single hypothetical cycle has one minimum;
using this asymptotic to rule it out would require a finite effective
bound or the fixed-source all-fates comparison.

At the calibrated source scale \(k=\lceil(\log(2a))^6\rceil\), even
the original finite \(W_R\) is at least \(\exp(-R/(3a))=1-o(1)\) on
a native path above \(a\), whether escaping or bounded. The rational
mass of the entire floor is \(o(1/a)\) at this same scale: take
\(2-\theta<\beta<2\) in the two-term ordinary endpoint bound, sum its
first term using (6) to get \(k^L O(a^{1-\beta-\theta})\), and sum
its second term to get \(O(u^{-1}e^{-c k^{1/5}})\) with
\(u\asymp k^{-2/5}\). This gives the finite-scale form of the same
wide-interval obstruction on either fate. [Endpoint tail](../mass/RATIONAL_ENTRANCE_KERNEL.md)

## What stationary intercept averaging leaves in the wide intervals

For orientation let \(S(x)=\lim_j W_j(x)\) on ordinary integers, and
let \(L(y)=\Pr(Z\ge y)\). These give an exact obstruction to closing the
wide range merely by replacing the running intercept by its stationary
law and integrating over the logarithm of the width. At fixed \(B<y\),
\[
 \int_{y-B}^\infty\frac{y-B}{Yy}\frac{dY}{Y}=\frac1y.
\]
After including the indicator \(B<y\), a stationary intercept gives
\((1-L(y))/y\). Replacing the multiplier \(1-L(y)\) by one has exactly
zero effect on the infinite signed trit sum with weight \(S(y)/y\):
\[
 \sum_{y\ge1}(3\mathbf1_{y\equiv2\ (3)}-1)\frac{S(y)L(y)}y=0.
                                                                    \tag{10}
\]
Indeed the series is absolutely convergent since \(L(y)\ll y^{-\alpha}\).
For \(x\) odd, \(S(2^e x)=S(x)\) and
\(S((3x+1)/2)=(1+1/(3x))S(x)\). Pairing the trit sum by the odd core
leaves \(S(x)/x\) times
\[
        2L((3x+1)/2)-\sum_{e\ge0}2^{-e}L(2^e x)=0,
\]
where the last equality is the exact stationary post-odd recursion.
This calculation does not pass to a limit in the full ladder. It
identifies why such stationary scalar smoothing alone preserves the
physical harmonic boundary. The remaining signed estimate for the
future-marked wide intervals needs the original path information.
[Physical harmonic boundary](ENTRANCE_COMPARISON.md)

[The exact-arithmetic checker](check_survival_ladder.py) independently
enumerates rational sources and affine words for the finite rung,
including a floor observed two odd departures beyond the evaluation
time. It also tests the first-repeat correction and equality of
ternary numerator depth with the count of integral inverse steps, and
the single endpoint cutoff for every full affine prefix floor.
The asymptotic and renewal bounds in this note are written arguments.
