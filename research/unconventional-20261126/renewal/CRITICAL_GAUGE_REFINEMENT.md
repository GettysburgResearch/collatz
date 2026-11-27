# The upper bound at the first logarithmic refinement

**Status — PROPOSED separate extension.** Use $g_b$ in
[(E1)](CRITICAL_GAUGE_ENDPOINT.md). The following upper bound is
independent of the lower construction. Together they give zero
measure for $b>1$ and infinite measure for $b\le1$.

**Theorem E.1.** For every $b>1$, $\mathcal H^{g_b}(\mathcal R)=0$.

For a critical script write $d_n>0$ for its depth-$n$ deficit.
The tilted probability of a depth-$n$ word is exactly
$\exp[-Hn+h d_n]$. If $\limsup d_n/n^{1/3}=\infty$ the words
at the infinitely many depths with $h d_n\ge 2A_*n^{1/3}$
cover its projection with a summably small $g_b$ cost, using the
total tilted probability at most one. It suffices to handle
$d_i\le C i^{1/3}$ for every $i\ge n_0$, taking a countable
union over $C,n_0$ with $n_0$ arbitrarily large.

For such a script fix the same mesh as in the [endpoint proof](CRITICAL_GAUGE_ENDPOINT.md):
$n_{j+1}=n_j+L_j$, $L_j=\lfloor n_j^{2/3}(\log n_j)^6\rfloor$.
Let $p_j=\max_{n_j\le i\le n_{j+1}}d_i$ be its true stage peak,
$f=f_*$, $A=A_*=3hf/2$, and set
$$
 w_j=\left\lceil \max\{p_j,\, f n_j^{1/3}/4\}\right\rceil,\qquad
 I(x)=\kappa\int_{n_0}^x w(t)^{-2}\,dt,\qquad
 w(t)=w_j\quad(n_j\le t<n_{j+1}).
$$
Each $w_j$ is between fixed positive multiples of $n_j^{1/3}$.
Define $G_c(x)=A x^{1/3}(1-c/(\log x)^2)$ for fixed $c$.

## A deterministic obstruction to avoiding all expensive peaks

For every fixed $c>1$, infinitely many stages satisfy
$$
                          h p_j+I(n_j)\ge G_c(n_j).                 \tag{E6}
$$
Choose any $1<b_0<c$. Suppose instead that the strict reverse
inequality holds on all sufficiently late stages. Both
$I(x)-I(n_j)=O((\log n_j)^6)$ and
$G_{b_0}(x)-G_{b_0}(n_j)=O((\log n_j)^6)$ uniformly on a stage.
The gap $G_{b_0}(n_j)-G_c(n_j)$ is a positive constant times
$n_j^{1/3}/(\log n_j)^2$ and dominates these errors and $O(1)$.
Hence for every sufficiently large $x$ in stage $j$,
$$
 I(x)+h(p_j+1)<G_{b_0}(x),\qquad
 w_j\le \max\{(f/3)x^{1/3},\,(G_{b_0}(x)-I(x))/h\}.              \tag{E7}
$$
The larger clamp $f/3$ absorbs the rounding of $f n_j^{1/3}/4$.

Set $t=\log x$ and
$v(t)=(G_{b_0}(x)-I(x))/(hf x^{1/3})$. This is positive for
all sufficiently large times by (E7), and is at most $3/2$
since $I\ge0$ and $b_0>0$. It is locally absolutely continuous
even at mesh jumps. At almost every $t$ the derivative bound
$I'(x)=\kappa/w_j^2$ from (E7) and the identity $6\kappa=hf^3$
give
$$
 v'(t)\le\tfrac12-\tfrac13v(t)-
    \frac1{6\max\{v(t),1/3\}^2}
    -\frac{b_0}{2t^2}+\frac{3b_0}{t^3}.                          \tag{E8}
$$
In $0<v\le1/3$ the first three terms are at most $-1$.
For $v\ge1/3$ they equal
$-(v-1)^2(2v+1)/(6v^2)$. Thus $v$ is eventually nonincreasing.
If it ever reaches $1/3$ it must cross zero in finite time.
Otherwise its limit exists, and it must equal one, because at any
other limit the right side is bounded away below zero. This would
give $v\ge1$ on its entire sufficiently late tail.

Fix $\epsilon>0$ small enough that $(1-\epsilon)b_0>1$.
For $v$ sufficiently close to one, the last quadratic factor is
at most $-(1-\epsilon)(v-1)^2/2$. Put $y=t(v-1)$, and compute
its derivative with respect to $\log t$. Equation (E8) implies
$$
 \frac{dy}{d\log t}\le y-\tfrac12(1-\epsilon)y^2-\tfrac12 b_0
                                    +O(1/t)\le-c_0<0 .
$$
Indeed the maximum of the displayed quadratic without the error is
$[1/(1-\epsilon)-b_0]/2<0$. This forces $y<0$ at a finite later
time, contradicting $v\ge1$. This proves (E6). The argument uses
only the actual stage maxima of the particular script.

## Covering at the first stage of a selected high-cost peak

Choose $1<c<b$. For each sufficiently large stage $j$, enumerate
the integer widths $w_i$ for $i<j$, the integer $\lfloor p_j\rfloor$
and a time $N\in[n_j,n_{j+1}]$ at which that peak is attained.
Using all peak times only enlarges the cover. There are at most
$\exp(O(n_j^{1/3}/(\log n_j)^5))$ resulting choices: each stage
admits $O(1+n_j^{1/3})$ integer widths, the number of stages
is $O(n_j^{1/3}/(\log n_j)^6)$ as in (E3), and the choices at
the last stage are polynomial in $n_j$. Initial constraints before
$n_0$ can be omitted.

For a fixed choice, the tilted probability of staying in the indicated
positive strips on all complete preceding stages is at most
$$
                  C_3^{\,j}\exp[-I(n_j)]
$$
by the uniform upper strip estimate in the endpoint proof, applied
conditionally on the actual starting value of each stage. If a start
is outside its current strip the required event is empty. The
last stage need supply only its peak, no complete survival estimate.
Any retained depth-$N$ word has probability at least
$\exp[-HN+h\lfloor p_j\rfloor]$, and its image is covered by one
ternary depth-$N$ cell. Retain only choices capable of satisfying
(E6), equivalently allowing the rounding loss
$h\lfloor p_j\rfloor+I(n_j)\ge G_c(n_j)-h$. Their total $g_b$
cost at this stage is at most
$$
 \exp\!\left[
 O\!\left(\frac{n_j^{1/3}}{(\log n_j)^5}\right)
 +\max_{n_j\le N\le n_{j+1}}\{G_b(N)-G_c(n_j)\}\right]
 \le \exp\!\left[-c_1\frac{n_j^{1/3}}{(\log n_j)^2}\right].
$$
For the last inequality, $G_b(N)-G_b(n_j)=O((\log n_j)^6)$,
whereas $G_c(n_j)-G_b(n_j)=A(b-c)n_j^{1/3}/(\log n_j)^2$.
The cost is summable even over all integer $n_j$.
By (E6), taking all qualifying stages $j\ge J$ covers every script
in the specified class. Let $J\to\infty$ and then take the
countable union over $C,n_0$. This proves Theorem E.1.
