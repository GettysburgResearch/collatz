# A dyadic height bound for open rational trajectories

**Status: PROPOSED.** This extends the [powered-prefix theorem](POWERED_WORD_HEIGHT.md) to open trajectories with arbitrary arc interiors and moving rational denominators. The closed-cycle corollary below has a stronger predecessor in PR212. The proof here uses only the classical fixed-form rational Subspace Theorem.

## Statement

Take a physical shortcut trajectory from a positive reduced rational \(x_0=A/q\), with \(\gcd(q,6)=1\); positive integer inputs have \(q=1\). The parity of a rational with odd denominator is its residue in \(\mathbb Z_2/2\mathbb Z_2\). The successive numerators \(A_i=q x_i\) are positive integers. Partition a length-\(D\) trajectory into at most a fixed number \(K\) of nonempty consecutive arcs. Let \(x_i\) be the endpoint after arc \(i\).

Supply rational references \(\xi_i,\eta_i\) at the two ends of each arc. They need only satisfy the *affine map of the known physical word*, not the parity constraints of its interior. Require \(x_{i-1}\ne\xi_i\) on every arc. Set \(b=\max_i\log_2\max(H(\xi_i),H(\eta_i))\), where \(H(p/s)=\max(|p|,s)\) for reduced fractions and \(H(0)=1\).

For any family of such paths with \(D\to\infty\) and \(b=o(D)\),
\[
 \liminf \frac{\log_2 \max(A,q)+(K-1)\log_2 q}{D}\ge1.             \tag{1}
\]
No hypothesis is imposed on the real terminal height or the interior valuations. The exponent of the numerator is sharp for positive integer sources consisting of one odd run. We have no sharpness result for the denominator cost \(K-1\) on open paths. The proof gives no uniform onset as \(K\) increases.

## Exact formulas and denominator costs

Pass to a fixed number \(k\le K\) of arcs. Write \(d_i,p_i\) for the length and odd count of arc \(i\), and \(U_i=2^{d_1+\cdots+d_i}/3^{p_1+\cdots+p_i}\), with \(U_0=1\). Its defining affine identity gives
\[
 U_i(A_i-q\eta_i)=U_{i-1}(A_{i-1}-q\xi_i).
\]
The reference difference at an interior join has the sign **previous end minus next start**. Thus
\[
 z_0+\sum_{i=1}^{k-1}z_i=U_k(A_k-q\eta_k)=L,\quad
 z_0=A-q\xi_1,\quad z_i=q(\eta_i-\xi_{i+1})U_i.              \tag{2}
\]
The initial separation ensures \(z_0\ne0\). The common denominator of \(\xi_i,\eta_i\) is at most \(2^{2b}\). Consequently \(|L|_2\le2^{-D+O(b)}\), including references with an even denominator.

With \(h_i\) a common denominator, the nonzero integer \(h_i(A_{i-1}-q\xi_i)\) is divisible by \(2^{d_i}\). Hence, uniformly,
\[
 d_i\le \log_2(A_{i-1}+q)+O(b+1),\qquad
 A_i+q\le2^{d_i}(A_{i-1}+q).                                  \tag{3}
\]
In particular the remaining length from boundary \(i\) is at most \(C_K(\log_2(A_i+q)+b+1)\).

Suppose the left numerator in (1) is at most \((1-\epsilon)D\) along infinitely many prefixes, with \(k\) in place of \(K\). The rational vector from (2) has all zero non-source terms deleted, passing to a fixed support. At infinity and three take all coordinate forms. At two replace the first by \(L\), preserving the other coordinates. On this vector their product satisfies
\[
  \prod_{p=\infty,2,3}\prod_j|L_{j,p}(z)|_p
  \le \max(A,q)\,q^{k-1}\,2^{-D+o(D)}.                        \tag{4}
\]
Indeed \(|z_0|_\infty\le\max(A,q)2^{o(D)}\), \(|z_0|_3\le2^{o(D)}\), and each remaining rational coefficient \(\eta_i-\xi_{i+1}\) has height \(2^{o(D)}\). The product of the three norms of \(U_i\) equals one, and the same product for \(q\) is \(q\). Clear only a power \(3^D\) and the small reference denominators, then primitive-normalize as in the [height ledger](POWERED_WORD_HEIGHT.md). The change in (4) costs \(2^{o(D)}\), and the primitive height is \(2^{O(D)}\) on the violating sequence. Thus the fixed-form theorem applies. Solving a rational exceptional relation omitting \(z_0\) for a non-source coordinate and substituting *only into the form at two* gives the same data in lower dimension. The following two alternatives deal with relations involving the source.

**When \(\log_2 q/D\) has a positive lower bound**, any such relation would express \(A/q\) as \(\xi_1\) plus a fixed rational linear combination of \((\eta_i-\xi_{i+1})U_i\). Every prime factor of the reduced denominator outside \(\{2,3\}\), with its full multiplicity, must then come from the fixed coefficients or the reference denominators. Their product is \(2^{o(D)}\). Since \(\gcd(A,q)=1\) and \(\gcd(q,6)=1\), this would give \(q\le2^{o(D)}\), a contradiction.

**When \(\log_2 q=o(D)\)**, (3) forces \(\log_2 A\gg_K D\). Pass to limits of all \(\log_2(A_i+q)/D\). Truncate at the first internal limit zero, when present, discarding only \(o(D)\) steps by (3). The violating margin survives (fewer arcs further decreases its left side). All earlier \(A_i\) are at least \(2^{cD}\) for some \(c>0\). For \(i<k\) the exact product
\[
 \frac{U_i A_i}{A}=\prod_{j=1}^i
       \frac{1-q\xi_j/A_{j-1}}{1-q\eta_j/A_j}=1+o(1)
\]
shows \(z_0/A\to1\) and \(z_i/A\to0\) for \(1\le i<k\). No fixed exceptional relation can then involve \(z_0\). Perform the truncation before applying (4) in this case.

The two alternatives suffice after passage to a subsequence since \(\log_2 q/D\) is bounded along a violating sequence. In either case, repeated elimination reaches a single coordinate. Then (2) has become \(z_0=L\). Since \(z_0\ne0\) has denominator at most \(2^{o(D)}\), its small two-adic norm implies \(|z_0|_\infty\ge2^{D-o(D)}\). This contradicts the real bound on \(z_0\) in (4) and the strict violating margin. This proves (1).

## A prior closed-cycle theorem and the open issue

In a primitive positive rational cycle of period \(D\), its common reduced denominator is coprime to six: it divides \(2^D-3^p\), with \(p\ge1\). For separated small-height references, PR212 proves a boundary has physical height at most \(2kH/(1-3^p/2^D)=2^{o(D)}\), using a standard two-logarithm bound and a bound \(H=2^{o(D)}\) for the common reference numerators and denominators. Cut at that boundary in (1). This recovers \(\liminf(\log_2 q)/D\ge1/K\).

**Priority.** This cycle rate, its general reference-arc formulation, and stronger clock-dependent conclusions are already in [PR212, MOVING_ARCS.md at 505d3fe782922904e86477990cc5d41e9110edda](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/MOVING_ARCS.md). Its [ARC_HEIGHT.md](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/ARC_HEIGHT.md) gives an effective, weaker rate and the small-boundary estimate. Here the cycle rate is an independently derived consequence of an **open-trajectory** inequality. None of the rational-spectrum conclusions follows from this argument.

At \(q=1\), a fixed positive input cannot have arbitrarily long prefixes with boundedly many separated reference arcs whose endpoint heights have logarithms \(o(D)\). The same restriction applies to *every* long window which costs more than its starting bit length by a fixed percentage. No such covers are constructed universally. For any arc one can formally take the physical trace as reference, in which case the separation fails identically. Replacing its ends by independently small rationals breaks the affine identity; that identity encodes the actual additive carry. The remaining issue is producing separated, low-height reference endpoints simultaneously on the actual successive words of a hypothetical exceptional orbit.
