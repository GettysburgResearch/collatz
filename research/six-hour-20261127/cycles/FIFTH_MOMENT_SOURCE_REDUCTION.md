# A fractional moment source test for ordinary binary cycles of real width less than two

Let λ=log₂3. A primitive positive ordinary integer cycle has odd period P, maximal odd phase X, binary accelerated valuations, and discrepancy width W=range(E_i−iA/P)<2. For a local mechanical slope θ=A/P, one writes E_i=⌊iθ+t⌋+z₀−z_i in a window, with layer bits z_i∈{0,1}. The allowed bits descend on mechanical gap one and ascend on gap two. On a segment of a letters with specified entrance and exit bits, let

$$
 B(z)=\sum_{i=0}^{a-1}3^{a-1-i}2^{r_i},\qquad
 r_i=\lfloor i\theta+t\rfloor+z_0-z_i,\qquad
 F(v)=\sum_{z}\exp(2\pi i B(z)v).
$$

Floors are local with 0≤t<1. The sum ranges over the entire binary layer path family with these cuts. A cycle supplies only a subset of these paths.

**Sufficient local inequality.** Suppose there are δ>0, a₀, a neighborhood of λ, and C such that, uniformly in the cuts, intercept and θ in this neighborhood, for a≥a₀,

$$
 \int_{\mathbb T}|F(v)|^5\,dv\le C 3^{(4/3-\delta)a}.\tag{1}
$$

Then along sequences of such ordinary cycles with P→∞, one has liminf log X/log P ≥4/(4/3−δ)>3. Consequently the source-qualified logarithm-ratio bound μ(λ)≤3 implies finiteness of the entire real W<2 binary ordinary cycle class. This does not classify a finite exception. The proof also applies if (1) holds in the joint limit a→∞, θ→λ with this strict exponential margin, instead of throughout one fixed open neighborhood. The source separation below imports the integral Subspace Theorem as applied in Weaver 145, Lemma 4. Neither (1) nor an unrestricted conclusion about Collatz is asserted here.

## Five real segments and reciprocal sampling

Fix η>0 small. Take b=⌈((5+η)/(4+η))(log₂ X+3)/θ⌉, total binary length K=E_b, h=⌊K/(5+η)⌋, N=2^h, a=⌊(1−η)h/θ⌋. Fix the window phase cell, end bits, and the exterior of five adjacent segments of length a, starting at j₀=⌈3ηh/θ⌉+1. The number of outside choices is at most 2^{b−5a+6}. The five cut-conditioned relaxations factor as a product. At a segment start j write u=E_j, T=E_{j+a}−E_j, m=K−u and n=j+a. The five segments end before b, the last start has u≤4h+O(1), and the first end has nθ≥(1+2η)h−O(1). Thus m,λn≥h for large X, and T≤(1−η)h+O(1). Since θ>λ, B≤4a2^T. Put D=⌈4a2^T⌉. By the actual source congruence modulo 2^K, the segment's normalized frequency is exactly

$$
 V(B)=\omega B\pmod1,\qquad \omega=[-3^{-n}]_{2^m}/2^m.
$$

Indeed multiplying each term of −2^{-m}Σ_i 2^{r_i}3^{−j−i−1} by 3^n modulo 2^m gives −B. This needs no independent random phase.

For each fixed B₀>0, eventually the numbers kω for 0≤k≤2D are pairwise B₀/N separated on the circle. Otherwise for some integer 0<k≤2D there is a representative b₀≡−k3^{-n} (mod 2^m), |b₀|≤B₀2^{m−h}. Set a₀=(k+3^n b₀)/2^m. The integer difference 2^m a₀−3^n b₀=k has size at most 8a2^T+2≤2^h exp(−cηK), with |a₀|≪3^n2^{-h}+1, |b₀|≪2^{m−h}. These are exactly the small-difference bounds excluded by Weaver 145, Lemma 4, for m,λn≥h and h comparable to K. This applies to all k in the stated range, independently of their occurrence as a sum difference.

Consider the sequence ωt, |t|≤N. Its number of points in any arc of length 1/D is O(N log(2D)/D). To see this use the nonnegative Fejér kernel at scale D (or ⌊D/2⌋), ≥cD across the arc centered at its test location. Its Fourier coefficients are bounded by one and supported on |k|<D. The k=0 sum is O(N), and for k≠0 the geometric progression sum is O(min(N,1/‖kω‖)). Separation of the points kω and of their distances from 0 bounds their sum by O(N log(2D)). In particular the estimate allows a polylogarithmic loss in the original height.

For any trigonometric polynomial F of degree ≤D and real q≥1,

$$
 N^{-1}\sum_{|t|\le N}|F(t\omega)|^q
 \ll_q \log(2D)\int_{\mathbb T}|F(v)|^q\,dv.\tag{2}
$$

Indeed convolution with 2K_{2D}−K_D reproduces F, where K_D is the Fejér kernel of order D. Its absolute kernel has L¹ norm at most three and size O(D(1+D‖v‖)^{-2}). Jensen with its absolute value bounds each |F(tω)|^q by an integral of |F|^q against this translated envelope. The arc count applied in intervals of size 1/D around each v gives a uniformly O(N log(2D)) sum of these envelopes by the convergent inverse-square series. This proves (2) without projecting F to a finite-group cell or substituting an auxiliary independent phase model.

The true interval in the normalized source circle has length at most 1/N since K−h≥log₂ X. An appropriate fixed translate of C K_N/N majorizes its indicator, including endpoints. Its Fourier coefficients have size O(1/N) and vanish for |t|≥N. Each admissible path in the fixed exterior contributes an actual source frequency. Summing the majorant and applying Hölder on this common integer frequency interval bounds the admissible path count by

$$
 C \prod_{l=1}^5 \left(N^{-1}\sum_{|t|\le N}|F_l(t\omega_l)|^5\right)^{1/5}
 \ll \log(2 D_{\max})\,3^{(4/3-\delta)a}.
$$

The distinct P cyclic phases give distinct original integers ≤X and therefore require at least P full words across O(b) phase-cell and bounded endpoint choices. Incorporating the exterior cost and then letting η↓0 as in the four-segment source bound gives limsup log P/log X≤(4/3−δ)/4. The facts that θ→λ and X≤4/(2^θ−3) follow from the all-terms geometric bound along a bounded-width cycle. The irrationality exponent input imposes limsup log X/log P≤3.

## Exact ternary phases and a finite criterion for (1)

Write M_i=⌊iθ+t⌋. Up to translation and integer dilation of the frequency, which preserve a Haar absolute moment, the relevant phase polynomial is

$$
 \sum_z\exp\left(2\pi i\sum_{i<a}z_i2^{M_i}3^{a-1-i}v\right).
$$

In fact 2 B(z) = 2^{z₀}Σ_i 2^{M_i}3^{a-1-i}(2−z_i). Put U_i=2^{M_i}3^{a-1-i}v mod 1 for uniform v. Then U₀ is uniform. Given the entire past up to i, U_{i+1} ranges uniformly over the three solutions of 3U_{i+1}=2^{m_i}U_i. The gcd of the first i+1 integer coefficients of v equals 3^{a-1-i}: after division their first and last entries are 3^i and 2^{M_i}. The joint observations therefore specify exactly 3^{a-1-i}v mod 1 and the next ternary digit is free. The last, unused U_a may be sampled with the same transition.

For the row amplitudes expressed as a column v=(A,C), put D(u)=diag(1,exp(2πiu)), S₁v=(A+C,C), S₂v=(A,A+C). The chronological update is v↦S_mD(U_i)v. The two cut-conditioned output polynomials are its individual components for a standard basis entrance. For any positive five-homogeneous test function H on the complex column and circle, set

$$
 (\mathcal L_m H)(u,v)=\tfrac13\sum_{3u'=2^m u}H(u',S_mD(u)v).
$$

Fix a lookahead n, one positive function H_v for each mechanical word v of length n, uniformly comparable to ‖·‖⁵ on the compact sphere. For each legal word w of length n+1 suppose

$$
 \mathcal L_{w_0}H_{w_{1:}}\le R_w H_{w_{:-1}}.\tag{3}
$$

The functions here depend on every source variable (u,v). Let I_w be the phase arc or union of arcs generating w at slope λ. If

$$
 \sum_w |I_w|\log R_w < (4/3)\log3,\tag{4}
$$

then iteration gives (1) in the joint limit. For fixed n, all allowed masks stabilize for slopes sufficiently close to λ, as the finite irrational breakpoints remain distinct. For θ→λ and arbitrary starting phase the fixed word frequencies in any length a→∞ converge uniformly to these arc lengths. For example, first verify uniform convergence of each nonzero Fourier mode by its geometric progression, then approximate the arc indicators from above and below by trigonometric polynomials. Boundary phases are covered by the same estimates.

Positive algebraic certificates for (3) may be chosen as homogeneous extensions of real polynomials in the Bloch sphere coordinates x=2Re(ĀC), y=2Im(ĀC), z=|A|²−|C|² on the unit column, and a finite Fourier series in u. Under the exact ternary sum a circle harmonic k disappears unless 3 divides k. The surviving harmonic becomes 2^m k/3. Applying the diagonal rotation to a spherical harmonic of azimuthal order s adds s to this circle frequency. The remaining maps are the two fixed real shears. For a unit vector their squared output norms are g=(3+2x±z)/2 at the rotated point. Consequently each instance of (3) is a compact real-algebraic inequality in unit-circle and sphere coordinates, using the positive root g^{1/2}. Rational coefficient witnesses and rational upper R_w admit exact verification by subdividing the domains with interval bounds or by real quantifier elimination. The scalar inequality (4) still requires certified bounds for the arc lengths and logarithms. This describes a finite family of sufficient certificate tests. It does not supply verified witnesses.

The numerical question left by (1) involves a single ordinary one-variable Haar integral. The even independent-segment obstruction proves that replacing five by four, six, or any fixed even moment cannot yield the same cubic inequality in this full unweighted family. The present true Markov law differs from the independent circle law sometimes used to estimate coordinatewise bit equality. Neither a simulation nor a finite harmonic truncation alone certifies (3)–(4).

**Primary antecedents.** Weaver 145 §§4–6 supplies the fixed-place integer separation and convolution-on-actual-segments architecture. Weaver 73/v2 and 181 supply earlier located source estimates. The full two-grade binary path representation and four-copy aggregate are discussed in the companion four-bridge note. The low-frequency cut and scalar noninteger transference (2), exact three-preimage phase dynamics, and the five-homogeneous finite super-solution criterion address the small unresolved margin for the full binary layer class. The optional consequence with μ≤3 uses Chudnovsky, arXiv:2610.28079v1, Theorem 11.1.
