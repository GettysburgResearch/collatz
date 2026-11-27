# Physical interval visits on one ordinary trajectory and the critical principal trace

Work with the positive ordinary shortcut map \(T(x)=(3x+1)/2\) for odd \(x\) and \(T(x)=x/2\) for even \(x\). Use base-two logarithms for entropy, set \(p=\log_3 2\), and write \(b_i=x_i\bmod2\). A word of \(m\) shortcut parity bits specifies one residue modulo \(2^m\). The two possible next bits distinguish its two lifts modulo \(2^{m+1}\). This follows inductively since after \(m\) prescribed steps the terminal changes by the odd number \(3^{\sum b_i}\) when the starting point changes by \(2^m\).

## One finite simple trajectory

Take any consecutive segment with distinct positive states \(x_0,\ldots,x_{P-1}\). Let \(I\) be any interval of diameter strictly less than \(2^m\), where \(1\le h<m\le P\). Set
\[
 A=\{0\le i\le P-m:x_i\in I\},\quad a=|A|,\qquad
 D_h=\#\{0\le i<P-h:b_i\ne b_{i+h}\}.
\]
For \(a>0\), let \(Q\) be the probability table of the ordered bit pair \((b_{i+j-h},b_{i+j})\), where \(i\) is uniform on \(A\) and independently \(j\) is uniform on \(h,\ldots,m-1\). Write \(H_2\) for binary entropy, and \(H_2^{-1}\) for its increasing inverse on \([0,1/2]\). Then
\[
 \log_2a\le h+(m-h)H_Q(V\mid U),\qquad
 D_h\ \ge\ a H_2^{-1}\!\left(\frac{(\log_2a-h)_+}{m-h}\right).       \tag{1}
\]
Indeed the \(a\) parity windows are distinct because their physical initial states lie in one interval shorter than their dyadic modulus. The uniform random window therefore has entropy exactly \(\log_2a\). In the chain rule keep the initial \(h\) bits and condition each remaining bit on the bit \(h\) places earlier. Concavity of conditional entropy gives the first bound. If \(e=Q_{01}+Q_{10}\), then \(H_Q(V\mid U)\le H_2(e)\), by conditioning the exclusive-or of the two bits. Each physical mismatch appears in at most \(m-h\) windows. Thus \(e\le D_h/a\) and \(e\ge H_2^{-1}((\log_2a-h)_+/(m-h))\), including \(e>1/2\). This proves (1) without wrapping the observed path or assuming an infinite continuation.

In particular, take \(P\to\infty\), intervals of diameter at most \(P^{B+o(1)}\) with fixed \(B\ge1\), and lag \(h=(\eta+o(1))\log_2 P\), \(0\le\eta<1\). If those intervals contain a lower asymptotic fraction \(\alpha>0\) of the observed phases, then
\[
 \liminf D_h/P\ \ge\ \alpha H_2^{-1}\!\left(\frac{1-\eta}{B-\eta}\right).       \tag{2}
\]
Choose \(m=(B+o(1))\log_2 P\) large enough for each diameter. The at most \(m-1\) unavailable right endpoints have negligible weight. In particular, if \(D_h=o(P)\), the largest fraction in *any moving interval* of width \(P^B\) tends to zero for every fixed \(B\ge1\). The initial height and the heights outside the interval are free.

## Polynomial physical height on an actual ray

Suppose the whole observed segment has \(\max_{i<P}x_i\le P^{B+o(1)}\). Let \(P\to\infty\) along this subsequence and use all dates \(0\le i\le P-m\) as the starts. Every subsequential limit \(\nu\) of the empirical parity process is shift invariant, has one-symbol mean \(p\), and has entropy rate
\[
                         h(\nu)\ge 1/B.                               \tag{3}
\]
Here one may append any continuation to each finite word when defining the empirical process. Fixed-length marginals lose only their last finitely many dates. For the mean, the exact product is
\[
 x_P/x_0=3^{\sum_{i<P}b_i}2^{-P}\prod_{i<P:b_i=1}(1+1/(3x_i)).
\]
Distinctness bounds the logarithm of the product by \(O(\log P)\) through the ordinary harmonic sum of \(P\) distinct positive integers. We have \(1\le x_P\le(3\max_{i<P}x_i+1)/2\). Both endpoint logarithms are \(O(\log P)\), which gives \(\sum b_i=pP+O(\log P)\). Removing either endpoint of the empirical process changes any fixed cylinder frequency by \(O(1/P)\), giving invariance.

For fixed \(k\), condition each date after the first \(k\) of the random \(m\)-window on its previous \(k\) symbols. Concavity gives
\[
 \log_2(P-m+1)\le k+(m-k)H_{Q_k}(V\mid W),
\]
where \(Q_k\) averages all the corresponding length-\((k+1)\) blocks. This average differs from the full empirical marginal by \(O(m/P)\) in total variation. Indeed the window-start average for any fixed internal offset is uniform on a subinterval missing at most \(m\) dates. Taking limits and then increasing \(k\) proves (3). It includes the known numerical restriction \(B\ge1/H_2(p)\) from ordinary orbit sparsity. The conclusion here also constrains the full limiting process and its short-lag correlations.

Specifically suppose \(h=(\eta+o(1))\log_2P\) with \(0\le\eta< B\), and the normalized mismatch converges to \(\delta\) on the chosen subsequence. The two marginal means of \(Q\) tend to \(p\) and its mismatch tends to \(\delta\), since every fixed internal offset samples all but \(O(m)\) parent dates. In (1) the initial entropy \(h\) may be replaced by the sum of the marginal entropies of those \(h\) individual bits, at most \(h(H_2(p)+o(1))\). The unique limiting two-by-two table has both off-diagonal entries \(\delta/2\). Therefore
\[
 1\le \eta H_2(p)+(B-\eta)
 \left[pH_2\!\left(\frac\delta{2p}\right)+(1-p)H_2\!\left(\frac\delta{2(1-p)}\right)\right]. \tag{4}
\]
For fixed lags these conditions apply pointwise to every hypothetical escaping positive integer with polynomial height on the selected horizons. They also apply to varying finite simple ordinary trajectories.

## A completely critical arithmetic trace

A finite odd-gap word \(w=(e_0,\ldots,e_{n-1})\) passes the critical test if \(2^{E_j}<3^j\) for each \(1\le j\le n\), where \(E_j=\sum_{i<j}e_i\). Let \(m(w)\) be the least positive odd seed of its exact valuation cylinder modulo \(2^{E_n+1}\). Put \(J_n^*=\sum_{w\text{ passes}}1/m(w)\), including every accepted word once. Then
\[
 \lim_n J_n^* =\sum_{x:\;2^{E_j(x)}<3^j\ \forall j\ge1}1/x,\qquad
 J_n^*\longrightarrow 0\quad\Longleftrightarrow\quad
 \text{all ordinary positive trajectories are eventually periodic}.  \tag{5}
\]
The minimum coefficient inside a completed odd-to-odd block is attained at one of its two ends, since its initial odd step is followed by halvings. Consequently the gate is exactly the all-prefix shortcut coefficient test at an odd source. The union of the principal seeds on the left is contained in PR 201's wider \(4E_j\le7j\) principal set, whose reciprocal sum is finite. At a fixed positive source the indicator of its accepted principal prefix converges to the indicated infinite test, by increasing modulus and permanent failure. Dominated convergence proves (5)'s first formula. For the second, an escaping trajectory has finite reciprocal sum along its distinct odd states, by the existing simple-trajectory estimate. Its shortcut coefficient goes to infinity by the exact product formula. The phase of the global minimum of that coefficient must be odd (an even next step lowers it), and that phase passes the critical test forever. Every eventually periodic trajectory instead has strictly subunit coefficient over a lap, by the same product formula. This is a critical centered specialization of known results. The earlier all-supercritical-tail argument already separates cycles from escape; PR 201 already distinguishes them using the wider gate and a noncentered denominator.

## A countermodel for passing to one fixed source

For **each real \(B>1\)** there exists an infinite shortcut word with all the following properties. Write \(q_n\) for the number of its first \(n\) ones, \(C_n=3^{q_n}/2^n\), and \(m_n\) for the least positive ordinary source of that binary cylinder.

* Every nonempty prefix is strictly coefficient-supercritical, and \(C_n=n^{B+o(1)}\).
* Frequencies of every fixed finite bit pattern equal its Bernoulli-\(p\) probabilities in the limit. The resulting stationary law has entropy \(H_2(p)\). Thus it meets (3) and every fixed-lag version of (4) whenever \(B\ge1/H_2(p)\).
* Following its indicated affine branches over the reals from **any** positive starting value gives \(y_n=n^{B+o(1)}\), with \(\sum_n1/y_n<\infty\). The unique 2-adic starting point has exactly the indicated parities. Every finite prefix separately occurs on a positive integer trajectory which subsequently reaches one.
* Nevertheless \(\log_2 m_n/n\to1\). Its critical principal contribution at binary depth \(n\) is at most \(2^{-n+o(n)}\). The analogous odd-gap least source is the binary least source after appending the odd endpoint bit, so the same conclusion holds along the strictly increasing completed odd-gap depths in shortcut time.

To construct the word put \(a=B/\log_2 3\). Choose \(K\) large enough that \(F(t)=pt+a\log_2(1+t/K)\) has derivative in \((0,1)\) for \(t\ge0\). At block number \(j\ge1\) use length \(L_j=1+\lfloor\sqrt{\log_2(j+1)}\rfloor\), and let \(t_j=\sum_{i<j}L_i\) be its starting time. Choose exactly \(k_j=\lceil F(t_j+L_j)\rceil-\lceil F(t_j)\rceil\) ones. This is in \([0,L_j]\), and \(k_j/L_j\to p\), so both first bits are eventually possible. At a block boundary \(q_t=\lceil F(t)\rceil\). At intermediate times the error in \(q_t-F(t)\) is \(O(L_j)=o(\log t)\), independently of the ordering. Because the excess \(F(t)-pt\) eventually exceeds \(2L_j+2\), all late prefixes satisfy \(q_t>pt\) for every ordering. In the finite early blocks put all ones first, then all zeros. The excess \(q_t-pt\) rises then falls and its two endpoint values are nonnegative; equality at a positive integer date is impossible because \(p\) is irrational. This proves strict initial safety and the claimed coefficient growth.

For each length and weight \((L,k)\), cycle through the lexicographic list of all \(\binom Lk\) words of this type on successive occurrences. This reference ordering has the claimed Bernoulli frequencies. At time \(t\), the total number of letters in incomplete cycles for all types is at most \(O(L_{\max}^3 2^{L_{\max}})=o(t)\), including a possible incomplete final block. In a complete cycle a specified pattern of length \(r\) at a fixed interior offset has the uniform-without-replacement probability, which tends to its Bernoulli-\(p\) value as \(L\to\infty\), \(k/L\to p\). At most \(r-1\) positions per block cross a boundary, a vanishing fraction. These estimates also prove convergence along partial blocks, and finite changes at early times are immaterial.

At each sufficiently late square block index \(j=s^2\), choose its first bit opposite the bit at time \(t_j\) of the actual current least source \(m_{t_j}\). Reorder its other letters to retain \(k_j\). Continue advancing the reference list even on each edited block. Through the first \(J\) blocks, at most \(O(\sqrt J L_J)=o(t_{J+1})\) letters change, preserving all fixed pattern frequencies. By the binary cylinder lift, the new least positive source after the forced bit is exactly \(m_{t_j}+2^{t_j}\). The least sources are nondecreasing. Since \(t_{(s+1)^2}/t_{s^2}\to1\), for every large \(n\) the last completed forced bit is at time \((1-o(1))n\). The lower bound and the trivial \(m_n\le2^n\) prove the claimed limit. The real affine recursion gives
\[
 y_n=C_n\left(y_0+\sum_{i<n:b_i=1}\frac1{3C_i}\right).
\]
Since \(B>1\), the sum converges. This validates the real and reciprocal assertions while keeping the real initial condition distinct from dyadic integrality.

For the terminal-one assertion, in fact *every* binary word of length \(n\) and weight \(q\) has such a positive lift. Write its affine branch \(2^ny=3^q x+D\). Choose \(c=2^{-n}D\pmod{3^q}\). Take \(1\le l\le3^q\) with \(4^l\equiv1+3c\pmod{3^{q+1}}\). Such an \(l\) exists since \(4\) generates the \(1\bmod3\) subgroup, as \(v_3(4^{3^k}-1)=k+1\). The odd positive terminal \(y=(4^l-1)/3\) has the required residue and reaches one in \(2l\) shortcut steps. Stripping the word backwards maintains integrality by the ternary congruence. Each even inverse is \(2z\), and each legal odd inverse is the positive odd integer \((2z-1)/3\). For \(q=0\) take \(l=1\). Equivalently every positive dyadic cylinder contains a positive source in the basin of one, as also follows from the well-known sufficiency of arithmetic progressions for this particular modulus.

The physical-interval and entropy inequalities concern genuine ordinary trajectories. Applying them to the formal real trajectory in the example would require actual parity legality at the same real starting value for all depths. The square-block steps exhibit its failure. A permanent critically safe positive ordinary source would carry a fixed atom in (5), and neither the local population inequality nor the Bernoulli laws bound its lifetime. No vanishing or nonvanishing of (5) is proved.

## Related work

* The parity cylinder, ordinary factor-collision principle, and critical Sturmian approximation estimates precede this argument. [Weaver, Paper 84, §2–4](https://rstation.ai/problems/collatz/papers/84) · [Dubickas, *On integer sequences generated by linear maps*](https://doi.org/10.1017/S0017089508004655)
* The limiting single-orbit population exponent \(H_2(\log_3 2)\) was already reached up to arbitrary exponent slack in the prior orbit Mellin packet. [Single-orbit sparsity](https://github.com/GettysburgResearch/collatz/blob/cd1b3689e8d37fc4232945072e2faf6bd5ee47bd/research/astra-three-routes/pass2/ORBIT_MELLIN.md) · [Shortcut supercritical tails](https://github.com/GettysburgResearch/collatz/blob/cd1b3689e8d37fc4232945072e2faf6bd5ee47bd/research/astra-three-routes/pass2/SC_TAIL_AND_ECHO.md)
* The summable principal-seed envelope and the positively tilted escape trace are taken from PR 201. The incoming laws in (5) are the actual finite word cylinders. [Global prefix trace](https://github.com/GettysburgResearch/collatz/blob/807d67ab049f1646398d8ca8c20948cdc1d87742/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md)

Prepared by the binary-energy reviewer on 27 November 2026 UTC. All analytic statements here are written mathematics.
