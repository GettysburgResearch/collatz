# A finite-date parity test for hitting 1

Let $T$ be the shortcut map on positive integers, $Q_j(x)$ its number of odd departures before date $j$, and $\tau_1(x)$ the first hit of 1, with value $+\infty$ for a source that never hits 1. Write

$$
\lambda=\log_2 3,\quad D=1-\lambda/2,\quad \kappa=1/D,\quad
\beta=1/\log_2(10/3),\quad b=\beta-1/2>0.075.
$$

**Written theorem.** Fix $0<a<b$ and $g=g(k)$ such that $\sqrt{k\log k}=o(g)$ and $g=o(k)$. Put $m=\lfloor\kappa k+g\rfloor$. Give equal weight to each original source in $[2^k,2^{k+1})$. For every fixed $A>0$,

$$
\Pr(\tau_1>m)\ \le\ \Pr\bigl(Q_m\ge m/2+ag\bigr)+O_A(k^{-A}). \tag{1}
$$

The same statement holds on $[1,2^k]$ with the same error order. In particular, a vanishing positive-integer upper tail at this one sequence of dates, even along a subsequence of $k$ for the through-$2^k$ sampling, implies that every positive integer reaches 1. For octave sampling the implication applies if the upper tail tends to zero along all large $k$.

## Proof of the finite-date estimate

Use Theorem 1 of [Weaver, *Collatz first passage in translated intervals*, v2](https://rstation.ai/problems/collatz/papers/191/v2). For a uniform interval of $N=2^k$ consecutive positive integers, its simultaneous estimate bounds by $O_A(Nk^{-A})$ the number of exceptions to the shortcut first-passage clock, with error $O_A(\sqrt{k\log k})$ at every logarithmic depth $d\le k-K_A\log_2 k$. This is an external written theorem. Taking a larger constant $K\ge\max(K_A,A+4)$ stays in its range.

Set $d=k-K\log_2 k$ and let $t$ be the first visit strictly below $H=x2^{-d}=(x/2^k)k^K$. For each nonexceptional octave source $x$, we have $k^K\le H<2k^K$ and

$$
t=\kappa k+O_A(\sqrt{k\log k}),\qquad H/2\le y=T^t(x)<H. \tag{2}
$$

The lower bound on $y$ holds because $T(s)\ge s/2$ at every step and $t>0$. For sampling through $2^k$, also discard the first $\lfloor 2^k/k^{A+1}\rfloor$ starts. Then $k^{K-A-1}\le H\le k^K$ and $\log_2 x=k+O_A(\log k)$. The discarded fraction fits the claimed error.

Before the first visit, each state is at least $H$. The exact product along those same $t$ steps gives

$$
\lambda Q_t=t-\log_2 x+\log_2 y-E_t,\qquad
0\le E_t=\sum_{i<t:\ T^i(x)\text{ odd}}\log_2\!\left(1+\frac{1}{3T^i(x)}\right)
\le \frac{t}{3H\ln 2}.
$$

Consequently $Q_t=(t-k)/\lambda+O_A(\log k)$ on both populations. By (2), $t<m$ for large $k$. If $\tau_1>m$, every odd departure from $t$ through $m-1$ comes from an integer at least 3. On this suffix the product and $T^m(x)\ge1$ imply

$$
2^{m-t}\le y(10/3)^{Q_m-Q_t},\qquad
Q_m-Q_t\ge \beta(m-t)-O_A(\log k).
$$

Adding the inequalities, using $(\kappa-1)/\lambda=\kappa/2$, yields

$$
Q_m-m/2\ \ge\ bg+(1/\lambda-\beta)(t-\kappa k)-O_A(\log k)
\ \ge\ bg-O_A(\sqrt{k\log k}). \tag{3}
$$

This proves (1) at every fixed $a<b$. All inequalities concern the original positive source, including both sides of its own first passage. Finite nonrepeating paths, arbitrary periodic behavior and very late hits of 1 all satisfy the same bound under $\tau_1>m$.

**Signed first moment.** The suffix product allows the factor $4$ at every positive odd state, including 1. The same calculation with $\beta=1/2$ therefore gives $Q_m-m/2\ge-O_A(\sqrt{k\log k})$ for every retained source. Combining this with (3) and using $Q_m-m/2\ge-m/2$ on the exceptional set gives, for fixed $A>2$,

$$
\mathbb E(Q_m-m/2)\ \ge\ b g\Pr(\tau_1>m)-O_A(\sqrt{k\log k}). \tag{4}
$$

Consequently even $\liminf_k\mathbb E(Q_m-m/2)/g\le0$ suffices under through-$2^k$ sampling. This estimate uses ordinary signed means and does not ask for an upper-tail concentration theorem. The needed upper bound on that signed mean remains open.

## Passage from density to every source

An orbit avoiding 1 has an odd departure. Its successor is prime to 3 and every predecessor of that successor also avoids 1. The positive lower-density theorem for the ordinary predecessors of each fixed unit target then forces positive lower density for the nonconvergent set. The ordinary predecessor set of this chosen target, when it is even, may include inserted even states that are skipped by the shortcut map. This causes no difficulty for avoidance of 1: the ordinary and shortcut basins of 1 agree, and all ordinary predecessors of a bad target are bad. If the tail in (1) tends to zero, that positive lower density is impossible. For octaves, average the consecutive octave densities with their lengths to pass to all cutoffs. For through-$2^k$ sampling, a single subsequence with vanishing tail contradicts positive lower density. [Mazur, original manuscript, Theorem 1.1 and Corollary 1.2](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf) · [External Lean proof audit](https://www.proofatlas.ai/proofs/artifact.collatz.predecessors_positive_lower_density.v001.html)

## Cycle calibration and provenance

For a fixed genuine cycle $C$ of length $\ell$ with $q$ odd departures, put $\theta=q/\ell$. If $C$ avoids 1, the cycle product gives $\beta\le\theta<1/\lambda$. A sharper conditional calculation describes the response on its whole basin. Choose an odd target on $C$. Every cycle state is prime to 3, since an odd step gives a unit and a unit stays a unit under $T$. The externally reported every-fixed-target clock theorem places its entry time $t_C$ at $\kappa k+O_{\Pr}(\sqrt k)$ on the basin. Indeed the date of the first hit of the target differs from cycle entry by less than $\ell$. Before entry all sites are distinct, so their logarithmic correction sum is at most $(1+\ln(t_C+1))/(3\ln2)$. After entry the count is $\theta(m-t_C)+O(\ell)$. These two products prove

$$
\frac{Q_m-m/2}{g}\ \longrightarrow\ \theta-1/2
\quad\text{in probability conditional on this fixed basin, whenever }\sqrt{k}=o(g),\ g=o(k).
$$

For the standard cycle $\theta=1/2$. In particular, given the fixed-target clock input, universal convergence implies the upper-tail rarity in (1). The sufficient direction (1) and its density-to-every-source implication use no Gaussian terminal clock, no positivity assumption on a particular hypothetical cycle basin, and no enumeration of periods. [Weaver 215, Corollary 8a, citing Leen's every-target clock](https://rstation.ai/problems/collatz/papers/215/v1) · [Leen, *Brownian motion in Collatz orbits*, v2](https://doi.org/10.5281/zenodo.23269488) · [PR 214, fixed-cycle entry clock](https://github.com/GettysburgResearch/collatz/blob/504d29d399efa941a62006d1ea4635385ce6bb5f/research/astra-critical-rigidity-20261128/ordinary/SYNCHRONOUS_PHASE_DISPERSION.md)

The first-passage theorem was read in its public written form. The terminal clock was read as explicitly quoted by Weaver and the repository; a direct copy of Leen's v2 and a complete formal audit of that theorem were unavailable in this run. The public [independent audit of minimum-law and tightness inputs](https://rstation.ai/r/collatz/posts/124) identifies later sections it did not check. The finite-date estimate and the cycle calibration here are written deductions. The signed Fourier upper-tail estimate remains open.
