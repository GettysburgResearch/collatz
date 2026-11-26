# What mandatory log-height occupation still permits

**Status — PROPOSED countermodels and ordinary finite realizations.**
The signed cycle $-1$ is fixed by the odd native shortcut. Sampling
every logarithmic height between consecutive coefficient records
gives total mass one on any formal script with $M_i\to\infty$ after
normalization by the accumulated height. Continuous sampling also
gives uniform angular measure modulo any fixed log-height period.
Neither observation forces positive label entropy. The examples
below retain the exact Collatz gap maps and distinguish a single
ordinary initial source from varying finite lifts.

Write $\alpha=\log_2 3$, $\delta=\alpha-1$, let $a_m=\{\alpha m\}$
in binary logarithms, and take the genuine first-ladder word
$$
 B_m=2^{[u]}1^{[v]},\qquad
 u=\lfloor\alpha m\rfloor-m,\quad v=m-u .
$$
Brackets count *letters*, not numerical powers. For $0<a_m<\delta$
and large $m$ this word has positive final log rise $a_m$. Its
proper prefixes stay below zero: it first descends through gaps
two, then rises by $\delta$ per gap one, and ends by a rise from
$a_m-\delta<0$. As $m\to\infty$, both $u$ and $v$ tend to infinity.
The native words corresponding to its two pieces are repetitions
of $10$ and $1$, respectively.

## All roofs on labels tending to infinity

Fix any irrational $\lambda\in(0,\delta)$. At stage $j$ choose six
distinct feasible lengths $m$ larger than all preceding stage lengths
and with $|a_m-\lambda|<1/j$, restricting further to a fixed compact
subinterval of $(0,\delta)$. Irrational rotation provides arbitrarily
many candidates. Divide the six lengths into three pairs. Precompute
the stage alphabets; delay the first record of each stage $j\ge2$
to an index $N_j\ge\exp(\max m)$ in that stage, and choose
$N_{j+1}-N_j\to\infty$. This is possible by using the preceding
stage for as long as needed. Ignore the fixed finite initial stage
when applying the resulting asymptotic bounds.

Use the letters of a ternary squarefree sequence as successive pair
labels. At record $i$, choose freely one of the two words in the
indicated pair of its current stage. Distinct complete first-ladder
words are incompatible forward prefixes: a common first strict
crossing determines the end of the word. Thus these choices can
be made to exclude the $i$th element in an enumeration of
$\mathbb Q\cap\mathbb Z_2$ from the forward native cylinder whenever
it has not already been excluded. One obtains a single irrational
dyadic starting address. The ternary squarefree word may for example
be Thue's fixed point of $0\mapsto012$, $1\mapsto02$, $2\mapsto1$.
[Squarefreeness of this word](https://www.lirmm.fr/~ochem/morphisms/pairs.pdf)

The resulting complete record-label list has no square $WW$ with
$W$ a nonempty word of complete labels, since the labels project
onto their squarefree pair labels. Within its arbitrarily long
stages some fixed length occurs on many separated occasions,
as required by the [harmonic run obstruction](MONOTONE_RECORDS.md).
The lengths tend to infinity and are $O(\log(i+2))$ eventually,
and their accumulated odd time is $O(l\log(l+2))$ by record $l$.
The deep local drawdown is $O(m_i)$; the log coefficient at the
starts grows as $(\lambda+o(1))i$. Thus $M_n\to\infty$ at all
odd depths, and $\sum_n M_n^{-s}<\infty$ for every $s>0$.
In particular this example satisfies the length-only necessary
condition $k_l=o(l\log M_{k_l})$ in the fixed-library test
[Theorem T](RECORD_TEMPLATE_COST.md), unlike a staircase with
$m_l\asymp l$.

Every record start tends dyadically to $1$ because its future begins
with $u\to\infty$ copies of gap two. Every record endpoint tends
ternarily to $-1$ because its preceding suffix has $v\to\infty$
copies of gap one. The ternary coordinate can be propagated
forward from any fixed element of $\mathbb Z_3$; the gap-one map
multiplies differences from $-1$ by $3/2$.
Set $t_i=\log_2M_{k_i}\bmod1$. Every limiting empirical law of
$t_i$ is invariant under addition of $\lambda$: replacing the true
next increment $a_{m_i}$ by $\lambda$ costs $o(1)$ on continuous
tests, and time-shifting by one index costs a boundary term.
Irrationality forces normalized Haar measure. Roof weighting has
the same limit because $a_{m_i}\to\lambda>0$. Sampling along the
whole intervals $[t_i,t_i+a_{m_i}]$ also gives Haar measure,
with the local pair still $(1,-1)$. Thus the mandatory probability
has escaped to infinite labels despite a roof bounded away from
zero throughout. The elapsed-time-normalized complete-edge mass
vanishes.

## All limiting height on a signed periodic diagonal

A second script alternates successively a block of
$r_j=\lfloor\sqrt j\rfloor+1$ *single* gap-one records and one
long exceptional complete word $B_{m_j}$. Choose its length in
$[\log(j+2),C\log(j+2)]$ with $a_{m_j}$ in a fixed nonempty
subinterval of $(0,\delta)$. For all large $j$ there are at least
two possibilities, by equidistribution; finite initial cases may
be adjusted. At these exceptions again diagonalize against all
rational dyadic seeds. Every long word starts with a growing
gap-two run and ends with a growing gap-one run.

Apart from $O(j)$ exceptional complete words, the first $j$ stages
have order $j^{3/2}$ single gap-one records. For every fixed $D$,
all but $O_D(j)$ of these have at least $D$ consecutive gap-one
records on each side. At their centers the dyadic coordinate lies
within $2^{-D}$ of $-1$ and the ternary coordinate within $3^{-D}$
of $-1$. Each ordinary-symbol gap-one record contributes the
same positive roof $\delta$, and the other roofs are at most
$\delta$. Hence the full limiting record-count and roof-weighted
local laws are both the point mass at $(-1,-1)$. The angular
law at record starts is Haar by the time-shift argument with
irrational increment $\delta$ outside a zero-density set; whole
height-interval sampling is Haar as well. The limiting edge
process has zero entropy. Yet the joint cluster also contains
$(1,-1)$ at starts of the blocks $B_{m_j}$, of zero limiting
height occupancy. This distinction is consistent with the
unconditional [rational-diagonal cluster theorem](RATIONAL_DIAGONAL.md).

At all odd depths $M_n\to\infty$ exponentially in the native clock:
the $O(j\log j)$ native bits in the exceptional words are negligible
among the order $j^{3/2}$ single gap-one records, including partial
stages. Each of the two scripts above can be executed to every
finite depth from some positive integer in its exact native
cylinder. Its one infinite dyadic address was expressly chosen
irrational. The angular laws apply also to any fixed positive *real*
initial value propagated by the assigned affine script: its value
divided by $M_n$ converges to a finite positive limit by the exact
carry formula. This real propagation does not impose ordinary
parity at that initial value.

For either script the full native omega language has entropy zero.
After a sufficiently late date, all constant-pattern runs in the
two regimes $(10)^\infty$ and $1^\infty$ have lengths exceeding
any prescribed threshold. This holds also across stage boundaries
after adjacent identical regimes are merged. Every finite
window seen arbitrarily late therefore has at most one change
of regime, giving only $O(n)$ recurrent factors of length $n$.
The upper rate says nothing about finite nonrecurrent factors
near the initial date.

## A known-basin ordinary check over growing logarithmic heights

For every $m\ge1$ let $t=3^{m-1}$,
$R=(2^t+1)/3^m$ and $x=2^mR-1$. The quotient is an odd positive
integer: repeatedly factoring $z^3+1=(z+1)(z^2-z+1)$ at
$z=2^{3^j}\equiv-1\bmod3$ adds at least one ternary factor per
iteration from $2+1$. The *actual* native states are
$$
          T^i(x)=3^i2^{m-i}R-1\quad(0\le i\le m),
          \qquad T^m(x)=2^t .
$$
All $m$ departures are odd and the endpoint descends to $1$ by
halving. For $D\le i\le m-D$ these positive genuine states are
simultaneously within $2^{-D}$ and $3^{-D}$ of $-1$. The
logarithmic coefficient-height gain is $m\log(3/2)$, tending to
infinity. Its interior normalized occupation converges to the
same signed rational atom and Haar mantissa by irrational rotation;
an arbitrary initial angle does not affect that convergence.
This is a uniform sequence of finite windows in the verified
basin, with their positive sources increasing. It does not supply
a persistent mass from any one fixed bounded source.

Thus neither mandatory logarithmic height nor zero-entropy fiber
classification, even paired with these finite ordinary checks,
forces positive entropy or positive height occupancy outside the
rational diagonal. Excluding either symbolic alternative for one
fixed positive ordinary starting point requires additional integer
arithmetic. The full arithmetic cofactor bound in the adelic
Theorem A is not asserted for the artificial scripts.
