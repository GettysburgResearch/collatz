# Higher additive orders force a stretched-exponential improvement in the narrow-band residence exponent

**Proposed written theorem.** Write \(\gamma=\log_2 3\), fix \(B\ge0\) and an upper bound \(\mu_0<\infty\) for the irrationality measure of \(\gamma\). Fix \(0<\eta<1\) and set \(R=2^{1+\eta}\). Let
\[
 L=L(\eta)=\min\{j\ge1:\|j\gamma\|\le\eta\},\qquad
 I_j=\log_2\left(\frac{4^j}{\binom{2j}{j}}\right),\qquad
 r_j=\frac{(1+B)\eta I_j}{\gamma j}.
\]
For a run of \(T\) consecutive **distinct** positive odd rational Collatz states in \([M,RM]\), let \(Q\) denote their common complete reduced denominator, prime to six. Suppose \(Q\le M^{B+o(1)}\) along the family under consideration, as \(M\to\infty\). For ordinary states take \(Q=1,\ B=0\).

Choose any fixed \(h\ge2\) such that \(h<3^L,\ r_1<1\) and
\[
       \big(1+j(\mu_0-1)\big)r_{j-1}<1
                         \qquad(2\le j\le h).                           \tag{1}
\]
Then
\[
                          T\le M^{r_h+o(1)}.                            \tag{2}
\]
In the proof an actual normalized label set from one chronological interval has all its unordered sums of \(h\) terms distinct, with repetitions allowed. The proof uses the true dyadic recurrence at every offset and every dilated offset over a common finite interval. Initial source size and both native divisors use the full \(Q\).

In particular, for every fixed
\[
   0<c<\min\left\{\log_2 3,\ \frac{\gamma}{(1+B)(2\mu_0-1)}\right\},
\]
the exponent in (2) is \(O_{B,c}(\eta L\,2^{-cL})\) for all sufficiently small fixed \(\eta>0\). At every fixed \(\epsilon>0\) this is at most
\[
          \exp[-c_{\epsilon,B,\mu_0}\,
                      \eta^{-1/(\mu_0-1+\epsilon)}]                    \tag{3}
\]
for some positive constant (which may also depend on \(\gamma\)). These are bounds on \(\limsup_{M\to\infty}\log T/\log M\) at each fixed width; the limit in \(M\) precedes the limit in \(\eta\). Classical published input allows \(\mu_0=5.116201\). The separately audited modern input allows \(\mu_0=3\), giving every power below \(1/2\) in the negative exponent of (3). No uniformity in the two limits, or assertion on the entire pooled population of independent source histories, is used. [BLS, Theorem 1](https://doi.org/10.22405/2226-8383-2018-19-1-15-25) · [Original exponent-three input and audit](../literature/CHUDNOVSKY_LOGARITHM_IMPORT.md)

## One short region of angles from a single actual run

First consider polynomial lengths \(T=M^{\lambda+o(1)}\) with \(0<\lambda<1\). Index actual odd dates \(0,\ldots,T-1\). Put \(U_t=2^{E_t}\) for genuine cumulative valuation with \(E_0=0\), \(V_t=U_t x_t\), so \(V_{t+1}=3V_t+U_t\). Choose \(N=\lfloor T/(\log M)^4\rfloor\) original times \(0\le t<N\). Partition the fractional parts \(\{t\gamma\}\) into \(O((\log M)^2)\) consecutive intervals of width \(O((\log M)^{-2})\). Retain a largest cell, subtracting its smallest time \(t_*\) from every retained time. Call the resulting set \(\mathcal S\); it contains zero, has size \(K=M^{\lambda-o(1)}\), and lies in \([0,N]\). Define
\[
 k_s=\lfloor(t_*+s)\gamma\rfloor-\lfloor t_*\gamma\rfloor,\quad
 D_s=2^{-k_s}\operatorname{shift}^{s},\quad w_s=3^s2^{-k_s}.
\]
Thus \(\log_2 w_s=\{(t_*+s)\gamma\}-\{t_*\gamma\}=o(1)\), with a uniform error. The factors \(w_s\) are all distinct by unique factorization. No coprimality or single-sheet sampling of a rational rotation is necessary.

Use \(J=M\sqrt R\) and \(F_i=\lfloor\log_2(V_i/J)\rfloor\). Fix any finite list of positive dilation factors \(l\). Uniformly on the available central dates, including every index used after a bounded number of offset compositions,
\[
  2^{-F_i}D_s^l V_i
     =2^{-F_i}V_i\,w_s^l(1+O_{R,l}(N/M)),\qquad
             C_{i,l,s}=2^{-F_i}D_s^l U_i\in\{1,2\}.                    \tag{4}
\]
The shape estimate sums the genuine log corrections
\(\log_2(1+1/(3x_j))\) over \(ls\) actual steps. The base label lies in \([J,2J)\). Since \(RM/2<J<2M\) with fixed margins, the rescaled label lies strictly between \(RM/2\) and \(4M\) for all large \(M\); dividing by its physical state in \([M,RM]\) leaves exactly the two possible dyadic powers. The statement is for one dilation at a time; the intermediate composed operators needed below act on a known zero interval and do not require a new chart. All rescaled labels belong to \(Q^{-1}\mathbb Z\).

For the original offsets \(l=1\), if the row contains both tags, \(z_i=\{\log_2(V_i/J)\}\) lies in an \(o(1)\) enlargement of the angular interval \([\log_2(2M/J),\log_2(RM/J)]\), of length \(\eta\). This follows by comparing a tag-two and a tag-one label in (4). For fixed \(1\le j<L\), the angular displacement over \(j\) dates differs from \(j\gamma\bmod1\) by \(O_R(j/M)\). The strict inequalities \(\eta<\|j\gamma\|\) force any two such variable rows to be at least \(L\) dates apart for all sufficiently large \(M\). On any consecutive coding interval of \(n\asymp\log M\) dates, the number of variable rows is at most \((\eta+o(1))n\), uniformly in the anchor. Indeed the angular displacement from the irrational rotation is \(O_R(n/M)\), and the usual finite geometric-sum estimate gives uniform equidistribution of length-\(n\) segments of that rotation. Fix an enclosing interval before decreasing its excess length to zero.

## Many actual integer power comparisons from one physical equality

Fix \(2\le j<3^L\). Suppose two unordered \(j\)-sums of the normalized labels \(2^{-F_a}D_sV_a\) coincide at the central anchor \(a=\lfloor T/2\rfloor\). Cancel all common occurrences. If the multisets differ there are \(1\le d\le j\) terms on each side and their remaining supports are disjoint. Write \(P=\sum_s c_sD_s\), where \(c_s\) are the remaining signed multiplicities, \(\sum c_s=0\) and the total positive mass is \(d\). Let \(H_i=2^{-F_i}PV_i,\ e_i=2^{-F_i}PU_i\). The full native edge is
\[
       2^{F_{i+1}-F_i} H_{i+1}=3H_i+e_i,\qquad
                    QH_i\in\mathbb Z,\quad |e_i|\le d .
\]
Inactive rows have \(e_i=0\). If a variable row \(i\) has \(H_{i+1}=0\), then its preceding \(L-1\) inactive rows give \(3^{L-1}\mid QH_i\) by the homogeneous recurrence and coprimality of powers of two to three. Hence \(3^L\mid Qe_i\). Since \(Q\) is prime to three and \(|e_i|<3^L\), we get \(e_i=H_i=0\). At an inactive row the reverse step is immediate. Peeling from \(a\) down to \(\lfloor T/5\rfloor\), with its \(L-1\) guard inside the supplied run, gives \(PU_i=0\) throughout \([\lceil T/4\rceil,a-1]\).

Choose \(j\) distinct odd primes \(l_1,\ldots,l_j>j\), all fixed before \(M\to\infty\). For any one such prime \(l\), \(P^l U_i=0\) on \([T/3,5T/12]\) for all large \(M\): each of the at most \(l-1\) shifts applied to \(PU\) has size \(\le N\), and \(lN=o(T)\). In the dyadic shift-operator ring modulo \(l\),
\[
                       P^l\equiv\sum_s c_sD_s^l .
\]
This is the characteristic-\(l\) identity with Fermat's congruence for signed integer coefficients. Evaluation on \(U\) and multiplication by \(2^{-F_i}\) preserve divisibility in \(\mathbb Z[1/2]\). The resulting dilated forcing \(\sum c_s C_{i,l,s}\) is an ordinary integer of absolute value \(\le d<l\) by (4), hence it vanishes there. Over that interval the corresponding dilated label difference follows the homogeneous native recurrence. Take \(i=\lceil 3T/8\rceil\), common to all \(l\), and \(n=\lceil\log_3(16jRQM)\rceil+3\) edges to its right. These edges fit for large \(M\). The full integer \(Q2^{-F_i}\sum_s c_s D_s^lV_i\) is divisible by \(2^{F_{i+n}-F_i}\), which is \(\ge 3^n/2\) by the genuine positive log correction. Its absolute value is \(\le4jRQM\) by (4). It is therefore zero. Dividing by the common positive base in (4) gives
\[
                  \left|\sum_s c_s w_s^{l}\right|\ll_{R,j,l} N/M       \tag{5}
\]
for all \(j\) distinct chosen primes. The comparison and the errors use a single physical interval, with no cyclic wrap. This extends the single-prime finite comparison used for pair sums. [Earlier finite native argument](FROBENIUS_BAND_EXITS.md) · [Classical finite-support prime dilation, Kari–Szabados, Lemma 7](https://arxiv.org/abs/1605.05929)

## Recovering repeated roots at the common angular scale

Here is the needed real algebra estimate. Fix \(d\) distinct positive integers \(l_1,\ldots,l_d\). For two lists of \(d\) real numbers tending uniformly to one, if their respective \(l_i\)-th power sums differ by \(O(\varepsilon)\) for every \(i\), their monic root polynomials in the variable \(X\), formed after subtracting one from each entry, have coefficient vectors differing by \(O_{d,l}(\varepsilon)\).

Indeed, put \(u_s=w_s-1\). The power sum \(p_l(1+u)\) is a polynomial in the elementary symmetric coordinates \(e_1,\ldots,e_d\) of the \(u\)'s. At \(e=0\) its partial derivative with respect to \(e_k\) is
\[
                       \binom{l}{k}(-1)^{k-1}k .
\]
Expand in the \(p_v(u)\): Newton's identities give linear term \((-1)^{v-1}v e_v\) for \(1\le v\le d\), and no linear term for \(v>d\) by weighted homogeneity. The matrix \((\binom{l_i}{k})_{1\le i,k\le d}\) is invertible. Divide row \(i\) by \(l_i\); the columns are polynomials in \(l_i\) of distinct degrees \(0,\ldots,d-1\) with nonzero leading coefficients. The inverse function theorem in these coefficient coordinates now gives a locally Lipschitz inverse on a neighborhood of the limiting output. This argument applies with colliding or repeated roots.

Use the first \(d\) primes in (5) for the two uncancelled lists. Evaluate the right list's monic root polynomial at any left root \(w_s-1\). Its absolute value is \(O(N/M)\) since the left polynomial vanishes and its argument tends to zero. Each of the \(d\) factors in that evaluation is \(|w_s-w_{s'}|\) for distinct offsets. For any fixed \(\epsilon>0\), the irrationality bound and the angular normalization give
\[
                   |w_s-w_{s'}|\gg_{\epsilon,\gamma}
                          T^{-(\mu_0-1+\epsilon)} .
\]
In fact \(|\log_2 w_s-\log_2 w_{s'}|\ge\|(s-s')\gamma\|\) and \(0<|s-s'|\le T\); finitely many small differences are absorbed into the constant. If
\[
                         \big(1+j(\mu_0-1)\big)\lambda<1,               \tag{6}
\]
choose \(\epsilon\) small enough to obtain a contradiction to (5), since \(N/M\le M^{\lambda-1+o(1)}\) and \(d\le j\). Thus every two equal physical \(j\)-sums of this entire sampled label set have the same multiset, with all repetitions counted. This step identifies the offsets from genuine homogeneous factors; a pair of independent source histories would not supply the separated \(w_s\)'s.

## Iteration of the binary additive-code bound

Over \(n=\lceil\log_3(16hRQM)\rceil+3\) future edges from \(a\), encode each offset by its actual tags minus one, retaining only variable rows. There are at most \((\eta+o(1))n\) binary coordinates. Coordinatewise equality between two \(j\)-sums of words makes the corresponding forcing zero on the entire window. The homogeneous recurrence gives the full divisor \(2^{F_{a+n}-F_a}\mid QH_a\); the same height estimate as above implies \(H_a=0\). Individual words are injective without (6): equality gives equality of two individual normalized labels, hence equality of their odd physical states by comparing dyadic valuations of the odd numerators. The run has distinct states. Thus \(K\le2^{(\eta+o(1))n}\) and \(\lambda\le r_1\). This first bound also excludes any exponent \(\ge1\), or superpolynomial length, when \(r_1<1\): truncate any such run to \(\lfloor M^\xi\rfloor\) dates with \(r_1<\xi<1\). All later estimates can therefore be applied on convergent positive-exponent subsequences; bounded or subpolynomial lengths satisfy (2) immediately.

Under (6) each code is \(B_j\): equal coordinate sums give equal initial label sums and hence the identical multiset by the preceding section. For a \(B_j\) subset of the binary \(k\)-cube with \(K\) points, independently sampling \(j\) words on each side gives collision probability \(\le j!/K^j\). It is also \(\ge(\binom{2j}{j}/4^j)^k\). Indeed, the collision probability for any probability law is the \(2j\)-th power of its Fourier polynomial's \(L^{2j}\)-norm on the \(k\)-torus. This functional is convex and invariant under coordinate flips. Averaging all flips minimizes it at the uniform law on the full cube, where the one-coordinate collision probability is the stated central binomial ratio. Consequently \(\log_2K\le(k/j)I_j+O_j(1)\), giving \(\lambda\le r_j\). This is Polyanskiy's symmetrization proof as recorded by Gu, applied here to the verified finite native code. [Gu, Proposition 3.8, original manuscript](https://arxiv.org/abs/1809.07364)

Start with \(\lambda\le r_1\), then apply (6) and the coding estimate successively for \(j=2,\ldots,h\), using (1). This proves (2).

Finally the \(L\) points \(0,\gamma,\ldots,(L-1)\gamma\bmod1\) have pairwise circular distance greater than \(\eta\), so \(\eta L\le1\) (also immediate if \(L=1\)). The central binomial coefficient is the largest of the \(2j+1\) binomial coefficients of order \(2j\), hence \(I_j\le\log_2(2j+1)\). For \(2\le j\le h\),
\[
  (1+j(\mu_0-1))r_{j-1}
     \le (1+B)(2\mu_0-1)\eta\,\log_2(2h+1)/\gamma .
\]
Choose \(h=\lfloor2^{cL}\rfloor\). Since \(L\to\infty\) as \(\eta\downarrow0\), all strict conditions hold for sufficiently small \(\eta\), giving the stated \(O(\eta L2^{-cL})\). From \(\|L\gamma\|\le\eta\) and the irrationality bound one has \(L\gg_{\gamma,\epsilon}\eta^{-1/(\mu_0-1+\epsilon)}\); absorbing the prefactors yields (3).

The exact factor-two inverse theorem and the rotation occupancy estimate for moving near-octaves concern a different order of limits. The physical source count for a collection of arbitrary confined prefixes permits independent histories. The high-order argument above requires one true chronology in order to dilate the same relation and separate the resulting factors. [Weaver, Paper 222/v1](https://rstation.ai/problems/collatz/papers/222/v1) · [Near-doubling finite-scale residence](../literature/NEAR_DOUBLING_RESIDENCE.md) · [Confined source entropy](../literature/CONFINED_SOURCE_ENTROPY.md) · [Previous open matched-width exponent](OPEN_MATCHED_WIDTH_RATES.md)
