# Visits to a sparse set at any height before the ordinary minimum

**Proposed, source-qualified written result.** Let \(T\) denote the positive shortcut, \(O(n)=\{T^j n:j\ge0\}\), and \(\tau(n)\) the first attainment of the global minimum \(m(n)\). Let \(U_X\) be uniform on the positive integers through \(X\). For an arbitrary deterministic set \(F\subset[R,\infty)\cap\mathbb N\), possibly infinite, define
\[
 w_R(F)=\sum_{i=0}^\infty
       \sqrt{\frac{|F\cap[2^iR,2^{i+1}R)|}{2^iR}}.
\]
There is an absolute constant \(C\) such that, uniformly in \(F\), as \(X,R\to\infty\) independently,
\[
 \Pr\big(\exists\,0\le t\le\tau(U_X):T^t U_X\in F\big)
                   \le C w_R(F)+o(1).                                  \tag{1}
\]
In particular, \(F\) may be the entire high part of **any** actual forward orbit, chosen afresh at each pair of cutoffs. The probability in (1) then tends uniformly to zero. The same holds for the union of any \(k=o(R^{1-\vartheta})\) orbit sets, for each fixed \(H_2(\log_3 2)<\vartheta<1\), where \(H_2\) is binary entropy in bits.

The single-shell square-root estimate and its matching sharp examples are due to the [ordinary lane in this pass](../ordinary/SHARP_SPARSE_TARGET_EXPONENT.md). Its independent-cutoff error cannot be summed over infinitely many target shells. Below we use its **finite word estimate before its error term**, control the end of each piece by an exponential tail in native time, and apply Leen's quantitative landing transport directly from the original source. Each target shell is charged only a bounded number of times. The single-shell examples also give the optimal order \(\sqrt\delta\) for a mask supported on one shell of fractional size \(\delta\). Formula (1) makes no assertion that the sum is optimal for multiple shells.

## A short descent from a reference source

Write \(\alpha=1001/1000\), and let \(W_b\) be uniform among odd integers in \([b,2b)\). An odd entrance below a threshold \(z\) means the first odd state at most \(z\) under the odd Syracuse step. A missing entrance has infinite date. Take \(z\) large, \(z\le b\le z^{\alpha^2}\), and \(K=\lfloor(\ln z)/10\rfloor\) native shortcut steps.

For any \(D\ge z/2\) and any \(A\subset[D,2D)\), the probability of seeing an odd member of \(A\) through date \(K\) is at most \(C\sqrt{|A|/D}\). This is the finite counting argument of equation (4) in [Sparse high targets](../ordinary/SPARSE_HIGH_TARGETS.md), with the endpoint argument of [Sharp sparse target exponent](../ordinary/SHARP_SPARSE_TARGET_EXPONENT.md). Its proof applies throughout this slightly larger source range. In detail, a true word of \(k\) odd gaps with total \(s\le K\) satisfies
\[
 1\le 2^s T^s n/(3^k n)\le \exp(K2^K/(3b))\le2 .
\]
Hence \(s-k\log_2 3\) belongs to an interval \(I\) of bounded length around \(\log_2(b/D)\), and \(b^{-1}\ll 2^{-s}3^k/D\). For each terminal value and word there is at most one source. Its terminal residue modulo \(3^k\) equals that of the stationary series with the reversed initial gap list. Fold the actual target onto the ternary residue grid using \(f(x)=3^K\#\{a\in A:a\equiv x\bmod 3^K\}/D\). Then \(f\le4\) since \(3^K=o(z)\), and its Haar integral is \(\delta=|A|/D\). With \(f_k\) its Haar conditional expectations and \(V\) the stationary random series, the word sum is bounded by an absolute constant times \(\mathbb E\sum_{k\le K} f_k(V)1_{\{s_k-k\log_2 3\in I\}}\), where the gaps are now iid of masses \(2^{-a}\). Stop the reversed string at its first simultaneous mark \(f_k(V)>t\) and drift in \(I\). Independent future increments give bounded expected further visits to \(I\), by the positive drift and exponential tail bound, uniformly in its position. The Haar maximal inequality and the stationary weak-\(L^2\) density give \(\Pr(\max f_k(V)>t)\ll\min(1,\sqrt{\delta/t})\). Integrating through \(4\) proves the finite estimate. Its only source-size restriction here is \(K2^K/b=o(1)\). The external endpoint is Weaver's original stationary law, in the cited written preprint. [Weaver, Paper 146/v1](https://rstation.ai/problems/collatz/papers/146/v1)

With probability \(1-O(z^{-c_1})\), a native state at most \(z\) occurs by date \(K\), for some absolute \(c_1>0\). Until such a state occurs, the total logarithmic additive correction is at most \(K/(3z)\). Failure through \(K\) therefore requires
\[
 g_K\ln3-K\ln2\ge -(\alpha^2-1)\ln z-\ln 2-K/(3z),
\]
where \(g_K\) counts odd departures. The native parity dictionary on the uniform odd residues modulo \(2^K\) gives \(g_K=1+\operatorname{Bin}(K-1,1/2)\) in law. Replacing those residues by \(W_b\) costs \(O(2^K/b)\) in total variation. The mean of the left side is \(-K\ln(4/3)/2+O(1)\), and \(\ln(4/3)/20>\alpha^2-1\). A binomial exponential inequality proves the claim. If the first native entrance is even, consecutive halvings thereafter lead to an odd value at most \(z\), with no intervening odd observation. Consequently, up to this same error, all odd observations **strictly before the first odd entrance** occur by date \(K\) and belong to \((z,z^2]\), since \(T(u)\le2u\) and \(2b\,2^K\le z^2\). This argument also controls missing entrances at the reference source. The clipped interval of possible observations is essential to the sum.

## First odd entrances on a grid of heights

First consider an odd target set \(E\subset[R',\infty)\), with its fixed dyadic shells \([D,2D)\), \(D=2^iR'\), \(i\ge0\). Fix a large cutoff \(B_0\). Start from \(W_b\), with \(b\to\infty\), and set \(z_j=b^{\alpha^{-j}}\), \(1\le j\le J\), stopping at the last \(j\) with \(z_j\ge B_0\). Thus \(z_J<B_0^\alpha\). For large \(b\) there is at least one threshold. Before the first odd entrance at \(z_1\) apply the short descent estimate with \(b=z_1^\alpha\).

For the portion beginning with the first entrance at \(z_j\), define \(g_j(v)\) to test whether an odd element of \(E\) is seen from \(v\), strictly before its first odd entrance at \(z_{j+1}\). Take \(g_j(v)=0\) for \(v\le z_{j+1}\), and allow an infinite path when the next entrance fails. A successful first landing at \(z_j\) is necessary to contribute to this piece. Its unconditional probability is exactly the success-masked landing functional \(\Lambda_{b,z_j}(g_j)\). Leen's Proposition *Transport*, at frequency zero, compares it to \(\Lambda_{z_j^\alpha,z_j}(g_j)\) with absolute error \(O((\ln z_j)^{-c})\), uniformly in the original \(b\ge z_j^\alpha\) and the bounded test. The latter piece is contained in the original reference path before its first odd entrance at \(z_{j+1}\): an entrance overshooting both thresholds makes the test zero. Its source is \(z_j^\alpha=z_{j+1}^{\alpha^2}\), in the short descent range. We never restart a transported entrance with a uniform distribution. [Leen, Proposition Transport and proper minimum law](https://doi.org/10.5281/zenodo.23269488)

For each threshold \(z=z_j\), the short descent charges only shells intersecting \((z,z^2]\), hence \(D\le z^2\) and \(2D>z\). Each fixed \(D\) qualifies at only \(O_\alpha(1)\) thresholds: the eligible \(\ln z\) range from at least \((\ln D)/2\) to at most \(\ln(2D)\), and increase by factor \(\alpha\) in reverse order. Uniformly in the original source,
\[
 \sum_j (\ln z_j)^{-c}\ll_\alpha(\ln B_0)^{-c},
 \qquad \sum_j z_j^{-c_1}\ll_{\alpha,c_1} B_0^{-c_1}
\]
for large \(B_0\), by the geometric progression of logarithms. Summing the local probabilities therefore costs at most \(Cw_{R'}(E)+O((\ln B_0)^{-c}+B_0^{-c_1})\) before the bottom entrance, including the case of a never completed grid.

On \(m(W_b)\le B_0\), the odd minimum forces entrance at \(z_J\). From the odd landing \(v\le B_0^\alpha\), the portion through the global minimum is a prefix of the true trajectory stopped at the minimum from \(v\). All the finitely many possible such prefixes have bounded maximum depending only on \(B_0\). Thus they avoid \(E\) for all sufficiently large \(R'\). The proper minimum law, applied to a uniform sample through \(2b\) and restricted to an odd source octave of proportion bounded below, implies \(\lim_{B_0\to\infty}\limsup_{b\to\infty}\Pr(m(W_b)>B_0)=0\). Taking \(b,R'\to\infty\) first and then \(B_0\to\infty\) proves the odd-target, odd-source estimate. The bottom argument uses properness only once and gives no numerical onset for the maximum of the retained stopped paths.

## All integer targets and whole future traces

For \(F\subset[R,\infty)\), include all its odd values in \(E\), and add every positive odd integer \((2^a y-1)/3\) with \(y\in F\) even and \(a\ge1\). After the first odd observation, a visit to an even \(y\) belongs to a halving string whose preceding odd value is precisely of this form. We have \(E\subset[R/2,\infty)\) for \(R\ge2\), and
\[
                         w_{R/2}(E)\ll w_R(F).
\]
Indeed the images of a fixed source shell \([D,2D)\) at a fixed \(a\) meet only a bounded number of shells of size comparable to \(2^aD\), with cardinality at most the original shell cardinality in each. Apply subadditivity of the square root and sum \(2^{-a/2}\). The odd elements alone cost exactly the original sum on the shifted grid.

A visit before the first odd value requires \(n=2^j y\) for some \(y\in F\). The contribution of each shell of left endpoint \(D\le X\) is at most \((|F_D|/X)(1+\log_2(X/D))\ll |F_D|/D\ll\sqrt{|F_D|/D}\). For the remaining path, condition on \(v_2(n)\) and split the odd part into dyadic octaves from the top. Truncating both indices at \(H\) loses \(O(2^{-H})+o_H(1)\) of the initial mass. The retained odd octaves all tend to infinity with \(X\) and have the same constant in the odd estimate. Now take \(H\to\infty\). This proves (1) with a uniform joint error, by the sequential characterization of the joint limit.

Leen's *Uniform sparsity of orbit sets* gives \(|O(n)\cap[a,a+u)|\le C_\vartheta u^\vartheta\) for every \(n,a,u\) and every \(H_2(\log_3 2)<\vartheta<1\), with rounding absorbed in the constant. Taking \(F\) to be the part above \(R\) of any union of \(k\) complete forward orbits gives \(w_R(F)\ll_\vartheta \sqrt{k}\,R^{-(1-\vartheta)/2}\) by a geometric sum. This proves the asserted uniformity over the choices of even unbounded orbits; the \(o(1)\) in (1) still has no explicit rate. [Leen, original Appendix A](https://doi.org/10.5281/zenodo.23252397)

Whenever \(w_R(F)=o(1)\), the law of the **entire possibly infinite set** \(O(U_X)\cap F\) is at total variation distance \(o(1)\) from
\[
                          \sum_C d_C\,\delta_{O(x_C)\cap F},              \tag{2}
\]
where \(x_C\) is any fixed representative of each actual component and \(d_C\) its density. Outside the event in (1) the observed set equals \(O(m(U_X))\cap F\) exactly, in all coordinates simultaneously. The discrete proper minimum law converges in total variation. For finitely many minima carrying mass \(1-\eta\), the symmetric differences of their forward orbits from the chosen component representatives are finite, since the respective ordinary paths actually meet. These differences miss **all** of \([R,\infty)\) for large \(R\). The common-coupling bound and \(\eta\downarrow0\) give (2), including its uniformity over such moving masks. This extends the single-octave component-mixture argument in [Sparse high targets](../ordinary/SPARSE_HIGH_TARGETS.md) to infinite target sets. For a fixed divergent representative \(x_C\) and \(F=O(x_C)\cap[R,\infty)\), the two possibilities in (2) are its whole actual high tail, with mass \(d_C\), and the empty set, with mass \(1-d_C\).
