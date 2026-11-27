# A point-mass bound for actual Collatz clocks

Write \(T(n)=n/2\) on even inputs and \(T(n)=(3n+1)/2\) on odd inputs. Partition the positive integers into connected components of this directed graph. Delete the outgoing edge of the minimum on each ordinary cycle. The remaining edges in each component form a tree. Choose any integer-valued function \(s\) on each tree satisfying \(s(Tn)=s(n)+1\) on every retained edge. Such a function exists by integration along the unique finite undirected path from an arbitrary base vertex. Different choices add a constant on each component. In the component of one, choose \(s(1)=0\). Then \(-s(n)\) is the genuine first hitting time of one.

Let \(N_X(C,k)\) count the positive integers through \(X\) in component \(C\) with \(s(n)=k\). The following bound holds for arbitrary choices of all the component origins:
\[
                  \sum_C \max_{k\in\mathbb Z} N_X(C,k)
                    \ll X/\sqrt{\log(2X)}.                         \tag{1}
\]
In particular, a prescribed set of at most \(w\) clock values **per component**, selected even after seeing the data, captures at most \(O(w X/\sqrt{\log(2X)})\) starts. A single clock band of width \(o(\sqrt{\log X})\) captures a vanishing fraction of all starts. Every set of \(\delta X\) starts in one component occupies at least \(c\delta\sqrt{\log(2X)}\) distinct clocks.

**Status.** Written deduction from the counted adjacent coalescence estimate (2). The cited primary repository gives a self-contained argument for that input. This note does not kernel-check the probabilistic estimate. All other steps of (1), including the uniform control of every cycle cut, are detailed below. No positive density of any specified component and no Collatz conjecture enter.

## 1. The synchronization input

For \(h\ge1\), the starts \(x\) modulo \(2^h\) whose paths from \(x,x+1\) fail to have both equal endpoints and equal numbers of odd inputs at some common clock \(j\le h\) number at most
\[
                                C2^h/\sqrt h.                       \tag{2}
\]
Only endpoint equality at a common clock is needed for (1). The two-count version also gives the [joint residue theorem](CLOCK_PHASES.md). Classical parity coding makes the stronger sufficient test in (2) depend only on the low \(h\) digits: two equal-slope affine forms meeting on one lift agree on the cylinder. Periodic covering of the first \(D X\) integers therefore bounds failed starts by \(O_D(X/\sqrt h)\) whenever \(2^h\le X\). The same absolute count bounds any subset of those starts.

Said Duran established the density-one statement. David Leen obtained the square-root tail. The canonical six-transition chain, its unbiased jump excursions, holding-time estimate, contracting boundary return, and finite absorbing words are written out at the frozen repository proof below. Set \((s,D)=(0,1)\) in its final bound to obtain (2). These are previously established inputs. Direct links to the original deposits and their pinned repository derivation follow. [Said Duran](https://doi.org/10.5281/zenodo.23003524) · [Leen, *Exact rates in Collatz synchronization*](https://doi.org/10.5281/zenodo.23268751) · [PR146 proof, frozen f4310782](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md) · [Counted arm and cylinder formulation](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md)

## 2. One error estimate works at every ordinary cycle cut

A cycle minimum \(r\) is odd, since an even minimum would map below itself. After reaching \(r\) the orbit stays at least \(r\). Fix \(D\ge1\), let \(J=\lfloor(\log_2 X)/64\rfloor\), and let \(H=\lfloor(\log_2 X)/2\rfloor\). Apart from \(O_D(X^{1-\delta})\) starts \(1\le x\le D X\), for an absolute \(\delta>0\), the prefix through \(J\) avoids every cut.

Indeed discard \(x\le X^{0.99}\). Every \(T^j x\) for \(j\le J\) is at least \(x/2^J>X^{0.97}\). A visit to any cut in this prefix would imply \(T^H x>X^{0.97}\). In a full period of \(2^H\) starts, the number \(P\) of odd inputs before clock \(H\) has the exact binomial law with parameters \(H,1/2\). Each parity word occupies one binary residue, by the odd slope in the affine cylinder. The Chernoff bound for \(P>0.55H\) and covering \([1,DX]\) by whole periods show that this occurs on \(O_D(Xe^{-cH})\) starts. On the complement the affine formula and a geometric bound on its additive remainder give
\[
 T^H x \le 2^{-H} 3^{0.55H}x+(3/2)^H < X^{0.95}
\]
for all sufficiently large \(X\). Here \((1-0.55\log_2 3)/2>0.064\). This proves the simultaneous assertion. The constants can absorb small \(X\). In particular there is no dependence on the number of cycles, their heights, or the chosen integer origins.

Let \(v(n)=\delta_{(C(n),s(n))}\), a point mass on the countable set of pairs \((C,k)\). Combining the cut estimate with (2) at \(h=J\) gives
\[
           \#\{n\le D X:v(n+1)\ne v(n)\}\ll_D X/\sqrt{\log(2X)}. \tag{3}
\]
If the two arms meet before either reaches a cut, subtracting the same elapsed time gives the equality. A cut lying on the outgoing edge after the meeting is immaterial. The estimate also bounds failures along any of the fixed arithmetic subsequences used below by enlarging \(D\).

## 3. A single positive measure dominates all nearby transport errors

Let \(S\) shift clock by \(-1\), keeping the component unchanged, so \((S\mu)(C,k)=\mu(C,k+1)\). For \(t>0\) put \(f(t)=v(\lceil t\rceil)\) and \(\mu_Y=Y^{-1}\int_0^Y f(t)\,dt\). For integer \(X\), \(X\mu_X(C,k)=N_X(C,k)\) exactly. All integrals at a bounded cutoff are finite sums of point masses with real coefficients.

For any positive \(X\) define the following **one fixed positive measure** on clock pairs. Absolute value is taken coordinatewise on signed measures:
\[
 \nu_X= X^{-1}\int_0^{3X}
   \bigl(|f(2t)-S f(t)|+|f(3t)-f(t)|\bigr)\,dt.                  \tag{4}
\]
We have \(\|\nu_X\|_1\ll 1/\sqrt{\log(2X)}\). To check every rounding alternative, put \(n=\lceil t\rceil\). Then \(\lceil 2t\rceil\) equals \(2n-1\) or \(2n\). The even edge gives \(v(2n)=S v(n)\) exactly. Except at the failures of (3), \(v(2n-1)=v(2n)\). Also \(\lceil 3t\rceil\) is one of \(3n-2,3n-1,3n\). The three labels coincide outside two instances of (3). The middle number is \(T(2n-1)\), hence
\[
                   v(3n-1)=S^{-1}v(2n-1)=v(n)
\]
unless the odd edge is cut or the previous pair failed. That edge exception is included in Section 2. All indexed starts here are at most \(10X+O(1)\). Each failure costs at most two in \(\ell^1\) per rounding comparison on a unit interval.

For **every real** \(Y\in[X,3X]\), changing variables in the integral gives the following coordinatewise inequalities:
\[
 \begin{aligned}
 |\mu_{2Y}-S\mu_Y|&\le X^{-1}\int_0^{3X}|f(2t)-S f(t)|\,dt,\\
 |\mu_{3Y}-\mu_Y|&\le X^{-1}\int_0^{3X}|f(3t)-f(t)|\,dt .
 \end{aligned}                                                     \tag{5}
\]
The normalization \(Y^{-1}\le X^{-1}\) and the common integration domain are essential. Individual scalar norm estimates would not give the translated summation used next.

## 4. Transport at bounded scales and a finite-support endpoint

Set \(b_j=\lfloor j\log 2/\log 3\rfloor\), \(c_j=2^j/3^{b_j}\), and \(\lambda_j=\mu_{c_jX}\). Then \(1\le c_j<3\), \(c_0=1\), and each step takes \(c_{j-1}\) to its double, optionally divided by three. If there is no division, the first line of (5) controls the error. Otherwise set \(Y=c_{j-1}X\), \(Z=c_jX=2Y/3\); both bases \(Y,Z\) belong to \([X,3X]\). Since \(3Z=2Y\),
\[
  |\lambda_j-S\lambda_{j-1}|
     \le |\mu_Z-\mu_{3Z}|+|\mu_{2Y}-S\mu_Y|\le \nu_X.           \tag{6}
\]
In particular the divided leg introduces **no time shift**. In both cases the very same measure (4) dominates the error coordinate by coordinate.

Evaluate (6) at \((C,k-j)\) and sum for \(1\le j\le m\):
\[
  \mu_X(C,k) \le \lambda_m(C,k-m)
                     +\sum_{j=1}^m \nu_X(C,k-j).                  \tag{7}
\]
Every \(\lambda_m\) has support among the labels of the finitely many integers through \(\lceil3X\rceil\). Thus the first term vanishes for all sufficiently large \(m\), for each fixed \(C,k,X\). The remaining atoms are distinct, giving
\[
                     \mu_X(C,k)\le \nu_X(C\times\mathbb Z).
\]
Taking the supremum **before** summing over components yields (1). Real \(X\) differs from its floor by at most one source in the unnormalized counting statement.

## 5. Entropy, physical hitting times, and scope

For uniform \(1\le n\le X\), write \(p_C=\Pr(C(n)=C)\) and \(p_{C,k}=\Pr(C(n)=C,s(n)=k)\). The conditional probability that two draws from within the same component have the same clock, averaged by \(p_C\), satisfies
\[
 \sum_{C:p_C>0}\sum_k p_{C,k}^2/p_C
       \le\sum_C\max_k p_{C,k}\ll(\log(2X))^{-1/2}.
\]
Consequently the conditional Shannon entropy in natural units is
\[
                        H(s(n)\mid C(n))\ge\tfrac12\log\log(2X)-O(1).
\]
Indeed Shannon entropy dominates collision entropy in each row and Jensen's inequality applies to \(-\log\). In the known component of one, (1) bounds the count of any single genuine first hitting time, irrespective of its magnitude or dependence on \(X\). Arbitrary relative clocks in an escaping component obey the same bound.

The estimate uses the ambient \(X\) as denominator. A family already known to have only \(X/\log X\) members may all occupy one clock without violating (1). In particular the sparse source set in the [BGNS implication](../CLOCK_SPECTRUM.md) need not disperse. Nothing here excludes a surviving component or proves universal ordinary descent.

The prefix normalization also matters geometrically. Formal [common-target blocks](../phase2/BasinBlocks.lean) produce arbitrarily long consecutive runs with one exact first-hit time to one: synchronize all arms to the ordinary vertex 85 at a common clock, then follow the certified path from 85 to one. No arm could have reached one earlier, since its subsequent periodic orbit omits 85. Consequently (1) cannot be made uniform over intervals of length \(X\) at arbitrary starting locations with the same right side. The finite-scale argument uses the shared nearby prefix \([1,3X]\) explicitly.

Recent unrefereed work claims substantially sharper local histogram laws for first hits of orbit minima. Within the basin of one this includes the same physical clock. The shared-measure derivation here uses the adjacent synchronization estimate alone and works with all componentwise signed clocks simultaneously. No priority claim is made for the scalar basin-one bound. [Leen, *Brownian motion in Collatz orbits*](https://doi.org/10.5281/zenodo.23252395) · [Leen's synthesis](https://doi.org/10.5281/zenodo.23652463) · [Terminal-law paper with dependency statement and local-profile comparisons](https://rstation.ai/problems/collatz/papers/175/v1)
