# Atomic eigenmeasures of the inverse shortcut operator

**PROPOSED written theorem. Positive-integer escape and universal termination remain OPEN.**

On the ternary integers put
\[
 (L_s f)(z)=2^{-s}f(2z)+(3/2)^s
    {\bf1}_{z\equiv2\ (3)} f((2z-1)/3).
\]
For every real \(s>1\) there are continuum many mutually singular, purely atomic finite positive measures satisfying \(L_s^*\lambda=\lambda\). A single family of countable supports works simultaneously for all these exponents. Any prescribed ternary ball contains an atom of one of the measures. Their atoms can all be chosen outside the rational numbers. In particular, for \(1<s<2\) these fixed measures coexist with strict contraction of positive Haar integrals. At \(s=2\) they coexist with additive Haar probability itself as a fixed measure.

The same eigenmeasure equation would have a finite positive solution supported on the **positive ordinary integers** in the presence of an escaping ordinary orbit. Conversely any such solution has an atom with an escaping orbit. The countable fake supports here specify precisely why a spectral argument on the full ternary space cannot eliminate that case. The theorem does not exclude a second positive cycle.

## The Green measure at an ordinary target

Throughout, \(T(2n)=n\), \(T(2n+1)=3n+2\). For a legal inverse word \(w\) at \(z\), let \(z_w\) be its final state and \(g_w=3^{d(w)}/2^{k(w)}\), where \(k\) is its shortcut length and \(d\) its number of odd inverses. The empty word has weight one. Use the positive measures
\[
 G_s(z)=\sum_{w\text{ legal at }z}g_w^s\delta_{z_w},\qquad H_s(z)=G_s(z)(\mathbb Z_3).
\]
All unrestricted identities of positive sums are in the extended nonnegative reals. The even and odd inverse branches above are continuous on their clopen domains. With normalized additive Haar measure \(m\), change of variables gives
\[
 \int L_sf\,dm=\alpha(s)\int f\,dm,\qquad
 \alpha(s)=2^{-s}(1+3^{s-1}).
\]
Strict convexity and \(\alpha(1)=\alpha(2)=1\) give \(\alpha(s)<1\) on \((1,2)\). Hence \(M_s:=\int H_s\,dm=(1-\alpha(s))^{-1}\) there.

At every positive ordinary integer \(y\), \(H_s(y)<\infty\) for every \(s>1\). Indeed a legal word ending at an ordinary backward source \(x\) is a true shortcut history from \(x\) to \(y\), with \(g_w x\le y\) by the nonnegative affine offset. If \(y\) is nonperiodic each \(x\) appears at most once, giving \(H_s(y)\le y^s\zeta(s)\). If \(y\) is periodic with least positive return clock, the return word has at least one odd step, hence strictly positive additive offset and gain \(0<r_y<1\). For each \(x\) the first hit and successive laps give the same bound times \((1-r_y^s)^{-1}\). The source-count and cycle argument at quadratic exponent for the odd-root, odd-inverse stopping rule is prior work. [Weaver, §8.1](https://rstation.ai/problems/collatz/papers/9)

For \(1<s<2\) these arithmetic values are actual ternary Lebesgue values. Fix \(B_D(y)=y+3^D\mathbb Z_3\), \(D\ge1\). Every legal prefix ending exactly on its \(D\)-th odd inverse is shared by the entire ball and sends its normalized Haar law onto full Haar law. In coordinates the free trit tail is multiplied by the unit \(2^k\). Let \(A_{<D}(y)\) sum gains to power \(s\) of all words with fewer than \(D\) odd inverses, and let \(S_D(y)\) sum gains over the stopped prefixes. Counting a word of at least \(D\) odd inverses at its first such prefix gives
\[
 \frac1{m(B_D)}\int_{B_D}H_s\,dm=A_{<D}(y)+M_s S_D(y).
\]
Both \(S_D(y)\) and the ordinary tail \(H_s(y)-A_{<D}(y)\) tend to zero, since \(H_s(y)<\infty\). The very same bound, \(M_sS_D(y)+H_s(y)-A_{<D}(y)\), controls the conditional mean of \(|H_s-H_s(y)|\). A normalized Green residue, a stationary density at exponent one and this unnormalized subcritical Haar integral are different quantities. Valbuena already identifies the critical ordinary trace with a lower semicontinuous stationary density and proves Cesàro mean absolute approximation by cylinder densities. [Valbuena, stationary envelope and arithmetic trace](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/main/paper/positive-stationary-envelope.tex)

## A negative ordinary target controls the side branches

The integer \(-2\) goes to \(-1\), which is fixed. Consequently each negative source visiting \(-2\) has just one such clock. All sites before arrival are negative with distinct absolute values at least two. For the set \(S\) of odd input magnitudes along any such word, the exact product identity is
\[
 g_w|z_w|=2\prod_{a\in S}\frac{3a}{3a-1}
 \le 2\prod_{a\in S}\frac a{a-1}\le2(|S|+1).
\]
Ordering the \(d=|S|\) distinct magnitudes puts the \(i\)-th at least \(i+1\) for \(1\le i\le d\). The product at these initial values telescopes. Thus both the sum of all words with fewer than \(D\) odd inverses and the sum on the \(D\)-th odd-inverse stopping line at \(-2\) are bounded, each, by \([2(D+1)]^s\zeta(s)\). Each count uses genuine source distinctness within its own sum. The reflected positive-integer encoding \(x\mapsto(3x-1)/2\) on odd inputs, the uniqueness of its clock reaching 2 and its full finite-word gain inequality are formalized in [NegativeShadow.lean](NegativeShadow.lean).

The same Haar stopping identity now gives, for \(1<s<2\),
\[
 \mathbb E[H_s(U)\mid U\equiv-2\pmod{3^D}]
 \le(1+M_s)[2(D+1)]^s\zeta(s).
\]
This uses a finite-depth bound at the distinguished negative root. No assumption about the total Green value at that root is needed.

## Fixed measures from the all-odd spine

Choose \(z\) Haar-uniform in \(\mathbb Z_3\). Write \(r=3/2\), \(z_j=-1+r^j(z+1)\), including \(z_0=z\). For \(j\ge1\), \(z_j\equiv2\pmod3\), and its odd inverse is \(z_{j-1}\). The even inverse \(2z_j\) is uniform on the ball \(-2+3^j\mathbb Z_3\). The Green decomposition at the two first edges gives the exact measure equality
\[
 r^{-js}G_s(z_j)-r^{-(j-1)s}G_s(z_{j-1})
 =r^{-js}\big(\delta_{z_j}+2^{-s}G_s(2z_j)\big).
\]
One can first write this as a sum of positive measures, avoiding subtraction before finiteness is known. The sum of expected masses on the right over \(j\ge1\) is finite by the preceding polynomial bound and geometric discount. The expected initial mass is \(M_s\). Thus, almost surely, the measures on the left before differencing form an increasing family of bounded mass and converge in total variation to \(\lambda_{s,z}\). The identity
\[
 (I-L_s^*)r^{-js}G_s(z_j)=r^{-js}\delta_{z_j}
\]
follows by removing the empty word and partitioning all remaining words by their last inverse step. The right side tends to zero, and \(L_s^*\) is bounded in total variation, proving the claimed fixed-point identity. The limit dominates \(\delta_z\). It is supported on the countable union of all the inverse-word endpoints used above, even when several word endpoints coincide.

Take a countable decreasing sequence of exponents in \((1,2)\) tending to one and intersect the full-measure sets just constructed. The masses in the displayed *increment* expansion are sums of \(s\)-th powers of a single countable list of nonnegative gains, including the discounts and the even edge. Finiteness at \(u>1\) implies finiteness at every \(s\ge u\), by elementary inclusion \(\ell^u\subseteq\ell^s\). This gives the same construction for every \(s>1\), without assigning a finite Haar integral to \(H_2\). Remove the countable rational points. Every endpoint is then an affine expression \(az+b\) with rational \(a\ne0,b\), and hence is nonrational. Two distinct rational-affine equivalence classes of seeds have disjoint supports. Every nonempty ternary ball contains continuum many seeds from the full-measure set and each equivalence class is countable.

## The ordinary fixed measures

For an escaping component \(C\) the previously constructed corrected height is
\[
 P(n)=n\prod_{\substack{x\text{ odd on the}\text{ forward orbit of }n}}
             (1+1/(3x)),\qquad P(Tn)=a_n P(n),
 \quad a_n=\begin{cases}1/2& n\text{ even},\\3/2& n\text{ odd}.\end{cases}
\]
A component here means eventual intersection, with either initial clock allowed to vary. Escape means that the ordinary iterates eventually exceed every fixed bound. The values on an escaping orbit are distinct. The uniform ordinary-orbit sparsity estimate \(\#(O\cap[1,X])\ll X^\theta\), \(\theta<1\), gives \(n\le P(n)\le K n\) with an absolute \(K\) by dyadic summation. This corrected height and its cocycle are prior work. [Prior construction on the frozen project branch](https://github.com/GettysburgResearch/collatz/blob/a1379492dbaae85e0d16662b41ccc7176ab3c66e/research/astra-global-synthesis-20261124/section/proof.md)

An ordinary, finite, positive fixed measure supported on \(\mathbb N_{>0}\) is fully classified by one scalar \(d_C\ge0\) for each escaping component:
\[
 \lambda\{n\}=\begin{cases}d_C P(n)^{-s}&n\in C,\\0&n\text{ eventually periodic},\end{cases}
 \qquad \sum_C d_C\sum_{n\in C}P(n)^{-s}<\infty .
\]
Indeed, in the ordinary support the even and odd branches have disjoint ranges, and each source has its single ordinary forward parent. Consequently \(c(n)=a_n^s c(Tn)\) for the atom masses. The factor around a positive cycle is strictly below one, hence every atom in an eventually periodic component vanishes. On an escaping component \(c(n)P(n)^s\) is invariant under the true forward edge, so common forward sites make it constant. The converse follows by nonnegative summation of the unique-source equations. A single component always has finite mass since \(s>1\).

There is a stronger recognition property when a binary coordinate is retained. Apply both inverse maps componentwise on \(\mathbb Z_2\times\mathbb Z_3\), with the odd inverse still licensed by the ternary coordinate. Additional coordinates may also be carried. Write \(m_n\) for the mass of the entire binary-coordinate fiber over a positive ordinary integer \(n\). For any finite positive fixed measure,
\[
 m_n\le a_n^s m_{Tn}.
\]
Indeed the binary coordinate of an inverse output fixes which branch produced it, and its parent has binary coordinate \(Tn\). The ternary gate can discard part of the parent fiber. Put \(v(n)=m_n^{1/s}\). The exact affine identity
\[
 Tn+\tfrac12=a_n(n+\tfrac12)+\tfrac14
\]
makes \((n+1/2)v(n)\) strictly increase at every forward step out of a positive-mass fiber. Hence all forward sites there are distinct, and the projected ordinary orbit escapes. Conversely every ordinary escape produces a diagonal fixed measure by the classification. Thus the existence of a finite positive fixed measure assigning positive mass to the **eventually-zero positive binary expansions** is already equivalent to ordinary escape. No atomicity assumption on the other coordinates is needed. An independent exclusion of nontrivial positive cycles would still be required for universal termination.

## Testing positivity and all finite primes

The countermodel can carry a genuine binary parity coordinate, integral coordinates at all other primes, and a positive, locally finite real coordinate at the same time. The real atom masses then have the ordinary power-law size. The proof keeps the affine offset.

Let \(W(z)\) be the supremum, over all single legal inverse paths, of the sum of all their prefix gains (including the empty prefix). For \(1<s<2\), the sum of the expected \(s\)-powers of the gains at length \(k\) equals \(\alpha(s)^k\). The maximum at that length is bounded by the \(\ell^s\) norm of the length layer. Minkowski's inequality therefore gives
\[
 \|W\|_{L^s(m)}\le\sum_{k\ge0}\alpha(s)^{k/s}<\infty .
\]
For a uniform \(U\equiv-2\pmod{3^j}\), all prefixes with fewer than \(j\) odd inverses coincide in legality with the negative target. Their gains are at most \(2(j+1)\) by the reflected bound, and at depth \(k\) they are also at most \(3^j2^{-k}\). Summing the smaller bound over \(k\) costs \(O((j+1)^2)\). Beyond the stopping line, the maximum of \(g_w W(U_w)\) over the stopped prefixes has conditional \(L^s\) norm at most
\[
 \left(\sum_w g_w^s\right)^{1/s}\|W\|_s\ll_s j+1
\]
because each stopped endpoint is Haar and the negative-target sum estimate applies. Thus \(\mathbb E W(2z_j)\ll_s(j+1)^2\). The positive sum \(\sum_{j\ge1}r^{-j}W(2z_j)\) and \(W(z)\) are finite almost surely.

Use the real seed \(Y>0\) and real spine \(Y_j=-1+r^j(Y+1)\). For an inverse word \(v\) from a real root \(u\), its endpoint is \((u-B_v)/g_v\), where \(B_v\) is one half of the sum of the gains of the prefixes immediately before odd edges. In particular \(0\le B_v\le W/2\) on each legal branch of the corresponding tree. In the initial tree the normalized gain is \(h=g_v\) and \(hX=Y-B_v\) for its real endpoint \(X\). In the tree from the even side at stage \(j\ge1\),
\[
 h=r^{-j}g_v/2,\qquad hX=Y+1-r^{-j}(1+B_v/2).
\]
At the spine points themselves, \(h=r^{-j}\) and \(hY_j=Y+1-r^{-j}\). The normalized offset in each of these displays is uniformly bounded. The gains \(h\) are uniformly bounded as well, since their powers are summable in the increment construction. Choose \(Y\) sufficiently large that every endpoint satisfies \(X\ge1\) and \(0<c\le hX\le C<\infty\). There are only finitely many listed endpoints in each bounded real interval. With the binary coordinate included, distinct entries in this list are distinct points: each inverse output determines its forward branch by parity, the successive spine points have distinct ternary coordinates at an irrational seed, and the even side branch separates it from the preceding odd spine branch. An inverse-descendant cycle would force a nontrivial rational affine return at that same irrational ternary coordinate. Consequently each atom mass is exactly \(h^s\asymp X^{-s}\).

Give the seed binary coordinate \(-1\). Every spine point has binary coordinate \(-1\); side and descendant coordinates are obtained by the actual integral binary inverse maps, with even and odd parity resolved by the branch. At primes \(p\ge5\) use any \(p\)-integral seed, propagate the same rational-affine maps (whose denominators are units), and assign compatible spine coordinates by the forward odd branch. The increasing-measure construction and fixed equation lift term by term to this product. One may define the operator on the full real line; its fixed measure is carried by real coordinates at least one.

This simultaneously realizes the local congruence domains, the parity clock, archimedean positivity, local finiteness and summable power-law atom sizes. The binary recognition theorem identifies the unresolved arithmetic restriction. These extended examples give zero mass to every positive ordinary binary fiber.
