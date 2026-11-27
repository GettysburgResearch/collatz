# A harmonic cost for repeated, possibly very long record words

**Status — PROPOSED actual-source obstruction.** This applies to one
positive escaping ordinary orbit. A *run* here means a maximal
consecutive string of equal complete chronological first-ladder
words. Its odd length $m$ refers to one copy, and its duration $R$
counts record blocks. The order of different runs can be arbitrary.

**Theorem V.** Suppose each sufficiently large odd length $m$ occurs
in at most nine such runs, and the small lengths together occur in
only finitely many runs. Then the run starts have positive lower
logarithmic density in the record index and
$\limsup_l k_l/l^2>0$. If the record lengths are eventually
nondecreasing under the same nine-run condition, the stronger
$k_l\gg l^2$ holds at every sufficiently large $l$.

Consequently no such orbit can also have $B_l=o(S_l)$ for any of
the fixed periodic libraries and fixed per-record exceptional
budgets of [Theorem T](RECORD_TEMPLATE_COST.md). In the unordered
case $\limsup B_l/S_l\ge\log_3 2$ for every such parse. In the
nondecreasing case $\liminf B_l/S_l\ge\log_3 2$.

## Replaying an exact word from the same positive integer

For a run beginning at record index $t$, its word has native clock
$s=\lfloor\alpha m\rfloor$, where $\alpha=\log_2 3$.
Write $B=3^m-2^s>0$, and $C$ for its positive integer carry.
The word fixes $z=-C/B$, and $C<(9/2)^m$ by [the carry bound](BRIDGE.md).
The affine identity iterated through the $R$ genuine repetitions gives
$$
  2^{Rs}(B q_{t+R}+C)=3^{Rm}(B q_t+C).
$$
In particular $2^{Rs}\mid B q_t+C$, which is positive.
This remains valid for any truncated final run. On the supplied
ray $q_t\ll_{q_0}(3/2)^t$ by simple-path distortion and the
maximum interrecord overshoot $3/2$. Thus for any
$c>1-\log_3 2$ and all sufficiently large $m$,
$$
                   R\le c\,t/m+C_0.                               \tag{V1}
$$
Indeed $\log_2(Bq_t+C)\le(\alpha-1)t+m\log_2(9/2)+O_{q_0}(1)$
and $s\ge\alpha m-1$. The additive constant is uniform after the
fixed start is chosen. No assertion about the structure *inside*
the repeated word is needed.

An infinite final run would contradict the same divisibility for
its one fixed starting value. Under the hypotheses we may discard
all runs of any bounded collection of lengths and start counting at
some positive index.

## The overshoot-weighted harmonic budget

Write $\delta=\alpha-1$ and $\rho_m=\{\alpha m\}$. Any admissible
first-ladder length has $0<\rho_m\le\delta$: its final rise is
at most the one-step rise $\delta$. After $t$ records the exact
binary log coefficient is the sum of the $t$ overshoots. Put
$$
 V_t=C_{q_0}+\log_2 M_{k_t}+\epsilon t ,
$$
where $\epsilon>0$ is fixed and small, and choose $C_{q_0}\ge1$
so that $\log_2(q_t+1)\le V_t$ always, by finite distortion.
Then $\epsilon t\le V_t\le C_{q_0}+(\delta+\epsilon)t$.
For a run of length $m$, the exact replay bound above gives
$R\le V_t/s_m+C_0$ uniformly, $s_m=\lfloor\alpha m\rfloor$.
The logarithmic growth through that run therefore satisfies
$$
 \log(V_{t+R}/V_t)
 \le R(\rho_m+\epsilon)/V_t
 \le(\rho_m+\epsilon)/s_m+C_\epsilon/t.                           \tag{V2}
$$

Let $P\le9$ be the bound on runs per length and $t_j,m_j$ their
successive starts and odd lengths, including a final partial run.
For lengths $m_j>l$ the sum of the first terms on the right of
(V2) through record $l$ is $O(1)$ because there are at most $l$
terms, each $O(1/l)$. The remaining first terms total at most
$$
 P\!\sum_{\substack{m\le l\\\rho_m\le\delta}}
       \frac{\rho_m+\epsilon}{s_m}
 =\left(\frac{P}{\alpha}(\delta^2/2+\epsilon\delta)+o(1)\right)
                                                         \log l .
$$
Indeed $1/s_m=1/(\alpha m)+O(m^{-2})$ and irrational rotation
has ordinary mean $\int_0^\delta (y+\epsilon)\,dy$ for the
bounded integrand in this sum. Partial summation gives its
logarithmic mean. Since $9\delta^2/(2\alpha)<1$, choose $\epsilon$
so that the coefficient $\gamma$ displayed here is strictly less
than one. The exact comparison $3^{17}<2^{27}$ gives $\alpha<27/17$;
monotonicity of $(x-1)^2/x$ for $x>1$ gives
$9\delta^2/(2\alpha)<900/918<1$.

Summing (V2) and using $\log V_l=\log l+O_\epsilon(1)$ yields
$$
 \liminf_{l\to\infty}\frac1{\log l}\sum_{t_j<l}\frac1{t_j}
                 \ge(1-\gamma)/C_\epsilon>0 .                     \tag{V3}
$$
Thus $\limsup D_l/l>0$ for the number $D_l$ of included runs:
$D_l=o(l)$ would give a vanishing normalized reciprocal sum by
partial summation. Each started run at a record index $<l$ supplies
at least one completed block among the first $l$. Sorting their odd
lengths, each length occurs at most $P$ times on the retained tail.
Hence $k_l\ge D_l^2/(2P)-O(D_l)$, proving $\limsup k_l/l^2>0$.

More generally, the same unordered conclusion holds when the bound
$P$ is any fixed integer, the allowed large lengths form a set $E$
and
$$
 \limsup_{M\to\infty}\frac{P}{\log M}
                 \sum_{m\in E,\ m\le M}\rho_m/s_m<1.
$$
The additional $\epsilon$ can be chosen sufficiently small because
the unrestricted harmonic sum of $1/s_m$ is $O(\log M)$.

## Nondecreasing order

Write $A(M)$ for the number of initial blocks through the last
one of odd length at most $M$, including the discarded fixed
prefix. The nondecreasing sequence is unbounded, since otherwise
the length hypothesis leaves finitely many runs and an impossible
infinite final run. A single run changes $V$ to at most
$V(1+(\rho_m+\epsilon)/s_m)+C_0(\rho_m+\epsilon)$.
Consequently processing at most $P$ runs at one admissible length
$M$ multiplies the preceding $V$ by at most
$(1+(\rho_M+\epsilon)/s_M)^P$ and adds $O(1)$. An inadmissible
length can be skipped. For some $\gamma'$ strictly between
$\gamma$ and one, products of these multipliers from $a$ through
$M$ are $O((M/a)^{\gamma'})$ uniformly for $1\le a\le M$.
For verification, the sum of their logarithms on
$[2^j,2^{j+1})$ is at most $(\gamma+o(1))\log2$ by the same
rotation mean and partial summation on a dyadic interval.
Use $\gamma'$ on all sufficiently large complete dyadic intervals.
The at most two partial boundary intervals cost an absolute
constant by the elementary unrestricted harmonic bound.
Iterating the inhomogeneous linear recurrence gives
$$
 V_{A(M)}\ll M^{\gamma'}+\sum_{a=1}^M(M/a)^{\gamma'}\ll M .
$$
Since $V_t\ge\epsilon t$, one has $A(M)=O(M)$, the $i$th length
is $\gg i$, and $k_l\gg l^2$. Apply
[Theorem T](RECORD_TEMPLATE_COST.md) to obtain the claimed
exceptional fractions in both cases.

## Two growing constant-gap pieces

Consider the alphabet of first-ladder words made of $u$ successive
odd gaps $2$ followed by $v$ successive gaps $1$.
Their odd length $m=u+v$ and clock $2u+v=\lfloor\alpha m\rfloor$
determine $u,v$ uniquely, if the resulting word is first-ladder.
The native encoding uses the two periodic pieces $(10)^\infty$
and $1^\infty$. Therefore no escaping positive source can realize
a sequence of these words with eventually nondecreasing lengths.
Indeed if the lengths are bounded and eventually constant, the final
word repeats forever, already impossible by (V1)'s divisibility.
If they grow, each length occupies just one run, and Theorem V
contradicts $B_l=0$. The same conclusion holds for arbitrary order
when the lengths tend to infinity and each length is eventually
used in at most nine separated runs. Equivalently, any escaping
positive realization entirely in this two-piece alphabet with
lengths tending to infinity must return to infinitely many
distinct lengths on at least ten separated runs. The explicit
symbolic positive-coefficient-divergence examples in
[ESCAPE_OF_MASS.md](ESCAPE_OF_MASS.md) illustrate the genuine
difference between a prescribed word and one fixed ordinary source.
