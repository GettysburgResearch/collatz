# The sharp law of the iterated logarithm on a true fixed-root inverse ray

**Proposed, source-qualified written theorem.** Let \(V_k\) be the genuine natural-density native inverse ray to a prescribed positive transient target \(a\) prime to three. Write \(d=\log(4/3)\), \(\mu=2/d\), \(\lambda=1/\mu\), and \(Z(k)=\log V_k-\lambda k\). Then almost surely
\[
 \limsup_{k\to\infty}\frac{Z(k)}{(\log3/2)\sqrt{2k\log\log k}}=1,
 \qquad
 \liminf_{k\to\infty}\frac{Z(k)}{(\log3/2)\sqrt{2k\log\log k}}=-1.    \tag{1}
\]
The same limits hold for the native cylinder information minus \(\lambda k\), by its [logarithmic tracking estimate](INVERSE_RAY_CYLINDER_INFORMATION.md). They transfer to the odd inverse valuation clock and real height as stated below. Every fixed residue and nonzero significand Fourier mode in the [joint arithmetic theorem](NATURAL_INVERSE_RAY_EQUIDISTRIBUTION.md) has count or sum discrepancy \(O_{\mathrm{ray},f}(\sqrt{k\log\log k})\); the latter assertion gives an upper bound without an optimal constant for those observables.

The sources are specific. Weaver's Paper 175, §8, couples successive ordinary sources through common odd landings on a geometric sequence of logarithmic heights. Leen's original preprint and moderate-deviation supplement give relative landing laws, an adjustable near-threshold comparison, and Gaussian clock tails against arbitrary bounded landing tests. We use those estimates on sparsely spaced source scales to obtain conditional lower excursions, and a denser family of short genuine trajectories to interpolate the upper constant. A distributional Brownian limit alone would not supply (1). [Weaver, Paper 175, §8](https://rstation.ai/problems/collatz/papers/175) · [Leen, Proposition Transport and Appendix A](https://doi.org/10.5281/zenodo.23269488) · [Leen, original moderate-deviation supplement, Relative landing law and Moderate deviations with clock–landing independence](https://zenodo.org/api/records/23269488/files/collatz-brownian-motion-md.tex/content)

## Common native paths at deterministic logarithmic heights

In this proof \(W_y\) is a uniform odd source in \([y,2y)\). Write \(J_x(W_y)\) for its odd-step first-entrance count at or below \(x\), and \(P_x(W_y)\) for the odd landing; assign a cemetery value on failure. Fix \(r>1,\ t_0>0\), let \(L_i=t_0r^i,\ x_i=e^{L_i}\), and take \(y_i=e^{(1+\delta)L_i}\) with \(0<\delta\le10^{-3}\) fixed. Use either \(r\ge2\), or the single local choice \(r=1.001,\delta=0.001\). Thus \(y_{i+1}\ge x_i^{1.001}\). All asymptotics in \(i\) take these parameters fixed first.

The successful odd landing laws at \(x_i\) for \(W_{y_i}\) and \(W_{y_{i+1}}\) differ in total variation by \(O_{\delta,r}(L_i^{-c})\) and have missing masses of that order. For \(y_{i+1}\) use Leen's *Transport* and relative landing law; at \(y_i\) use Appendix A's *Timed relative passage on a general source interval* at frequency zero with \(e_-=1+\delta\) and \(e_+=1.001\). The same shell functional \(H_{x_i}\) appears with these fixed source exponents, has total \(1+O(L_i^{-c})\), and also approximates the reference source \(x_i^{1.001}\). The onset can depend on \(\delta\).

Construct a Markov sequence \(W_i\) with these prescribed ordinary marginals. Given \(W_i\), form its landing below \(x_i\), use a maximal coupling of the two finite landing laws to choose a landing for \(W_{i+1}\), and finally sample \(W_{i+1}\) from its correct conditional uniform-source law given that chosen landing. Perform this last sampling with fresh randomness at every link. The probability of disagreement or cemetery at link \(i\) is summable. Eventually the odd point \(P_i=P_{x_i}(W_i)=P_{x_i}(W_{i+1})\) is shared at every link.

We record three short-block facts about \(W_i\); the statements hold eventually almost surely. With an absolute \(C\) independent of the fixed small \(\delta\),
\[
 \log P_i=L_i+O(\log L_i),\qquad
 \left|J_{x_i}(W_i)-\delta L_i/d\right|\le C\sqrt{\delta L_i\log i}.
                                                                         \tag{2}
\]
Indeed put \(m=\lceil 20\delta L_i\rceil\). Through \(2m+2\) shortcut bits the odd-source complete-grid error is exponentially small in \(L_i\). On the independent tape after the first fixed one, the maximum centered odd count up to \(2m+1\) is at most \(C_0\sqrt{\delta L_i\log i}\) with summable failure probability, by the exponential martingale maximal inequality with \(C_0\) absolute (any fixed \(\delta>0\) is taken before \(i\to\infty\)). The longest zero run there is \(O(\log L_i)\) with summable failure probability by the union bound. All these true heights are at least \(y_i 2^{-2m-2}\), exponentially large in \(L_i\), so their cumulative nonlinear log correction tends to zero. At date \(m\), the expected homogeneous drop is \(m/\mu>\delta L_i\) by a fixed factor. Hence the first native value at most \(x_i\) occurs by date \(m\); that value is at least \(x_i/2\), and the first subsequent odd value comes after at most \(O(\log L_i)\) more halvings. This gives the first claim of (2). At the odd landing, the native duration \(b\) satisfies \(b=2J_{x_i}(W_i)+O(\sqrt{\delta L_i\log i})\). Substitution in the native log product gives the second claim; the \(O(\log L_i)\) overshoot is eventually smaller than \(\sqrt{\delta L_i\log i}\) for each fixed \(\delta\). The same argument with \(m=\lfloor L_i/10\rfloor\) shows for the local choice of \(r,\delta\) that both \(P_{i+1}\) and \(P_i\) are reached on \(W_{i+1}\) within its first \(L_i/4\) native dates, since \(\log(y_{i+1}/x_i)=0.002001L_i\).

In particular the successive shared \(P_i\)'s have strictly increasing heights eventually. On \(W_{i+1}\)'s actual forward trajectory the first upper-threshold entrance \(P_{i+1}\) precedes \(P_i\). The events that \(W_i\) reaches \(a\) eventually coincide along the coupled sources: for these high shared odd landings, reaching \(a\le x_i\) earlier would force an odd landing at \(a\) or its odd part before the high \(P_i\). On eventual success the nested paths from \(P_i\) down to \(a\) specify an infinite inverse ray. Its conditional law is exactly \(\mathsf Q_a\). Indeed for each fixed native depth the suffix of every sufficiently late \(W_i\) agrees with that ray, since \(P_i\to\infty\) forces its distance to \(a\) to diverge. For each such fixed suffix the ordinary octave probability tends to the basin density of its ancestor endpoint, by Leen's fixed-target and progression laws; the eventual success event has probability \(h(a)>0\). Division gives the natural cylinder probability. This also proves that any almost-sure property of these coupled successful paths holds for the original prescribed-root law.

## A uniform small-interval modulus on the fixed ray

Let \(b_i\) denote the native depth of \(P_i\) on the successful ray. Use the local \(r,\delta\) choice first. From (2) and the earlier almost-sure speed, \(b_i\sim\mu L_i\). Also \(b_{i+1}-b_i\gg L_i\): the log-height gap is \((r-1)L_i+O(\log L_i)\), while a true native inverse edge raises the log height by at most \(\log2\). Every segment between these marks is a subinterval of the short, genuinely sampled prefix of \(W_{i+1}\).

There is an absolute \(C_1\) such that for every sufficiently small fixed rational \(\eta>0\), almost surely
\[
 \limsup_{K\to\infty}
 \frac{\displaystyle\max_{\substack{K\le n\le m\le 2K\\m-n\le\eta K}}
                   |Z(m)-Z(n)|}{\sqrt{K\log\log K}}
                          \le C_1\sqrt{\eta}.                           \tag{3}
\]
Here \(K\) runs through all positive integers. To verify this, subdivide the first \(L_i/4\) native bits of \(W_{i+1}\) into consecutive blocks of length \(\lceil\eta L_i\rceil\). Each block has maximal centered parity deviation at most \(C_2\sqrt{\eta L_i\log i}\) outside a set of probability \(O(i^{-3})\), with \(C_2\) absolute, by the same complete-grid estimate and exponential martingale bound. The first fixed odd has bounded effect. There are \(O(1/\eta)\) blocks per prefix; \(\eta\) is fixed before Borel–Cantelli. Every subinterval of length \(O(\eta L_i)\) meets a bounded number of blocks (the constant in this length bound below is fixed independently of \(\eta\)). Native log drift differs from the centered parity sum times \(\log3\) by \(o(1)\) on the whole prefix. Reverse chronological order changes the sign of the centered increment only. For \(K\le n\le m\le2K\), every intersected segment has \(L_i\asymp K\); by the lower bound on mark spacing, an interval of length \(\eta K\) meets at most two marks for all sufficiently small fixed \(\eta\). This gives (3), with \(\log i\sim\log\log K\). Countably many rational \(\eta\)'s can be used on the same ray. The proof also controls ranges straddling a dyadic endpoint by dividing them or simply choosing \(K\) to be their smaller endpoint.

For the finite-state or Fourier tests from the equidistribution theorem, the same maximal bounded-difference argument on each entire local prefix gives discrepancy \(O_f(\sqrt{L_i\log i})\) on any one of its subintervals. For nonzero Fourier modes the multiplicative phase in a chronological subinterval is included in the cumulative test; applying the maximal inequality to the original weighted partial sums controls all differences. The true nonlinear correction and the complete-grid errors remain exponentially small. Summing these bounds geometrically over the successive segments, with at most one partial segment, proves the asserted \(O_f(\sqrt{k\log\log k})\) discrepancy at all depths.

## The sharp positive and negative excursions on sparse scales

Let \(r\ge2\) be fixed and use the general small \(\delta\). Put \(\sigma_J^2=2(\log2)^2/d^3\). Let \(q_i\) be the number of odd arrivals in the outward ray through the depth \(b_i\); equivalently it counts odd departures on the forward segment \(P_i\) down to, and excluding, \(a\). Write
\[
 U_i=q_i-L_i/d,\qquad B_i=\sigma_J\sqrt{2L_i\log i},\qquad
 A_i=J_{x_i}(W_{i+1})-\log(y_{i+1}/x_i)/d .
\]
On successful links the native ancestry gives exactly
\[
 U_{i+1}-U_i=A_i-\bigl(J_{x_{i+1}}(W_{i+1})-\delta L_{i+1}/d\bigr).
                                                                         \tag{4}
\]
The last term is bounded by (2). Write \(s=\sqrt{1+\delta-1/r}\); the Gaussian variance scale of \(A_i\) in the cited moderate-deviation theorem is \(\sigma_J^2 s^2 L_{i+1}\). Since \(\log\log y_{i+1}\asymp i\), the arguments \((1\pm\epsilon)\sqrt{2\log i}\) lie within that theorem's zone. Its lower and upper tails, together with the relative landing law, imply for each fixed \(0<\epsilon<1\) the following three assertions on the coupled sequence.
\[
 \begin{gathered}
 |A_i|\le(1+\epsilon)s\,\sigma_J\sqrt{2L_{i+1}\log i}
        \quad\text{eventually},\\
 A_i\ge(1-\epsilon)s\,\sigma_J\sqrt{2L_{i+1}\log i}\quad\text{infinitely often},\\
 A_i\le-(1-\epsilon)s\,\sigma_J\sqrt{2L_{i+1}\log i}\quad\text{infinitely often}.
 \end{gathered}                                                         \tag{5}
\]
The first is the ordinary summable Gaussian tail. For the other two, fix one sign, let \(\nu_i\) be the outer successful landing measure at \(x_i\), and let \(p_i=\overline\Phi((1-\epsilon)\sqrt{2\log i})\). Uniformly for each landing subset \(E\), the outer joint probability of the specified tail and landing in \(E\) is \((1+O(L_i^{-c}))p_i\nu_i(E)+O_A(L_i^{-A})\), for every fixed \(A\). This is precisely *Moderate deviations with clock–landing independence*, using *Relative landing law* to replace the shell functional by \(\nu_i\). Both theorem hypotheses hold at \(y_{i+1},x_i\), since their logarithms are in fixed ratio with \(y_{i+1}\ge x_i^{1.001}\). Taking for \(E\) the subset where the conditional tail probability is below \(p_i/2\) shows that this bad subset has \(\nu_i\)-mass \(O_A(L_i^{-A}/p_i)\). The inner landing of \(W_i\) has this exceptional mass plus \(O(L_i^{-c})\), summable in \(i\). Also, by the maximal coupling bound and Markov's inequality, the inner landing values with conditional matching probability below \(1/2\) have summable probability. The cemetery is eventually absent. Thus almost surely, conditional on the history through \(W_i\), the chance of a match followed by this tail at \(W_{i+1}\) is at least \(p_i/4\) at all large \(i\). The fresh conditional draw in the construction is essential here. Since \(\sum_i p_i=\infty\), the conditional Borel–Cantelli lemma gives infinitely many such events. Applying it to both signs proves (5), also after restriction to eventual target success.

Sum (4) from a fixed attained mark, using \(B_{i+1}/B_i\to\sqrt r\). There is an absolute \(C_3\), independent of \(r,\epsilon,\delta\), such that almost surely
\[
 \limsup_i |U_i|/B_i\ \le\
 K_*=\frac{(1+\epsilon)s+C_3\sqrt\delta}{1-r^{-1/2}} .
\]
At each of the two kinds of infinitely often dates in (5), (4) moreover gives, with its appropriate sign,
\[
       \limsup_i (\pm U_i)/B_i
             \ \ge\ (1-\epsilon)s-C_3\sqrt\delta-K_*/\sqrt r .         \tag{6}
\]
These conclusions use only fixed choices of parameters, so no uniformity in the external comparison constants is required.

## All native dates and the exact constant

The native product and the finite correction sum on the ray give
\[
 Z(b_i)=-\frac{d\log3}{2\log2}\bigl(q_i-\log P_i/d\bigr)+O_{a,\rm ray}(1).
\]
By (2) one may replace \(\log P_i\) by \(L_i\) in the parentheses at cost \(O(\log L_i)=o(B_i)\). Also \(b_i/(\mu L_i)\to1\), and in fact \(|b_i-\mu L_i|=O_{\rm ray}(\sqrt{L_i\log i})\), from the bound for \(U_i\) and the product. Since \(d\sigma_J/(\log2\sqrt\mu)=1\), (6) gives the same upper and signed lower constants for the normalized \(Z(b_i)\), with the two signs interchanged. Formula (3) allows replacement of \(b_i\) by the **deterministic** \(n_i=\lfloor\mu L_i\rfloor\) at cost \(o(\sqrt{L_i\log i})\): their separation is \(o(L_i)\); apply (3) at each fixed rational \(\eta\), then send \(\eta\) to zero. The modulus concerns the physical ray regardless of which coupling supplied these new marks. Thus the bounds now hold at the deterministic dates for \(\mathsf Q_a\) itself.

For the lower constants in (1), take countably many fixed choices \(r\to\infty,\delta\downarrow0,\epsilon\downarrow0\). The right side of (6) tends to one. For the upper constant, keep these parameters fixed initially and use all the finitely many starting offsets \(t_0=r^{j/H}\), \(0\le j<H\). Their deterministic dates interlace into a grid of consecutive ratios tending to \(r^{1/H}\), with the same upper constant \(K_*\) on each. Every large native date lies within a relative distance \(O(r^{1/H}-1)\) of the preceding grid date. Equation (3) controls the intervening difference, and the normalizing \(\sqrt{k\log\log k}\) varies by a ratio tending to one as \(H\to\infty\). Use countably many increasing integers \(H\) and take \(H\to\infty\), then \(r\to\infty,\delta,\epsilon\to0\). This proves the upper constant one in (1).

For odd depth \(j\), \(D_j\), the native date of the \(j\)-th outward odd, is \(2j+O(\sqrt{j\log j})\) almost surely by the earlier theorem. All large native dates \(k\) are therefore within \(o(k)\) of \(D_{\lfloor k/2\rfloor}\); (3) shows that both sharp signs persist along the odd dates. The exact identities \(\log V_{D_j}=\log a+D_j\log2-j\log3+O_{a,\rm ray}(1)\) and \(D_j/j\to2\) then give the two signs with coefficient \(\log2\) for \((\log V_{D_j}-dj)/\sqrt{4j\log\log j}\), and coefficient one for \((D_j-2j)/\sqrt{4j\log\log j}\). The equivalent canonical odd law at a transient root, and its finite exit from a periodic unit root, preserve these almost-sure limits. The limsup and liminf refer to the infinitely continued inverse path and leave the fixed target's forward behavior open.
