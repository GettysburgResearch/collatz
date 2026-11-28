# Decoding a growing ordinary shift from the critical ternary source

Let \(X\sim\mu_*\), let \(d_W=H(E\mid X\bmod3^W)\) be the conditional entropy of its first planted gap, and let \(J\) be independent and uniform on \(\{0,\ldots,D-1\}\). There exists an absolute \(\eta>0\) such that, as \(W\to\infty\),
\[
   D\le d_W^{-\eta}\quad\Longrightarrow\quad
          H(J\mid X+2J\bmod3^W)=o(1),\qquad
          H(X+2J\bmod3^W)-H(X\bmod3^W)=\log D-o(1).                 \tag{1}
\]
The error is uniform on this range. Since \(d_W\downarrow0\), the allowed number of shifts tends to infinity. For every fixed finite independent integer jitter, even or odd, exact translation singularity already gives eventual recovery. Formula (1) gives a growing range for the specified evenly spaced family, with an explicit choice of exponent below. [Affine classification](CRITICAL_AFFINE_OVERLAPS.md)

Fix \(d\ge1\). The [deterministic zero-level steering](DETERMINISTIC_COUNTED_FUSION.md) supplies positive odd starts separated by \(2d\) which fuse at a common odd endpoint with common odd count \(n\ge1\) and common physical clock
\[
            t\le 6+7\log(2+3d),\qquad n\le t.
\]
The corresponding distinct length-\(n\) inverse words \(u,v\) satisfy \(A_u(z)=A_v(z+2d)\) as affine maps. Both have exactly the same planted probability \(p=\theta^nq^{t-n}\), at least \(m^t\) where \(m=\min(\theta,q)>0\). In a planted depth-\(n\) sample, condition on the event that the first word is \(u\) or \(v\). This has probability \(2p\), the label is fair, and the independent suffix has law \(\mu_*\). The observed planted source modulo \(3^{W+n}\), after the common affine change of coordinates, contains exactly the same information about the label as observing one of \(X,X+2d\) modulo \(3^W\), because the common slope has 3-adic valuation \(n\).

For the unconditioned planted sample the conditional prefix entropy equals
\[
 H(E_1,\ldots,E_n\mid Z\bmod3^{W+n})
   =n\log3+H(\mu_W)-H(\mu_{W+n})
   =\sum_{i=1}^n d_{W+i}\le n d_W.
\]
The identity follows by inverting the *known* prefix on a residue; no unknown digits are refreshed. Discarding the entropy contribution from the complementary event shows that the binary-label entropy in the two-shift experiment is at most \(n d_W/(2p)\). If the two component laws on residues have mass functions \(P_0,P_d\), concavity of binary entropy on each side of one half yields
\[
              \sum_x\min(P_0(x),P_d(x))\le\frac{n d_W}{2p\log2}.
\]
Indeed for a binary posterior \(v\), \(h(v)\ge2\log2\min(v,1-v)\); integrate this against the equal mixture. In particular there is an absolute \(C\) such that for \(1\le d<D\) the overlap is at most \(C\log(2+D)(2+D)^{K} d_W\), with \(K=7\log(1/m)\).

The maximum-posterior estimate of a uniform \(D\)-way label has error at most \(D^{-1}\sum_{j<k}\sum_x\min(P_j(x),P_k(x))\): at each residue each nonmaximal likelihood is bounded by its pairwise minimum with a maximizing one. All these overlaps are of the two-shift form with \(d=k-j\). Thus its error is at most \(C D(2+D)^K\log(2+D)d_W\). Choose, for instance, \(\eta=1/[2(K+2)]\). At \(D\le d_W^{-\eta}\) this error times \(\log(2+D)\) tends to zero. The elementary error-indicator entropy bound \(H(J\mid\text{observation})\le h(P_e)+P_e\log D\) proves (1). For the entropy gain use translation invariance of entropy on the finite group to identify \(H(X+2J\bmod3^W\mid J)=H(\mu_W)\).

The same proof works for every fixed \(\theta_*\le\theta<1\) with its own \(d_W=H(E\mid Z\bmod3^W)\to0\), replacing the prefix input entropy \(n\log3\) by \(nH(p_\theta)\) and taking \(K=7\log(1/\min(\theta,1-\theta))\). This predicts separation of shifted copies of the critical or lower-entropy planted law. Bounding below the mass assigned to a typical Haar cylinder would still require a new argument.
