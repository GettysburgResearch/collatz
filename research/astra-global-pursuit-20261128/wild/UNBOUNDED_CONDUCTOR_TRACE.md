# Passing the unbounded one-sided pole test through the full ternary conductor

**Source-qualified written theorem.** Let $(R,Z)$ have the joint stationary
law of the two fair affine shortcut branches. Use the symbols of the
[cycle residue theorem](CYCLE_MELLIN_RESIDUE.md). For a positive real $y$
define $f_{s,y}(r)=(1-r/y)^{-s}$ when $0\le r<y$, and zero for $r\ge y$.
For every fixed $0<s<1$ and every positive odd ternary unit $a$,

$$
 \lim_{K\to\infty}\frac1K\sum_{k=1}^{K}
   \frac{3^k}a\mathbb E\!\left[f_{s,a}(R)\,
                         1_{\{Z\equiv a\bmod3^k\}}\right]=G_a(s).       \tag{1}
$$

The sum over **all** such $a$ with weights $w(a)=\log(1+1/(3a))$
also passes through this conductor limit. Thus two ordered limits of
one stationary expectation compute the ordinary density of positive
cycle basins. Restricting to $a=1$ computes half the density of the
basin of one:

$$
 \lim_{s\uparrow1}(1-s)\lim_{K\to\infty}
 \frac1K\sum_{k=1}^K3^k
 \mathbb E[(1-R)^{-s}1_{\{R<1,\ Z\equiv1\bmod3^k\}}]=d_1/2.          \tag{2}
$$

This uses the genuine unbounded observable at each finite conductor.
Neither a uniform error as $s\uparrow1$ nor a proof that the left side
is $1/2$ follows. The [prior stationary whole-window selector at PR218](https://github.com/GettysburgResearch/collatz/blob/960b4252f9a787ab8d25e9e5894cb007d1b08977/research/astra-full-proof-20261128/ACTUAL_SOURCE_STATIONARY_TRACE.md)
instead conditions on a rare finite native-word event and tests a late
signed parity grade. Formula (2) is local to the specified stationary
endpoint and sums all valuations at every conductor.

## A relative small interval at any large real height

For $y\ge1$ and $0<\epsilon\le1/2$ we have

$$
 \Pr(|R-y|\le\epsilon y)
 \le \frac{C\epsilon}y
 (1+\log y+\log(1/\epsilon))^2(1+\log(1/\epsilon)).                    \tag{3}
$$

Here and below all constants can be chosen independently of $y$.
[Weaver 19 v2, (S2)](https://rstation.ai/problems/collatz/papers/19/v2)
gives joint product-metric balls of radius $r\le1/2$ mass at most
$Cr^2\log(e/r)$. Cover the integral ternary coordinate by $O(1/r)$
balls. Thus the mass of an arbitrary real interval of radius $r$ is
$O(r\log(e/r))$. We also use the elementary stationary moment
$\mathbb E R^p<\infty$ for $0<p<1$.

Write the forward outer series with iid multipliers $A_j$ equal to
$1/2$ or $3/2$ and translations $B_j$ equal respectively to $0$ or $1/2$.
With $\Pi_0=1$, $\Pi_j=A_1\cdots A_j$, it is
$R=\sum_{j\ge0}\Pi_j B_{j+1}$. Hence $R\le\frac12\sum_j\Pi_j$.
The products form a nonnegative mean-one martingale.

Given a threshold $M>1$, stop at $\tau=\inf\{j:\Pi_j\ge M\}$.
The hitting probability is at most $1/M$ by the nonnegative martingale
maximal inequality. For a starting product $0<u<M$, put $V$ equal to
the sum of the successive products strictly before hitting $M$,
including $u$. Fix $0<p<1$ and $\rho_p=\mathbb E A_1^p<1$. The
uniform first moment estimate follows from $v\le M^{1-p}v^p$ for
$v<M$:

$$
                      \sup_{u<M}\mathbb E_u V
                          \le M/(1-\rho_p).
$$

In particular there are absolute $c,C>0$ with
$\Pr_u(V>zM)\le C e^{-cz}$ uniformly in $u<M$.
For a direct proof, stop when the subtotal first exceeds
$2M/(1-\rho_p)$. Its probability is at most $1/2$, and its overshoot
is at most $M$. The remaining sum from the next product is either zero
or has the same uniform bound by independence. Iterating gives the
estimate at multiples of $M[2/(1-\rho_p)+1]$ and monotonicity fills
the intervals.

Choose $L=C_0[1+\log y+\log(1/\epsilon)]$, with $C_0$ sufficiently
large, and $M=y/L$. When $M>1$, on $\tau=\infty$ the event in (3)
forces $V\ge y$, of probability at most $C e^{-cL}\le C\epsilon/y$.
On $\tau<\infty$, the remaining real series is an independent copy of
$R$ scaled by $\Pi_\tau\ge M$ and translated by the known stopped sum.
The conditional interval has radius at most $\epsilon L$, and hence
mass $O(\epsilon L[1+\log(1/\epsilon)])$. This remains valid when that
radius exceeds $1/2$ by the trivial probability bound. Multiply by
$1/M=L/y$. If $M\le1$, the original interval bound gives
$O(\epsilon y[1+\log(1/\epsilon)])$, which is at most the right side
of (3) because $y\le L$. This proves (3).

## The terminal factor at a high integer

Set, for odd units $y$,

$$
 g_s(y)=3\mathbb E[f_{s,y}(R)\,1_{\{Z\equiv y\bmod3\}}],
 \qquad \rho_1(y)=3\Pr(Z\equiv y\bmod3).
$$

For each fixed $s<1$,

$$
      \sup_{y\ge1}g_s(y)<\infty,\qquad g_s(y)-\rho_1(y)\to0
                             \quad(y\to\infty).                         \tag{4}
$$

On $R\le\sqrt y$, the test approaches 1 uniformly as $y\to\infty$.
On $\sqrt y<R\le y/2$, its difference from 1 is bounded and the event
has vanishing probability by the fractional moment. The same moment
bounds $\Pr(R\ge y)$. On $y/2<R<y$, divide $1-R/y$ into
$(2^{-j-1},2^{-j}]$, $j\ge1$. Equation (3) bounds the expectation
of the test over this region, after dropping the residue condition, by

$$
 \frac{C_s}{y}\sum_{j\ge1}2^{-j(1-s)}
            (1+\log y+j)^2(1+j)
       \le C'_s(1+\log y)^2/y.                                        \tag{5}
$$

This proves uniform boundedness and the limit, and the real interval
bound excludes atoms at the endpoints. The constants deteriorate as
$s$ approaches one.

## Finite conductor, fixed root, and the global sum

Take $j=k-1$. For a legal depth-$j$ inverse prefix write $R_j,A_j$
for its offset and multiplier so $a=R_j+A_j X_j$. Write
$W_j=A_jX_j/a=\prod_{i\le j}c(X_i)$. The one remaining ternary digit
and independence of the stationary tail give the exact identity

$$
 \frac{3^k}a\mathbb E[f_{s,a}(R)\,1_{\{Z\equiv a\bmod3^k\}}]
  =\frac{h(a)}a\,\mathbb E_a\left[
       W_j^{-s}\frac{g_s(X_j)}{h(X_j)}\right].                         \tag{6}
$$

Indeed $1-(R_j+A_jR')/a=W_j(1-R'/X_j)$ on each prefix, including
the direction of the strict cutoff. Its probability under $P_h$ is
$A_jh(X_j)/h(a)$. Equation (F4) of the cited paper, or first the
prefix identity for truncated tests and monotone convergence, proves
(6). Immediate nonunit terminal states have zero contribution because
the last ternary digit must be a unit. Retaining that last digit
accounts for the factor 3 in $g_s$.

Under $P_{h,a}$ a nonperiodic inverse path has distinct integer states
with $X_j\to\infty$. A periodic root is left after a finite number of
laps almost surely; its later inverse path has the same property.
We have $W_j^{-s}\uparrow W_a^{-s}$, integrable for each $s<1$ by (4)
of the companion residue note. The canonical trace floor $h\ge\alpha>0$
and (4) therefore allow replacing $g_s(X_j)$ by $\rho_1(X_j)$ and
$W_j^{-s}$ by $W_a^{-s}$ with error tending to zero in expectation.

The [bounded selection identity in Paper 12, Lemma 8](https://rstation.ai/problems/collatz/papers/12/v1)
states that averaging $\rho_1(X_j)/h(X_j)$ against a bounded full
path test gives its ordinary $P_h$ expectation. The same conclusion
holds for the integrable test $W_a^{-s}$ by truncation, because the
averaging factor is bounded by $2/\alpha$. This proves (1).

For fixed $s<1$, (6) is bounded by $(\sup g_s/\alpha)G_a(s)$
simultaneously in $a,k$. The companion note proves
$\sum_a w(a)G_a(s)<\infty$. Dominated convergence passes the entire
root sum through the conductor Cesàro average, and then its separate
pole calculation gives the density of all positive cycle basins.
Only the chosen root survives in (2). No independence between the
real and ternary coordinates was assumed.

The small-interval argument, singular test extension and residue
identities are written deductions. In particular, convergence against
bounded Lipschitz tests alone would not justify (1).

The [single-scale theorem](SINGLE_SCALE_POLE.md) subsequently removes the need for ordered limits, allowing the explicit exponent $1-K^{-1/5}$ at conductor average $K$.
