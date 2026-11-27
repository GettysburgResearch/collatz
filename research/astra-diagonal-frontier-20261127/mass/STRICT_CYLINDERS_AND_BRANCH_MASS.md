# Exponential cylinder bounds for the strict law and summability below one on a ray

Write \(\lambda=\log_23\). Fix any \(\lambda<\beta\le7/4\), \(\omega=2^{\beta-\lambda}>1\) and \(\kappa=(\beta-\lambda)/(\beta-1)>0\). At a nonperiodic positive odd unit \(z\), let \(Q_z\) be the inverse natural entrance law and \(d_z\) its relative ordinary predecessor density. Let \(G_\beta\) denote \(S_i>\beta i\) at every positive reverse prefix. For any prescribed ordinary unit inverse word \(w\) of length \(k\) at \(z\) and integer \(E\ge1\),
\[
 d_z Q_z(G_\beta,\ [w],\ E_{k+1}\ge E)
       \le C_{\beta,\epsilon}
          \bigl(z\omega^k\,2^{\kappa E}\bigr)^{-1+\epsilon}
      \qquad(0<\epsilon<1).                                          \tag{1}
\]
With no lower bound specified on the next gap the same bound holds with the last factor omitted. All constants are independent of the root, word and gap threshold. The [positive physical lower floor](NO_RETURN_LANDING_FLOOR.md) implies \(d_zQ_z(G_\beta)\ge c/z\), so the conditional maximum cylinder mass given \(G_\beta\) is \(O_{\beta,\epsilon}(z^\epsilon\omega^{-(1-\epsilon)k})\). These bounds apply to the all-prefix strict event; an unconstrained ordinary inverse law can concentrate on arbitrarily long actual incoming segments.

On any one positive escaping unit ray \(a_0,a_1,\ldots\), form \(\mathcal A\) from all ordinary unit immediate parents \(x\) of \(a_n,\ n\ge1\), *other than* \(a_{n-1}\). The associated predecessor basins are disjoint. Put \(h=H_2(\log_32)=0.9499555271\ldots\). There is an absolute \(H<h\), conditional on the same external real-source (R4) input as in the [minimum-power theorem](PREDECESSOR_MINIMUM_POWER.md), such that
\[
 \sum_{x\in\mathcal A} d_x^{\,p}\ll_p 1,\qquad
 \sum_{n\ge1}(d_{a_n}-d_{a_{n-1}})^p\ll_p 1\qquad(p>H).              \tag{2}
\]
The same assertions, with the same constants, hold on **every finite positive unit path \(a_0,\ldots,a_N\) whose terminal \(a_N\) is nonperiodic**. In particular the statement has content on ordinary terminating trajectories before a cycle is reached. The unnormalized constants are independent of the particular path, its length and endpoint. Using just the elementary dyadic parity count, the same argument gives every \(p>h\). The usual disjointness proof only gives the case \(p=1\). The divergent-spine relative sibling summability and the earlier inverse-logarithm sufficient condition are attributed to Wren and Weaver in [Paper 200 v2, introduction](https://rstation.ai/problems/collatz/papers/200). Neither that lower condition nor its improvement below is established.

## Restricted real offsets at one root

As before \(A_i=3^i2^{-S_i}\) and \(B_i=\tfrac13\sum_{\ell=1}^iA_\ell\). A word failing the strict test already has zero mass in (1), so fix one which passes. On every subsequent strict word, \(A_{k+t}<\omega^{-(k+t)}\). Under \(E_{k+1}\ge E\) the step bound \(3\,2^{-E_{k+t}}\le3/2\) also gives
\[
 A_{k+t}\le\omega^{-k} 3\,2^{-E}(3/2)^{t-1}\qquad(t\ge1).
\]
This includes the case \(k=0\), using \(A_0=1\). Summing the smaller of the geometric upper bounds, first through \(\lfloor E/(\beta-1)\rfloor\), then after that clock, gives
\[
   0\le B_j-B_k\le C_\beta\,\omega^{-k}2^{-\kappa E}\qquad(j>k).      \tag{3}
\]
Indeed \(\log_2(3/2)=\lambda-1\), so the growing sum costs at most \(C\,2^{-E+(\lambda-1)E/(\beta-1)}\) and the decreasing tail costs at most \(C_\beta\,2^{-(\beta-\lambda)E/(\beta-1)}\). Without the next-gap restriction, direct summation gives \(C_\beta\omega^{-k}\). The shared prefix fixes \(B_k\) itself.

Use the true finite event that \(v\) first reaches \(z\) in \(j\ge k+1\) odd steps and satisfies the specified strict reverse constraints, including the word and optional next gap. All departed sites on its path to a nonperiodic \(z\) are distinct, also in the shortcut expansion. By the [uniform packing bound](CRITICAL_FIRST_ENTRY.md), \(z-B_j\ge c_0z\). Hence \(v=(z-B_j)2^{S_j}/3^j\ge c_0z\omega^j\), and for \(v\in[Y,2Y)\) there are \(O_\beta(1+\log(2+Y))\) possible \(j\). At each \(j\) only \(O(1)\) totals \(s=S_j\) are possible since \(Y/z\le2^s/3^j\le2Y/(c_0z)\). Formula (3) counts at most
\[
          1+C_\beta Y/(z\omega^k2^{\kappa E})
\]
ordinary sources per such pair. This integer \(+1\) is retained irrespective of the interval's width. The finite uniform source probability is bounded by
\[
 C_\beta(1+\log(2+Y))\bigl(Y^{-1}+(z\omega^k2^{\kappa E})^{-1}\bigr). \tag{4}
\]

The indicator of this finite event is a label whose one-edge exceptions lie in the union of the \(\beta\)-passing-to-\(z\) set, the endpoint of \(w\), its immediate parents, and \(z\). To verify this, if the retained suffix word still exists after removing the oldest forward edge, shortening preserves both that suffix and strictness of every remaining reverse prefix. If extending a retained word by one older edge fails the strict test, its new reverse debt is a weak running maximum and the new source therefore passes to \(z\). The only boundary where shortening can remove the requested suffix is its minimal length, ending at a direct parent of the endpoint of \(w\) (or at the endpoint in the version omitting that next gap). The first-arrival convention's boundary at \(z\) is included. Direct parents of any given target have \(O(1+\log Y)\) representatives through \(Y\), uniformly, and the passing-to-\(z\) sets satisfy the [uniform fixed-target entropy bound](CRITICAL_FIRST_ENTRY.md). Thus the [relative sparse-passage estimate](RELATIVE_SPARSE_PASSAGE.md) has constants common in \(z,w,k,E\).

Take \(D=z\omega^k2^{\kappa E}\) and \(Y=\exp(D^\eta)\) with \(0<\eta<\epsilon\). The octave estimate has relative multiplicative error tending to zero, and additive \(O_A(D^{-\eta A})\). Using (4) and \(A>1/\eta\) bounds the limiting natural mass by \(C_\epsilon D^{-1+\epsilon}\), enlarging constants for bounded \(D\). This limiting mass equals the left of (1): at fixed reverse depths the actual conditional source partition tends to \(Q_z\). The discrepancy between strictness through only a finite depth and full first-arrival strictness disappears by the tight countable first passing-to-\(z\) law and uniqueness of the hitting depth of any fixed label, as in [the ordinary exponent proof](ORDINARY_NO_RETURN_EXPONENT.md). Intersecting with the fixed cylinder and next-gap event only decreases that error. Short paths having fewer than a fixed number of letters have natural density zero. The version omitting the gap follows by \(E=1\) or directly by the shorter suffix.

## Entire-ray branch spectrum

Choose the fixed \(\beta>\lambda\) from the minimum-power theorem. For some \(H<h\) it supplies \(\#(P_\beta\cap[1,M])\ll M^H\), while its first-entry law satisfies
\[
        \mu_\beta(\{y\})\ll_\epsilon y^{-1+\epsilon},\qquad
        \mu_\beta\{y\ {\rm finite}:y>M\}\ll_\epsilon M^{H-1+\epsilon}.
                                                                         \tag{5}
\]
The constants are uniform across roots. On an escaping ray the forward \(\beta\)-debt tends to \(+\infty\), using the corrected height identity. Every input joining that ray therefore has a finite first permanent label \(y=F_\beta(v)\). Nonunit finite labels are single-source cells of zero natural mass. No independent resampling is performed at the attachment.

For \(M\ge3\), consider first labels \(y\le M\). If \(y\) occurs strictly before the source's first contact with the ray, then \(y\)'s deterministic future identifies its first attachment parent, provided the contact is at \(a_n,\ n\ge1\). Each such small \(y\) therefore specifies at most one possible member of \(\mathcal A\). If the first permanent label occurs on the ray, write \(y=a_i\) and denote its actual attachment by \(x\to a_n,\ i\ge n\ge1\). In reverse chronological order the final word to \(y\) then follows the prescribed ray backwards for \(k=i-n\) letters, and takes the gap of \(x\) at its next step. This segment is strict because \(y\) was the first permanent label at the original source.

If \(k\ge L\) the source satisfies the single prescribed \(L\)-letter reverse word at \(y\); if that word fails strictness the event is empty. Equation (1) bounds the total limiting mass by \(C_\epsilon(y\omega^L)^{-1+\epsilon}\). If \(0\le k<L\) but the attachment gap exceeds \(E\), sum (1) over the one possible spine word at each such \(k\). The bound is \(C_\epsilon y^{-1+\epsilon}2^{-(1-\epsilon)\kappa E}\sum_{k\ge0}\omega^{-(1-\epsilon)k}\). The finite sum over \(y\le M\) of \(y^{-1+\epsilon}\) is uniformly bounded by (5)'s counting estimate once \(\epsilon<1-H\). Consequently all these exceptional late clocks or large gaps cost \(O(\omega^{-(1-\epsilon)L}+2^{-(1-\epsilon)\kappa E})\) in natural source mass. This applies even when \(a_n\) or its parent is very large compared to the fixed small permanent label.

Among the remaining small-label sources, a pair \((k,e)\) at a specified \(y=a_i\) now determines its ordinary attachment parent by the unique physical parent formula. There are at most \(LE\) choices per \(y\). Together with the labels occurring before contact, this gives a set \(\mathcal A_M\) of at most \(C M^H(1+LE)\) parents which covers all the remaining possibilities. Natural upper probabilities here need only be summed over finitely many small \(y,k\); the globally larger labels were already covered by the tight probability in (5). Applying the bounds first to an arbitrary finite subset of the leftover disjoint branch basins and then taking the supremum proves
\[
  \sum_{x\in\mathcal A\setminus\mathcal A_M}d_x
    \ll_\epsilon M^{H-1+\epsilon}
                    +\omega^{-(1-\epsilon)L}
                    +2^{-(1-\epsilon)\kappa E}.
\]
Choose \(L,E\) as sufficiently large fixed multiples of \(\log M\). For the branch masses \(w_j\) rearranged nonincreasingly, this means
\[
  \sum_{j>K}w_j\ll_\epsilon K^{-(1-H)/H+\epsilon},\qquad
          w_j\ll_\epsilon j^{-1/H+\epsilon}.
\]
The logarithmic factors in \(|\mathcal A_M|\) are absorbed by arbitrarily small losses: for large \(K\) choose \(M\) of order \((K/(\log K)^2)^{1/H}\). The pointwise bound follows by comparison to the tail beyond \(\lfloor j/2\rfloor\). Hence \(\sum w_j^p\) is uniformly bounded for every \(p>H\). Each chronological increment \(d_{a_n}-d_{a_{n-1}}\) equals the sum of the disjoint ordinary sibling-basin densities for that \(n\), by the natural transition law at a nonperiodic unit. For \(H<p<1\), subadditivity of the \(p\)-th power proves the second assertion of (2); for \(p\ge1\) it is immediate from the mass bound. The relative version obtained by division by \(d_{a_{n-1}}\ge d_{a_0}>0\) has a ray-dependent constant.

Consequently, if at a positive-lower-density set of chronological indices every hypothetical escaping unit ray had relative off-spine gain \(\gg(\log(2+a_n))^{-B}\) with any \(B<1/H\), it could not escape. The maximum odd growth is \(Uu+1\le(3/2)(u+1)\), hence \(\log(2+a_n)=O_{a_0}(n+1)\), so choose \(H<p<1/B\) when \(B>1\) and sum the resulting divergent lower sequence in (2). The same conclusion holds for \(B\le1\) by plain summability. In particular the reduction allows \(B=1/H_2(\log_32)\), slightly above \(1.0526\), without knowing the extra R4 gain. No such lower bound has been established on every escaping ray. The proof gives new upper bounds for its genuine ordinary sibling spectrum and a weaker sufficient lower-bound target for excluding divergence.

For a finite path with nonperiodic terminal \(a_N\), use the target-stopped first passing-to-\(a_N\) label \(L_{a_N}\) throughout the branch cover. All designated branch sources reach \(a_N\) and hence have finite labels. Its possible labels are the set \(E_{a_N}\), which has the same uniform bound \(O(M^H)\) by the short/long original-source counting theorem, and the uniform atom and tail estimates in (5) hold for this law by that same theorem. A site passing to \(a_N\) has a passing continuation from itself to the end of this finite path. Its first-entry cell at \(y\) therefore has a strict reversed prefix from \(y\). The prefix and following-gap estimates (1) apply at the nonperiodic \(y\) just as on the infinite ray. If the low label is before contact its future identifies at most one designated branch, and if it is on the finite path the clock-and-gap argument only has fewer candidate phases. This proves (2) for every such finite path, without assuming global escape. Conversely uniform finite-path bounds recover the entire escaping-ray sums by monotone passage to the limit. The hypothesis on the finite terminal deliberately excludes cycle-parent basin overlaps.

## Sharpness of the fixed-root exponential scales

At every fixed \(\lambda<\beta\le7/4\), the exponential factors in (1) cannot be improved uniformly while allowing arbitrarily small power losses in \(z\). This assertion concerns a family of varying, explicitly constrained positive-integer roots that reach 1. It does not infer a counterexample to Collatz.

We use the extended ternary-precision version of the fixed-total lower bound stated and derived as [Weaver and Wren, Paper 200 v2, Input 3.3, equation (3.4)](https://rstation.ai/problems/collatz/papers/200). It gives fixed \(\delta,c,F>0,n_0\) such that for \(m\ge n_0,\ |s-2m|\le\sqrt m,\ 0\le b\le\delta m\), at each prescribed unit class modulo \(3^{m+b}\) there are at least \(c2^s/(3^{m+b}\sqrt m)\) words of length \(m\), total \(s\) and real offset at most \(F\) in that class. This is the source's retained fixed-total assumption, independent of the separate R4 assumption. Any positive lower bound for the count ensures a word.

Fix an odd unit \(u>2F+2\) reaching 1; for example take \(u=(4^t-1)/3\) at a sufficiently large \(t\not\equiv0\bmod3\). Given a unit class \(r\bmod3^b\), take \(m=\lceil 2b/\delta\rceil+n_0,\ s=2m\) and demand offset congruent to \(u-3^m2^{-s}r\bmod3^{m+b}\). This is a unit class. A selected word gives an ordinary positive odd source \(z=2^s3^{-m}(u-B_m)\equiv r\bmod3^b\); all earlier inverse offsets are likewise at most \(F<u/2\). Thus \(z\) reaches \(u\), is nonperiodic for sufficiently large \(b\), and \(\log z=O(b)\) with absolute constants. This prescribed-class result includes the actual ordinary size control needed to distinguish two exponential rates in (1).

For a chosen positive gap string \(w\) of length \(n\), its affine target congruence modulo \(3^n\), lifted once more to prescribe a unit residue of its final ancestor, determines a unit class \(r\bmod3^{n+1}\). Intermediate inverse states before the last one are units because each is the positive forward image of the next valid ancestor. In the constructions below strictness bounds every intercept by \([3(\omega-1)]^{-1}\), and the preceding roots grow exponentially in \(n\), ensuring positivity throughout. At the ordinary final ancestor \(x=(z-B_n)2^{S_n}/3^n\), arrange a strict infinite continuation using the lower bound \(d_xQ_x(G_\beta)\ge c/x\). The prefix is itself strict, so its continuation remains strict at \(z\). The natural cylinder telescope gives unnormalized mass at least \(c/x\) since \(d_z Q_z([w])=d_x\).

For the clock rate take \(S_j=\lfloor\beta j\rfloor+1\) for \(1\le j\le k\) and \(S_0=0\). Differences are positive integers and every prefix is strict, with final excess in \((0,1]\). Hence \(x\le2z\omega^k\), and the prescribed \(k\)-word has unnormalized strict mass \(\gg(z\omega^k)^{-1}\) at roots with \(\log z=O_\beta(k)\). For the gap rate take a sufficiently large initial \(E\) followed by ones; after \(t\) further letters the excess is \(E-\beta-(\beta-1)t\). Use the largest nonnegative \(t\) for which it is strictly positive. Then \(n=t+1=E/(\beta-1)+O_\beta(1)\), all prefixes are strict and the final excess is \(O_\beta(1)\). Its leaf has \(x\ll_\beta z2^{\kappa E}\), giving mass \(\gg_\beta(z2^{\kappa E})^{-1}\) for first gap at least \(E\), at roots with \(\log z=O_\beta(E)\). To realize both factors, precede the large gap by the preceding \(k\)-letter strict word and again continue with ones until only a bounded positive excess remains; then \(n=k+E/(\beta-1)+O_\beta(1)\), \(\log z=O_\beta(k+E)\), and the same proof gives the matching product lower bound.

If either exponent in the \(k\) or \(E\) factor were increased by any fixed positive amount, choose a power loss \(\epsilon>0\) sufficiently small compared with that amount and the linear upper bounds for \(\log z\). The just-constructed lower bounds contradict such a uniform strengthening even among terminating roots.

The unnormalized summability also bounds ordinary source diversity and Shannon information. If \(m_*(x)\) is the smallest positive odd ancestor of a nonperiodic unit parent, it may be divisible by three and then its own basin has zero density. To count small ancestor sources using a reciprocal density floor, restrict instead to the least **unit** ancestor \(m_*^\times(x)\), which always exists since \(x\) itself is a unit. Nesting and the unit density floor give \(d_x\ge c/m_*^\times(x)\). Thus \(\sum_{x\in\mathcal A}(m_*^\times(x))^{-p}\ll_p1\) for \(p>H\): at most \(O_p(M^p)\) distinct off-spine parents on any such whole path can receive unit sources at most \(M\). A nonunit source \(u\le M\) entering a unit branch has \(Uu\) a unit of size at most \(2M\) in the same branch unless \(u\) itself was the designated first parent, which the definition excludes. Hence \(m_*^\times(x)\le2m_*(x)\), and the same sum and counting bounds hold allowing all positive odd sources, with adjusted constants. This argument makes no claim that an individual nonunit has positive predecessor density.

For fixed \(H<p<1\), the natural inverse choice at \(a_n\) has probabilities \(d_{a_{n-1}}/d_{a_n}\) and \(d_x/d_{a_n}\) at its off-spine parents. Its Shannon entropies in nats satisfy, on every escaping ray,
\[
          \sum_{n\ge1}\mathsf H(Q_{a_n}(X_1\in\cdot))
                     \ll_p d_{a_0}^{-p}+d_{a_0}^{-1}<\infty .
\]
Indeed \(-u\log u\ll_p u^p\) on \([0,1]\) bounds all the off-spine terms by (2) and \(d_{a_n}\ge d_{a_0}\). The individual main-parent term satisfies \(-u\log u\le1-u\); summing uses the total off-spine weight at most one. The same estimate holds up to the end of every finite path covered above. This controls the Shannon entropy of the *full* one-step choice at every root on the specified ordinary path. Fixed-root positivity of the limiting entropy rate on an infinitely long reverse sample has different quantifiers. The bound does not assign any first moment to the numerical valuation \(E_1\).
