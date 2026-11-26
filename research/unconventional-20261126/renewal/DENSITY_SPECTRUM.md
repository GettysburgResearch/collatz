# Record density and the dimension seen by a stationary ordinary record flow

**Status — PROPOSED.** Let $\mathcal L$ be the countable alphabet
of genuine first-ladder words, with $N_m$ letters of odd length $m$.
For a sequence read backwards from a record, concatenate the
reversed words and write $n_k$ for its odd depth after $k$ complete
blocks. Its ternary coding is the critical series of [the gauge
theorem](GAUGE.md). For $0<\rho\le1$, let $E_\rho$ consist of
the ternary points admitting at least one such infinite coding
with $\limsup k/n_k\ge\rho$. Individual words have no length
cutoff. Codings of the same ternary point need not be unique.

Set $Z(s)=\sum_{m\ge1}N_m e^{-sm}$ for $s\ge H$, where
$H=\theta\log3$. The [first-maximum factorization](PRESSURE.md)
gives $q=Z(H)\in(0,1)$.

**Theorem M (density spectrum).** For $0<\rho\le1$,

$$
 \dim_H E_\rho
 =D(\rho):=\frac1{\log3}\inf_{s\ge H}\{s+\rho\log Z(s)\}
 \le\theta+\rho\log q/\log3<\theta.                                \tag{M1}
$$

For $0<\rho<1$ the same formula holds if one requires the actual
limit $k/n_k=\rho$. The minimizing $s=s_\rho>H$ is the unique
solution of $-Z'(s)/Z(s)=1/\rho$, and $D(1)=0$.
The recurrently parsed set with limit density zero has dimension
$\theta$. As $\rho\downarrow0$, writing $\overline\Phi$ for the
coefficient in (P6) of [the pressure proof](PRESSURE.md),

$$
 D(\rho)\log3
 =H+\rho\log q-\pi(\overline\Phi/q)^2\rho^2+o(\rho^2).              \tag{M2}
$$

**Theorem M.1 (fixed ordinary orbit).** Let a subsequential
odd-time-normalized record flow (F1) of [the stationary-flow
theorem](RECORD_FLOW.md) have mass $\delta>0$. Normalize its
ternary marginal to probability $\nu$. Then

$$
 \nu\!\left(\bigcup_{j\ge1}E_{1/j}\right)=1,\qquad
 \nu(E_\rho)\ge 1-\rho/\delta\quad(0<\rho<\delta).                 \tag{M3}
$$

In particular at least half the limiting record mass is on a set
of Hausdorff dimension at most $D(\delta/2)<\theta$. The countable
union in (M3) has zero Hausdorff measure for every finite
cube-root gauge $g_K$ of the [sharp theorem](SHARP_GAUGE.md).
The proposal concerns temporal occupancy. Rare individual record
subsequences are not controlled by this statement.

## Upper count at a complete boundary

For any $s\ge H$ and a fixed number $k$ of blocks, the sum of
$e^{-s n_k}$ over all their choices is exactly $Z(s)^k$.
Hence the number with ending depth precisely $n$ is at most
$e^{sn}Z(s)^k$. If $k\ge a n$ with $a>0$, sum over $k\le n$;
since $Z(s)\le q<1$ the resulting count is at most
$(n+1)\exp[n(s+a\log Z(s))]$. One ball of diameter $3^{-n}$
covers each coded prefix. To cover $E_\rho$ take all such depths
$n\ge M$, for any fixed $a<\rho$: every representing sequence has
infinitely many admissible complete endpoints. Sum the geometric
bound for dimensions greater than $(s+a\log Z(s))/\log3$, then
let $a\uparrow\rho$ and infimize over $s$. At $\rho=1$,
$Z(s)=e^{-s}(1+o(1))$ as $s\to\infty$ because $N_1=1$;
the upper bound is zero and the constant word realizes the set.

## Lower count through the ternary overlaps

For $s>H$ assign each individual block $w$ the probability
$e^{-s |w|}/Z(s)$ independently. The length has exponential
tails and mean $L(s)=-Z'(s)/Z(s)$. Its derivative is minus its
strictly positive variance because there are blocks of lengths 1
and 2. As $s\to\infty$ the mean tends to one. As $s\downarrow H$
it tends to infinity: (P3)–(P4) and the rotation lower count
in [the pressure proof](PRESSURE.md) give
$e^{-Hm}N_m\gg m^{-3/2}$ on a syndetic set of lengths. Thus
$s_\rho$ exists and uniquely minimizes (M1). Fix $s=s_\rho$.

The strong law gives $k/n_k\to\rho$. Exponential tails and
Borel–Cantelli give a constant $C$ for which, almost surely,
the first $n+1$ blocks all have length at most $C\log(n+2)$
for all sufficiently large $n$. For each $\varepsilon>0$ restrict
the product probability to a set $G$ of positive mass on which
both conclusions hold **uniformly** for all sufficiently large
indices, with $|k/n_k-\rho|\le\varepsilon$ there. This follows
by the countable union of sets defined by a common starting index.
Take the set inside the full-measure event with limiting density
exactly $\rho$.

A specified prefix of $n$ gaps compatible with $G$ forces whole
blocks through all but $O(\log n)$ letters, despite the unbounded
alphabet. Indeed, take $J=\lceil C\log(n+2)\rceil$. Every block
meeting that prefix has length at most $J$ on $G$, since at most
$n+1$ blocks are needed. When at least $J$ letters remain,
the largest nonempty backward prefix ratio $2^{S_i}/3^i$ on
the remaining segment is attained uniquely at the end of the
first complete block. This follows from the strict reversed
first-ladder inequalities and all later normalized prefixes being
below one. Remove the forced block and repeat. Stop when fewer
than $J$ letters remain. Write $l$ for the depth of determined
complete blocks and $k$ for their number. Then
$l=n-O(\log n)$, and $k/l=\rho+O(\varepsilon)$ for all sufficiently
large $n$ on $G$. The restricted prefix mass is at most the full
mass $e^{-s l}Z(s)^{-k}$ of these forced blocks. It is therefore
bounded by

$$
          \exp[-n(s+\rho\log Z(s)-O_s(\varepsilon)-o(1))].          \tag{M4}
$$

For this same restricted set, at depth $n$ the normalized real
inverse offset $C_w/3^n$ is at most $\exp(O(\log n))$. To see
this, the reversed affine offset from any complete block or one
of its prefixes of length at most $J$ is at most $J\,3^J$ by
the elementary carry formula and its total clock at most
$\lfloor\alpha J\rfloor$. All these pieces have real inverse
multiplier $\le1$, so their offsets add to at most $(n+1)J\,3^J$.
At fixed clock and ternary residue the carry is fixed modulo
$3^n$, and distinct words of that clock have distinct carries by
the valuation decoder in [the elementary gauge proof](GAUGE.md).
Only $O(n)$ clocks are possible. Consequently at most
$\exp(O(\log n))$ relevant words meet any depth-$n$ ternary
cell. Multiplying (M4) by this factor and normalizing the
restriction to $G$, the mass distribution principle gives
dimension at least $(s+\rho\log Z(s)-O_s(\varepsilon))/\log3$.
Let $\varepsilon$ decrease to zero. This proves (M1) even for
the exact-limit subset. The unbounded-block partial parsing is
the point at which merely quoting the independent block
probabilities would have been insufficient.

For density zero, use the measure in the elementary cube-root
lower proof [GAUGE.md](GAUGE.md). At every large depth $n$ its
deficit $d_n=\alpha n-S_n$ is between positive constant multiples
of $n^{1/3}$. Since these deficits tend to infinity, their smallest
nonempty value in any remaining tail is attained. Cut there and
continue: these are precisely complete reversed ladder blocks,
giving an infinite parsing. If $k/n_k\ge\eta>0$ infinitely, at
least $\eta n_k/2$ of the first $k$ blocks have length at most
$\lceil 2/\eta\rceil$. Each contributes at least the smallest
positive overshoot at these finitely many lengths to $d_{n_k}$.
This would give linear deficit along that subsequence. Thus every
such script has density zero, while its ternary image has full
dimension $\theta$ by the mass bound in that proof.

## The low-density expansion

For $a_m=e^{-Hm}N_m$, (P6) gives
$m^{3/2}a_m=\Phi(\{\alpha m\})+o(1)$ with bounded
Riemann-integrable periodic $\Phi$ of positive mean $\overline\Phi$.
Irrational rotation therefore gives ordinary Cesàro mean
$\overline\Phi$ for the left side. As $t\downarrow0$,

$$
  Z(H+t)=q-2\sqrt\pi\,\overline\Phi\sqrt t+o(\sqrt t),\qquad
 -Z'(H+t)=\sqrt\pi\,\overline\Phi/\sqrt t+o(1/\sqrt t).
$$

For the first formula apply the Cesàro mean in Riemann sums
against $(1-e^{-x})x^{-3/2}$ on $x=tm$; the second uses
$e^{-x}x^{-1/2}$. Both test functions are integrable on
$(0,\infty)$, with integrals $2\sqrt\pi$ and $\sqrt\pi$
respectively. On a compact interval bounded away from zero
one may approximate by step functions and use the mean. The
discarded tails are uniformly bounded by the corresponding
integrals times a constant since $m^{3/2}a_m$ is bounded.
With $c=\sqrt\pi\,\overline\Phi/q$ the optimizing equation gives
$\sqrt{s_\rho-H}=c\rho+o(\rho)$. Substitution in (M1) gives (M2).

## Finite mean on one ordinary record flow

Normalize the limiting edge measure in (F1) by its mass $\delta$.
Fatou's lemma on the finite length truncations gives mean odd
block length at most $1/\delta$, since the total completed lengths
at horizon $n$ are at most $n$. Equal source and target marginals
give a stationary two-sided process of labelled edges with this
same one-edge law. Explicitly, disintegrate the edge measure over
its source coordinate, sample successive adjacent edges with that
transition rule and use stationarity to extend to two-sided
times. These spaces are compact metrizable at the vertices and
countable discrete at the labels, so the ordinary regular
conditional distribution and extension theorems apply. This
auxiliary process represents the existing marginal; it makes no
claim that the true ordinary blocks are independent or Markov.

Along this backward process, the ergodic theorem gives
$n_k/k\to L=E(m\mid\mathcal I)$ almost surely, with
$1\le L<\infty$ and $E L\le1/\delta$. The ternary point at
time zero is the infinite backward code: composing the last
$k$ edge maps contracts any possible starting ternary difference
by exactly $3^{-n_k}$. Therefore its sample belongs to
$E_\rho$ whenever $L\le1/\rho$. Markov's inequality gives
$\Pr(L>1/\rho)\le\rho/\delta$, proving (M3), and finiteness of
$L$ gives the countable-union assertion. The sets can be used
in the universal completion of the measures: the stated coding
conditions are Borel in the countable sequence space and the
continuous images are analytic. Finally each $E_{1/j}$ has
dimension below $\theta$ and hence zero measure for every
$g_K(r)=r^{\theta+o(1)}$. Countable subadditivity gives the last
claim without any assumption about the topology of the full
ordinary cluster set.

**Related work.** Positive-frequency dimension spectra for infinite
iterated function systems are classical. Ternary coding can have
overlaps here; the measure argument explicitly bounds the whole
carry and the ambiguities in reading incomplete blocks. Related
Collatz affine laws have exact-dimensional results for independent
geometric gaps under other conditions. [Infinite-system spectra](https://arxiv.org/abs/0902.2473)
· [Ternary Syracuse laws, section 5](https://rstation.ai/problems/collatz/papers/9)
· [The first-descent inverse-speed strata](https://rstation.ai/problems/collatz/papers/184)
