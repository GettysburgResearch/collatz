# Absolute-width real strips forced by one escaping source

**Status.** Written consequence for the true ordinary canonical inverse fibres. It turns singularity at one fixed source into growing mass at every sufficiently late ordinary point of its putative escape. No pointwise upper bound of the required order is proved here.

Let \(\lambda_y=h(y)\mu_y\), where \(h\) is the stationary integer trace and \(\mu_y\) is the physical canonical inverse real-offset law at a positive odd unit. Assume the counted-synchronization, ordinary positive trace and first-passage hypotheses of [PR193's fixed-root singularity theorem](https://github.com/GettysburgResearch/collatz/blob/795cfa38fbd6a2436285edfe82580680df4f9b0d/research/astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md). In particular \(\mu_y\) is carried by a set of zero Hausdorff measure for \(g_s(r)=r(\log(1/r))^s\) for \(0\le s<1/2\). [Weaver, Paper 175, Theorem 3](https://rstation.ai/problems/collatz/papers/175)

Suppose \(m\) is one fixed odd unit in an escaping component and \(a_n=S^n m\). Write \(F(x)=\prod_{i\ge0}3S^ix/(3S^ix+1)\), \(P(x)=x/F(x)\), \(b_n=P(a_n)/P(m)\), and let \(\beta_n=a_n-b_n m\) be its own word's real affine offset. For a fixed real code \(r\) in the canonical fibre of \(m\), put \(c_n(r)=\beta_n+b_nr\). At every \(n\) the infinite inverse histories from \(a_n\) whose reversed prefix reaches \(m\) give the exact submeasure
\[
                     \lambda_{a_n}\ \ge\
                   b_n (r\mapsto\beta_n+b_n r)_*\lambda_m.          \tag{1}
\]
This is the finite inverse-cylinder probability telescope with the physical real-coordinate composition. Since \(b_n\to\infty\), for \(\mu_m\)-almost every *fixed* \(r\) one has
\[
     \lambda_{a_n}([c_n(r)-1,c_n(r)+1])\longrightarrow\infty .
                                                                        \tag{2}
\]
Indeed \(\lambda_m([r-u,r+u])/u\to\infty\) at \(\lambda_m\)-almost every point by differentiation of one-dimensional Lebesgue measure with respect to the singular measure \(\lambda_m\). Use \(u=1/b_n\) in (1).

There is \(\delta_m>0\) such that all these intervals lie inside \([\delta_m a_n,(1-\delta_m)a_n]\) for large \(n\), uniformly over canonical \(\mu_m\)-typical \(r\). In fact \(1-c_n(r)/a_n=(P(a_n)/a_n)(m-r)/P(m)\). The uniform distinct-path bound at the nonperiodic root puts \((m-r)/m\) in \([b,1]\) for an absolute \(b>0\); also \(m/P(m)=F(m)<1\) and \(P(a_n)/a_n\to1\). This is a bound in ordinary absolute real units at a position proportional to the actual moving terminal.

At \(\mu_m\)-almost every \(r\), for every fixed \(0<s<1/2\),
\[
 \limsup_{n\to\infty}
 \frac{\lambda_{a_n}([c_n(r)-1,c_n(r)+1])}{(\log a_n)^s}=\infty.   \tag{3}
\]
For a measure supported on a \(g_s\)-Hausdorff-null set, its upper interval density relative to \(g_s\) is infinite at almost every point. Otherwise a positive restriction with a uniform finite upper bound at small radii would give positive Hausdorff measure by the elementary mass distribution bound. For each witness radius \(u\downarrow0\), take \(n\) just before the first \(b_{n+1}>1/u\). Since the upward multiplier \(b_{n+1}/b_n=3\,2^{-e(a_n)}\le3/2\), we have \(u\le1/b_n<(3/2)u\). Thus the interval in (1) contains the witness interval, and its radius changes by only a fixed factor. Finally \(\log b_n=\log a_n+O_m(1)\). A countable sequence of \(s\)'s tending to \(1/2\) gives the assertion simultaneously for all smaller \(s\).

Consequently any upper bound \(O_\delta((\log(2+y))^s)\), with one \(s<1/2\), on all absolute-width-two strips inside \([\delta y,(1-\delta)y]\) of every nonperiodic positive odd unit would exclude every escape if available for each fixed \(0<\delta<1/2\). Conversely if all ordinary orbits are eventually periodic, for each \(\delta\) only finitely many nonperiodic targets have any such mass: every simple inverse history with relative offset at least \(\delta\) visits a fixed small floor by the uniform reciprocal tail, and the forward orbits from the finite floor are then finite. No assumption excluding additional cycles is needed.

Paper 19's uniform stationary product-ball bound is \(O(s_0^2\log(e/s_0))\) at radius \(s_0\). Covering a fixed absolute real strip at ternary precision \(3^{-k}\) yields \(O(k)\) after multiplication by \(3^k\). This depends on ternary resolution and is neither the estimate in (3) nor a bound uniform as \(k\to\infty\) at a fixed integer terminal. The finite high-odd suffix from \(m\) to \(a_n\) is common to all the histories in (1); their fine concentration is inherited from the original untilted fibre at \(m\). [Weaver, Paper 19 v2, §10.1, (S2)–(S4)](https://rstation.ai/problems/collatz/papers/19)

## An outer band with an unconditional upper bound

There is a finite \(Y_0\) such that every nonperiodic odd unit \(y>Y_0\) has
\[
                    \lambda_y([y/5,y])=0 .                           \tag{4}
\]
Here the upper bound uses the published verification through \(2^{68}\). Take for \(Y_0\) the largest integer on the finitely many forward orbits from \([1,2^{68}]\), all of which reach \(1\). No positive inverse path to such a \(y\) can meet that floor, and every finite backward segment from a nonperiodic \(y\) is simple, including its shortcut states. Weaver's rational bound for distinct shortcut segments above this floor is \(c=216449006435109/10^{15}\) in natural logarithms. The exact partial product for the inverse real code then gives \(R_k/y\le 1-e^{-c}<1/5\), uniformly in the word. The strict numerical bound follows for example from \(\log(5/4)\ge 1/4-1/32=7/32>c\). Take the infinite path limit. The same argument applies on an entire escaping component, irrespective of the size of a particular target. Its own macroscopic witness in (2) can lie below \(y/5\). [Weaver, Paper 175, §11, (23)](https://rstation.ai/problems/collatz/papers/175)

The independent [fixed-floor distortion calculation](../descent/DISTORTION.md) and the cited verification through the larger cutoff give the stronger outer constant \(1/6\): for simple segments entirely above \(2^{71}\), their multiplicative distortion is bounded by the exponential of a constant strictly below \(\log(6/5)\). Increase \(Y_0\) to cover the finite known orbits through that floor. Then the same proof yields \(\lambda_y([y/6,y])=0\) for all sufficiently large nonperiodic \(y\).

## Exact transport throughout each interior band of an escape

Fix an escaping ordinary component \(C\), its ray \(a_n\), and \(0<\delta<1\). There is \(N=N(C,\delta)\) such that at every \(n>N\), *all* the canonical measure on \([\delta a_n,a_n]\) is inherited from \(a_N\):
\[
 \left.\lambda_{a_n}\right|_{[\delta a_n,a_n]}
   =\left.\left[
    \frac{b_n}{b_N}
       (r\mapsto a_n-(b_n/b_N)(a_N-r))_*\lambda_{a_N}
           \right]\right|_{[\delta a_n,a_n]}.                        \tag{5}
\]
Choose a floor \(B(\delta)\) so that the sum of \(\log(1+1/(3x))\) on the part of any simple positive shortcut path with \(x>B(\delta)\) is strictly less than \(-\log(1-\delta)\). The uniform reciprocal tail exists by the bounded-multiplicity path sparsity estimate. A history with \(R_\infty\ge\delta a_n\) must visit some odd \(u\le B(\delta)\). The finitely many such \(u\) in \(C\) have joined the ray by a common finite index \(N\); increase \(N\) past their own ray indices as necessary. Every such history at \(a_n\) passes through \(a_N\). The histories with this prescribed prefix give the right-hand canonical submeasure exactly by (1). Restriction now gives equality. [Weaver, Paper 176, §4, orbit packing](https://rstation.ai/problems/collatz/papers/176)

This applies to every *fixed* relative band even when \(\delta\) is much smaller than \(1/5\). It identifies where a unit-strip estimate has to use fresh arithmetic information. After the finite meeting index, the entire high-odd suffix is shared by all histories in the band. Reweighting independent mismatches on that suffix does not estimate the unknown fine scale structure at its input.

## A long consecutive interval of large physical strip masses

On any escape as above, for \(\mu_m\)-almost every fixed \(r\) there are increasing \(n_j\) and real intervals \(I_j\) with
\[
 \begin{gathered}
 c_{n_j}(r)\in I_j\subset[\delta_m a_{n_j},(1-\delta_m)a_{n_j}],
 \qquad |I_j|\longrightarrow\infty,\qquad |I_j|/a_{n_j}\longrightarrow0,\\
 \inf_{\substack{J\subset I_j\\ |J|=1}}\lambda_{a_{n_j}}(J)
                          \longrightarrow\infty .                    \tag{6}
 \end{gathered}
\]
This does not give the logarithmic lower rate of (3) simultaneously for every strip in \(I_j\).

Partition a bounded interval containing \([0,m]\) into \(2^k\) equal dyadic descendants at level \(k\); denote by \(Q_k(r)\) the cell containing \(r\). Endpoints are harmless by the atomless fibre theorem. Its entropy satisfies \(H_k=k\log2+o(k)\). In fact the lower local dimension one bounds \(\liminf[-\log\mu_m(Q_k(r))]/(k\log2)\) from below by one almost everywhere, since the cell lies in a comparable centered ball; use Fatou and the maximal entropy bound \(H_k\le k\log2\).

Fix a positive integer \(d\). Write \(\Delta_k=k\log2-H_k\). The \(\mu_m\)-average entropy deficit of the conditional vector of \(2^d\) subcells inside its parent cell \(Q_k\) is \(\Delta_{k+d}-\Delta_k\), by the entropy chain rule. Its Cesàro mean over \(k<K\) tends to zero, by cancellation of all but \(2d\) end terms and \(\Delta_k=o(k)\). A probability vector with some entry below \(2^{-d-1}\) has a positive entropy deficit depending only on \(d\), by compactness and the unique maximizing uniform vector. Thus the Cesàro mean of the probability of a bad parent tends to zero. Fatou gives zero lower limiting frequency of bad parents almost surely, hence infinitely many good \(k\) for each \(d\). Intersect these probability-one conclusions over \(d\).

At the same typical point, the dyadic differentiation theorem applied to Lebesgue measure relative to singular \(\mu_m\) gives \(\mu_m(Q_k(r))/|Q_k(r)|\to\infty\). This can equivalently be obtained by differentiating both measures relative to their sum on the refining dyadic partitions. For each increasing \(d\), choose a good \(k\) as large as needed, and take the first \(n\) with \(b_n|Q_k|\ge 2^d/4\), enforcing increasing \(n\). By the upward gain bound \(b_n/b_{n-1}\le3/2\), each of the \(2^d\) transported children has length between \(1/4\) and \(3/8\). Any unit interval inside \(I=\beta_n+b_n Q_k\) contains a whole child. By (1) its mass is at least
\[
         b_n h(m)\,2^{-d-1}\mu_m(Q_k)
                  \ \ge\ \frac{h(m)}8\,\frac{\mu_m(Q_k)}{|Q_k|}.
\]
The right side can be made arbitrarily large while \(|I|\ge2^d/4\). Since \(b_n/a_n\) stays bounded and \(|Q_k|\to0\), the relative length tends to zero. The compact interior placement follows from the previously proved endpoint margin, shrinking \(\delta_m\) if necessary. This proves (6).

In particular the closed global gaps do not by themselves give uniform porosity of the actual affine cylinders at their own scale. A finite inverse prefix at \(m\) with endpoint \(x\), multiplier \(A\) and offset \(R\) carries the raw mark \(R+A R_x\). Its possible tail has a bounded-real typical part of width \(O(A)\). A fixed forbidden interval in the normalized mark \(1-R_x/x\) has raw displacement and width of order \(x\), which after transport is order \(Ax\), not \(A\). Here \(Ax=m-R\) is bounded away from zero on nonperiodic prefixes. Nor do all other prefixes have to avoid a gap specific to one selected prefix. Equation (6) gives actual increasingly long regions with substantial mass in every unit subinterval, even though their relative centres lie near a fixed compact null set.

## The one-sided finite-source lower bound at all intermediate scales

The one-sided lower estimate in [PR193's closed-support theorem, (4),(6)](https://github.com/GettysburgResearch/collatz/blob/2796977d3f02ad57daeb7510f16da29527f9afde/research/astra-six-hour-20261127/escape/CLOSED_CORRECTION_SUPPORT.md) also implies a lower bound at every point of the closed **unit-ended** finite correction set. On a compact interior range, uniformly in its centre \(\theta\) and all sufficiently small \(r>0\),
\[
                             \nu(B(\theta,r))\ge c r.                  \tag{7}
\]
Here \(\nu\) is the fixed-root canonical law of the multiplicative mark, or the bilateral \(J\)-law in one fixed escaping component. The constant may depend on that root or component. For the first choice use \(s(x)\) equal to the finite correction to the first target; for the second use \(s(x)=F(x)\). In both cases \(s(Sx)-s(x)=s(x)/(3x)\), the factors are uniformly bounded away from zero, and every increasing deterministic future reaches or approaches one.

Take a unit \(x\) with \(|s(x)-\theta|<r/8\). Follow its path until \(s\) exceeds \(\theta+r/2\). If one of the successive increments is at least \(\epsilon r\), its lower vertex has height \(O_\epsilon(1/r)\). Apply the cited one-sided estimate there at \(M=C_\epsilon/r\), choosing the constant large enough that the guaranteed interval lies inside \(B(\theta,r)\). Otherwise each increment \(\ell=s(Sz)-s(z)\) is at most \(\epsilon r\), with \(\ell\asymp 1/z\). Applying the estimate at \(M=z\) around its lower end gives a symmetric interval of radius \(C\ell\) carrying mass at least \(c\ell\); choose \(C\ge1\) also to cover the edge. These intervals stay inside \(B(\theta,r)\) by choosing \(\epsilon\) sufficiently small. Their union covers length at least \(3r/8\). A disjoint subfamily whose fixed dilates cover their union (the finite interval covering lemma) has total length at least a constant times \(r\). Summing its mass bounds proves (7). Unit-ended restriction ensures the required one-sided estimate at every lower vertex, including the chosen initial one. A linear lower bound of this kind is consistent with a singular full-dimensional fibre.
