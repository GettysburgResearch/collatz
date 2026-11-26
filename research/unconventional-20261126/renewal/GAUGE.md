# The cube-root gauge of the full ternary critical trace

**Status — PROPOSED.** Let $\alpha=\log_2 3$,
$H=\alpha\log\alpha-(\alpha-1)\log(\alpha-1)$ and
$\theta=H/\log3$. A backwards gap word has positive integer letters
$e_j$, clocks $S_j=\sum_{i\le j}e_i$ and deficits $d_j=\alpha j-S_j$.
It is critical if every $d_j>0$. An infinite such word gives the
ternary point

$$
 z=\sum_{j\ge1}3^{j-1}2^{-S_j}\in\mathbb Z_3.
$$

Write $\mathcal R$ for the set of all these points. The depth-$n$
word fixes a residue modulo $3^n$. All statements of this file concern
this universal symbolic image. Every actual critical-record cluster
lies inside it, but a positive ordinary orbit need not produce all its
points.

**Theorem T.** For small $r>0$ put
$g_K(r)=r^\theta\exp[K(\log(1/r))^{1/3}]$. Extend it monotonically
away from zero as a Hausdorff gauge. There are finite constants
$0<K_0<K_1$ such that

$$
 \mathcal H^{g_{K_0}}(\mathcal R)=0,\qquad
 \mathcal H^{g_{K_1}}(\mathcal R)=\infty .                         \tag{T1}
$$

Consequently the exponent $1/3$ in the logarithmic correction is
sharp: for every fixed $0<\xi<1/3$ the gauge
$r^\theta\exp[(\log(1/r))^\xi]$ gives zero measure, and for
$1/3<\xi<1$ it gives infinite measure. No exact critical constant
or measure at that constant is asserted.

The number $W_n$ of critical *words* of length $n$ obeys

$$
                 W_n\asymp e^{Hn}/(n+1)^{3/2}.                    \tag{T2}
$$

This counts the complete scripts, not necessarily distinct ternary
residues. The mass bound below gives at least
$\exp[Hn-Cn^{1/3}]$ distinct depth-$n$ cells in the ternary image.
The effective difference between (T1) and (T2) is that Hausdorff
covers can stop different paths at different depths.

## Exact order of the word count

Put $\beta=1/\alpha$, and use the centered Bernoulli shortcut walk
$Z_j=\alpha P_j-j$ of [the one-sided estimate](OCCUPATION.md),
where $P_j$ counts its ones. A critical $n$-gap word of clock $s$
encodes the binary string of length $s$ with ones exactly at
$S_1,\ldots,S_n=s$. At a marked position its $Z$ is positive.
Until the next mark $S_{i+1}<\alpha(i+1)$ it stays greater than
$-\alpha$, including the initial zeros if any. Its terminal position
is $t=\alpha n-s\ge0$. Here $n\le s<\alpha n$.

The first/middle/last-third argument proving (O4), retaining a
specified unit terminal bin, bounds the probability of the eligible
strings by $C(1+t)s^{-3/2}$. They all have identical probability
$2^{-\theta s}\exp(a t)$, where
$a=\log(\beta/(1-\beta))/\alpha>0$. Thus their number is at most
$C(1+t)n^{-3/2}\exp[Hn-(\theta\log2+a)t]$. As $s$ varies,
the values of $t$ are spaced by one; summing this exponential
bound gives the upper half of (T2). The use of the Bernoulli
clock avoids any bounded-increment assumption on the gap letters.
The same tilted ballot method for native parity words is present
in Lyapunov Weaver's Paper 28/v3, Proposition 4 and its killed kernel.
[Primary source](https://rstation.ai/problems/collatz/papers/28)

For a lower bound use $s=\lfloor\alpha n\rfloor$. Every cyclic class
among its $\binom{s-1}{n-1}$ positive compositions has a critical
rotation: start after the maximum of $S_j-\alpha j$ over
$0\le j<n$, and use the strictly negative one-lap total after
wraparound. No two partial sums tie. A class has at most $n$
rotations. Stirling's formula, including the bounded displacement
$s-\alpha n$, gives
$\binom{s-1}{n-1}\asymp e^{Hn}/\sqrt n$, proving (T2). This lower
rotation argument is already in PR201's finite-alphabet dimension proof.

## Small gauges — use two different covers

For this part work with independent geometric gaps
$\Pr(e=k)=p u^{k-1}$, $p=1/\alpha$, $u=1-p$. Their mean is
$\alpha$, and their centered finite positive variance is
$\sigma^2=\alpha(\alpha-1)$. On any fixed word the probability is

$$
               p^n u^{S_n-n}=e^{-Hn}u^{-d_n}.                     \tag{T3}
$$

First cover the scripts for which $d_n>n^{1/3}$ infinitely often.
At such a depth there are at most $e^{Hn}u^{n^{1/3}}$ words,
since their individual probabilities sum to at most one. The sum of
their $g_K(3^{-n})$ over all $n\ge N$ tends to zero for sufficiently
small positive $K$, since the remaining summand is bounded by
$\exp(-c n^{1/3})$. The included images exhaust this first class.

For the other scripts there is an $N_0$ after which
$0<d_i\le i^{1/3}$. Fix $N_0$ and use one depth $n\ge2N_0+2$.
On the last half of any eligible word, every subblock has centered
gap sum of absolute value at most $n^{1/3}$. Choose
$k=\lceil 2 n^{2/3}/\sigma^2\rceil$. For $Z_k=\sum(\alpha-e_i)$
we have $EZ_k^2=k\sigma^2$ and
$EZ_k^4=kE(\alpha-e_1)^4+3k(k-1)\sigma^4\le C(k\sigma^2)^2$.
Cauchy--Schwarz applied to the upper part of $Z_k^2$ yields
$\Pr(|Z_k|>n^{1/3})\ge c_0>0$. Each disjoint block of $k$ positions
in that half must avoid this event, so these words have total
probability at most $\exp(-c_1 n^{1/3})$ for all large $n$.
Every word has probability at least $e^{-Hn}$ by (T3), because
$d_n>0$. The level cover has $g_K$ cost tending to zero for
sufficiently small $K>0$. Countably many choices of $N_0$ cover
the second class. This proves the first assertion in (T1).

## Large gauges — a measure with expanding permitted deficits

We construct a nonstationary measure on infinite legitimate gap
scripts. At stage $k$ use $L_k=\lfloor k^2/1000\rfloor$ fresh tilted
geometric gaps. If the current deficit $x$ is in $[k,2k]$, condition on
the event

$$
 d_{\rm end}\in[k+1,2k+2],\qquad
            k/2\le d_{\rm within\ stage}\le5k/2.                  \tag{T4}
$$

For every sufficiently large $k$ the conditional normalizer is at
least one fixed $\eta>0$, uniformly in $x$. Indeed if $x\le3k/2$,
require the endpoint increment to lie in
$[\sigma\sqrt{L_k}/2,\sigma\sqrt{L_k}]$; if $x>3k/2$, use its
negative. For all large $k$ this places $x$ plus that increment in
the target interval. Each test has probability at least $1/10$ by
the classical central limit theorem (the standard normal mass from
$1/2$ to $1$ exceeds $1/10$). Kolmogorov's maximal inequality
bounds the probability that any centered partial sum in the stage
has absolute value exceeding $k/2$ by
$4\sigma^2 L_k/k^2\le4\sigma^2/1000<1/100$. Here
$3/2<\alpha<8/5$ gives $\sigma^2<1$. On the complementary event
the path stays in the indicated band. One may take $\eta=9/100$.

Begin at a sufficiently large stage $k_0$ by a deterministic string
of ones of length $\lceil k_0/(\alpha-1)\rceil$. It stays
strictly critical and ends in $[k_0,2k_0]$. Concatenating the
conditioned laws in (T4) then defines a probability on infinite
critical scripts. The number of completed stages by depth $n$ is
$O(n^{1/3})$, because $\sum_{i\le k}L_i$ grows cubically. At every
prefix $d_j\le C(1+j^{1/3})$, including the fixed initial string.
For a prescribed $n$-word, conditioning costs at most $\eta^{-1}$
per intersected stage, including the last partial one. Its prefix
probability under the constructed law is therefore at most

$$
                 \exp[-Hn+C(1+n^{1/3})]                           \tag{T5}
$$

by (T3) and the deficit bound. The fixed initial prefix changes
only the absolute multiplicative constant.

## Ternary multiplicity of the measure

Let $A_j=2^{S_j}/3^j=2^{-d_j}$ and
$B_n=\sum_{j=1}^n3^{j-1}2^{-S_j}$. For a fixed depth $n$, clock
$s=S_n$, and ternary cell $y+3^n\mathbb Z_3$, possible integer
carries $C_w=2^s B_n$ satisfy a single congruence
$C_w\equiv2^s y\bmod3^n$. In real coordinates,

$$
             0<C_w/3^n=(A_n/3)\sum_{j=1}^n A_j^{-1}
                         \le n\,2^{C(1+n^{1/3})}.                 \tag{T6}
$$

At fixed $n,s$ the carry specifies the whole finite word. If
$n\ge2$, subtract the last term $3^{n-1}$ from $C_w$; the result
has valuation exactly $e_n$ at 2. Divide out $2^{e_n}$ and repeat
on the preceding carry. The first remaining gap is fixed by $s$.
Thus at most $1+n\,2^{C(1+n^{1/3})}$ words of this clock can hit
the same cell. There are at most $\lfloor\alpha n\rfloor+1$ possible
clocks. Multiplying this bound by (T5), the pushforward probability
$\nu$ satisfies, uniformly over ternary cells,

$$
       \nu(y+3^n\mathbb Z_3)\le \exp[-Hn+C'(1+n^{1/3})].          \tag{T7}
$$

No open set condition or injectivity of the ternary coding appears
in the argument. By the mass distribution principle (T7) implies
positive Hausdorff measure for $g_K$ with a sufficiently large
finite $K$. Arbitrary sets in a ternary ultrametric of positive
diameter lie in a ball of that diameter; singleton sets have zero
mass by (T7). Increasing $K$ once makes the gauge ratio tend to
infinity, giving the infinite-measure assertion in (T1). This
also proves the stated lower count on occupied cells.

**Literature and scope.** A cube-root correction in constrained
centered walks also occurs in different, random branching models.
Fang and Zeitouni studied consistent minimal displacement, and
Jaffuel studied a critical moving barrier for branching random
walk. The fixed ternary coordinates, congruence overlap and
Hausdorff gauges above are derived directly. Those branching
theorems are not hypotheses here. [Fang and Zeitouni](https://www.wisdom.weizmann.ac.il/~zeitouni/pdf/FBRWsub.pdf)
· [Jaffuel](https://archive.numdam.org/articles/10.1214/11-AIHP453/)
