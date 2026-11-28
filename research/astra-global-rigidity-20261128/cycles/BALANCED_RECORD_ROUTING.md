# Uniform inverse blocks realizing the last possible parity-record clock

Let \(T\) be the shortcut map. Put \(b_t(x)=2Q_t(x)-t\), and let \(v(x)\) be the first date of its lifetime minimum. Write \(D=1-\tfrac12\log_2 3\). The elementary record theorem gives \(v(x)<D^{-1}\log_2(2x)\) whenever the minimum is negative.

For every \(\eta<1\), every sufficiently large octave \([X,2X)\) contains at least \(X^\eta\) terminating integers with
\[
       v(x)=D^{-1}\log_2 x+O_\eta(1).                              \tag{1}
\]
At each of these integers the first lifetime minimum occurs exactly at the first visit to one. The discrepancy on the whole trajectory up to that visit is bounded in terms of \(\eta\) alone. This conclusion uses Weaver's supplied-state finite-policy theorem and Leen's qualitative absolute continuity at parameters just above one half. The fixed-total fine-scale input (J) in the confined-visitor proof is unnecessary. Using just the one finite policy of Weaver 127, Corollary 8, the same conclusion holds for every \(\eta<H(1/100)/\log(4/3)\), where \(H\) is binary entropy in nats. The latter ratio is approximately 0.194665.

## A balanced integer tree from cheap blocks

At an odd positive ternary unit \(y\), an inverse label \(e\ge1\) is legal when \(I_e(y)=(2^ey-1)/3\) is an integer prime to three. Each child is positive and odd. Its forward odd departure takes precisely \(e\) shortcuts to \(y\). Fix a block depth \(Q\), meaning a block contains \(Q\) odd inverse steps. The integer \(Q\) may have either parity. Suppose that every supplied positive odd unit admits at least \(L\) legal words of this depth, each with total clock at most \(2Q\) and last label at most \(R\).

If the previous outward discrepancy \(d=S-2q\) belongs to \([-5,0]\), and a supplied word has total \(s\le2Q\), increase its final label by
\[
              6\left\lfloor(2Q-d-s)/6\right\rfloor .               \tag{2}
\]
The child remains a positive odd unit because \(2^6\equiv1\pmod9\). The outward discrepancy after the modified word again belongs to \([-5,0]\). Among original words leading to the same modified word, the first \(Q-1\) labels agree and the last labels agree modulo six. Thus each modified word has at most \(\lceil R/6\rceil\) originals. Keep one copy of each. Starting with \(d=0\), iterate this construction. Each node has at least \(L/\lceil R/6\rceil\) children at the next block boundary.

Each modified block has at most \(2Q+5\) native steps. At native inverse depth \(i\), write \(d_i=i-2q_i\), counting the odd inverse edges encountered through \(i\). Each edge changes \(d_i\) by one, so \(|d_i|\le C=2Q+10\) everywhere. If \(S_j\) is the native depth of the \(j\)-th odd arrival, then \(S_j\ge2j-C\). At a completed boundary with \(q=mQ\) odd arrivals the full inverse iterate is
\[
 x=2^{S_q}3^{-q}(a-\beta_q),\qquad
 \beta_q=\sum_{j=1}^q3^{j-1}2^{-S_j}\le 2^C.
\]
Choose a fixed integer \(M\equiv4\pmod6\) sufficiently large that \(a=(2^M-1)/3>2^{C+1}\) and \(M>C+12\). This \(a\) is a positive odd unit, with shortcut word \(10^{M-1}\) to one. Start the tree there. Every physical terminal source obeys
\[
 (a-2^C)2^{-5}(4/3)^{mQ}\le x\le a(4/3)^{mQ}.                      \tag{3}
\]
Different complete words of the same odd depth give different odd sources, since the actual forward odd map recovers each label. The number of sources at depth \(mQ\) is at least \((L/\lceil R/6\rceil)^m\).

For a source at native inverse depth \(S=S_q\), its forward prefix discrepancy through time \(t\le S\) equals \(d_{S-t}-d_S\). In particular it is at least \(-C-d_S\) and its value at \(a\) is \(-d_S\). The last native segment to one has final discrepancy \(-d_S+2-M<-C-d_S\) and attains that value for the first time at its end. The subsequent cycle alternates between this value and one more. There was no earlier visit to one, because any such visit would keep the path in \(\{1,2\}\) and it later reaches \(a>2\). Thus the first lifetime minimum occurs exactly at \(S+M=2mQ+O_Q(1)\), with (1) following from (3).

Choose \(m=\lfloor\log(X/a)/(Q\log(4/3))\rfloor\). All these odd sources lie in \([c_QX,X]\) for a fixed \(c_Q>0\). Each has a unique dyadic lift into \([X,2X)\). The added number of initial even steps is uniformly bounded. The original minimum was strictly negative, so the new minimum is first reached at the same visit to one, after those extra steps. Distinct odd parts give distinct lifts. Consequently (1) holds with at least \(X^\eta\) examples for every
\[
            \eta<\frac{\log(L/\lceil R/6\rceil)}{Q\log(4/3)}.       \tag{4}
\]

## Fixed policies and the exponent tending to one

A fixed finite-precision, finite-cap, strictly positive legal policy from Weaver 127, Theorem 5, has uniform Cesàro convergence for continuous functions on the compact unit space. Let \(A\) be its stationary mean gap and \(B\) its stationary mean one-step choice entropy. If \(A<2\), then for any \(\epsilon>0\), for every sufficiently large \(Q\), every original unit supplies at least \(\tfrac12\exp((B-\epsilon)Q)\) legal depth-\(Q\) words with total at most \(2Q\).

For completeness, split a long run into chunks of fixed length \(k\). Choose \(k\) so the expected average gap and conditional choice entropy of a chunk differ from their stationary values by less than the chosen tolerance uniformly in its starting state. Both observables are continuous. Differences of realized chunk sums and their conditional expectations are bounded martingale differences, with variance \(O(k^2)\) per chunk. This applies to gap and to negative log transition probability, which is bounded for the fixed finite positive policy. Normalizing by the total length gives convergence in probability uniformly in the originally supplied unit. For \(Q\) large, paths with cost \(\le2Q\) and probability \(\le\exp[-(B-\epsilon)Q]\) therefore have mass at least one half. This proves the count. The cap \(R\) is fixed before \(Q\), so (4) gives every \(\eta<B/\log(4/3)\).

The 486-residue cap-six policy in Corollary 8 has \(A<1.938\) and \(B=H(1/100)\). All quantitative inputs to this specialization are present in the stated policy and its finite bias certificate. The supplied-state conclusion still uses the analytic stationarity theorem. [Weaver 127 v1, Theorem 5, Corollary 8 and (39)](https://rstation.ai/problems/collatz/papers/127/v1)

For the near-full exponent, take \(p>1/2\) approaching \(1/2\) in Leen's open tilted absolute-continuity range. The finite-policy construction through (4) in the pinned PR215 note produces, for any desired accuracy \(\epsilon\), a positive finite-precision policy with \(|A-1/p|<\epsilon\) and
\[
 B\ge -\log p-((1-p)/p)\log(1-p)-\log3-\epsilon .
\]
This construction derives the branching entropy on Haar-typical finite cylinders from the conditional independent-gap coding entropy, averages finite block flows, and mixes with a positive legal stationary flow before invoking Weaver 127. Only that construction and its supplied-state uniform law are used here. Its later exact-total correction lemma and the (J)-based central row floor play no role. Choose the tolerance also below \(2-1/p\). Then \(A<2\), and the certified lower bound for \(B\) tends to \(\log(4/3)\) as \(p\downarrow1/2\). This proves (1) for every fixed \(\eta<1\). The constants in its additive error and its octave threshold may depend on that fixed exponent. [Leen, *Tilted 3-adic Syracuse laws*, Theorem B(a) and §4](https://doi.org/10.5281/zenodo.23268832) · [PR215, finite-policy construction through (4), pinned commit 121054c](https://github.com/GettysburgResearch/collatz/blob/121054cf6569859585ede5c2d6e024eb2d97bbc5/research/astra-nine-hour-20261128/machinery/phase4/TILTED_ENTROPY_TRANSFER.md)

The bounded-discrepancy populations at first visits were already constructed in Weaver 211 with a quantitative strip-width relation under (J). This argument gives a separate route to the count exponent tending to one, with no quantitative dependence on the strip width. A previous padding by six in PR215 corrected a single terminal clock. Here feedback at every block confines the entire history, while bounding the loss of distinct histories. [Weaver 211 v1, Theorem 2](https://rstation.ai/problems/collatz/papers/211/v1)

The [exact finite control](check_balanced_routing.py) replays the six-step padding, genuine multiple fibres, bounded native discrepancy, rational inverse offset and literal first visits to one on a five-level physical tree. It does not certify the asymptotic policy supply or the external absolute-continuity theorem. Root retrieved Leen's primary TeX and matched SHA-256 `3855fc67c0c30c0e8e78af3de93fd85279d4376f2cb7c1e5d63d24433ce70afc`, then read Theorem B(a), the interval proof and its formalization boundary. Its analytic criterion and external Lean development were not independently rebuilt in this pass.
