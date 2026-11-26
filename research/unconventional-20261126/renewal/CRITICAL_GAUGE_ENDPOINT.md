# Infinite measure at the critical cube-root gauge

**Status — PROPOSED.** The critical trace $\mathcal R$ and constants
$H,\theta,\kappa,h,f_*,A_*,K_*$ are as in [Theorem S](SHARP_GAUGE.md).
All logarithms in this note are natural. For ternary depth $n$ define
the small-scale gauge by
$$
 g_b(3^{-n})=\exp\!\left[-Hn+
               A_* n^{1/3}\left(1-\frac{b}{(\log n)^2}\right)\right].
                                                                    \tag{E1}
$$
**Theorem E.** $\mathcal H^{g_b}(\mathcal R)=\infty$ for every real
$b\le1$. In particular the measure at the *original* exact
cube-root transition constant $K_*$ is infinite, by $b=0$.
The [matching upper bound](CRITICAL_GAUGE_REFINEMENT.md) treats
$b>1$. These results concern the ternary image of all infinite
positive-prefix deficit paths. They impose upper covering bounds
on subsets, including an actual ordinary record cluster when
applicable. Lower bounds on this universal set do not transfer to a
particular ordinary orbit.

## Quantitative strip estimates on polylogarithmically long stages

Under the geometric tilt of Theorem S the centered deficit increments
have mean zero, variance $\sigma^2$ and an exponential moment for all
parameters in a neighborhood of zero. On each stage, KMT gives a
coupling of these partial sums $Z_i$ to Brownian motion $B_t$ of
variance rate $\sigma^2$ such that
$$
 \Pr\big(\max_{i\le L}|Z_i-B_i|>C\log(2L)+x\big)\le C e^{-cx}
       \quad(x\ge0).                                                \tag{E2}
$$
Normalize by $\sigma$, use Theorem 1, equation (1.1), and extend
the Gaussian increments to Brownian paths between integer times.
The constants depend only on this one fixed increment law.
[Komlós, Major and Tusnády, 1976, Theorem 1, p. 33](https://www.renyi.hu/~major/articles/KMT2.pdf)

Start a stage at large odd depth $n$. Set $T=(\log n)^6$ and
$L=\lfloor n^{2/3} T\rfloor$. Uniformly when
$c_1n^{1/3}\le w\le c_2n^{1/3}$ for fixed $0<c_1<c_2$,
the following hold.

* From any point in $[w/3,2w/3]$, the probability of remaining
  inside $(0,w)$ for all $L$ steps and ending in
  $(.45w,.55w)$ is at least $c_3\exp[-\kappa L/w^2]$.
* From any point in $[0,w]$, the probability of remaining inside
  $[0,w]$ for those steps is at most $C_3\exp[-\kappa L/w^2]$.

For the first bound use (E2) with displacement $\Delta=C_4 T$
for a sufficiently large fixed $C_4$. Here $\log L=O(\log n)=o(T)$,
so the coupling failure is $o(\exp[-\kappa L/w^2])$ uniformly in
the prescribed widths. For Brownian motion impose the narrower
interval $(2\Delta,w-2\Delta)$ and the terminal window
$(.48w,.52w)$. By Brownian scaling and the absorbing interval
sine series in Theorem S, its probability is at least
$c\exp[-\kappa L/(w-4\Delta)^2]$ uniformly in the interior
starting point, since $L/w^2\to\infty$. Its ratio to
$\exp[-\kappa L/w^2]$ is bounded below by a positive constant,
because $T\Delta/w\to0$. Subtracting the coupling failure gives
the first bound.

For the upper bound replace the Brownian interval by
$[-2\Delta,w+2\Delta]$. When the walk stays in the original closed
interval and the coupling succeeds, each integer-time Brownian
sample lies within $[-\Delta,w+\Delta]$. The probability that
some continuous Brownian displacement from its left integer
endpoint during one of the $L$ unit intervals exceeds $\Delta$
is at most $4L\exp[-\Delta^2/(2\sigma^2)]$ by reflection.
Adding this error and the coupling error to the enlarged-interval
upper bound $C\exp[-\kappa L/(w+4\Delta)^2]$ proves the assertion.
Both errors are controlled at a scale smaller than the rare
strip-survival probability itself.

## A slowly varying width

Write $f=f_*$ and $A=A_*$. Then $6\kappa=hf^3$ and $A=3hf/2$.
For sufficiently large $x$ put $t=\log x$,
$$
 u(t)=\frac1t+\frac1{t\log t},\qquad W(x)=f x^{1/3}(1+u(t)).
$$
This width is increasing eventually and $W'(x)=O(x^{-2/3})$.
Use the stages $n_{j+1}=n_j+\lfloor n_j^{2/3}(\log n_j)^6\rfloor$
starting at a large fixed $n_0$. Fix an initial critical prefix
ending in the middle third of $W(n_0)$, by the cyclic rotation
construction in Theorem S. On each subsequent stage condition the
fresh centered walk to stay in $(0,W(n_j))$ and end in
$(.45W(n_j),.55W(n_j))$. The endpoint is in the middle third
of the next width because $n_{j+1}/n_j\to1$. Thus the first strip
bound applies uniformly at every stage after increasing $n_0$.

At depth $n$, each complete or partial stage meeting the prescribed
prefix costs at most its reciprocal normalizer. Including the last
partial stage in full costs $O((\log n)^6)$ in the logarithm. In
the range $[x,2x]$ the number of stage starts is
$O(1+x^{1/3}/(\log x)^6)$, by their length lower bound there.
Dyadic summation gives $O(n^{1/3}/(\log n)^6)$ stages before $n$.
Moreover, $(W^{-2})'(x)=O(x^{-5/3})$. Over a whole stage starting
at $x$, the absolute error of its left Riemann rectangle for
$\int W^{-2}$ is at most $C L^2x^{-5/3}$. Summing stages in a
dyadic range costs $O((\log(2x))^6)$, and summing the ranges up to
$n$ costs $O((\log n)^7)$. Consequently their total logarithmic
normalizer cost, including the final partial stage, is at most
$$
       \kappa\int_{n_0}^n W(x)^{-2}\,dx+
       O\!\left(n^{1/3}(\log n)^{-6}+(\log n)^7\right).             \tag{E3}
$$

As in Theorem S the probability of a specific depth-$n$ word before
stage conditioning is $e^{-Hn+h d_n}$, where $d_n$ is its terminal
deficit. At fixed native clock and any given ternary residue its
carry lies in a single congruence class modulo $3^n$, and distinct
words have distinct integer carries. All prefixes satisfy
$d_i\le W(n)+O(1)$ up to depth $n$. Thus the number of such words
at this clock and residue is at most
$C n 2^{W(n)-d_n}$, by the exact carry computation in Theorem S.
There are $O(n)$ native clocks. The strict $h>\log2$ absorbs the
overlap exponent into $hW(n)+O(1)$, uniformly in $d_n$.
The resulting pushforward probability $\nu$ satisfies
$$
 \log\sup_y\nu(y+3^n\mathbb Z_3)
 \le -Hn+hW(n)+\kappa\int_{n_0}^n W(x)^{-2}\,dx+
       O\!\left(n^{1/3}(\log n)^{-6}+(\log n)^7\right).             \tag{E4}
$$
The $O(\log n)$ cost of summing clocks and bounding the integer
carry has been included. This estimate applies to every sufficiently
large depth, including depths strictly inside a stage.

## Expansion including the term that decides equality

Put $F(t)=(1+u(t))^{-2}$. Changing variables $x=e^v$ gives
$$
 \int_{n_0}^n W(x)^{-2}\,dx
 =3 f^{-2}n^{1/3}\left(F(t)-3F'(t)+O(t^{-3})\right).
$$
Indeed $F''(t)=O(t^{-3})$, and two integrations by parts reduce
the remainder to $\int^{t}e^{v/3}O(v^{-3})\,dv=O(e^{t/3}t^{-3})$.
The finite lower endpoint is harmless. Since
$F=1-2u+3u^2+O(t^{-3})$ and $F'=-2u'+O(t^{-3})$, using
$3\kappa/f^2=hf/2$ gives
$$
 \frac{hW(n)+\kappa\int_{n_0}^n W^{-2}}{A n^{1/3}}
        =1+u(t)^2+2u'(t)+O(t^{-3})
        =1-\frac1{t^2}-\frac1{t^2(\log t)^2}+O(t^{-3}).           \tag{E5}
$$
In particular the integral uses the width at all earlier times.
Replacing it by $3n^{1/3}/[f(1+u(t))]^2$ would omit the derivative
term and reverse the relevant inequality. Equations (E3)–(E5)
give
$$
 \sup_y\frac{\nu(y+3^n\mathbb Z_3)}{g_1(3^{-n})}
 \le \exp\!\left[-(A+o(1))
        \frac{n^{1/3}}{(\log n)^2(\log\log n)^2}\right]\to0.
$$
The ultrametric mass distribution bound proves infinite $g_1$
measure. The gauges with $b<1$ are larger, proving Theorem E.
