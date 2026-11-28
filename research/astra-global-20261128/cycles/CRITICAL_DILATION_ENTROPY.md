# Positive entropy of a fixed computable Collatz deadline along multiplicative dilations

**Source-qualified written theorem.** The orbit inputs are the complete exact-label first-landing template, counted equal-date synchronization for translated starts, and the fixed-target Gaussian clock law with its ordinary positive predecessor density. The initial joint invariance principle uses its separately specified two-adic logarithm input.

Fix a positive odd target $y$ with ordinary shortcut-predecessor density $d>0$. Define a single function on ordinary positive integers by the finite test
\[
       f_y(n)=1\quad\Longleftrightarrow\quad
        T^m n=y\text{ for some }m\ge0\text{ with }4^m\le3^m n^2.          \tag{1}
\]
Its deadline is $\lfloor 2\log n/\log(4/3)\rfloor$, computable by integer comparisons. Under the fixed-target Gaussian clock input specified below, $f_y$ has natural density $d/2$.

Put $b=\log2$, $P=\log3$, $a=b-P/2=\log(4/3)/2$, $\sigma=P/(2a^{3/2})$ and
\[
       \theta=a/b,\qquad c=\sqrt\theta,\qquad
       u=\tfrac14+\frac{\arcsin c}{2\pi}.
\]
Let $I_d$ denote the mutual information of bits $B,F$ having
\[
       \Pr(B=1)=\tfrac12,\quad \Pr(F=1)=d/2,\quad \Pr(B=F=1)=du.          \tag{2}
\]
Thus $I_d>0$. For any fixed positive odd $A_1,\ldots,A_r$ with all pairwise ratios outside $3^{\mathbb Z}$ and fixed integer offsets $e_i$, uniform ordinary $n\in[X,2X)$ satisfies
\[
     \liminf_{X\to\infty}
       H(f_y(A_1 n+e_1),\ldots,f_y(A_r n+e_r))\ \ge r I_d.               \tag{3}
\]
Entropy is in natural units. In particular, for every prime $p\ge5$ the actual patterns read along $n,pn,\ldots,p^{r-1}n$ have support of size at least $\exp(r I_d-o(1))$ in large octaves at each fixed $r$. Arbitrary growing observation lengths require a separate uniform estimate. This is a positive entropy rate for a genuine, finite, post-binary orbit measurement. It does not establish independence of the late clocks. The pure eventual-visit bit has no median clock cutoff, and the argument gives no positive entropy bound for that bit alone.

Here are two further conclusions. The scaled genuine first times at the same $r$ sources, assigning zero to missing clocks and normalizing the Gaussian finite part by $\sqrt d$ as specified below, have in every joint weak limit a covariance matrix with eigenvalues $\lambda_1\ge\cdots\ge\lambda_r$ satisfying
\[
       \sum_{j>k}\lambda_j\ \ge            r\left(\sqrt{d\theta}-\sqrt{k/r}\right)_+^2
                \quad (0\le k\le r).                                      \tag{4}
\]
Thus the rank is at least $\lceil rd\theta\rceil$. For first odd landing at any floor $B=B(X)\to\infty$ with $\log B=o(\log X)$, the same result holds with $d=1$ and the first-landing clock centred at $a^{-1}\log(X/B)$. In particular, five such nonsmooth dilations cannot all have the same Gaussian critical fluctuation.

In logarithmic source windows the deadline field has a stationary rational-dilation realization. Every such limiting field has positive entropy on each nonsmooth rational cyclic subgroup. Its covariance spectral measure has a nonzero absolutely continuous part, of mass at least $d^2\arcsin(\theta)/(2\pi)$ for (1), before variance normalization. For the standardized critical clock the lower mass is $d\theta$. All these results allow arbitrary genuine components and use no Riemann hypothesis.

## Early physical passage from a single actual source

Write $L=\log X$, $N=\lfloor L/b-L^{2/3}\rfloor$, $s=L/b-2L^{2/3}$ and $B'=\exp(L-as)$, rounding the floor threshold if desired. Thus $v'=\log(X/B')=as$ and $B'=X^{1-\theta+o(1)}$. Let $Q_i$ be the first shortcut time to any odd site at most $B'$ from $A_i n+e_i$ and let $Y_i$ be its actual landing. Use a single cemetery symbol when it fails.

By [the physical multiplier joining theorem](MULTIPLIER_BERNOULLI_JOINING.md), the vectors of signed counts $2k_m-m$ through $N$ jointly have independent standard Brownian limits after normalization by $\sqrt N$. This holds for uniform ordinary octaves since $2^N/X\to0$. Until the first shortcut state, of either parity, at or below $B'$, the exact log identity is
\[
  \log T^m x=\log x-am+\tfrac P2(2k_m(x)-m)+O(N/B'),\qquad m\le N.       \tag{5}
\]
Each departed site before that first crossing exceeds $B'$. Indeed every odd departure contributes the nonnegative correction $\log(1+1/(3T^j x))$, at most $1/(3B')$ there. The crossing height is between $B'/2$ and $B'$ because every shortcut step is at least half its input.

We give the inversion detail. The maxima of the rescaled signed-count paths are tight and $\log x=L+O(1)$ for the octave and fixed multipliers. Uniformly on the event that all those maxima are at most $K$, equation (5) excludes crossing before $s-O_K(\sqrt L)$ and forces it by $s+O_K(\sqrt L)<N$ for large $X$. At the crossing use its bounded log overshoot. The joint tight moduli of continuity of the rescaled paths replace the signed count there by its value at $\lfloor s\rfloor$, at error $o_{\Pr}(\sqrt L)$. If the first site below $B'$ is even, the consecutive halvings leading to its odd part cost $o_{\Pr}(\sqrt L)$ as well: among the first $N$ parities the probability of any run of $j$ even departures is at most $N2^{-j}+O(2^N/X)$ for each affine source, by the native parity coding and the odd multiplier. Choose $j=\lceil3\log_2 N\rceil$ and use the $L^{2/3}$ time margin. All these halvings stay below $B'$. Since $\sigma\sqrt{as}=P\sqrt s/(2a)$ and $s/N\to1$, we have
\[
      E_i=\frac{Q_i-s}{\sigma\sqrt{v'}}
             \quad\Longrightarrow\quad (G_i)_{1\le i\le r}
        \quad\text{jointly, with independent standard normal }G_i.          \tag{6}
\]
The left side denotes the vector of the displayed coordinates, setting a cemetery coordinate to zero. The cemetery probability tends to zero.

## The early clock is weakly independent of every function of its own true label

The required one-coordinate input is the [full first-landing law](../escape/GLOBAL_LANDING_CLOCK.md), equation (1), with its [mesoscopic source and normalization](../escape/MESOSCOPIC_LANDING_CLOCK.md). At any two growing $B',X'$ with $v=\log(X'/B')\to\infty$, the complete clock and exact odd label from an ordinary octave $[X',2X')$ have, up to arbitrarily small total variation in the specified template limit, the array
\[
             h_{B'}(z) f_v(t)
                 W(tb+\log(z/B')-v).
\]
Here $h_{B'}(z)=2g(z/B',z)/B'$ for a fixed bounded nonnegative template at each desired accuracy, $f_v$ is the Gaussian density of mean $v/a$ and variance $\sigma^2v$ at the integer $t$, and $W$ is a bounded Riemann-integrable function periodic modulo $P$ with circular mean one. The same theorem gives vanishing cemetery mass. The exact clock and label retain the circular factor, which we now average only in the rescaled clock.

For any fixed bounded continuous function $F$,
\[
 \sup_{u\bmod P}\left|
  \sum_{t\in\mathbb Z} f_v(t)
       F\!\left(\frac{t-v/a}{\sigma\sqrt v}\right)W(tb+u)
                           -\mathbb E F(G)\right|\to0.                  \tag{7}
\]
The irrational rotation $t\mapsto tb\pmod P$ has asymptotically uniform averages over long integer blocks, uniformly in the initial phase, for a fixed Riemann-integrable $W$. This follows by continuous upper and lower envelopes and trigonometric approximation for the continuous tests. Truncate first to a fixed compact standardized-time window, with uniformly small Gaussian tail, since $W$ is bounded. Divide that window into integer blocks whose length tends to infinity and is $o(\sqrt v)$. The Gaussian weight and continuous $F$ vary by $o(1)$ on the standardized block scale. Summing the block means gives (7) by ordinary Riemann sums. This argument is uniform in the actual label $z$.

Consequently, for any functions $h_X$ of the exact early landing label with $|h_X|\le1$,
\[
   \mathbb E[F(E_i)h_X(Y_i)]
        -\mathbb EF(G)\,\mathbb E h_X(Y_i)\to0.                         \tag{8}
\]
For a full octave use (7) in the template, whose $\sum_z h_{B'}(z)$ stays bounded for the fixed template, and send the template error to zero last. Taking $X'=A_iX+O(1)$ changes the clock centre by $O(1)$ and scale by a relative $o(1)$.

Here the actual inputs run through one fixed progression of odd step $A_i$. To justify (8) on that progression, compare its point to the same point plus each fixed offset $0\le j<A_i$. The [counted-pair displacement input](ALL_SEMIPRIME_COMPONENTS.md) bounds failure of equal-date fusion by $O_j(t_0^{-1/2})$ on uniform binary residue classes at time $t_0\to\infty$. The progression source uses an odd multiplier, so its residues differ from uniform by $O(2^{t_0}/X)$. Choose $t_0$ a sufficiently small constant times $\log(X/B')$. Every true state before then exceeds $B'$ since each step is at least half its input. Successful fusion preserves the exact first landing, time and all its future data. Averaging the offsets fills an ordinary octave up to bounded endpoints. This proves the claimed transfer, including any moving $h_X$. The full array of the $r$ different labels has not been factored.

## The scalar critical continuation

For the fixed target $y$ use its genuine first shortcut time $T_i$, with a cemetery at infinity. Its finite mass tends to $d$, and the finite subprobability of
\[
              W_i=(T_i-m_X)/b_X,\qquad m_X=L/a,\quad b_X=\sigma\sqrt L,
\]
converges to $d$ times standard Gaussian measure. This is the source-qualified fixed-target clock theorem obtained in [PR 215, equations (6)–(7), with the signed source proof and prior Leen attribution](https://github.com/GettysburgResearch/collatz/blob/7902faf17d50851b46cdcd420ae479d19f0c845c/research/astra-nine-hour-20261128/escape/phase2/NATIVE_BINOMIAL_TRANSFER.md). Its cumulative-cutoff form passes to octaves by subtraction, since a bounded shift in $\log X$ is negligible on the fluctuation scale; fixed odd-step progressions then follow by the same counted fusion. For the alternative moving first-odd floor $B$ use $m_X=a^{-1}\log(X/B)$ and $b_X=\sigma\sqrt{\log(X/B)}$. Its finite mass tends to one and its normalized law tends to the standard Gaussian by the full first-landing theorem and (7). Both definitions give $c_X=\sigma\sqrt{v'}/b_X\to c$.

Let $J_i$ be the genuine event of a finite late clock. On that event the early landing must occur since $y\le B'$ or $B\le B'$ for large $X$. The complete late clock is exactly $Q_i$ plus the remaining time from $Y_i$ to the specified target or floor, including zero when already there. Put
\[
    R_i=\frac{T_i-Q_i-(m_X-s)}{b_X}\quad(J_i=1),
\]
and give it a cemetery symbol on failure. Then $R_i$ and $J_i$ are functions of $Y_i$ apart from the negligible early cemetery. On $J_i=1$,
\[
                           W_i=c_X E_i+R_i.                              \tag{9}
\]
The finite parts of $R_i$ are tight because the finite late $W_i$ and the full early $E_i$ are tight. Thus every joint subsequential limit has $G_i$ independent of its own pair $(J_i,R_i)$ by (8). On the finite event the known characteristic function of $W_i$ is $d e^{-u^2/2}$ before normalizing its mass. Equation (9) factors it as $e^{-c^2u^2/2}$ times the Fourier transform of the finite subprobability of $R_i$. Hence this subprobability is exactly the Gaussian of variance $1-c^2$ times $d$. In particular, conditional on finite arrival, the pair $(G_i,W_i)$ is bivariate standard normal with correlation $c$, and $J_i$ is independent of $G_i$. This scalar joint law is unique even when the coupling between different late clocks has subsequential choices.

Set $Z_i=W_i/\sqrt d$ on finite arrival and $Z_i=0$ on failure, using $d=1$ for the growing floor. In every joint weak limit $\mathbb EZ_i=0$, $\|Z_i\|_2=1$ and $\langle Z_i,G_i\rangle=c\sqrt d$. These moments refer to the limiting Gaussian finite part and its specified atom. They do not presume a uniform second moment for rare finite hitting times in the prelimit.

View the $Z_i$ as vectors in the limiting real $L^2$ space and the $G_i$ as an orthonormal list. For any projection $P_k$ onto a subspace of dimension at most $k$,
\[
 r c\sqrt d
  =\sum_i\langle Z_i,G_i\rangle
  \le\sqrt{r k}+
       \sqrt{r\sum_i\|(I-P_k)Z_i\|_2^2}.
\]
Indeed $\sum_i\|P_kG_i\|_2^2\le k$ by Bessel, $\sum_i\|P_k Z_i\|_2^2\le r$, and Cauchy–Schwarz bounds the residual. For the best $k$-dimensional approximation the error sum is the tail of the covariance eigenvalues, by the singular values of the map sending coordinate basis vectors to $Z_i$. This proves (4).

## Positive entropy on every fixed family

Let $B_i=1_{G_i\le0}$ and $F_i=1_{J_i=1,\,W_i\le0}$ in a joint limit. The early $B_i$ are independent fair bits. The own-event table is (2), since a standard correlated Gaussian pair has negative-quadrant probability $1/4+\arcsin(c)/(2\pi)$. For example this follows by writing the pair as the projections of a rotationally uniform planar Gaussian onto directions separated by $\arccos c$. For actual $A_i n+e_i$ the cutoff in (1) differs from $L/a$ by $O(1)$ on an octave, and the finite limiting Gaussian puts zero mass at the decision threshold. Hence the actual deadline bits have precisely these limiting coordinates.

For any joint coupling with this information,
\[
 \begin{aligned}
 H(F_1,\ldots,F_r)&\ge I((F_i)_i;(B_i)_i)\\
  &=\sum_i H(B_i)-H((B_i)_i\mid(F_i)_i)\\
  &\ge\sum_i\bigl(H(B_i)-H(B_i\mid F_i)\bigr)=rI_d.
 \end{aligned}
\]
Finite entropy is continuous in the joint bit law. Every subsequential limit therefore satisfies (3). This is a lower bound on the actual pattern distribution, rather than a count of possible symbolic words in an unrestricted model.

## Logarithmic sampling and the exact rational-dilation field

We specify the limiting system rather than assume that all ordinary-octave joint limits are invariant. Set $w=L^{1/4}$ and sample $n\in[X,Xe^w]$ with probability proportional to $1/n$. The same octave conclusions hold here with $B',B,m_X,b_X,s$ kept fixed throughout this source window. One justification is to choose $\log X'$ uniformly on $[L,L+w]$ and then sample an ordinary octave $[X',2X')$. On the interior the unnormalized input mass is $\int_{n/2}^n dX'/(X')^2=1/n$ up to relative rounding error $O(1/X)$; the strips at the two ends have normalized mass $O(1/w)$. Across the window $\log X'=L+o(\sqrt L)$, uniformly. Equations (5)–(8), the marginal late-clock law, and the early functional limit remain uniform by applying their sequence forms to any sequence of such octave scales. In (5) the initial difference $\log x-L$ is now uniformly $o(\sqrt L)$, sufficient for the same inversion. The use of the current site's centre in (1) changes it by $o(\sqrt L)$, as required.

Initially index the field by $\mathcal M=\{m\in\mathbb N:(m,6)=1\}$. At each index $m$ record the standardized early first landing $E_m$, the late finite/cemetery flag, and its finite standardized late clock (zero if missing). Take any weak limit of these countably many coordinates along a subsequence. Tightness on every coordinate and a diagonal argument give such joint limits; for a statement about any preselected late-coordinate limit, extract its early fields along a further subsequence.

These joint laws are stationary under each $h\in\mathcal M$. Indeed inputs $mn$ for the shifted index $mh$ agree with the same formula at source $hn$. To spread the progression $hn$, compare $hn$ with $hn+j$ for $0\le j<h$ simultaneously at any fixed finite list of indices $m$. The true pair offsets there are $mj$, so counted equal-date fusion occurs with probability tending to one before a visit to $B'$ or the lower target, by the binary-cell and height-clearance argument for (8). This also applies to the logarithmic source weights by the octave mixture above. Smearing these $h$ offsets replaces the logarithmic progression by the full log-weighted interval $[hX,hXe^w]$ in total variation for the tested records, with rounding and relative weight errors $O_h(1/X)$. Replacing that interval by $[X,Xe^w]$ costs $O_h(1/w)$ in normalized logarithmic mass. Thus the unshifted and shifted finite fields have the same limit.

For clarity, the true native fields also identify the smooth scales two and three in the limiting clock and deadline observables. Doubling changes a late first time by exactly one once the targets lie below the start, and changes an early first time by one as well. For tripling, at odd $x$ the pair $x,3x+1$ meets at date one. The pair $3x,3x+1$ has an equal-date meeting by a large fixed clock with limiting failure $O(t^{-1/2})$ by counted neighbor synchronization. For even $x$ remove the common initial halvings, whose number is tight on each fixed ordinary multiplier progression. Thus the two paths from $x,3x$ meet at tight early dates; the bound on each early height excludes a prior target or floor visit. This is the [physical small-group proof](MULTIPLICATIVE_MEETING_TIME.md), with the meeting times kept rather than merely a matching component. The eventual hit flags agree and any first-clock difference is tight. The late Gaussian finite part has no atom at the normalized deadline. These checks show directly that the fixed deadline observables at a finite collection of smooth-related multipliers agree in the limiting system. The growing floor is kept common when comparing the inputs.

Let $G$ be the group of positive rationals with numerator and denominator in $\mathcal M$, equivalently $\mathbb Q_+^\times/\langle2,3\rangle$. To extend a stationary semigroup field to $G$, define the law at any finite set $g_i$ by using the existing joint law at $Dg_i\in\mathcal M$ for a common denominator $D$. Stationarity removes the choice by passing through a common multiple of two denominators. The consistent finite laws give a stationary $G$-indexed field. For every $g\ne1$, its distinct powers satisfy (3), by common denominators and stationarity. Hence the entropy of the coordinate deadline partition under the discrete shift by $g$ is at least $I_d$ per iterate. The full action similarly has at least $I_d$ per group element along any Følner sequence, by (3) for each finite set. These entropy conclusions hold for the limiting measure; ergodicity of this entire field is unnecessary.

## An absolutely continuous multiplicative spectrum of the genuine critical clock

In this stationary field the $E_g$ are independent standard Gaussians. Let $\mathcal H_0$ be the closed span of the mean-zero square-integrable functions of a *single* $E_g$ as $g$ varies. Different indices give orthogonal spaces. The multiplicative shifts preserve $\mathcal H_0$ in both directions. They act there by the regular shift of $G$ with fibre $L^2_0$ of one standard Gaussian. Thus every vector in $\mathcal H_0$ has absolutely continuous covariance spectral measure on the compact dual $\widehat G$ with respect to normalized Haar measure. Explicitly a vector with square-summable coefficient functions $h_g$ corresponds by Fourier series to an $L^2(\widehat G;L^2_0)$ function, and its spectral density is the squared fibre norm. A vector's projection onto this reducing space and its orthogonal remainder contribute positive measures additively to its covariance spectrum.

For the normalized $Z_1$ used in (4), its projection onto the mean-zero functions of $E_1$ has norm squared at least $d c^2$ by testing against $E_1$. Hence the full absolutely continuous mass is at least $d\theta$. Its density is positive on Haar measure at least $d\theta$ as well: for the subprojection onto the span of the translates of $E_1$, the scalar Fourier coefficient function $C(\chi)$ has $|\int C|=c\sqrt d$ and $\int|C|^2\le1$, so Cauchy–Schwarz gives the support bound. Along any sequence of distinct $g$ the Fourier coefficients of this absolutely continuous subprojection tend to zero. For each fixed invariant field this yields $\liminf_{g\to\infty}\mathbb E|Z_g-Z_1|^2\ge2d\theta$. The limit here means outside finite sets in the discrete group. There is no uniform claim about changing the multiplier with the original finite source scale.

For the binary median deadline $F=f_y$ the projection onto functions of $E_1$ has squared norm
\[
 \operatorname{Var}(\mathbb E[F\mid E_1])
                 =d^2\frac{\arcsin(c^2)}{2\pi}.                         \tag{10}
\]
Indeed conditionally on $E_1=e$ the probability is $d\Phi(-ce/\sqrt{1-c^2})$. Square it by sampling two conditionally independent Gaussian residuals. The resulting two standard clock variables have correlation $c^2$, so the same quadrant formula gives (10). This projects into $\mathcal H_0$ and proves the stated spectral lower. In particular for each such field
\[
     \liminf_{g\to\infty}\Pr(F_g\ne F_1)
                      \ge d^2\arcsin(\theta)/\pi .
\]
A finite-family disagreement bound is also available on ordinary octaves, without any choice of stationary limit. Put $m=d^2\arcsin(\theta)/(2\pi)$, $v=(d/2)(1-d/2)$, and centre $F_i$ in any joint limit. The standardized single-$G_i$ projection of $F_i$ gives an orthonormal family $U_i$ with $\langle F_i-\mathbb EF_i,U_i\rangle=\sqrt m$. Apply the proof of (4) to $(F_i-\mathbb EF_i)/\sqrt v$ and $U_i$, projecting onto the line spanned by the mean of the $r$ centred bits. Since $r^{-2}\sum_{i,j}\|F_i-F_j\|_2^2$ is twice their mean squared distance to that mean, its liminf is at least $2(\sqrt m-\sqrt{v/r})_+^2$. This is uniform as a formula over arbitrary fixed lists and does not single out an individual pair in advance.

More generally put a square-integrable test $\phi$ on the finite Gaussian clock and any constant on cemetery. Its conditional expectation given $E_1=e$ is $d\,\mathbb E[\phi(ce+\sqrt{1-c^2}G)]+\mathrm{const}$. If $h_j$ are the orthonormal probabilists' Hermite polynomials and $\phi_j=\mathbb E[\phi(G)h_j(G)]$, the centred projection has squared norm
\[
                         d^2\sum_{j\ge1}c^{2j}|\phi_j|^2.
\]
This follows first for polynomials from the Gaussian exponential generating function and then in $L^2$ by density. It is strictly positive whenever the finite profile is nonconstant under Gaussian law. The positive lower describes the limiting spectrum of actual critical observables. Its value vanishes for a pure eventual-hit indicator, as its finite profile is constant.

The last $L^2$ formula is a statement inside the limiting field. A bounded finite-clock test with Gaussian-almost-everywhere continuous profile passes directly from the actual weak convergence. An unbounded or arbitrarily discontinuous prelimit test needs its own approximation or integrability argument. The binary median-deadline test has only the zero threshold discontinuity, which the Gaussian finite part does not charge.

[MedianDeadline.lean](MedianDeadline.lean) proves the finite true-orbit test agrees with (1) for every natural input and target. Any admissible date lies strictly below $5B$ when $n<2^B$, so the implementation searches the first $5(1+\lfloor\log_2 n\rfloor)$ dates, including date zero. The finite Lean examples prove 3 reaches 1 before its cutoff and 27 reaches 1 at date 70 after missing its cutoff. [Independent exact enumeration](check_critical_dilations.py) · [Deadline pattern counts](../../../reports/astra-global-20261128/cycles/CRITICAL_DILATIONS.json)

[The relative endpoint-information law](TERMINAL_INFORMATION.md) identifies the clipped Gaussian ordinary self-information at critical time and the escaping-density coefficient of Shannon entropy at sufficiently late dates. [The precritical pair-word theorem](PRECRITICAL_PAIR_WORDS.md) independently carries empirical synchronous word frequencies through the critical scale.
