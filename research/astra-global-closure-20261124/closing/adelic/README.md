# Adelic continuation of the generating function of one actual orbit

Fix a positive odd integer \(q=q_0\). Write \(q_{n+1}=(3q_n+1)/2^{a_n}\), \(a_n=v_2(3q_n+1)\), \(A_0=0\), \(A_n=\sum_{i<n}a_i\), and \(F_q(z)=\sum_{n\ge0}2^{A_n}z^n\). The results below concern a hypothetical injective orbit. Determinism makes every non-eventually-periodic positive orbit injective.

**Main conclusion.** If the mean \(A_n/n\) converges on such an orbit, the entire complex convergence circle of \(F_q\) is a natural boundary. Equivalently, this applies whenever the exponential growth rate \(\lim(\log q_n)/n\) exists. It includes all uniformly subexponentially escaping candidates. Without this limit we obtain an explicit upper bound on the conformal radius of any continuation. This is a written proof using an external algebraization theorem. The nine Lean declarations at the end check finite integer identities and bounds.

## A1. Exact local data

Put \(s=\liminf A_n/n\), \(t=\limsup A_n/n\), \(\alpha=\log_2 3\), and \(u_n=2^{A_n}/3^n\). The finite affine telescope and the real Euler product are
\[
 L_n=u_nq_n=q+\frac13\sum_{i<n}u_i
     =q\prod_{i<n}\left(1+\frac{1}{3q_i}\right).
\]
The repository's fixed-orbit separated-visit theorem gives \(\sum_i1/q_i<\infty\). Hence \(L_n\to\Lambda>q\) in the reals. Also \(q_n\to\infty\), \(u_n\to0\), and \(\log q_n=n\log3-A_n\log2+O_q(1)\). In the dyadic field \(L_n\to0\) by integrality and \(A_n\ge n\). These facts and the fixed-source two-place pathology are already in PR192. [Separated visits](https://github.com/GettysburgResearch/collatz/blob/a7fd3ac9e5bff7412858df23d776bb847e9c1371/research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md) · [PR192, §1 and §6](https://github.com/GettysburgResearch/collatz/blob/d2081d1cd2410e6004eaee9f9b13c5553afaf3f4/research/astra-closure-attack-20261124/FIXED_SOURCE.md)

We have \(1\le s\le t\le\alpha\). Cauchy–Hadamard gives every Taylor radius in the normalization \(|p|_p=p^{-1}\).

| Place | Absolute value of the \(n\)-th coefficient | Radius |
| --- | --- | --- |
| \(\infty\) | \(2^{A_n}\) | \(2^{-t}\) |
| \(2\) | \(2^{-A_n}\) | \(2^s\) |
| Every odd prime \(p\) | \(1\) | \(1\) |

Thus \(\prod_vR_v=2^{s-t}\le1\). A rational dilation multiplies each radius by the reciprocal local absolute value of the dilation, whose product is one. For logarithmic rational height \(h\), \(h(2^{A_n})=A_n\log2\) and \(h(u_n)=\log\max(2^{A_n},3^n)=n\log3\) eventually. For \(n\ge1\) the orbit relation implies \(3\nmid q_n\), so the denominator of \(L_n\) in lowest terms is \(3^n\) and \(h(L_n)=n\log3+O_q(1)\).

**Two-place test for rationality.** In the reals \(F_q(1/3)=3(\Lambda-q)>0\) by absolute convergence, and in \(\mathbb Q_2\), \(F_q(1/3)=-3q\). A rational formal germ over \(\mathbb Q\) would have no pole at the positive real point, since it has a finite limit along the real radius. Its value would be the same rational number at both places, by multiplying the convergent series by a reduced polynomial denominator. This proves nonrationality on every injective orbit. Finite-to-periodic orbits have periodic gaps after a prefix and rational \(F_q\), by summing a geometric progression. For the stronger equivalence involving D-finiteness see [the companion analysis](../../analytic/README.md).

At \(t=\alpha\) the series converges uniformly on the entire closed disk \(|z|\le1/3\). The point \(z=1/3\) nevertheless admits no meromorphic continuation. Indeed, for any nonnegative-coefficient series of finite radius \(R\), analyticity at \(R\) would imply analyticity on a disk about some \(r<R\) of radius strictly greater than \(R-r\): choose \(r\) near enough to \(R\) that this disk lies in the continuation neighborhood of \(R\). Evaluating the Taylor series there at \(R+\epsilon\) and using the nonnegative binomial expansion about \(r\) then gives convergence of the original series beyond \(R\). At the critical point finiteness of the radial limit also excludes a pole. For \(t<\alpha\), \(1/3\) lies strictly inside the real convergence disk. One rational dyadic value does not imply equality of the real and dyadic values even then.

## A2. Capacity bound and a whole natural boundary

Write \(\rho(D,0)=|\phi'(0)|\) for the conformal radius, where \(\phi:\mathbb D\to D\) is a conformal isomorphism taking \(0\) to \(0\). Suppose \(D\) is a bounded simply connected conjugation-invariant domain with regular boundary, containing \(0\), on which the germ \(F_q\) has a single-valued meromorphic continuation. Then
\[
                          \rho(D,0)\le 2^{-s}.                 \tag{1}
\]
Indeed Bost and Chambert-Loir, Theorem 7.9, applies on \(X=\mathbb P^1_{\mathbb Q}\), \(P=0\). It requires an adelic tube adapted to the point, meromorphic extension on each local open, an A-analytic formal graph, and **strictly positive** capacitary Arakelov degree. Take \(D\) at infinity, open unit disks at odd primes, and an open disk of radius \(r\in 2^{\mathbb Q}\), \(r<2^s\), at 2. Definition 5.16 is satisfied, including the standard reduction tube at almost every place. The paragraph following Theorem 7.9 supplies A-analyticity directly from the integral formal coefficients. The degree on the tangent line is \(\log \rho(D,0)+\log r\): at infinity the Green function is \(-\log|\phi^{-1}(z)|=-\log|z|+\log\rho(D,0)+o(1)\), and each finite disk contributes the logarithm of its radius as in Example 7.10. If (1) fails, one can choose \(r\) with positive degree. The theorem then makes \(F_q\) rational, contradicting A1. Example 7.10 identifies its all-disk case with Borel–Dwork rationality. The zero-degree variant in Theorem 7.8 assumes prior algebraicity and further boundary conditions. [Primary paper, Definition 5.16 and Theorems 7.8–7.9](https://arxiv.org/pdf/math/0702593)

In particular, assume \(A_n/n\to s\), so the complex radius is \(R=2^{-s}\). Any meromorphic extension through any point of \(|z|=R\) allows a small open round bulge added to the convergence disk. For a nonreal point add its disjoint conjugate bulge as well, using the real Taylor coefficients to extend there. The resulting bounded simply connected domain has a regular piecewise-circular boundary and strictly contains the convergence disk. Its conformal radius at the origin is strictly greater than \(R\): compose the inclusion of the radius-\(R\) disk with the inverse Riemann map of the larger domain and use the equality case of Schwarz's lemma. This contradicts (1). When \(s<t\), (1) bounds the permitted factor of increase over the Taylor radius by \(2^{t-s}\); it gives no exclusion of all small bulges.

Classical Pólya–Carlson assumes integer Taylor coefficients at unit radius. Here rescaling the radius to one generally loses integrality, and this adelic argument accounts explicitly for the dyadic compensation. Bell and Lagarias's Collatz natural-boundary theorem concerns the indicator of the set of all backward iterates of a given state; the present coefficients depend on time along a single forward orbit. [Carlson, original paper](https://people.math.ethz.ch/~airibar/Polya_Carlson.pdf) · [Bell and Lagarias, original paper](https://www.impan.pl/shop/publication/transaction/download/product/82190)

## A3. Physical shifts and removal of the dyadic zero

For each fixed \(j\) there is a polynomial \(P_j=\sum_{i<j}2^{A_i}z^i\) with
\[
                    F_q=P_j+2^{A_j}z^jF_{q_j}.
\]
Consequently every shift carries the very same meromorphic-continuation data away from \(z=0\). For a fixed evaluation point \(1/3\), these identities express every shifted evaluation as an affine rational function of the first; they do not add independent interpolation conditions.

The natural exact removal is
\[
 G_q(z)=\frac{F_q(z)+3q}{1-3z}
       =\sum_{n\ge0}2^{A_{n+1}}q_{n+1}z^n .
\]
Its coefficient identity is the physical telescope. In \(\mathbb Q_2\) the apparent singularity at \(1/3\) is removable. In the reals \((1-3z)G_q(z)\to3\Lambda>0\) as \(z\uparrow1/3\). It is a simple pole for \(t<\alpha\). At \(t=\alpha\) its radial growth is of this same order and there is no meromorphic germ there. The coefficients equal \(3^{n+1}L_{n+1}\), and each \(q_n\) is odd. At any odd prime \(p\), two consecutive states cannot both be multiples of \(p\), by the affine step equation. Hence infinitely many coefficients are \(p\)-adic units. We obtain exactly
\[
 R_\infty(G_q)=1/3,\qquad R_2(G_q)=2^s,\qquad R_p(G_q)=1\quad(p\text{ odd}).
\]
The product is \(2^s/3\le 2^{s-t}\). Even a separate Subspace-Theorem argument granting algebraicity of \(\Lambda\) already encounters the lower bound \((\Lambda3^n-2^{A_n}q_n)/2^{A_n}=\frac13\sum_{h\ge0}u_{n+h}/u_n\ge1\). PR192 proves this bound, including the fixed-future-subtraction version, and obtains a genuine saving only under additional bounded-defect hypotheses. [PR192, §6](https://github.com/GettysburgResearch/collatz/blob/d2081d1cd2410e6004eaee9f9b13c5553afaf3f4/research/astra-closure-attack-20261124/FIXED_SOURCE.md)

## A4. A smooth critical countermodel with positive integral states on every shift

The following control retains exact integer states, positive coefficients with an odd multiplier in a fixed set of size four, the same two-place specializations, reciprocal summability, critical product of radii one, and smooth boundary values. It relaxes the single numerator carry \(+1\).

Let \(\psi(x)=(x+16)/\log(x+16)\) for \(x\ge0\), put \(A_n=\lfloor\alpha n-\psi(n)+\psi(0)\rfloor\), \(g_n=A_{n+1}-A_n\), \(u_n=2^{A_n}/3^n\). We have \(A_0=0\), \(g_n\in\{1,2\}\), since \(0<\psi'(x)=(\log(x+16)-1)/\log^2(x+16)\le1/4\), and \(u_n\asymp 2^{-\psi(n)}\). Start from any positive odd \(q_0\) and recursively take \(q_{n+1}\) to be the smallest odd integer strictly larger than \(3q_n/2^{g_n}\). Define \(d_n=2^{g_n}q_{n+1}-3q_n\). Oddness and the spacing of odd integers give \(d_n\in\{1,3,5,7\}\). For \(B(z)=\sum d_n2^{A_n}z^n\) the exact finite identity is
\[
             u_nq_n=q_0+\frac13\sum_{i<n}d_i u_i .
\]
It gives \(q_n\asymp 2^{\psi(n)}\), in particular \(\sum 1/q_n<\infty\). It also gives \(B(1/3)=-3q_0\) dyadically and a positive finite value in the reals. The tail from every \(j\), normalized by \(2^{A_j}\), satisfies the same identity with \(q_j\).

**Eventual injectivity.** If \(q_m=q_n\) with \(m>n\), the two-sided size estimate gives \(\psi(m)-\psi(n)=O(1)\) uniformly. Since \(\psi(2n)-\psi(n)\to\infty\), eventually \(m<2n\). The mean-value theorem and \(\inf_{[n,2n]}\psi'\gg1/\log n\) give \(h=m-n=O(\log n)\). On a return the affine telescope reads
\[
 (2^{A_m-A_n}-3^h)q_n=
       \sum_{0\le j<h}3^{h-1-j}2^{A_{n+j}-A_n}d_{n+j}>0 .
\]
The multiplier on the left is a positive integer, and the right side is at most \(7h4^{h-1}\). Such \(q_n\) would be at most polynomial in \(n\), contradicting \(q_n\asymp 2^{\psi(n)}\). Thus after deleting one fixed prefix there are no repeats. All the conclusions persist on the resulting injective tail.

The coefficients of \(B\) are integers, with odd bounded multipliers. Their \(p\)-adic valuations for each odd \(p\) are bounded, so the radii are \(1/3\) at infinity, \(3\) at 2 and \(1\) at every odd prime. The different values at the two places exclude rationality as in A1. The proof of A2 therefore yields the entire circle \(|z|=1/3\) as a natural boundary. At this same circle the series has uniformly convergent derivatives of *every* order, since \(\sum n^k d_nu_n<\infty\) for every \(k\).

In fact the angular boundary trace \(f(\theta)=B(e^{i\theta}/3)\) satisfies
\[
            \|f^{(k)}\|_\infty
               \le C^{k+1}\bigl[k\log(k+2)\bigr]^k\quad(k\ge1).       \tag{2}
\]
To see this, write \(d_nu_n\ll \exp(-c\psi(n))\) and sum one half of this decay, leaving the supremum of \(x^k\exp(-c\psi(x)/2)\). Its logarithmic derivative is \(k/x-c\psi'(x)/2\), which is negative for \(x\ge C_1 k\log(k+2)\) with \(C_1\) large: there \(x\psi'(x)\gg x/\log(x+16)\ge 2k/c\). On the complementary interval \(x^k\le[C_1k\log(k+2)]^k\). This proves (2), which in particular implies a bound \(C_\epsilon^{k+1}(k!)^{1+\epsilon}\) for every \(\epsilon>0\). Thus even this level of regularity at every boundary point allows a natural boundary.

A second, autonomous control uses only two positive carries. At each odd \(x\), take \(y\) to be the least odd integer strictly greater than \(3x/2\). Then \(2y=3x+d(x)\) with \(d(x)=3\) for \(x\equiv1\bmod4\) and \(d(x)=1\) otherwise. The states strictly increase and grow at least geometrically. The same argument for \(\sum d(q_n)2^nz^n\) gives positive real and negative integral dyadic values at \(1/3\), convergent reciprocals, and a full natural boundary at radius \(1/2\). Here the real specialization is strictly inside the disk.

**The missing unit carry is exact.** For any proposed word \(g_i\ge1\), define \(x_j=-\frac13\sum_{h\ge0}2^{A_{j+h}-A_j}/3^h\in\mathbb Z_2\). All \(x_j\) are odd, by the first term, and \(2^{g_j}x_{j+1}=3x_j+1\). If \(x_0\) is a positive ordinary integer then \(v_2(3x_0+1)=g_0\), its quotient is an ordinary positive odd integer, and induction reconstructs the genuine orbit. Thus coefficient purity together with that signed ordinary integer specialization already encodes the genuine-source condition. The four-carry control explains exactly which information is lost by replacing coefficient purity with estimates on coefficients, radii, heights and boundary derivatives. The outstanding arithmetic step is to exploit that exact restriction to control continuation or exclude the forced boundary behavior (and to handle oscillating mean slopes). This argument gives neither universal recurrence nor nontrivial cycle exclusion.

## Verification scope

The accompanying Std-only Lean 4.34.1 file verifies the finite physical telescope, the autonomous two-carry dynamics and its telescope, four-carry rounding for gaps 1 and 2, the splitting and bound of the affine block numerator, and the return-height estimate \(q_0\le7n4^n\) used above. The sharper displayed bound \(7n4^{n-1}\) is the direct termwise estimate, and either version suffices. The local radius identities, application of Bost–Chambert-Loir, infinite control, and smoothness are written proofs. [Lean source](OrbitTransform.lean) · [Compiler receipt](../../../../reports/astra-global-closure-20261124/closing/adelic/lean_receipt.json)

