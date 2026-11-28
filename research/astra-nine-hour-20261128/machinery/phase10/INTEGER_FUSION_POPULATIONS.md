# Integer counted-fusion populations of a biased odd source

Let \(x\) have the dyadic odd law \(\nu_\theta\), the iid Bernoulli physical parity law of parameter \(\theta\) conditional on starting odd. Its successive forward gaps \(E_1,E_2,\ldots\) are independent positive geometrics. Put \(S_n=\sum_{i=1}^n E_i\), \(H=H(E_1)\), \(b=(H-\log3)_+\). For this path define the finite class size
\[
 K_n(x)=\#\{h\in2\mathbb Z:T^{S_n}(x+h)=T^{S_n}x,
                            \ F_{S_n}(x+h)=n\}.
\]
The endpoint parity is odd on both streams, and since both start odd the companion's \(n\)-th gap is completed at this same physical clock. These sets increase with \(n\), including \(h=0\). Let \(K_\infty=\lim K_n\). This is the size of the source's full counted-fusion class among even ordinary integer translations. Any finite counted fusion persists to the next odd date. On ordinary positive inputs the same finite identities hold, with the additional sign check for any companion under consideration.

**Exact finite identity.** For the reversed gap word \(w=(E_n,\dots,E_1)\), let \(s=S_n\), \(D_w=2^s\beta_w\), and write \(z=D_w2^{-s}\bmod3^n\). Then \(K_n\) counts exactly all words \(v\) of length \(n\), sum \(s\), with \(D_v\equiv D_w\bmod3^n\). Indeed \(h=(D_w-D_v)/3^n\) is an even integer. On the dyadic input \(x+h\), composing the corresponding physical shortcut choices gives the same odd endpoint as the word for \(x\); peeling the exact inverse odd maps of that odd endpoint guarantees each prescribed gap is its actual gap. Conversely fusion specifies just such a word, and the fixed-length, fixed-total numerator determines it uniquely. Every word of the specified shape has probability \(p(w)=\theta^n(1-\theta)^{s-n}\), so for the sampling joint atom \((s,z)\),
\[
                  K_n=\mathbb P(S_n=s,Z_n=z)/p(w).                   \tag{1}
\]
Here \(Z_n\) is the residue of the reversed word's affine offset. For fixed \(s\), all \(\binom{s-1}{n-1}\) compositions are equally likely. In particular
\[
 \mathbb P(K_n\le M\mid S_n=s)\le \frac{3^nM}{\binom{s-1}{n-1}}.       \tag{2}
\]
This also gives exact counts for positive complete binary periods: conditioning positive odd \(x\) in a complete period of length \(2^{s+1}\) on its \(n\)-th gap ending at \(s\) gives exactly this uniform composition law. Since \(0<D_w/3^n<2^s\), all candidate shifts have absolute value below \(2^s\). In any such interval starting above \(2^s\), every counted companion is a positive integer.

**Exponential rate.** For every \(0<\theta<1\),
\[
                    \frac{\log K_n(x)}n\longrightarrow b
                   \qquad\nu_\theta\text{-almost surely}.              \tag{3}
\]
Extend the gap process bilaterally. Let \(Y_j=A_{E_j}(Y_{j-1})\) be its stationary ternary past coordinate. Then \(Y_n\bmod3^n=Z_n\) exactly, independent of the choice of earlier past. Write \(Q_j(e\mid y)\) for the posterior of the latest letter at a \(j\)-trit coordinate and \(\mu_j\) for that coordinate law. Stationarity, independence of the fresh letter, and deterministic affine recovery of the previous \(j-1\) trits give
\[
  -\log\mu_n(Z_n)=\sum_{j=1}^n[-\log p(E_j)+\log Q_j(E_j\mid Y_j)].    \tag{4}
\]
The posterior losses converge pointwise at a fixed bilateral time to the loss given the entire ternary coordinate. Their supremum is integrable. To see the last point, conditional on a fixed latest letter \(e\), the reciprocal likelihood \(p(e)/Q_j(e\mid Y)\) is the ratio of the marginal to the letter-conditional cylinder probabilities, a nonnegative supermartingale of initial value one. Its maximal inequality bounds the probability of a positive log excess \(u\) by \(e^{-u}\). Add \(-\log p(e)\) and average over \(e\). Conditional entropy convergence and the ternary entropy identity give expected limiting loss \(b\). To average the varying depths in (4), first discard the fixed first \(J\) terms, then dominate the rest of the difference from the stationary limiting loss by the ergodic average of the integrable envelope \(\sup_{j\ge J}|\log Q_j-\log Q_\infty|\). Its expectation tends to zero. Birkhoff now gives \(-\log\mu_n(Z_n)/n\to H-b\). [Leen, entropy dimension, Theorem C](https://doi.org/10.5281/zenodo.23268832) · [Conditional entropy identity](../phase7/CRITICAL_AFFINE_OVERLAPS.md)

By the strong law, eventually \(S_n\le Cn\) for a fixed \(C>1/\theta\). Among these possible totals, the probability that the sampled conditional atom \(\mathbb P(S_n=s\mid Z_n)\) is below \(n^{-3}\) is \(O_C(n^{-2})\): sum their small conditional masses at each \(Z_n\). Borel–Cantelli gives \(\log\mathbb P(S_n\mid Z_n)=o(n)\) along almost every path. Combining (4) and (1) with the strong law for \(-\log p(E_j)\) proves (3). Below the entropy threshold, failure of the one-sided rate \(\log K_n\ge(b-\varepsilon)n\) even has exponentially small probability. Restrict first to \(S_n\le Cn\) and word information \(-\log p(w)\ge(H-\varepsilon/2)n\), whose complement has exponentially small probability by the geometric exponential moment. The remaining bad words number at most \(Cn\,3^n e^{(b-\varepsilon)n}\), and each has probability at most \(e^{-(H-\varepsilon/2)n}\).

**The entropy threshold.** At \(\theta=\theta_*\) where \(H=\log3\), the full class is infinite almost surely despite its zero exponential rate. Indeed \(\mathbb P(S_n=s,Z_n=z)\ge3^{-n}n^{-3}\) eventually almost surely by the same counting over all \(s\le Cn\), \(z\bmod3^n\). Thus (1) gives
\[
  \log K_n\ge\sum_{j=1}^n[-\log p(E_j)-\log3]-3\log n
  \quad\text{eventually almost surely}.
\]
The centered increments have finite, strictly positive variance \(\sigma_*^2\). The iid law of the iterated logarithm gives \(\limsup_n\log K_n/\sqrt{2n\log\log n}\ge\sigma_*\). The underlying information fluctuation also drives Weaver's prior critical singularity theorem for the *ternary marginal*; the multiplicity here enumerates exact, synchronously counted integer translates at the original odd binary source. [Weaver 135, §§3–4](https://rstation.ai/problems/collatz/papers/135)

**Beyond the real drift threshold.** If \(\theta>\log2/\log3\), the full class is finite almost surely. The normalized positive affine intercept on the actual forward code is
\[
 R_n^+(x)=D_w/3^n=\sum_{j=1}^n 2^{S_{j-1}}/3^j,\qquad S_0=0.
\]
Its limit \(R^+\) is finite by negative mean log multiplier, and every matched integer \(h\) satisfies \(h\le R_n^+(x)\) by the numerator identity and positivity of \(D_v\). On a conull set closed under all counted-fusion partial translations, every class of integer offsets therefore has a largest member in its usual ordering. The partial translations preserve \(\nu_\theta\) on their domains: aligned equal-count prefixes have equal probabilities and identical fresh tails. This holds also at the fair bias, though only the biased range specified here is used. [Exact binary overlap decomposition](../phase8/BIASED_BINARY_FUSION.md)

For completeness, assume a positive-measure family of infinite classes with such maxima. The set of their maxima is measurable, as are all offset sets, by countability of \(2\mathbb Z\). Map each maximum to the \(j\)-th largest member of its class. For each fixed \(j\ge1\), this injective, countably piecewise integer translation preserves measure. The resulting sets for different \(j\) are disjoint so the maxima have measure zero. Their countably many partial translates cover the hypothesized infinite classes, a contradiction. The same argument allows class averaging on each finite size stratum. In a class of size \(k\), the \(k\) numbers \(R^+\) at its ordered members are respectively at least the numbers of members lying above them. Hence for any \(p>0\),
\[
                  \mathbb E K_\infty^p\le(p+1)\mathbb E(1+R^+)^p.
\]
Here use \(\sum_{i=1}^k i^p\ge k^{p+1}/(p+1)\) on each finite class. A positive moment exists by \(\mathbb E(2^{E_1}/3)^p<1\) for all sufficiently small positive \(p\) and subadditivity for \(p\le1\). In particular for \(\theta>3/4\), \(\mathbb E R^+=(2\theta-1)/(4\theta-3)\), giving a finite expected number of fused integer companions, equivalently summability over even offsets of their exact binary common masses. These arguments leave finitude of the class unresolved for \(\theta_*<\theta\le\log2/\log3\).

## How much fresh ternary information the actual class supplies

Let \(J_n^{(r)}=H(\beta_w\bmod3^{n+r}\mid S_n,\beta_w\bmod3^n)\) for the reversed word above. For every fixed \(r\ge1\) the sequence \(J_n^{(r)}\) is nondecreasing, so its limit exists in \([0,r\log3]\). This assertion concerns the undisclosed higher trits of the *finite prefix itself*. The independent infinite tail is absent.

To prove monotonicity, partition the odd dyadic sources by their finite relation at the \(n\)-th epoch: a class consists of exactly the translated members counted by \(K_n\). Within a class the conditional law is uniform. Indeed each member carries one of the matching finite words of equal geometric probability with precisely the same remaining infinite gap sequence. Independently mark the source by a uniform \(i\in\mathbb Z/3^r\). For each partial translation \(x\mapsto x+h\) in the finite class, include its marked translation \((x,i)\mapsto(x+h,i+h)\). The resulting finite equivalence class still has uniform conditional law. The entropy of the original mark conditional on this marked class is exactly the entropy of the offset residues \(h\bmod3^r\) inside the unmarked class. The numerator formula identifies these, up to a fixed affine permutation on each class, with the upper \(r\) trits of \(\beta_w\) given its lower trits and total. Its expectation is \(J_n^{(r)}\). The marked relations increase with \(n\) and their invariant sigma-fields decrease, so conditional entropy of the mark increases.

Let \(\mathcal I\) be the sigma-field invariant under the entire increasing union of the unmarked classes. Write \(J_\infty^{(1)}=\lim_n J_n^{(1)}\). There is an exact identity
\[
               J_\infty^{(1)}=H(E_1\mid\mathcal I)-(H-\log3)_+.          \tag{5}
\]
Indeed \(b_n=\mathbb E\log K_n=nH-H(S_n,\beta_w\bmod3^n)\) has \(b_n/n\to b\) by finite total entropy and the ternary entropy theorem. After fixing the first chronological gap \(e\), the next \(n\) gaps have total \(s-e\). Their reversed offset is the full reversed offset minus \(3^n2^{-s}\), so knowing the full total and the first \(n+1\) trits is exactly knowing that tail total and its first \(n+1\) trits. The chain rule gives
\[
 b_{n+1}-b_n=H(E_1\mid\mathcal I_{n+1})-J_n^{(1)},
\]
where \(\mathcal I_{n+1}\) is the finite class invariant field. Its additional common infinite dyadic tail is independent of the prefix. Reverse martingale convergence with finite entropy gives the limiting conditional first-letter entropy, and Cesàro averaging proves (5).

There is always strictly positive first extra-trit information. At total seven and three odd edges, the chronological gap words \((1,3,3)\) and \((2,4,1)\) have cleared numerators \(9+3\cdot2+16=31\) and \(9+3\cdot4+64=85\), differing by \(2\cdot3^3\). They represent the same three-trit cell and different fourth trits, each with mass \(\theta^3(1-\theta)^4\). Concavity on that two-word submixture yields \(J_n^{(1)}\ge2\theta^3(1-\theta)^4\log2\) for every \(n\ge3\). Complete equidistribution of this additional trit when \(H\ge\log3\) would be equivalent by (5) to \(E_1\) being independent of all integer-fusion-invariant information. Exponential growth of the classes only establishes their sizes. It does not prove that independence or provide a uniform conditional distribution in an arbitrary specified ordinary root cell.
