# How often an inverse word can save a prescribed factor

Write $j=11+162m$, $M=2^j-1$ and $Y_u=3^u2^{j-u}-1$ for
$0\le u\le j$. A physical witness is a positive integer $w$ with $T^h w=Y_u$.
Its surplus odd count is $q_h(w)-u$. The following ordinary estimate allows
all positive witnesses, including every residue of $w$, every meeting phase
through the peak, and arbitrary clocks.

For $F>1$ let $A_{N,F}$ be the nonnegative integers $m$ admitting such a
witness with $Fw<M$ and surplus odd count at most $\lfloor\log_3 N\rfloor$.
Then
$$
 \limsup_{N\to\infty}\ \sup_{a\ge0}
 \frac{\#(A_{N,F}\cap[a,a+N))}{N}\ \le\ \frac{486}{F^2}.       \tag{1}
$$
The actual least-parent cutoff $2^{40}w<z$ corresponds to $F_0=81\cdot2^{33}$:
$$
       81(z-2^{40}w)=128(M-F_0w)-143.
$$
The positive difference $M-F_0w$ is $22$ modulo $81$ and so is at least $22$.
Consequently the bound for this cutoff is $1/(27\cdot2^{65})$.
The bound remains valid with a larger allowance. For every fixed
$0<\delta<1/2$, one may replace $\lfloor\log_3 N\rfloor$ by
$$
 D_N=\left\lfloor\frac{\log_3 N+(1/2-\delta)\log_3(\log N)}
                      {H_2(\log_3 2)}\right\rfloor .
$$
Here $H_2(x)=-x\log_2x-(1-x)\log_2(1-x)$ and the inner $\log N$ is
natural. The leading allowance is about $1.05268\log_3 N$.
Words of greater surplus are outside this ordinary upper bound.

There is also a uniform lower density with the same quadratic exponent.
For an integer $n\ge1$ satisfying
$F(256/243)(16/27)^n\le1$, the parameters admitting physical witnesses at
phase zero already contain a union of residue classes of lower density at least
$$
           \frac{9}{26\cdot676} \cdot
           \frac{\binom{4n}{3n}}{3^{3n}} .                          \tag{2}
$$
If the source is required to be $17$ modulo $48$, replace $256/243$ by
$4096/2187$ and divide (2) by $27$. Choosing the least admissible $n$
gives $\gg F^{-2}/\sqrt{\log(2F)}$ in both cases. At $F_0$, the unconstrained
source takes $n=53$ and gives $2.6423\cdot10^{-29}$; the restricted source
takes $n=54$ and gives $3.4047\cdot10^{-31}$. These are lower bounds.
The denominator in (1) comes from an independent upper estimate. All
statements concern the supplied parameter and ordinary physical orbits.

## Arithmetic and mass of an inverse word

Use $E(y)=2y$ and $O(y)=(2y-1)/3$, admissible at $y\equiv2\pmod3$.
A word of length $V$ with $d$ letters $O$ has a nonnegative numerator $C$
and gives $3^d x=2^V y-C$. For every $y>0$, the condition
$2^Vy\equiv C\pmod{3^d}$ is necessary and sufficient for all intermediate
steps to be legal and positive. At the first letter $O$, the congruence
modulo three forces $y\equiv2\pmod3$. Subtract the common term and divide
the remaining congruence by three. A first letter $E$ just replaces $y$ by
$2y$. Induction proves sufficiency. At the other end of the word,
appending $E$ replaces $C$ by $2C$, and appending $O$ by $2C+3^d$.
Its parity thus recovers the last letter, proving that $(V,d,C)$ determines
the complete word. [Formal legality and numerator uniqueness](InverseMultiplicity.lean)
[Formal word equation and cylinder bound](InverseBudget.lean)

The first-crossing argument and the squared inverse-gain weighting
appear in Lyapunov Weaver's Paper 177/v1, §7, and Paper 179/v1, §4.
Paper 179 also sums such tails over a family of labels after an inverse
word has used its prescribed number of odd steps. The argument below
recovers the finite inequality in Lean. Its application here uses the
original exponential row's prepeak gates, the ordinary height correction
and an explicit growing surplus bound for counting in integer intervals.
[Paper 177/v1, §7](https://rstation.ai/problems/collatz/papers/177)
[Paper 179/v1, §4](https://rstation.ai/problems/collatz/papers/179)

The normalized slope of a word is $R=2^V/3^d$. Cut the inverse tree at
the first prefix with $R\le F^{-1}$. These prefixes form an antichain.
Give each $O$ independent weight $3/4$ and each $E$ weight $1/4$.
The ternary class size of a word factors as
$$
                   3^{-d}=R^2\,3^d/4^V .
$$
The Bernoulli weights of an antichain sum to at most one. All corresponding
ternary classes together therefore have Haar measure at most $F^{-2}$.
The elementary finite-level version holds for every horizon; monotone
convergence of the union gives the unlimited normalized-slope assertion.
[Kernel-checked finite-level inequality](InverseBudget.lean)

## Removing every prepeak phase at once

An ordinary inverse trace from $Y_u$ stays at least $M$ until its $u$th
odd inverse. After $p\le u$ odd inverses and $s$ doublings its state is
$$
       3^{u-p}2^{j-u+p+s}-b,\qquad 1\le b\le2^s.
$$
Initially $b=1$. An $E$ doubles $b$. If $p<u$, legality of an $O$ and the
remaining ternary factor force $b\equiv1\pmod3$ and replace $b$ by
$(2b+1)/3\le b$. The lower bound on the state follows from
$3^{u-p}\ge2^{u-p}$ and the displayed bound on $b$.
Thus every witness below $M$ traverses a gate $x=2^s2^j-b\ge2^s M$.
For each $s$ there are at most $2^s$ gate labels, independent of $u$.
The remaining word has exactly the stated surplus odd count.
[Kernel-checked full-phase gate](InversePhase.lean)

The map $m\mapsto2^{11+162m}$ changes ternary precision by exactly five,
as proved in the changing-center construction. For each fixed gate
$(s,b)$ this means a single class modulo $3^d$ in $x$ selects at most
one class modulo $3^{\max(d-5,0)}$ in $m$. Its Haar mass is at most
$243\cdot3^{-d}$. Charge the first postgate word with
$R\le(F2^s)^{-1}$ and sum $243\cdot2^s/(F2^s)^2$ over $s\ge0$.
This gives $486/F^2$ for all normalized gate classes. This argument permits
unbounded word length. Its conclusion is about ternary Haar measure.
[Exact precision proof](AdelicSwitch.lean)

## Converting a physical height saving into a slope saving

For a physical edge with odd inverse output $n$, its slope divided by the
actual output/input ratio is $1+1/(3n)$. Doublings have ratio exactly two.
The following uniform bound over all simple orbit segments controls that
product even when their lengths are unrestricted.

In a simple ordinary segment, write $X_h$ for the number of values in
$[2^h,2^{h+1})$. At most $h$ positions lack a following $h$-step segment.
Among the others with at least $3h/5$ odd inputs in those steps, each
parity word has one source residue modulo $2^h$. For $t=3/2$ a binomial
tilt bounds their number by $2^h\theta^h$, where
$\theta=(5/4)(2/3)^{3/5}<0.99$. The remaining positions with $q<3h/5$
map after $h$ steps to integers below
$2\,3^{3h/5}+(3/2)^h$, using
$T^hn\le3^q2^{-h}n+(3/2)^h-1$. Their endpoints are distinct by
simplicity. Hence $2^{-h}X_h\le6(0.99)^h$ for $h\ge1$.
If the entire segment lies above $2^L$ with $L\ge1$, its sum of
$1/(3n)$ is at most $200(0.99)^L$.

Given a physical witness below $M/F$, retain the gate and stop the tail
at its first visit to $w'<M/F$. The crossing is an odd inverse, whence
$w'\ge(2M/F-1)/3$. All earlier states of the tail are at least $M/F$.
Delete any loops within this tail. This shortens the word, preserving its
gate and endpoint and decreasing its surplus. With $L$ the integer part of
$\log_2((2M/F-1)/3)$, the product of the correction factors is at most
$1/(1-200(0.99)^L)$ whenever the denominator is positive. It follows that
the simplified tail contains a first normalized crossing with
$2^sR<1/F'$ for every fixed $1<F'<F$ once $m$ is sufficiently large.
Its surplus counts at most the surplus of the original witness.
This is the step that permits a physical endpoint inequality in (1).

## Counting in ordinary exponent intervals

Fix $F'$ as above and $D=\lfloor\log_3 N\rfloor$. Each selected tail word of
surplus $d\le D$ contributes at most $243N3^{-d}+1$ ordinary parameters
in any interval of length $N$, for each gate label. The mass part sums to
at most $486N/(F')^2$. For the extra one per cylinder the inequality
$2^{s+V}\le3^d/F'$ implies $d/V\ge3/5$ and $0\le s,V\le2d$ with $V\ge d$.
For each $s,V$, at most $2^s\binom Vd\le2^{s+V}\theta^V
\le(3\theta)^d$ labelled words occur. Thus the total rounding contribution
is $O((D+1)^2(3\theta)^D)=o(N)$, uniformly in the interval. The discarded
small parameters are finite for fixed $F'$; finally let $F'\uparrow F$.
This proves (1).

For the sharper allowance, the first normalized crossing ends with an
odd inverse. Thus for fixed $d$ the integer $k=s+V$ lies in
$$
 \bigl(d\log_2 3-\log_2F'-\log_2(3/2),\quad d\log_2 3-\log_2F'\bigr] .
$$
This interval has width less than one. There is at most one $k$ to charge.
Write $\alpha=\log_3 2$, $\theta=H_2(\alpha)$. For $k\ge d$,
$$
 \frac{2^s\binom{k-s}{d}}{\binom{k}{d}}
 =2^s\prod_{i=0}^{s-1}\frac{k-d-i}{k-i}
 \le[2(1-\alpha)]^s,\qquad 0\le s\le k-d ,
$$
because $k\le d/\alpha$. Since $2(1-\alpha)<1$, the sum of all the
rounding charges at this $d$ is $O(\binom{k}{d})$. Stirling's bound at
$k\le\lfloor d/\alpha\rfloor$ gives
$\binom{k}{d}\ll3^{\theta d}/\sqrt{d+1}$. Summing the geometric
growth through $D$ gives $O(3^{\theta D}/\sqrt{D+1})$. For the
displayed $D_N$ this is $O(N(\log N)^{-\delta})=o(N)$, with no
change to the Haar-mass or physical correction terms.

A Haar estimate by itself allows an open union of tiny measure to contain
all ordinary nonnegative integers. In (1) the growing surplus horizon is
essential to the rounding argument. No conclusion here excludes every
possible large-surplus witness of an individual $m$.

## Many positive cylinders with bounded multiplicity

Start at $M_m$. The five inverse odd gaps $(2,1,2,2,1)$ are all legal at
$M_0=2047$ and end at $2155$. They lift to all $m$ since
$M_m\equiv M_0\pmod{243}$. The endpoint is
$X_m=(256M_m-367)/243$, positive and less than $(256/243)M_m$.
By the exact precision identity it visits every residue modulo $3^d$ once
per $3^d$ successive values of $m$.

Take all words of length $V=4n$ and grade $d=3n$. Their common slope
is $(16/27)^n$. For a word let $B=C/3^d$ be its real offset. An odd
letter at position $i$ contributes $1/3$ times the product of the
subsequent slope factors, each factor being either $2$ or $2/3$.
Choose a word uniformly from the fixed-grade class. For any suffix of
length $l$, the expected product of its square-root slope factors is
at most $\rho^l$, where
$$
             \rho=(\sqrt2+\sqrt6)/4<0.966 .
$$
Indeed each factor is $\sqrt{2/3}(1+(\sqrt3-1)I)$, where $I$ indicates
a doubling. The probability that $t$ specified distinct positions are all
doublings is $(n)_t/(4n)_t\le(1/4)^t$. Expand the product, whose terms
are nonnegative. Using subadditivity of square roots now gives
$\mathbb E\sqrt B\le1/(\sqrt3(1-\rho))<17$. Thus more than $9/26$ of the
words have $B\le26^2=676$.

For exact checks, squaring gives $\sqrt2<70711/50000$,
$\sqrt6<4899/2000$ and $\sqrt3>433/250$, hence
$\rho<483/500$ and
$17(433/250)(1-483/500)=125137/125000>1$.
[Reproducible integer checks](check_adelic.py)

These words have $0<C\le676\cdot3^d$. For fixed $V,d$ an admissible
residue of $X_m$ fixes $C\bmod3^d$ and accounts for at most $676$ exact
numerators. Each numerator determines one word as above. This yields at
least $9\binom{4n}{3n}/(26\cdot676)$ distinct positive cylinders.
Each is physically legal and yields an ordinary positive $w$ smaller than
$(16/27)^nX_m$. This proves (2). For $w\equiv17\pmod{48}$, select one more
class modulo $27$ inside each cylinder so that its terminal is $27l+10$.
The lifted terminal sweeps all these residues by the same precision
identity. The ordinary source $48l+17$ reaches it in four steps and is
smaller than $(16/9)(27l+10)$. This proves the restricted formula.

Finally $\binom{4n}{3n}/3^{3n}$ equals $(16/27)^{2n}$ times the
probability of the mode $3n$ of a $\mathrm{Binomial}(4n,3/4)$ variable.
That probability is $\gg n^{-1/2}$ by Stirling's formula, or just by
Chebyshev's inequality on an interval of width $O(\sqrt n)$ about the
mean and maximality of the mode. Minimality of $n$ gives the asserted
dependence on $F$.
