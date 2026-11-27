# Integral test at the Hausdorff gauge of unbounded incoming slopes

**Status — PROPOSED joint refinement.** Use the ternary target set
$X=\{y\in\mathbb Z_3:B(y)=\infty\}$ and the notation of
[the logarithmic-gauge theorem](../operator/UNRESTRICTED_GAUGE.md).
The two lanes independently identified length-weighted first-passage
excursions to settle the missing endpoint. The integral test below uses
operator OP-U2, independently checked in [the audit](REVIEW_UNRESTRICTED.md).
The construction uses compatible inverse scripts in the symbolic
ternary target space. The exceptional set $X$ contains no positive ordinary integer.

Write $\theta=H_2(\log_3 2)$. Let $\psi:[1,\infty)\to(0,\infty)$
be eventually nondecreasing, with $\psi(2t)\le C\psi(t)$ for all
sufficiently large $t$. Suppose $g(3^{-q})=3^{-\theta q}\psi(q)$
is a Hausdorff gauge at small ternary scales. Finite initial changes
and fixed positive multiplicative constants have no bearing on this
theorem. Define
$$
 I_\psi=\sum_{\ell\ge1}2^{-\ell}\psi(4^\ell).
$$

**Theorem U.** The measure $\mathcal H^g(X)$ is zero if
$I_\psi<\infty$, and is infinite if $I_\psi=\infty$.
Equivalently the test is convergence of
$\int^\infty \psi(t)t^{-3/2}\,dt$, by monotonicity and doubling.
In particular $\psi(q)=\sqrt q$ gives infinite measure. For
$\psi(q)=\sqrt q/(\log q)^v$ the measure is zero for $v>1$
and infinite for $v\le1$. Iterated logarithms can be tested by
the same criterion.

## Convergent series

Write $a=\log(3/2)$, $b=\log2$,
$p=b/\log3$ and $h=-\log(1-p)/b>1$. Give odd and even inverse
letters the counting probabilities $p$ and $1-p$. At native clock
$k$ and odd count $q$ the log slope is $S_k=q\log3-kb$, and a
specified word has probability $3^{-\theta q}e^{hS_k}$. Write
$\tau_L$ for first strict passage above $L$. The [one-sided
survival bound](OCCUPATION.md) gives
$\Pr(\tau_L>n)\le C(1+L)/\sqrt{n+1}$ for $L\ge1$.
The complete first-passage cylinders cover $X$, their odd counts
are at least $L/a$, and their total gauge cost is at most
$e^{-hL}\mathbb E[\psi(\tau_L)]$. By dividing the positive integers
into $[4^\ell,4^{\ell+1})$ and treating bounded lengths separately,
$$
 \mathbb E[\psi(\tau_L)]\le C_\psi(1+L)(1+I_\psi).
$$
The inclusion of $\tau_L=4^\ell$ uses survival through $4^\ell-1$.
Passage is almost surely finite by this same tail bound. Taking
$L\to\infty$ proves zero measure. No compatibility between the
different scripts of an arbitrary target was assumed.

## Normalizing over many length scales

We may take $\psi\ge1$ and nondecreasing, with
$\psi(2t)\le D\psi(t)$ for every $t\ge1$, by equivalent finite
changes. Fix $I_\psi=\infty$. For $N=4^\ell$ large, let $G_N$ be
the event in OP-U2 that the first strict positive passage $\tau$
lies in $[N,2N]$, its overshoot is in $[a/4,3a/4]$, and
$V=\sum_{i<\tau}e^{S_i}\le K$, where $K$ and $c>0$ are uniform
and $\Pr(G_N)\ge c/\sqrt N$. The $G_N$ are pairwise disjoint.

A stage uses any finite range $\mathcal N=\{4^l,\ldots,4^u\}$
of these powers. Multiply the original probabilities of its stopped
words on $G_N$ by $\psi(N)/Z$, where
$$
                     Z=\sum_{N\in\mathcal N}\psi(N)\Pr(G_N).
$$
This defines a probability on stopped words. Starting the range
arbitrarily far out, $Z$ can be made arbitrarily large, by divergence
of $I_\psi$.

For a completed stage of length $m$, the likelihood ratio of its
word to the original counting probability is at most $\psi(m)/Z$.
For a nonempty unfinished prefix of $r$ native steps, having
nonpositive local log slope $s$, its likelihood ratio is at most
$$
                     C(1+|s|)+D\psi(r)/Z.                    \tag{U5}
$$
For $N\le2r$ the remaining events are disjoint under the conditional
law given that prefix, and their weights are all at most $\psi(2r)$.
For $N>2r$, the future must stay at most $-s$ relative to the current
position until native time $N-1$. This costs at most
$C(1+|s|)/\sqrt N$ by the survival estimate. Summing the weighted
bounds and dividing by $Z$ costs at most $C(1+|s|)/c$.
This proves (U5); an empty partial prefix has ratio exactly one.
No upper first-passage local limit estimate is needed here.

Choose successive finite ranges inductively. If $L_{j-1}$ denotes
the maximum, over all possible supports of the completed stages
$1,\ldots,j-1$, of their cumulative likelihood ratio, then
$0<L_{j-1}<\infty$ (take $L_0=1$). Choose the next range with
$$
                      Z_j\ge e^{j^2} L_{j-1}.                 \tag{U6}
$$
Take its lower endpoint beyond the preceding finite range if desired.
Concatenate independent stages under their respective normalized
laws. Their actual endpoint gains lie in $[a/4,3a/4]$, so slopes at
stage endpoints tend to infinity. All scripts can be decoded from
successive first passages above their own starting levels. An
unfinished prefix is never charged for more than the single current
stage.

Let $k$ be total native length of a prescribed compatible prefix,
with its current (possibly empty partial) stage numbered $j\ge2$.
Write $R_{j-1}$ for its completed likelihood ratio and $m_{j-1}$
for the last complete length. Equation (U6) gives both
$$
 R_{j-1}\le e^{-(j-1)^2}\psi(m_{j-1}),\qquad
 R_{j-1}/Z_j\le e^{-j^2}.
$$
Use (U5), $\psi(r),\psi(m_{j-1})\le\psi(k)$ and
$|s|\le 3aj/4+(-S_k)_+$. The binary prefix measure satisfies
$$
 \mu([w])\le C\Pr(w)e^{-(j-1)^2}\psi(k)
                     (1+j+(-S_k)_+).                           \tag{U7}
$$
This control includes the first few steps following an arbitrarily
long completed excursion, where a normalization by the length of
the current excursion alone would give the wrong bound.

## Projection to ternary targets

Stop each script at its $q$th odd letter. All $q$ are reached since
each completed stage strictly increases log slope. The stopped word
determines one ternary class modulo $3^q$ and the compatible
nested classes define a point of $X$. For that fixed $q$, group
stopped words by stage index $j$ and native clock $k$. At these
counts $S=S_k=q\log3-kb$ is fixed. For every compatible word the
single-stage occupation truncations and endpoint bounds give
$$
 S\le 3aj/4,\qquad
 \sum_{i<k}e^{S_i}\le K j e^{3aj/4}.
$$
This estimate includes the initial part of the current stage because
it is completable to a word in $G_N$. The integer carry of
[OP-B1](../operator/TERNARY_BARRIER.md) satisfies
$0\le A/3^q\le\frac12e^{-S}\sum_{i<k}e^{S_i}$.
At fixed $k,q$ and target residue the carry lies in one class
modulo $3^q$, and the word is recovered from its carry. Thus the
number of compatible stopped words in this group for the ball
is at most $C(1+j)e^{3aj/4-S}$, absorbing the extra one since
$S\le3aj/4$.

Doubling implies $\psi(k)\le C\psi(q)(1+(-S)_+)^{c_D}$:
indeed $k=(q\log3-S)/b\le C q(1+(-S)_+)$ for $q\ge1$, and
iterating the doubling inequality proves the claim. Combining
(U7) with the carry count and the exact word probability leaves,
apart from $C3^{-\theta q}\psi(q)$, at most
$$
 e^{-(j-1)^2+O(j)}
 \sum_{\substack{k\ge q\\S=q\log3-kb\le 3aj/4}}
 e^{(h-1)S}(1+(-S)_+)^{1+c_D}.
$$
The sum is $O(e^{C'j})$ uniformly in $q$: the negative side is a
polynomially weighted geometric series, and the nonnegative side is
a geometric series up to $3aj/4$. The strict inequality $h>1$ is
needed for this arithmetic projection. No factor proportional to
$q$ was discarded.

There is a deterministic $J(q)\to\infty$ such that every stopped
prefix at odd depth $q$ has $j\ge J(q)$: a fixed finite collection
of stages has fixed finite maximal total length. Summing the last
bound over $j\ge J(q)$ gives for the ternary pushforward probability
$\nu$,
$$
 \sup_y\frac{\nu(y+3^q\mathbb Z_3)}
                  {3^{-\theta q}\psi(q)}
 \ \le C\sum_{j\ge J(q)} e^{-(j-1)^2+O(j)}
 \longrightarrow0.                                             \tag{U8}
$$
Eventually the first stage is absent. Every positive-diameter
subset of $\mathbb Z_3$ is contained in a ball of the same diameter,
and (U8) gives zero mass to singletons. Thus for covers at small
scales the total gauge cost is at least the reciprocal of a
quantity tending to zero. This proves infinite measure.

This result gives an exact criterion for the unrestricted inverse
maximum. The all-prefix positive critical trace has a different
small-deviation cost, characterized by [Theorem S](SHARP_GAUGE.md).
