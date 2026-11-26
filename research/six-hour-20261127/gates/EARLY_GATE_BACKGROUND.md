# The diffuse part of the physical exit gates

**Status.** Written proposal on the positive ordinary shortcut map. The harmonic result and the auxiliary finite-clock estimates below use elementary counting. They do not use a basin-density theorem or assume that any orbit escapes. The identification of a possible normalized residual with infinite-orbit charges remains source-qualified.

## A nonzero limit before the critical depth

Use the shortcut \(T(2u)=u\), \(T(2u+1)=3u+2\). From each \(1\le x<X\), let \(\tau_X(x)\) be the first time its orbit is at least \(X\), with value infinity on failure. Its first exit \(z=T^{\tau_X(x)}x\) lies in \([X,3X/2]\). At an exit, write \(w\) for the product of \(3v/(3v+1)\) at the odd departures before that first hit. All measures in this note are **unnormalized**. In particular each harmonic source pays \(w/x\), without division by \(H_{X-1}\).

Under fair independent binary letters, set \(S_j=B_j\log3-j\log2\), where \(B_j\) counts the ones through time \(j\). Put \(a=\log(3/2)\). Let \(L\) be the defective distribution of \(H=S_\sigma\) at the first strict time \(\sigma\ge1\) with \(S_\sigma>0\). Thus \(0<H\le a\) on success, and \(p=L((0,a])<1\). Define
\[
 \mu(dv)=\frac{L((v,a])}{1-p}\,\mathbf1_{0\le v\le a}\,dv .
 \tag{1}
\]
For every fixed
\[
 0<c<c_0=1+\frac{\log2-\tfrac12\log3}{\log(3/2)}
         =\frac{\log3}{2\log(3/2)}=1.35475\ldots
\]
put \(K=\lfloor c\log_2 X\rfloor\). Then
\[
 \sum_{x<X,\,\tau_X(x)\le K}\frac{w}{x}\,
        \delta_{\log(z/X)} \ \Longrightarrow\ \mu .
 \tag{2}
\]
Its total tends to \(\mathbb E\sup_{j\ge0}S_j=\int H\,dL/(1-p)>0\), an ordinary constant. In particular it is only of order \(1/\log X\) in the *normalized* harmonic gate law. The assertion for \(c>1\) concerns the clocks of ordinary exits only. It requires no equidistribution of physical parity words of length \(c\log_2 X\) across the shell.

There is an exact law for the complete off-sieve gates. Use PR201's OP-G3 sieve \(E_X\) at rank \(k=\lfloor\log_2X\rfloor\). Read a native length-\(k\) word backwards from a possible gate. Its suffix multipliers must be at least \(1/2\) at every depth. Retain shell integers satisfying its rank-\(k\) terminal congruence modulo \(3^{B_k}\), then union over the retained words. Every exit of time at least \(k\) enters this sieve for all large \(X\). Indeed on any last \(j\le k\) steps from \(u<X\) the real affine intercept is at most \((3/2)^j-1=o(X)\), so the multiplier is at least \(1-o(1)\). The integral endpoint equation supplies the congruence. Also \(|E_X|=o(X)\). For this weaker cardinal estimate, the final multiplier alone implies \(B_k\ge(k-1)\log_3 2\). The binomial upper tail gives \(O(2^{(\theta+o(1))k})\) such words with \(\theta=H_2(\log_3 2)<1\), and each word has \(O(1)\) representatives since \(3^{B_k}\ge2^{k-1}\). PR201 proves the sharper \(O(X^\theta/(\log X)^{3/2})\) using every suffix constraint. [PR201, OP-G3 at 21bed7ac](https://github.com/GettysburgResearch/collatz/blob/21bed7ac2b1b1bb4baf0f6cabd53f8b9dd11b58a/research/unconventional-20261126/operator/GATE_ARITHMETIC.md)

Then
\[
 \sum_{x<X,\,\tau_X(x)<\infty,\ z\notin E_X}
          \frac w x\,\delta_{\log(z/X)}\ \Longrightarrow\ \mu .
 \tag{3}
\]
In particular, writing \(A_X=H_{X-1}\|J_X\|_1\), the *unnormalized* mass at the explicit thin labels is \(A_X-\mu([0,a])+o(1)\). Formula (3) estimates the actual leakage through the sieve, including its positive leading constant. It permits both bounded and diverging mass on the retained labels.

### Uniform control between fixed and logarithmic clocks

For a native length-\(j\) history write \(M_j=3^{B_j}/2^j\). Its affine formula gives
\[
 M_jx\le T^jx\le M_jx+(3/2)^j-1.
\]
This upper bound follows by iterating the all-odd upper affine map on the intercept. At any exit of time \(j\le K\), it gives \(M_j\ge X/(2x)\) for large \(X\), since \((3/2)^K=o(X)\) when \(c<c_0\).

Partition the sources into dyadic shells \([D,2D)\), \(D=2^m\). For an upper bound extend the last partial shell to its full length only *after* imposing the necessary slope inequality \(M_j\ge X/(4D)\). The shell has one source in each residue modulo \(2^m\), and its first \(m\) physical parity bits run over all binary words exactly once. For example, translating the source by \(2^h\) preserves its first \(h\) bits and changes the state at time \(h\) by the odd integer \(3^{B_h}\). The next parity flips. Induction proves the binary-word bijection. The harmonic charge of an event in this shell is at most its cardinality divided by \(D\).

Choose \(0<t<1\) and write
\[
 \lambda(t)=\frac{1+3^t}{2^{1+t}}<1,\quad
 \alpha=\log_2(3/2),\quad b_t=t(1-\alpha)+\log_2\lambda(t).
\]
Strict convexity of \(\lambda(t)=\tfrac12((1/2)^t+(3/2)^t)\), with endpoint values 1, gives its strict inequality. For \(J\le j\le\min(K,m)\), the exact mean of \(M_j^t\) is \(\lambda(t)^j\). Markov's inequality and a union bound show that the harmonic charge on this shell at those times is at most \(C_t(D/X)^t\lambda(t)^J\). Its sum over shells is \(O_t(\lambda(t)^J)\).

If \(m<j\le K\), all continuations satisfy \(M_j\le M_m(3/2)^{K-m}\). Only the first \(m\) bits are sampled. The resulting shell charge is at most
\[
 (4D/X)^t \lambda(t)^m(3/2)^{t(K-m)}
 \le 4^t X^{-t(1-c\alpha)}D^{b_t}.
\]
As \(t\downarrow0\), \(b_t/t\to 1-\alpha+(\tfrac12\log_2 3-1)>0\). With small fixed \(t\) the sum over \(D\le X\) is therefore
\[
 O_t\big(X^{t\alpha(c-1)+\log_2\lambda(t)}\big)=O_c(X^{-\eta_c}).
\]
The limiting ratio of this exponent to \(t\) is \(\alpha(c-1)+\tfrac12\log_2 3-1<0\). For \(c=1\) one may simply take \(t=1/2\). Combining the two bounds gives
\[
 \sum_{x<X,\ J\le\tau_X(x)\le K}w/x
       \ll_c \lambda(t)^J+X^{-\eta_c}.\tag{4}
\]
In particular there is no accumulating last-period error at depth \(K\).

### The limit at fixed clock and its ladder law

At fixed \(J\), split into the \(2^J\) genuine source classes. In each the real normalized heights converge uniformly to \(u\exp(S_j)\) for \(j\le J\), with \(u=x/X\). An exiting source has \(u\gg_J1\). For this fixed number of steps the odd-departure factor tends uniformly to 1 there, since its states are at least \(x/2^J\). The finitely many inequalities deciding a first passage have only finitely many boundary points in \(u\). Riemann summation on each class gives the fair-word expectation of the measure obtained from \(du/u\) on \((0,1)\) by its first multiplicative upcrossing, retaining just upcrossings through clock \(J\). Equation (4) justifies the subsequent limit \(J\to\infty\).

Writing \(u=e^{-r}\) turns the source intensity into \(dr\) on positive initial log gaps. For a realized random walk, each strict ladder increment \(h\) covers the adjacent gaps between its old and new records. Their overshoot is uniform Lebesgue measure on \([0,h]\). Independent increments restart the same defective law after each strict record. Its success mass is strictly below one. Indeed after a first even letter the walk is at \(-\log2\), and the positive martingale \(\exp S_j\) has probability at most \(1/2\) of climbing the remaining distance, by stopping at the threshold and then letting a finite horizon increase. Thus \(p\le3/4\). Summing the expected level-crossing measures over the successive records now gives (1). A first odd letter already has probability \(1/2\) and contributes an increment of size \(a\).

Finally any gate has at most \(2^j\) incoming physical words of length \(j\), and a fixed word and gate determine at most one ordinary source. For \(j\le J\) these sources have \(1/x=O_J(1/X)\). Any \(o(X)\) labels consequently collect \(o_J(1)\) charge from the fixed clocks. Apply (4) to the remaining clocks, send \(X\to\infty\) and then \(J\to\infty\). All paths of greater clock are already in \(E_X\). This proves (3).

## The unresolved charge

Under the distinct-path and ordinary first-passage inputs of [PR200's harmonic gate theorem](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/unconventional-20261126/trace/CRITICAL_EXIT_GATES.md), a fixed escaping component has a positive normalized gate charge. Every such charge is concentrated on the thin labels in (3), and its short histories have individually vanishing normalized mass. A proof of vanishing would still need a sequence on which the unnormalized mass of the retained labels is \(o(\log X)\). Counting the labels alone supplies no bound on the harmonic weight routed to each. The full proof of (1)–(4) is written mathematics. The companion Lean module checks its underlying finite ordinary affine bounds and dyadic moment identities.
