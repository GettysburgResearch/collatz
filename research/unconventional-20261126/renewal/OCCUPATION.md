# A critical Mellin budget for unrestricted low visits

**Status — PROPOSED.** Use shortcut $T$, $\alpha=\log_2 3$,
$\beta=1/\alpha$, and $\theta=H_2(\beta)$ as in
[the height theorem](HEIGHT.md). For each finite simple ordinary
trajectory $\mathcal P$ let $V_{\mathcal P}(X)$ count its vertices at
most $X$. The trajectory can rise arbitrarily far above $X$ between
the visits. Cycles are allowed for one primitive lap only.

**Theorem O.** Uniformly for $X\ge2$ and all such paths,

$$
  V_{\mathcal P}(X)\ \ll\
  X^\theta\,\frac{(\log\log(3X))^2}{(\log(2X))^{3/2}}.            \tag{O1}
$$

In particular the critical Mellin sum itself converges on each
infinite nonrepeating trajectory, with a uniform tail estimate

$$
 \sum_{\substack{y\in\mathcal P\\ y\ge M}} y^{-\theta}
   \ \ll\ \frac{(\log\log(3M))^2}{\sqrt{\log(2M)}}
       \qquad(M\ge2).                                               \tag{O2}
$$

Both conclusions concern the states of a single path. They do not
count a branching predecessor basin. This proof does not insert a
bounded-height estimate for all the low visits of an uncapped path.
Its new ingredient is the one-sided barrier for actual windows above a
lower floor, with an exponentially weighted terminal bin. The
earlier square-root logarithmic orbit-sparsity estimate alone does
not make the critical integral finite.

**Prior stronger ordinary estimate.** Weaver's Paper 28/v3,
Theorem 1, gives an effective bound without the two $\log\log$
factors in (O1) in the larger translated-interval setting. Theorem A
and section 8.1, (P2)--(P3), state a fixed ineffective ordinary power
improvement $\theta-\gamma$ and a tail $O(M^{-\gamma})$ at
$t=\theta$. Thus (O1)--(O2) give an independent elementary
derivation of weaker ordinary statements. The critical Mellin
convergence itself has already been stated there. We use this
self-contained finite-window argument for the critical-trace
calculation, and its signed fixed-denominator version for rational
shadows. The external power improvement is not an input into either
proof.
[Primary source, Theorems 1 and A, section 8.1](https://rstation.ai/problems/collatz/papers/28)

## A finite one-sided counting estimate

Let $\xi=\alpha{\bf1}_{\rm odd}-1$ under independent Bernoulli
$\beta$ bits, let $Z_j=\xi_1+\cdots+\xi_j$. These increments have
mean zero, variance $\sigma^2=\alpha-1>0$ and magnitude at most one.
For either choice of sign, every $h\ge1$ and $d\ge0$ satisfy

$$
 \Pr\bigl(\min_{0\le j\le h}(\pm Z_j)\ge-d\bigr)
           \ll (d+1)/\sqrt h.                                      \tag{O3}
$$

For a direct proof stop the signed walk on its first exit below $-d$
or at or above $b=\sqrt h$. At the stopping time $\tau\wedge h$ the
walk has mean zero and is at least $-d-1$. Thus the probability of
an upper exit by $h$ is at most $(d+1)/(b+d+1)$. The function
$f(z)=(z+d+1)(b+1-z)$ is nonnegative at every position before and
at the stopped time, because an overshoot is at most one. At each
nonstopped step its conditional expected decrease is $\sigma^2$.
Summing up to $h$ gives $\sigma^2 E(\tau\wedge h)\le(d+1)(b+1)$.
Therefore $\Pr(\tau>h)\le(d+1)(b+1)/(\sigma^2 h)$. A path surviving
the lower barrier up to $h$ either has exited above, or has not
exited, proving (O3).

For any fixed $b_0>0$, $a>0$ and $D\ge b_0+1$, we have

$$
 E\!\left[e^{-aZ_t}\,{\bf1}_{\{\min_{j\le t}Z_j\ge-D,\
                                  Z_t\ge-b_0\}}\right]
     \ll_{a,b_0} (D+1)^2/t^{3/2}\quad(t\ge3).                     \tag{O4}
$$

Partition $Z_t$ into unit intervals $[k,k+1)$ with
$k\ge-\lceil b_0\rceil$. Use the first and last $\lfloor t/3\rfloor$
increments and the independent middle block. For a path in the
indicated event the first block stays above $-D$. Reading the last
increments backwards from the terminal, all their partial sums
$Z_t-Z_{t-j}$ are at most $D+k+1$. By (O3) these necessary events
have independent probabilities bounded by $C(D+1)/\sqrt t$ and
$C(D+k+2)/\sqrt t$. Given the first and last blocks, the middle
block must finish in a prescribed unit interval. Its support has
spacing $\alpha>1$ and its maximum binomial atom is $O(t^{-1/2})$
by Stirling's formula. Multiplying these three bounds and summing
$e^{-ak}$ gives (O4), including a harmless constant for bounded $t$.
This is a counting estimate for an auxiliary walk; the orbit is
never assigned these probabilities.

## Applying the estimate to fixed ordinary vertices

Take $t=\lfloor\log_2 X\rfloor$ and discard at most $t$ terminal
vertices lacking a $t$-step window. In a low-odd-count window,
$p\le\lfloor\beta t\rfloor-2$, the endpoint is at most $X/2$
for sufficiently large $X$, by the elementary full-carry estimate in
[the proof of (H3)](HEIGHT.md). Advancing by these same $t$ steps is
injective on the supplied finite simple path. Count such starts by
$V_{\mathcal P}(X/2)$.

For the remaining windows define $Y=X/t^4$. At most
$(t+1)V_{\mathcal P}(Y)$ of all windows pass below $Y$, irrespective
of their peaks, because each low vertex belongs to at most $t+1$
windows. By the baseline (H3) this contributes
$O(X^\theta t^{1/2-4\theta})$, which is $O(X^\theta/t^{3/2})$
since $\theta>1/2$. The last inequality follows, for example, from
$1/2<\beta<2/3$ and $H_2(2/3)>1/2$.

On a remaining window all states are at least $Y$ and the initial
one is at most $X$. At every prefix,

$$
 Z_j=\alpha p_j-j
 =\log_2(y_{i+j}/y_i)
    -\sum_{\substack{0\le d<j\\ y_{i+d}\ {\rm odd}}}
                 \log_2(1+1/(3y_{i+d}))
 \ge -4\log_2 t-t/(3Y\log2).
$$

In particular $Z_j\ge-D$ with $D=4\log_2 t+1$ for all sufficiently
large $X$. This uses a lower bound on the intermediate states only.
The retained odd count gives $Z_t\ge-2\alpha$.

The reciprocal of the auxiliary probability of a specific word is
$2^{\theta t}e^{-aZ_t}$ where
$a=\log(\beta/(1-\beta))/\alpha>0$. Thus (O4), with $b_0=2\alpha$,
counts the eligible words by
$C\,2^{\theta t}(1+\log t)^2/t^{3/2}$. Each has at most two positive
sources $\le X$ since $2^t\le X<2^{t+1}$ and the exact native parity
word fixes its residue. We obtain the recursion

$$
 V_{\mathcal P}(X)\le V_{\mathcal P}(X/2)+
 C X^\theta(\log\log(3X))^2/(\log(2X))^{3/2}+O(\log X).
$$

A dyadic summation proves (O1), as for (H3), with the same uniformity.
Finally, integrating $y^{-\theta}=
\theta\int_y^\infty t^{-\theta-1}\,dt$ for all $y\ge M$ reduces
(O2) to the integral of
$(\log\log(3t))^2/[t(\log(2t))^{3/2}]$. With $v=\log(2t)$ this
is $O((1+\log v)^2/\sqrt v)$ at the lower limit. Exhausting an
infinite simple path by finite prefixes proves the infinite statement.
Indeed the same estimate makes the sum with an additional factor
$(\log(2y))^\gamma$ finite whenever $\gamma<1/2$.
