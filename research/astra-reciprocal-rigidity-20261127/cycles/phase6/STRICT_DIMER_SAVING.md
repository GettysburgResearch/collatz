# A strict power saving below the dimer critical entropy for ordinary forward survivors

Let \(S_D\) consist of all positive odd integers whose entire forward Syracuse trajectory avoids \(5,7\bmod8\). With \(h_D=0.3208518\ldots\) as in [the elementary interval bound](../phase5/INTERVAL_COUNTS.md), there are **fixed** \(\gamma>0\), \(K<\infty\) such that every real interval \(I\) of length \(X\ge1\) satisfies
\[
                        \#(I\cap S_D)\le K X^{h_D-\gamma}.             \tag{1}
\]
The constants are ineffective because the proof uses the fixed-place Subspace Theorem. The controlled quantity is the number of actual integer starts. It includes all purely periodic and all one-sided nonperiodic dimer survivors.

We prove (1) by watching a slightly longer physical word than the dyadic width of the source interval. At near-critical composition, the small allowed arc for the canonical residue gives a strict gain. The argument transfers the original-source counting idea of Weaver 28 and 73 from the unrestricted geometric model to the positively constrained dimer shift. The dimer input is [canonical arc concentration](CANONICAL_ARCS.md). [Weaver 28, Theorem A](https://rstation.ai/problems/collatz/papers/28), [Weaver 73, §5](https://rstation.ai/problems/collatz/papers/73)

### High odd counts at a longer physical horizon

Use \(p_*=\log_32\), \(\beta_*=(2p_*-1)/(1-p_*)\), \(\alpha=\log_23\). Given \(I=[a,a+2^k)\), choose \(P=\lfloor e k\rfloor,\ T=k+P\), for a positive constant \(e\) to be fixed small. Read \(T\) physical departure bits of each odd source. The no-\(00\), no-\(111\) words starting in 1 have unique representation as \(M\) complete blocks \(10,110\), followed by \(1^s\), \(s\in\{0,1,2\}\). For a fixed total odd count \(q\),
\[
       M=T-q,\qquad j=T-2M-s,\qquad \ell=T-s ,
\]
where \(j\) is the number of second blocks and \(\ell\) the length of the complete prefix. For large \(k\), \(M\) is comparable to \(k\), since \(q/T\le2/3+O(1/T)\) and \(q/T\ge1/2-O(1/T)\). The strings in each slice number \(\binom Mj\). For \(s\le2\), each complete-block word can provide at most one source in \(I\), because \(2^\ell\ge2^k\). To do so its canonical residue divided by \(2^\ell\) must lie on the image of \(I/2^\ell\) in the circle, an arc of length \(2^{-(P-s)}\).

Fix \(d\in(h_D,1)\), and let \(\tau,c_2\) come from [CANONICAL_ARCS.md](CANONICAL_ARCS.md). Choose a positive constant \(e\) small enough that \(P-s\) fits in \([c_1M,c_2M]\) for some fixed \(c_1>0\) at every possible high-count slice. It can be decreased below in terms of \(\tau\).

The entropy function \(f(\beta)=H_2(\beta)/(2+\beta)\) has strictly negative derivative for \(\beta\ge\beta_*-\xi\) for some \(\xi>0\). This follows from \(\beta_*>1/2\), \(H_2'(\beta)<0\) beyond \(1/2\), and the positive denominator. In particular \(f(\beta_*)=h_D\). For a valid slice,
\[
         \log_2\binom Mj\le M H_2(j/M)=(T-s) f(j/M).
\]
Classify a word as high when \(q\ge p_*T-\eta k\), where \(\eta>0\) will be chosen much smaller than \(e\). Then \(\beta=j/M\ge\beta_*-O(\eta)-O(1/k)\), uniformly, using \(M=T-q\). Take \(\eta\) small enough that \(\beta\ge\beta_*-\min(\tau,\xi)\) eventually. All high slices satisfy \(f(\beta)\le h_D+C\eta+O(1/k)\) with \(C\) independent of \(e,\eta\); only the compact near-critical region is needed for the Lipschitz estimate.

If \(\beta>\beta_*+\tau\), compactness and monotonicity give \(f(\beta)\le h_D-c_\tau\) for some \(c_\tau>0\), unless this range is empty. Take \(e\) so small that \((1+e)(h_D-c_\tau)<h_D-c_\tau/2\). The raw word count already gives a strict saving here. For each remaining high slice, arc concentration bounds its integer count by
\[
                     O\bigl(2^{(h_D+C\eta)T-d(P-s)}\bigr).
\]
Select \(\eta\) after \(e\) to satisfy \(C\eta(1+e)<(d-h_D)e/4\) and the preceding smallness conditions. The exponent is at most \(h_D k-(d-h_D)ek/2\) for all large \(k\). Summation over \(O(k)\) possible \(q,s\) and absorption of this polynomial factor give a bound \(O(2^{(h_D-2\gamma)k})\) on the entire high group, for a fixed \(0<2\gamma<h_D\).

### Low odd counts and the same survivor set at the image

For fixed \(q<p_*T-\eta k\), affine expansion places every \(T\)-step shortcut image of \(x\) in a translated interval of length at most
\[
                   3^q\,2^{k-T}+(3/2)^T+1 .
\]
The first term is at most \(2^{(1-\alpha\eta)k}\); the second is \(2^{(1+e)k\log_2(3/2)}\). Choose \(e\) also so small that \((1+e)\log_2(3/2)<1\). Then for large \(k\), rounding those lengths up to powers of two costs at most a scale \(2^{(1-c)k}\) with some fixed \(c>0\).

As proved in [AVOIDER_COUNTS.md](../phase5/AVOIDER_COUNTS.md), a fixed number of physical steps is injective on odd forward dimer survivors. Odd endpoints are still in \(S_D\), and even endpoints halve into \(S_D\). If \(A(k)=\sup_a\#(S_D\cap[a,a+2^k))\), all \(O(k)\) low classes therefore give
\[
                  A(k)\le O\bigl(2^{(h_D-2\gamma)k}\bigr)
                         +O(k)\,A(\lfloor(1-c')k\rfloor)               \tag{2}
\]
for some \(0<c'<c\) after allowing integer rounding. Induction gives \(A(k)\ll 2^{(h_D-\gamma)k}\), as the second term divided by this target decays exponentially at large \(k\). Rounding an arbitrary interval up to the next dyadic width proves (1).

### Cycle consequence and remaining gap

Partial summation now gives \(O(m^{-(1-h_D+\gamma)})\) for the combined reciprocal mass of all surviving odd points above \(m\), and hence for the sum of all logarithmic defects over ordinary dimer cycles with minimum at least \(m\). Combining with the separately sourced \(\mu(\log2/\log3)\le3\) estimate strengthens the minimum and phase-occupation power bounds in [AVOIDER_COUNTS.md](../phase5/AVOIDER_COUNTS.md) by a fixed amount. The exponent in (1) stays positive and the argument permits an isolated orbit. The effective all-period \(2^{-44}\) estimate at the verified floor remains the separate elementary bound.
