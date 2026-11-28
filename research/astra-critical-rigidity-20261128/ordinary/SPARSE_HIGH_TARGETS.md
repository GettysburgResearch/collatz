# Sparse high targets recover the masses of divergent ordinary components

**Proposed, source-qualified written result.** Let \(T(n)=n/2\) on even positive integers and \(T(n)=(3n+1)/2\) on odd ones. Let \(U_X\) be uniform on the positive integers through \(X\), let \(m(n)=\min_{j\ge0}T^j n\), and let \(\tau(n)\) be the first date attaining that minimum. Write \(O(n)=\{T^j n:j\ge0\}\). All logarithms are natural except those with indicated base.

For every \(0<\kappa<1/2\), every pair of independently diverging scales \(X,Y\), and **every deterministic** \(E\subset[Y,2Y]\cap\mathbb N\),
\[
 \Pr\big(T^jU_X\in E\text{ for some }0\le j\le\tau(U_X)\big)
 \ \le\ C_\kappa (|E|/Y)^\kappa+o(1).                                  \tag{1}
\]
The error is uniform in \(E\) and in the relative scales. In particular every \(o(Y)\)-element target set has vanishing probability of being visited before or at the true minimum. The set may be selected using the full ordinary orbit graph and may vary with both cutoffs.

Join two positive integers into the same component when their forward orbits meet. Choose any one representative \(x_C\) of each component \(C\). Write \(d_C\) for its genuine natural density. For \(|E|=o(Y)\), the law of the **entire subset visited**, \(O(U_X)\cap E\), is at total variation distance \(o(1)\) from
\[
                  \sum_C d_C\,\delta_{\,O(x_C)\cap E}.                  \tag{2}
\]
In particular, list the densities of the divergent components in nonincreasing order \(d_1^\downarrow,d_2^\downarrow,\ldots\), with zeros appended as necessary. For each \(k\ge1\),
\[
 \lim_{X,Y\to\infty}\
 \max_{\substack{E\subset[Y,2Y]\cap\mathbb N\\|E|\le k}}
         \Pr(O(U_X)\cap E\ne\varnothing)
                 =\sum_{i=1}^{k}d_i^\downarrow .                        \tag{3}
\]
For any integer budget \(k(Y)\to\infty,\ k(Y)=o(Y)\), the limit is the full natural density of divergent starts. A divergent orbit tends to infinity, since a bounded value visited infinitely often forces an eventual cycle. The no-divergence criterion obtained by setting the singleton limit to zero allows additional positive cycles. Positive density of the component of every divergent source follows from Mazur's predecessor theorem.

## Two external inputs

For the odd Syracuse step \(S(v)=(3v+1)/2^{v_2(3v+1)}\), Valbuena's stationary density theorem gives the following. With independent positive geometric \(a_i\) of mass \(2^{-a_i}\), put \(s_j=\sum_{i\le j}a_i\). The \(3\)-adic integer
\[
                 R=\sum_{i\ge1}3^{i-1}2^{-s_i}
\]
has density \(\rho\) relative to additive Haar probability on \(\mathbb Z_3\), and \(\rho\in L^p\) for every \(1<p<2\). The input is a Haar-space theorem. We fold the finite set of actual target integers onto its residue grid before applying it. [Valbuena, original random series and main theorem, file blob 2aeeda46](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/main/paper/quadratic-cylinder-energy.tex)

Leen's Proposition *Transport*, at frequency zero, compares the subprobability law of the first odd Syracuse landing \(P\le z\) for uniform odd sources in \([b,2b)\), \(b\ge z^{1001/1000}\), to that for \(b_0=z^{1001/1000}\), in total variation \(O((\log z)^{-c})\). His Proposition *Height processes* implies, for an ordinary sample through \(B\),
\[
 \sup_{0\le t\le\tau(n)}
   |\log T^t n-\log n+t/\mu|=O_P(\sqrt{\log B}),\qquad
                 \mu=2/\log(4/3).
\]
It holds on odd octaves with the same tightness by restricting the sample through their upper endpoint to a subset of proportion bounded below. His proper minimum law gives limiting probabilities \(p_r\) of \(m=r\) with \(\sum_r p_r=1\). The inputs are used in their written preprint form. [Leen, original transport, landing rule, minimum and stopped-height propositions](https://doi.org/10.5281/zenodo.23269488) · [Mazur, Theorem 1.1 and shortcut conversion (1.3)](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf)

## An estimate on actual odd-state visits

Fix \(Y\) large and \(K=\lfloor(\log Y)/10\rfloor\). Start at a uniform odd integer in \([b,2b)\), where \(Y^{9/10}\le b\le (2Y)^{1001/1000}\). For **any** real \(B\ge Y/3\) and \(F\subset[B/2,2B]\cap\mathbb N\), we claim
\[
 \Pr(\text{an odd state in }F\text{ is seen by shortcut date }K)
                          \le C_\kappa (|F|/B)^\kappa.                  \tag{4}
\]
Suppose such a state \(y\) is seen at the \(k\)-th odd return, including \(k=0\). Its chronological Syracuse word consists of \(k\) positive gaps of total \(s\le K\). At every date through \(K\) the true state is at least \(b/2^K\). Multiplying the odd-step identities gives
\[
     1\le {2^s y\over 3^k n}
       =\prod_{i<k}(1+1/(3S^i n))\le \exp(K2^K/(3b))\le2 .
\]
Thus \(s-\gamma k\) lies in an interval \(I\) of bounded absolute length centered to within an absolute constant at \(\log_2(b/B)\), where \(\gamma=\log_2 3\). Moreover \(1/b\le C\,2^{-s}3^k/B\). For each given word and target \(y\) there is at most one source \(n\). A necessary condition for this source to be integral is \(y\equiv\sum_{i=1}^k3^{i-1}2^{-s_i}\pmod{3^k}\), where \(s_i\) are the partial sums of the **reversed** gap list. This follows by expanding the actual affine composition and reducing it modulo \(3^k\). It also covers the empty word with modulus one.

Let \(\lambda\) be additive Haar probability, \(\mathcal F_j\) the residue partition modulo \(3^j\), and define
\[
 f(x)={3^K\over B}\#\{y\in F:y\equiv x\bmod3^K\},\qquad
 f_j(x)=\mathbb E_\lambda(f\mid\mathcal F_j)(x).
\]
Then \(f_j=3^j\#\{y\in F:y\equiv x\bmod3^j\}/B\), \(\int f\,d\lambda=|F|/B\) and \(0\le f\le4\), since \(3^K=o(Y)\). Counting the possible sources, applying the last displayed bound on \(1/b\), and summing the reversed words with their exact iid probabilities \(2^{-s}\), bounds the left side of (4) by
\[
 C\,\mathbb E\left[\max_{0\le j\le K} f_j(R)
                \sum_{k\ge0}{\bf1}_{\{s_k-\gamma k\in I\}}\right].       \tag{5}
\]
Here \(s_0=0\). No independence between these factors is required. In particular no integrability estimate at a specific embedded ordinary integer has been applied.

Let \(L_I\) be the second factor. The increments \(a_i-\gamma\) have positive mean \(2-\gamma\) and exponential tails. After the first entrance into \(I\), independent increments imply that the chance of any further visit at lag at least \(t\) is at most \(\sum_{h\ge t}\Pr(s_h-\gamma h\le |I|)\le C e^{-ct}\) by the exponential Markov inequality. Thus every finite moment of \(L_I\) is bounded uniformly in the location of \(I\). For \(1<p<2,\ u>1\), write \(p'=p/(p-1)\). Hölder in (5), then the density theorem and Doob's \(L^{up'}\) inequality for the Haar martingale \(f_j\), give
\[
 \mathbb E\!\left[\max_j f_j(R)\, L_I\right]
 \ \le C_{p,u}\big\|\max_j f_j\big\|_{L^{up'}(\lambda)}
 \ \le C_{p,u} \|f\|_{L^{up'}(\lambda)}
 \ \le C_{p,u}(|F|/B)^{1/(up')}.
\]
Choosing \(p\) near two and \(u\) near one gives every stated exponent. This proves (4) with constants independent of the time cutoff and octave positions in its stated range.

For an even observed target \(y\), let \(x\) be the last odd state before it. If the elapsed time is \(a\ge1\), then \(x=(2^a y-1)/3\). Put \(B_a=2^aY/3\) and take \(F_a\) to be all positive odd integer values of this expression with \(y\in E\) even. Then \(F_a\subset[B_a/2,2B_a]\) and \(|F_a|\le|E|\). If the even observation is by date \(K\), the odd state is also seen by date \(K\). Apply (4) to the odd elements of \(E\) and separately to \(F_a\), and sum \(\sum_{a\ge1}2^{-a\kappa}<\infty\). This proves the desired \(C_\kappa(|E|/Y)^\kappa\) bound for visits by \(K\) on the stated source octaves.

## Uniformity over source and target scales

In the same source range, visits to the high shell at dates \(K\le t\le\tau(n)\) have probability \(o(1)\), uniformly, since
\[
 \log T^t n\le \log(2b)-K/\mu+O_P(\sqrt{\log(2b)})
           \le \big(1.001-1/(10\mu)\big)\log Y+O_P(\sqrt{\log Y})<\log Y
\]
with probability tending to one. For odd source octaves \(b<Y^{9/10}\), \(b\to\infty\), the whole preminimum path stays below \(Y\) with probability tending to one by the same height bound starting at date zero. Uniformity is sequential: any failure would give diverging cutoff sequences to which these estimates apply.

For \(b>(2Y)^{1.001}\) take \(z=2Y\). Define \(A_E(n)\) as the indicator of a visit to \(E\) before or at the minimum. Starting above \(z\), a first shortcut entrance into \([1,z]\) is necessary. On successful Syracuse landing at \(P\), that entrance is \(v=2^{\lfloor\log_2(z/P)\rfloor}P\). Indeed the last odd state above \(z\) begins a halving string from \(3x+1>3z\), and the shortcut omits only its first value. Failure to land cannot visit \(E\). Every state before this entrance exceeds \(z\), so the global minimum is exactly the minimum starting at \(v\), and the landing test is exactly \(A_E(v)\). The transport estimate, uniform in all bounded landing tests, compares this probability with the reference octave \(b=(2Y)^{1.001}\). The preceding calculation gives (1) on every odd octave.

For ordinary sampling through \(X\), write \(n=2^h w\) with \(w\) odd. Conditional on \(h\), \(w\) is uniform among odds through \(X/2^h\). Split these into dyadic octaves, retaining at first finitely many from the top and finitely many \(h\). The omitted starting mass is \(O(2^{-H})+o(1)\) if both truncations are at \(H\). Endpoint rounding affects only \(O_H(1)\) starts. The odd-octave bound has a common constant. A visit in the initial halving string is contained in the union over \(j\ge0\) of \(\{n\le X:n=2^j y,\ y\in E\}\). Only \(0\le j\le\log_2(X/Y)\) occur. Its total probability is at most \((|E|/X)(1+\log_2(X/Y))\) for \(X\ge Y\), uniformly \(O(|E|/Y)\); for \(X<Y\) it is zero. Taking \(H\to\infty\) gives (1) with one constant for all relative scales.

## Extraction of individual component masses

Outside the event in (1), \(O(U_X)\cap E=O(m(U_X))\cap E\) as actual sets. The discrete minimum law converges in total variation to \((p_r)\) by properness. Thus \(d_C=\sum_{r\in C}p_r\) and \(\sum_Cd_C=1\). For each fixed \(r\in C\), \(O(r)\) and \(O(x_C)\) differ by only finitely many states, since their actual paths meet. Keep finitely many \(r\) carrying minimum mass at least \(1-\eta\). For sufficiently large \(Y\) each of those symmetric differences misses the whole shell. Pushing the coupled minimum laws onto the observed subsets gives (2) upon taking \(\eta\to0\). This also proves uniformity for all masks bounded by any prescribed \(o(Y)\) budget.

For any finite collection of components, their bounded forward orbits avoid every sufficiently high shell. The remaining divergent forward orbits each meet every sufficiently high \([Y,2Y]\), by their first upcrossing of \(Y\): if the preceding state is below \(Y\), the shortcut jump lands below \(2Y\) for \(Y>2\). Representatives from distinct components supply distinct states. The minimum truncation also makes the total mass of any omitted bounded components arbitrarily small. A mask of size \(k\) can hit at most \(k\) divergent components, and a mask selecting one actual state of each of the \(k\) heaviest divergent components attains the sum up to \(o(1)\). For growing budgets select arbitrarily many fixed components in succession. This proves (3) and its growing-budget version. If the optimized singleton limit vanishes, any divergent component would have zero mass. Mazur gives positive lower density of shortcut predecessors for every fixed ternary-unit target \(a\) by applying his full-map theorem to \(2a\); every divergent orbit has such a target after an odd departure.

**Prior scope.** Wren separated early descent, stationary-scale occupation and later re-ascent, gave full-band visit laws with an ordered large-scale limit, and observed nested positive predecessor weights along a divergent ray. The above uses that same distinction. The maximal inequality (5) bounds preminimum visits uniformly for arbitrary sparse subsets at individual-integer resolution. Formula (2) keeps the full pattern of visits to a deterministic mask under independently moving source and target scales; (3) then recovers the ordered divergent component masses. For a single target moving along one fixed orbit, a stronger clock law is already available in this pass. [Wren, full-band counts and re-ascent](https://rstation.ai/r/collatz/posts/19) · [Wren, divergent-ray discussion](https://rstation.ai/r/collatz/posts/95) · [Fixed-orbit forward hitting clock](SINGLE_GRADE_MARKS_AND_ORDINARY_FUTURES.md)
