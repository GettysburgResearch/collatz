# Exact additive separation of decoded Syracuse source measures

Let $1<b\le a_*$ and let $\mu$ be the ternary source of iid positive geometric gaps of mean $b$, with $\theta=1/b$. Every nonzero integer translation $\tau_j(x)=x+j$ satisfies
$$
                        \mu\perp (\tau_j)_*\mu.                    \tag{1}
$$
There is a single Borel set of full $\mu$-measure on which no two distinct points differ by an ordinary integer. For dyadic rational translations $h/2^r$ the actual overlap is given by the exact finite sum (4) below; it can be positive. At the real-drift threshold and below, the finite-depth approach to (1) has a polynomial rate, uniform over sufficiently slowly growing polynomial ranges of integer shifts. At the entropy threshold we prove separation without assuming a quantitative entropy-dimension rate.

**Priority and scope.** PR 215 checkpoint 7 already proves the stronger exact common-measure classification for the entire positive $2,3$ affine group, including (1), the conull wandering carrier, the overlap at $1/4$, and an exact finite algorithm. Its proof credits Paper 212's constructive counted-fusion steering, obtains logarithmic witness length, and bounds finite overlap on a growing range of even shifts by the first-gap conditional entropy. The argument below gives a physical binary-word specialization, an equal-clock rational-affine representation, and finite entropy rates from the ordinary numerator size below and at the real-drift threshold. Section 3 makes the resulting polynomial ranges explicit for odd and even shifts. [PR 215, affine classification](https://github.com/GettysburgResearch/collatz/blob/dd69808eac0577f387d46cd6bc66af197bb6875e/research/astra-nine-hour-20261128/machinery/phase7/CRITICAL_AFFINE_OVERLAPS.md) · [Counted steering and antecedents](https://github.com/GettysburgResearch/collatz/blob/dd69808eac0577f387d46cd6bc66af197bb6875e/research/astra-nine-hour-20261128/machinery/phase7/DETERMINISTIC_COUNTED_FUSION.md) · [Growing integer jitter](https://github.com/GettysburgResearch/collatz/blob/dd69808eac0577f387d46cd6bc66af197bb6875e/research/astra-nine-hour-20261128/machinery/phase7/GROWING_INTEGER_JITTER.md).

## 1. Encode in physical bits and synchronize an arbitrary integer shift

Write $B_0(x)=x/2$, $B_1(x)=(1+3x)/2$ and compose letters from left to right as function symbols, $B_w=B_{w_1}\circ\cdots\circ B_{w_r}$. For $k$ ones in positions $s_1<\cdots<s_k$, the exact affine map is
$$
 B_w(x)=\frac{3^k x+C_w}{2^r},\qquad
 C_w=\sum_{j=1}^k3^{j-1}2^{r-s_j}.
$$
Independent Bernoulli-$\theta$ letters, read through each next one, have independent geometric interarrival gaps. A full grouped block $0^{e-1}1$ equals $A_e(x)=(1+3x)/2^e$, hence the physical source has exactly law $\mu$. At $b\le a_*$ the whole sequence of geometric gaps is almost surely determined by the original ternary source, by the critical/subcritical entropy-dimension identity and the conditional branch entropy formula. For completeness let $h_j=H(X\bmod3^j)$ and $H=H(b)$. Then $H(g_1\mid X\bmod3^j)=H+h_{j-1}-h_j$ for $j\ge1$, since $g_1$ fixes the first trit and permutes the remaining suffix cells. The left side decreases to a limit by finite gap entropy; its Cesàro mean tends to zero as $h_j/j\to H$ by Leen. Thus $g_1$ is recovered, and iteration recovers every gap. This also determines every finite physical prefix even when its last letter is zero. Therefore unequal same-length physical words have mutually singular full source images $(B_u)_*\mu,(B_v)_*\mu$. Both words have positive probability. [Leen, *Tilted 3-adic Syracuse laws*, Theorem C](https://doi.org/10.5281/zenodo.23268832).

For each $h\in\mathbb Z$ we construct words $u,v$ of the same physical length and the same number of ones with
$$
                         B_u^{-1}B_v(x)=x+h.                         \tag{2}
$$
The empty pair represents zero. If $B_U^{-1}B_V=x+j$, append one-one blocks $c,d$ of a common length $s$ to $U,V$. Their new translation is $(2^s j+C_d-C_c)/3$. For $s=2$ the available one-one numerators are $1,2$; for $s=3$ they are $1,2,4$. To obtain $h=\pm1$ use $s=3$, $j=0$ and $C_d-C_c=\pm3$. For nonzero even $h$, append one zero letter on each side of the pair for $j=h/2$; this doubles its translation. For odd $|h|>1$, choose $s=2$ and $\Delta=C_d-C_c\in\{-1,1\}$ congruent to $3h\bmod4$. This gives the predecessor $j=(3h-\Delta)/4$. In either induction case $|j|\le7|h|/8$. Thus induction terminates in $O(1+\log(1+|h|))$ blocks, each consuming at most three physical letters. Equal maps are impossible for $h\ne0$, so the final equal-length words differ. Apply physical decoding and pull back by the common injective affine map $B_u$ to obtain (1). For the single full-measure set, first take for each nonzero $h$ a full carrier $F_h$ with $\mu(F_h-h)=0$. After intersecting those full carriers, remove all their common carrier's nonzero integer translates; the resulting Borel subset still has full measure and has the stated pairwise separation.

## 2. Separation of integer-affine components and dyadic overlaps

In fact $\mu\perp(g_{m,d})_*\mu$ for $g_{m,d}(x)=3^m x+d$, any $m\ge0,d\in\mathbb Z$, except $(m,d)=(0,0)$. There are equal-physical-length words $u,v$ with $B_u^{-1}B_v=g_{m,d}$ and whose numbers of ones differ by $m$. For $m=0$ this is (2). For $m>0$ and nonzero even $d$, use $g_{m,d}=B_0^{-1}g_{m,d/2}B_0$ repeatedly until the remaining $d$ is odd. If $d=0$ first use $g_{m,0}=B_1^{-1}g_{m,(1-3^m)/2}B_1$, whose new integer is nonzero. For odd $d$,
$$
           g_{m,d}=B_0^{-1}\,g_{m-1,(d-3^{m-1})/2}\,B_1 .
$$
This reduces $m$. The resulting representation by equal-length words follows by appending the displayed single labels at each induction step. At $m>0$ the two words have different numbers of ones and so are distinct. This proves singularity by the same pullback.

For integers $h$ and $r\ge0$ put $\nu=(\tau_{h/2^r})_*\mu$. Let $k_w$ count the ones of an $r$-bit word and $p_w=\theta^{k_w}(1-\theta)^{r-k_w}$. Expanding the first $r$ independent bits gives $(2^r)_*\mu$ as a mixture of the laws of $3^{k_w}X+C_w$, and $(2^r)_*\nu$ as the analogous mixture with the additional intercept $h$. For two such components, divide out the lower of their powers of three. If their intercept difference is not divisible by that power, the supports lie on different residue classes. Otherwise pullback reduces the comparison to $x\mapsto3^m x+d$ with integer $d$ as above. Thus distinct affine maps give mutually singular component laws. At fixed $r,k$, distinct words have distinct $C_w$ (successive binary valuations recover the last one and then all previous positions). All coincident affine components have the same weight. The common mass is consequently
$$
 (\mu\wedge\nu)(\mathbb Z_3)
 =\sum_{\substack{u,v\in\{0,1\}^r\\ k_u=k_v,\ C_u=C_v+h}}
          \theta^{k_u}(1-\theta)^{r-k_u}.                           \tag{4}
$$
For $h/2^r=1/4$ the mass is $\theta(1-\theta)$, from the two possible positions of one odd symbol in two steps. For nonzero integers one may take $r=0$, recovering (1). The formula concerns dyadic rational translations of the original source measure. It gives no general assertion about rational shifts with other denominator primes.

## 3. Quantitative finite-depth separation by native entropy

Let $E_N=NH-H(X\bmod3^N)=H(g_1,\ldots,g_N\mid X\bmod3^N)$, where the second equality uses determination of $N$ trits by those gaps. Then $E_N$ is nonnegative and nondecreasing, and for $r\le n$,
$$
 H(g_1,\ldots,g_r\mid X\bmod3^n)=E_n-E_{n-r}.                    \tag{5}
$$
Condition on the gaps and use affine permutation of the remaining $n-r$ free trits. Write $J_N(h)$ for the overlap of the depth-$N$ distributions of $X$ and $X+h$. Choose the two witness words in (2), with length $r$, $k$ ones, and common prior mass $p\ge\min(\theta,1-\theta)^r$. At observed precision $n+k$, their two conditional suffix laws are the depth-$n$ laws of $X$ and $X+h$ up to a common affine permutation. Hence the conditional entropy of the first $r$ physical bits given those observations is at least $2p\log2\,J_n(h)$. Indeed restrict to the event that the prefix is one of the two words, include its posterior weight, and use binary entropy $h_2(z)\ge2\log2\min(z,1-z)$. The first $r$ gaps determine the first $r$ physical bits. Therefore for $n+k\ge r$,
$$
       2p\log2\,J_n(h)\le E_{n+k}-E_{n+k-r}.
$$
Sum over $\lceil N/2\rceil\le n\le N$. Each nonnegative entropy increment on the right occurs at most $r$ times. Monotonicity of finite overlap yields, for $N\ge2r$,
$$
 J_N(h)\le\frac{r E_{N+r}}{p\log2\,N}.                            \tag{6}
$$
Since $r=O(1+\log(1+|h|))$, the coefficient is at most $C_b(1+|h|)^{A_b}$ for finite constants. Leen's dimension theorem gives $E_N=o(N)$ throughout the stated range, including $b=a_*$. This yields simultaneous finite-depth separation on a slowly increasing range of shifts, without identifying an explicit growth power at that endpoint.

For $b<\alpha=\log_2 3$ we have $E_N=O_b(\log(N+1))$, and at $b=\alpha$ we have $E_N=O(\sqrt{N}+\log(N+1))$. To see this, write $S_N=\sum_{j\le N}g_j$ and $C=\sum_{j=1}^N3^{j-1}2^{S_N-S_j}$. Given $X\bmod3^N$, $S_N$ and $Q=\lfloor C/3^N\rfloor$, the exact congruence $C\equiv2^{S_N}X\bmod3^N$ recovers the integer numerator, hence the word by binary valuation decoding. Thus $E_N\le H(S_N)+H(Q)$. The mean of $S_N$ gives $H(S_N)=O_b(\log(N+1))$ by the geometric maximum-entropy bound. The integer entropy of $Q\ge0$ is at most $2\mathbb E\log(1+Q)+\log\sum_{j\ge1}j^{-2}$ by comparison with a probability proportional to $(1+Q)^{-2}$.

In reverse letter order $C/3^N$ has the law of $\frac13\sum_{j=0}^{N-1}\exp Z_j$, where $Z_j$ is the partial sum of iid increments $g\log2-\log3$. If $b<\alpha$ these increments have negative mean and a finite exponential moment near zero; choose $0<s<1$ with $\mathbb E e^{sZ_1}<1$. Subadditivity of the $s$-power and the geometric sum give a uniform $s$-moment, hence uniformly bounded expected logarithm. At $b=\alpha$, Doob's square-integrable maximal inequality gives $\mathbb E\max_{j\le N}|Z_j|=O(\sqrt N)$; add $O(\log(N+1))$ for summing the exponentials. This proves the entropy estimates. In (6) the resulting overlap bounds are $O_b((1+|h|)^{A_b}\log(N+1)/N)$ below $\alpha$ and $O_b((1+|h|)^{A_b}/\sqrt N)$ at $\alpha$. The dyadic numerator decoding is the same arithmetic separation used by Tao. [Tao, Lemma 6.2](https://arxiv.org/abs/1909.03562).

The route in `CRITICAL_OVERLAP_AND_ROUTING.md` amplifies a finite corridor set by many distinct integer translations. Here those translations all separate the infinite critical source. Formula (6) locates the unresolved quantitative size: a short route can offer exponentially many shifts, while at $a_*$ only $E_N=o(N)$ is guaranteed. Neither infinite mutual singularity nor a fixed-shift convergence rate proves that the exponentially many moving finite corridor sets overlap little enough to reach the optimum.

The explicit physical identities `integer_shift` and `integer_affine` in [TranslationWords.lean](TranslationWords.lean) quantify over all rational arguments and all signs of the intercept; they also retain equal word lengths and the prescribed difference of odd counts. The measurable decoder, finite-depth entropy estimates and rates are written arguments. [Exact witness and dyadic refinement controls](check_translation_words.py). PR 215 phase 10 independently bounds a positive moment of the equal-total fusion population below the real-drift threshold, which also yields logarithmic ambiguity after adding the entropy of the total. The centered real-drift estimate above bounds the numerator directly without requiring a finite limiting fusion class. [PR 215, integer fusion populations](https://github.com/GettysburgResearch/collatz/blob/18e1e631/research/astra-nine-hour-20261128/machinery/phase10/INTEGER_FUSION_POPULATIONS.md).
