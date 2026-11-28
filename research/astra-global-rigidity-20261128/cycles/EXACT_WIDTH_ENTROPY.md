# Exact two-octave word entropy and rational realization

**PROPOSED.** Put \(\gamma=\log_2 3\), \(a=\gamma-1\in(1/2,1)\), and \(B=\log_2 R=1+\eta\). For \(2\le R\le4\), hence \(0\le\eta\le1\), let \(\mathcal Z_m(R)\) be the strings of positive Syracuse exponents \(e_0,\ldots,e_{m-1}\) such that every nonempty contiguous block of length \(j\) and exponent sum \(A\) obeys \(|j\gamma-A|<B\). This is the zero-correction language of Witteveen §5, with the same strict endpoints. Its entropy in nats per odd step is
\[
 \boxed{\quad h(R)=\lim_{m\to\infty}\frac{\log|\mathcal Z_m(R)|}{m}
   = \eta\log2+(\eta-a)_+\log(3/4).\quad}                              \tag{1}
\]
For \(2\le R\le3\), this is \(\log(R/2)\). For \(3\le R\le4\), it is \((2a-\eta)\log2+(\eta-a)\log3\). In particular \(h(12/5)=\log(6/5)\) without a transfer matrix computation.

Weaver 181/v1 §4 already identifies the equivalent singleton-and-pair symbolic profile on the shortcut clock, with a matching lower construction in §4.4. For \(K=3R/2\) and \(\alpha=\log_3 2\), Weaver's shortcut bit rate \(D(K)\) satisfies \(D(K)\log2=\alpha h(R)\). Indeed its available-site and paired-site frequencies per shortcut time are respectively \(\alpha\eta\) and \(\alpha(\eta-a)_+\). Equation (1) identifies that same profile with Witteveen's particular strict subword definition, directly on the odd clock. The primitive positive rational realizations with controlled complete denominators below supply an additional conclusion. [Weaver 181/v1, §4.1, equations (9), (14), and §4.4](https://rstation.ai/problems/collatz/papers/181/v1)

At clocks tending to the critical slope, exponentially many genuine primitive positive rational cycles attain this count to leading exponential order, with odd width at most \(R+o(1)\). For each fixed \(2<R\le4\) and \(\epsilon>0\), all but an exponentially small fraction of the constructed rooted words have complete reduced denominator
\[
                 q\ge \exp((h(R)-\epsilon)p),                          \tag{2}
\]
where \(p\) is the odd period. Their real odd states have comparable polynomial heights in \(p\) and tend uniformly to infinity.

## A one-dimensional matching

For a given word write \(E_j=\sum_{i<j}e_i\) and \(d_j=j\gamma-E_j\), \(0\le j\le m\). The strict inequalities on all subwords are equivalent to \(\max d_j-\min d_j<B\). Translate the \(d_j\) into the half-open band \([0,1+\eta)\) by subtracting their minimum. Record their fractional phases \(\theta_j=\{\theta_0+ja\}\) and grades \(g_j\) with translated heights \(y_j=\theta_j+g_j\). Conversely any such band path with positive exponents yields a legal word because its finitely many heights inside a half-open band have range strictly below its length.

The grades are zero and one. A one is available exactly at \(\theta_j<\eta\). Put \(b_j=\lfloor\theta_j+\gamma\rfloor=1+\mathbf1_{\theta_j\ge1-a}\). Then
\[
                   e_j=b_j+g_j-g_{j+1}.                                \tag{3}
\]
At \(b_j=2\) this is always positive. At \(b_j=1\) the only forbidden pair is \(g_j=0,g_{j+1}=1\). This pair is possible before enforcing positivity exactly at \(\theta_j<(\eta-a)_+\), because the next phase is \(\theta_j+a\). At such an edge both grades are available at both dates. The constrained edges form a matching: their entry phase is below \(1-a<a\), their exit phase at least \(a\).

For \(0\le j\le m\) let \(A_m\) count available high grades, and let \(F_m\) count constrained edges for \(0\le j<m\). The exact fixed-intercept grade-array count is
\[
                    2^{A_m-2F_m}3^{F_m}.                              \tag{4}
\]
For a fixed word and intercept, \(g_0\) determines the entire array by (3), so each word has at most two preimages. As the intercept varies, availability and winding arrays together take \(O(m+1)\) values. Their only breakpoints are translates of their fixed endpoints. Include endpoint singletons if needed. Irrational rotation equidistribution gives \(A_m/m\to\eta\), \(F_m/m\to(\eta-a)_+\) uniformly in the intercept. One elementary proof majorizes and minorizes interval indicators by continuous functions of arbitrarily close integrals, then approximates these by trigonometric polynomials; the geometric sum bound is uniform in the initial phase. The polynomial number of cells, (4), and the two-preimage bound give (1) including \(\eta=0,a,1\).

Witteveen obtains a lower bound by independently swapping a subset of disjoint binary pairs and uses an overlap matrix at \(R=12/5\). Equation (1) treats all positive integer exponent words in that definition. For \(R\le8/3\) the strict one-letter condition already excludes exponent three, since \(3-\gamma=\log_2(8/3)\). Above \(8/3\) the matching also permits exponent three. [Witteveen, §5, frozen primary source](https://github.com/kulltc/collatz-entropy-barriers/blob/fc0854799b094fa04250ce8309279609276f3c58/paper/main.tex#L331-L416)

## Closing the word in the positive rationals

Take upper continued-fraction convergents \(H/p>\gamma\) in lowest terms. Here \(p\to\infty,\ 0<\Lambda=H-p\gamma<1/p\). Use the circular \(p\)-grid \(\theta_j=\{jH/p\}\) and (3) with \(\gamma\) replaced by \(H/p\). High grades are allowed precisely at \(\theta_j<\eta\). The same disjointness proof applies for \(a_p=H/p-1>1/2\). On the circle the two counts in (4) are \(A=p\eta+O(1)\), \(F=p(\eta-a_p)_++O(1)\) by exact uniform spacing. There are \(\exp((h(R)+o(1))p)\) different rooted exponent words because each has at most two preimages. All have exponent sum \(H\); none has a proper period dividing \(p\) since \(\gcd(H,p)=1\).

Each word has a unique positive rational periodic realizer
\[
 x_0=\frac{\sum_{j=0}^{p-1}2^{E_j}3^{p-1-j}}{2^H-3^p},
 \qquad 2^{e_i}x_{i+1}=3x_i+1.                                        \tag{5}
\]
Every rotated numerator in (5) is odd, as is the determinant. The displayed \(e_i\) is therefore the exact native valuation in the odd-denominator normalization. The reduced denominator divides \(D=2^H-3^p\) and is common around the lap because both 2 and 3 are units at every divisor of \(D\). The least odd period is \(p\), and forgetting the root identifies at most \(p\) words.

Put \(y_i=\theta_i+g_i\), \(r_i=\log_2(1+1/(3x_i))>0\). Subtraction of the two equations of motion gives
\[
 \log_2 x_i-y_i=(\log_2 x_0-y_0)
            +\sum_{j<i}r_j-i\Lambda/p,\qquad \sum_{j<p}r_j=\Lambda.
\]
The difference of the final two terms between any two dates has magnitude at most \(\Lambda\), since each increment is a difference of two nonnegative interval sums bounded by \(\Lambda\). Thus the actual odd width is at most \(R2^\Lambda\). Since \(\Lambda\to0\), the \(r_i\) tend uniformly to zero and \(\min x_i\to\infty\). Bounded width and the product identity then give \(x_i\asymp_R p/\Lambda\) uniformly. The two-logarithm estimate of Bondareva, Luchin and Salikhov gives \(\Lambda\gg p^{-4.116201}\), hence real odd states \(O_R(p^{5.116201})\). The reduced numerators may be exponentially larger. [Primary logarithmic estimate, Theorem 1](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)

At a fixed denominator \(q\), the roots at this clock give distinct rational states by deterministic odd numerator dynamics. They number at most \(O_R(qp^{5.116201}+1)\). The fixed determinant satisfies \(\log D=O(p)\), \(\tau(D)=\exp(o(p))\). For the second bound, at fixed \(\varepsilon>0\) all sufficiently large primes \(\ell\) satisfy \(v+1\le\ell^{\varepsilon v}\) for \(v\ge1\). The finite set of smaller primes contributes only \(O_\varepsilon((1+\log D)^{O_\varepsilon(1)})\). Sum over \(q\mid D\) below \(\exp((h(R)-\epsilon)p)\). Their total \(\exp((h(R)-\epsilon+o(1))p)\) proves (2). The exponentially small exceptional fraction survives quotienting by cyclic rotations since multiplicities are at most polynomial.

## Actual rational parity laws at \(2<R<3\)

There is a direct shortcut-clock construction of a stationary limiting law. Let \(\alpha=\log_3 2\), \(\beta=\log_3(R/2)\in(0,1-\alpha)\). Choose lower convergents \(u/n<\alpha\) (inverses of the upper convergents above), set \(v_i=\{-iu/n\}\) and \(c_i=\mathbf1_{v_i<u/n}\). At dates \(v_i<\beta\) independently choose a fair bit \(t_i\); all other \(t_i=0\). Put
\[
                         w_i=c_i+t_{i+1}-t_i .
\]
For large \(n\), every eligible date has \(c_i=1,c_{i-1}=0\), so these are disjoint adjacent swaps. The binary word contains \(u\) ones and is primitive by coprimality. Its homogeneous shortcut lift is \(y_i=v_i+t_i\). Each odd departure has \(t_i=0\) and \(v_i<u/n+\beta\), since it is an unchanged baseline one or the date before an upward grade change. The shortcut version of the preceding correction identity has total \(n\alpha-u\to0\) in base-three logs. Hence the realized odd width is at most \(3^{u/n+\beta+n\alpha-u}=R+o(1)\).

On the limiting irrational rotation \(v\mapsto v-\alpha\) take uniform \(v_0\) and independent fair bits exactly in the indicated arc. The resulting parity law has entropy \(\beta\) bits per shortcut step. Conditional on \(v_0\), the bits at \(m+1\) dates have conditional entropy averaging \(\beta(m+1)\). The \(m\) parity symbols recover them once one supplies \(t_0\). In the opposite direction the winding and availability schedules have \(O(m+1)\) phase cells. Their entropy plus the entropy of the independent bits bounds the word entropy by \(\beta(m+1)+O(\log(m+1))\). Divide by \(m\).

For each fixed \(k\)-bit pattern, its empirical frequency in the random rational words converges in probability to this law. Expectations are Riemann sums on the permuted \(n\)-grid for finitely many piecewise constant indicators whose endpoints converge as \(u/n\to\alpha\). Two occurrence indicators are independent unless their circular time windows of \(k+1\) independent inputs overlap, so the variance is \(O(k/n)\). Diagonal selection gives individual rational cycles converging in every fixed block frequency. The same fixed-determinant count as above applies to these shortcut roots, using their bounded odd width and hence polynomial maximum shortcut state. Bit choices are equiprobable and rooted words have at most two preimages; one can select the sequence with \(q\ge2^{(\beta-o(1))n}\) simultaneously.

At \(\beta=1/5\) the upper limiting odd width is \(2\cdot3^{1/5}<5/2\), the real minima grow, the total clock gap tends to zero, and the limiting parity entropy \(1/5\) exceeds the [ordinary lower bound](HEIGHT_ENTROPY.md) \(1/5.116201\). The denominators in the selected examples grow exponentially. This separates the entropy and real-width conditions from actual ordinary integrality. The [ordinary width-three theorem at PR213](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/WIDTH_THREE.md) uses additional integer stencil and divisibility arguments.

PR212 proves stronger denominator estimates for various families with width approaching two or a shrinking exceptional set. Formula (1) is the exact rate for a fixed band and includes the matching regime above three. The typical denominator result (2) leaves exceptional choices unrestricted. [PR212 coprime near-octave theorem](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/COPRIME_NEAR_OCTAVE.md) · [PR212 independent clocks](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/INDEPENDENT_CLOCKS.md)

