# The natural distribution of the least ordinary predecessor relative to its target

**FS-010–012: PROPOSED, pending independent review.** These results concern
ordinary positive integer paths of unrestricted length. They use no external
positive-density theorem and no Collatz convergence assumption. The conclusion
is a population law for the *targets*. It leaves open the behavior of any
individual nontrivial merger component.

Use the shortcut $T(n)=n/2$ for even $n$ and $(3n+1)/2$ for odd $n$.
For odd $t$, let $m(t)$ be the least positive starting integer whose orbit
reaches $t$, allowing the empty path. This minimum exists and is odd:
an even predecessor can first be replaced by its smaller odd core,
since the target is odd. Write $\mu_3$ for Haar probability on the
ternary integers. Densities below are relative natural densities among
odd positive targets unless stated otherwise.

## FS-010. All-depth density equals an explicit ternary first-crossing probability

For $0<\theta\le1$, let $H_\theta\subset\mathbb Z_3$ consist of the endpoints
for which some nonempty inverse valuation word $a_1,\ldots,a_q\ge1$ is
legally integral in $\mathbb Z_3$ and satisfies
$2^A/3^q\le\theta$, where $A=\sum a_i$. The inverse recurrence starts
at $y_0=t$ and reads $y_i=(2^{a_i}y_{i-1}-1)/3$.
Then the density exists and

$$
 d_{\rm odd}\{t:m(t)<\theta t\}=\mu_3(H_\theta)\le\theta^2.
$$

The comparison on the ordinary side is strict. Equality of a *nonempty*
word coefficient with $\theta$ qualifies on the symbolic side, because
the ordinary inverse affine correction is strictly negative. For example,
among odd targets the limiting fraction with any ancestor below one tenth
of the target is at most one percent. The full law is the same within each
fixed odd residue class modulo any power of two. An additional fixed
ternary congruence instead conditions $\mu_3$ on that congruence.

This improves on a finite-depth CRT calculation: the proof below accounts
for every real positive predecessor, however late its first encounter.
The forward no-descent parity bound is credited to the
[fixed-height packet](../external/mazur-2026/fixed-height-forward-power-saving.md)
at base `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; the elementary
fixed-clock version needed here is reproduced.

### 1. Rare long no-descent starts

Fix $0<u<v$. For integer $L\ge1$ define
$p_L=2^{-L}\sum_{q\ge\lceil L\log_3 2\rceil}\binom Lq$.
The number of $n\in[uX,vX]$ with $T^i(n)\ge n$ for all $i\le L$,
divided by $X$, has limsup at most $v p_L$ as $X\to\infty$.
Indeed $L$ parity bits determine one residue modulo $2^L$. If $q$ bits
are odd then $T^L(n)/n\le (3+1/(uX))^q/2^L$ on this population.
For fixed $L$ and large $X$, $q\ge\lceil L\log_3 2\rceil$ since
$L\log_3 2$ is nonintegral. Count each prefix at most $vX/2^L+1$ times.
The standard binomial tail bound gives
$p_L\le (L+1)2^{-(1-h_2(\log_3 2))L}$, exponentially small.

There are arbitrarily large integer clocks $L$ for which, whenever
$1\le k\le L$ and $0\le q\le k$,

$$
 |k\log2-q\log3|\ge \Delta_L:=\frac{\log2}{2(L+1)}.
$$

Take $L=Q_j-1$, with $Q_j$ a continued-fraction convergent denominator
for the irrational $\log_2 3$. For $1\le q<Q_j$ the best-approximation
property bounds $\|q\log_2 3\|$ below by
$\|Q_{j-1}\log_2 3\|>1/(Q_{j-1}+Q_j)$; the case $q=0$ is immediate.
We take $X\to\infty$ for each such fixed $L$ before sending $L\to\infty$.

### 2. Counting late first-smaller crossings as targets

For fixed $0<u<v$, call $y\in[uX,vX]$ a late endpoint if for some
$x<y$ and $\ell>L$ there is a path

$$
 T^\ell(x)=y,\qquad T^i(x)>y\quad(1\le i<\ell).
$$

Along the selected clocks $L$, the number of late endpoints divided by
$X$ has limsup $O_{u,v}((L+1)p_L)$. The count is over endpoints, even
when multiple smaller sources reach one endpoint.

To prove this, the first step must be odd and
$(2y-1)/3\le x<y$. Thus $x\in[uX/2,vX]$ for large $X$ and it has no
descent through $L$. For each such $x$, consider the successive strict
record minima of the forward orbit starting at $r_0=T(x)$. If another
record follows $r$ it is the unique first subsequent value $r'<r$.
The endpoint $y$ is one of these records after $r_0$, and all records
from $r_0$ to $y$ lie in $[uX,2vX]$.

Separate the final record transition $r\to r'$ by its own time $k$.
If $k\le L$ and both records are in that interval, the exact logarithmic
identity is

$$
 \log(r'/r)=q\log3-k\log2+
   \sum_{\substack{i<k\\ T^i(r)\text{ odd}}}
       \log(1+1/(3T^i(r))).
$$

All states before $r'$ are at least $r$, so the correction is between
zero and $L/(3uX)$. For fixed $L$ and sufficiently large $X$, the
strict drop has logarithmic size at least $\Delta_L/2$. The total
logarithmic drop of all such transitions before leaving $[uX,2vX]$ is
at most $\log(2v/u)$. Hence each possible $x$ accounts for only
$O_{u,v}(L+1)$ record destinations with a short final transition.
There are at most $O_{u,v}(Xp_L)+o_L(X)$ possible $x$ by section 1.

For a final transition with $k>L$, the preceding record $r\in[uX,2vX]$
itself has no descent through $L$. Count it globally by section 1:
each $r$ supplies only its unique next strict record, however many starting
$x$ may run through that segment. This proves the asserted bound.
Charging every late endpoint merely to its initial $x$ without this
short/long split would not give the required multiplicity bound.

### 3. Chaining first-smaller crossings to an arbitrary fixed ratio

Suppose $X\le t\le2X$ admits $m<\theta t$ reaching it. Take the path
from $m$ up to its first hit of $t$. It has no repeated states, since
a repeated state before that hit would already have closed a cycle.
Read the path backwards from $s_0=t$, recording successive new strict
minima $s_1,s_2,\ldots$ until the first $s_j<\theta t$. Each forward
arc $s_{i+1}\to s_i$ is a first-smaller crossing in section 2's sense,
with all interior values strictly above $s_i$. Before the last crossing,
$s_i\ge\theta t$ and its smaller source is at least $(2s_i-1)/3$.
All record endpoints up to and including $s_j$ are therefore in
$[\theta X/2,2X]$ for large $X$.

A short arc (at most $L$ shortcut steps) has
$\log(s_i/s_{i+1})\ge\Delta_L$ for sufficiently large $X$. Indeed the
displayed logarithmic identity applies, now with positive net change.
The additive correction is at most $2L/(3\theta X)$, which cannot reverse
a negative coefficient log with magnitude at least $\Delta_L$.
Thus the number of short arcs before the first long arc or the stopping
record is at most $1+\log(4/\theta)/\Delta_L$. Their total clock is at most

$$
 M=L\left\lceil1+\log(4/\theta)/\Delta_L\right\rceil=O_\theta(L^2).
$$

If all arcs are short, $s_j<\theta t$ reaches $t$ within $M$ steps. If a
first long arc occurs in backward order, its upper endpoint $s_i$ is a
late endpoint in $[\theta X,2X]$. The original $t$ is one of at most
$M+1$ forward iterates of $s_i$. By section 2, the limsup fraction
of targets in this latter case is $O_\theta((L+1)^3p_L)$, which tends
to zero. This controls unrestricted paths via the ordinary forward
determinism at the record endpoints.

### 4. Finite words, limits and the quadratic bound

A word of $q$ inverse odd steps is integral on exactly one residue class
modulo $3^q$. Prescribing each next inverse step fixes one new ternary
digit, since the preceding affine numerator has unit slope. On an
odd positive representative every integral inverse is positive and odd.
The resulting source has the form $D_w t-C_w$, with
$D_w=2^A/3^q$ and $C_w>0$ for every nonempty word.
Any word with $D_w\le\theta$ therefore supplies a strictly smaller
ordinary witness below $\theta t$.

Conversely any first-smaller record source is odd, since an even first
step cannot rise above it. Thus the bounded-clock witness $s_j\to t$
of section 3 between odd endpoints is an odd word of total valuation
$A\le M$. There are finitely many such words. For all sufficiently
large $t$, no word in this finite set with $D_w>\theta$ has
$D_wt-C_w<\theta t$. The ordinary hit event in the shell is therefore
sandwiched between the finite cylinder union with $A\le M$ and that
same union plus a set of limsup fraction $O_\theta((L+1)^3p_L)$.

For each fixed $M$ the finite union has relative density among odds in
$[X,2X]$ equal in the limit to its ternary Haar probability, by CRT.
The same holds after any additional fixed dyadic and ternary conditioning;
dividing the sparse error by a fixed positive class proportion still
gives a vanishing limit as $L\to\infty$. The unions increase to
$H_\theta$ as $M\to\infty$. The shell limit gives the same cumulative
natural density by dyadically partitioning $[1,X]$ and discarding a
fixed initial fraction before taking limits.

Finally, sample independent geometric letters with probability $2^{-a}$.
Then $J_q=3^q/2^{A_q}$ is a nonnegative mean-one martingale since
$\sum_{a\ge1}2^{-a}(3/2^a)=1$. At a first nonempty crossing of
$J_q\ge1/\theta$, the ternary measure of that word's legality class is
$3^{-q}=\Pr(w)/J_q\le\theta\Pr(w)$. The geometric first-cross words
are disjoint as symbolic events. Their total probability is at most
$\theta$ by the martingale maximal inequality. A union bound in ternary
space gives $\mu_3(H_\theta)\le\theta^2$.

## FS-011. Certified interval for the ordinary minimum density

The relative density of odd $t$ with **no** positive predecessor strictly
below $t$ belongs to $[0.522537,0.533554]$. In particular even after
removing all ternary multiples, these minima have positive density:
the ternary multiples contribute exactly $1/3$ of all odd targets,
since their only shortcut predecessors are successive doublings.
The interval follows from FS-010 and the finite integer computation below.

At depth $q$ a first unit-threshold crossing requires
$A\le b_q=\lfloor q\log_2 3\rfloor$. Let $N_q$ count compositions of
positive letters with this terminal condition and $A_i>b_i$ for
$i<q$. For depth up to $D$, start at total zero, take prefix sums in
the total to append a positive letter, count and discard states up to
$b_q$ at each stage, and truncate above $b_D$ throughout.
This gives all $N_1,\ldots,N_D$ exactly. Beyond $D$ the total expected
cross count is bounded by

$$
 \sum_{q>D}3^{-q}\binom{b_q}q
 \le \sum_{q>D}(97/100)^q .
$$

Indeed $b_q\le8q/5$ by $3^5<2^8$.
The coefficient bound $\binom{b_q}q\le 3^{b_q}/2^q$ and
$3^8<(6\cdot97/100)^5$ prove the geometric bound.

The [exact checker](check_minima.py) uses $D=512$ and verifies the total
union bound (finite sum plus geometric tail) is below $517167/10^6$.
For the stronger displayed density interval, it counts the *union*,
including overlaps, through depth 12. In each residue modulo $3^j$
store the smallest total excess $\sum(a_i-1)$ of an integral depth-$j$
word, capped above by $b_{12}-12$. This cap suffices because excess only
increases and $b_j-j$ is nondecreasing. For each possible first letter
compute its inverse residue on the smaller ring and add the first excess.
A residue counts if it hit at this or an earlier depth. The exact
depth-12 union is $247889/531441$. Add only $\sum_{12<q\le512}N_q3^{-q}$
and the geometric remainder to obtain an upper bound on the all-depth
union. Directed rational rounding of its complement gives the stated
interval. Increasing the exact-union depth makes the precision arbitrary
because the proved tail tends to zero.

The finite ordinary comparison enumerated all smaller odd starts for
odd targets through 100,000; every explored prefix reached a previously
classified suffix ending at one. Of 50,000 odd targets, 23,400 had a
smaller predecessor; 96 of those were beyond the depth-12 symbolic screen.
This finite sample supports the implementation only.

## FS-012. Conditional tail and the finite-depth entropy boundary

If a ternary endpoint residue modulo $3^q$ admits no cheap inverse
prefix through $q$, each legal length-$q$ word has $D=2^A/3^q>1$.
On that class its last inverse residue has Haar-uniform later ternary
digits: the affine map divides by $3^q$ with a unit numerator slope.
The same first-cross martingale bound at the new endpoint, with
threshold $1/D$, bounds the conditional probability of a later
crossing along that word by $D^{-2}$. Summing gives the conditional
upper bound $\sum_w(3^q/2^A)^2$, the usual finite-depth inverse pressure.
The union argument needs no independence between different inverse branches.

The positive ternary Haar mass of *all-depth* survivors also gives a
direct finite-screen limitation. Modulo $3^q$ at least a fixed positive
proportion of ternary-unit residues admit no cheap coefficient word
through $q$. For an ordinary endpoint $t$ in any such class, no actual
smaller odd predecessor within $q$ odd steps exists if
$t>q(3^q+1)/3$. Indeed for an integral prefix put
$D_i=2^{A_i}/3^i>1$. Then
$y_i=D_i(t-\sum_{j=1}^i(3D_j)^{-1})\ge D_i(t-i/3)$ and
$D_i/(D_i-1)\le3^i+1$.

Combine these classes with forward length-$l$ parity words all of whose
prefix coefficients $3^{q_i}/2^i$ exceed one. At least
$\binom l{\lceil l\log_3 2\rceil}/l$ such words exist by rotating a word
of that terminal weight after its minimum, as in the earlier entropy
packet. Each such word is one dyadic class, starts odd for $l\ge1$,
and gives no physical descent to its source through that clock.
Whenever $2^l3^q\le X/2$ and $X>q(3^q+1)/3$, CRT in $[X,2X]$
therefore supplies at least a constant times
$X\,2^{-l}\binom l{\lceil l\log_3 2\rceil}/l$ simultaneous candidates.
At this full-modulus budget the inverse screen gives no additional
exponential saving. These finite candidates can change with $X$; neither
this statement nor the all-depth population law constructs a least
counterexample to Collatz.

## Prior inverse-minimum and fixed-depth results

The versioned rStation manuscripts below precede this work. Paper 1 v3
proves genuine matched-depth minima and sharp additional-depth exclusions
on specified source cylinders, including arbitrarily long protected
prefixes with a later genuine forward escape. Paper 139 v2 extends
matched-depth minimality to balanced valuation words up to near the
critical slope. Paper 148 v1 permits unrestricted reference letters,
with exact cylinder tests and finite weight cutoffs for rival depths
$1\le r\le s$ relative to the supplied reference length $s$. These
are direct precedents for finite-word inverse-minimality tests.
[Paper 1 v3](https://rstation.ai/problems/collatz/papers/1/v3) ·
[Paper 139 v2](https://rstation.ai/problems/collatz/papers/139/v2) ·
[Paper 148 v1](https://rstation.ai/problems/collatz/papers/148/v1).

Paper 150 v2, Theorem 3, controls the minimum *shortcut cost* of reaching
a prescribed odd inverse depth at a Haar ternary input, including a
critical $3/2$ logarithmic correction and an effective deficit bound.
Its Corollary 4 gives a quantitative rare-cylinder visit bound and a
universal Haar-null set carrying at least $0.088551\ldots$ of any
limiting ternary empirical law of an escaping odd orbit. The
all-depth record argument above addresses a different limit: the least
actual ordinary source height at an unrestricted hit, measured over
ordinary target intervals. In particular the preceding fixed-depth
barrier and escaping-orbit rarity are prior results.
[Paper 150 v2](https://rstation.ai/problems/collatz/papers/150/v2).
