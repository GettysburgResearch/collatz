# Finite total variation in depth for the original marked trace

For the original all-visit rows, including all positive odd targets, the following series converges:
\[
 \boxed{\quad
 \sum_{d\ge0}\sum_{z\ge1\ {\rm odd}}\frac{1}{z(3z+1)}
 \sup_{0\le t\le1}|L_{d+1,z}(t)-L_{d,z}(t)|<\infty .\quad}       \tag{1}
\]
The unmarked difference is the test at \(t=1\). In particular the entire original \(Q_d^*\) of PR212 is summable. Thus its dyadic sums tend to zero, and \(dQ_d^*\to0\) along some unbounded sequence. The earlier bound on the dyadic sums was \(O(\sqrt D)\). The new result permits absolute differences, the entire mark interval, target one, and all visits on cycles. The unmarked conclusion follows from [PR195's finite-period propagation, equation (2)](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/DEPTH_DIFFERENCE.md) and the one-edge loss identity. The new extension controls the full intercept distributions with independently chosen thresholds. It uses Tao's published fine-scale mixing. It gives no exponential depth rate and does not exclude an escaping orbit or an additional cycle.

## The periodic measure and its physical evolution

Write \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odds and \(\rho_1(x)=x\bmod3\). At an odd positive target \(z\), a legal length-\(d\) inverse word \(w\) follows the actual positive integral parents. In target-first order write its gaps \(g_i\ge1\), partial clocks \(s_i=g_1+\cdots+g_i\), and
\[
 A_w=3^d2^{-s_d},\qquad F_w=\sum_{i=1}^d 3^{i-1}2^{-s_i},
 \qquad z=F_w+A_wx_w.
\]
Here \(x_w\) is the actual odd source. A terminal nonunit receives zero weight. A nonunit in the interior has no inverse continuation. Set
\[
 M_{d,z}=\sum_{w}A_w\rho_1(x_w)\,\delta_{F_w},\qquad
 N_d(z)=\sup_{u\in\mathbb R}
 |M_{d+1,z}([u,\infty))-M_{d,z}([u,\infty))|.
\]
The empty word has intercept zero. The total mass of \(M_{d,z}\) is \(\rho_{d+1}(z)\). Its upper-ray value at \(u=z(1-t)\) is exactly \(L_{d,z}(t)\). Every contributing mark lies in \((0,1]\). Thus the supremum defining \(N_d\) is also the full supremum in (1). The one-letter row sum is at most two, giving \(N_d(z)\le2^{d+2}\).

For a word of length \(d\), compatibility is exactly \(z\equiv F_w\pmod{3^d}\) using dyadic inverses modulo powers of three. This follows successively from the reverse divisibility tests. For a positive odd representative a compatible parent is always positive and odd. The source residue modulo three requires one additional digit of \(z\). Consequently \(M_{d,z}\), in the intercept coordinate, has period \(3^{d+1}\) in the residue of the positive odd representative. In particular \(N_d\) is defined on \(\mathbb Z/q_d\) for \(q_d=3^{d+2}\). Extend it to all integer representatives by this period whenever taking a residue sum.

An inverse edge with \(3x+1=2^e z\) pushes an intercept from \(x\) by the increasing map \(v\mapsto 2^{-e}+3\,2^{-e}v\), with weight \(3\,2^{-e}\). Splitting a word at this edge gives
\[
  N_{d+1}(z)\le\sum_{U(x)=z}3\,2^{-e(x)}N_d(x).                       \tag{2}
\]
All series at fixed depth converge absolutely by the one-step row bound. Inequality (2) compares the actual two consecutive rows, with the same affine map at the two grades.

## A complete-period estimate with every threshold retained

Define \(H_d=q_d^{-1}\sum_{r\bmod q_d}N_d(r)\). For every fixed \(B>0\),
\[
                         H_d\ll_B (1+d)^{-B}.                            \tag{3}
\]

First consider unmarked differences. For independent gaps with \(\Pr(g_i=e)=2^{-e}\), set \(Y_n=F_{g_1,\ldots,g_n}\pmod{3^n}\). Then
\[
 \rho_n(r)=3^n\Pr(Y_n=r).
\]
For one gap the two unit residues receive densities one and two. Conditioning on the first gap in \(Y_n=2^{-g_1}(1+3Y'_{n-1})\) gives the exact physical recurrence. The law projects from depth \(n\) to depth \(n-1\), since its last summand is divisible by \(3^{n-1}\). Hence for \(n=d+2\)
\[
 h_d:=3^{-n}\sum_{r\bmod3^n}|\rho_n(r)-\rho_{n-1}(r)|
     =\mathrm{Osc}_{n-1,n}(\mathcal L(Y_n))
     \ll_B(1+d)^{-B}.                                                   \tag{4}
\]
The final inequality is [Tao, Forum of Mathematics, Pi **10** (2022), Proposition 1.14, pp. 10–12, equations (1.26)–(1.29)](https://doi.org/10.1017/fmp.2022.8). His oscillation is the unnormalized sum of absolute deviations of probability masses from their coset averages. Taking adjacent levels uses only the published range \(1\le m\le n\).

Take \(k=\lfloor d/2\rfloor\). In both marked rows temporarily replace the intercept by the intercept \(F_k\) of the first \(k\) target-side gaps. For a compatible fixed prefix \(w\), the difference of the surviving suffix masses is \(A_w(\rho_{d-k+2}(x_w)-\rho_{d-k+1}(x_w))\). Its frozen threshold is common to both rows. The compatible residues comprise one class modulo \(3^k\). As \(z\) runs over this class modulo \(q_d\), the endpoint \((z-F_w)/A_w\) runs bijectively over all residues modulo \(q_d/3^k\). The multiplier in this residue bijection is the ternary unit \(2^{s_k}\). Even if the threshold is chosen separately at every residue, the average supremum of the frozen difference is at most
\[
       \sum_{w:|w|=k} (A_w/3^k)h_{d-k}=h_{d-k}.                       \tag{5}
\]

Two estimates pay for freezing. At length \(l=d,d+1\), a word property depending only on its gaps has mean row mass at most twice its iid geometric probability. In fact a word occupies a fraction \(3^{-l}\) of the residues and its terminal weight is at most two. For \(a=1/2\), put \(p=3^a/(2^{1+a}-1)<1\). Subadditivity of the power and independence of the gaps give
\[
 \mathbb E|F_l-F_k|^a\le 3^{-a}\sum_{i>k}p^i\ll p^k.                 \tag{6}
\]
The mean weight of words with \(F_l-F_k>\epsilon\) is therefore \(O(p^k\epsilon^{-a})\).

For the remaining words, changing the threshold statistic requires \(F_l\) in an interval of length at most \(\epsilon\) touching the threshold. The interval may be selected independently for each residue. Fix \(z\) and the total clock \(m\). Its distinct legal words of length \(l\) have distinct sources since each positive source has exactly one forward word of that length. The intercepts \(z-3^l2^{-m}x_w\) therefore have spacing at least \(A=3^l2^{-m}\). Each has mass at most \(2A\). Every interval of length \(\epsilon\), even closed, costs at most \(2(\epsilon+A)\) on this clock. On the central clocks \(7l/4\le m\le4l\) there are \(O(l+1)\) summands and \(A\le(3\,2^{-7/4})^l\). The complement has mean mass \(O(e^{-cl})\) by the elementary Chernoff bounds for a sum of positive geometric variables of mean two. This gives uniformly
\[
 q_d^{-1}\sum_{r\bmod q_d}\sup_{I:\,|I|\le\epsilon}M_{l,r}(I)
       \ll (l+1)\epsilon+O(e^{-c' l}).                                  \tag{7}
\]
Equations (6)–(7), with \(\epsilon=p^{k/(2a)}\), make the total error in (5) exponentially small in \(d\). Bounded grades cost an absolute constant. This proves (3) without a joint-clock mixing assumption and without a claim of pointwise mixing at a prescribed integer.

## Moving harmonic cutoff and the full stopped budget

Retain the fundamental size \(q=q_d\) and let
\[
 B_d=\sum_{1\le x\le q_d\ {\rm odd}}N_d(x)/x,\qquad
 P_d=\sum_{1\le x\le q_d\ {\rm odd}}N_d(x)/[x(3x+1)].
\]
Use (2) on \(1\le z\le3q=q_{d+1}\). For every positive odd source its actual edge has the harmonic identity
\[
       \frac{3\,2^{-e}}{z}=\frac{3}{3x+1}
                        =\frac1x-\frac{1}{x(3x+1)}.                    \tag{8}
\]
Thus the contribution from \(x\le q\) is at most \(B_d-P_d\). Let \(I_d\) be the remaining incoming majorant, summed over \(x>q\) with actual target \(z\le3q\), using \(N_d(x)3\,2^{-e}/z\).

For a fixed exponent \(e\), each such factor \(3\,2^{-e}/z\) is at most \(1/q\) by (8). The sources give distinct classes modulo \(q\). Indeed if \(q\mid x-x'\), then \(3q\mid 2^e(z-z')\). Since \(3q\) is odd, \(3q\mid z-z'\); targets from 1 through \(3q\) must be equal, and so must sources. Each fixed exponent contributes at most \(H_d\). For \(e>4(d+2)\), instead sum the crude bound \(3\,2^{-e}2^{d+2}/z\) over every retained target and this geometric tail. Hence
\[
 B_{d+1}+P_d\le B_d+I_d,\qquad
 I_d\le 4(d+2)H_d+3\,{2^{-3(d+2)}}[1+\log(3q_d)].                   \tag{9}
\]
The discarded-lift argument in [PR195, equation (2)](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/DEPTH_DIFFERENCE.md) also gives the sharper \(I_d\le2H_d\) for our half-period cutoff. Fix the odd representative \(1\le r<2q\) and write \(x=r+2qj\). The \(j=0\) contribution from \(x>q\) costs at most \(1/q\). On \(2^h\le j<2^{h+1}\), an accepted edge has \(2^e=(3x+1)/z>2j\ge2^{h+1}\). Therefore \(2^{h+1}\mid(3r+1)/2+3qj\), which specifies a single class of \(j\) modulo \(2^{h+1}\). At most one term in this shell has to be paid, at harmonic weight at most \(1/(2q\,2^h)\). Summing all shells gives a further \(1/q\) per residue. The argument applies to any nonnegative periodic row seminorm.

The positive sequence \(I_d\) has finite sum and indeed has every polynomially weighted moment, by (3). Summing (9) over a finite depth interval proves \(\sum_{d\ge0}P_d\le B_0+\sum_d I_d\). Finally, on the exterior \(x>q_d\) even the elementary bound \(N_d\le2^{d+2}\) gives a stopped-weight total at most \(2^{d+2}/(3q_d)\). Summing over depths gives (1). Alternatively, full periods in each interval \((h q_d,(h+1)q_d]\) give the smaller exterior bound \(O(H_d/q_d)\).

A nonnegative summable sequence has tails tending to zero. If \(dQ_d^*\) were bounded below by a positive constant eventually, the harmonic series would contradict (1). This establishes the stated subsequence. For a possible escaping ray, the transport of any finite packet can preserve a positive part of its harmonic mass while depositing a summable sequence of stopped losses. The finite total alone gives no upper bound of the form \(\operatorname{poly}(d)(2/3)^d\).

## Fixed-target limits and their atoms

The CDFs at every fixed positive odd target converge uniformly. Indeed their successive uniform distances form a summable series by (1), since each target has positive kernel weight. More strongly, if \(L_{\infty,z}\) denotes the resulting finite CDF, then
\[
 \sum_z\pi(z)\sup_t|L_{d,z}(t)-L_{\infty,z}(t)|
 \ \le\sum_{j\ge d}\sum_z\pi(z)N_j(z)\longrightarrow0.
\]
Extend each CDF by zero below zero and by its total mass above one. The uniform limit is nondecreasing, right-continuous and supported on the compact interval \([0,1]\).

This limit is **atomless at every fixed target**. Put \(a_d(z)=\sup_v M_{d,z}(\{v\})\). An increasing affine map on an inverse edge is injective, so \(a_{d+1}(z)\le\sum_{U(x)=z}3\,2^{-e(x)}a_d(x)\). Also \(a_d\le 2^{d+1}\), and (7) at \(\epsilon=0\) makes its average over a complete period exponentially small. The moving-cutoff proof now gives \(\sum_{d,z}\pi(z)a_d(z)<\infty\). Thus \(a_d(z)\to0\) at each fixed target. Uniform convergence of the CDFs also gives convergence of their left limits at each point. Every jump of the limit is therefore zero. Affine passage between the normalized mark and the intercept preserves atom mass at fixed \(z\).

This argument proves convergence and atomlessness directly from Proposition 1.14 and the physical word formulas. The identification of the unmarked limiting mass in [Weaver, Theorem 2](https://rstation.ai/problems/collatz/papers/176/v1), and the stationary interpretation of specified real fibres in [PR193](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md), use further inputs.

[Exact finite controls](check_summable_trace.py) exercise per-gap capped words with the exact terminal selector, all upper-ray breakpoints, fixed-clock spacing, frozen bounds, and the moving-cutoff inequality. Their [receipt](../../../reports/astra-global-20261128/escape/SUMMABLE_TRACE_CHECKS.json) is a bounded calculation.

[The ordinary arithmetic kernel](MarkedCutoffArithmetic.lean) identifies the exact odd-clock landing and proves injectivity at a fixed gap and ternary residue in a retained target period. [The ordered-field flux kernel](MarkedCutoffFlux.lean) proves the real one-edge carry and depletion, the summed arbitrary finite-window inequality, and its telescoping budget. The complete-period analytic mixing and the infinite summability conclusion in (1) remain written arguments.
