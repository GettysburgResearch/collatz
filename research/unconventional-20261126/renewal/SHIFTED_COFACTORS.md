# Prime-to-pool cofactors at every growth rate on one ordinary escape

**Status — proposed fixed-source theorem.** Let $x_t=T^t(x_0)$
be one injective positive ordinary shortcut orbit. Let $Z$ be any
fixed nonempty finite subset of $\mathbb Q\cap\mathbb Z_2$, with
common positive odd denominator $D$. Write $Y_t(z)=D(x_t-z)$.
For a finite set of primes $S$, put
$$
 R_S(Y)=|Y|\prod_{p\in S}p^{-v_p(Y)}\qquad(Y\ne0).
$$
All $Y_t(z)$ are positive eventually. Finitely many earlier zeros
may be omitted. Fix $0<\epsilon<1$, an integer $r\ge0$ and
$\beta=\log_3 2$. On each prefix of length $N$, choose **any**
single prime pool $S_N$ of cardinality at most $r$, even after
examining the whole trajectory prefix. Then
$$
 \liminf_{N\to\infty}{1\over N}\#\{0\le t<N:
 R_{S_N}(Y_t(z))\ge |Y_t(z)|^{1-\epsilon}
                        \ \hbox{for every }z\in Z\}\ \ge\ \beta.       \tag{C1}
$$
For a finite set consisting entirely of nonperiodic rational phases
under the genuine dyadic shortcut map, the limit is **one**. More
generally, if the proportion of odd native departures has a limit
$d$ and $\liminf_t \log(x_t+1)/t>0$, the limit is one provided
no periodic phase in $Z$ has odd-letter frequency $d$. These
additional hypotheses apply only to this last refinement.

In particular, with $S=\{2,3\}$, at least the fraction in (C1)
simultaneously satisfies, for every specified rational phase,
$$
 v_2(Y_t(z))\log 2+v_3(Y_t(z))\log 3\le\epsilon\log |Y_t(z)|.
$$
One can use any fixed number of additional primes without reducing
the guaranteed fraction. This does not imply that an orbit stays
outside a *fixed* neighborhood of a rational phase. Both local
precisions can grow unboundedly while using an arbitrarily small
fraction of the current real log-height.

## Large prime powers force exact periodic return intervals

Use binary logarithms in the proof. Write
$h_t=\log_2(x_t+1)\ge1$. We have $h_t\to\infty$ by injectivity,
$|h_{t+1}-h_t|\le1$, and $\log_2|Y_t(z)|/h_t\to1$ uniformly
over the fixed set $Z$. A native word $w$ of length $l$
and grade $b$ acts by $F_w(x)=(3^bx+C_w)/2^l$, with
$0\le C_w\le3^l-2^l$. An induction by appending one letter proves
this carry bound. If $p^k$ divides $Y_i(z)$ and $Y_j(z)$,
$j>i$, subtraction of the two endpoint expressions gives
$$
 p^k\mid E_w(z)=D(3^bz+C_w-2^lz),\qquad
 |E_w(z)|\le C_Z3^{j-i}.                                             \tag{C2}
$$
This is ordinary integral divisibility, including at two and three.
If $E_w(z)=0$, then the actual intervening word $w$ takes the
rational $z$ exactly to itself. Its bits are the **genuine** dyadic
itinerary of $z$: the inverse of either specified affine branch
maps any dyadic integer to a dyadic integer, and the parity of that
preimage is the indicated bit. Apply this statement backwards from
the dyadic integer $z$. Thus a nonempty zero-return word exists
only on a periodic rational phase, and follows its fixed periodic
word at the indicated phase.

Here is the local covering consequence. On an interval of length
$L\le K^2H+1$, suppose every departure has $h_t\ge H$, with
$K\ge2$ fixed and $H$ sufficiently large. Fix a pool of size
at most $r\ge1$. Call a time bad if it violates (C1)'s pointwise
test. Some pair $p,z$ then has
$v_p(Y_t(z))\log_2p\ge\epsilon H/(2r)$. For that pair select
all hits divisible by $p^{k_p}$, where
$k_p=\lceil\epsilon H/(2r\log_2 p)\rceil$.
Split its time-ordered hits at gaps at least
$cH$, where $c=\epsilon/(4r\log_2 3)$. By (C2), every shorter
gap is an exact periodic return once $H$ is large enough.
There are $O_{K,\epsilon,r}(1)$ resulting groups. All letters
from the first hit up to, but excluding, the last in each group
therefore follow a single fixed periodic itinerary. Cover the
one final departure in each group with the appropriate one-letter
template. This includes singleton groups.

The union of the intervals for the at most $r|Z|$ pairs covers
every bad time, using a bounded number of genuine periodic pieces
from a **fixed finite library**: the periods of the periodic $z$
and the two single-letter words. Split at all their endpoints;
where several marked pieces overlap, choose any one that covers
the resulting subinterval. The complementary intervals have total
length $B$ at most the number of good times. Zero-length charged
intervals permit switching between abutting templates. The total
number of intervals in this parse is bounded in terms of
$K,\epsilon,r,Z$, uniformly in the magnitudes of the primes
and in the native starting clock.

## Choosing windows with a small total starting charge

For $U$ uniform on $[0,1)$, divide the positive height axis into
the bands $[K^{j+U},K^{j+1+U})$, $j\in\mathbb Z$. Divide the
clock prefix at each change of band. For every $t>0$ the crossing
probability is at most
$$
   {|\log h_t-\log h_{t-1}|\over \log K}.
$$
Here the logarithms in the ratio may have any common base.
The natural-log inequality
$h_t|\ln h_t-\ln h_{t-1}|\le2|h_t-h_{t-1}|\le2$
uses $h_t,h_{t-1}\ge1$ and their distance at most one. Therefore
some choice of $U=U_N$ makes the sum of $h_t$ over all band
crossings at most $2N/\ln K$. This is only averaging the cut
locations of an already fixed deterministic ordinary prefix.

Within each uninterrupted band with base $H=K^{j+U}$, split after
every $\lceil K^2H\rceil$ departures until the band ends. An
additional starting charge is at most $KH$, hence at most
$1/K$ times the length of the preceding full piece. For the
resulting intervals $I=[a,a+L)$ we have
$$
 \sum_I h_a\le h_0+2N/\ln K+N/K,\qquad
       L\le K^2H+1,\qquad H\le h_t<KH\ (t\in I).                    \tag{C3}
$$
For fixed $K$ the number of pieces is $o(N)$: discard the at
most $M$ starts before time $M$, divide (C3) by
$\inf_{t\ge M}h_t$, then let $M\to\infty$. All pieces with
start clock bounded have bounded length, uniformly in $N$, by
$H\le h_a$.

Use the actual-ray [arithmetic template theorem A](../adelic/README.md),
section 3. In its length-only consequence, for any fixed library,
fixed interval budget and $\eta>0$, every sufficiently late and
sufficiently long such ordinary window has
$$
              h_a+(\log_2 3)B\ge(1-\eta)L.                          \tag{C4}
$$
The two thresholds are uniform over the allowed parses by the
sequential formulation of that theorem. Its external Diophantine
input is the classical $p$-adic Subspace Theorem. In the present
proof (C4) is invoked only after fixing $K,\epsilon,r,Z,\eta$.
Early pieces cost $O(1)$ clocks. Pieces shorter than a fixed
threshold cost $o(N)$ clocks by the count of starts. Also $H$
in all sufficiently late pieces exceeds any fixed bound since
$H>h_a/K$. Thus (C2)'s local parse applies to every remaining
piece. Sum (C4), bounding $B$ by the number of good times in each
piece and the starting charges by (C3), to get
$$
  \liminf_N{\#\{\text{good times}\}\over N}\ge
       \beta(1-\eta-2/\ln K-1/K).
$$
Take $\eta\downarrow0$, then $K\to\infty$, proving (C1).
An empty pool makes every nonzero time good directly.

## Which shifts can cause a positive density of exceptions?

For a nonperiodic $z$ all the groups in (C2) are singletons.
They account for $O_{K,\epsilon,r,Z}(1)$ departures per piece in
(C3), hence $o(N)$ in total. The same argument applies to an
arbitrary phase if one counts only the two ends of every nontrivial
group and the clocks within a fixed distance of an end. Therefore,
for *every* fixed integer $b$, outside $o(N)$ exceptions any
bad time attributed to $z$ lies centrally inside a genuine copy
of its periodic itinerary extending at least $b$ native steps
in each direction. Its current reference phase is $z$, since it
is itself a divisibility hit in that group. In particular its
dyadic coordinate agrees with $z$ to at least $b$ binary
digits. If the period contains a one, choosing $b$ large
enough also yields any specified ternary precision by forward
contraction along the past segment to that phase. The all-zero
cycle has no such ternary contraction. This bilateral statement
concerns the bad times themselves after deleting $o(N)$
departures from the whole prefix; it makes no assertion after
conditioning on a zero-density exceptional set.

For the frequency refinement assume the positive lower native
growth stated above. Discard times $t<\delta N$ for fixed
$\delta>0$. On the rest $h_t\ge c\delta N$ for large $N$.
Apply (C2)'s grouping directly to this whole interval, with
$H=c\delta N$ and a constant length ratio depending on
$c,\delta$. There are $O_{\delta,c,\epsilon,r,Z}(1)$ groups.
Writing $p_t$ for the cumulative number of odd departures,
the frequency limit gives $\max_{j\le N}|p_j-dj|=o(N)$.
A span of length $l$ on a periodic phase of frequency $d_z$
has $d_z l+O_Z(1)$ odd letters. Comparison at its endpoints
gives $|d_z-d|l=o(N)$. Under the stated nonresonance all these
groups have total length $o(N)$. Let $\delta\downarrow0$.

Weaver's [prime-power return theorem, Paper 138/v1, §§2,6](https://rstation.ai/problems/collatz/papers/138/v1)
treats unshifted odd states and gives density-one relative cofactor
bounds there. Its positive unshifted carry forbids the exact
periodic returns that arise for shifted native states. Its
prime-power method is a direct antecedent to (C2).
[Weaver, Paper 174/v1, Theorem 2](https://rstation.ai/problems/collatz/papers/174/v1)
bounds the share of rises in a fixed number of rise groups. Neither
result is needed as a black box for (C1); the periodic-piece
arithmetic used in (C4) is stronger than a count of defects.
The conclusion is consistent with a singular statistical limit at
a signed cycle, and places no upper bound on the integer factors
outside the selected pool. This remaining possibility prevents a
deduction of ordinary descent.
