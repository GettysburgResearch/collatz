# A first moment of exact marked return atoms separates an extra positive cycle

Use the original physical rows and weights of [the delayed-trace theorem](DELAYED_CYCLE_TRACE.md), pooling the raw measures at a fixed depth,
\[
   \Phi_d=\sum_{y\ge1,\ y\ \mathrm{odd}}\frac{1}{y(3y+1)}
                 \sum_{w:|w|=d,\,U^d x_w=y}
                      3^d2^{-s_w}\rho_1(x_w)\,
                      \delta_{\,3^d2^{-s_w}x_w/y}.
\]
The inner sum runs over the legal inverse words to the indicated target and $s_w$ is their total division count. These are finite measures because each depth-$d$ row mass is at most $2^{d+1}$ and the stopping weights are summable in $y$. Define a nonnegative extended-real number
\[
       \mathcal J=\sum_{d=1}^\infty d
                       \sum_{s=d}^\infty\Phi_d(\{3^d2^{-s}\}).
                                                               \tag{1}
\]
The observable selects only the exact indicated atoms of the original measures. There is no limit from a surrounding interval in (1).

If the fixed odd cycle at one is the only positive integer cycle, then $\mathcal J=3$. Every additional positive cycle contributes **strictly more than $15/4$**, so
\[
      \boxed{\quad
        \mathcal J=3\quad\text{or}\quad\mathcal J>27/4 .
      \quad}                                                  \tag{2}
\]
Finiteness of $\mathcal J$ is equivalent to finiteness of the set of positive cycles. A proof of the scalar upper bound $\mathcal J\le27/4$ would exclude even one extra cycle independently of any escaping trajectory. We have no such upper bound. Unlike the conventional count of primitive cycles, the contribution here is fixed by the given, unmodified stopping and terminal weights and involves the distribution of individual reciprocal heights.

## Exact return extraction and repetitions

A legal word contributes at the displayed atom only if $3^d2^{-s_w}x_w/y=3^d2^{-s}$. Both $x_w$ and $y$ are positive odd integers. Their ratio is a power of two only when they are equal, so $x_w=y$ and $s_w=s$. Conversely a fixed point of $U^d$ with that division total contributes. In particular every positive atom at the selected location comes from a true return, with no nonperiodic or escaping sources. Distinct $s$ give different locations.

For a cycle $C$ with least odd period $p$, write $h$ for its complete division total and $\lambda=3^p/2^h<1$. At $d=kp$, every $y\in C$ contributes $\lambda^k\rho_1(y)/[y(3y+1)]$ to the selected $s=kh$. At other $d$ the cycle contributes zero. Summing $k\lambda^k=\lambda/(1-\lambda)^2$ by Tonelli gives the exact identity
\[
  \mathcal J=\sum_C J_C,\qquad
  J_C=\frac{p\lambda}{(1-\lambda)^2}
       \sum_{y\in C}\frac{\rho_1(y)}{y(3y+1)}.                \tag{3}
\]
At $(p,h,y)=(1,2,1)$ this gives $(3/4)(1/4)/(1-3/4)^2=3$.

One can also recover each individual primitive clock mass. Put
\[
 A(d,s)=3^{-d}2^s\Phi_d(\{3^d2^{-s}\}),\qquad
 P(p,h)=\sum_{C:\,(p_C,h_C)=(p,h)}\sum_{y\in C}\pi(y)\rho_1(y).
\]
Then $A(d,s)=\sum_{k\mid\gcd(d,s)}P(d/k,s/k)$. Ordinary finite Möbius inversion gives $P(p,h)=\sum_{k\mid\gcd(p,h)}\mu(k) A(p/k,h/k)$. Least symbolic period and reduced clock slope are different; the divisor sum accounts for returns to genuine least cycles.

## Cost of any extra component

Set $g_y=\log(1+1/(3y))$ and $g=\sum_{y\in C}g_y=-\log\lambda$. Since $w(y)=e^{-g_y}$, the actual stopping weight satisfies
\[
      \frac1{y(3y+1)}
        =3\frac{(1-w(y))^2}{w(y)}
        =12\sinh^2(g_y/2).
\]
Consequently
\[
       J_C=\frac{3p\sum_{y\in C}\rho_1(y)\sinh^2(g_y/2)}
                          {\sinh^2(g/2)}
       \ \ge\ 
       \frac{3p}{\sum_{y\in C}1/\rho_1(y)}
                \left(\frac{g/2}{\sinh(g/2)}\right)^2.        \tag{4}
\]
The inequality uses $\sinh u\ge u$ for $u\ge0$ and weighted Cauchy–Schwarz on $(g_y)$. The finite integer selector strengthens the bound: after a predecessor with division exponent $e$, the landing residue $y$ modulo three equals $2^{-e}$, so $\rho_1(y)=2$ whenever $e$ is odd. At least $2p-h$ of the $p$ exponents equal one, since the others are at least two. It follows that $\sum 1/\rho_1(y)\le h/2$.

Use the published verification below $2^{71}$ and the stated gap estimate of Paper 217/v1. They give $\min(C)>1000$ and $g<0.024$ on every extra cycle. The product identity also gives $h/p\le\log_2(3+1/\min(C))<159/100$, by $(3001/1000)^{100}<2^{159}$. For $0<u<1$, the series for $\sinh$ gives $\sinh(u)/u\le1/(1-u^2)$. Hence the right side of (4) is at least
\[
        (600/159)\bigl(1-(3/250)^2\bigr)^2>15/4.
\]
This establishes (2), along with the finiteness equivalence, using only the two indicated quantitative inputs for the numerical separation. These comparisons do not bound the total contribution from above. [Bařina, computational verification](https://doi.org/10.1007/s11227-025-07337-0) · [Paper 217/v1, total gap with the verified floor](https://rstation.ai/problems/collatz/papers/217/v1)

At each fixed $d$ there are only finitely many positive returns, because every actual positive lap has $s_w\le2d$ and the word specifies its unique rational fixed point. Thus the depth truncations in (1) increase to $\mathcal J$ and indefinitely many initial values can coincide with those from the fixed cycle before the least period of an extra cycle is reached. The discontinuity required to extract the exact dyadic-clock atoms also prevents the stationary weak limit, or the CDF-depth convergence alone, from evaluating (1).

## Actual upper bounds in the loss clock

Write $a_C=\sum_{y\in C}\pi(y)\rho_1(y)$. The physical selector is at most two. Since $\sinh^2(u+v)\ge\sinh^2u+\sinh^2v$ for $u,v\ge0$, we have
\[
 a_C\le24\sinh^2(g/2)=6(1-\lambda)^2/\lambda .
\]
Writing $B_{d,s}=3^d2^{-s}$, the total and the logarithmic-loss moment of the selected return atoms over the extra cycles therefore satisfy
\[
 \sum_{C\ne\{1\}}a_C\sum_{k\ge1}\lambda_C^k
    \le 6\sum_{C\ne\{1\}}(1-\lambda_C)<0.14301,
 \qquad
 \sum_{C\ne\{1\}}a_C\sum_{k\ge1}kg_C\lambda_C^k
    \le 6\sum_{C\ne\{1\}}g_C<0.14301 .
\]
Both estimates use the stated total-gap bound $\sum_{C\ne\{1\}}g_C<0.023835$ of Paper 217. The exact contributions to add for the fixed cycle are $3/4$ and $3\log(4/3)$ respectively. For every fixed $v\ge0$, also $\sum_{C\ne\{1\}}a_C\sum_{k\ge1}(kg_C)^v e^{-kg_C}<\infty$, since $g\sum_{k\ge1}(kg)^v e^{-kg}$ is bounded on $0<g<0.024$. Thus all nonnegative logarithmic moments of actual selected returns are finite. Depth $d=kp$ replaces the loss $kg_C=-\log B_{d,s}$ by the unbounded factor $p/g_C$.

For example, let $\mathcal J_{\rm extra}(r)$ insert $r^d$ in (1) and omit the fixed cycle, $0<r<1$. The bound $d r^d\le1/(e|\log r|)$ against the finite unweighted measure gives $\mathcal J_{\rm extra}(r)<0.14301/(e|\log r|)$. In fact $|\log r|\,\mathcal J_{\rm extra}(r)\to0$ by dominated convergence for that finite measure. Neither assertion controls $\mathcal J_{\rm extra}(1)$.

## Test of a possible strengthening

Retaining only the circular arrows of disjoint true positive rational Collatz cycles shows why the summed CDF-depth variation and fractional gap bounds cannot alone force a finite ordinary-clock moment. Take distinct upper continued-fraction convergents $h_j/p_j$ of $\log_2 3$. Their positive gaps satisfy $g_j=h_j\log2-p_j\log3< (\log 2)/p_j$, with $p_j$ growing at least geometrically along this upper subsequence. A positive integer composition of $h_j$ into $p_j$ positive exponents yields a genuine positive rational orbit via the affine fixed-point formula. Its odd numerator and odd denominator are both coprime to three at every phase, because the loop equation reduces modulo three to a positive power of two. The clock is coprime, hence every such loop is primitive. Distinct clocks give disjoint circles. Use the native weights $\rho_1$ interpreted in $\mathbb F_3$ and $\pi(y)=1/[y(3y+1)]$ at these rational sites. Delete all incoming arrows off the selected circles.

Let $S_j=\sum_{y\in C_j}1/y$. In this model each finite target row contains one atom. The sum over all $d\ge0$ and all sites of $C_j$ of $\pi(y)L_{d,y}(1)$ is at most
\[
   \frac{2}{3(1-e^{-g_j})}\sum_{r=0}^{p_j-1}
                           \sum_{i\bmod p_j}\frac1{x_i x_{i-r}}
   =\frac{2S_j^2}{3(1-e^{-g_j})}.
\]
Indeed at $d=kp_j+r$ the survival along the selected word is at most $e^{-kg_j}$; use its actual affine multiplier $B x_i/x_{i-r}$. Since $1/y=3(e^{g_y}-1)\le3 e^{g_j}g_y$, this bound is $O(g_j)$. Adjacent CDF differences are bounded by the sum of the two full masses. The model therefore has summable unrestricted variation and all fractional gap sums $\sum_j g_j^s$ finite for every $s>0$. Nevertheless (4) gives $J_{C_j}\ge3[g_j/(2\sinh(g_j/2))]^2\to3$, so its ordinary first diagonal moment diverges. The construction uses rational sites and deletes the other integer-map parent branches. It does not satisfy the full ordinary all-parent harmonic equations or assert the presence of any extra integer cycle.

The [exact checker](check_diagonal_moment.py) tests pure-atom extraction through twelve true odd steps for all unit sources below 10,001, verifies the fixed contribution exactly, and checks the physical selector and stopping identity on small rational loops. [Recorded control](../../../reports/astra-global-20261128/cycles/DIAGONAL_CYCLE_MOMENT.json) · [Five strictly checked trace kernels](CycleTrace.lean)
