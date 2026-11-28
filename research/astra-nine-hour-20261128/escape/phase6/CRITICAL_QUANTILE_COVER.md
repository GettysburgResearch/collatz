# The sharp mass-covering scale of ordinary terminal corrections

Let \(\nu_r\) be the natural first-minimum log-correction measure on a fixed positive-mass minimum cell, in natural log units. At mesh \(1/T\) use the half-open grid on the real line. For \(0<\alpha<\nu_r(\mathbb R)\), let \(N_\alpha(T)\) be the least number of cells carrying mass at least \(\alpha\). Under the signed-trit, fixed-target-clock and Weaver marked-ray inputs,
\[
                    N_\alpha(T)\asymp_{r,\alpha} T/\sqrt{\log T}.
                                                                        \tag{1}
\]
In particular this controls the genuine minimum-one law. The upper estimate comes from Weaver's explicit covers, not just the statement of Hausdorff nullity. The lower estimate uses ordinary source sampling at the moving resolution. It concerns fixed-scale quantiles; it is not an assertion of positive Hausdorff measure at the endpoint gauge.

On every actual escaping odd-unit ray, let \(\mu_y\) be the canonical probability on the physical real offset at a late root \(y\). Then for every fixed \(0<\alpha<1\) the least number of **unit physical bins** carrying mass \(\alpha\) is
\[
                     \asymp_{C,\alpha} y/\sqrt{\log y}.                \tag{2}
\]
Consequently for every fixed \(0<\delta<1\),
\[
   \inf_{0\le\sigma\le\mu_y,\,\sigma(\mathbb R)\ge1-\delta}
       y\sum_{k\ge0}\sigma([k,k+1))^2
                     \asymp_{C,\delta}\sqrt{\log y}.                   \tag{3}
\]
The same order holds after multiplying by the PR213 weight \(h(y)^2/y^2\), bounded above and below on that ray. The untrimmed energy can still receive additional contributions from bins of vanishing total mass.

## Native source sampling for moving marks

For an odd target \(y\), let \(B_y(n)\) be the sum of \(\log(1+1/(3v))\) over odd departures before its first shortcut hit, defined on its first-hit basin. Denote the ordinary, unweighted, first-hit mark measure by \(\lambda_y\). Uniformly over **every target height**, every \(|g|\le1\) with Lipschitz constant at most \(T\ge2\), and all \(X/T\to\infty\), one has
\[
 X^{-1}\sum_{X<n\le2X:\ n\to y}g(B_y(n))=\int g\,d\lambda_y+o(1).
                                                                        \tag{4}
\]
The same holds with one fixed first-minimum cell in place of the first-hit basin, with constants allowed to depend on that fixed minimum. The argument also constructs the ordinary mean for every fixed Lipschitz test.

Write \(a=\log2,b=\log(3/2)\), \(F(n)=\mathbf1_{n\to y}g(B_y(n))\) and \(U(x)=e^{-x}\sum_{n\le e^x}F(n)\). Except at the target, even steps preserve the mark and odd steps change it by at most \(1/(3n)\). Consequently for \(r(x)=U(x)-[U(x-a)+U(x+b)]/2\), uniformly in these choices,
\[
         |r(x)|\ll_A (1+x-\log T)^{-A}\qquad (x\ge\log T+2).          \tag{5}
\]
Here are the details for the signed term from the odd image. At physical size \(Y=e^x\), discard \(z<\sqrt{YT}\) in the image prefix at a normalized cost \(O(\sqrt{T/Y})\). On any remaining octave of size \(Z\) the signed starting trit can be tested after \(t=\lfloor c\log_2(Z/T)\rfloor\) updates for a small absolute \(c>0\). The terminal label is \(F(T^tz)\). Fewer than \(2^t\) initial integers on the entire line hit the target strictly before date \(t\), by injectivity for each prescribed parity word. All others have the same basin label as their image; before that image their log correction is \(O(t2^t/Z)\). Thus testing with the terminal label costs \(O(2^t/Z+Tt2^t/Z)\) in octave normalization. The signed-term bound is \(O_A((1+\log(Z/T))^{-A})\), by [the original-source marked-trit estimate (3)](../phase2/NATIVE_BINOMIAL_TRANSFER.md), applied on the octave or a partial octave by prefix differences. The few octaves with bounded ratio are covered by the trivial bound. Sum over octaves with their geometric normalization. In the direct first step the positive odd mark adjustment costs at most \(O(\min(2,T/n))\) per start, and the single defective start and the odd image cutoff cost \(O(1/Y)\). This proves (5). For a fixed minimum cell, possible exceptional edges lie below that minimum and the large-octave starting states in this argument all stay above it through the short date. The direct-step cost acquires an additional bounded number of sites.

For fixed parameters the ordinary mean exists from the signed-increment renewal argument used [for the scalar residual](../phase5/NATIVE_MELLIN_RIGIDITY.md). For the moving statement note that \(U\) is uniformly bounded, with \(|U(x+h)-U(x)|\ll |h|+e^{-x}\) for \(|h|\le1\). Along any sequence \(x_0-\log T\to\infty\), the centered profiles \(U(x_0+v)\) admit locally uniform subsequential limits, by the grid bound (or piecewise linear interpolation with vanishing error). Each such bounded continuous limit obeys the zero-residual equation by (5). Iteration with the shifted-binomial variation bound first makes it \(\log3\)-periodic and then \(\log2\)-periodic. Irrationality makes it constant. In particular the oscillation on \([x_0-a,x_0]\) tends uniformly to zero. For any higher start stop the fair size walk on first entry below \(x_0\); the terminal log lies in that interval. The expected total forcing before the crossing is \(o(1)\) uniformly in the higher start by (5) and the unit-strip occupation estimate. Taking the higher start to infinity proves that \(U(x_0)\) differs from its own ordinary mean by \(o(1)\), uniformly in the parameters. Prefix subtraction gives (4). This comparison costs no factor for the number of changes in a Lipschitz test.

## Counting original integers in selected cells

For (1) choose \(X=T^2\). If a union of \(K\) grid cells is selected, majorize its indicator by a function between zero and one, equal to one on the cells and zero outside their \(1/T\)-neighborhood. Its Lipschitz constant is at most \(T\) and its support is covered by at most \(3K\) closed intervals of length \(1/T\), allowing endpoints. Apply (4) in the fixed cell. Among ordinary sources in the shell that hit \(r\), all but a mass with arbitrarily small limiting upper bound satisfy \(|s-\mu\log X|\le B\sqrt{\log X}\) for their first physical time \(s\) to \(r\), by taking a large fixed \(B\) in the true fixed-target Gaussian. Restricting to the minimum cell only decreases the exceptional mass. At such a source, with \(p\) odd departures,
\[
       B_r(n)=\log r+s\log2-p\log3-\log n .
\]
A uniform simple first-hit path bound gives \(0\le B_r(n)\le K_0\). Each \(s\) thus has only \(O(1)\) physical grades \(p\) on the original octave. At a fixed pair \((s,p)\) the original \(n\) giving a specified mark interval of length \(1/T\) lie in an interval containing \(O(X/T+1)\) integers. These are counts of *all* eligible original integers, before even imposing the true parity word. There are only \(O_B(\sqrt{\log X})\) pairs in total. [Fixed-time Gaussian and its source pins](../phase2/NATIVE_BINOMIAL_TRANSFER.md) · [Simple-path correction bound](../phase4/HARMONIC_SOURCE_PHASE.md)

It follows that for every sequence of unions with \(K=o(T/\sqrt{\log T})\) the mark mass tends to zero, after first letting \(T\) and then \(B\) increase. This implies the fixed-quantile lower in (1) by subsequence contradiction. For its upper bound, Weaver §7 gives eventual membership in the mesh-\(2^{-8N}\) cover \(V_{N,1/i}\) for some finite \(i,N_0\), almost surely in the fixed cell. Increasing \(i,N_0\) makes the selected probability arbitrarily near full. Each such cover uses \(O_i(2^{8N}/\sqrt N)\) cells. Use \(2^{-8N}\asymp1/T\); the change between fixed-root real intercept and terminal log is bi-Lipschitz on the supported interval. This gives the asserted upper for any quantile strictly less than total mass. [Weaver, Paper 175, §7 (11) and the construction of \(V_{N,\epsilon}\); §8 identifies the natural cell law](https://rstation.ai/problems/collatz/papers/175)

There is also a direct independent route to the sampling strength needed just for the covering proof. For a fixed target (or for \(y=T\) moving) take a first odd landing threshold \(R=T^{A}\) with fixed \(A\) so large that \(T R^{-\sigma}\to0\) for the uniform simple-path tail exponent \(\sigma>0\). Any trajectory counted for this target first lands below \(R\); its preceding odd contributions sum to \(O(R^{-\sigma})\) by simple-path packing. Thus any test of Lipschitz constant \(T\) may be evaluated on the landing label with error \(o(1)\). The complete first-landing comparison is uniform over bounded tests and over the far source, so it compares the limiting mark directly with the ordinary shell at \(X=R^2\). Its \(\log X\) is still a fixed constant times \(\log T\), which suffices for the counting argument. The same argument works for a fixed minimum cell because every earlier site lies above the landed odd value. This second proof only supplies the indicated polynomial separation. [Relative first-landing source pin and all-positive octave form](../TERMINAL_WINDOWS.md)

## An entire escaping ray at physical resolution one

Use a fixed reference in the escaping component and let \((s,p)\) now be the signed physical comparisons of \(n\) with that reference. Its corrected height satisfies \(\log P(n)=\log P(a_C)+s\log2-p\log3\). For every reached ray target \(y\),
\[
 B_y(n)=\log P(n)-\log n-\log(P(y)/y).
\]
The final translation is constant across this target's sources. The signed physical clock of all \(n\in C\) in the shell is tight in a window \(\mu\log X+O_B(\sqrt{\log X})\), by exhausting the component with fixed waypoints and using their Gaussian. Restricting to sources hitting any moving \(y\) cannot enlarge its exceptional mass. Bounded simple corrections again give only a bounded number of grades per signed time. Thus the preceding counting lower applies uniformly over the targets on the ray for the **ordinary unnormalized** \(B_y\) measure. [Signed comparison and waypoint exhaustion](../phase2/MOVING_CLOCKS.md)

At a nonperiodic odd target the ordinary first-hit measure, after weighting by \(e^{-B_y}\) and applying \(B\mapsto y(1-e^{-B})\), equals a fixed constant times \((h(y)/y)\mu_y\). This is the nonperiodic case of PR213's weighted occupation formula (4); leading even halvings contribute no mark, so natural odd and all-source means agree. Simple-path packing bounds the weight above and away from zero uniformly. Also \(h(y)/y\to H_C>0\) along the ray. The physical unit bins pull back into \(B\)-intervals of length \(O(1/y)\) on the supported interval. Taking \(T=y\) in (4) and \(X=y^2\) in the finite count proves the lower in (2). [Weighted ordinary mark identity, PR213 (4)](https://github.com/GettysburgResearch/collatz/blob/ca48af42546268771e34297872783631f61e8f02/research/astra-global-rigidity-20261128/mass/REAL_OFFSET_ORDINARY_TRACE.md)

For the upper in (2), the laws of \(F(y)(1-R/y)\), \(R\sim\mu_y\), converge in total variation along the ray to the bilateral survival law. The latter is a countable mixture of fixed integer-root canonical laws after fixed affine changes of coordinate. The fixed-root gap law satisfies Weaver's same almost-sure frequency and mean conditions. Given \(\alpha<1\), choose a finite submixture of mass greater than \(\alpha\) and retain a sufficiently large quantile in each member. Their transformed finite covers have \(O_\alpha(y/\sqrt{\log y})\) cells at mesh \(1/y\). Total variation transfers their selected mass at each sufficiently large target, and \(F(y)\to1\) keeps the change to physical unit bins bounded. [PR193, fixed-root and bilateral identification](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md) · [PR213, earlier macroscopic unit-bin energy lower](https://github.com/GettysburgResearch/collatz/blob/ca48af42546268771e34297872783631f61e8f02/research/astra-global-rigidity-20261128/mass/MACROSCOPIC_REAL_ENERGY.md)

Finally take any \(\alpha>\delta\) in the upper covering bound. Every retained \(\sigma\) places at least \(\alpha-\delta\) mass on that cover, giving the lower in (3) by Cauchy–Schwarz. Bins heavier than \(K\sqrt{\log y}/y\) number at most \(y/(K\sqrt{\log y})\). The fixed-quantile lower in (2), applied at \(\alpha=\delta\), makes their combined mass smaller than \(\delta\) for sufficiently large fixed \(K\). Discard them. The squared sum of the remaining bin masses is bounded by their supremum times their total, proving the upper in (3). This proof preserves the distinct roles of original source size, mark resolution, root height, and discarded probability.

For either normalized law the estimates also determine typical information at one resolution. If \(J_T\) denotes the cell containing a sample, then
\[
    -\log\Pr(J_T)=\log T-\tfrac12\log\log T+O_{\Pr}(1),
\]
where \(\Pr(J_T)\) means the mass of that random cell. In (2) take \(T=y\) and the physical unit bins. The upper tail of cell mass follows by discarding the heavy bins as above. For the lower tail first cover mass \(1-\epsilon\) using at most \(C_\epsilon T/\sqrt{\log T}\) bins. Within this cover the bins lighter than \(u\sqrt{\log T}/T\) have total mass at most \(C_\epsilon u\). Let \(u\) and then \(\epsilon\) decrease to zero. This is a tightness assertion in probability, with no moment-convergence claim.

There is quantitative control on the heavy tail after taking the fine-scale limit first. Let \(m_T(K)\) be the normalized mass in bins heavier than \(K\sqrt{\log T}/T\). Their number is at most \(m_T(K)T/(K\sqrt{\log T})\). In the native count above retain the actual numerator \(m_T(K)\) in that cardinal bound; the contribution from central signed clocks is at most \(C B m_T(K)/K\), and the limiting upper contribution from other clocks is at most \(C'e^{-cB^2}\) by the source Gaussian, for each fixed large \(B\). Normalization and the uniformly bounded physical change of variables only alter the constants. Taking \(B=K/(2C)\) and absorbing the central term gives
\[
             \limsup_{T\to\infty}m_T(K)\ll e^{-c'K^2}
\]
for each fixed sufficiently large \(K\). The constants may depend on the fixed cell or component. This order of limits does not control moments of spikes with heights growing arbitrarily rapidly with \(T\).

Earlier work determined the logarithmic Hausdorff exponent for the actual fibres. It proves a lower neighborhood bound for the whole support, exhaustion by Frostman submeasures for every gauge exponent strictly greater than one half, and an almost-everywhere local-density limsup exponent of one half. PR193 previously gave the critical support-neighborhood order for target one and an escaping component. The estimates here bound the covering number of every fixed positive mass quantile at every sufficiently fine scale with the critical exponent itself. They give the information tightness above and the moving-root fixed-discard energy estimate. Whether a critical Hausdorff gauge gives positive finite measure is a separate question. [PR212 checkpoint four, real-fibre logarithmic gauge](https://github.com/GettysburgResearch/collatz/blob/0e4b428211b0bce432efc7d9d19ff4ea552248ec/research/astra-global-20261128/escape/REAL_FIBRE_LOG_GAUGE.md)
