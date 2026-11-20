# A critical negative-moment criterion from uniform orbit sparsity

**PROPOSED source-qualified deduction. The arithmetic criterion remains
OPEN, and nontrivial positive cycles are a separate obligation.** The
critical logarithmic saving already proved in the pinned interval-count
source upgrades a logarithmic partial-sum obstruction to a finite
infinite-series obstruction. It does not prove that the actual arithmetic
moments violate that obstruction.

## Exact source boundary

The two inputs are:

1. PR146 at `fd991063721e9c157d318e40bb20131762f7d750`,
   `research/upper-bit-mergers/CRITICAL_INTERVALS.md`, equation (1) and
   its section "Critical reciprocal-power summability". For the
   distinct values of any one ordinary orbit it gives the uniform count
   `O(N^rho/(1+log N)^(3/2))` in every interval of length `N`, and hence
   a finite reciprocal-power sum at the critical exponent itself.
2. PR169 at `6cb9bfdc828f91576066b0e4a099d47d8144e915`,
   `research/certificate-renewal-20261121/MOMENT_QUANTILES.md`, MQ1--MQ2,
   for the exact primitive-word moment and its comparison with the
   contribution from one fixed ordinary source. The moment identity and
   its pointwise consequence are reconstructed below.

The comparison with the fifth-denominator estimate uses the same PR169
head, `FIXED_ENDPOINT_SUMMABILITY.md`, ES3--ES4. No independent-residue
model or GRH consequence is assumed. The critical interval-count theorem
is an imported source-qualified theorem, not a consequence of the finite
checks associated with this note's neighboring sieve programs.

## CNM1. Definitions and the fixed-source lower bound

Let

\[
p=\log_3 2,\qquad
\rho=-p\log_2p-(1-p)\log_2(1-p)
      =0.949955527\ldots .
\]

For a word `w=(a_1,...,a_q)` of positive accelerated valuations, put

\[
A_j=\sum_{i=1}^j a_i,\quad A_0=0,\qquad
C_w=\sum_{j=0}^{q-1}3^{q-1-j}2^{A_j},\qquad
J_w=3^q2^{-A_q}.
\]

Let `r_w` be the unique positive odd representative below `2*3^q`
such that `2^(A_q)r_w=C_w mod3^q`, and set

\[
b_w=(2^{A_q}r_w-C_w)/3^q,
\qquad P_q=\sum_w\frac{J_w^4}{r_w^2},
\qquad Q_q=P_q+\tfrac12(3/5)^q.
\tag{C1}
\]

The imported primitive-source calculation gives `b_w` positive odd,
`b_w<2^(A_q+1)`, and exactly the source cylinder

\[
n=b_w+2^{A_q+1}k\quad(k\ge0),\qquad
U^q(n)=r_w+2\cdot3^qk.
\]

For reference, positivity is part of the exact ordinary calculation.
The full inverse numerator enforces every integral odd inverse step.
A negative odd source stays negative under every legal forward odd
step, so it could not end at the prescribed positive `r_w`; zero is
not odd. This excludes a merely formal rational-word interpretation.

Positive summation over the disjoint ordinary source cylinders gives

\[
\mathcal D_q:=\sum_{n>0\text{ odd}}
\frac{J_q(n)^4}{U^q(n)^2}
=P_q+R_q\le Q_q,
\tag{C2}
\]

where

\[
0<R_q<\tfrac12(3/5)^q.
\]

Indeed `sum_w J_w^4=(27/5)^q`; bounding the positive higher-source
terms by `sum_(k>=1)k^(-2)<2` gives the stated envelope. All sums are
finite at each fixed `q` because `P_q<=(27/5)^q`.

Suppose one fixed positive odd source `n_0` has a nonperiodic orbit
`n_q=U^q(n_0)`. Here nonperiodic means not eventually periodic, so
all its ordinary states are distinct. Exactly

\[
n_q=n_0J_q(n_0)I_q,
\qquad I_q=\prod_{j<q}\left(1+\frac1{3n_j}\right).
\tag{C3}
\]

The critical count below implies `sum_j 1/n_j<infinity`, so there is
a finite constant `M` with `1<=I_q<=M` for every `q`. Retaining just
the same original source `n_0` in C2 proves

\[
\boxed{Q_q\ge\frac{n_q^2}{n_0^4M^4}.}
\tag{C4}
\]

No source is replaced when `q` changes. This is the pointwise MQ2
inequality, with its correction-product factor retained.

## CNM2. The full critical negative series is finite on any counterexample

The critical interval theorem applies to the odd orbit states because
they form a subset of one simple shortcut orbit. In the shell
`[2^h,2^(h+1))`, it gives at most

\[
K\frac{2^{\rho h}}{(1+h)^{3/2}}
\]

states, for one absolute finite `K`. Hence

\[
\sum_{j\ge0}n_j^{-\rho}
\le K\sum_{h\ge0}(1+h)^{-3/2}<\infty.
\tag{C5}
\]

This uses the logarithmic saving at the critical exponent; a bare
`O(N^rho)` count would give a divergent shell upper bound. Since
`0<rho<1` and every `n_j>=1`, C5 also gives the reciprocal sum needed
for the uniform product bound in C3.

Raise C4 to the negative power `-rho/2` and sum nonnegative terms:

\[
\boxed{\sum_{q\ge1}Q_q^{-\rho/2}
\le n_0^{2\rho}M^{2\rho}
     \sum_{q\ge1}n_q^{-\rho}<\infty.}
\tag{C6}
\]

Consequently the following purely arithmetic statement would exclude
every nonperiodic positive orbit:

\[
\boxed{\sum_{q\ge1}
\left(P_q+\tfrac12(3/5)^q\right)^{-\rho/2}=\infty.}
\tag{CN}
\]

CN is a sufficient condition that has **not** been proved for the
actual moments C1. Its deduction does not require numerical knowledge
of `K`, `M`, or the hypothetical fixed source.

## CNM3. A critical quantile version

C4 and the same count give a slightly more general sufficient target.
For any hypothetical nonperiodic original source, there is a finite
constant `K_(n_0)` such that, for every `Y>=1`,

\[
\boxed{
\#\{q\ge1:Q_q\le Y\}
\le K_{n_0}\frac{Y^{\rho/2}}{\log(2Y)^{3/2}}.}
\tag{C7}
\]

Indeed those times have `n_q<=n_0^2M^2 sqrt(Y)` by C4. Apply the
uniform count in the initial interval up to that height. Changing the
fixed scale inside the logarithm and treating a bounded initial range
only changes the finite constant. The orbit's states are distinct,
so this really counts times and not just endpoint values.

Thus it would also suffice to establish

\[
\boxed{\sup_{Y\ge1}
\frac{\log(2Y)^{3/2}}{Y^{\rho/2}}
\#\{q\ge1:Q_q\le Y\}=\infty.}
\tag{CQ}
\]

The count can equivalently be restricted to `1<=q<=N` and the
supremum taken over `N,Y`. CN implies CQ: if the displayed normalized
counts were bounded, dyadic decomposition in the values of `Q_q`
would bound the series in CN by a convergent multiple of
`sum_h (1+h)^(-3/2)`. Finitely many values below one cause no problem;
if there were infinitely many, CQ would already hold at `Y=1`.

## Why this strengthens the prior moment target

For every fixed `alpha>rho`, PR169 MQ3 obtains an `O(log N)` bound
on `sum_(q<=N) Q_q^(-alpha/2)`. The critical input yields the full
finite series C6, with the smaller negative exponent `rho/2` and
without normalizing partial sums by a logarithm.

The prior quantile-excess condition with normalization `Y^(-alpha/2)`
implies CN. To see this, if the critical series were finite with total
`B`, then `# {q:Q_q<=Y}<=B Y^(rho/2)`, so all the old normalized
counts for `Y>=1` would be bounded by `B`. The prior bounded-liminf,
chronological negative-moment and positive-average conditions imply
that old quantile-excess condition, as proved in the pinned source.

The improvement is strict at the level of possible positive comparison
sequences. For example, `Q_q=q^(2/rho)` makes CN the divergent harmonic
series. For every `alpha>rho`, its old normalized quantile count is
bounded, its old negative-moment series converges, and its old
positive-average smallness condition fails. This is an illustrative
sequence, **not** an asserted model or estimate for the actual C1.

## Fifth-denominator summability does not yet prove CN

PR169 ES3 establishes the unconditional ordinary-source bound

\[
\sum_{q\ge1}\sum_w\frac{J_w^4}{r_w^5}
<\frac{512}{175}.
\tag{C8}
\]

It includes repeated visits on possible cycles, using a telescoping
correction product. This is a useful positive all-time estimate, but
it weights an endpoint by three additional inverse powers compared
with `P_q`. Concentration moving to larger endpoints can respect C8
while `P_q` grows quickly enough that the series in CN converges.

For a precise limitation of the aggregate estimates alone, consider
an illustrative positive array with one odd endpoint `r_q=2q^3-1` at time
`q` and second-denominator mass `epsilon*q^(4/rho)`. Its critical
negative series converges like `sum q^(-2)`, whereas its
fifth-denominator total is at most
`epsilon*sum q^(4/rho-9)<infinity`. Choosing `epsilon>0` small
meets any prescribed positive bound of the form C8, and its fixed-time
mass is also bounded by a constant times `r_q^2`, since `rho>2/3`.
This array is not
claimed to satisfy the actual congruence-word constraints. It shows
exactly why C8 and the coarse endpoint cutoff bounds alone do not
justify CN; those additional arithmetic constraints must supply the
missing step.

The earlier simple-prefix product sieve and the present critical
moment criterion therefore meet at the same fixed-source boundary:
orbit sparsity controls the affine correction, but does not establish
the required concentration estimate for the arithmetic representatives.
No extrapolation from finitely computed moment values is used here.

## Cycles and final scope

On a nontrivial positive cycle, the same ordinary states repeat. C5
is valid for its set of distinct values, but not for the time-indexed
sum. The product `I_q` accumulates a factor greater than one on each
lap, so the uniform bound used in C4 is unavailable. Thus CN or CQ,
even if proved, would exclude nonperiodic orbits only. A proof excluding
all nontrivial positive cycles would still be required for full Collatz.

This note adds a sharper source-qualified arithmetic closing target.
It proves neither CN nor CQ, and it does not settle that cycle
obligation.
