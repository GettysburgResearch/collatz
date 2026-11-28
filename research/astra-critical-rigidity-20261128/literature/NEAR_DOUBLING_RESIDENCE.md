# Residence of an actual positive orbit in a band slightly wider than a factor of two

Let \(S(x)=(3x+1)/2^{v_2(3x+1)}\) on odd positive integers and \(\gamma=\log_2 3\). For a real floor \(M\ge2\) and relative width \(2\le R<4\), use the closed band \([M,RM]\). We count distinct positive starts and chronological segments, allowing both endpoints of the band. Put
\[
 n=\lceil\log_3(16M+1)\rceil,\quad w=\log_2(R/2),\quad
 s=w+\frac{n}{3M\ln2}.
\]
For \(s<1\) write \(Q_n(s)\) for the largest number of the dates \(i=1,\dots,n\) whose circle phases \(\{i\gamma\}\) lie in a single closed arc of length \(s\). The following source count is effective with an absolute constant \(C\):
\[
 \#\{x\text{ positive odd}: S^i(x)\in[M,RM]\ (0\le i\le n)\}
                       \ \le C(n+1)2^{Q_n(s)}.                           \tag{1}
\]
Consequently every chronological segment of distinct odd states confined to that band has length at most \(n+C(n+1)2^{Q_n(s)}\), counting states. For a finite trajectory with distinct states which makes several visits, its total number of in-band dates is at most the same quantity plus \(n\) times its number of observed exits from the band. No conclusion about the direction of an exit is needed.

The condition on the rotation has an explicit inverse. If \(Q=Q_n(s)>2ns+2\), there is an integer \(1\le b\le n/(Q-1)\) with
\[
                         \|b\gamma\|\le s/(Q-1).                          \tag{2}
\]
In particular, for a proposed long confined run, (1) lower bounds \(Q\); equation (2) then tests a specific finite range of possible integer clocks. Both displays are independent of any claimed recent improvement in logarithm bounds.

Assume the [October 2026 rational log-ratio theorem](CHUDNOVSKY_LOGARITHM_IMPORT.md), which gives \(\mu(\gamma)\le3\). For each \(\eta>0\),
\[
          Q_n(s)\le 2+2ns+C_\eta(n^{2+\eta}s)^{1/(3+\eta)}.              \tag{3}
\]
Hence every nonrepeating positive odd segment in a band with \(R-2=O((\log M)^{-2-\eta})\) exits within \(O_\eta(\log M)\) odd dates, where the onset may also depend on the width constant. More generally, (1) and (3) give explicit powers inside the exponential when \(R-2\) is an inverse power of \(\log M\). If \(R-2\to0\) at *any* rate, every such residence is \(M^{o(1)}\) even without the exponent-three input. On each sequence where \(n\) is between a convergent denominator of \(\gamma\) and a fixed multiple of it, (1) gives \(O(\log M)\) residence already when \(R-2=O(1/\log M)\), independently of the irrationality exponent. All conclusions are on individual actual orbit segments. A repeated odd state is the alternative to exit for a segment to which distinctness has not been imposed.

## Counting legal cumulative divisions

Fix an eligible source and set \(x_i=S^i(x)\), \(a_i=v_2(3x_{i-1}+1)\), \(A_i=\sum_{j=1}^i a_j\). Put \(z=\log_2(x/M)\). The exact identity
\[
 \log_2(x_i/M)=z+i\gamma-A_i+E_i,\qquad
 E_i=\sum_{j=0}^{i-1}\log_2(1+1/(3x_j))\in[0,n/(3M\ln2)]
                                                                            \tag{4}
\]
shows that \(A_i\) is an integer in \([z+i\gamma-1-w,z+i\gamma+n/(3M\ln2)]\). Each such interval has length \(1+s<2\). With \(t=z+n/(3M\ln2)\), its integer options are \(W_i=\lfloor t+i\gamma\rfloor\) and, only when \(\{t+i\gamma\}\le s\), also \(W_i-1\). Requiring all \(a_i\ge1\) can only reduce this count. Thus for a fixed phase there are at most \(2^{Q_n(s)}\) cumulative-division words. As \(z\) ranges over \([0,1+w]\), these lists change only when \(t+i\gamma\) or \(t+i\gamma-s\) is integral. These \(O(n)\) points and the open intervals between them give \(O(n+1)\) phase cases, including ties. This proves the asserted bound for the words.

From (4) at the endpoint, \(2^{A_n}\ge3^n/R>4M\). A fixed observed word admits at most one original integer in this band: subtract its two affine endpoint formulas to obtain \(2^{A_n}(x_n-y_n)=3^n(x-y)\). Thus \(2^{A_n}\mid x-y\), larger than the possible absolute difference. This proves (1). All but the last \(n\) dates of a confined segment start an eligible word. In a segment with exits, an additional initial in-band date whose next \(n\) dates include an exit is charged to the first such exit, which receives at most \(n\) charges.

For (2) lift all arc hits to \((i,i\gamma-r_i)\) for suitable integers \(r_i\), so they lie in one rectangle of width \(n\) and height \(s\). These points are a determinant-one linear image, up to sign, of integer lattice points. If they are noncollinear, one can triangulate their convex hull using all \(Q\) points, with at least \(Q-2\) nondegenerate triangles. For instance start with the hull triangulation and insert each additional point, splitting a face or boundary edge as necessary. Every nonzero triangle has area at least \(1/2\); the rectangle has area \(ns\). Otherwise all hits lie on a primitive line of the integer lattice before the linear map. Its integer direction \((b,r)\) can be chosen with \(b>0\) since dates differ. The first and last hits differ by at least \(Q-1\) copies of that vector. Their horizontal and vertical distances yield (2).

For each fixed \(\eta>0\) the log-ratio input supplies \(\|b\gamma\|\ge c_\eta b^{-2-\eta}\) for all \(b\ge1\). On the collinear branch of (2),
\((Q-1)^{3+\eta}\le n^{2+\eta}s/c_\eta\), proving (3). For the logarithmic-width claim use (3) with any smaller positive loss than the one in the assumed width. Arc occupancy is \(o(n)\) whenever \(s\to0\), simply by uniform distribution of an irrational rotation and domination by finitely many fixed small arcs. Finally, over a block of a convergent denominator \(b\) the points \(i\gamma\) differ by at most \(1/b\) from a shifted uniform grid, using \(|\gamma-a/b|<1/b^2\). A fixed number of such blocks covers \(n\le Cb\) dates, hence \(Q_n(O(1/n))=O_C(1)\).

Weaver's November 24 Paper 222 gives an exact mechanical-word characterization at factor two. The logarithmic residence bound in the factor-two band was already public before that paper. Weaver's Paper 145, Theorem 6, bounds confined residence at any fixed width below four by \(O(M^{0.433398})\), with the stronger formulation for any exponent greater than \(0.4333973955\ldots\), and handles multiple visits by paying per exit. The moving-width estimates (1)–(3) here retain the small overrun above two and its exact rotation obstruction. The [fixed-width population count](CONFINED_SOURCE_ENTROPY.md) gives matching source exponents at shorter deadlines. These bounds do not exclude an ordinary orbit leaving one band and entering another. [Weaver 222](https://rstation.ai/problems/collatz/papers/222/v1) · [Weaver 145, Section 11.3](https://rstation.ai/problems/collatz/papers/145/v1)
