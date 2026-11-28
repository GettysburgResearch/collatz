# The exact clock and original label at a moving first landing

**Source-qualified written local theorem.** Let $B\to\infty$, $v=\log(X/B)\to\infty$, with $v=o(\log B)$. The input is a uniform positive odd integer in $[X,2X)$. Keep the first odd state $y\le B$ and the sum $t$ of the valuations up to that state, so $t$ is the actual shortcut time to this odd landing. Use a cemetery on failure. Full ternary resolution at an exact central sum uses [Weaver and Wren, Paper 48, Theorem 6, (65)–(66)](https://rstation.ai/problems/collatz/papers/48). The stochastic overshoot identification and sampled templates are in [the first-landing profile](LOCAL_LANDING_PROFILE.md). The result also holds for $v\le c\log B$ with a sufficiently small absolute $c>0$ and $v\to\infty$.

Write $D=\log(4/3)$, $P=\log3$, $\sigma^2=2P^2/D^3$, and
\[
 f_v(t)=\frac{1}{\sqrt{2\pi\sigma^2v}}
       \exp\!\left(-\frac{(t-2v/D)^2}{2\sigma^2v}\right),\qquad
 W(r)=P e^r 1_{[0,\log2)}(r)\quad (r\bmod P).
\]
Here $W$ is periodic, its argument is reduced to $[0,P)$, and its circular Haar mean is one. For every $\epsilon>0$ choose a nonnegative fixed interval–ternary template $g$ approximating $G$ sufficiently closely in $L^1$. One then has, for the actual joint probabilities $p(y,t)$,
\[
 \limsup\left[p(\dagger)+\sum_{y\le B\ {\rm odd}}\sum_{t\ge0}
 \left|p(y,t)-\frac2B g(y/B,y)f_v(t)
       W\!\left(t\log2+\log(y/B)-v\right)\right|\right]<\epsilon.       \tag{1}
\]
The limit is along every indicated sequence. The templates can be evaluated at the original labels. Equation (1) permits arbitrary tests of that integer and the exact clock together. The factors include a Gaussian clock envelope, the first-landing density, and the circular phase of the original source octave. In particular the exact clock and the label do retain a common phase even when the unmarked label law has equilibrated.

For each fixed real $c$, compare these joint laws from the two source octaves with logarithmic separations $v$ and $v+c$, using the same $B$ and the same clock origin. With probability-convention variation distance,
\[
       \lim\|p_{v,B}-p_{v+c,B}\|_{\rm TV}
             =\tfrac12\int_{\mathbb R/P\mathbb Z}|W(r)-W(r-c)|\,dm_P(r).
                                                                         \tag{2}
\]
Thus powers of three in the input scale have vanishing joint discrepancy in this range. Formula (2) is for first arrival at a growing height. Earlier real/clock profiles include Leen's fixed-target stopping-time teeth, PR145's critical source and fixed-basin clocks, and PR215's late full-endpoint comparison on separated source windows. The preservation of a source Mellin phase is the ordinary affine identity. Here it is also sufficient for the limiting comparison of **simultaneous exact landing clocks and all physical labels** in the mesoscopic source range. [Leen, stopping-time histogram](https://doi.org/10.5281/zenodo.23252397) · [Earlier clock sources and scope](ORDINARY_PRODUCT_TRANSITION.md) · [PR215, separated late endpoint shells](https://github.com/GettysburgResearch/collatz/blob/6758aa3e72a27882c1ee41e75bf84b0b57b7c025/research/astra-nine-hour-20261128/escape/phase3/SEPARATED_SOURCE_SHELLS.md).

## The ternary law at an exact total and a maximum-multiplier cap

Use inverse-order iid positive geometric gaps. At grade $j$ put $D_j=\sum_{i\le j}E_i$, $A_i=3^i2^{-D_i}$, $K_j=\max_{1\le i\le j}A_i$, $Z_j=\sum_{i\le j}A_i/3\bmod3^j$. For $0<u\le1$, let
\[
 H_{j,t,u}(z)=3^j\Pr(D_j=t,Z_j=z\bmod3^j,K_j<u),\qquad
 b_j(t)=\binom{t-1}{j-1}2^{-t}\quad(t\ge j\ge1).
\]
For every $0<\delta<1$ and each fixed $M$,
\[
  \sup_{\substack{\delta\le u\le1\\ |t-2j|\le M\sqrt j}}
      \left\|H_{j,t,u}/b_j(t)-h_u\right\|_{L^1(\mathbb Z_3)}\to0,       \tag{3}
\]
where $h_u$ is the density of the stationary phase with its entire maximum multiplier $K<u$, so $h_u=D uG(u,\cdot)$ for almost every $u$. Strict caps are retained at every truncation.

First remove the cap and denote the corresponding full-depth density by $R_{j,t}$. Project onto the first $m=\lfloor j^{1/8}\rfloor$ trits. By the joint oscillation bound (66) cited above with $K=0$ in its notation, the $L^1$ projection error at any one total is at most $C_A m^{-A}$. On the central windows in (3), $b_j(t)\gg_M j^{-1/2}$. The first $m$ trits are determined by the first $m$ letters. Conditional on them, the relative total weight is $b_{j-m}(t-D_m)/b_j(t)$. This tends to one uniformly for $D_m\le4m$ and central $t$, by the ordinary local central limit estimate for the negative binomial probabilities (equivalently by Stirling on the displayed formula). The difference on $D_m>4m$ is $O_M((1+\sqrt j)e^{-cm})$ after summing the prefix law. The unconditioned coarse phase density is $\rho_m$, which tends to the stationary ternary density $\rho$ in $L^1$ by Tao, Proposition 1.14. Together these facts give
\[
      \sup_{|t-2j|\le M\sqrt j}\|R_{j,t}/b_j(t)-\rho\|_1\to0.           \tag{4}
\]
All norms here use probability Haar measure; (66) uses the equivalent sum of absolute differences of the corresponding masses. [Tao, Proposition 1.14](https://doi.org/10.1017/fmp.2022.8).

Freeze $K_j<u$ after the first $m$ letters. For $0<s<1$ one has $r_s=\mathbb E A_1^s=3^s/(2^{1+s}-1)<1$, so the probability that any $A_i\ge\delta$ at $i>m$ is $O_\delta(r_s^m)$. At one exact central total divide this error by $b_j(t)$. On a frozen prefix $w$ of total $d\le4m$, the suffix has its ordinary density $R_{j-m,t-d}$ pushed forward by the fixed ternary word map, with scalar prefix probability $2^{-d}$. Replace the suffix by $b_j(t)\rho$: (4), the central total ratio just proved, and preservation of the mass norm by an injective ternary affine pushforward give total error $o(b_j(t))$, uniformly in $u$. Remove the exponentially rare $d>4m$, with the previous $\sqrt j$ allowance. Restoring the infinite cap after mixing costs $O_\delta(r_s^m)$. This proves (3).

## The source interval selects one odd grade

For fixed $v$ in the fresh word model start the scaled real source at $e^v V$ with $V$ uniform on $[1,2]$, independent of the gaps and an initial Haar ternary state. A word at grade $j$, total $t$, has slope $A=3^j2^{-t}$. With $u=y/B$ the complete first-crossing condition in this multiplicative model is
\[
           0<u\le1,\qquad K_j<u,\qquad
           0\le r:=t\log2-jP+\log u-v<\log2 .                        \tag{5}
\]
Here the suffix maxima are read in inverse order. Boundary equalities in the continuum variable have measure zero. The joint density at $j,t$ on $(u,z)$ is exactly $e^rH_{j,t,u}(z)/u$ on the window for $r$, and zero elsewhere. Indeed $3^j2^{-t}=A$ is the density contribution per word at fixed total and eligible ternary phase, while the template coefficient per word in the fresh model is $e^{-v}$ before summing those indicators. Their ratio is $e^{-v}/A=e^r/u$. For each $t,u$ at most one integer $j$ obeys (5), because the window width $\log2$ is smaller than $P$. For fixed $j,u$, at most one integer $t$ does, by the half-open endpoints and the spacing $\log2$.

Restrict temporarily to $\delta\le u\le1$ and $|j-v/D|\le M\sqrt v$. The admissible $t$ are central in (3), with a bound depending only on $M,\delta$. Summing the $L^1$ approximation (3) over these cells costs $o_{M,\delta}(1)$: at fixed $u$ there are $O_M(\sqrt v)$ grades and at most one $t$ per grade, $b_j(t)\ll_M v^{-1/2}$, and $e^r/u\le2/\delta$. After replacing $H$ by $b_j(t)D u G$, the density is $D e^r b_j(t)G(u,z)$. The clock relation gives
\[
             t-2j=(2v-Dt)/P+O_\delta(1),\qquad j=v/D+O_M(\sqrt v).
\]
The negative-binomial local central limit estimate thus yields $b_j(t)=(P/D) f_v(t)+o_{M,\delta}(v^{-1/2})$ uniformly here. Summing gives the asserted product $G(u,z) f_v(t)W(t\log2+\log u-v)$ in the continuum variables, on the retained cells.

The omitted part can be made uniformly small. The multiplicative model's real crossing has $j$ within $M\sqrt v$ of $v/D$ except with probability $O(M^{-2})+o(1)$. Indeed its chronological forward levels are sums of the iid centered fluctuations around drift $D$, crossing $v+\log V$. An early crossing requires a maximal centered fluctuation of order $M\sqrt v$; use Kolmogorov's maximal inequality up to the proposed early time. A late crossing requires a one-time negative fluctuation of that order, bounded by Chebyshev's inequality. The model's unmarked real output converges to the $G$ marginal by the template and Palm result, so its mass at $u<\delta$ is $O(\delta)+o(1)$ using the bounded real marginal. Conversely the predicted term has mass at $u<\delta$ at most $O(\delta)$, since $W$ is bounded and $\sum_t f_v(t)=1+o(1)$. For $u\ge\delta$ and an admissible grade outside the retained window, (5) forces $|t-2v/D|\gg M\sqrt v$ after a constant adjustment of $M$, so Gaussian tails exhaust the predicted mass. Increasing $M$, then decreasing $\delta$, proves the continuum comparison in sum norm over all dates.

## Transferring the estimate to every actual label

Choose a fixed bounded interval–ternary template $g$ such that $\|g-G\|_1$ is arbitrarily small. Replacing $G$ by $g$ in the predicted continuum sum over $t$ costs $O(\|g-G\|_1)$ by bounded $W$ and the uniform bound on $\sum_t f_v(t)$. To pass to ordinary source counts, truncate their words at $L=\lceil C_0v\rceil$ and total $4L$ as in [the growing-phase count](GROWING_LANDING_PHASES.md). Take $C_0$ sufficiently large for the central grades and typical totals. The omitted actual probability is $O(e^{-cv}+B^{-c})$. At any specified target, each compatible word gives one source if its deformed interval conditions hold. Replacing these intervals by (5), on each original word, changes only $O(1)$ compatible targets: the largest endpoint displacement before division by $B$ is $(3/2)^j$ and eligible odd targets are spaced by $2\,3^j$. Summing the result over every word, with its exact date still attached, and correcting the fresh octave normalization costs $O((2^{4L}+1)e^{-v}/B)$. The retained original probabilities are thus approximated in full sum norm by the grid sample of the finite continuum word densities.

Here the $L^1$ bound for continuum density differences can itself be sampled, without assigning arbitrary point values to $G$. On $u\ge\delta$ for retained $j,t$, the possible changes in $K_j<u$ are among $O(L^2)$ fixed numbers $3^i2^{-d}$ ($1\le i\le j$, $d\le t$). Add the finitely many endpoints of $g$, the endpoints of (5), and the cutoff $\delta$. On each resulting interval and each ternary class modulo $3^{\max(j,m_g)}$, where $m_g$ is the template depth, the finite actual-word density is constant because $e^r/u=e^{t\log2-jP-v}$ is constant. The predicted $g f_v W$ is linear in $u$ on its admissible interval for that grade. Their absolute difference is monotone on at most two subintervals there and has supremum $O_{g,\delta}(3^j+1)$. The ordinary sample averaged at weight $2/B$ differs from the Lebesgue–Haar integral by $O(B^{-1})$ times that supremum for each such progression and monotone subinterval, by interval counting and partial summation. Summing all central $(j,t)$, intervals and classes gives $O_{g,\delta}(e^{C v}/B)$ with absolute $C$. This tends to zero in the stated range after the absolute source exponent is chosen small enough. At the cutoffs, equality on a grid point is included in the same endpoint allowance.

For the omitted actual mass, grid samples of whole retained word intervals agree in total with the uncorrected model up to $O(2^{4L}e^{-v}/B)$, by that same progression count word by word. This handles the complement of the central grade window and $u<\delta$ after splitting each interval at $\delta$. The predicted grid mass with $u<\delta$ is bounded by $O(1)\,(2/B)\sum_{y/B<\delta}g(y/B,y)$, tending to $O(\int_{u<\delta}g)$; its complementary central-date tails above $\delta$ use the same Gaussian bound as before, irrespective of fine ternary phase. A possible nonpositive grade selected by (5) in the prediction is included in those tails. This proves (1).

## Comparing two source scales and the clock-phase obstruction

For any bounded periodic piecewise continuous $F$ with finitely many jumps, Gaussian averaging gives
\[
         \sum_{t\ge0} f_v(t) F(t\log2+\theta)
               \longrightarrow \int F\,dm_P
                  \qquad\text{uniformly in }\theta.                   \tag{6}
\]
The nonconstant Fourier modes have uniformly bounded partial sums because $\log2/P$ is irrational. Summation by parts against $f_v$, whose total variation tends to zero, handles each mode. Continuous majorants and minorants with arbitrarily close circular integrals handle the jumps uniformly after rotation. The missing negative Gaussian tail tends to zero. In (1) use the same template for both sources; $\sum_t|f_{v+c}(t)-f_v(t)|=o(1)$ for fixed $c$, by their explicit scales and means. Now (6) with $F=|W(r)-W(r-c)|$ yields the right side of (2), multiplied before taking the template limit by $(2/B)\sum_y g(y/B,y)\to\int g$. Let the template errors tend to zero; $\int G=1$. This proves (2).

At any actual first arrival, writing $b$ for its product of $3x/(3x+1)$, the exact identity is $t\log2+\log y\equiv\log x-\log b\pmod P$. The simple-path reciprocal tail gives $-\log b=O(B^{-\kappa})$ on all such paths, including ones taking longer than the central window. Thus separated wrapped log-source intervals remain identifiable from the joint clock and label at high floors. In particular coupling the first-landing **labels** alone does not supply equal-clock coupling needed for the late endpoint or escaping-ray question. The joint local theorem above has a mesoscopic separation hypothesis; no unrestricted-clock estimate at arbitrary $X/B$ is inferred from the unmarked relative passage law.
