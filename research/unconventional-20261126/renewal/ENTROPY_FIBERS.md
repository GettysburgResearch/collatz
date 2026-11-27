# Conditional ternary dimension above an exact dyadic record address

**Status — PROPOSED actual-flow theorem.** Take a positive-mass
subsequential record-flow limit of one positive ordinary
nonrepeating trajectory, as in [Theorem F](RECORD_FLOW.md).
Normalize and represent it by a stationary two-sided process of
actual limiting labeled edges as in [Theorem M.1](DENSITY_SPECTRUM.md).
Work in any ergodic component with finite mean odd block length $L$;
almost every component has this property. Write $h$ for the
entropy rate, in nats per complete first-ladder word, of its
stationary label process. Let $\mu$ denote the joint two-local
record-coordinate law in that component.

**Theorem Q.** For $\mu_2$-almost every dyadic address $x$, the
conditional distribution $\nu_x$ of the ternary address given
$x$ is exact dimensional with
$$
 \lim_{n\to\infty}
 \frac{-\log \nu_x(z+3^n\mathbb Z_3)}{n\log3}
                   =\frac{h}{L\log3}
            \quad\hbox{for }\nu_x\hbox{-almost every }z.            \tag{Q1}
$$
In particular $h>0$ forces, above almost every such dyadic address,
a ternary fiber of the actual joint cluster set of Hausdorff dimension
at least $h/(L\log3)$. If this cluster set has only countable
ternary fibers, every finite-mean component has zero label entropy.
These are consequences for the supplied orbit's limiting
occupancy. No positive-entropy component is asserted to exist.

General exact-dimensional projection theorems for conformal systems
use projection entropy to account for overlaps. Here a uniform
subexponential count at typical finite-mean histories retains the
full *conditional past-label* entropy after ternary projection.
[Feng and Hu, 2009, related Euclidean result](https://doi.org/10.1002/cpa.20276)

## What is conditioned on

Let $w_i$ be the block from record $i$ to record $i+1$. By the
dyadic edge equations, the entire forward list
$w_0,w_1,\ldots$ determines the dyadic address $x$:
the common native prefix of accumulated clock $s$ fixes its residue
modulo $2^s$, and these clocks tend to infinity. Conversely the
bits from $x$ are genuine and the first strict coefficient crossing
parses them uniquely into these blocks. To see genuineness on a
given edge, the final odd dyadic bit and the affine equation over
$\mathbb Z_2$ put the input in the exact native parity cylinder;
equivalently replaying the assigned native word backwards from its
integral terminal reconstructs the unique congruence. Thus the
future labels and the dyadic point generate the same measurable
information. The infinite past labels determine the ternary
coordinate by the $3^{-m}$ contraction per block. These statements
also apply after projecting away the circle coordinate.

The single-label entropy is finite. For instance the number of
labels of odd length $m$ is at most $2^{\lceil\alpha m\rceil}$,
where $\alpha=\log_2 3$. Comparing the label law to the normalized
reference weights $e^{-a m}$ on individual labels for any sufficiently
large $a$ gives $H(w_0)\le aL+\log\sum_w e^{-a|w|}<\infty$.
This is the elementary entropy inequality, first for finite
partitions and then by truncation. Take the conditional probability
of the realized label $w_{-1}$ given the entire future and write
$I$ for its negative logarithm. By the entropy chain rule and
decreasing conditional entropies, $E I=h$, the usual label entropy
rate. More explicitly, the entropy of one preceding label
conditioned on a future of length $k$ decreases to the corresponding
infinite-future entropy, by martingale convergence and finite
single-label entropy; its Cesàro average is the normalized entropy
of the $k$-block partition.

For almost every sample, the conditional probability of its $k$
realized past labels given the future is the product of the
one-step conditional probabilities at those $k$ shifts. This
follows by successive conditioning on the previously revealed,
countable-valued labels. Ergodicity and Birkhoff's theorem give
$$
 -k^{-1}\log \Pr(w_{-k},\ldots,w_{-1}\mid w_0,w_1,\ldots)\to h,
 \qquad n_k/k\to L,                                                \tag{Q2}
$$
where $n_k=\sum_{i=1}^k |w_{-i}|$. Also
$\max_{1\le i\le n+1}|w_{-i}|=o(n)$ almost surely:
stationarity and finite mean give
$\sum_i\Pr(|w_{-i}|>\eta i)<\infty$ for each $\eta>0$.
Borel–Cantelli and discarding a finite initial list prove the maximum
assertion. All these full-measure statements hold under the
conditional past law for almost every future, by disintegration.

## Upper local dimension and arbitrary clocks

Fix such a future. At past depth $n$ use the first full block
boundary $n_k\ge n$. Its conditional cylinder has probability
$\exp[-(h+o(1))k]$ on a typical sample and maps entirely into
the ternary ball of depth $n$. As $n_{k+1}/n_k\to1$,
$k/n\to1/L$. This gives the upper bound on pointwise dimension
in (Q1), including all intermediate depths.

For the opposite bound, fix $0<\eta<1/2$. Exhaust the typical
conditional pasts by sets on which the convergences in (Q2) and
the maximum bound above hold, to accuracy $\eta$, at every
sufficiently large index with a *common* starting index. Also
bound the total length of the first finitely many blocks before
that index by a common constant. Such sets, with the thresholds
and constants increased, exhaust conditional measure one. Fix one
set $G$ of this kind of positive conditional mass and let
$\nu_{x,G}$ be its ternary image measure before renormalization.

In a compatible prefix of $n$ backwards gaps all blocks meeting
it have length at most $J=\lceil\eta n\rceil$ for sufficiently
large $n$. If at least $J$ letters remain, the maximum among the
nonempty inverse multipliers $2^{S_i}/3^i$ in the remaining prefix
is attained uniquely at the end of its first complete reversed
block. Each proper prefix of that block has smaller multiplier
by the strict first-ladder property, and every continuation
across the boundary multiplies by a number strictly less than
one. Thus the concrete prefix forces all complete labels through
some depth $l\ge n-J$, with no boundary supplied externally.
If $k$ labels were forced, uniformity on $G$ gives
$k\ge l/(L+\eta)$ and their conditional mass is at most
$\exp[-(h-\eta)k]$ for $n$ large. The fixed bound on initial
blocks ensures $k$ passes the required threshold. When $h=0$
the nonnegative lower bound in (Q1) is immediate; assume
$0<\eta<h$ in this estimate otherwise.

For each full or incomplete piece of at most $J$ letters,
its native clock is at most $\alpha J$ and its real inverse
multiplier is at most one. Its normalized inverse affine offset
is at most $J3^J$, for example by bounding each summand in the
finite carry formula. All piece multipliers are at most one,
so for the entire prefix $0\le C/3^n\le(n+1)J3^J$. At fixed
total native clock and fixed target residue the integer $C$ lies
in one class modulo $3^n$ and uniquely determines that gap
prefix, by the valuation decoder in [the trace proof](GAUGE.md).
The native clock is less than $\alpha n$ for the entire backwards
critical prefix. Summing those clocks shows that at most
$\exp(\eta n\log3+O(\log n))$ compatible gap prefixes on $G$
meet a given depth-$n$ ternary cell. Multiplying by their
forced-cylinder conditional probability bounds the restricted
measure on every such cell by
$$
 \exp\!\left\{-n\left[
       \frac{(h-\eta)(1-\eta)}{L+\eta}
       -\eta\log3\right]+O(\log n+1)\right\}.                      \tag{Q3}
$$
This conditioning on the actual future is essential. Attaching
independent pasts to it would not generally reproduce the record
flow.

Finally $\nu_{x,G}\le\nu_x$. The ratios of their masses on nested
ternary cells converge to $d\nu_{x,G}/d\nu_x$ almost everywhere
by the martingale differentiation theorem. This derivative is
strictly positive at $\nu_{x,G}$-almost every point. Hence the
lower local dimension bound in (Q3) holds also for $\nu_x$ at
$\nu_{x,G}$-almost every point. Exhaust by the good sets, then
take a countable sequence $\eta\downarrow0$. Together with the
upper bound this proves (Q1). The joint cluster set is closed
and carries the stated joint law because it carries every
limiting vertex marginal; its fibers therefore carry the
conditional laws almost everywhere. Positive exact dimension
implies the asserted Hausdorff dimension lower bound on these
fibers and excludes their countability.
