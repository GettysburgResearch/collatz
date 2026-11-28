# Neutral odd grades recur for two nonresonant affine starts

**Proposed written theorem on the genuine dyadic parity driver.** Start the shortcut map on \(X=A n+c\), \(Y=B n+d\), where \(A,B\) are positive odd integers and \(B/A\notin3^{\mathbb Z}\). Take \(n\) Haar-uniform in \(\mathbb Z_2\); finite prefixes also apply to ordinary affine starts in complete binary blocks. The offsets \(c,d\) are integers. Let \(P_j,Q_j\) count odd departures on the two arms, and let \(X_j,Y_j\) denote their genuine states. There is an integer \(M_{A,B}\), independent of the offsets, such that almost surely infinitely many physical dates \(j\) satisfy
\[
        P_j=Q_j,\qquad A Y_j-B X_j\in[-M_{A,B},M_{A,B}]\cap\mathbb Z. \tag{1}
\]
The second expression at equal grade is an **ordinary** integer determined by the exposed finite low bits. At these returns the two arms reproduce an affine relation of their initial slope ratio with a bounded new offset. For either arm its homogeneous multiplicative slope tends to zero exponentially along these dates. This result concerns the full-measure dyadic driver and finite symbolic returns among ordinary starts. It does not assert infinite recurrence at any one positive ordinary parameter.

For \((A,B)=(1,5)\), set \(D_j=Q_j-P_j\). There are absolute constants with
\[
 \mathbb E D_h^2\ge\lfloor h/3\rfloor/2,\qquad
 \mathbb E D_h^4\le3h^2+h,\qquad
 \sum_{j<h}\Pr(|D_j|\le K)\ll(K+1)\sqrt{h+1}.                        \tag{2}
\]
These finite inequalities hold exactly for a uniform ordinary parameter in any complete binary interval of length \(2^h\) with positive arms. In particular a fixed positive fraction have grade difference of order at least \(\sqrt h\) in absolute value for all sufficiently large \(h\). This proof extends the affine-level and normalized-offset analysis for pairs of slope ratio \(3^s\). The resonant process can absorb at an exact merger. Here exact Haar mergers have probability zero at all dates. [PR146 affine-gap process](https://github.com/GettysburgResearch/collatz/blob/0410811710af2f7da71522ec67233528048adb9a/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md) · [Primary finite slope criterion, Proposition 1](https://rstation.ai/problems/collatz/papers/204/v1)

## The embedded simple walk

After exposing \(j\) low bits write \(n=r+2^j m\). The current states are \(A3^{P_j}m+c_j,B3^{Q_j}m+d_j\) with integers \(c_j,d_j\), and the remaining parameter \(m\) is fresh Haar. The two next parities are either always equal or always opposite before the next fair bit is drawn, since both coefficients are odd. Accordingly \(D_j\) either stays fixed or makes an equiprobable signed unit jump. Successive signs at jumps are independent fair signs, because the decision to jump uses only the past.

At level \(D_j=z\), a run of at least \(h\) equal pairs of parities requires the two current states to coincide modulo \(2^h\): the length-\(h\) shortcut parity word parametrizes the original residue modulo \(2^h\) bijectively. Thus, conditional on the past, that run has probability at most \(\min(1,2^{v(z)-h})\), where
\[
       v(z)=v_2(A3^{(-z)_+}-B3^{z_+})<\infty.
\]
The integer inside is nonzero by the slope hypothesis, and \(v(z)\ll_{A,B}1+|z|\) by its usual size. Every next jump occurs almost surely. The expected number of physical dates spent on one visit to embedded level \(z\) is \(O_{A,B}(1+|z|)\), including its initial date. The same conditional bound is valid at any deterministic or stopping date within that visit. For \((1,5)\) the coefficients modulo eight lie in \(\{1,3\}\) versus \(\{5,7\}\), so \(v(z)\le2\) at every level.

Let \(J_N\) be the physical date just after the \(N\)-th jump. At embedded dates the levels form an ordinary simple symmetric random walk. Its expected number of visits to any one specified level before step \(N\) is \(O(\sqrt N)\), uniformly in the initial and tested levels, by the binomial point bound. At level zero it is at least \(c\sqrt N\) for sufficiently large \(N\) depending on the fixed initial level, by the binomial local lower bound on the correct parity. Consequently
\[
 \mathbb E\sum_{j<J_N}{\bf1}_{|D_j|\le l}
       \ll_{A,B}(l+1)^2\sqrt N,\qquad
 \mathbb E\sum_{j<J_N}{\bf1}_{D_j=0}\ge c\sqrt N.                    \tag{3}
\]
When \(v(z)\le2\) uniformly, the first bound improves to \(O((l+1)\sqrt N)\). Since \(J_h\ge h\), this gives (2)'s occupation estimate. In each three physical steps the chance of at least one differing pair is at least \(1/2\) in that case. The conditional second-moment increment of \(D_j\) is the activity indicator. The fourth-moment increment is \((6D_j^2+1)\) times that indicator. Summing, using \(\mathbb E D_j^2\le j\) from initial zero, gives both moments in (2). Paley–Zygmund on \(D_h^2\) gives the stated positive fraction.

## A bounded integer offset at recurrent visits

Define \(R_j=(B/A)3^{D_j}\) and
\[
             Z_j=(Y_j-R_jX_j)/\max(1,R_j).
\]
The coefficient of the unexposed parameter cancels, so \(Z_j\) is a real rational determined by the past. For a branch write \(s_x=3^{e_x}/2,\ s_y=3^{e_y}/2\), with \(e_x,e_y\in\{0,1\}\) its two parities. The true updates have offsets \(e_x/2,e_y/2\) and \(R_{j+1}=R_js_y/s_x\). Thus
\[
 |Z_{j+1}|\le a_j |Z_j|+1,\qquad
 a_j=s_y\max(1,R_j)/\max(1,R_{j+1}).
\]
For \(R_j\ge1\) the coefficient \(a_j\le s_x\), and for \(R_j\le1\) one has \(a_j\le s_y\). In either case the bounding multiplier is \(1/2\) or \(3/2\) with equal conditional probabilities. Fix \(0<p<1\), and put \(\gamma=((1/2)^p+(3/2)^p)/2<1\). Then
\[
      |Z_{j+1}|^p\le a_j^p|Z_j|^p+1,\qquad
                         \mathbb E(a_j^p\mid\mathcal F_j)\le\gamma.
\]
An \(l\)-fold future product has conditional expectation at most \(\gamma^l\) by iterated conditioning. Expand the displayed recurrence and retain returns \(D_j=0\) with \(j<J_N\). The initial term sums to at most \(|Z_0|^p/(1-\gamma)\). For the term whose future product has length \(l\), its starting date \(i=j-l\) must satisfy \(|D_i|\le l\) and \(i<J_N\). Both restrictions are known at date \(i\). Drop the later restrictions before estimating the conditional product. Equation (3) gives
\[
 \mathbb E\sum_{j<J_N:D_j=0}|Z_j|^p
       \ll_{A,B,p}|Z_0|^p+\sqrt N\sum_{l\ge0}\gamma^l(l+1)^2.          \tag{4}
\]
All terms are nonnegative. In particular the estimate remains valid at the unbounded physical stopping date.

Choose \(M\) large enough in terms of \(A,B,p\). By (3)–(4), for sufficiently large \(N\) depending also on the initial state, the expected number \(L_E\) of visits before \(J_N\) to \(E=\{D=0,|Z|\le M\}\) is at least \(c'\sqrt N\). The second moment of the full zero-level occupation \(L_0\) before \(J_N\) is \(O_{A,B}(N)\). In fact at each date counted in \(L_0\), the conditional expected number of its own and subsequent zero-level visits before \(J_N\) is \(O_{A,B}(\sqrt N)\) by the same holding and embedded Green bounds with at most \(N\) jumps still available. Summing the ordered pairs of dates and doubling bounds \(\mathbb E L_0^2\). Cauchy–Schwarz now gives a fixed positive probability of a future visit to \(E\), uniformly over every initial history, by sending \(N\) sufficiently far for that history.

In fact the future visit has conditional probability one. Otherwise, on the event of no visit the conditional probabilities of that event given the first \(j\) bits tend to one by bounded martingale convergence. At each such date the preceding uniform positive lower bound for a subsequent visit makes those conditional probabilities at most \(1-c''\). Restarting at every deterministic date gives infinitely many visits almost surely. At level zero, \(A Y_j-B X_j=\max(A,B)Z_j\) is integral, proving (1). Each arm separately starts from Haar measure and has iid fair shortcut parities. Its long-run log slope per time equals \(-\log(4/3)/2\), proving the simultaneous slope assertion.

For ordinary inputs the same arguments imply a finite return after every **fixed** requested date, with both states reduced by any fixed factor, for a set of parameters of natural density one. Indeed the almost sure event contains a qualifying finite symbolic prefix, and a finite selection of such prefix cylinders has Haar mass arbitrarily close to one. Each of the finitely many affine constants is then negligible compared with the growing positive parameter. Complete residue periods give their ordinary density. The location-uniform finite assertions (2) need no such limiting argument.

At a specified date \(j\), equal endpoints of the two arms impose one affine equality with slopes \(A3^{P_j}\ne B3^{Q_j}\) on each of the \(2^j\) parameter cylinders. There are at most \(2^j\) individual ordinary solutions over *all* integers, and at most countably many dyadic solutions across all finite dates. Thus (1) does not produce direct Haar mergers, whose probability is zero. Conversely, if two fixed ordinary arms share an escaping component, after their asynchronous merger they follow one simple escaping ray with a fixed time displacement \(r\). At a neutral bounded-offset return their current values then satisfy \(A Y_j-B X_j=O_{A,B}(1)\). At that fixed displacement the actual endpoint is an affine function of the earlier value with slope \(3^k/2^{|r|}\), in one of finitely many parity words. None can coincide with \(B/A\) or its reciprocal: an equality between these odd rational ratios and such a slope forces \(r=0\), then equality of the two initial slopes. The bounded offset therefore bounds the current value, contradicting simplicity and escape at all sufficiently late dates. This excludes infinite returns for those actual pairs, while the density-one statement supplies only one finite return beyond each separately fixed date.
