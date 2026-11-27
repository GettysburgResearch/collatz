# Exact Hausdorff transition constant of the ternary critical trace

**Status — PROPOSED written proof.** With the critical trace
$\mathcal R$, entropy $H$ and dimension $\theta$ of [the elementary
gauge proof](GAUGE.md), let $\alpha=\log_2 3$, $u=1-1/\alpha$,
$h=-\log u$, $\sigma^2=\alpha(\alpha-1)$ and
$\kappa=\pi^2\sigma^2/2$. Logs without subscript are natural. Define

$$
 A_*=\min_{f>0}\left(hf+\frac{3\kappa}{f^2}\right)
     =\left(\frac{81\pi^2\sigma^2 h^2}{8}\right)^{1/3},
 \qquad K_*=\frac{A_*}{(\log3)^{1/3}}.                             \tag{S1}
$$

**Theorem S.** For $g_K(r)=r^\theta\exp[K(\log(1/r))^{1/3}]$ near zero,

$$
 \mathcal H^{g_K}(\mathcal R)=0\quad(K<K_*),\qquad
 \mathcal H^{g_K}(\mathcal R)=\infty\quad(K>K_*).                   \tag{S2}
$$

The minimizing width is $f_*=(6\kappa/h)^{1/3}$, approximately
$3.0198910$. The depth constant $A_*$ is approximately $4.5151974$,
and the Hausdorff-gauge constant $K_*$ approximately $4.3758449$.
The argument leaves the measure at equality undetermined. This
is an exact transition for the universal ternary trace. Its application
to one positive ordinary ray gives the upper bound for a subset.

## Fixed-width estimate from the Brownian interval

Use independent geometric gaps with $\Pr(e=k)=(1-u)u^{k-1}$.
The centered walk adds $X_i=\alpha-e_i$, with variance $\sigma^2$.
A length-$n$ word of terminal deficit $d_n$ has exact probability

$$
                   \exp[-Hn+h d_n].                                \tag{S3}
$$

Fix $\varepsilon>0$. Choose $T$ sufficiently large and thereafter
fixed. Over $L=\lfloor T W^2\rfloor$ steps, as $W\to\infty$, the
following two estimates hold for all sufficiently large $W$.

* From any $x\in[0,(1+o(1))W]$, the probability of staying in
  $[0,(1+o(1))W]$ throughout is at most $\exp[-(\kappa-\varepsilon)T]$.
  Here the deterministic relative errors must tend to zero.
* From any $W/3\le x\le 2W/3$, the probability of staying strictly
  inside $(0,W)$ and ending in $(.45W,.55W)$ is at least
  $\exp[-(\kappa+\varepsilon)T]$.

For the proof, the interpolated walk divided by $W$ on time interval
$[0,T]$ converges in distribution to Brownian motion of variance rate
$\sigma^2$ by Donsker's theorem. Uniformity follows by taking any
putative bad sequence and a subsequence on which $x/W$ converges.
For the upper bound use the closed event that the limiting continuous
path stays in $[0,1]$. Starting at an endpoint its Brownian probability
is zero, and interior starts which reach a boundary before time $T$
cross it almost surely. Hitting exactly at terminal time has
probability zero. The same closed-set upper bound holds for expanding
widths $1+o(1)$ by first enlarging the limiting interval by a fixed
$\delta$ and then decreasing $\delta$ to zero. For the lower bound
the event of remaining inside $(0,1)$ for all of $[0,T]$ and ending
in $(.45,.55)$ is open in the uniform topology. Path interpolation
preserves both strip conditions between consecutive discrete times.

The killed Brownian transition density from $x$ to $y$ in $(0,1)$ is

$$
       2\sum_{k\ge1}e^{-\kappa k^2 T}\sin(k\pi x)\sin(k\pi y).
$$

It follows either by the sine expansion of the Dirichlet heat equation
or the standard Brownian interval formula. Its integral over $(0,1)$
is uniformly at most $C e^{-\kappa T}$ for $T\ge1$. Integrated over
$(.45,.55)$ it is at least $c e^{-\kappa T}$ uniformly on
$x\in[1/3,2/3]$ for $T$ large, since the first sine is positive
there and all remaining terms contribute $O(e^{-4\kappa T})$.
Taking $T$ large enough to leave strict margins on both comparisons
gives the two walk estimates after passage to the limit.

## The price of an expanding strip

Fix $f>0$, a large integer $n_0$, and define successive stages by

$$
 W_j=f n_j^{1/3},\qquad
 n_{j+1}=n_j+\lfloor T W_j^2\rfloor.
$$

The stages grow indefinitely and $n_{j+1}/n_j\to1$. By the mean
value theorem,
$n_{j+1}^{1/3}-n_j^{1/3}\to Tf^2/3$. Thus the number of complete
stages up to depth $n$, as well as the number including a last partial
one, equals $(3/(Tf^2)+o(1))n^{1/3}$. The estimates below hold
after any fixed initial time.

An eventually confined path with $0<d_i\le f i^{1/3}$ must stay
within $[0,W_{j+1}]$ over every complete stage. The first
fixed-width estimate applies with width ratio $W_{j+1}/W_j\to1$.
Independence of successive increments and conditioning on the
starting position show that, for fixed $N$ and sufficiently large $n$,

$$
 \Pr(0<d_i\le f i^{1/3}\text{ for }N\le i\le n)
 \le \exp[-(3(\kappa-\varepsilon)/f^2+o(1))n^{1/3}].               \tag{S4}
$$

Start the stages beyond $N$ to ignore any finite initial positions.
In (S4) the first starting position is unrestricted before imposing
the displayed band, so conditioning on it causes no loss.

## Upper bound by the limsup of the actual deficit ratio

Write $A=K(\log3)^{1/3}$, so $g_K(3^{-n})=\exp[-Hn+A n^{1/3}]$.
For $0\le a<f$, consider scripts with $d_i\le f i^{1/3}$ eventually
and $d_n\ge a n^{1/3}$ infinitely often. Fix the initial confinement
time $N$. By (S3), each eligible length-$n$ endpoint word has
probability at least $\exp[-Hn+ha n^{1/3}]$. Division of (S4) by
this lower bound counts all such words. Their image cylinders at all
$n\ge M$ cover the specified limsup class. The $g_K$ cost of this
cover tends to zero as $M\to\infty$ whenever

$$
                         A<ha+3\kappa/f^2,                           \tag{S5}
$$

by taking $\varepsilon$ small and summing a bound $\exp(-c n^{1/3})$.
Countably many $N$ suffice. If $L=\limsup d_n/n^{1/3}\in(0,\infty)$
and $A<A_*$, choose rational $0\le a<L<f$ close to $L$ so that
(S5) holds. These countably many pairs cover all finite positive
$L$. For $L=0$ choose $a=0$ and a sufficiently small positive $f$.
For $L=\infty$, (S3) alone bounds the word count at the infinitely
many endpoints $d_n\ge a n^{1/3}$ by $\exp[Hn-ha n^{1/3}]$, and
one may take any $a>A/h$. This proves the zero half of (S2).

## Lower bound after ternary projection

Fix $f>0$ and use the stages above with $T$ large. Choose $n_0$ large
enough that a fixed critical prefix has $d_{n_0}\in[W_0/3,2W_0/3]$.
For example choose a clock $\lfloor\alpha n_0-W_0/2\rfloor\ge n_0$,
take any composition into $n_0$ positive gaps, and rotate just after
the largest nonterminal partial sum $S_j-\alpha j$. All subsequent
partial sums are strictly negative, including after wraparound,
because the full sum is negative and all proper partial sums differ.
All deficits of the fixed initial word are bounded by a constant
depending on that word.

At each stage condition fresh increments to stay inside $(0,W_j)$
and end in $(.45W_j,.55W_j)$. For all large $j$ such endpoints lie
in $[W_{j+1}/3,2W_{j+1}/3]$. Increase $n_0$ to arrange this from
the first stage. By the second fixed-width estimate the normalizing
probability is at least $\exp[-(\kappa+\varepsilon)T]$. This gives
a probability $\mu$ on infinite critical scripts. For any prescribed
depth-$n$ word, each intersected stage costs at most that reciprocal
normalizer, including its last partial stage since completion probability
is at most one. Hence uniformly over positive-mass words

$$
 \mu([w])\le
 \exp[-Hn+h d_n+
        (3(\kappa+\varepsilon)/f^2+o(1))n^{1/3}].                  \tag{S6}
$$

The fixed prefix only changes a constant factor.
For every such word $\max_{i\le n} d_i\le f n^{1/3}+O(1)$.

At fixed depth $n$ and clock $s$, $d_n=\alpha n-s$ is fixed.
The integer carry $C_w$ determines the word when $n,s$ are given,
and the ternary residue $y$ requires $C_w\equiv2^s y\bmod 3^n$.
The carry identity in [the elementary proof](GAUGE.md) gives

$$
 0<C_w/3^n
 =\frac13\sum_{i=1}^n 2^{d_i-d_n}
 \le (n/3)2^{f n^{1/3}-d_n+O(1)}.
$$

At this clock and residue there are at most one plus the last
displayed bound many words. The exponent bound remains valid for
the added one after modifying its constant because
$d_n\le f n^{1/3}+O(1)$. Multiply by (S6). Here
$h=-\log(1-1/\alpha)>\log2$ since $\alpha<2$, so

$$
  h d_n+(\log2)(f n^{1/3}-d_n)
     \le h f n^{1/3}+O(1).
$$

There are only $O(n)$ clocks. For the pushforward probability $\nu$
we therefore have, uniformly in each ternary depth-$n$ ball $B$,

$$
 \nu(B)\le
 \exp[-Hn+(hf+3(\kappa+\varepsilon)/f^2+o(1))n^{1/3}].             \tag{S7}
$$

Take $f=f_*$, select an $A'$ strictly between $A_*$ and $A$, and
choose $\varepsilon>0$ with the coefficient in (S7) strictly below
$A'$. The mass distribution principle gives positive Hausdorff
measure for the depth coefficient $A'$. Since the gauge ratio for
$A$ over $A'$ tends to infinity, the measure for $A$ is infinite.
This proves (S2).

## Sources and comparison

The probabilistic inputs are the ordinary functional central limit
theorem and the heat kernel for absorption at the ends of one
interval. The growing-strip calculation above is a blocking proof
of the relevant special case of Mogul'skii's small-deviation method.
[Functional central limit theorem, Mörters and Peres, Theorem 5.22
in their book draft](https://www.mi.uni-koeln.de/~moerters/book/book.pdf)
· [Brownian interval formula, Lalley](https://galton.uchicago.edu/~lalley/Courses/383/BrownianMotion.pdf)
· [Mogul'skii, *Small Deviations in a Space of Trajectories*](https://doi.org/10.1137/1119081)

The optimized constant has the same expression as the critical
absorption-barrier constant in Jaffuel's branching-random-walk theorem
when the variance is scaled by $h^2$. This resemblance follows from
the common interval eigenvalue and the minimization in (S1).
Here the claim concerns Hausdorff measure of a fixed ternary image,
including its arithmetic overlaps. [Jaffuel, 2012](https://archive.numdam.org/articles/10.1214/11-AIHP453/)
