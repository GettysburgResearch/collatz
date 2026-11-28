# One explicit finite-conductor scale for the ordinary basin residue

**Source-qualified written theorem.** Let $(R,Z)$ have the unconditioned
joint stationary law of the fair affine shortcut branches. For positive odd
ternary units $a$, put $w(a)=\log(1+1/(3a))$ and
$f_{s,a}(r)=(1-r/a)^{-s}$ for $0\le r<a$, taking value zero elsewhere.
Take any $u=u_K\in(0,1/2]$ with
\[
                   u\longrightarrow0,\qquad K u^4\longrightarrow\infty.
\]
In particular one may use $u=K^{-1/5}$ for all sufficiently large $K$.
Let $s=1-u$ and define the **actual finite conductor** statistic
\[
 H_k(a,s)=\frac{3^k}{a}\,
          \mathbb E[f_{s,a}(R)1_{\{Z\equiv a\bmod3^k\}}].
\]
There is no separate normalization by ternary atom mass. Then
\[
 \begin{aligned}
 \frac{u}{K}\sum_{k=1}^K H_k(1,1-u)&\longrightarrow d_1/2,\\
 \frac{u}{K}\sum_{k=1}^K\sum_{a\ {\rm odd},\,3\nmid a}
            w(a)H_k(a,1-u)&\longrightarrow \delta\,\mathcal D_{\rm per},
                  \qquad \delta=\tfrac12\log(4/3).                    \tag{1}
 \end{aligned}
\]
Here $d_1$ and $\mathcal D_{\rm per}$ are the relative odd natural
densities of the basin of one and of all eventually periodic sources.
This improves the ordered limits in the [fixed-$s$ transfer](UNBOUNDED_CONDUCTOR_TRACE.md).
The full-proof target is a lower bound $1/2$ for the first explicit scalar
limit. Its value has not been proved. All real intervals and congruences
in $H_k$ refer to the same sample of the stationary law.

## Bounds uniform in the moving exponent

Equation (3) and the terminal decomposition in the fixed-$s$ note give
the following bounds with an **absolute** constant $C$ for $0<u\le1/2$:
\[
 \begin{aligned}
 |g_{1-u}(x)-\rho_1(x)|
    &\le C x^{-1/4}+C u^{-4}\frac{(1+\log x)^2}{x},\\
 g_{1-u}(x)&\le C+C u^{-4}\frac{(1+\log x)^2}{x}.                    \tag{2}
 \end{aligned}
\]
Use the half moment on $\{R>\sqrt x\}$. In (5) of that note use
$\sum_{j\ge1}2^{-uj}(1+j)^3\le C u^{-4}$. The bounded range
$1\le x\le4$ is absorbed by the second term. No absolute constant
here depends on $x,a,k,K$ or $u$.

Any finite segment of a nonperiodic inverse ray $X_0=a,X_1,\ldots$
consists of distinct positive integers in one ordinary orbit. In
particular, uniformly over such finite segments,
\[
 \sum_j\frac{(1+\log X_j)^2}{X_j}\le C,\qquad
              \sum_{j<K}X_j^{-1/4}\le CK^{3/4}.                       \tag{3}
\]
The first bound is dyadic summation of the published uniform orbit
sparsity exponent $\vartheta<1$. The second follows by comparison with
the first $K$ positive integers. The same first bound holds for arbitrarily
long finite prefixes even though an infinite inverse ray need not be one
forward orbit.

Use (6) of the fixed-$s$ note, $W_j=\prod_{i\le j}c(X_i)\in[e^{-B},1]$
on nonperiodic rays, and the absolute floor $h\ge\alpha>0$. The error
in replacing $g_s(X_j)$ by $\rho_1(X_j)$, after averaging $j<K$ and
dividing by $h(a)/a$, is at most
\[
                        C(K^{-1/4}+u^{-4}/K).
\]
Replacing $W_j^{-s}$ by $W_j^{-1}$ costs $O(u)$ uniformly on this interval.
For a **fixed** nonperiodic unit $a$, bounded convergence gives the
Cesàro replacement of $W_j^{-1}$ by $W_\infty^{-1}$; no rate is needed
because the moving exponent and singular terminal factor are already gone.
The bounded canonical selection identity for $\rho_1(X_j)/h(X_j)$ and
the nonperiodic inverse moment now give
\[
      \frac1K\sum_{k=1}^K H_k(a,1-u)\ \longrightarrow\ \delta d_a.     \tag{4}
\]
For any deterministic $0\le b_t\le1$, (2) and (3) also give the uniform
domination
\[
 \sum_{t=1}^{K} b_t H_t(a,1-u)
       \le C\frac{h(a)}a\left(\sum_{t=1}^{K} b_t+u^{-4}\right).        \tag{5}
\]
It holds for the same constant for every nonperiodic positive odd unit;
indeed $W_{t-1}^{-s}/h(X_{t-1})\le e^B/\alpha$ on every such path.
Source-dependent convergence in (4) is distinct from this uniform bound.

## Resolving an individual cycle

A single outer odd inverse step gives the exact finite recurrence
\[
 H_{k+1}(a,s)=\sum_{\substack{U(y)=a\\3\nmid y}}c(y)^u H_k(y,s),
 \qquad H_1(a,s)=g_s(a)/a.                                            \tag{6}
\]
The factor is $c(y)^{1-s}$ because the one-step multiplier is
$A=3/2^e=a c(y)/y$ and the normalized deficit gains the factor $c(y)$.
All terms are nonnegative.

Fix a cycle $C$ of odd period $p$ and a phase $a\in C$. Put
$L=\sum_{x\in C}w(x)>0$ and let $O_C$ be the off-cycle unit parents
of its phases. For $y\in O_C$, let $b_y\in\{1,\ldots,p\}$ be its
first forward distance to $a$ and
$V_y=\sum_{i=0}^{b_y-1}w(U^i y)$. The contributions to $H_k(a,s)$
using this exit, with complete preceding inverse laps, are exactly
\[
 \sum_{\ell\ge0:\ b_y+\ell p\le k-1}
        e^{-u(V_y+\ell L)}H_{k-b_y-\ell p}(y,s).
\]
The remaining term follows the cycle throughout the $k-1$ peeled
edges and ends at $H_1$ at a cycle phase. Each full lap contributes
$e^{-uL}$ there. Its total after multiplication by $u/K$ and summation
in $k\le K$ is $O_C(u^{-4}/K)$ by (2) and the geometric series.

For fixed $y$, the exit contribution to the $u/K$ average is exactly
\[
 e^{-uV_y}\frac{u}{1-e^{-uL}}\frac1K
 \sum_{t=1}^{K-b_y}H_t(y,s)
 \left(1-e^{-uL(1+\lfloor(K-b_y-t)/p\rfloor)}\right).                \tag{7}
\]
The final exponential weights have total $O_C(1/u)$, and the missing
$b_y$ end dates are bounded by $p$. By (5), deleting the weights and
restoring the missing dates costs
$O_C((h(y)/y)(u^{-1}+u^{-4}+1)/K)$ inside the normalized sum.
Thus (4) gives a limit of $\delta d_y/L$. Formula (5) dominates
(7) by $C_C h(y)/y$ for large $K$. The off-cycle inputs satisfy
\[
 \sum_{y\in O_C}h(y)/y
      =\delta\sum_{y\in O_C}\beta_y\le\delta d_C .
\]
The countable entrance partition and its tightness proof are in the
[cycle residue note](CYCLE_MELLIN_RESIDUE.md). Dominated convergence
therefore gives $\delta d_C/L$ for the limit of the $u/K$ average
at $a$. At the standard cycle $p=1$, $L=\log(4/3)$, yielding
$d_1/2$ in (1).

## Uniform summation across cycles of unbounded lengths

Let $\mathrm{Per}$ be the union of all positive odd periodic vertices.
The sum $\sum_{y\in\mathrm{Per}}1/y$ is finite. Here is a short elementary
verification that avoids any assumption on the number of cycles.
For $X\le2^m$, $m=\lceil\log_2 X\rceil$, all possible length-$m$
shortcut words from positive $x\le X$ are distinct as words for
distinct starts. For grade $q\le3m/5$, every endpoint is at most
$3^{3m/5}+(3/2)^m$, using the maximal all-odd affine offset.
There are at most $2^{m H_2(3/5)}$ exceptional words of higher grade by
the binary entropy bound. The shortcut map is injective on the union of
all its cycles, since each periodic vertex has exactly one periodic
predecessor. Each odd $U$-cycle lies on a shortcut cycle. Consequently
\[
 \#(\mathrm{Per}\cap[1,X])=O(X^\eta),\qquad
       \eta=\max\{(3/5)\log_2 3,H_2(3/5)\}<1 .
\]
Dyadic summation proves the assertion. This is the elementary
synchronous-image argument also used in the project's orbit sparsity
proof, applied to the union where synchronous injectivity still holds.

For any forward sequence of positive odd integers $z,U z,\ldots$, set
$S_j=\sum_{i<j}w(U^i z)$. Since $w\le\log(4/3)$, a telescoping sum gives
\[
       \sum_{j\ge0}w(U^j z)e^{-uS_j}\le C/u,                           \tag{8}
\]
using $1-e^{-u w}\ge c_0uw$ for $0<u\le1$. This uses no lower bound
on a cycle's individual $w$-values.

In the sum of all terms that stay on a cycle for $j=k-1$ inverse
steps, index by their terminal cycle vertex $y$ and then follow its
forward trajectory to $a=U^j y$. The contribution before averaging
is $w(U^j y)e^{-uS_j}H_1(y,s)$. Equation (8) shows their **total**
in (1) is at most
\[
      \frac C K\sum_{y\in\mathrm{Per}}H_1(y,s)
        \le C u^{-4}K^{-1}\sum_{y\in\mathrm{Per}}1/y\longrightarrow0. \tag{9}
\]
For the exits of one cycle $C$, instead fix $y\in O_C$ and the
remaining time $t\ge1$. A consuming phase must be $a=U^j y$ for some
$j\ge1$, with coefficient $w(U^j y)e^{-uS_j}$. Equations (8) and (5)
bound the whole exit contribution from this cycle in (1) by
\[
     \frac C K\sum_{y\in O_C}\sum_{t=1}^{K}H_t(y,s)
           \le C(1+u^{-4}/K)\sum_{y\in O_C}h(y)/y \le C' d_C.         \tag{10}
\]
All constants in (9) and (10) are independent of cycle and period.
Since $\sum_C d_C\le1$, we may sum the fixed-cycle limits from (7)
after weighting by $w(a)$ and using (9). They contribute
$\delta\sum_C d_C=\delta\mathcal D_{\rm per}$. Finally (5) and
$\sum_{a\ {\rm nonperiodic}}w(a)h(a)/a\le\delta B$ bound the entire
nonperiodic-root contribution by $Cu(1+u^{-4}/K)$, which vanishes.
This proves both parts of (1).

The published bounded-test integer fibre, positive predecessor floor,
entrance laws and orbit packing remain separate inputs. The finite
controls do not evaluate $\nu$, its singular integrals, or either
unknown basin density. No interchange involving $s=1$ at fixed $K$
is used.
