# Unlimited inverse clocks in the ordinary rank obstruction

**PROPOSED.** The Haar estimate of [the centered merger theorem](CENTERED_MERGERS.md) has an ordinary natural-density consequence even when the reverse arm is unbounded. Keep \(v\ge1\) and \(a\ge0\) fixed while taking \(U\to\infty\) through sources \(y=(3^v u-1)/2\), \(1\le u\le U\) odd and prime to 3. Let \(p_a\) be the proportion of resistant length-\(a\) words defined there. For any \(1/2<\theta<1\), at \(v>a\), the density of sources admitting \(P(m)<P(y)\) and \(T^t(m)=T^b(y)\) for *some* \(b\le a\) and arbitrary finite \(t\) exists and belongs to
\[
 [\,1-p_a,\quad 1-p_a+K_\theta^{a+1}(3/4)^{\theta v}\,].    \tag{1}
\]
All positive \(m\) are permitted. Consequently for a fixed small \(\eta>0\) and all large \(v\), at least \(c/\sqrt{a+1}\) of the ordinary sources in this slice have no such merger whenever \(a\le\eta v\), regardless of the reverse clock. Setting \(a=0\), most sources in high ternary-depth slices have **no cheaper pure ancestor at any depth**. A forward arm growing with \(v\) itself is necessary on the displayed populations. The source-dependent clock in a complete certificate, if any, remains open.

The proof adapts the parallel fixed-floor investigation's charging of long first-ancestry paths to descending records. To retain a positive forward arm we apply it to the least rank among a fixed-depth fiber.

## A transported rank

Use \(P(x)=(2x+1)^2/3^{d(x)}\), \(d(x)=v_3(2x+1)\), on all positive integers. For fixed \(a\), put
\[
 Q(z)=\min\{P(m):T^a(m)=z\},\qquad M(z)=\mathop{\rm argmin}_{T^a(m)=z}P(m).
\]
Every \(z>0\) has the preimage \(2^az\); every fiber is finite; and injectivity of \(P\) makes \(M\) unique. Also \(Q\) is injective, since a minimizing source has a unique endpoint. We have \(Q(z)\le (2^{a+1}z+1)^2\). All uses of \(Q\) are auxiliary to producing or excluding physical lower-\(P\) witnesses.

For \(z=T^a(y)\), if \(Q(z)<P(y)\), there is already an equal-\(a\) witness. Otherwise \(Q(z)=P(y)\). A witness with reverse length \(t\ge a\) gives a lower-\(Q\) ancestor \(T^a(m)\) of \(z\) at distance \(t-a\). Conversely, any lower-\(Q\) ancestor at distance \(b\) gives a lower-\(P\) witness by prepending the \(a\) steps from its minimizer. Any witness with a shorter forward arm can be extended to forward length exactly \(a\) by appending the same trajectory to both arms. These statements compare the two clocks explicitly.

## Rare long no-descent starts in a rank sublevel

Let \(D_L^Q=\{z:Q(T^j z)\ge Q(z)\text{ for }1\le j\le L\}\), and define \(D_L^P\) likewise. Using \(Q(T^j z)\le P(T^j M(z))\) gives \(M(z)\in D_L^P\) for \(z\in D_L^Q\). There is an absolute \(C\) such that
\[
 \limsup_{Y\to\infty}\frac1{\sqrt Y}
 \sum_{\substack{Q(z)\le Y\\z\in D_L^Q}}(1+d(M(z)))
 \le C\,2^{-(1-h)L},\qquad h=H_2(p),\quad p=\log_3 2.       \tag{2}
\]
Indeed \(M\) is injective, so one may sum over \(P(m)\le Y,\ m\in D_L^P\). At depth \(d(m)=s\) the inputs have \(2m+1=3^s u\) with odd unit \(u\le\sqrt{Y/3^s}\). For \(m\) large with \(L\) fixed, \(P(T^L m)\ge P(m)\) gives \(q_L-pL\ge-s/2-1\). To see this, write \((2T^L m+1)/(2m+1)=3^{q_L-pL}(1+O_L(1/m))\) and use \(d(T^L m)\ge0\). For fixed \(s,L\), the parity words are equinumerous in the limiting slice by the dyadic bijection and coprimality of 2 and 3. The fair-binomial bound, with \(\lambda=\log(p/(1-p))\), is
\[
 \Pr(q_L\ge pL-s/2-1)\le e^{\lambda(s/2+1)}2^{-(1-h)L}.
\]
Sum this against \(O((1+s)3^{-s/2})\), using \(e^\lambda<3\). Passing the limsup through the slice sum is valid by truncation: a tail \(s\ge S\) has trivial normalized contribution \(O(\sum_{s\ge S}(1+s)3^{-s/2})+O((\log Y)^2/\sqrt Y)\). This proves (2).

## Short drops and long gaps

Choose integers \(L\to\infty\) along which \(\min_{1\le j\le L}\|2pj\|_{\mathbb R/\mathbb Z}\ge c/L\). For example take \(L=q_k-1\) for convergent denominators \(q_k\) of the irrational \(2p\). Best approximation and \(\|q_{k-1}2p\|>1/(q_k+q_{k-1})\) give the bound.

For \(z'=T^j z\), \(1\le j\le L\), suppose both \(Q(z),Q(z')\ge B\). Their minimizers \(m,m'\) are at least \((\sqrt B-1)/2\), and meet at \(T^{a+j}(m)=T^a(m')\). For any fixed \(a,L\), all the states in these two indicated segments are \(\gg_{a,L}\sqrt B\) when \(B\) is large, since a step at least halves its input. Comparing the two product identities and the factors \(2m+1,2m'+1\) gives
\[
 \log Q(z')-\log Q(z)=k\log3-2j\log2+O_{a,L}(1/\sqrt B)
 \quad\text{for some integer }k.
\]
Thus any strict rank drop in such a gap reduces log-rank by at least \(c'/L\) for \(B\) sufficiently large in terms of \(a,L\). Also
\[
 Q(Tz)\le P(T M(z))\le C\,3^{d(M(z))}Q(z)
\]
with absolute \(C\), directly from \(2T(m)+1\le2(2m+1)\).

Fix a target \(z=T^a(y)\) with \(P(y)\le Y\) and \(Q(z)=P(y)\). Suppose it has a cheaper \(Q\)-ancestor, but its nearest such ancestor \(n\) is more than \(L\) steps away. Then \(n\in D_L^Q\), and \(z\) is a strict descending rank record on the path from \(Tn\), all of whose intermediate states have rank greater than \(Q(z)>Q(n)\). Equality would be an earlier occurrence of \(z\) by injectivity, shortening the original witness. Let \(r\) denote the preceding strict descending record, taking \(Tn\) as the first record.

If the gap from \(r\) to \(z\) is at most \(L\), charge \(z\) to \(n\). For this same \(n\) the records above \(Q(n)\) have total available log decrease at most \(\log(Q(Tn)/Q(n))\le C'(1+d(M(n)))\). Thus there are at most \(O(L(1+d(M(n))))\) such short-gap targets. The finitely many \(n\) with \(Q(n)\) below the cutoff for the log estimate contribute only \(O_{a,L}(1)\): their possible integer record ranks are bounded by \(Q(Tn)\).

If the gap exceeds \(L\), charge \(z\) to \(r\in D_L^Q\). Each \(r\) is charged at most once: \(z\) is its first strict drop. The state immediately before \(z\) is at most \(2z\), and its \(Q\)-rank is at least \(Q(r)\). Thus
\[
 Q(r)\le(2^{a+2}z+1)^2\le C_a(2y+1)^2=C_a3^vP(y).
\]
Here \(T^a(y)\le (3/2)^a(y+1)\). This rank bound is independent of the reverse clock and of the original smaller ancestor.

By (2), the upper number of long-tail targets divided by \(\sqrt Y\) has limsup at most \(C_a(L+3^{v/2})2^{-(1-h)L}\). A \(z\) has at most \(2^a\) preimages \(y\) at depth \(a\). The exact-\(v\) input slice has size comparable to \(3^{-v/2}\sqrt Y\); taking \(Y=3^vU^2\) recovers the stated parameter ordering. With \(v,a\) fixed, the relative tail tends to zero along the chosen \(L\)'s.

## Taking the reverse cutoff to infinity

For each finite reverse cutoff, the true success set has a density in the exact-\(v\) slice. For fixed forward and reverse words, ternary admissibility is a congruence, and a physically legal forward word is a dyadic congruence. The competing ancestor \(m\) is an affine function of \(y\) with positive rational slope. At large \(y\), strict rank advantage is decided by an integer threshold on \(d(m)\), with at most one boundary valuation requiring the sign of a fixed affine difference. Thus the set for each pair is eventually a finite union of residue classes on the slice. More explicitly, compare \((2m+1)/(2y+1)\) with \(3^{(d(m)-v)/2}\): the former tends to a positive constant, and in the equality-at-the-limit case its approach is from one fixed side or is identically equal. Positivity of all inputs holds for large \(y\).

The long-tail estimate shows that the increasing union over reverse cutoffs has natural density equal to the limit of the finite-cutoff densities. Indeed, if no lower-\(P\) witness at forward \(a\) occurs through reverse length \(a+L\), any eventual witness supplies a \(z\) of exactly the long-tail kind just counted. The lower bound in (1) comes from true centered competitors. The upper bound for every finite cutoff follows by the Haar/CRT estimate on off-center words and the resistant-prefix property in [the centered merger theorem](CENTERED_MERGERS.md). Taking the cutoff to infinity proves (1).

The order of limits matters. Constants in the long-tail estimate may depend on \(a,v\); for each integer \(v\) and \(a\le\eta v\) they are fixed when taking natural density. The resulting bound in (1) is uniform in these integers. No assertion of uniformity for \(v=v(U)\) is made with unlimited reverse time.
