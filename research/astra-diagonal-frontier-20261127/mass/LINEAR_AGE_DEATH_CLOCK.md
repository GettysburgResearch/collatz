# A future failure clock for each surplus cohort in each original interval

Use the physical shortcut map, \(Q_j\), \(W_j(p)\), \(h=H_2(p)\), and \(\lambda=\log_2 3\) of [the linear upper bound](LINEAR_NATIVE_SOURCE_LOSS.md). Throughout
\[
          1/2<p<\log_3 2,\qquad v=p-1/2 .
\]
These assertions include \(p=4/7\). They concern complete specified original binary intervals \(I_q=q2^L+[0,2^L)\), \(q\ge0\); \(x=0\) never passes the initial gate. Fix the first \(L\) bits' total \(r\), and write \(e=r-pL>0\) for the initial surplus, in units of odd departures. Among the actual sources \(x\in I_q\cap W_L(p)\) with \(Q_L(x)=r\), let \(B(x)\) be the additional time to first strict failure of the original gate. Set \(B=\infty\) if there is no future failure.

For every fixed \(0<\epsilon<v\) there exists \(\delta_\epsilon>0\) with the following property. On every fixed band
\[
                  0<\delta_1\le e/L\le\delta_2<\delta_\epsilon
\]
and uniformly over integer \(r,q\) in that range, except for a relative count \(O(\exp(-c e))\) in the specified initial cohort,
\[
 \left\lfloor\frac{e}{v+\epsilon}\right\rfloor
       < B(x)\le \left\lfloor\frac{e}{v-\epsilon}\right\rfloor+1.       \tag{1}
\]
The implicit constants can depend on the fixed parameters and the band. On \(q\ge1\) the exceptional proportion also holds in *reciprocal mass of that same cohort*, with factor at most two. The number of passing sources in this initial exact-total cohort is at least \(\binom Lr/L\) for all \(q\). Equation (1) is thus a high-probability, physical first-failure clock with arbitrarily small relative error in the iterated regime \(L\to\infty\) then \(e/L\downarrow0\). This statement gives no arbitrary accuracy at one fixed positive ratio \(e/L\), and gives no individual prediction for a fixed small \(x\).

### The modular input at the needed temperature

The following modular estimate is the counterpart of the real-source extension, using [lyapunov_weaver, Paper 28 v3, §§7.2–7.9, (M12), (M15), (A5)–(A14)](https://rstation.ai/problems/collatz/papers/28). It is a written use of the fixed-place Subspace Theorem. Uniformly for holding parameters \(p'\) in a sufficiently small fixed compact neighborhood \(J\subset(1/2,\log_3 2)\) of \(p\), each \(d<1\) has a fixed \(v_d>0\) such that on any fixed band \(0<c_0\le j/r\le v'<v_d\), a uniform composition of \(L\) into \(r\) positive parts, \(r/L=p'\), has canonical endpoint \(u_r\) satisfying
\[
           \max_a\Pr(u_r\equiv a\bmod 2^j)\le C r^{3/2}2^{-dj}.        \tag{2}
\]
The endpoint may be even. We give the changes to the [real proof](LINEAR_NATIVE_SOURCE_LOSS.md) to account for both the parameter range and endpoint law.

Take independent geometric holdings of parameter \(p'\), mean \(R'=1/p'\ge\lambda\). For a central chunk ending at index \(n\), write \(t,U,V,B\) as in (5) of the real proof. Its raw endpoint contribution is \(3^{r-n}V\), and \(2^tV-3^nU=B\). If two signed-copy sums agree modulo \(2^j\), the odd factor \(3^{r-n}\) can be canceled. For their differences \(\Delta V=2^j a,\ \Delta U=c\), we have
\[
 D=\Delta B=2^{t+j}a-3^n c,\qquad
 |a|\le C r3^n/2^j,\quad |c|\le Cr2^t .
\]
Choose central chunks, so \(n\ge r/4-O(1)\), and \(v_d\) small enough for \(j/n\) to stay in a compact subinterval of \((0,\lambda)\). Outside the clock tail \(S>C_0r\), \(t=O(r)\). On the retained mean-\(R'\) strip, the chunk length \(A\lfloor(1-\zeta)j/(R'A)\rfloor\) gives \(|D|\le C 2^j2^{-\zeta j/2}\), as \(R'\ge\lambda\). A nonzero difference now contradicts (M12), with its *unchanged* upper precision \(j/n<\lambda\) and its margin proportional to \(j\ge c_0r\). The sign-copy decoder follows, including the exact physical coefficient \(3^{r-n}\).

The signed entropy budgets are \(R'H_2((1-(1-2p')^m)/2)\) per holding for each fixed copy count \(m\). Their convergence in the coarse size \(A\) is uniform on \(J\): the variance bound (M11) is uniform away from the trailing fraction of a coarse block, its total divided by \(A\) has variance \(O_J(1/A)\), and the fixed XOR entropy is uniformly continuous. The balanced-tree average tends uniformly to one, since \(\sup_{p'\in J}|1-2p'|<1\). The coarse Chernoff and strip exponents are uniform by common exponential moments, bounded centered second exponential moments and the fixed positive margins. The large-coarse-alphabet entropy exclusion is uniform since \(\inf J>1/2\) gives uniform integrability of the needed \(2^a\) for fixed coarse length (enlarge the compact interval slightly within \((1/2,1)\) for domination). All groups then have the same locally good fixed-order entropy bound and bad probability \(Ce^{-c j}\), independently between disjoint local environments before conditioning, exactly as in the real proof. Young's inequality is applied directly on \(\mathbb Z/2^j\), with no quantization loss. The unconditioned raw maximum atom is \(C2^{-dj}\). A canonical endpoint subtracts an integer multiple of \(3^r\) with coefficient in \([0,r)\), and hence costs at most a factor \(r\). Finally the negative-binomial probability at the specified mean total \(S=L\) for \(p'=r/L\) is \(\binom{L-1}{r-1}(p')^r(1-p')^{L-r}\ge c_J/\sqrt r\), by Stirling. Divide the unconditioned nonnegative upper bound by this quantity. Given \(S=L\) the law is exactly the uniform positive composition law. This yields (2). No independence between distinct groups after exact-total conditioning is needed.

### A full population at every specified location

At time \(L\), ordinary sources with first bit one and count \(r\) in \(I_q\) are in bijection with the \(\binom{L-1}{r-1}\) compositions used in (2). If the canonical source is \(m\), then the actual source and endpoint are \(q2^L+m\) and \(q3^r+u_r\). This follows from the affine word rule at the original time \(L\). The translation is fixed under this exact total.

At least \(\binom Lr/L\) of all length-\(L\) binary words having \(r\) ones pass every initial prefix. Indeed for any such word, take a circular shift after a minimum of its partial sums of \({\bf1}_{\rm odd}-p\), excluding the full endpoint which is positive. The shift has all partial sums nonnegative, including through wrap since the total \(e\) is positive. A given successful word has at most \(L\) preimages in this mapping even if it has a shorter period. Every successful word begins with one. Thus under the composition law the initial gate has conditional probability at least \(1/r\). This bound is uniform in \(q\).

For every fixed \(0<c_1<c_2\), provided \(\delta_2>0\) is sufficiently small, all integers \(c_1e\le j\le c_2e\) satisfy (2)'s band and \(r/L\in J\). Take \(d>H_2(1/2-\epsilon)\). By the parity-vector bijection modulo \(2^j\), the union of residues whose *actual next \(j\) bits* have \(|Q_j/j-1/2|\ge\epsilon\) has at most \(2\cdot2^{H_2(1/2-\epsilon)j}\) elements (with integer thresholds). Its translation by \(-q3^r\) has the same cardinality. Applying (2), summing over the indicated \(j\), and dividing by the initial-gate probability lower bound \(1/r\), gives
\[
 \Pr\bigl(\exists j\in[c_1 e,c_2 e]:
   |Q_j(T^Lx)/j-1/2|\ge\epsilon
       \mid x\in I_q\cap W_L,\ Q_L(x)=r\bigr)
       \ \le\ C r^{5/2} e^{-c'e}\ \le\ C'e^{-c e}.                 \tag{3}
\]
Every probability here is a count of the same physical starting population. The final absorption of the polynomial uses \(e\ge\delta_1 L\), and is made only after the band is fixed.

For \(j\le e/p\) the initial surplus prevents failure even with no more odds. Choose \(c_1<1/p,\ c_2>1/(v-\epsilon)\), with fixed slack for rounding. On the complementary event of (3), the surplus through each further \(j>e/p\) in that range lies between \(e-(v+\epsilon)j\) and \(e-(v-\epsilon)j\). The sign at the two stated integer endpoints proves (1).

### A lower count for every interval and loss between two positive linear ages

Let \(b=\lfloor\delta L\rfloor\) and fix \(0<\epsilon<v\). For all sufficiently small fixed \(\delta>0\), choose \(r=\lceil pL+(v+\epsilon)b\rceil\). The lower bound in (1) ensures passage through \(L+b\) except on an exponentially small proportion of this one initial cohort. Its cardinality and Stirling's bounds give
\[
 \#(I_q\cap W_{L+b})
       \ge c L^{-3/2}2^{L H_2(p+(v+\epsilon)\delta)}
                                                                    \tag{4}
\]
for all \(q\). Replacing \(I_q\) by any interval of \(2^L\) consecutive positive integers loses only fixed multiplicative factors: keep an aligned block of length \(2^{L-1}\) inside it, and use \(b+1\) extra steps. The rounding in \(r,L,b\) costs \(O(1)\) bits since these parameters stay away from the endpoints of the binary entropy function.

Define \(F_{\min}(\delta)\) as the lower limit in \(L\) of \(L^{-1}\log_2\) of the *minimum* count across aligned intervals. For \(p=4/7\), the exact average upper \(2^L P_{L+b}\) and (4) give
\[
 -v\log_2[p/(1-p)]\ \le\
 \liminf_{\delta\downarrow0}\frac{F_{\min}(\delta)-h}{\delta}
 \ \le\
 \limsup_{\delta\downarrow0}\frac{F_{\min}(\delta)-h}{\delta}
 \ \le -(1-h).                                                     \tag{5}
\]
Take \(L\to\infty\) first, then \(\delta\downarrow0\), then \(\epsilon\downarrow0\). Together with (1) of the linear upper note, this has a same-population consequence. For
\[
  \kappa>\frac{v\log_2[p/(1-p)]}{1-h}
\]
at \(p=4/7\) (threshold \(2.0068920030\ldots\)), there are \(\delta_0,c>0\) such that for every sufficiently small fixed \(0<\delta<\delta_0,\ s=\lfloor\delta L\rfloor\), and all large \(L\) depending on \(\delta\), uniformly in each original interval,
\[
 \frac{\#(I_q\cap W_{L+\lfloor\kappa s\rfloor})}
      {\#(I_q\cap W_{L+s})}\ \le\ C_\delta e^{-c s}.                \tag{6}
\]
Indeed choose \(d<1\) near one and \(\epsilon>0\) small so that \(\kappa(d-h)>(v+\epsilon)\log_2[p/(1-p)]\). Use the linear upper bound at age \(\lfloor\kappa s\rfloor\) and (4) at age \(s\). Taylor expansion \(H_2(p+t)=h-t\log_2[p/(1-p)]+O_p(t^2)\) absorbs the \(O(\delta^2L)\) remainder with fixed slack, followed by the polynomial \(L\)-factor. The numerator counts exactly the subset of the denominator with no subsequent original-gate failure in that time window. On each interval with bounded ratio of extreme positive values, including every \(I_q,\ q\ge1\), the same estimate up to that ratio holds for actual reciprocal mass. The arbitrary-interval version follows from the corresponding upper and lower counts. This controls cohorts already a positive linear time past birth, with neither a lower bound on a particular preassigned trajectory nor permission to iterate (6) beyond its small linear age range.
