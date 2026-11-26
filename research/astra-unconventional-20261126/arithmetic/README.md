# Joint binary and ternary windows on one ordinary candidate cycle

**Proposed written theorem.** On the bounded least-tripling-disagreement branch, every polynomial-length chronological interval of odd phases has asymptotically uniform joint binary and ternary digit windows in the integer mantissas. The two depths can be chosen independently anywhere in the interior of the natural height range. Their product may exceed the height. For the original odd integers every subsequential joint law has density at most three. The theorem applies to every admissible octave assignment of a putative ordinary cycle. It provides no contradiction at the bottom binary or ternary digits and leaves full-denominator exclusion open.

The [inverse-curve spacing argument](INVERSE_WRAP.md) obtains the stronger physical lower bound $s\gg p^{1000/479+1/3}$ on the ordinary minimum and a separate pointwise lower bound on the complete reduced denominator.

## Ordinary states, ranks and the conclusion

Use accelerated odd phases $x_j$, with $2^{a_j}x_{j+1}=3x_j+1$, $a_j\in\{1,2\}$, and take the temporal index cyclically modulo its primitive period $p$. Write $h=\sum a_j$ and $s=\min x_j$. The bounded least-disagreement alternative gives $x_j<8s$. Let $k_j\in\{0,1,2\}$ put $z_j=2^{-k_j}x_j$ in $[s,2s)$, and define the **integer** $Z_j=4z_j=2^{2-k_j}x_j$. In increasing order of $z$, the rank of temporal phase $j$, starting at the minimum, is $R_j=jh\bmod p$. Thus $b_j=\lfloor(R_j+h)/p\rfloor=a_j+k_{j+1}-k_j$ and
$$
  2^{b_j} Z_{j+1}=3 Z_j+c_j,\qquad c_j=2^{2-k_j}.
$$
The rank theorem follows from quarter-integer spacing, the order of $3z+2^{-k}$, and the unique dyadic fold at the top of the octave. In this branch $s$ lies between fixed positive powers of $p$, and $h/p=\log_2 3+O(1/s)$. In particular there exist absolute $B,\kappa>0$ with $p^\kappa\ll s\ll p^B$. The proof below only needs these weaker bounds, the rank rotation and the literal affine equations. [Pinned cycle-order proof and height interfaces](https://github.com/GettysburgResearch/collatz/blob/f192322f70073ba44bc9f98785a51c27a4da9ee5/research/astra-global-closure-20261124/round9/critical/README.md) · [Pinned upper and lower height exponents](https://github.com/GettysburgResearch/collatz/blob/f192322f70073ba44bc9f98785a51c27a4da9ee5/research/astra-global-closure-20261124/round10/arithmetic/README.md)

Fix $\epsilon,\theta>0$, with $0<\theta\le1$. In every chronological interval $I$ of at least $p^\theta$ and at most $p$ successive phases, and simultaneously for every pair of powers
$$
        p^\epsilon \le q=2^a,\ r=3^b \le s/p^\epsilon ,
$$
the empirical probability measures of $(\{Z_j/q\},\{Z_j/r\})$, $j\in I$, converge weakly to Haar probability on the two-torus as $p\to\infty$. Both denominators separately obey both bounds. Uniformity means that any choices of the periods, intervals, admissible masks and depths in this statement have the indicated limit. The highest fixed number of digits of each residue therefore realize every prescribed joint block with its Haar frequency. These are fixed depths for a single orbit and a single time interval. The two digit arrays are read at the same physical phase.

## Freezing a short chronological interval

Put $\rho=2^{1/p}$, $L_0=\rho^h$, and $A_j=Z_j\rho^{-R_j}$. The product of the actual positive odd steps gives
$$
     L_0^p=2^h=\prod_{j<p}(3+1/x_j),\qquad 3<L_0\le 3+1/s.
$$
In particular $2s<A_j\le8s$, and
$$
           L_0 A_{j+1}=3 A_j+c_j\rho^{-R_j}.
$$
The last summand lies in $[0,4]$, and $(L_0-3)A_j\in[0,8]$. Hence $|A_{j+1}-A_j|\le8/3$. On any interval of $M$ successive phases beginning at $i$,
$$
          Z_j=A_i 2^{R_j/p}+O(M)
          \tag{1}
$$
uniformly across all seams. The chronological bound allows $M$ to be a small power of $p$ even when the selected digit moduli are much smaller than $p$. The integer folding, exact real amplitude recurrence and finite telescoping estimate are [verified in Lean](FrozenAmplitude.lean).

## Oscillation on a short piece of the rational rotation

Let $\alpha=\log_2 3$, $\gamma=h/p$, and $e(t)=\exp(2\pi i t)$. Fix $m,\sigma,C>0$. On any interval of $M=\lfloor p^m\rfloor$ clocks, uniformly in the initial angle and $p^\sigma\le |V|\le p^C$,
$$
          \frac1M\sum_{j=0}^{M-1}e\big(V\,2^{\{y+j\gamma\}}\big)=o(1).
          \tag{2}
$$
Here $|\gamma-\alpha|\ll p^{-\kappa}$. A fixed two-logarithm bound gives constants $D\ge1,c>0$ such that $\|t\alpha\|\ge c t^{-D}$ for every positive integer $t$. It applies to the nonzero form $t\log3-n\log2$ with $n$ the nearest integer to $t\alpha$. [Matveev, homogeneous rational linear forms in logarithms, Part II, §2](https://doi.org/10.1070/IM2000v064n06ABEH000314)

Choose a fixed small $v>0$ with $(D+1)v<\min(m,\kappa)$. By Dirichlet's box argument there is $1\le t\le p^v$ for which $\beta=\|t\gamma\|\ll p^{-v}$. The preceding lower bound, after subtracting $O(t p^{-\kappa})$, gives $\beta\gg p^{-Dv}$. Split the clock interval by its index modulo $t$. Within each progression the angle changes by $+\beta$ or $-\beta$ until it wraps. Discard only the two incomplete end traversals on each progression, a total of $O(t/\beta+t)=o(M)$ clocks. Each remaining monotone traversal has $N=\beta^{-1}+O(1)$ sample points, so $p^v\ll N\ll p^{Dv}$.

On a traversal the phase function, up to reversing the index or conjugating, is $f(u)=|V|2^{y_0+\beta u}$ on $N$ consecutive integers, with its argument in a bounded interval. Choose one fixed integer $d\ge3$ with $dv>C+1$. Then $f^{(d)}\asymp |V|\beta^d=\lambda$, with implied constants depending only on $d$, and
$$
    \lambda\ll p^{-1},\qquad \lambda N^d\asymp |V|\ge p^\sigma,\qquad N\gg p^v.
$$
The classical $d$-th derivative bound in the form of Arias de Reyna's displayed theorem bounds the normalized sum, up to $d$-dependent constants, by the maximum of $N^{-2/2^d}$, $\lambda^{1/(2^d-2)}$ and $(\lambda N^d)^{-2/2^d}$. Each term saves a fixed power of $p$. Summing completed traversals and adding the discarded ends proves (2), in fact with a power saving depending on $m,\sigma,C,\kappa,D$. [J. Arias de Reyna, explicit derivative estimate, theorem on p. 1](https://arxiv.org/abs/2407.02094)

## The joint Fourier characters

Fix a nonzero $(u,w)\in\mathbb Z^2$. Set $T=u/q+w/r$. The bound $T=O_{u,w}(p^{-\epsilon})$ follows at once. Also
$$
         s|T|\gg_{u,w} p^\epsilon\,(\log p)^{-C_{u,w}}.       \tag{3}
$$
If one term vanishes or their signs agree or their absolute ratio is outside $[1/2,2]$, this follows from the larger term. In the cancellation case use the linear form
$$
             b\log3-a\log2+\log(|u|/|w|).
$$
It is nonzero for large $p$ by the valuation at 2, since $a\to\infty$. If $|u|=|w|$, omit the zero logarithm. Matveev's bound for the fixed positive rationals and $a,b=O(\log p)$ gives an inverse power of $\log p$. On the comparable range $|e^\ell-1|\asymp|\ell|$ for this form $\ell$, proving (3). Multiplying either denominator by an arbitrary fixed positive integer preserves the estimate, by absorbing the multiplier into the fixed characters after a common rescaling.

Choose $0<m<\min(\theta,\epsilon)$. Divide $I$ into intervals of length $\lfloor p^m\rfloor$, discarding an $o(1)$ proportion. In each subinterval (1) changes $e(TZ_j)$ by $O(p^m |T|)=o(1)$. Its main term is (2) with $V=TA_i$, which is between $p^{\epsilon/2}$ and $p^{O(1)}$ in absolute value by (3). This kills every nontrivial fixed character uniformly. Trigonometric polynomial approximation gives the stated Haar law, also for rectangles whose boundaries have Haar measure zero.

For the literal odd phases use the just-proved law at $(4q,4r)$ for $Z$. Equivalently $Y_j=(\{z_j/q\},\{z_j/r\})$ has Haar limit. The observed odd window is $M_{2^{k_j}}Y_j$, with $M_t(y_1,y_2)=(ty_1,ty_2)$ on the torus. On every subsequence, take further weak limits $\nu_k$ of the subprobabilities marked by $k_j=k$. They sum to Haar, so $0\le\nu_k\le\mathrm{Haar}$. Each $M_{2^k}$ preserves Haar. Thus every joint weak limit of the original odd window measures is bounded above by $3\,\mathrm{Haar}$. For example the two original windows lie simultaneously in $[0,\delta)^2$ on at least $\delta^2/16-o(1)$ of the interval for fixed $0<\delta<1$, since $Y_j\in[0,\delta/4)^2$ works for every band.

## The arithmetic gate

The theorem keeps the common positive integer and the common temporal phase in both positions. It excludes a concentration in a fixed small region at any of the specified pairs of depths. It leaves the finely scattered residue classes of an inverse ternary word or a forward binary word possible within those windows. The full cycle condition at an odd cut remains
$$
    (2^h-3^p)x_0=\sum_{j=0}^{p-1} 3^{p-1-j}2^{a_0+\cdots+a_{j-1}}.
$$
A proof that admissible cylinders on the same realized phases must violate the window law, or that their all-cut full-divisor cancellation is impossible, is missing. Haar limits at arbitrarily small positive fractions of the logarithmic height do not give Haar law at the single bottom trit: every $Z_j$ on an ordinary cycle is a ternary unit. The Furstenberg intersection theorem for invariant closed subsets of the circle and the separate binary-window measure-invariance argument do not supply this transfer. [M. Wu, Annals of Mathematics (2019)](https://annals.math.princeton.edu/2019/189-3/p02) · [rStation paper 170, binary windows averaged over heights and times](https://rstation.ai/problems/collatz/papers/170)

[Replay record and verification scope](../../../reports/astra-unconventional-20261126/arithmetic/VERIFICATION.md)
