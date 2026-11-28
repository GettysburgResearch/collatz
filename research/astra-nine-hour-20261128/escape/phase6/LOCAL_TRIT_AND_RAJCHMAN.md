# High-frequency cancellation in the ordinary terminal correction

For real \(\tau\) set \(u_0=2^{-i\tau},u_1=(3/2)^{i\tau}\). For any bounded genuine eigenfunction \(f(Tn)=u_{n\bmod2}f(n)\), \(|f|\le1\), let \(c(f)\) be the ordinary source mean of \(n^{-i\tau}f(n)\). Then for every \(\epsilon>0\),
\[
            \sup_f|c(f)|\ll_\epsilon(1+\log(2+|\tau|))^{-1/2+\epsilon}.
                                                                        \tag{1}
\]
The same bound holds for functions where the branch equations are imposed only at \(n>m\), uniformly when \(m\le |\tau|^\theta\) for any fixed \(0\le\theta<1\), allowing a constant depending on \(\theta\). For a single defective edge the bound is uniform in its location, which can exceed the source scale. Existence of the ordinary mean in these settings is proved below. For a fixed positive-mass first-minimum cell, its natural terminal log-correction law is consequently **Rajchman**: its Fourier transform tends to zero. This includes the minimum-one law, which Weaver already proved singular continuous and exact-dimensional of dimension one. The two original-source inputs are the signed marked trit estimate and the growing-block counted-fusion theorem. [Marked trit and the exact source recursion](../phase2/NATIVE_BINOMIAL_TRANSFER.md) · [Weaver, Paper 124, Theorem 1](https://rstation.ai/problems/collatz/papers/124/v1) · [Weaver, Paper 175, Theorem 1](https://rstation.ai/problems/collatz/papers/175)

## Relative signed trit in an arbitrarily translated interval

Let \(I\subset[X,2X]\) have length \(H\ge2\). Write \(F_t\) for the true shortcut odd count. For every mean-zero ternary periodic \(\psi\), \(|\psi|\le1\),
\[
 \left\|H^{-1}\sum_{n\in I}\psi(n)\delta_{(F_t(n),T^t n)}\right\|_1
   \ll_A (1+\log H)^{-A}+(1+t)^{-A}
                                                                        \tag{2}
\]
for \(t\ge1\), uniformly in the location. Half-open intervals avoid ambiguity at a common endpoint. Here is the required change to the [physical-source proof](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/PHYSICAL_SOURCE.md). At odd starts choose \(k=\lfloor\min(\log_2 H,t)/64\rfloor\). At total \(h\le4k\), the old and transported interval cutoffs differ at only \(O(2^{4k})\) sources over all clocks. Their reciprocal weights cost \(O(2^{4k}/X)\). The large-total event has reciprocal mass \(O((H/X)e^{-c k}+2^{4k}/X)\) by counting the complete binary periods *in this interval*. In the remaining output window of length \(3^k2^{-h}H\), a residue modulo \(3^{k+1}\) has at most \(1+H/(3\cdot2^h)\) representatives. The coefficient prefactor is \(O(2^h/X)\). Thus the signed mixing error summed in \((h,y)\) costs \(O_A((H/X)k^{-A})\) by the same one-extra-trit theorem. The original source product differs from one by \(O(k2^{4k}/X)\) on the retained paths. Push the genuine marked pair forward as in (3) of the [native transfer note](../phase2/NATIVE_BINOMIAL_TRANSFER.md).

Partial summation removing the reciprocal weight needs all prefixes of \(I\) at the same \(k\). The calculation for such a prefix of length \(J\le H\) gives \(O_A((J/X) k^{-A}+2^{4k}/X)\), since the residue count is \(1+J/(3\cdot2^h)\); positive and negative endpoint errors were bounded before summing over words. Multiplication by \(O(X)\) gives (2) for odd inputs. For all inputs separate \(n=2^e z\), \(z\) odd. Discard \(e>\min((\log_2 H)/4,t/2)\) at normalized cost \(O(H^{-1/4}+2^{-t/2}+H^{-1})\) using one divisibility class. The remaining odd intervals have length \(H/2^e\ge H^{3/4}\), remaining time at least \(t/2\), and mean-zero trit \(\psi(2^e z)\). Sum with their geometric normalization. Bounded parameter ranges are immediate by the unsigned count.

## The source scale where both estimates apply

Put \(z=2+|\tau|\) and \(a=\log2,b=\log(3/2)\). For \(U(x)=e^{-x}\sum_{n\le e^x} n^{-i\tau}f(n)\) use the physical residual \(r=U-\tfrac12(U(\cdot-a)+U(\cdot+b))\). At all \(x\ge\log z+2\),
\[
                  |r(x)|\ll_{A,\theta}(1+x-\log z)^{-A}.              \tag{3}
\]
Indeed formula (8) in [the amplitude proof](../phase5/NATIVE_MELLIN_RIGIDITY.md) still holds with an additional \(O(m/e^x)\) from exceptional original edges. Let \(Y=e^x\). Dropping \(y<\sqrt{Yz}\) in its signed sum costs \(O(\sqrt{z/Y})\). On the retained ranges the physical odd phase differs from one by \(O(|\tau|/y)\). In each octave \([Z,2Z]\) above that cutoff, partition the summation interval into pieces of length \(H\asymp\sqrt{Z/z}\), charging any final incomplete piece of length at most \(H\) by its unsigned mass. The change of \(y^{-i\tau}\) on one piece is \(O((Z/z)^{-1/2})\). Apply (2) to \(f(y)\) with \(t=\lfloor c_\theta\log H\rfloor\) and \(c_\theta>0\) sufficiently small. All states through this date from such \(y\) exceed \(m\), since they are at least \(Z2^{-t}\), with \(Z\ge z\) and \(m\le z^\theta\). Hence \(f(y)\) is exactly reconstructed from the complete terminal pair and its two branch phases. The interval has normalized signed sum \(O_{A,\theta}((1+\log(Z/z))^{-A})\). The smallest retained \(\log(Z/z)\) is at least \((x-\log z)/2-O(1)\). Summing the physical lengths on the octaves and dividing by \(Y\) proves (3), with the incomplete pieces negligible. For any fixed \(m,\tau\), the residual is integrable, vanishes sufficiently far to the left and is piecewise smooth on bounded intervals. The same signed-increment renewal proof as in the amplitude note gives an ordinary limiting mean, including the finite-defect case.

Fix \(0<\gamma<1/8\), write \(L=\log z\), and stop the negative-drift fair size walk on its first crossing below \(h=L+L^\gamma\). The overshoot lies in \([h-a,h]\). Its accumulated pre-crossing forcing from (3) is \(O_{A,\theta}(L^{-A\gamma})\), by the uniform expected occupation of every unit strip, using a larger residual exponent. Iteration and bounded convergence therefore give, uniformly at every initial scale \(x\ge h\),
\[
        |U(x)|\le \sup_{h-a\le u\le h}|U(u)|
                          +O_{A,\theta}(L^{-A\gamma}).                   \tag{4}
\]
This statement requires no quantitative convergence estimate for a continuous limiting overshoot law.

It remains to estimate the true ordinary sums at \(Y=e^u\in[e^h/2,e^h]\). Ignore the prefix below \(Y/L^B\) at cost \(O(L^{-B})\) with a fixed large \(B\), and set \(D=\lceil e^{2L^\gamma}\rceil\). Replace the remaining sum of \(g(n)=n^{-i\tau}f(n)\) by its mean over sliding blocks \(n,n+1,\ldots,n+D-1\) with starts in the same interval; changing the two endpoints costs \(O(D/Y)\). Use \(t=\lfloor c_\theta\log_2 Y\rfloor\), with \(0<c_\theta<(1-\theta)/2\). Every input through this date starting in these blocks exceeds \(m\) for sufficiently large \(z\). Failure of full counted fusion by date \(t\) depends only on the starting residue modulo \(2^t\): on any cylinder, two equal states with equal counts on one lift give equal affine expressions on every lift, and unequal counts already prevent fusion. W124 Theorem 1 thus bounds the fraction of bad sliding starts, normalized by \(Y\), by
\[
          O_\theta\left(\frac{(1+\log D)^4}{\sqrt{\log Y}}
                             +\frac{2^t}{Y}\right).
\]
On every other block the values of \(f\) are identical, since the terminal states and both branch multiplicities coincide through date \(t\). The elementary first derivative sum estimate for the logarithmic phase gives
\(\big|\sum_{j<D}(n+j)^{-i\tau}\big|\ll Y/|\tau|\). Indeed \(|\tau|/v\) is monotone on the block, bounded below by a constant times \(|\tau|/Y\) and above by \(O(L^B e^{-L^\gamma})<1\); summing differences with the reciprocal of \(1-e^{-i\tau\log(1+1/v)}\) gives the bound by summation by parts. After normalization by \(D\), the result is \(O(e^{-L^\gamma})\). Accordingly (4) is \(O_{\gamma,\theta}(L^{-1/2+4\gamma})\). Choose \(4\gamma<\epsilon\) and then \(A\) sufficiently large to prove (1).

## One defective edge at an arbitrary height

If the branch equation fails at just one site \(y_0\), the residual from the first exact step still has magnitude at most \(2/Y\) there. In the proof of (3), the terminal test can misrepresent \(f(n)\) only if the first \(t\) sites include \(y_0\). A prescribed length-\(i\) parity word has an affine output of positive slope, so determines at most one integer source ending at \(y_0\). Summing over \(i<t\) leaves fewer than \(2^t\) exceptional integers on the entire line. In each local source interval of length \(H\), choose \(t=\lfloor(\log_2 H)/4\rfloor\); after division by \(H\) the exceptional cost is \(O(H^{-3/4})\), uniformly in \(y_0\). For the sliding blocks at \(Y\), at most \(D2^t\) starts touch one of these exceptional inputs before the counted-fusion date \(t=\lfloor(\log_2 Y)/4\rfloor\). Their normalized cost tends to zero faster than any inverse logarithm. This proves the version uniform in the location of one defective edge.

## Which measures this controls

On the cell with first orbit minimum \(r\), let \(B_r(n)\) be the sum of the natural logarithms \(\log(1+1/(3v))\) at odd inputs strictly before that first minimum. Put \(f(n)=n^{i\tau}\exp(i\tau B_r(n))\) on this cell and zero elsewhere. At \(n>r\) the future minimum label is unchanged by the first step, and the correction cocycle gives exactly the required branch phase; if \(Tn<r\) then both values vanish. The result applies with \(m=r\). The frequency scaling by \(\log2\) gives the stated conclusion for Weaver's base-two coordinate. The same proof applies to the first visit to any fixed target, using zero off its basin and allowing a single defective edge at the target; the unnormalized Fourier bound is uniform over all target heights. Fixed nonzero cell masses can be normalized after the estimate. For a genuine escaping component use \(f(n)=P(n)^{i\tau}\) on that component and zero elsewhere. This gives (1) for its complete future log correction without a boundary exception. In fact the sum of absolute Fourier amplitudes across all escaping components has the same bound, by multiplying each component by any complex unit before the uniform estimate.

The estimate concerns frequencies tending to infinity. It does not force cancellation at \(2\pi/\log3\), where a putative escaping component has a positive lower bound proportional to its density.
