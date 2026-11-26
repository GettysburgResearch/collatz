# What an unbounded coefficient-record gap costs

**Status — proposed written mathematics.** We work with one positive odd
ordinary trajectory, or an explicitly identified finite gap word. The
ordinary-source problem and the exclusion of nontrivial positive cycles
remain open.

## Results and their scope

| Question | Conclusion |
|---|---|
| How much integer height survives prime removal on an actual escape? | For any finite list of rational dyadic shifts, at least a lower fraction $\log_3 2$ of all native clocks simultaneously retain exponent $1-\epsilon$ of every shifted height after deleting an adaptively chosen bounded prime pool. All nonperiodic shifts give density one. The same fraction applies across a family of large primitive positive cycles. [Shifted ordinary cofactors](SHIFTED_COFACTORS.md) · [cycle extension](CYCLE_COFACTORS.md) |
| What is stronger for nonlinear polynomial values? | On every finite distinct ordinary path, the fraction retaining exponent $1-\epsilon$ tends to one for each fixed polynomial without rational roots, uniformly over growing pools with $r\log(2r)=o(\log N)$. A nonzero return resultant also bounds visits to adaptive finite-rank multiplicative cosets. [Polynomial cofactors](POLYNOMIAL_COFACTORS.md) |
| Which joint local limits must an ordinary escape have? | At least one record limit lies outside the rational diagonal, with no bound on gaps or assumption of positive record density. The dyadic record limits cannot all be negative periodic. With bounded gaps the ternary limits cannot all be rational dyadic units. [Rational diagonal theorem](RATIONAL_DIAGONAL.md) |
| How costly are long gaps on the actual positive path? | Finite ternary confinement forces the sparse inexact transitions and height lower bound proved below. Rational endpoint precision forces large drawdown; superlogarithmic gaps force almost full-size signed shadow denominators. [Two local ends](RATIONAL.md) · [joint precision and spacing](BRIDGE.md) · [long-gap denominators and the shallow corridor](LONG_GAPS.md) |
| Can growing, two-piece return words realize ordinary escape? | Eventually nondecreasing lengths are excluded at every growth rate. More generally, lengths tending to infinity require infinitely many distinct lengths to occur on at least ten separated runs. Grouped fixed-source template costs and a harmonic budget give the exclusion. [Template cost](RECORD_TEMPLATE_COST.md) · [repeated record words](MONOTONE_RECORDS.md) |
| What does positive limiting record occupancy see? | Actual odd-time-normalized flows have classified rational atoms. A positive-mass flow places at least $1-\rho/\delta$ of its ternary mass on an explicitly smaller-dimensional stratum. Conditional fibers of an ergodic finite-mean component have dimension $h/(L\log3)$ above its exact dyadic future. [Stationary flow](RECORD_FLOW.md) · [density spectrum](DENSITY_SPECTRUM.md) · [entropy fibers](ENTROPY_FIBERS.md) |
| Which numerical gates can carry persistent ordinary mass? | Heavy pre-gates are within $p^{-\log3/\log(3/2)}(\log p)^{O(1)}$ of the critical trace. At exponent $1<s<2$, leakage outside the specified sparse gate sieve has sharp order $X^{1-s}$; at $s=2$ it has sharp order $(\log X)/X$. [Gate proximity and leakage](GATE_PROXIMITY.md) |
| What happens to the previous bounded-record dimension? | The finite-alphabet proof survives the audit. The truncation defect has a three-term asymptotic, including its explicit constant. [Earlier proof audit](AUDIT.md) · [pressure calculation](PRESSURE.md) |
| How thin is the universal ternary critical trace? | The leading cube-root transition constant is $4.3758449\ldots$, with infinite measure at equality. At the first logarithmic refinement the measure is zero for $b>1$ and infinite for $b\le1$. The larger unrestricted incoming-slope set has a distinct exact integral test. [Elementary gauge](GAUGE.md) · [leading constant](SHARP_GAUGE.md) · [equality](CRITICAL_GAUGE_ENDPOINT.md) · [refined upper bound](CRITICAL_GAUGE_REFINEMENT.md) · [unrestricted test](INCOMING_GAUGE_TEST.md) |
| Which ordinary height counts enter these arguments? | The bounded-height proof and its effective convolution include a finite $2^{128}$ cap. The unrestricted simple-path Mellin proof is elementary; Weaver's Paper 28/v3 already gives stronger asymptotic ordinary bounds. [Height](HEIGHT.md) · [unrestricted visits](OCCUPATION.md) |
| What survives purely symbolic tests? | Arbitrary compact joint clusters in the specified no-rise-by-critical product have formal histories with diverging coefficients, long blocks and finite positive ordinary lifts. Formal laws can place all logarithmic height on a signed rational diagonal while retaining an off-diagonal cluster. The infinite dyadic addresses in these examples are irrational. [Escape of mass](ESCAPE_OF_MASS.md) · [log-height models and finite ordinary realizations](LOG_HEIGHT_MODEL.md) |

The finite arithmetic [Lean file](RenewalArithmetic.lean) proves
the two-ended divisibility and the centered Fourier carry injection.
The [exact controls](controls.py) and [receipt](CONTROLS.json) test
the indicated finite specializations. Independent audits in this
lane cover the [operator core](REVIEW_OPERATOR.md), [cycle
index](REVIEW_CYCLE_INDEX.md), [primitive pressure](REVIEW_PRIMITIVE.md),
[unrestricted gauge](REVIEW_UNRESTRICTED.md), and [numerical gate
arithmetic](REVIEW_GATE_ARITHMETIC.md), [regular logarithmic
occupation](REVIEW_REGULAR_OCCUPATION.md), [square-root record-gate
budget](REVIEW_ROUGH_GATES.md), and [landing frontiers and dyadic
cycle order](REVIEW_LEVEL_AND_ORDER.md). The [shorter Fourier
patch](CYCLE_SIEVE_REVIEW.md) strengthens the growing-prime cutoff
for the sibling rational-cycle construction.

The main remaining ordinary alternative is an off-diagonal or
nonrational cluster, potentially with unbounded return lengths
and zero elapsed-time record density. Even a singular distribution
at a signed cycle allows its physical integer differences to have
arbitrarily large factors outside every fixed prime pool. A proof by rational-diagonal confinement would
need a new fixed-source arithmetic statement, and positive cycle
uniqueness is a separate open obligation.

## A single set of ordinary clocks for every algebraic target

For one fixed injective positive ordinary shortcut trajectory $(x_t)$
there is a set $G$ of native times of lower natural density at least
$\log_3 2$ such that, simultaneously for every prime $p$ and every
number $\xi$ algebraic over $\mathbb Q$ in a chosen embedding into
$\overline{\mathbb Q}_p$,
$$
 \frac{\log^+(1/|x_t-\xi|_p)}{\log x_t}\longrightarrow 0
                        \qquad(t\to\infty,\ t\in G).                 \tag{4}
$$
When only algebraic numbers of degree at least two are tested, a
single set of **natural density one** works. These statements control
the precision relative to the logarithm of the actual integer. They
allow any tested coordinate to accumulate at fixed precisions, and
this native-time set can miss a sparse sequence of record clocks.

Indeed for any primitive integral minimal polynomial $f$ of a
tested number, factor $f$ over $\overline{\mathbb Q}_p$. At
ordinary integers the valuations of every factor $x_t-\xi_j$
are bounded below by $\min(0,v_p(\xi_j))$. Consequently
$v_p(x_t-\xi)\le v_p(f(x_t))+O_{p,f}(1)$ after omitting zeros.
Also $\ln|f(x_t)|/\ln x_t\to\deg f$. For any finite list of
polynomials and primes, and any prescribed precision tolerance,
the polynomial and linear theorems above give lower density at
least $\log_3 2$ for their simultaneous good clocks, or density
one when every polynomial has degree at least two and is irreducible.
To obtain a single set, enumerate these countably many polynomial
and prime tests at tolerances tending to zero and let $G_j$ impose
the first $j$ tests. For $c=\log_3 2$ or $c=1$ as appropriate,
choose increasing $N_j$ so every prefix of length $N\ge N_j$ has
at least $(c-1/j)N$ clocks in $G_j$. On $[N_j,N_{j+1})$ use
$G_j$. At a prefix ending in stage $j$, all earlier stages were
supersets of $G_j$ (the finite initial prefix can be included).
Hence the union has lower density at least $c$ and each fixed
test eventually holds on it. This proves (4).

## Conventions and scope

Write $U(x)=(3x+1)/2^{v_2(3x+1)}$, let $e_i$ be the chronological odd
gaps and let $M_k=3^k/2^{e_1+\cdots+e_k}$. On a nonrepeating positive
ordinary orbit the simple-path reciprocal estimate T-A3-651 gives
$x_k/M_k\to L\in(0,\infty)$. Indeed this ratio is the initial value
times the product of $1+1/(3x_i)$. Distinct positive odd integers tend to
infinity, hence $M_k\to\infty$ and its strict upper records $k_l$ are
cofinal. Include $k_0=0$. Put $q_l=x_{k_l}$.

A chronological block $w=(e_1,\ldots,e_m)$ between successive records
has prefix clocks $S_j=e_1+\cdots+e_j$, $S_0=0$, and local
multipliers $P_j=3^j/2^{S_j}$. Thus $P_j<1$ for $0<j<m$, and
$r=P_m>1$. Conversely these inequalities define the first-ladder
alphabet without any length cutoff. There are no ties, by unique
factorization. With $\alpha =\log_2 3$, the last gap is one and
$S_m=\lfloor\alpha m\rfloor$. Indeed
$0<\log_2 P_m\le\alpha -1<1$. In particular $1<r\le3/2$.
The exact chronological affine map is

$$
 F_w(z)=r(z+h_w),\qquad
 h_w=\frac13\sum_{j=0}^{m-1}P_j^{-1}\ \ge\ m/3.                 \tag{1}
$$

It maps rational inputs to rational outputs, is invertible over
$\mathbb Q$, and acts continuously on $\mathbb Z_3$. Define the
block drawdown in binary logarithms by
$D(w)=\max_{0\le j<m}(-\log_2 P_j)\ge0$.

## 1. Finitely many ternary accumulation points force rare transitions

Let $K\subset\mathbb Z_3$ be the set of subsequential limits of
$q_l$, and call a finite word recurrent when it occurs as an entire
record block at arbitrarily late indices. No bound on record gaps is
assumed in the following result.

**Theorem 1 (recurrent words and ordinary clock cost).** If $K$ is
finite, only finitely many distinct record words are recurrent. Label
each sufficiently late $q_l$ by its unique nearest point $u_l\in K$.
Call its next edge exact when $F_{w_l}(u_l)=u_{l+1}$. There are
infinitely many inexact edges. Along those edges the block lengths tend
to infinity. Every consecutive run of exact edges starting at a
sufficiently late height $q$ has total shortcut clock at most

$$
                         \log_2 q + O_K(1).                         \tag{2}
$$

The clock counts all gaps on the run. In particular, unbounded lengths
among the *recurrent* words already force an infinite ternary cluster
set even if other gaps can be arbitrarily long.

*Finite edge alphabet.* For each ordered pair $u,v\in K$, consider all
first-ladder words satisfying $F_w(u)=v$ in $\mathbb Q_3$. The two
coordinates are either both rational or both irrational, since the
affine map has nonzero rational slope and rational offset. In the
rational case the same equality holds in $\mathbb R$. Equation (1)
gives $m/3\le v/r-u\le \max(v,0)-u$. There are finitely many words
of bounded length, since their total clock equals $\lfloor\alpha m\rfloor$.
For an irrational ordered pair, two distinct affine maps taking $u$
to $v$ would give a nonzero rational affine equation for $u$;
parallel unequal maps cannot agree either. Equal maps have equal
slopes, hence equal $m,S_m$, and equal integer carries
$C=\sum_{i=1}^m3^{m-i}2^{S_{i-1}}$. The valuation of
$C-3^{m-1}$ is $e_1$ for $m\ge2$; removing the first summand and
dividing by $2^{e_1}$ recovers the carry of the remaining word. The
last letter is fixed by the total clock. Thus the maps themselves
determine the words. The set of exact labeled edges is finite.

Compactness gives $d_3(q_l,K)\to0$, so distinct labels are separated
for all sufficiently late times. Every recurrent word occurs infinitely
often at one fixed pair of labels. Continuity gives an exact edge at
that pair. For each fixed $J$, there are only finitely many words of
length at most $J$ and pairs of labels, so all sufficiently late
inexact edges have length greater than $J$.

*Paths in the exact graph.* A nonempty directed loop has composite
$z\mapsto(3^m z+C)/2^s$ with $3^m>2^s$, positive odd $C$, and
$s\ge1$. Its unique fixed point $C/(2^s-3^m)$ is negative with
odd numerator and odd denominator prime to three. The same holds at
each vertex on the loop, by rotation. Starting at a rational of
2-adic valuation zero and denominator prime to three, a gap larger
than the genuine $v_2(3z+1)$ makes the next valuation negative.
A smaller gap makes it positive, followed by a negative valuation at
the next step. Once negative, every gap subtracts its clock from that
valuation. Thus any finite concatenation between two loop vertices
consists exclusively of genuine signed rational gaps. From a loop
vertex the genuine subsequent gap sequence is periodic: one return
replays its deterministic signed gap word. Its first strictly
increasing coefficient time from any given record phase is unique.
Consequently an exact path between loop vertices follows this single
deterministic periodic itinerary throughout. In particular it cannot
move to a different cycle itinerary while retaining such endpoints.

For an arbitrary consecutive exact run, take its first and last
vertices that belong to any loop. Before and after them there are at
most $|K|$ edges each, because repetition would create a loop there.
If there is no loop vertex at all, its length is bounded as well.
The finite exact alphabet bounds all the clocks and affine constants
of these outer pieces by constants depending on $K$. Along the central
piece let $a/d<0$ be its first rational label, with $d>0$ odd, and
let $y$ be the positive ordinary value there. At its end the same
gaps take these starting values to $a'/d$ and $y'$, with
$a'\in\mathbb Z$, by the genuine signed gap rule. If the central
piece has $b$ odd gaps and total clock $s$, subtraction gives
$3^b(dy-a)=2^s(dy'-a')$. Hence $2^s\mid dy-a$, a positive
integer. There are finitely many choices of $a/d$ and
$y\le C_K(q+1)$ by the bounded initial piece. Adding the bounded
outer clocks proves (2). An infinite final exact run would contradict
(2) for its fixed positive start, so there are infinitely many
inexact edges. This proof uses the real positivity of that very
ordinary source.

**Corollary 1.1 (frequency in height).** Write $N_l$ for the number
of inexact edges from a fixed sufficiently late record up to record
$l$. With natural logarithms,

$$
 N_l\ \ge\ \frac{\log\log q_l}{\log(\log_2 3)}-O_{K,x_0}(1)
 \qquad(q_l\to\infty).                                           \tag{3}
$$

On each individual edge, $q_{l+1}/q_l\le (3/2)C_{x_0}$, by the
uniform finite distortion $1\le (x_k/M_k)/x_0\le C_{x_0}$.
For a full or partial exact run with shortcut clock $s$, its
coefficient is at most $(3/2)^s$, since the odd count is at most
the clock. Thus its endpoint is at most $C_{K,x_0}q^{\log_2 3}$
by (2). Alternate such runs with single inexact edges, including the
initial and terminal partial runs. Taking logarithms gives
$\log q_l\le C_{K,x_0}(\log_2 3)^{N_l+1}$, proving (3).
The count concerns the inexact edges defined from the true limit set.
It does not claim a positive temporal density of them.
