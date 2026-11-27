# Critical cubic spectrum of exact physical rows

Write \(m_{j,s}(y)\) for the normalized mass of positive odd inputs first arriving at a specified odd target \(y\) after \(j\) odd departures and \(s\) native steps. It includes the empty row, and the weight of each input is \(1/p\), \(p=y2^s/3^j\). These are source-qualified deductions from the signed-source representation (6)–(7) in [the uniform first-arrival theorem](SHARP_UNIFORM_FIRST_ARRIVAL_ROWS.md) and the full escaping-component representation in [PR 195, LOCAL_HEIGHT_LAW (4)–(5)](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/LOCAL_HEIGHT_LAW.md). Their analytic inputs have not been formalized here.

## The physical clock kernel

Put \(K(j,s)=g_j(s)\), extended by zero at \(j<0\), with \(g_0=\delta_0\), \(g_j(s)=\binom{s-1}{j-1}2^{-s}{\bf1}_{s\ge j}\). This is a kernel on \(\mathbb Z^2\), with counting measure. For a function \(V\) on any countable table, define \(N_V(t)=\#\{|V|>t\}\). Then
\[
 \sup_{t>0}t^3 N_K(t)<\infty,\qquad
 \lim_{t\downarrow0}t^3N_K(t)
       =\frac23\int_{\mathbb R}\phi(z)^3\,dz=\frac1{6\pi\sqrt3},
 \quad \phi(z)=(4\pi)^{-1/2}e^{-z^2/4}.                              \tag{1}
\]
Indeed \(\|g_j\|_\infty\le C(1+j)^{-1/2}\) while \(\sum_sg_j(s)=1\). A row above threshold \(t\) requires \(j\le C't^{-2}\); summing the row masses and dividing by \(t\) gives the weak bound. For the limit, rescale \(u=t^2 j,\ v=t(s-2j)\), giving lattice cell area \(t^3\). The small range \(u<\delta\) contributes at most \(\delta+O(t^2)\) to the rescaled count by the mass bound; the range above an absolute constant is empty. On the remaining compact \(u\)-interval the local central limit theorem for independent positive geometric increments gives, uniformly in \(s\),
\(\sqrt j\,g_j(s)=\phi((s-2j)/\sqrt j)+o(1)\). This span-one kernel has mean 2, variance 2 and exponential moments; the displayed local limit also follows directly from Stirling's formula on bounded central intervals and unimodality outside. The lattice set above threshold converges in area to \(u^{-1/2}\phi(v/\sqrt u)>1\): the boundary has zero area, and sufficiently large \(|v|\) are excluded uniformly. Letting \(\delta\downarrow0\), its area is \(\int dz\int_0^{\phi(z)^2}\sqrt u\,du\), proving (1).

Every fixed lattice translate \(T_bK\) satisfies \(T_bK-K\in\ell^3\). A single spatial shift has \(\|\Delta g_j\|_1=2\|g_j\|_\infty=O(j^{-1/2})\) by unimodality and \(\|\Delta g_j\|_\infty=O(j^{-1})\) by a single Fourier difference of \(\big(e^{i\theta}/(2-e^{i\theta})\big)^j\). Thus its cubed row norm is \(O(j^{-5/2})\). A shift of one grade uses \(g_{j+1}=G*g_j\) and \(\sum_e e2^{-e}=2\), giving the same two bounds by summing \(e\) translates of the one-step difference. The finitely many end rows belong to \(\ell^3\). Iterate finitely many shifts.

For any signed \(c\in\ell^1(\mathbb Z^2)\) write \(V=c*K,\ H=\sum c\). Then
\[
 \sup_{t>0} t^3N_V(t)\ll\|c\|_1^3,\qquad
 \lim_{t\downarrow0} t^3N_V(t)=\frac{|H|^3}{6\pi\sqrt3}.              \tag{2}
\]
For the weak bound use the equivalent set norm \(\sup_{0<|A|<\infty}|A|^{-2/3}\sum_A |V|\). The layer formula gives finiteness for \(K\) from (1), and the triangle inequality and translation invariance give the factor \(\|c\|_1\). Conversely testing on a finite subset of \(\{|V|>t\}\) gives the weak bound. For the limit, truncate \(c\) to a finitely supported array with discarded sum norm at most \(\epsilon\). The retained convolution differs from its net multiple of \(K\) by an \(\ell^3\) function. For such a function \(b\), \(t^3N_b(t)\to0\) by first keeping a finite part. The omitted convolution, and its net multiple of \(K\), each have weak level coefficient \(O(\epsilon^3)\). Comparing the level sets of \(V\) and \(HK\) at thresholds \((1\pm\delta)t\), with discrepancies charged at \(\delta t\), gives (2) by taking \(\epsilon\to0\) and then \(\delta\to0\).

The corresponding cropped cubic residue for any fixed integer \(j_0\) is
\[
 \lim_{L\to\infty}\frac1{\log L}
      \sum_{j=j_0}^{j_0+L}\sum_s |(c*K)(j,s)|^3
                 =\frac{|H|^3}{4\pi\sqrt3}.                            \tag{3}
\]
In fact \(\sum_s g_j(s)^3\sim j^{-1}\int\phi^3=1/(4\pi\sqrt3\,j)\) by the local limit; the tails follow from \(\|g_j\|_\infty^2\Pr(|S_j-2j|>B\sqrt j)\ll j^{-1}/B^2\). The cubic norm of \(K\) on *any* grade window of length \(L+1\) is \(O((1+\log(2+L))^{1/3})\), since the row cube sum is at most \(C/(1+j)\) for \(j\ge0\). Applying Minkowski to each translated kernel from the \(\epsilon\)-tail of \(c\) bounds its cropped norm by \(C\epsilon(1+\log(2+L))^{1/3}\) uniformly in the positions of the omitted sources. The retained finite translates differ from their net multiple of \(K\) by a fixed \(\ell^3\) error. Divide the norm by \((\log L)^{1/3}\), take the limits and cube to obtain (3).

## Consequences for genuine ordinary rows

For each fixed \(y\), the target-stopped forcing \(c^y\) has uniformly bounded sum norm, including the exact negative primitive-lap impulse when \(y\) is periodic. Define
\(H_y=\sum_{i,t}c^y_{i,t}=\lim_{j\to\infty}\sum_s m_{j,s}(y)\ge0\). This follows by summing the finite-grade convolution and then taking \(j\to\infty\). Equations (2) and (3) give the exact level and cubic residues \(H_y^3/(6\pi\sqrt3)\) and \(H_y^3/(4\pi\sqrt3)\), respectively, for the ordinary first-arrival table at this root. Uniformly in \(y\), at most \(C t^{-3}\) of its rows have mass exceeding \(t\); all power sums above three are uniformly bounded. Positive \(H_y\) forces divergence of the cubic sum. At \(y=5\) the physical central lower of [the terminating controls](MAXIMIZING_CLASS_CONTROLS.md) gives \(H_5>0\). At a multiple of 3 there are no positive-depth odd-to-odd first arrivals, so \(H_y=0\). For all positive starts the initial halving kernel \(\sum_{a\ge0}2^{-a}\delta_{(0,a)}\) multiplies the net by 2 and the cubic coefficients by 8.

In each escaping component \(C\), reflect the signed grade \(v\) by \(j=-v\). The normalized *full* corrected-height table \(M_{C,v}(l)\) then has the same convolution with a signed source of net \(H_C>0\). The source norms are summable across all components by PR 195 (4). Consequently
\[
 \#\{(C,v,l):M_{C,v}(l)>t\}\ll t^{-3},\qquad
 \lim_{t\downarrow0} t^3\#\{(C,v,l):M_{C,v}(l)>t\}
                 =\frac{\sum_C H_C^3}{6\pi\sqrt3}.                     \tag{4}
\]
To pass to all components, apply (2) separately and sum, using the summable majorant \(C\|c^C\|_1^3\). The countable sum is zero when there is no escaping component. The formula records every class in its own original component. Its all-positive version again has a factor of 8.

## Looking at all targets at one ordinary depth

At one fixed odd depth \(n\), let \(V_n(y,s)=m_{n,s}(y)\), allowing all positive odd \(y\). Each original odd \(x\) occurs in at most one row of this table: its endpoint is \(U^nx\) and its native total is determined. A first visit is required. At an octave \(2^k\le p<2^{k+1}\) all its starts have \(c_0 2^k\le x<2^{k+1}\). Thus the sum of the row masses in an octave is \(O(1)\) independently of \(k,n\), while the maximum is \(O((1+k)^{-1/2})\) by the uniform first-arrival theorem. Rows above threshold \(t\) require \(k\ll t^{-2}\), so
\[
 \sup_n N_{V_n}(t)\ll t^{-3},\qquad
 \sup_n\sum_{\substack{y,s\\p\ge R}} V_n(y,s)^q
      \ll_q (1+\log R)^{-(q-3)/2}\quad(q>3,\ R\ge2).                  \tag{5}
\]
The second estimate sums the \(O_q((1+k)^{-(q-1)/2})\) per octave. Both statements hold for all positive sources, since the first visit to an odd target is determined by the initial halving segment and its odd source row; the simple correction bound on \(x/p\) persists.

The true first-hit count at common depth has limits at all thresholds \(t>0\) which are not masses of any positive escaping class:
\[
 \lim_{n\to\infty}N_{V_n}(t)=\#\{(C,v,l):M_{C,v}(l)>t\},\qquad
 \lim_{n\to\infty}\sum_{y,s}V_n(y,s)^q=\sum_{C,v,l}M_{C,v}(l)^q
 \quad(q>3).                                                          \tag{6}
\]
At a finite original cutoff \(x<R\), the partition into distinct eventual synchronized cells stabilizes. A periodic or eventually periodic \(x\) gives no first visit at sufficiently large \(n\); escaping sources give the same row eventually exactly when they have the same corrected height in the same component. Their contributions converge to \(1/P(x)\). For the threshold assertion the sup difference upon cropping the inputs is \(O((1+\log R)^{-1/2})\) on both sides, by the moving-target theorem and the full-class bound of PR 195. The number of positive masses exceeding \(t/2\) is finite on each side by (4) and (5), and a threshold off the limiting spectrum has a positive gap near \(t\). This proves the count limit by taking the cutoff large before \(n\). For the moments the entire difference of power sums upon cropping is bounded by the sum over rows with a removed source, hence with \(p\ge R\), in (5). The same summable octave bound holds for the full escaping array since every ordinary source belongs to at most one class. Let \(R\to\infty\). These arguments apply also to all-positive sources and their corrected table.

Thus the entire positive-mass distribution, and not only its maximum, has an ordinary finite-source horizon approximation. The positive cubic divergence at fixed terminating roots shows why there is a difference between summing all clocks at one root and summing all targets at *one common* odd depth. The [common-depth cubic law](COMMON_DEPTH_CUBIC_RESIDUE.md) computes the leading term for the latter.
