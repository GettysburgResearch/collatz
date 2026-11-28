# Every sparse native rotation forces an exponential complete denominator

Let a primitive positive rational Collatz cycle have least odd period \(p\), common reduced denominator \(q\), and native division counts \(a_i=v_2(3y_i+q)\), where \(y_i/q\) is its odd state. Thus \(y_i\) are distinct positive odd integers, \(q\) is prime to six, and \(2^{a_i}y_{i+1}=3y_i+q\). For a proper lag \(0<r<p\) write
\[
                 m(r)=\#\{i\bmod p:a_i\ne a_{i+r}\}.
\]
**Theorem.** For each fixed nonnegative integer \(s\) there exist \(c_s>0\) and \(p_s\) such that every such cycle with \(p\ge p_s\) and \(\min_r m(r)\le s\) has \(q\ge 2^{c_s p}\). In particular, along hypothetical ordinary integer cycles of increasing least odd period, the native mismatch count tends to infinity uniformly over every proper rotation. The constants here are ineffective. No upper bound on the largest native division, width, or number of low points is imposed.

The local statement responsible for the long lags also applies without closure. In a positive native path over an odd denominator \(q\) prime to three, suppose the \(2r\) departures \(y_0,\ldots,y_{2r-1}\) are distinct odd integers and its adjacent length-\(r\) division words differ at most \(s\) times. Then \(\log_2(y_0+q)\ge c'_s r\) for all sufficiently large \(r\), with \(c'_s>0\). The terminal \(y_{2r}\) may equal an earlier state. All denominators in the cyclic theorem are the actual complete reduced denominator. The finite-path assertion uses the supplied denominator.

Santiago Armstrong posed the native-rotation growth problem with an explicit diverging lower function. Wren distinguishes it from his shortcut-clock theorem. The conclusion here gives qualitative divergence and exponential complete-denominator growth at each fixed cutoff. PR212 obtained an explicit exponential complete-denominator bound at up to six native mismatches, an eight-mismatch conclusion with a near-circuit hypothesis, and an unbounded-order ordinary-cycle exclusion using Weaver's finite-descent theorem. Its bounded-order question above six mismatches explicitly remained open in those sources. The present proof compares adjacent native words and uses fixed rational forms at \(2,3,\infty\). Its flexible terminal dates and grouping by effective ternary start phase accommodate any fixed number of defects. [Armstrong, original rotation-distance question](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/questions/rotation-distance-growth.md) · [Wren, Paper 218/v3, §7](https://rstation.ai/problems/collatz/papers/218) · [PR212, native rotation complexity](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/ODD_ROTATION_COMPLEXITY.md) · [PR212, six mismatches](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/ROTATION_DENOMINATORS.md) · [PR212, eight near-circuit mismatches](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/MISMATCH_CHAINS.md)

## 1. The actual finite path

Suppose the local theorem fails. Take \(r\to\infty\) with \(s\) fixed and \(\log_2(y_0+q)=o(r)\). Put \(\beta=\log_2(3/2)\), \(\gamma=\log_2 3\), \(S_t=\sum_{i<t}a_i\), \(B_t=2^{S_t}3^{-t}\), and \(H_t=B_ty_t\). We have
\[
  y_t+q\le (3/2)^t(y_0+q),\qquad
  H_b-H_a=(q/3)\sum_{a\le i<b}B_i,\qquad
  B_i/B_b\le (3/2)^{b-i}\quad(0\le i\le b).                         \tag{1}
\]
All numerator logs are \(O(r)\). In fact \(S_{2r}=O_s(r)\). Partition \([0,r)\) into at most \(s+1\) matching runs and at most \(s\) individual mismatches. On a matching run \([b,c)\), subtract the two native affine iterates to get
\[
  2^{S_c-S_b}(y_c-y_{c+r})=3^{c-b}(y_b-y_{b+r}).                     \tag{2}
\]
The distinct sources imply \(2^{S_c-S_b}\le |y_b-y_{b+r}|\), even if \(c=r\). At unmatched steps both individual exponents are bounded by \(\log_2(3\max_i y_i+q)=O(r)\). This proves the halving bound, with no extra clock hypothesis. For every \(t>0\), \(y_t\) is prime to three by the preceding step.

For definiteness place the counterexample sequences in the field \(\mathcal K=\mathbb Q^{\mathbb N}/\mathcal U\), for any nonprincipal ultrafilter \(\mathcal U\). Equality means equality on a set belonging to \(\mathcal U\); a finite partition has exactly one part belonging to it. Write \(\lim_{\mathcal U}\) for the limit of a bounded real sequence in this sense. The elements represented by rational sequences of logarithmic height \(O(r)\), together with zero, form a subfield. On its nonzero elements put
\[
                     \nu(z)=\lim_{\mathcal U} v_3(z)/r.                 \tag{3}
\]
The limit exists since the normalized valuations are bounded, after disregarding sets outside \(\mathcal U\). Valuations add under multiplication and obey the ultrametric inequality under addition, with equality at distinct values. In particular a finite family with pairwise distinct \(\nu\)-values is rationally independent. All path coordinates used below have logarithmic height \(O_s(r)\) by (1) and the halving bound. One could instead successively stabilize the countable rational expressions on a diagonal subsequence.

## 2. Recovering a full unit of ternary gain

Stabilize the number of matching runs in the first half. Write \([b_j,c_j)\) for them, with \(0\le b_j<c_j\le r\). Discard those of length \(o(r)\) in the ultralimit. Define the real endpoints \(b_j^*=\lim_{\mathcal U}b_j/r\), \(c_j^*=\lim_{\mathcal U}c_j/r\), and the nonnegative
\[
             e_j=\lim_{\mathcal U}v_3(y_{b_j}-y_{b_j+r})/r.
\]
These are finite because the nonzero integer differences have logarithmic size \(O(r)\). At any \(b_j\le t\le c_j\), (2) gives the exact ternary gain
\[
             v_3(y_t-y_{t+r})=v_3(y_{b_j}-y_{b_j+r})+t-b_j.             \tag{4}
\]
On the unit circle \(\mathbb R/\mathbb Z\) enlarge each positive limiting run to the projected oriented interval \([b_j^*-e_j,c_j^*]\). It contains \([b_j^*,c_j^*]\). These ordinary limiting runs cover the circle, since all mismatches and discarded runs have total normalized length zero and there are only boundedly many intervals. Group enlarged intervals by their starting point modulo one. Within a group the projections are nested by length, including lengths at least one, and an interval of maximal length covers the group. Select one representative per group. If there are \(k\) representatives with lengths \(d_j=c_j^*-b_j^*+e_j\), then
\[
                      \sum_{j=1}^k d_j\ge 1.                           \tag{5}
\]
Indeed their projections cover the circle and each projected length is at most its unprojected length. This step allows some initial differences to be divisible by a macroscopic power of three. No genericity of the mismatch sites or jump sizes is needed.

Fix a small \(\epsilon>0\), eventually satisfying \(\gamma(1-\epsilon)>2\beta\). For each representative choose \(\tau_j\) strictly inside \((b_j^*,c_j^*)\) and sufficiently close to \(c_j^*\) that \(\sum_j(c_j^*-\tau_j)<\epsilon\). Require all \(-\tau_j\bmod1\) to be distinct and disjoint from all the classes \(-b_j^*+e_j\bmod1\). Finitely many excluded points leave such choices. Let \(t_j=\lfloor \tau_jr\rfloor\). These dates lie strictly inside the selected actual runs on a set in \(\mathcal U\). In particular \(0<t_j<r\), and \(t_j+r<2r\). Define
\[
 \lambda_j=B_{t_j+r}/B_{t_j}=2^{u_j}3^{-r},\qquad u_j=S_{t_j+r}-S_{t_j}=O_s(r),\qquad
 D_j=H_{t_j}-\lambda_j^{-1}H_{t_j+r}=B_{t_j}(y_{t_j}-y_{t_j+r}).
\]
For \(g_j=v_3(y_{t_j}-y_{t_j+r})\), (4) and (5) yield
\[
       \lim_{\mathcal U}\sum_jg_j/r>1-\epsilon,\qquad
       \nu(H_{t_j})=-\tau_j,\qquad \nu(D_j)=-b_j^*+e_j.               \tag{6}
\]
The \(2k\) displayed valuation classes are pairwise distinct modulo one.

## 3. The coefficient field has integral normalized ternary valuation

Let \(F=\mathbb Q(\lambda_1,\ldots,\lambda_k)\subset\mathcal K\). Every nonzero \(f\in F\) satisfies \(\nu(f)\in\mathbb Z\). Moreover, monomials in the \(\lambda_j\) whose ratios are nonconstant in \(\mathcal K\) are linearly independent over \(\mathbb Q\), provided all distinct pairs have nonconstant ratio.

To prove these assertions, a Laurent polynomial is a finite rational linear combination of \(2^d3^{mr}\) with integer \(m\) fixed termwise and \(d=O(r)\). Combine globally proportional monomials and discard zero coefficients. Within each fixed \(m\), the differences of the remaining dyadic exponents have absolute values tending to infinity in \(\mathcal U\): any bounded integer difference on a set in \(\mathcal U\) would be fixed there. Order them. The largest dyadic monomial dominates every smaller one in the real absolute value, so these monomials are linearly independent over \(\mathbb Q\) in \(\mathcal K\).

We claim a nonzero sum \(V=\sum_i b_i2^{d_i}\) of such distinct terms satisfies \(\nu(V)=0\). Its valuation is bounded below by \(\min_i v_3(b_i)\). If its normalized valuation were positive, apply the fixed-place Subspace Theorem to the vector \((2^{d_i})_i\), taking at three its sum with coefficients \(b_i\) in place of one of the coordinate forms, and the coordinate forms everywhere else in \(S=\{2,3,\infty\}\). The replaced coefficient is nonzero. All coordinates are \(S\)-units and three-adic units, so the product of all local forms is \(3^{-v_3(V)}\). The projective logarithmic height is \(O(r)\). When there is more than one coordinate, a fixed rational relation on a set in \(\mathcal U\) follows from the finite exceptional subspaces. This contradicts the real independence. One coordinate has constant valuation directly. Therefore each nonempty fixed-\(m\) group, including its \(3^{mr}\) factor, has \(\nu=m\). Distinct such values cannot cancel. The entire polynomial has integral normalized valuation, ratios give the assertion for \(F\), and the same argument gives the monomial independence just claimed. This uses no uniform-in-dimension estimate.

By (6), multiplying any of \(H_{t_j},D_j\) by a nonzero element of \(F\) preserves its normalized valuation class modulo one. The least valuation of any nontrivial \(F\)-linear combination of these \(2k\) coordinates therefore occurs only once. They are independent over \(F\). Replacing each \(D_j\) by \(H_{t_j+r}=\lambda_j(H_{t_j}-D_j)\) is invertible over \(F\). Hence all \(2k\) true endpoint coordinates are independent over \(F\).

## 4. One fixed-dimensional Subspace Theorem contradiction

In the multiplicative group of \(\mathcal K\), take the images of the \(\lambda_j\) modulo \(\mathbb Q^*\). They generate a finitely generated torsion-free abelian group. Indeed, a positive rational sequence whose fixed positive power is a fixed rational on a set in \(\mathcal U\) takes the same positive rational value there. Choose a basis and lift it to monomials \(g_1,\ldots,g_d\) in the generators and their inverses. Write \(g^n=\prod_i g_i^{n_i}\), and write \(\lambda_j=c_jg^{v_j}\) with \(c_j\in\mathbb Q^*\) fixed and \(v_j\in\mathbb Z^d\) fixed. Each \(c_j\) is an \(S\)-unit; a fixed factor in the estimates below would also suffice. The rank is positive since \(v_3(\lambda_j)=-r\).

Take a box \(E=\{0,\ldots,N-1\}^d\) of cardinality \(M\). For each \(j\), the fraction of \(n\in E\) with \(n+v_j\in E\) tends to one as \(N\to\infty\), since \(d,v_j\) are fixed. Fix a small \(\delta>0\) with \(\gamma(1-\delta)(1-\epsilon)>2\beta\); fix \(N\) so these fractions are all at least \(1-\delta\). The vector for the theorem consists of
\[
        Z_{n,l}=g^n H_l,\quad n\in E,\qquad
        l\in \mathcal T=\{t_1,\ldots,t_k,t_1+r,\ldots,t_k+r\}.
\]
The coordinate labels use the fixed chronological ordering of the limiting \(\tau_j\), followed by the same ordering shifted by \(r\). These are \(S\)-integers of projective logarithmic height \(O_{s,E}(r)\). Every coordinate is a fixed product of finitely many \(S\)-units of logarithmic height \(O_s(r)\) with one such endpoint. They are rationally independent as sequences. Indeed, group a putative rational relation by endpoint label. The coefficients of the \(H_l\) are in \(F\), so each must vanish by their independence over \(F\). The distinct box monomials have nonconstant ratios by the lattice basis; their rational independence from Section 3 forces every rational coefficient to vanish.

Use all coordinate forms at two. At infinity, for each \(n\) keep its first chronological coordinate and replace every subsequent coordinate by its difference with its immediate predecessor **among the selected dates for that same \(n\)**. At three, for each \(j\) and each \(n,n+v_j\in E\), replace the coordinate \(Z_{n,t_j+r}\) by
\[
                      Z_{n,t_j+r}-c_j Z_{n+v_j,t_j}.
\]
This equals \(g^n B_{t_j+r}(y_{t_j+r}-y_{t_j})\). Distinct replacements delete distinct upper labels, involving only themselves and retained lower labels. Thus the forms at three are independent. Chronological differencing at infinity is triangular and invertible. Every form at every place is fixed over \(\mathbb Q\) before applying the theorem.

First use the chronological forms at infinity and coordinates at two and three. For each fixed \(n\), the factors \(g^n\) across the three places cancel by the product formula. If \(l_1<\cdots<l_{2k}\) are the selected dates, the remaining local product in that row is exactly
\[
 y_{l_1}\prod_{i=2}^{2k}\frac{H_{l_i}-H_{l_{i-1}}}{B_{l_i}}.
\]
Indeed \(B_l\) is an \(S\)-unit and all selected \(y_l\) are prime to six. By (1) this is at most
\[
       (y_0+q)(2rq)^{2k-1}(3/2)^{l_{2k}}\le 2^{2\beta r+o(r)}.
\]
The bound on each factor uses \(B_t/B_{l_i}\le(3/2)^{l_i-t}\) independently of the sizes of the divisions. The chronological gaps sum to the last date. At three each indicated replacement gives an additional factor \(3^{-g_j}\), because the replaced upper numerator is a three-adic unit. In total the logarithm to base two of the product of all local forms is at most
\[
            M\left(2\beta r+o(r)-\gamma(1-\delta)\sum_j g_j\right).
\]
By (6) and the choices above it is \(\le-\eta r\) on a set in \(\mathcal U\), for a fixed \(\eta>0\). In view of the projective height bound, the fixed rational \(S\)-integer Subspace Theorem puts the numerical vectors in finitely many proper rational subspaces. At least one subspace contains the vectors on a set in \(\mathcal U\). This is a nontrivial rational relation in \(\mathcal K\), contradicting the independence already proved. This completes the local theorem. All dimensions, rational coefficients, basis representatives and box sizes are fixed when that application is made; the coefficient field serves only to establish independence of the fixed finite list of sequences.

The precise external Diophantine input is the usual fixed-place, fixed-form Subspace Theorem for \(S\)-integers, stated with the projective height in Weaver §2 and in Bilu's original survey formulation. Weaver §§5–8 also use a field of monomial sequences and many translates of a basis. Here normalized ternary valuations, movable native endpoint dates, the circle-cover argument and the chronological real product supply the necessary independence and savings. [Bilu, Theorems 2.3 and 2.3′](https://www.numdam.org/item/AST_2008__317__1_0.pdf) · [Weaver, Paper 173/v1, §§2, 5–8](https://rstation.ai/problems/collatz/papers/173)

## 5. The complete denominator along every proper rotation

If the cyclic assertion fails, there is a sequence of primitive positive rational cycles with \(p\to\infty\), a lag with at most \(s\) mismatches, and \(\log_2 q=o(p)\). Reverse the lag if necessary so \(1\le r\le p/2\), preserving the count. Start chronology at a minimum real odd state \(m=y_0/q\). Then \(\log_2(y_0+q)=o(p)\). For the last assertion, the positive lap gives \(0<A-p\gamma\le p\log_2(1+1/(3m))\), where \(A=\sum a_i\). For \(A\ge2p\) this implies \(m\le1\). Otherwise the usual lower bound for a nonzero form in the fixed logarithms of two and three gives \(A-p\gamma\gg p^{-B}\) for an absolute \(B\), hence \(m\ll p^{B+1}\). The denominator is common because each odd native iterate has a power of two in the new denominator before reduction, which cancels at the prescribed exponent; any denominator prime other than two that disappears cannot reappear, so all reduced denominators on a cycle coincide. A factor of three in the reduced denominator cannot survive a complete lap; equivalently the full denominator divides \(2^A-3^p\), prime to six. [Bondareva–Luchin–Salikhov, Theorem 1](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)

Pass to a subsequence with \(r/p\) convergent. If its limit is positive, apply the local result to the first \(2r\) departures at the minimum. They are distinct because \(2r\le p\), and the adjacent words have at most \(s\) mismatches, giving the contradiction directly.

If \(r=o(p)\), put \(P=\max(1,r,\lceil\log_2(y_0+q)\rceil)\), so \(P=o(p)\). Take \(s+1\) successive disjoint half-open integer intervals with endpoints
\[
       u_j=\left\lfloor P\bigl(p/(2P)\bigr)^{j/(s+1)}\right\rfloor,
       \qquad j=0,\ldots,s+1.
\]
Their consecutive endpoint ratios tend to infinity. On at least one interval \([u,v)\) there is no discrepancy \(a_i\ne a_{i+r}\). The word on \([u,v)\) has period \(r\). Choose \(R=r\lfloor (v-u)/(2r)\rfloor\), so \(R\asymp v\), \(u=o(R)\), \(r=o(v)\). Its two adjacent length-\(R\) words starting at \(u,u+R\) agree exactly. Equation (2) gives \(2^R\le |y_{u+R}-y_u|\) by integrality and distinctness. But (1) bounds both source heights by \((3/2)^R(y_u+q)\), with \(\log_2(y_u+q)\le\beta u+\log_2(y_0+q)=o(R)\). Since \(\beta<1\) this contradicts the same lower bound. This small-lag argument also imposes no condition on \(p/\gcd(p,r)\). The two cases finish the cyclic theorem.

The theorem leaves open cycles in which all native rotations have unbounded mismatch count. It gives no explicit rate of mismatch growth when \(q=1\).

The [coefficient refinement](NATIVE_ROTATION_COEFFICIENT.md) retains the height terms in the same product and gives the explicit lower limiting coefficient `log₂(4/3)/(8(s+1)16^(s+1))` for `log₂ q / p`. Its period threshold remains ineffective. Thus the coefficient can be specified while Armstrong's effective diverging mismatch-rate question remains open.

This proves the qualitative finiteness assertion in Armstrong's separately stated [rotation-distance-finite-exceptions question](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/questions/rotation-distance-finite-exceptions.md): for each fixed mismatch bound there are only finitely many positive integer cycles satisfying it. Indeed the theorem bounds their period, and the same minimum-height estimate bounds the least integer state at each bounded period. A deterministic cycle is fixed by that state. Root retrieved the complete pinned question and its related mismatch-chain criterion; the question expressly accepts an ineffective proof. This is distinct from the explicit-rate question cited above.

## Independent reconstruction and finite verification

Root and the ordinary-source agent separately reconstructed the complete written argument. The [independent review](../../../reports/astra-global-rigidity-20261128/checkpoint13/native-rotation-independent-review.md) identifies the original manuscript hash; the subsequent manuscript changes correct attribution and add this verification boundary. This is internal written review, not external peer review or full formalization.

[NativeRotationCover.lean](NativeRotationCover.lean) proves five finite roots: congruent-start arc nesting, the projection cardinality bound, attainment of each grouped maximum, the grouped representative-cover inequality, and the exact dyadic/ternary cofactor transport. The [finite checker](check_native_rotation_separation.py) replays actual positive rational paths and the full local-form product at all three places, together with circle covers having coincident effective starts. The sequence field, the two Subspace Theorem applications, the asymptotic extraction and the two-logarithm minimum bound are written mathematics and are not formalized by those roots.
