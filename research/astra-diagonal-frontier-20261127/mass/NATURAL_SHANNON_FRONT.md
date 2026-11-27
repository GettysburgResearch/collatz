# The expected information of the ordinary inverse path

Use nats and set \(D=\log(4/3)\). At a fixed nonperiodic odd unit \(a\), \(Q_a\) is the natural predecessor entrance law and \(P_{a,n}\) its distribution on complete reverse words of \(n\) odd steps. If the realized word ends at the ordinary unit \(x\), its information is \(I_{a,n}=-\log P_{a,n}([w])=\log(d_a/d_x)\). Write \(\mathsf H_{a,n}=\mathbb E_{Q_a}I_{a,n}\).

There are an absolute \(H<1\) and constants \(C_p\ge1\) for \(H<p<1\) such that
\[
 \sum_{U^nx=a,\ x\ {\rm unit}} d_x^p\le C_p^{n+1},\qquad
 \mathbb E_{Q_a} e^{(1-p)I_{a,n}}\le C_p^{n+1}d_a^{-p}.              \tag{1}
\]
One can use the same \(H<H_2(\log_3 2)\) after a choice of the R4 parameters as in the marker theorem. Without R4, elementary parity bounds give some \(H<1\), already sufficient for all Shannon conclusions below.

For **each** specified nonperiodic positive unit,
\[
 \lim_{n\to\infty}\mathsf H_{a,n}/n=D,\qquad
 \lim_{n\to\infty}\sum_w P_{a,n}([w])^{\,1+\xi/n}=e^{-\xi D}
                      \quad(\xi\in\mathbb R).                         \tag{2}
\]
The exponent is positive eventually for every fixed \(\xi\). In fact \(I_{a,n}/n\) converges to \(D\) in every finite positive moment. The input about realized information is [PR193, fixed-root theorem, equations (1)–(2)](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md), which explicitly includes the ordinary \(Q_a\). Existence of an almost-sure information limit alone does not allow averaging its unbounded logarithm.

If \(a_0,a_1,\ldots\) is one actual positive escaping unit ray with \(a_N=U^Na_0\), and \(k_N/N\to\tau\in[0,\infty)\), then
\[
 \lim_{N\to\infty}{\mathsf H_{a_N,k_N}\over N}=D(\tau-1)_+,\qquad
 \lim_{N\to\infty}\sum_w P_{a_N,k_N}([w])^{\,1+\xi/N}
                  =\exp[-\xi D(\tau-1)_+] \quad(\xi\in\mathbb R).      \tag{3}
\]
The oldest reference \(a_0\) is fixed while \(N\) moves. Here \(N\) counts physical odd steps along the ray, whereas \(k_N\) is the number of odd steps into the ordinary inverse distribution at \(a_N\). Also
\[
            \sup_{1\le k\le N}\mathsf H_{a_N,k}/k\longrightarrow0.      \tag{4}
\]
If \(k_N/N\to\infty\), then \(\mathsf H_{a_N,k_N}/k_N\to D\). This describes how positive fixed-root entropy and summable one-step entropies on a forward escaping ray can coexist. It uses no stationary root distribution.

## A uniform subunit moment at every finite depth

The depth-\(n\) ancestors of a nonperiodic \(a\) have pairwise disjoint predecessor basins, and each is itself nonperiodic. Fix \(b>0\) independently of \(a,n\). For an ancestor \(x\le X\) at exactly \(n\) odd steps the physical product gives \(2^s\le 4^n X/a\le4^n X\) for its division total. Since every word determines at most one source at fixed target,
\[
 \#\{x\le X:U^nx=a\}\le
 (4^nX)^b \sum_{e_1,\ldots,e_n\ge1}2^{-b\sum e_i}
          =\left({4^b\over 2^b-1}\right)^n X^b .                      \tag{5}
\]
This covers nonunit starts too. It concerns the actual number of physical candidate targets. It does not assert independence under \(Q_a\).

Choose the fixed \(\lambda<\beta\le7/4\), \(\delta,\eta,\tau_0\) in the proof of the [minimum-power theorem](PREDECESSOR_MINIMUM_POWER.md); write \(h=H_2(\log_3 2)\), \(g=\eta/2\) after decreasing \(\eta\) as there. Decrease \(\beta-\lambda\) if necessary to have \((1+\delta)(\beta-\lambda)<h/4\). Then choose \(b>0\) so \((2+\delta)b<h/4\). All choices precede \(n,a\). For each unit depth-\(n\) ancestor \(x\), split inputs in its basin by their first \(\beta\)-passing-to-\(x\) label \(y\). Its countable limiting weights \(\nu_x(\{y\})\) add to \(d_x\), and satisfy \(\nu_x(\{y\})\ll_\epsilon y^{-1+\epsilon}\), independently of \(x\), by the [target-stopped physical counting argument](ORDINARY_NO_RETURN_EXPONENT.md) at slope \(\beta\) and the common sparse-label estimate. No limiting theorem with constants depending on the exponentially large union of targets is used. The disjoint basins imply that each \(y\) can occur for at most one such \(x\).

Count the union of all these candidate \(y\in[Y,2Y)\) with \(Y\) large. As in the minimum-power proof, use \(M'=\lfloor Y^{1-\tau_0}\rfloor,\ k=\lfloor\log_2M'\rfloor,\ T=k+\lfloor\delta k\rfloor\). If its passing-to-\(x\) word has native duration \(s\le T\), then \(x\le 2^{T+1}Y\le2Y^{2+\delta}\). By (5) there are at most \(2^b C_b^nY^{(2+\delta)b}\) candidate \(x\). For each such fixed \(x\), each odd length and division total allows \(O_\beta(1+2^{(\beta-\lambda)T})\) original \(y\), by the bounded forward normalized offset in (5) of the minimum-power proof. Including the \(O((1+\log Y)^2)\) pairs, this gives \(O_\beta(C_b^nY^{h/2}(1+\log Y)^2)\) short sources on this octave. If \(s>T\), the same original \(y\) stays above \(M'\) at all shortcut times through \(T\), regardless of the eventual \(x\) and \(a\). Thus equation (29) of [Weaver, Paper 176 v1, §5.3](https://rstation.ai/problems/collatz/papers/176/v1) bounds the entire long group once by \(O(Y^{h-3\eta/4})\), exactly as in the minimum-power argument. Consequently the union has cardinality \(\ll C_b^nY^H\) with \(H=h-g<h\), adjusting constants for small \(Y\). No second factor counting targets occurs in the long group.

There is also a version independent of R4. Fix \(\beta=7/4,\ h_0=H_2(4/7)<1\), use \(T=\lfloor\log_2Y\rfloor\) and choose \(b>0\) so \(2b+(\beta-\lambda)<h_0\). For short words the same argument bounds the union by \(O(C_b^n(1+\log Y)^2Y^{2b+\beta-\lambda})\). For long words, the first \(T\) native parity positions have at least \(T/\beta\) odd departures. Each parity string is one residue modulo \(2^T\), and each residue has at most four representatives in \([Y,2Y)\). The number of strings is at most \(2^{h_0T}\) by the binary entropy bound. Thus the number of labels is \(O(C_b^nY^{h_0})\) for this slope, and every fixed \(p>h_0\) can be used below. The one-root information theorem and relative passage remain external inputs.

For \(H<p<1\), choose \(0<\epsilon<1-H/p\). By subadditivity and (5)'s counting consequence,
\[
  \sum_{U^nx=a,\ x\ {\rm unit}}d_x^p
    \le\sum_{x,y}\nu_x(\{y\})^p
    \ll_\epsilon \sum_{\text{distinct candidate }y} y^{-p(1-\epsilon)}
    \ll_{p,\epsilon} C_b^n ,
\]
where the last dyadic sum converges since \(p(1-\epsilon)>H\). This proves (1). Only nonperiodic roots are used: for cyclic roots, the unmodified depth partition can count multiple laps.

## Uniform integrability and the two clocks

Let \(p\in(H,1)\) be fixed. Equation (1) implies
\[
           \mathsf H_{a,n}\le { (n+1)\log C_p +p\log(1/d_a)\over1-p}.
                                                                         \tag{6}
\]
For fixed \(u>0\) and \(n\ge u/(1-p)\), concavity of \(t^{u/((1-p)n)}\) also bounds \(\mathbb E\exp(u I_{a,n}/n)\) by the right side of (1) to that power, uniformly for all sufficiently large \(n\). One may use \(2u\) to get uniform integrability at \(u\), and similarly for any fixed power of \(I_{a,n}/n\). PR193's almost-sure fixed-root limit now implies (2) and the moment assertion; writing the near-one sum as the expectation of \(\exp(-\xi I_{a,n}/n)\) covers both signs of \(\xi\).

For the moving root put \(d_N=d_{a_N}\); the increasing sequence has limit \(d_\infty\ge d_{a_0}>0\). At each \(a_i,\ i\ge1\), let \(\mathcal A_i\) be its unit parents apart from \(a_{i-1}\). Natural mass balance gives \(\sum_{x\in\mathcal A_i}d_x=d_i-d_{i-1}\). The finite branch-choice partition comprised of the main event at \(a_0\) and departures at the individual parents through \(a_N\) has entropy bounded independently of \(N\): the single main probability is \(d_0/d_N\), each other probability is \(d_x/d_N\), and \(\sum_{i,x}d_x^p<\infty\) holds uniformly by the [whole-ray bound](STRICT_CYLINDERS_AND_BRANCH_MASS.md). The word “finite” here refers to the number \(N\) of phases; the collection of parents at each phase is countable. Truncating the partition when fewer reverse letters are observed only merges outcomes and cannot increase this entropy.

Stopping at reference \(a_0\) or at the first off-spine parent gives a direct probability proof of (3). Conditional on following the main spine to \(a_0\), a prefix of length at least \(N\) consists of the fixed main word followed by a fresh \(Q_{a_0}\) inverse word. Conditional on first departing at \(x\in\mathcal A_i\), the number of fixed letters before reaching \(x\) is \(N-i+1\); subsequent letters have law \(Q_x\). These are the actual conditional cylinders, of respective probabilities \(d_0/d_N,d_x/d_N\), for the *same ordinary entrance law*. If the observed prefix ends before the nominated departure, its whole word follows the main ray and its information is \(\log(d_N/d_{N-k})\le\log(1/d_0)\). If it reaches the departure, its information is \(\log(d_N/d_x)+I_{x,k-N+i-1}\); the corresponding main formula uses \(\log(d_N/d_0)+I_{a_0,k-N}\).

Select \(a_0\) and a finite set of attached parents whose unnormalized masses cover all but an arbitrarily small part of \(d_\infty\), possible since \(d_0+\sum_{i,x}d_x=d_\infty\). For \(N\) beyond their phases, their conditional probability in this partition is close to one. At each fixed selected root the realized information divided by its own residual clock tends to \(D\); any bounded residual clock gives a fixed finite random information instead. Thus \(I_{a_N,k_N}/N\to D(\tau-1)_+\) in probability if \(k_N/N\to\tau<\infty\). For \(k_N=O(N)\), (1) gives bounded \(\mathbb E\exp(u I_{a_N,k_N}/N)\) for every fixed \(u>0\) and sufficiently large \(N\), by the same concavity bound with \(d_N\ge d_0\). Uniform integrability for every fixed power and both signs of the exponential proves (3). For \(k_N/N\to\infty\), the selected-root proof gives \(I_{a_N,k_N}/k_N\to D\) in probability and (1) again permits averaging.

For (4), take any sequence \(1\le k_N\le N\). Whenever \(N-k_N\to\infty\), its main \(k_N\)-prefix has probability \(d_{N-k_N}/d_N\to1\) and information tending to zero. The complementary event has probability tending to zero. Equation (1) gives a uniformly bounded positive exponential moment for \(I_{a_N,k_N}/k_N\) even at bounded \(k_N\): choose \(u=(1-p)/2\) in the concavity bound, using \(k_N\ge1\) and \(d_N\ge d_0\). Thus \(\mathsf H_{a_N,k_N}/k_N\to0\). If \(N-k_N\) is bounded along a subsequence, (3) with \(\tau=1\) gives the same result since \(k_N/N\to1\). The usual subsequence argument proves the supremum assertion.

In particular there is no inconsistency between the nonzero one-root entropy rate (2) and (4). At a specified root almost every infinite inverse sample accumulates unbounded information. On a putative escaping forward ray, probability concentrates on its actual incoming history for a macroscopic number of odd dates before reaching the oldest reference phase. The limiting expected information switches at that physical travel time. Excluding that delay requires ordinary arithmetic beyond the one-root information theorem.
