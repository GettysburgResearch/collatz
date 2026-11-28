# Every ordinary odd unit is identifiable in the spectrum

Let $X$ be the positive odd units modulo three, let $t_x=1/(3x+1)$, and use the actual all-parent operator $L$ and its principal projection $\Pi$ from [the positive Green theorem](POSITIVE_GREEN_SPECTRUM.md). The present statements concern individual ordinary integer states, including those eventually reaching a cycle and those on any escaping component.

For every $y\in X$,

\[
 \boxed{\quad t_y\in\sigma(L)\quad\Longleftrightarrow\quad
          y\text{ is nonperiodic}.\quad}                                \tag{1}
\]

Every physical grid value that occurs is an isolated algebraically simple eigenvalue. In particular the known cyclic site $1$ removes $1/4$. Each other positive cycle would remove its own sites from the same explicit grid. Nonprincipal eigenvalues contributed by cycles can never replace any of those missing grid values.

## The parity calculation

Put $T=X\setminus Z$ for the nonperiodic sites and $Z$ for the union of the cycles. Every $y\in T$ contributes $t_y$ to the compact transient compression $L_T$. Indeed choose finite compressions retaining $y$ and exhausting $T$. Their triangular matrices have the distinct diagonal values $t_x$ of their sites. If $t_y$ were in the resolvent set of $L_T$, norm convergence would make all sufficiently large compressions invertible at $t_y$, a contradiction. The other nonzero spectral points of $L_T$ were already shown to be in the grid. A small circle isolating $t_y$ therefore gives norm convergence of Riesz projections; the finite projections have rank exactly one. This proves the asserted transient algebraic multiplicity.

For a genuine cycle $C$ with $p$ sites, $w_x=3x/(3x+1)$ and $\lambda=\prod_C w_x$, its finite stochastic Green block has characteristic polynomial

\[
        \frac{\prod_{x\in C}(\zeta-t_x)-\lambda\zeta^p}{1-\lambda}.
\]

Substitution of $\zeta=t_y$ and clearing the positive denominators gives

\[
             \prod_{x\in C}(x-y)=\prod_{x\in C}x.                        \tag{2}
\]

Every factor on the left is even for odd $y$, whereas the right side is odd. Hence (2) fails for all such $y$, including those lying outside $C$. The direct cycle sum has no spectral accumulation except possibly zero and one, by the uniform rank-one and resolvent estimates of the Green theorem. The triangular resolvent then preserves the algebraic multiplicity at each $t_y$. This proves (1). The pointwise eigenmode equation at this grid value, after writing $f(x)=\sqrt{t_x}\,u(x)$ and splitting the first edge, is $u(Ux)=(1-y/x)u(x)$.

For general $\zeta\ne0$ coming from a cyclic block, $Y=(1/\zeta-1)/3$ solves $\prod_{x\in C}(x-Y)=\prod_{x\in C}x$. In particular $Y$ is an algebraic integer and $Y=0$ gives the principal eigenvalue. Every other such $Y$ has positive real part, since $|x-Y|>x$ for all $x>0$ when $\operatorname{Re}Y\le0$ and $Y\ne0$. A rational $Y$ must be an even integer by (2).

## A nonreal pair from any extra cycle

The complete spectrum of $L$ is real if and only if the fixed positive cycle is the only one. An extra cycle would contribute a nonreal conjugate pair, even when arbitrary escaping orbits are present. This gives a single geometric target whose proof would exclude every extra cycle; reality of the actual spectrum has not been established.

Here are the estimates on the cyclic characteristic polynomial. Write $m=\min C$, $p=|C|$, $a_i=(1/x_i)/\sum_C1/x$, and sort these weights from largest to smallest. The numerical inputs $m\ge1000$ and $p\ge32$ are much weaker than the published floor and period bounds. [Floor and period sources](DELAYED_CYCLE_TRACE.md). Since $U(x)\le(3+1/m)x/2$, each adjacent ratio of the sorted weights satisfies $a_{i+1}\ge r a_i$ for $r=333/500$. Indeed some physical forward edge must exit the top $i$ weights, and its landing weight is at least $r$ times its departure weight.

A normalized decreasing list of length $k$ with this ratio bound is majorized by the normalized list $1,r,\ldots,r^{k-1}$. The quotients of its entries by the corresponding normalized geometric entries are nondecreasing, so their differences change sign at most once and every initial weight sum is at most the geometric initial sum. Convexity of the square, or summation by parts against the decreasing sum of the two lists, gives

\[
       \sum a_i^2\le\frac{1-r}{1+r}\frac{1+r^k}{1-r^k}<201/1000
                       \qquad (k\ge30).                                  \tag{2a}
\]

Apply this to the entire list and to its renormalized tail after its largest entry $a$. Write $M_j=\sum_i a_i^j$ and $b=201/1000$. Thus $M_2\le b$ and $M_2\le a^2+b(1-a)^2$. If $M_2\le19/100$, the variance bound $M_3\ge M_2^2$ gives

\[
   1-6M_2+8M_3-3M_2^2\ge (1-M_2)(1-5M_2)>9/1000.
\]

If $M_2>19/100$, then $a\ge M_2>19/100$. On $[19/100,7/25]$ the function $a^2+b(1-a)^2$ is increasing and its right value is $0.1825984<19/100$, so $a>7/25$. The variance satisfies $M_3-M_2^2=\sum_i a_i(a_i-M_2)^2\ge(7/25)(7/25-b)^2$. Since $1-6x+5x^2$ decreases throughout this range,

\[
 1-6M_2+8M_3-3M_2^2\ge 1-6b+5b^2+8(7/25)(7/25-b)^2>9/1000.
\]

For the elementary symmetric functions of the normalized weights, the left side is $12(2e_3-e_2^2)$. The nonzero roots $Y$ of (2), now viewed as complex roots, are the zeros of $[\prod_{x\in C}(1-Y/x)-1]/Y$. Comparing its first three coefficients gives

\[
  \sum_{Y\ne0}\frac{1}{(3Y)^2}
     =\left(\sum_{x\in C}\frac1{3x}\right)^2(e_2^2-2e_3)
     <-\frac{3}{4000}\left(\sum_{x\in C}\frac1{3x}\right)^2.            \tag{2b}
\]

The sum is real, with multiplicities, and cannot be negative if every root is real. A nonreal $Y$ gives a nonreal $\zeta=(1+3Y)^{-1}$ of the cyclic block. The triangular operator estimates lift it to the spectrum of $L$; the transient block has only real spectrum. Conversely with only the fixed cycle all the remaining spectral values are the real transient grid and its limit zero.

There is also an operator whose cyclic square trace is exactly (2b). Set $A=(L-\Pi)(I-L+\Pi)^{-1}$, well-defined and Hilbert–Schmidt by the gap. Its transient eigenvalues are $1/(3x)$, and its nonprincipal cyclic eigenvalues are $\zeta/(1-\zeta)=1/(3Y)$. Thus every extra cycle contributes a strictly negative real number to $\operatorname{Tr}A^2$ alongside the positive transient squares. This uses the true loss ratios and the actual upward step bound on a cycle. It gives no independent lower bound proving the absence of that negative contribution.

## A signed trace with a finite arithmetic upper bound

The entire nonprincipal operator $L-\Pi$ is Hilbert–Schmidt; its square has a well-defined trace $\Xi$. Put

\[
       B=\sum_{x\in X\setminus\{1\}}\frac1{(3x+1)^2}
        =\frac{\psi_1(2/9)+\psi_1(8/9)}{18^2}-\frac1{16},
\]

where $\psi_1(a)=\sum_{k\ge0}(k+a)^{-2}$. The two progressions $3x+1=18k+4,18k+16$ give the formula. With the source-qualified aggregate extra gap below $0.023835$, the actual trace satisfies

\[
       0\le B-\Xi < (0.023835)^2.                                       \tag{3}
\]

Equality $B=\Xi$ holds exactly when the fixed cycle is the only positive cycle. More sharply the deficit dominates the sum of $1-[g_C/(2\sinh(g_C/2))]^2$ over every extra positive cycle. The upper and the sign are proved estimates. An independent lower estimate $\Xi\ge B$ that would force equality is missing.

For proof, in one cycle let $S=\sum_{x\in C} t_x$, $V=\sum_{x\in C}t_x^2$, $g=-\log\lambda$, and $d=1-\lambda$. In the ordered two-point terms of $\operatorname{Tr}(K_C^2)$, distinct endpoints give a circular survival product $\lambda$, while the diagonal gives one. Hence

\[
 \operatorname{Tr}(K_C^2)=\frac{d V+\lambda S^2}{d^2},\qquad
 \delta_C:=V-\big[\operatorname{Tr}(K_C^2)-1\big]
        =1-\frac{\lambda(S^2+dV)}{d^2}.                                 \tag{4}
\]

Since $g-S\ge V/2$ by the logarithm series and $g+S\ge2d$ by the union bound, $S^2+dV\le g^2$. As $d^2/\lambda=4\sinh^2(g/2)$, this proves the strict lower bound for every $\delta_C$.

For the opposite estimate write $e_j$ for the elementary symmetric functions of the $t_x$, with $e_j=0$ above the number of sites. Bonferroni's inequalities give $S-d\ge e_2-e_3$ and $d\ge S-e_2\ge S-S^2/2$. Also $3e_3\le S e_2$. All actual cycles have $S\le1/4$: use the fixed cycle directly and $S\le g<.024$ on extras. Thus $d\ge7S/8$, $d\le S\le1/4$, and $S(1+d)\le3d$. It follows that $S-d\ge e_2(1-S/3)\ge e_2/(1+d)$. Multiplication by $S+d\ge2d$ gives $(1+d)(S^2-d^2)\ge2de_2=d(S^2-V)$, or $S^2+dV\ge d^2(1+d)$. In (4) this yields $\delta_C\le d^2$.

On the transient diagonal $(L-\Pi)^2$ contributes just $t_x^2$, since no different forward target can return to $x$. On cyclic sites the corresponding block is $K_C^2-\Pi_C$ up to diagonal similarity, with $\operatorname{Tr}\Pi_C=1$. All diagonal sums are justified by trace class. The fixed cycle spends $\delta_{\{1\}}=1/16$. Summing (4) over the rest gives $B-\Xi=\sum_{C\ne\{1\}}\delta_C$, at most $\sum_C(1-e^{-g_C})^2\le (\sum_C g_C)^2$ with both sums here restricted to extras. This proves (3). [Aggregate gap input](DIAGONAL_CYCLE_MOMENT.md)

## Entire determinant on the arithmetic grid

In the Hilbert–Schmidt regularized determinant $F(z)=\det_2(I-z(L-\Pi))$, a zero occurs at $z=3y+1$ exactly for $y\in X$ nonperiodic, always simply. The reference diagonal $M_t$ has the explicit entire determinant

\[
 E(z)=\prod_{x\in X}(1-zt_x)e^{zt_x}
   =\prod_{a\in\{2/9,8/9\}}
       \frac{\Gamma(a)}{\Gamma(a-z/18)}\exp[-(z/18)\psi(a)],             \tag{5}
\]

by the Weierstrass gamma product, where $\psi=\Gamma'/\Gamma$. Away from its zeros, the ratio $F/E$ has one factor per actual cycle,

\[
 \frac{\prod_C(1-zt_x)-\lambda}
 {(1-z)(1-\lambda)\prod_C(1-zt_x)}
  \exp\bigl(z[S/(1-\lambda)-1-S]\bigr).                                 \tag{6}
\]

Here each product on the right is over the sites of the single cycle indexing the factor, and the quotient at $z=1$ is interpreted by continuity. Indeed the cyclic nonprincipal eigenvalues have sum $S/(1-\lambda)-1$. Formula (6) divides their regularized polynomial by the regularized diagonal factors on those same sites. The Hilbert–Schmidt property gives square-summability, with multiplicity, of the compact nonprincipal eigenvalues. Direct-sum spectral control and finite-rank contour approximation identify the nonzero algebraic multiplicities with those of the transient sites and finite cyclic blocks. The canonical genus-one products converge locally uniformly, permitting grouping by cycle. The fixed cycle removes precisely the factor $(1-z/4)e^{z/4}$ from $E$.

In particular any extra cyclic site forces a nonremovable pole of $F/E$ at its own integer grid point by (1). A reference gamma factor alone cannot exclude these poles: the actual numerator still contains the unknown cyclic characteristic polynomials. [Physical Green matrix and polynomial checks](check_green_spectrum.py) · [Exact counts](../../../reports/astra-global-20261128/cycles/GREEN_SPECTRUM.json)
