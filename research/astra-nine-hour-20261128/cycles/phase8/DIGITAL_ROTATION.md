# An exact rounded-rotation clock and its information horizon

**Written theorem.** Let \(Y\) be the distinct odd states of a positive integer Syracuse cycle, \(m=\min Y\), \(p=|Y|\), \(A\) its sum of native exponents, and \(\gamma=\log_2 3\). For each integer \(K\ge1\), let \(\Lambda_K\) be all dyadic multiples, in both directions, of the integers \(K,\ldots,2K-1\). Define the order-preserving maps
\[
    F_K(z)=\min\{w\in\Lambda_K:w\ge 3z\},\qquad
    G_K(z)=\max\{w\in\Lambda_K:w\le z/3\}\qquad(z\in\Lambda_K).
\]
They commute with doubling. The rotation clock \(\eta_K\) of \(F_K\) is rational, is computable from an orbit begun at \(K\), and obeys
\[
                      \gamma< A/p\le \eta_{2m}.                         \tag{1}
\]
There is no restriction on the largest state, the canonical height or the gcd of the two native counts. If \(X=\max Y<4m\), then \(A/p=\eta_K\) for **every** integer \(X/2<K\le2m\). Conversely, a cycle modulo doubling of \(G_K\) whose fundamental integer representatives are all prime to three and indivisible by four yields a genuine positive odd cycle of ratio strictly below four. This criterion dispenses with a prescribed slope. The ordered-state and prescribed-schedule precursors are described in [our scheduled floor note](../phase5/SCHEDULED_FLOOR.md) and Weaver's phase-order paper. [Weaver, rStation 114/v1](https://rstation.ai/problems/collatz/papers/114/v1)

### Prefix counts of an arbitrary actual cycle

For \(a>0\) define \(B(a)=\sum_{y\in Y}\lfloor\log_2(y/a)\rfloor\). Then \(B(2a)=B(a)-p\). Using all the true edges \(2^{e_y}y'=3y+1\) and their permutation of \(Y\),
\[
 B(3a)-B(a)+A=E(a)
 =\sum_{y\in Y}\left(\left\lfloor\log_2((y+1/3)/a)\right\rfloor
                            -\left\lfloor\log_2(y/a)\right\rfloor\right)\ge0 .
\]
For integral \(a\ge1\), a contribution occurs precisely when
\[
            2^j y < a \le 2^j(y+1/3)\quad\text{for some } j\ge2.       \tag{2}
\]
Indeed a power-of-two multiple of \(a\) must be in \((y,y+1/3]\). Nonnegative powers give integers and cannot do so. At half scale the interval in (2) contains no integer. Thus \(E(a)=0\) for \(1\le a\le4m\), while \(E(4m+1)=1\). Equivalently the nonnegative prefix masses \(w_a=B(a)-B(a+1)\) satisfy
\[
 w_a=w_{2a}+w_{2a+1},\qquad
 w_{3a}+w_{3a+1}+w_{3a+2}=w_a+E(a)-E(a+1).
\]
In particular both exact refinement identities hold at every \(a<4m\). The first positive discrepancy is attained by the least odd state and the second binary dilation.

### Finite clock, adjoint and physical reconstruction

The fundamental representatives of \(\Lambda_K\) are the \(K\) consecutive integers in \([K,2K)\). Thus every positive orbit of \(F_K\) is eventually periodic after reducing by doubling. If \(F_K^q(z)=2^a z\) on a repeated orbit then its clock is \(a/q\). All starting values give the same limiting \(\log_2(F_K^h(z)/z)/h\), by placing one between two fixed dyadic multiples of another and iterating the order-preserving map. The limit is \(\eta_K\). Since \(F_K(z)\ge3z\), \(\eta_K\ge\gamma\), with strict inequality by irrationality. The grid \(\Lambda_{K+1}\) adds exactly the odd ray \(2K+1\) to \(\Lambda_K\), replacing the old representative \(K\) by the equivalent \(2K\). Its upward rounding is finer, so \(\eta_{K+1}\le\eta_K\), by iterated order comparison. The identity
\[
          F_K(x)\le z\quad\Longleftrightarrow\quad x\le G_K(z)
\]
iterates to the corresponding \(h\)-th powers. Taking \(z\) to run through dyadic multiples of one fixed point shows that \(G_K\) has clock \(-\eta_K\). Explicitly if \(F_K^h(x)\in(2^{j-1}z,2^jz]\), adjointness gives \(x\in(2^{j-1}G_K^h(z),2^jG_K^h(z)]\); divide the two logarithmic errors of at most one by \(h\).

Now set \(K=2m\). All integral fundamental representatives have \(E=0\), as do their dyadic multiples. At such \(z\),
\[
       B(F_K(z))\le B(3z)=B(z)-A .
\]
Sum around any periodic \(F_K\) orbit with \(q\) dates and \(a\) windings. This gives \(ap\ge qA\), proving (1). Wider grids with a positive discrepancy on some test rays need that term restored.

For the equality statement, fold the actual odd states into \([K,2K)\) for \(X/2<K\le2m\). Their labels \(z=cx\) have \(c=1\) or \(2\), according as \(x\ge K\) or \(x<K\). At a reversed native edge the lifted identity has \(2^b z=3z'+c'\). Here the factors represent reduction to the common octave. In fact \(b=1\) or \(2\): since \(z',z\in[K,2K)\), one has \(2^b>3/2\) and \(2^b<6+2/K\le8\), with strictness at the endpoint. Consequently \(z'=\lfloor2^b z/3\rfloor\). This is exactly \(G_K\) after normalization: use \(b=1\) if \(2z\ge3K\), otherwise \(b=2\). The case of a normalized output at the upper seam is handled by the half-open fundamental interval. Thus the one closed physical path gives the asserted common clock.

Conversely along a periodic \(G_K\) orbit let \(2^b z=3z'+r'\) denote this floor division. Since \(3\nmid z\), \(r'\in\{1,2\}\). Evenness of the left gives \(r'\equiv z'\bmod2\). Since \(4\nmid z'\), \(r'\) equals the exact lowbit \(c'\) of \(z'\). Put \(z=cx,z'=c'x'\) with both odd parts. Then \(2^{b}cx=c'(3x'+1)\) gives a true odd edge of exponent \(b+\log_2 c-\log_2 c'\). This exponent is positive because \(x\) is odd and \(3x'+1\) is even. Distinct fundamental orbit labels have distinct odd parts. Those odd parts lie in \([K/2,2K)\), so their ratio is strictly less than four.

A tempting further claim would give the same periodic representatives for the adjoints. The actual grid \(K=2\) disproves it: on the two representatives \(2,3\), the periodic representative of \(F_2\) is \(3\), whereas the periodic representative of \(G_2\) is \(2\). Their clocks have equal absolute value. One therefore cannot impose *both* maps' separate digit caps on a common cycle, or derive a three-quarter balanced-minimum bound that way.

### Sharp coefficient question

For forward \(F_K\) at a fundamental \(x\), choose \(b=1\) if \(3x<4K\) and \(b=2\) otherwise. Compute \(z=\lceil3x/2^b\rceil\); if \(z=2K\) it represents \(K\) with one additional winding. The forward residual \(r=2^b z-3x\) lies in \([0,2^b-1]\). All periodic angle measures tend weakly to Haar measure as \(K\to\infty\): true increments are \(\gamma+O(1/K)\), so every weak limit is invariant under the irrational rotation. The exact excess clock is the average of \(\log_2(1+r/(3x))\). If the conditional distribution of \(x\bmod 2^b\) approaches uniform sufficiently to average this observable, the predicted coefficient is
\[
 C=\frac{1}{3\ln2}\int_0^1 2^{-\theta}
              \frac{2^{b(\theta)}-1}{2}\,d\theta
      =\frac1{6(\ln2)^2}=0.34689\ldots,\qquad
 b(\theta)=\begin{cases}1&2^\theta<4/3,\\2&2^\theta\ge4/3.\end{cases}
\]
The problem is to prove or refute \(\limsup K(\eta_K-\gamma)\le C\). The proven worst-residual bound gives only \(2C+o(1)\) at this scale. Formula (1) would turn the sharper bound into
\[
   \limsup m\,p^{-1}\sum_{y\in Y}y^{-1}\le 1/(4\ln2)
\]
along every sequence of distinct ordinary cycles. This follows by a uniform Taylor expansion since \(m\to\infty\). In an orbit confined below \(4m\), the last right side is the asymptotic minimum permitted by angular equidistribution, attained only by concentrating in the higher physical octave up to a vanishing fraction. The upper bound \(C\) is an open homogenization question about **integer periodic** orbits.

### All possible behavior occurs through the information horizon

For every sufficiently large \(N\), there are \(K\asymp3^N\) and a genuine *integer* segment of \(N\) consecutive forward \(F_K\) edges attaining the maximum residual \(2^b-1\) at every date. There are separate such segments with residual zero throughout. More generally all permitted residual strings can be realized for the common mechanical calendar below.

Choose \(\theta\) at the midpoint of a longest circular gap in \(\{-t\gamma\bmod1:0\le t\le N\}\), so its distance to every boundary is at least \(1/(2(N+1))\). Put \(b_t=\lfloor\theta+(t+1)\gamma\rfloor-\lfloor\theta+t\gamma\rfloor\) with \(0\le\theta<1\). For any prescribed \(0\le r_t<2^{b_t}\), the chain \(2^{b_t}x_{t+1}=3x_t+r_t\) fixes one residue for \(x_0\bmod 2^{B}\), \(B=\sum_{t<N}b_t\): solve the final affine equality modulo \(2^B\) using the invertibility of \(3^N\), then reduce through the partial sums to obtain all intermediate divisions. Choose its representative \(2^B\le x_0<2^{B+1}\) and take \(K\) nearest \(2^{-\theta}x_0\). Thus \(K\asymp3^N\).

The initial normalized logarithm differs from \(\theta\) by \(O(1/K)\). As long as branches agree the extra error through any prefix is \(O(N/K)\), since its true integer residuals have absolute size at most three and its mantissas stay at least \(K\). Induction, using the uniform boundary margin and the relative rounding grid size \(O(1/K)\), keeps every step in the chosen octave with exactly its prescribed branch; no seam carry occurs. Because the residual also lies in the unique ceiling range, these are genuine \(F_K\) steps. For the maximum string the segment average of \(K\log_2(1+r_t/(3x_t))\) tends to \(2C\). The ideal angular averages converge uniformly in the initial phase for this bounded piecewise continuous integrand, and the real angle errors tend uniformly to zero. The zero string gives exactly zero. Thus even actual positive integer segments with \(N=\log_3K+O(1)\) attain both extremes.

There is a second local obstruction of arbitrary depth. Along any two-sided mechanical angle path, prescribe any \(r_t\) in the same permitted ranges. The affine recursion above has a unique compatible two-sided \(\mathbb Z_2\) solution from its future, by division by three and contraction by the increasing powers of two when solved backwards. It has a unique two-sided \(\mathbb Z_3\) solution from its past, by contraction by powers of three and division by two when solved forwards. For any modulus prime to six one may start in uniform residue and transport by the affine permutations. Consequently the maximal-residual path survives at all finite residue precisions; a rotation-invariant distribution on starting angles gives an invariant model with coefficient \(2C\). A coboundary or pointwise averaging bound on these compact local states cannot give \(C\). Whole integer return, or information beyond the tested horizon, is essential here.

The digital-rotation analogy concerns a one-dimensional positively ordered logarithmic grid. Work on discretized *planar* rotations uses different maps. [Vivaldi, *The arithmetic of discretized rotations*](https://maths.qmul.ac.uk/~fvivaldi/research/DiscretizedRotations.pdf)

### Every change in clock is one Farey edge

**Written theorem.** If increasing the resolution from \(K\) to \(K+1\) changes the reduced clock from \(a/q\) to \(a'/q'\), then
\[
                            aq'-a'q=1.                                \tag{3}
\]
In particular the staircase \(\eta_K\downarrow\gamma\) visits *every* best upper rational in the denominator sense between \(\gamma\) and the starting clock: these are the reduced \(A/P>\gamma\) for which no rational in \((\gamma,A/P)\) has denominator at most \(P\). Visiting a clock of exceptionally good upper approximation therefore does not require an ordinary cycle.

To prove (3), choose one periodic orbit each of the old and new maps, with fundamental states \(x_i\), \(y_j\) represented in one common octave, and write \(F_K(x_i)=2^{b_i}x_{i+1}\), \(F_{K+1}(y_j)=2^{b'_j}y_{j+1}\). Use their least periods \(Q,Q'\). The windings of each periodic orbit in lowest terms have these respective denominators: the map is increasing and injective on the lifted orbit, hence translates the sorted ranks; one complete cycle requires that shift to be coprime to the number of rays. Thus \(Q=q,Q'=q'\).

For nonzero positive \(u,v\) let \(L(u,v)=\lceil\log_2(u/v)\rceil\). Sum
\[
          L(F_K(x_i),F_{K+1}(y_j))-L(x_i,y_j)
\]
over all \(q q'\) pairs. Moving the windings out of the first term and reindexing the two permutations gives \(aq'-a'q\). If one summand is positive, put \(t=L(x_i,y_j)\) so \(x_i\le2^t y_j\). Its positivity requires \(F_K(x_i)>F_{K+1}(2^t y_j)\). Extend both ceiling formulas to positive real arguments just for this comparison. Monotonicity gives \(F_K(x_i)\le F_K(2^t y_j)\). Since the only new ray is \(2K+1\), the latter old ceiling must be the immediate old-grid successor of a representative of that new ray, and \(F_{K+1}(2^t y_j)\) must be the inserted representative itself. The intermediate old ceiling \(F_K(x_i)\) is that same successor: there is no other old point in between. The two displayed outputs are closer than a factor of two. Consequently the positive summand equals exactly one. The earlier and later target rays are both uniquely specified. Periodic injectivity in each orbit allows at most one such pair in the entire sum. Hence the determinant is at most one. The strict drop and integrality finish the proof.

For the best-upper assertion, downward convergence follows directly from the maximum spacing bound \(F_K(z)/(3z)=1+O(1/K)\) on the fundamental octave. If the decreasing staircase passed a best upper \(A/P\) without hitting it, two consecutive distinct clocks would straddle it. Between two reduced Farey neighbors each intermediate fraction has denominator at least the sum of their denominators: writing the numerator/denominator column in their determinant-one integer basis gives positive integer coefficients. The lower neighbor would consequently lie strictly between \(\gamma\) and \(A/P\) with denominator below \(P\), a contradiction.

Here are finite stress tests at the right edge of selected upper-convergent plateaux. In every row the two displayed clocks are computed at the two stated resolutions; each clock comparison and the determinant of each pair use integers. A gap of two between the resolutions brackets the transition but does not specify which of its two individual increments changed the clock. The rightmost column uses a decimal approximation only to describe the scale.

| upper clock \(a/q\) | last tested \(K_-\) with this clock | first tested \(K_+\) below it | clock at \(K_+\) | \(K_-(a/q-\gamma)\), approx. |
|---|---:|---:|---|---:|
| \(65/41\) | 1,078 | 1,080 | \(474/299\) | .43481 |
| \(485/306\) | 78,662 | 78,663 | \(10754/6785\) | .37911 |
| \(24727/15601\) | 210,662,570 | 210,662,572 | \(2918840/1841583\) | .35445 |
| \(125743/79335\) | 5,264,480,272 | 5,264,480,274 | \(26330795/16612882\) | .35084 |
| \(301994/190537\) | 715,839,935,431 | 715,839,935,433 | \(2171815105/1370262769\) | .34964 |

The last new period exceeds 1.37 billion. The constant-memory C++ replay accepts individual resolutions; the default Python controls include the first two comparisons, 2,048 adjoint clocks and all best uppers through denominator 41, the prefix identities, the distinct-support counterexample, and integer block realization through 200 dates. The finite table does not establish the coefficient limit. The rank and width-nine consequence of the near-dyadic inversion criterion is also available in concurrent PR214. [PR214, 7307fb0ecd756a4affc4c831f5bef4279ac5d3fe, RESIDUE_FIBER_INVERSIONS.md](https://github.com/GettysburgResearch/collatz/blob/7307fb0ecd756a4affc4c831f5bef4279ac5d3fe/research/astra-critical-rigidity-20261128/cycles/RESIDUE_FIBER_INVERSIONS.md)

[GridClock.lean](GridClock.lean) verifies the iterated prefix decrement, the periodic clock comparison, and the single-edge reconstruction of a genuine exponent. [FareyClock.lean](FareyClock.lean) verifies the double-sum winding cancellation and determinant-one conclusion from the one-pair crossing cap. The dyadic-grid geometry supplying that cap, the rotation arguments, the information horizon and the best-upper result are written proofs.
