# Full small-order Rényi bounds and the clocks required by a power spike

**Source-qualified written deduction.** This extends the cited first-passage and certified-stage inputs. The strict incoming mass used in the limitation example is the previously pinned ordinary no-return floor. No whole analytic statement in this note has been formalized.

Use $g$, $\lambda_y$, the complete escaping log-mark law $\Lambda$, and the first-uncertified rank decomposition from the [all-interval power estimate](UNTRIMMED_FIRST_HIT_MARK.md). In $\Lambda$ each component may still be translated independently. For either original unnormalized measure $\nu$ and all grids of mesh $r=1/T$, put $m_I=\nu(I)$. Uniformly in the target height or component translations, for
\[
         1<p<1/(1-g)
\]
there are finite $C_p,D_p$ such that
\[
     T^{p-1}\sum_I m_I^p\le C_p(1+\log T)^{D_p}\qquad (T\ge2).        \tag{1}
\]
In particular for each fixed positive-mass target or escaping population of positive mass with bounded mark support, the full Rényi dimension of every such order is one. For a fixed translated escaping law without a bounded support, lower bound its $p$-sum on any compact subinterval of positive mass to obtain the same conclusion. This quantitative upper applies to the entire law, with no deletion of an exceptional part. At physical scale $1/y$ on a fixed escaping ray it gives the same polynomial-log upper for the complete $p$-th unit-bin density moment. The order-two question remains outside this range.

## A variable density bound at the physical first landing

Let $R=T^M$ for a sufficiently large fixed $M$, to be chosen in terms of $p$. Write $f(z)=R\mu_R(z)$ for the limiting first landing on odd labels $z\le R$, measured against counting measure divided by $R$. Fix any finite $s>1$ and put $\xi=g/(4s)$. Then
\[
 \frac1R\sum_{z:f(z)\le R^\xi} f(z)^s\ll_s(1+\log R)^{C_s},\qquad
 \sum_{z:f(z)>R^\xi}\mu_R(z)\ll_s R^{-g/2}.                          \tag{2}
\]
In the second inequality apply the usual global set majorant $F_R(|E|/R+R^{-g})$, $F_R=\exp(O(\sqrt{\log R}))$, to that very high-density set. Since $|E|/R\le\mu_R(E)R^{-\xi}$, absorption gives $\mu_R(E)\ll F_RR^{-g}$.

For the first bound use the finite-scale balancing proof of Weaver 102/v1 with a variable comparison scale. For $u\ge 3\log\log(3R)$ set $x_*=\exp(\exp u)$, $X=x_*^\gamma$, $\gamma=1.001$. The finite summed inequality (19) gives at this source scale
\[
 p_{X,R}(E)\le C e^u((1+\log R)|E|/R+(1+\log R)^2 R^{-g}).
\]
Telescoping the stopped-set law (20) along $x_*,x_*^\gamma,x_*^{\gamma^2},\ldots$ compares this probability to its limiting value with absolute error $O(e^{-c'u^2})$, by (24) with smaller $c'>0$. The limiting value for this smooth octave is $\mu_R(E)$ by ordinary existence and partial summation. Constants do not depend on $R,u,E$. For $L=2C e^u(1+\log R)$ apply the result to $E=\{f>L\}$. Its counting term is at most $\mu_R(E)/2$, so
\[
 \sum_{z:f>L}\mu_R(z)\ll L(1+\log R)R^{-g}
                 +\exp[-c'(\log(L/[2C(1+\log R)]))^2].                \tag{3}
\]
This holds once $L$ exceeds a fixed power of $1+\log R$. Integrate (3) against $(s-1)L^{s-2}dL$ up to $R^\xi$, using total mass at most one at lower $L$. The first term costs $O((1+\log R)R^{-g+s\xi})$ and the Gaussian in $\log(L/[2C(1+\log R)])$ gives at most a power of $1+\log R$ at each fixed $s$. This proves (2), which controls the $s$-moment of the retained pointwise density while making the discarded total a negative power of $R$. [Weaver 102/v1, (19), (20), (24)](https://rstation.ai/problems/collatz/papers/102)

## Transfer through the true physical stopping labels

Let $b_I$ be the unweighted finite-source bin masses in the preceding paper, assigning $1/R$ to each selected odd $z\le R$. By the actual first-uncertified rank proof there, for each $1<q<1/(1-g)$,
\[
      \sum b_I^q\ll_q (1+\log R)^{D_q}r^{q-1}.                         \tag{4}
\]
Choose $s>p$ large enough that $q=1+(p-1)s/(s-p)<1/(1-g)$. For a bin with $b_I>0$, put $u_I$ equal to the mean of $f1_{f\le R^\xi}$ among its actual labels under those counting weights. Use zero on an empty bin. Jensen and (2) give $\sum b_I u_I^s\ll_s(1+\log R)^{C_s}$. Hölder in that same finite measure gives
\[
 \sum_I (u_I b_I)^p\le
    \left(\sum_I b_I u_I^s\right)^{p/s}
    \left(\sum_I b_I^{1+(p-1)s/(s-p)}\right)^{1-p/s}.
\]
Inserting (4) yields $r^{p-1}$ times a polynomial in $1+\log R$, since $(q-1)(1-p/s)=p-1$. The high tail in (2) has bin $\ell^p$ norm at most $O_s(R^{-g/2})$. The early-hit or missing-landing exception has norm $O(R^{-\eta})$, as in the original source proof, and a fixed number of neighboring bins absorbs the small prior mark. Choose $M>\max(100,2/g,2/\eta)$, so these errors are at most $O(r)$ in norm. This proves (1). The fixed-root and escaping-ray changes of variables are bi-Lipschitz on their supported first-hit log marks after passing to the relative complementary coordinate, as in the preceding paper. A geometric lap mixture incurs at most a constant times a polynomial in $\log T$ at these exponents, by the same norm and scale summation.

## Genuine first-hit grade outliers forced by a large bin

A different consequence uses the first-visit grade $J_y(z)$ of the original odd source $z$ at $y$. Fix $0<\alpha<1$, $M>\max(100,2/g,2/\eta)$ and $R=T^M$. If at any positive odd unit $y$ an interval $I$ of width $1/T$ has $\lambda_y(I)\ge T^{-\alpha}$, then for all sufficiently large $T$, uniformly in $y$, the following holds. For **every** set of at most $T^{1-\alpha-o(1)}$ prescribed grades, with the $o(1)>0$ chosen below independently of $y$, there are at least $R T^{-\alpha-o(1)}$ actual odd $z\le R$ reaching $y$ in some other grade. Each such $B_y(z)$ belongs to a fixed $O(1/T)$ enlargement of $I$. One can require $z$ to be a ternary unit with a slightly enlarged interval after a single bounded change described below.

Indeed the early-before-$R$ bound and first-landing set estimate give at least $cR T^{-\alpha}/F_R$ such physical labels before excluding grades, $F_R=C\exp(C\sqrt{\log R})$. At one prescribed odd grade $j$ their integer division total $S$ has $O(1+\log R)$ possibilities: from (3) of the preceding paper with $w=y$ and $t=S$, one has $S\log2=j\log3+\log(z/y)+B_y(z)$, and $0\le\log z\le\log R$ while all first-hit corrections stay in one fixed bounded interval. There are at most $C(R/T+1)$ sources per $(j,S)$ on the prescribed mark interval. Thus for any set of at most $c'T^{1-\alpha}/[F_R(1+\log R)]$ grades the discarded physical labels cost less than half the lower bound, with sufficiently small absolute $c'$. In particular some first-hit grades exceed $T^{1-\alpha-o(1)}$ at inputs at most $T^M$, and no translation of this many consecutive grades covers the marked population. A polynomial spike of the full correction law would require a polynomially large native dispersion in the physical cutoff. The premise concerns mass of a single narrow interval. Weaver 175 Theorem 2 obtains unusually long times from positive Lebesgue length of a closed support, a different premise and scale. [Weaver 175/v1, Theorem 2](https://rstation.ai/problems/collatz/papers/175)

For the unit-source refinement, one may instead retain only labels $z>cRT^{-\alpha}/F_R$ by decreasing the absolute $c$. For a nonunit $z$, the odd integer $z'=4z+1$ is a unit and satisfies $U(z')=U(z)$, since $3z'+1=4(3z+1)$. The grades to the unit target agree for a positive-time hit, except that $z'=y$ can occur for at most one source. The correction change at the first departure is $O(1/z)$ and hence $o(1/T)$ in this retained range. Existing unit labels and images of nonunits have multiplicity at most two. This yields at least a fixed fraction as many true unit labels through $4R+1$ in the slightly enlarged interval, with the same excluded grades.

## Why a certification failure cannot be restarted with an arbitrary terminal mark

This obstruction concerns a genuine stopped observable on a large **set** of possible ordinary terminal sites. It distinguishes what the first-bad-label upper can imply from the stronger assertion for a single specified target. Write $\ell=\log_2 3$ and $p_*=(15/14)/\ell\in(1/2,1)$. For arbitrarily large integer $K$, put $P=2^{K+1}$. There are at least
\[
          P^{H_2(p_*)-o(1)}                                           \tag{5}
\]
odd ternary units $w\in[P/2,P)$ that fail Weaver 102's true certified stage at rank $K$. Choose $L=K-2$ and $h=\lceil (K+\lfloor K/14\rfloor+1)/\ell\rceil$. Of the $\binom Lh$ length-$L$ binary parity strings of weight $h$, at least $\binom Lh/L$ have every prefix of length $j$ containing at least $jh/L$ ones: move the starting point of any word to a minimum of its centered partial sums, and then bound the number of its cyclic rotations by $L$. Every retained word starts odd. The shortcut parity bijection gives one residue modulo $2^L$ per word. The shell contains four consecutive lifts in that class, at least two of which are ternary units because $2^L$ is invertible modulo three. For every realized prefix its additive corrections are nonnegative, so its height ratio after $j\le L$ is at least $3^{jh/L}2^{-j}\ge1$. At date $L$ its height is at least the starting height times $2^{K+\lfloor K/14\rfloor+1-L}$. Even the most rapid permitted descent in the remaining $K+\lfloor K/14\rfloor-L$ shortcuts leaves it above its starting height. Thus these lifts all miss the prescribed lower rank within the certified deadline. Stirling gives (5).

Every odd ternary unit $w\in[P/2,P]$ has a **genuine disjoint incoming** population of natural mass $\gg1/P$ whose first odd landing through $P$ is precisely $w$ and whose entire prior log correction is $O(1/P)$. Choose a unit odd parent $x=(2^e w-1)/3$ between $C_1 P$ and $C_2P$ for absolute large constants. There are several choices: exponents in the legal parity, taken in successive blocks of three choices, give unit parents at two of the three positions by the cycle of $4$ modulo nine. At most one is periodic since the deterministic cycle has only one predecessor on it. Choose a nonperiodic $x$ exceeding $2P$ by a sufficiently large fixed factor. The positive strict inverse floor at $x$ gives natural unnormalized mass $\gg 1/x$ for sources whose outward gap totals from $x$ satisfy $S_j>7j/4$ at every positive prefix. In the ordinary finite source limit this is precisely the source-qualified strict first-hit mass. Its multipliers $A_j=3^j2^{-S_j}$ decay geometrically, and the affine offsets $\sum_{i\le j}A_i/3$ are bounded by an absolute constant. Therefore every earlier state on these finite successful paths is $>P$, and the total correction to $x$ is at most $C/x$ by the exact ratio $1-\beta_j/x$. The one last odd step $x\to w$ adds $O(1/x)$. Different $w$ give disjoint first-landing labels. [PR213, ordinary strict no-return floor and finite-source interpretation, at 5ac2b4a7](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/mass/ORDINARY_NO_RETURN_EXPONENT.md)

Consequently the real law stopped at first odd landing through $P$, restricted to the uncertified unit labels in (5), places mass at least $P^{-(1-H_2(p_*))-o(1)}$ in the single width-$C/P$ interval at the origin. Its full square-energy divided by this mesh is at least $P^{1-2(1-H_2(p_*))-o(1)}$, far above a square root of a logarithm. This uses the actual incoming population and the actual correction on its entire path to the bad label. An argument that treats all the subsequent corrections at those bad labels as arbitrary constants must allow the common value zero, so it cannot by itself give the sharp square-root-log energy. Actual target-specific or component-specific continuation can spread this spike and is the remaining issue. This auxiliary stopped law does not provide a lower bound for an individual target's untrimmed energy.
