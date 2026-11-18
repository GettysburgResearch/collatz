# A Gaussian transition for the distortion of a finite ordinary orbit

**Proposed, source-qualified.** Let $U(x)=(3x+1)/2^{v_2(3x+1)}$ on the positive odd integers and draw $n$ uniformly from the odd integers in $[X/2,X]$. After $q$ odd steps compute
$$
 V_q(n)=\prod_{i=0}^{q-1}\left(1+\frac{1}{3U^i(n)}\right)^{-1},\qquad V_0=1 .
$$
This is the exact rational number $n3^q/(2^{A_q}U^qn)$, where $A_q$ is the sum of the first $q$ valuations. Put $d=\log(4/3)$ and $\sigma_J^2=2(\log 2)^2/d^3$. At depth
$$
 q_X(s)=\max\{0,\lfloor d^{-1}\log X+s\sigma_J\sqrt{\log X}\rfloor\}
$$
the finite product has a limiting law
$$
 (1-\Phi(s))\,\delta_1+\Phi(s)\,\mathcal L(W).
 \tag{1}
$$
Here $\Phi$ is the standard Gaussian distribution function. The variable $W$ is the limiting natural-source whole-orbit reciprocal distortion. It vanishes on periodic basins. On an escaping orbit it is bounded below by an absolute positive constant. In particular, for each fixed real $s$,
$$
 \lim_{X\to\infty}\mathbb E V_{q_X(s)}
 =1-\Phi(s)+\frac{\Phi(s)}{\delta}\,\mathcal E,
 \qquad \delta=d/2,\qquad
 \mathcal E=\sum_{\text{escaping components }C}(3/2)H_C .
 \tag{2}
$$
Thus a single computable sequence of forward products measures the same total escape mass as the [signed inverse harmonic sum](SIGNED_MASS.md). At $s=0$ its limiting mean is at least $1/2$, with equality exactly when every positive orbit is eventually periodic. No effective bound on the difference between a finite empirical mean and its limit is obtained.

## The limiting jump

Write $m$ for the global orbit minimum, $J_*$ for its first odd clock and $R_*$ for the sum of $\log_2(1+1/(3u))$ before that first visit. Write $r(t)=\lim_{j\to\infty}V_j(t)$, with $r(t)=0$ if $t$ belongs to a periodic basin. The limiting natural terminal pair $(M,R)$ gives $W=2^{-R}r(M)$. Leen's joint terminal theorem gives
$$
 \left(\frac{J_* -(\log X)/d}{\sigma_J\sqrt{\log X}},m,R_*\right)
 \ \Longrightarrow\ (G,M,R),
$$
with $G$ standard Gaussian independent of $(M,R)$. The odd-clock variance follows either from his Syracuse clock formula or the exact relation between the shortcut clock and odd count. For the shell one can difference the cumulative laws at $X$ and $X/2$. For the odd subsample strip the even starts, whose $(J_*,m,R_*)$ is identical to that of their halved inputs. Fixed multiplicative changes of cutoff alter the center by $O(1)$ and give the same normalization. The finite cells of the discrete $M$ and its tightness justify applying the map $(t,v)\mapsto 2^{-v}r(t)$, whether or not $r(t)$ is effectively known. [Leen, terminal data and clock dictionary](https://doi.org/10.5281/zenodo.23252395)

Fix an integer $B$. The largest first-minimum clock among odd starts at most $B$ is a finite number $K_B$. If $J_*-q>K_B$, then every state up to $q$ exceeds $B$. These states form a simple prefix, so $1-V_q$ is at most the uniform reciprocal tail above $B$, which tends to zero. In the other direction, if $m\le B$ and $q\ge J_*+K$, exact factorization gives
$$
 |V_q-2^{-R_*}r(m)|\le\max_{t\le B,\ t\ {\rm odd}}|V_K(t)-r(t)|\longrightarrow0\quad(K\to\infty).
$$
On periodic basins each complete lap contributes a fixed product strictly less than one. Simple escaping orbits have uniformly bounded reciprocal sum, giving their positive lower bound on $V_\infty$. The probability of the remaining bounded clock strip around $q_X(s)$ vanishes by the continuous Gaussian limit. First enlarge $B$, then choose $K$ for that finite set and let $X$ tend to infinity. The arguments apply jointly at any finitely many $s$. They give the common random step $1$ for $s<G$ and $W$ for $s\ge G$. [Uniform reciprocal tail and prior packing estimates](../critical-orbit-mellin/PRIOR_WORK.md)

On every compact time interval the paths are bounded and nonincreasing. Finite-dimensional convergence at every deterministic continuity point, including both endpoints, therefore gives scalar Skorokhod $M_1$ convergence to that random step. Equivalently the completed graphs allow the microscopic decreases within the shrinking transition window to traverse a single vertical segment. The stronger $J_1$ convergence fails on any nondegenerate interval. Each prelimit jump has size at most $1/4$, whereas $M=1$ has positive probability and gives a jump of size one whenever $G$ lies inside the interval. Uniform convergence after a time change cannot create that jump. [Whitt, *Stochastic-Process Limits*, chapter 12](https://doi.org/10.1007/b97457)

Boundedness gives convergence of the means. Partial summation identifies the limiting mean of $W$ with its normalized odd logarithmic mean. Valbuena's component formula and the [whole-orbit identification of the offset law](../critical-orbit-mellin/HARMONIC_OFFSET_CONE.md) give $\delta\mathbb EW=\mathcal E$. Formula (2) follows. Monotonicity also yields the outer limits for any $s_X\to-\infty$ or $s_X\to+\infty$, namely mean one or $\mathcal E/\delta$, respectively.

## Distinguishing the two obstructions

At the same finite clock one can record which of three events has occurred: the path has reached 1, it has repeated a state on some other cycle, or neither certificate has occurred. Write $p_1,p_{\rm other},p_{\rm esc}$ for the natural masses of these three ultimate fates. They exist because the fate is determined by the terminal minimum and its law is tight. The three limiting probabilities are
$$
 \Phi(s)p_1,\qquad \Phi(s)p_{\rm other},\qquad
 1-\Phi(s)(p_1+p_{\rm other}).
$$
A completed certificate implies $q\ge J_*$, since any repeated state entails an entire cycle and the orbit has already attained its minimum. Once the minimum is reached, the delay to either available certificate is uniformly bounded over the finite set of minima at most $B$. The shrinking-strip argument applies again. At each fixed $s$, the limiting frequency of arrivals at 1 is $\Phi(s)$ exactly when every positive integer reaches 1. Indeed any other component has positive natural mass: advancing a possible odd nonunit once gives a unit, whose predecessor basin has positive density. The basin clock of 1 and its conditional Gaussian law are prior results of Leen. The weighted forward observable in (2) separately identifies the contribution from escape. [Published basin clock and stopping-time histogram](https://doi.org/10.5281/zenodo.23252397) · [Predecessor lower bound](https://rstation.ai/problems/collatz/papers/12/v1)

## Finite arithmetic replay

The largest shell checked was $X=2^{22}$, with all 1,048,576 odd starts in $[2^{21},2^{22}]$. Each mean below is enclosed by summing the rational identity for $V_q$ with directed integer rounding. At $s=0$ exactly 564,031 starts had reached 1 by the cutoff. The finite mean can lie below the asymptotic Gaussian baseline.

| $s$ | Odd steps | Lower mean | Upper mean | Reached 1 by cutoff |
|---:|---:|---:|---:|---:|
| −2 | 3 | 0.999995 | 0.999996 | 17 |
| −1 | 28 | 0.882317 | 0.882318 | 160,516 |
| 0 | 53 | 0.499505 | 0.499506 | 564,031 |
| 1 | 77 | 0.184510 | 0.184511 | 887,055 |
| 2 | 102 | 0.038942 | 0.038943 | 1,015,422 |

The [finite-shell replay](check_distortion_cutoff.py) covers the smaller powers 10, 14 and 18 by default and accepts 22 as an argument. The large case is small enough to reproduce without auxiliary data files.

## The logarithm resolves the eventual cycle

The finite product itself vanishes after sufficiently many laps on any periodic basin. Taking its logarithm before passing to the limit recovers the average correction per odd step. For a positive odd cycle $C$ of period $d_C$, set
$$
 \lambda_C=d_C^{-1}\sum_{u\in C}\log(1+1/(3u))
          =d_C^{-1}\log(1/J_C).
$$
Set $\lambda=0$ on escaping basins. The variable $\Lambda=\lambda(M)$ is determined by the eventual fate of the limiting minimum. In particular $\lambda_{\{1\}}=d=\log(4/3)$. On every nontrivial cycle all the odd inputs are at least three, so $\lambda_C\le\log(10/9)<d$.

For every fixed $T>1/d$ and every finite list of real $s$, jointly with the terminal clock and minimum,
$$
 \frac{-\log V_{\lfloor T\log X\rfloor}}{\log X}\ \Longrightarrow\ (T-1/d)\Lambda,
 \qquad
 \frac{-\log V_{q_X(s)}}{\sigma_J\sqrt{\log X}}\ \Longrightarrow\ (s-G)_+\Lambda .
$$
Indeed the preminimum log product is uniformly bounded by simple-path reciprocal summability. After the first minimum $m$, the log product over $j$ additional steps is $j\lambda(m)+O_m(1)$ on a cyclic basin, by decomposing a finite transient and whole laps. The same estimate with $\lambda(m)=0$ holds for a simple escaping tail. Therefore, on $m\le B$, $-\log V_q=(q-J_*)_+\lambda(m)+O_B(1)$ uniformly in $q$ and in the input. The Gaussian clock, independence and tightness of $m$ give the two assertions.

In particular choose $T=2/d$. The single finite observable $Z_X=-\log V_{\lfloor 2\log X/d\rfloor}/\log X$ has limiting law $\Lambda/d$. It is bounded by two, since every odd factor contributes at most $d$. Its limiting mean lies in $[0,1]$, and
$$
 (1-p_1)\left(1-\frac{\log(10/9)}{d}\right)
 \le 1-\lim_X \mathbb E Z_X\le 1-p_1 .
$$
Thus its limiting mean equals **one exactly when all positive integers reach 1**. This is a forward finite-clock version of the two-obstruction question and requires no cycle classification to calculate the observable. A nonempty offending component has positive density by the predecessor lower bound. The formula supplies no bound forcing that limiting mean to one. In the [period-averaged endpoint coefficient](../critical-orbit-mellin/CYCLE_ENDPOINT_MEAN.md), the same $\lambda_C$ instead appears through its reciprocal weighted by the basin probability.

The [replay's logarithmic mode](check_distortion_cutoff.py) gives $1.009685\le\mathbb E Z_X\le1.009686$ for the same $X=2^{22}$ shell at $q=106$. Exactly 1,024,279 of the 1,048,576 odd starts reached 1 by that clock. The bound of one in this section concerns the limiting mean; a finite shell can exceed it.
