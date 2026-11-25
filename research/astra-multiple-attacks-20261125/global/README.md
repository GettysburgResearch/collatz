# Additive Fourier cancellation for ordinary Collatz basin marks

**PROPOSED, source-qualified written theorem. Universal termination remains OPEN.** Fix the ordinary shortcut map $T(2n)=n, T(2n+1)=3n+2$. Under the cited adjacent-merger estimate, the actual bad indicator and every fixed positive odd target's visit indicator are Fourier-uniform after subtracting their current row mean. There is a power saving in the logarithm, uniformly at every additive frequency, including frequencies changing with the row. As a consequence, any three prescribed positive odd targets prime to three occur on the three actual orbits of $x,y,x+y$ for a positive proportion of pairs. A near-diagonal version fails for the explicit targets $5,5,85$.

## The estimate and its arithmetic inputs

Let $b:\mathbb N\to\{0,1\}$, set $b(0)=0$, and assume $b(2n)=b(n)$, with at most finitely many exceptional edges $b(2n+1)\ne b(3n+2)$. Write

$$
 V(B)=\sum_{0\le n<B}|b(n+1)-b(n)|,\qquad
 p_N=N^{-1}\sum_{0\le n<N}b(n),\qquad e(t)=\exp(2\pi i t).
$$

The following deduction assumes $V(B)\ll B/\sqrt{\log B}$ as $B\to\infty$. For sufficiently large $N$, all intervals $I\subset[0,1]$, and every real $t$,

$$
 \left|\sum_{0\le n<N,\ n/N\in I}(b(n)-p_N)e(nt)\right|
 \ll_b N(\log N)^{-1/96}.                                      \tag{1}
$$

At zero frequency the right side improves to $O_b(N(\log N)^{-1/16})$. Either choice of endpoints changes the sum by at most two. Both bounds also hold with triangular weight $1-n/N$ by summation by parts. The estimates use the measured $p_N$ on each row, without any rate for convergence to a limiting density.

For a mark invariant above a fixed height, the imported bound on $V$ follows from the counted-merger estimate with gap one. On $[X,2X)$ take $h=\lfloor(\log_2 X)/2\rfloor$. The original shortcut paths have values at least $X/2^h$ through that time. Every merger already equates the marks there. Each complete binary period of length $2^h$ has exceptional fraction $O(1/\sqrt h)$, and the last incomplete piece costs at most $2^h$. Summing octaves gives the claimed bound, including for a fixed odd target's visit mark, which can fail invariance only on its own outgoing edge. Doubling remains exact for that mark. We use the written finite-cylinder estimate as an external input. [Leen, *Exact rates in Collatz synchronization*, Theorem 2.11](https://doi.org/10.5281/zenodo.23268751) · [Complete-block statement and attribution, equation (1)](https://rstation.ai/problems/collatz/papers/13) · [Repository finite-block application at f431078244e868dc699fad011044f0d5e7f76437](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md)

### Dilation on real rows

Set $f(x)=b(\lfloor Nx\rfloor)$ for $x\ge0$ and $L=\log N$. For $q=2,3$ and any fixed $B>0$,

$$
 \int_0^B |f(qx)-f(x)|\,dx\ll_{B,b}L^{-1/2}.                    \tag{2}
$$

Indeed, inside a parent cell the comparisons are $b(qn+r),b(n)$, $0\le r<q$. Binary mismatches use the edge $2n,2n+1$. For $q=3$, pass from $b(n)=b(2n)$ through $b(2n+1)$, the possible defect to $b(3n+2)$, and at most two neighboring edges back to $b(3n+r)$. Summing cells through $n<D$ costs at most $3V(2D)+2V(3D)+3E(D)$, where $E(D)$ is the number of odd defects through $n<D$. Division by $qN$ and enlargement to the last complete cell give (2). The two discrete inequalities, including their defect terms, are checked in [DilationRows.lean](DilationRows.lean).

Write $Q=\lfloor L^{1/16}\rfloor$. Dirichlet approximation to $\log_2 3$ gives $1\le k\le Q$ and a positive integer $m=O(Q)$ with

$$
 cQ^{-4.2}\le u=|k\log 3-m\log2|\le (\log2)/Q.
                                                                    \tag{3}
$$

For the lower bound, apply Wu and Wang's Theorem 1 with constant coefficient zero and an exponent $4.2>4.1163051$. Absorb the finitely many small nonzero forms into $c$. Uniqueness of prime factorization excludes a zero form. [Wu and Wang, *On the irrationality measure of log 3*, Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007)

Let $a=e^u$ (ordinary real exponential). The ratio $a$ has a representation as a product of $O(Q)$ factors $2,3,1/2,1/3$ for $a$, all of whose partial products lie in a fixed compact subinterval of $(0,\infty)$, independent of $N$. Follow $3^j2^{-\lfloor j\log_2 3\rfloor}\in[1,2)$, multiplying by three, then dividing by two once or twice at each step. At the end, one extra factor $1/2$ suffices if $m$ is the upper integer. Invert every factor if the original signed form is negative. For each factor the local $L^1$ cost follows from (2), including inverse factors by a change of variables. Bounded partial products keep the Jacobians and integration domains bounded when the word is telescoped. Thus, for each fixed $B$,

$$
 \int_0^B |f(ax)-f(x)|\,dx \ll_{B,b} QL^{-1/2}.                 \tag{4}
$$


### Slow frequencies and arbitrary intervals

Let $P(s)=s^{-1}\int_0^s f$, $s>0$. For $Q^{-1}/2\le s\le1$, (4) gives $|P(as)-P(s)|\ll Q^2L^{-1/2}$. For $Q^{-1}\le x\le1$, choose a grid point $s=a^{-j}\le x<as$. There are $O(Q^{4.2}\log Q)$ steps back to 1 by (3). The ratio error in replacing $P(x)$ by $P(s)$ is $O(1/Q)$ since $0\le f\le1$. The accumulated error from (4) is $O(Q^{6.2}\log Q/\sqrt L)=O(1/Q)$. For $x<1/Q$ bound the integral by its length. Since $P(1)=p_N$, this proves

$$
 \sup_{0\le x\le1}\left|\int_0^x(f-p_N)\right|\ll Q^{-1}.     \tag{5}
$$

Integration by parts on any $I\subset[0,1]$ bounds the centered integral against $e(\lambda x)$ by $O((1+|\lambda|)/Q)$. This is $O(Q^{-1/6})$ throughout $|\lambda|\le Q^{5/6}$.

### Fast frequencies

Set $M=\lfloor Q^{1/3}\rfloor, \eta=Q^{-1/6}$. Choose $s_j=a^{k_j}$, $1\le j\le M$, by rounding $j\eta/(Mu)$ down to the integer $k_j$. For large $Q$, (3) gives

$$
 1\le s_j\le e^\eta,\quad |s_j-s_l|\gg Q^{-1/2} (j\ne l),
 \quad k_j\ll Q^{4.2}.
$$

The gap before rounding is $\eta/M\asymp Q^{-1/2}$ in log scale, larger than the rounding error $u$. Repeating (4) at most $O(Q^{4.2})$ times now costs $O(Q^{5.2}/\sqrt L)$ in local $L^1$. All cumulative multipliers stay between 1 and 2. With $g=f-p_N$, a substitution and the symmetric difference of $I,s_jI$ give, uniformly in $I,\lambda,j$,

$$
 \left|\int_I g(x)e(\lambda x)\,dx-
           \int_I g(x)e(s_j\lambda x)\,dx\right|
 \ll \eta+Q^{5.2}/\sqrt L.                                     \tag{6}
$$

Indeed the first integral may be replaced by its integral over $s_jI$ at cost $O(\eta)$, then scale back, drop the Jacobian error $O(\eta)$, and replace $g(s_jx)$ by $g(x)$.

Average the second integrals in (6) and use Cauchy–Schwarz. The squared $L^2(I)$ norm of $M^{-1}\sum_j e(s_j\lambda x)$ is at most

$$
 M^{-1}+O\big((|\lambda|Q^{-1/2})^{-1}\big)
$$

by direct integration of every off-diagonal exponential. For $|\lambda|\ge Q^{5/6}$ its square root is $O(Q^{-1/6})$. Together with (5) this proves the same bound for all centered integrals.

Choose $t\in[-1/2,1/2]$, set $\lambda=Nt$, and take $I$ to be the union of the complete $N^{-1}$ cells involved in the sum, itself an interval. Integrating within each cell multiplies the normalized discrete sum by $\int_0^1e(ty)\,dy$, whose modulus is at least $2/\pi$. This proves (1) even at frequencies on the lattice scale. At $t=0$, apply (5) directly. These arguments are written mathematics.

## Three prescribed ordinary targets

Let $b_c(n)$ indicate that $n>0$ visits a specified positive odd ternary unit $c$, write $p_c(N)$ for its row mean, and put $\rho_N=(\log N)^{-1/96}$. For arbitrary finite sets $A,B\subset\{1,\ldots,\lfloor(N-1)/2\rfloor\}$, including sets selected by full path information, Fourier orthogonality and Parseval give

$$
 \left|\#\{(x,y)\in A\times B:b_c(x+y)=1\}
             -p_c(N)|A||B|\right|
 \ll_c N\rho_N\sqrt{|A||B|}.                                  \tag{7}
$$

Indeed $(b_c(n)-p_c(N))1_{[0,N)}(n)$ has Fourier sup norm $O_c(N\rho_N)$. The integrals of the product of the other two Fourier polynomials in absolute value are at most $\sqrt{|A||B|}$. The sum stays inside the row for these sets. A product of two dense sets may retain constraints on both original histories. A requirement coupling the choices of the two summands changes the counting measure.

More generally take three fixed positive odd ternary-unit targets $a,b,c$. The number of positive ordered pairs with $x+y<N$ such that their orbits from $x,y,x+y$ visit $a,b,c$, respectively, equals

$$
 \tfrac12 p_a(N)p_b(N)p_c(N) N^2+O_{a,b,c}(N^2\rho_N).       \tag{8}
$$

Expand the three finite Fourier polynomials on $[0,N)$ one factor at a time about their means times the interval polynomial. Every difference uses (1) in sup norm and two Parseval bounds $O(\sqrt N)$. The count for three interval polynomials is $N(N+1)/2$, with $O(N)$ possible endpoint corrections. Each mean has positive lower limit by the fixed-target theorem, since a shortcut cannot skip an odd target visited by the ordinary Collatz map. Thus (8) gives $\gg_{a,b,c} N^2$ genuine pairs even for targets with disjoint predecessor sets. [Mazur, *Positive Lower Density of Collatz Predecessors*, manuscript and external Lean roots](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

## The prescribed diagonal and the missing contradiction

Take $a=b=5,c=85$. The forward path of 5 goes through 8 to the cycle at 1, and 85 goes through 128 to the same cycle. Neither visits the other, so the two visit sets are disjoint by determinism. Equation (8) supplies positive density of the prescribed pairs. **There are zero such pairs on $x=y$** since $2x$ visits 5 whenever $x$ does. Lean checks the separation of the two forward paths and this assertion for all ordinary $x$. [TargetDiagonal.lean](TargetDiagonal.lean)

In fact take $N/4\le x<N/2, y=x+d, 0\le d\le H=N^{o(1)}$. Only $o(N(H+1))$ of these pairs can have the stated visits. Such a pair would require different 5-marks at $2x$ and $2x+d$. With $h=\lfloor(\log_2 N)/2\rfloor$, all sites of both arms exceed 5 through clock $h$ for large $N$. Leen's uniform gap estimate makes the fraction of failing residues at most $C\sqrt{(1+\log(1+H))/(1+h)}$. Restriction to even original inputs costs at most a factor two, and the incomplete binary period costs $O(2^h/N)$. Summing over $d$ proves the claim. This includes bands of every fixed polylogarithmic width. The argument uses the stated uniform-in-gap coefficient and exact finite residue realization in [Leen's preprint](https://doi.org/10.5281/zenodo.23268751) and [the displayed transfer version, equation (1)](https://rstation.ai/problems/collatz/papers/13).

For the actual indicator of failure to reach 1, a positive bad integer would force both colors to have positive lower natural density. To find a bad odd ternary unit, strip twos, and if an odd multiple of three remains apply an odd step and strip twos again. Every predecessor of the resulting target is bad, and every predecessor of 1 is good. Consequently $p_N$ stays bounded away from 0 and 1. Center the previous packet's symmetric triangular polynomial by setting $C_N=K_N-p_N F_N$, where $F_N$ is the ordinary Fejér kernel including its constant coefficient. The triangular version of (1) and reflection give $\|C_N\|_\infty\ll N\rho_N$. Parseval gives $\|C_N\|_2^2\gg_b N$, since each centered coefficient before weighting has absolute value bounded below and the first half of the row has weight at least $1/2$. Hence

$$
 \|K_N\|_1\ge \frac{\|C_N\|_2^2}{\|C_N\|_\infty}-1
             \gg_b (\log N)^{1/96}\quad(N\text{ sufficiently large}). \tag{9}
$$

This gives a quantitative lower bound for every sufficiently large cutoff. It requires neither an assumed limiting density nor an idempotent-measure structure theorem. Under the same hypothetical nonconstancy, (5) also puts a positive fraction of each color in every row interval of length at least $C_b N/(\log N)^{1/16}$, for sufficiently large $C_b$.

For a contradiction one needs an incompatible *upper* bound for the exactly invariant bad mark, for instance $\|K_{N_j}\|_1=o((\log N_j)^{1/96})$ on some unbounded row sequence. The previously obtained $O(\sqrt N/(\log N)^{1/8})$ upper bound permits (9). The exact odd edge removes the term $3E(D)$ in the ternary comparison, but this changes the normalized estimate by only $O(1/N)$ for a single failed edge. The visit-to-5 mark itself satisfies (9) because the visits to 85 supply positive lower density of its complementary color. In particular, eliminating the single defect from the row bound, or applying (7) on the prescribed diagonal, gives no such upper estimate. For the least bad triple the vanishing coefficients below its height form a fixed prefix; (1) and (7) do not enlarge that prefix along the same ordinary source. This is the first missing global inference. A separate positive-definite construction tests the same issue directly on the actual component partition. [Component averages and fixed-pair retention](COMPONENT_GRAM.md). [Prior Fejér criterion and upper bound](../../astra-closure-20261125/global/README.md) · [True-parent restriction in PR192 at 1f1d3d690d7517e1b2a44b5f2f4930bd45b63302](https://github.com/GettysburgResearch/collatz/blob/1f1d3d690d7517e1b2a44b5f2f4930bd45b63302/research/astra-diagonal-closure-20261125/joint/README.md) · [PR201's polynomial-width source bands at 02fb390a76fb2ffb00fee612649ca23a82d99d31](https://github.com/GettysburgResearch/collatz/blob/02fb390a76fb2ffb00fee612649ca23a82d99d31/research/killed-green-head-closure-20261124/thin-band/README.md)
