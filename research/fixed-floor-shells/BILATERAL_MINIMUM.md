# A minimum against every incoming branch at every future time

**PROPOSED.** Write \(U(n)=(3n+1)/2^{v_2(3n+1)}\) on positive odd integers. There is a probability law on simultaneous dyadic and ternary input digits under which a positive fraction of inputs resist *every* smaller affine competitor at *every* future time. Its probability equals the tail constant for the least predecessor times an explicit drift factor. The dyadic digits in this assertion are genuinely random, with positive entropy. An ordinary positive integer among these inputs would force an escaping orbit.

## Comparing sources at the same future target

Write \(F_a(x)=(3x+1)/2^a\) and \(I_a(t)=(2^a t-1)/3\). A forward positive-integer valuation word specifies one dyadic residue among odd integers. An infinite sequence specifies one odd dyadic integer. Independently prescribe a ternary origin \(z\). Reading the same forward letters from \(z\) defines ternary targets \(t_j\). At \(t_j\) every finite inverse word \(v\) legal in the ternary integers gives, as a function of a formal real starting variable \(x\), an affine competitor
\[
       I_v(F_{a_j}\circ\cdots\circ F_{a_1}(x))=s x+b .
\]
The inverse letters in \(I_v\) are read away from the target. Call this competitor smaller at large height if \(s<1\), or if \(s=1\) and \(b<0\). Include the empty inverse word. Let \(E_j\) mean that there is no smaller competitor at \(t_j\). Any earlier competitor persists by following the reference arm backwards first, so \(E_{j+1}\subset E_j\). Put \(E_\infty=\bigcap_j E_j\).

These are closed conditions in the joint space of finite-valued forward labels and ternary digits. Each specified failure is decided by finitely many digits. With the empty inverse word allowed, every surviving forward prefix satisfies \(2^{A_j}\le3^j\), where \(A_j=\sum_{i\le j}a_i\). This bounds each coordinate on the infinite survivor set and makes it compact. The corresponding odd dyadic and ternary points form a compact set as well. A fixed finite list of lowering comparisons cannot cover it.

For a Haar ternary target \(t\) write \(M(t)=\max_w 3^{|w|}/2^{A(w)}\), maximizing over its legal inverse words, including the empty word. Almost surely only finitely many words have multiplier at least one. For example the expected number at length \(j\) is at most \(3^{-j}\binom{\lfloor j\log_2 3\rfloor}{j}\), summable by Stirling's formula. Among maximizers choose the smallest inverse affine output at large height. The selected word \(w_*(t)\) is unique. Equal slopes force the same length and total valuation. For fixed length and total, distinct words have distinct affine numerators, by successively extracting their powers of two, or by the disjoint dyadic forward cylinders of two distinct words with the same total. The [least-predecessor renewal theorem](../critical-orbit-mellin/MINIMUM_CONSTANT.md) gives \(\Pr(M>u)\sim c_*u^{-2}\) with \(c_*>0\).

## The exact probability of infinite resistance

Draw the ternary origin from Haar probability and the forward letters independently with
\[
       p(a)=3\,4^{-a},\qquad
       S_j=j\log 3-A_j\log 2,\qquad
       \mu=\mathbb E S_1=\log 3-\tfrac43\log 2>0 .
\]
Then
\[
                      \Pr(E_\infty)=2\mu c_*>0.                 \tag{1}
\]
A typical path under this law has mean valuation \(4/3\) and every finite word has its iid frequency. These statements still hold almost surely conditional on \(E_\infty\). Thus even enforcing the entire collection of incoming inequalities leaves a positive-measure population with this growing forward itinerary.

For a fixed forward word of length \(j\), the affine map from its ternary origin onto its target cylinder multiplies Haar measure by \(3^{-j}\). The event that this word, read backwards from that target, is the chosen minimizer is exactly \(E_j\). Its word probability is \(p(w)=3^j4^{-A_j}=3^{-j}e^{2S_j}\). Consequently for every bounded nonnegative Borel test \(f\),
\[
 \mathbb E_{t} f(\log M(t))=
       \sum_{j\ge0}\mathbb E_{z,a} [e^{-2S_j}f(S_j)\mathbf1_{E_j}].       \tag{2}
\]
In particular this counts a tie only once. Every positive affine reparametrization of the terminal variable preserves the order used for the tie.

Here are the moving-window details in (1). Set \(K(s)=e^{-2s}\mathbf1_{[0,1)}(s)\). The expected renewal occupation \(N_v=\sum_{j\ge0}\mathbf1_{[v,v+1)}(S_j)\) has uniformly bounded second moment, over all real \(v\). After entry, a visit \(n\) steps later requires an independent displacement at most 1, an event of exponentially decreasing probability by the positive drift and an exponential moment. Summing over first entries bounds the first moment uniformly. Conditioning on each visit and counting subsequent visits bounds the second moment. The nonarithmetic renewal theorem for a positive-drift random walk gives
\[
    \sum_{j\ge0}\mathbb E K(S_j-v)\ \longrightarrow             (1-e^{-2})/(2\mu).
\]
For completeness this version follows by splitting the walk into excursions ending at strict ascending ladder epochs. Each ladder excursion has finite expected length since \(\Pr(S_n\le0)\ll e^{-cn}\). The convolution of the expected pre-ladder occupation with the compactly supported directly Riemann integrable kernel is directly Riemann integrable, by summable translated upper sums and truncation of the finite occupation measure. The first ladder height is nonarithmetic, since its support contains \(\log(3/2)\) and \(\log(9/8)\) with irrational ratio. Wald's identity and the ordinary positive-step key renewal theorem give the displayed limit. The uniform occupation bound permits conditioning on the first \(k\) steps for any fixed \(k\).

In (2) take \(f(s)=e^{2v}\mathbf1_{[v,v+1)}(s)\). The terms with \(j<k\) vanish for all large \(v\), since \(S_j\le j\log(3/2)\). For \(j\ge k\), replace \(\mathbf1_{E_j}\) by \(\mathbf1_{E_k}\). The total error is at most
\[
       (\mathbb E N_v^2)^{1/2}\,\Pr(E_k\setminus E_\infty)^{1/2}.
\]
First let \(v\to\infty\) with \(k\) fixed and condition on the ternary origin and the first \(k\) letters. Then let \(k\to\infty\). The renewal limit gives \(\Pr(E_\infty)(1-e^{-2})/(2\mu)\). The quadratic tail of \(M\) gives \(c_*(1-e^{-2})\) for the same quantity. This proves (1).

## What ordinary positive integers see

Let \(m(t)\) be the smallest odd positive integer reaching the odd target \(t\), including \(t\), and put
\[
       B_j=\{n:m(U^j n)=n\},\qquad b_j=d_{\rm odd}(B_j).
\]
These source sets decrease with \(j\). Their relative natural densities exist and satisfy the two identities
\[
 b_j=\mathbb E[e^{-S_j}\mathbf1_{E_j}]
     =\mathbb E_{t}[M(t)\mathbf1_{\{|w_*(t)|=j\}}],\qquad
       \sum_{j\ge0} b_j=\mathbb E_t M(t)\le2 .                  \tag{3}
\]
In particular \(\liminf_{j\to\infty} j^{-1}\log b_j\ge-\mu\). Indeed on \(E_\infty\), almost surely \(S_j/j\to\mu\), so the part with \(S_j\le(\mu+\varepsilon)j\) has probability bounded away from zero. These source sets resist arbitrarily deep incoming branches throughout the specified forward arm. The bound \(\sum b_j\le2\) concerns their limiting densities.

To justify the ordinary transfer for a fixed word \(w\), first allow competitors only up to a fixed total shortcut cost. For each of these finitely many words, the sign of the ordinary comparison eventually agrees with the affine comparison, including equal slopes. Congruence counting transfers that comparison to the terminal Haar cylinder. The following tightness observation permits removing the cutoff. Fix \(0<\eta<1\). Apart from an arbitrarily small fraction of odd targets in \([X,2X]\), the smallest predecessor is either below \(\eta t\) or reaches \(t\) along a path of bounded shortcut length. To see this, follow backwards the successive strict records on the simple path from the smallest predecessor to its first hit of \(t\). When \(m(t)\ge\eta t\), all records lie in \([\eta X,2X]\). Along the good clocks \(L\) of [FS-010, sections 1–3](PREDECESSOR_MINIMA.md), each record arc of at most \(L\) drops the logarithm of the backward record by \(\gg 1/L\) for sufficiently large \(X\). Thus at most \(O_\eta(L)\) short arcs occur before the first long arc or the minimum. The upper endpoint of any first long arc is one of \(O_\eta(X L p_L)+o_L(X)\) late endpoints of FS-010, and the original target is within \(O_\eta(L^2)\) subsequent shortcut steps. Since \(p_L\) decreases exponentially this exceptional fraction tends to zero. The fraction with \(m(t)<\eta t\) is at most \(\eta^2+o(1)\) by FS-010. These bounds also control every fixed terminal cylinder after dividing by its fixed density. Let the shortcut cutoff grow and then take \(\eta\downarrow0\). On the ternary side the finite comparisons decrease to the defining event for the selected word.

The source density of the given forward word among odds is \(2^{-A(w)}\). The target within that progression is equidistributed in its ternary cylinder. Long forward totals at a fixed \(j\) can be discarded with arbitrarily small upper density by the same dyadic word law. Thus the first formula of (3) follows from \(2^{-A}=p(w)e^{-S_j}\). Formula (2) at a single depth gives the second expression in (3), and \(\Pr(M>u)\le u^{-2}\) for \(u\ge1\) gives its last bound. Passing between proportional shells and initial intervals follows by dyadic subdivision with a final interval of arbitrarily small relative length.

## Exactly where the positive integer is needed

A positive ordinary integer in the **dyadic projection** of \(E_\infty\) has positive forward homogeneous multipliers at least one at every time. Its actual orbit cannot be eventually periodic, since the homogeneous multiplier around any positive cycle is strictly less than one. Conversely an escaping ordinary merger component contains an integer on the full diagonal of \(E_\infty\). On its positive odd states define
\[
    h(x)=x\prod_{i\ge0}\left(1+\frac1{3U^i(x)}\right).
\]
The product is finite by the [distinct-orbit reciprocal bound](../integrated/orbitwise-boundaries/README.md). We have \(h(x)\ge x\) and \(h(Ux)=3h(x)/2^{v_2(3x+1)}\). Choose a state minimizing \((h(x),x)\) in lexicographic order over the entire component. Such a minimum exists since the height is proper. Every legal inverse word ending at any actual future state gives a positive odd ordinary source in the same component. Its relative homogeneous multiplier is the ratio of the two \(h\)-values. That ratio is at least one, and at equality the second coordinate disposes of every strictly smaller offset. The chosen ordinary state therefore lies in \(E_\infty\).

Consequently the dyadic projection contains a positive odd integer exactly when a positive orbit escapes. Formula (1) determines the probability in an independent two-prime sampling law. The arithmetic question is whether that projection contains such an integer.
