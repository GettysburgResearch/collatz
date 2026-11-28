# Every rational denominator rate occurs, even at common clocks

For positive rational shortcut cycles let \(L\) be the least native period, \(p\) its odd grade, and \(q\) the full reduced denominator. Let \(\mathcal S_p\) be the limits of \(\log_2 q/L\) along such cycles at fixed \(p\) as \(L\to\infty\).

**Inverse theorem.** Given any nonempty finite set \(E\subseteq\mathbb Q\cap(0,1]\), there are integers \(g,r_0\ge1\) such that for **every** \(r\ge r_0\) and all sufficiently large \(n\), every \(\lambda\in E\) is represented by a primitive positive rational cycle with the **same** prescribed clocks \(p=gr, L=gn\) and
\[
                       \log_2 q_{\lambda,n}=\lambda L+O_{g,r}(1).      \tag{1}
\]
The cycles for different rates may have different parity words and denominators. In particular
\[
                         \bigcup_{p\ge1}\mathcal S_p
                                      =\mathbb Q\cap(0,1].              \tag{2}
\]
Fixed-grade necessity, including positivity and rational quantization, comes from the [PR212 moving-arc theorem](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/MOVING_ARCS.md) or the [fixed-grade denominator reductions](../ordinary/PRIME_GRADE_DENOMINATORS.md). The constructive assertion here supplies the opposite inclusion, the synchronized clocks, and occurrence at every sufficiently large multiple of a common grade divisor.

A varying-grade consequence is that for every real \(0\le\theta\le1\) and every function \(f(L)\to\infty\), there are primitive positive rational cycles with \(p\to\infty\), \(p\le f(L)\), \(L/p\to\infty\), and \(\log_2 q/L\to\theta\). Choose positive rational targets tending to \(\theta\), then increasing grades afforded by (1), and then periods sufficiently large for each target and grade. This puts no convergence assertion on any fixed positive ordinary integer source.

## An integer Fourier profile can be implemented by genuine parity words

Let \(g\ge2\) and choose a set \(S\) of divisors of \(g\) containing both one and \(g\). Put \(k=\sum_{d\in S}\varphi(d)\). We construct the rate \(k/g\). For \(i\in\mathbb Z/g\mathbb Z\) set
\[
 F_i=\sum_{d\in S,\ d>1}c_d(i),\qquad
 c_d(i)=\sum_{\substack{0\le j<d\\\gcd(j,d)=1}}\exp(2\pi\mathrm{i}ji/d).
\]
These are integers, since Möbius inversion gives \(c_d(i)=\sum_{e\mid\gcd(d,i)} e\,\mu(d/e)\). They have absolute value at most \(g\). By orthogonality of the characters of the cyclic group, the discrete Fourier transform of \((F_i)\) is exactly \(g\) at the characters whose orders lie in \(S\setminus\{1\}\), and zero elsewhere. This also works with the opposite sign convention for the transform, since the retained orders are invariant under inversion.

We require words at one common length and odd grade whose integer affine carries contain a whole arithmetic progression of \(2g+1\) distinct values. Here the input is a **proved** finitary Collatz theorem, not a distribution assumption. The theorem \(\texttt{Collatz.BlockClock.cover}\) at [pinned PR212, commit 505d3fe782922904e86477990cc5d41e9110edda](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/merger/BlockClock.lean), specialized by [SharpMotifInput.lean](SharpMotifInput.lean), gives a positive \(t\), length \(b\), grade \(r_0\), and \(2^b>3^{r_0}\), such that all inputs \(t,t+1,\ldots,t+2g\) reach one at that exact native clock and grade. The [fresh Lean 4.34.1 receipt](ROUTER_FRESH_LEAN.json) rebuilds the eight pinned router modules, the local specialization, and an isolated audit of the two stated roots. Both roots depend exactly on \(\texttt{propext}\), \(\texttt{Classical.choice}\), and \(\texttt{Quot.sound}\). Only the common-clock motif input is formally checked there. The Fourier and inverse results here are written arguments.

The carry on starting input \(t+j\) is \(2^b-3^{r_0}(t+j)\). All are positive since \(r_0>0\) (distinct starts cannot all reach one with zero grade). Reverse the ordering to obtain an increasing progression of carries. Appending one common odd letter at the common end of the *words* multiplies every carry by three and adds the same power of two. Hence for every specified \(r\ge r_0\) one has equal-length, grade-\(r\) words \(w_m\), \(-g\le m\le g\), with carries \(C+t' m\) for positive integers \(C,t'\). Appending letters constructs new parity words; their subsequent periodic realizations are supplied by the usual word-fixed-point identity.

At native position \(in\) place \(w_{F_i}\), for \(0\le i<g\); fill the remaining length \(gn\) with even letters. For \(n\) large the groups are disjoint. With \(X=2^n\), the full carry and raw denominator are
\[
 B(X)=\sum_{i=0}^{g-1}3^{r(g-1-i)}(C+t'F_i)X^i,\qquad
 D(X)=X^g-3^{rg}.
\]
At \(X=3^r\zeta\), \(\zeta^g=1\), the value \(3^{-r(g-1)}B(X)\) is the Fourier sum of \((C+t'F_i)\). At the trivial character it is \(gC>0\); at each retained nontrivial character it is \(gt'\); at all others it vanishes. Thus exactly \(k\) roots of the squarefree \(D\) survive. The monic factors and the quotient of \(B\) by the monic polynomial gcd are integral. After this cancellation, the numerical gcd divides a fixed nonzero polynomial resultant. The surviving denominator polynomial has absolute value \(2^{kn+O_{g,r}(1)}\). This proves (1) for this \(S\) and for the **actual** reduced denominator.

For large \(n\), exactly \(g\) cyclic gaps grow with \(n\), one between each pair of adjacent nonempty groups, while all within-group gaps stay bounded. A repetition factor \(e>1\) of the parity word would divide \(g\), so its spatial shift by \((g/e)n\) carries nominal group windows exactly onto corresponding nominal group windows. It would preserve the indexed word sequence and hence its carries. A cyclic vector with a nontrivial shift period has zero Fourier coefficients at primitive \(g\)-th roots, contradicting \(g\in S\). The primitive parity word realizes a positive rational cycle of that same least period by the unique word fixed point, since \(2^{gn}>3^{gr}\) eventually. The initial denominator is odd and prime to three and remains the complete denominator around the cycle.

## Attaining every required numerator at a common denominator

Let \(N>1\) be odd, \(a\ge1\), \(2^a\ge\varphi(N)\), and \(g=2^aN\). With orders one and \(g\) required, the values of \(\sum_{d\in S}\varphi(d)\) include **every integer**
\[
                             1+\varphi(g)\le k\le g .                 \tag{3}
\]
First take the mandatory one and arbitrary other pure two-power divisors of \(g\). Their weights \(1,1,2,4,\ldots,2^{a-1}\), with the first one mandatory, give all integers from one to \(2^a\). For each odd divisor \(e>1\) of \(N\), the new divisors \(e2^j\), \(0\le j\le a\), have weights \(\varphi(e)\) times \(1,1,2,4,\ldots,2^{a-1}\). Their subset sums realize all the corresponding multiples of \(\varphi(e)\) between zero and the sum of these weights. For \(e=N\), reserve the last divisor \(g\) as mandatory and use only \(0\le j<a\) in this step, with the same assertion for the shorter list. Each progression can be added without opening integer holes in the existing interval, since its step \(\varphi(e)\le\varphi(N)\le2^a\) is at most the number of consecutive integers already present. Before adding \(g\) the resulting interval is \([1,g-\varphi(g)]\), by \(\sum_{d\mid g}\varphi(d)=g\). The mandatory final weight proves (3).

To serve the prescribed finite \(E\), choose \(N\) divisible by the odd parts of all its reduced denominators and by sufficiently many odd primes that \(\varphi(2N)/(2N)<\min E\). Such a choice exists because the product of \((1-1/\ell)\) over primes tends to zero, as follows from Euler's product and divergence of the harmonic series. Increase \(a\) so that \(2^a\ge\varphi(N)\) and every reduced denominator divides \(g=2^aN\). Then \(k=\lambda g\) is an integer strictly larger than \(\varphi(g)\) for every \(\lambda\in E\). Use (3) to choose one support \(S\) per target. The same common-clock motif family and the same \(r,n\) work for all of them, proving the theorem. Given the finite targets, the choices can be found by integer search and enumerating the common-clock trajectories promised by the pinned theorem; no running-time bound is asserted.
