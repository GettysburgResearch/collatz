# How many ordinary starts can use one canonical arrow?

**PROPOSED written theorem.** Use the positive shortcut map with odd step
$x\mapsto(3x+1)/2$. Treat each ordinary edge as traversable in either
direction and permit the extra forward edge $q\to3q$ at $q\equiv17\bmod48$.
PR 201 constructs a route from every positive input to 1 in this augmented
graph. The following bound counts original sources in one octave that use
one specified arrow. It allows arbitrary choices among local paths respecting
the published size and length bounds.

## Source congestion

For $X\ge2$, let $N_X(q)$ count distinct integers $X\le n<2X$ whose route
uses $q\to3q$ at least once. There is an absolute constant $C$ for the
frozen route such that, writing $\log^+ x=\max(0,\log x)$,

$$
N_X(q)\le C(1+X/q)(1+\log^+(X/q)),\qquad
N_X(q)=0\quad(q\ge2KX),\qquad K=98304. \tag{1}
$$

The upstream path consists of successive stages starting at
$u_0=n,u_1,\ldots$, where $u_{i+1}\le\lambda u_i$ and $\lambda=725/763$.
Each stage takes at most $D=30367$ edges and each canonical arrow within
it has source at most $Ku_i$. The even stage halves its source. These
written bounds and their finite arithmetic certificates are upstream
inputs. The argument here is independent of ordinary Collatz convergence.
[PR 201 frozen construction](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/six-hour-20261127/coupling/CANONICAL_PATHS.md)

Stop immediately before a specified charge $q$ in stage $s$, numbered
from zero. Every augmented edge multiplies its positive input by at least
$1/3$. Both endpoints of every edge in stage $i$ are therefore at least
$3^{-D}u_i$. The contraction between stages gives

$$
\sum_{i=0}^s u_i^{-1}\le[(1-\lambda)u_s]^{-1}
\le K/[(1-\lambda)q],\qquad
s\le \log(Kn/q)/(-\log\lambda).
$$

All edge ratios are powers of 2 and 3, apart from factors
$(1+1/(3v))^{\pm1}$ on odd native edges with native odd input $v$. The
same estimate holds for either orientation. Adding logarithms gives
integers $a,b$ such that

$$
\log(q/n)=a\log2+b\log3+\epsilon,\qquad
|\epsilon|\le C_0/q,\qquad |b|\le D(s+1),\qquad
C_0=D3^DK/[3(1-\lambda)]. \tag{2}
$$

For $q\ge C_0$ the source octave has logarithmic width $\log2$ and the
error is at most one. Each $b$ permits only a bounded number of $a$.
For each pair $(a,b)$ the permitted logarithms of $n$ form an interval
of length at most $2C_0/q$. Within the source octave this permits at most
$1+4C_0X/q$ integers by the mean value theorem. The stage bound gives
$O(1+\log^+(X/q))$ different $b$. For $q<C_0$ the trivial $N_X(q)\le2X$
is absorbed by adjusting the absolute constant. The cutoff follows from
$q\le Kn<2KX$. Repeated visits and overlapping paths only reduce the count.

## Bad-to-good arrows

Write $\mathcal D$ for canonical sources $q$ failing to reach 1 with
$3q$ reaching 1. A route from a bad start to 1 must have such a charge
at its first bad-to-good change. For $Y\le2KX$, (1) gives

$$
X^{-1}\#\{X\le n<2X:\text{the route uses some }q\in\mathcal D\cap[Y,2Y)\}
\ll_K (1+\log^+(X/Y))Y^{-1}\#(\mathcal D\cap[Y,2Y)). \tag{3}
$$

For odd $q$ the starts $q$ and $3q+1$ share a future. Thus a reverse
defect requires noncoalescence of $3q$ and $3q+1$. Alternatively the
finite-clock tripling coalescence estimate quoted by PR 201 directly
gives the source-qualified input
$\#(\mathcal D\cap[Y,2Y))\ll Y/\sqrt{\log(2Y)}$. Indeed, at
$h=\lfloor(\log_2 Y)/2\rfloor$ each complete block of $2^h$ sources
contributes $O(2^h/\sqrt h)$ failures. The two incomplete blocks cost
$O(2^h)$. Inequalities (1) and (3) require no coalescence estimate.
[Exact finite-clock input used by PR 201](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/infinity-20261127/coupling/PINNED_TARGETS.md)

Summing (3) over octaves from $Xe^{-J}$ to $2KX$ bounds the fraction
of sources using any reverse defect at or above $Xe^{-J}$ by

$$
O\big((1+J)^2/\sqrt{\log X}\big),\qquad 0\le J\le(\log X)/2. \tag{4}
$$

For $J=o((\log X)^{1/4})$, outside $o(X)$ exceptions a bad start must
charge a strictly smaller scale than $Xe^{-J}$. If $z$ is the least
reverse defect, summing (3) from $z$ to $2KX$ gives, for $X\ge z/(2K)$,

$$
X^{-1}\#\{X\le n<2X:n\text{ fails to reach 1}\}
\ll (1+\log^+(X/z))^2/\sqrt{\log(2z)}.
$$

This bound increases with $X/z$. A single least reverse defect can
attract arbitrarily large original sources. The mandatory even stages on
$2^j n$ reproduce the route from $n$ afterwards. The argument leaves
open the exclusion of such a fixed defect.

## A forced low vertex for short all-pairs paths

In the entire ordinary-plus-tripling graph, even allowing tripling at
every positive integer in either direction, fix $X\le n<2X$. For a path
of length at most $L$ all of whose vertices are at least $M\ge L\ge1$
and whose endpoint $m$ is also in this octave, edge ratios give

$$
\log(m/n)=a\log2+b\log3+\epsilon,\qquad
|b|\le L,\qquad |\epsilon|\le L/(3M).
$$

Counting as in (2) permits $O(L+XL^2/M)$ distinct endpoints. Thus a
family of paths of length at most $L=o(X)$ connecting every pair in
the octave sends at least a fixed positive fraction through the first
$A L^2$ integers, for a sufficiently large absolute $A$. Some one low
vertex then lies on $\gg X^2/L^2$ chosen routes. This applies in
particular to the published logarithmic all-pairs route. The graph
argument does not identify this low vertex as a basin disagreement.
