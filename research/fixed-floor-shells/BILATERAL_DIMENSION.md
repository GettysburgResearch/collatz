# Unlimited reverse competitors preserve the critical source exponent

**PROPOSED.** Let \(B_n\) be the positive odd sources \(x\) for which no smaller odd integer reaches \(U^n(x)\), however long its incoming path. This protects all earlier forward targets as well. Write \(b_n\) for the relative odd natural density of \(B_n\), and let \(E_\infty\) be the set of joint dyadic and ternary inputs resisting every smaller affine competitor at every forward time, with slope ties resolved by the constant term. The [bilateral minimum theorem](BILATERAL_MINIMUM.md) gives these definitions and the ordinary density transfer. Then
\[
 \begin{split}
 \dim_{\rm H}(\operatorname{proj}_2 E_\infty)&=h=H_2(\log_3 2),\\
 \lim_{n\to\infty}n^{-1}\log b_n&=-(1-h)\log3.                 \tag{1}
 \end{split}
\]
The projection is in the odd dyadic integers. The clock in the second formula counts odd steps. The exponent agrees with that of forward homogeneous no-descent alone. Formula (1) leaves open the subexponential factor and whether the dyadic projection contains a positive ordinary integer.

## A range of growing forward laws

For \(\lambda>0\) put \(p_\lambda(a)=(2^\lambda-1)2^{-\lambda a}\) on positive integers. Let \(b=2^\lambda/(2^\lambda-1)\) be its mean and let \(\lambda_c\) be the unique parameter with \(b=\log_2 3\). Take \(\lambda_c<\lambda<2\). Under iid forward labels of this law and an independent Haar ternary origin,
\[
                        \Pr_\lambda(E_\infty)>0.                \tag{2}
\]
The endpoint \(\lambda=2\) and its exact probability are in the [renewal identity](BILATERAL_MINIMUM.md). Use natural logarithms below and set
\[
 s=\log3-b\log2,quad H=-\sum_a p_\lambda(a)\log p_\lambda(a),\quad
 I=\log3-H=\lambda s+\kappa,quad
 \kappa=\log(2^\lambda-1)-(\lambda-1)\log3 .
\]
Here \(s,\kappa>0\). Indeed \(\kappa=0\) at 1 and 2, and \(\log(2^\lambda-1)\) is strictly concave. Also \(\lambda_c>1\). Put \(\psi=b\log2-H=I-s\), so that \(\psi-\kappa=(\lambda-1)s>0\).

### Target cylinders at the prescribed depth

At depth \(n\), require inverse words with total \(A=\lfloor bn\rfloor\). Write their integer numerator and legality equation in inverse letter order as
\[
 C_n=\sum_{i=1}^n3^{i-1}2^{A-A_i},\qquad 2^At\equiv C_n \pmod{3^n}.
\]
Retain only words for which each suffix of length \(d\ge K\) has total at most \((b+\epsilon)d\), with \(b+\epsilon<\log_2 3\). For sufficiently large fixed \(K\) this retains a fixed positive proportion of the words at the given total. Indeed the fixed-total conditional law of \(p_\lambda\) is uniform. Its probability of that total is \(\asymp n^{-1/2}\) by the negative-binomial formula. The unconditional bad-suffix probability is at most \(e^{-c_\epsilon d}\). Conditioning costs a bounded factor for \(d\le n/2\) by the local upper bound \(O((n-d)^{-1/2})\) on the complementary sum. For \(d>n/2\) it costs at most \(O(\sqrt n)\). Summing establishes the claim.

These words have \(C_n\le D3^n\) for a constant \(D\): sum the geometric bound \(2^{(b+\epsilon)d}/3^{d+1}\) for large suffixes, and use the length-\(K\) bound for the shorter ones. Distinct words at fixed total have distinct numerators. The recursion \(C_j-3^{j-1}=2^{a_j}C_{j-1}\) with odd \(C_{j-1}\) recovers the last \(n-1\) letters and the total recovers the first. Thus at most \(D+1\) retained words can occupy any one target residue. Let \(G_n\) be the union of their ternary cylinders. For Haar probability \(m\),
\[
              m(G_n)\gg e^{-In}/\sqrt n.                         \tag{3}
\]
This construction adapts the [least-predecessor cylinder count](../critical-orbit-mellin/MINIMUM_SHARP.md). The following longer suffix test is needed when the drift approaches zero.

Uniformly on *every* residue \(D_r\) modulo \(3^r\), for \(0\le r<n\), one has
\[
       m(G_n\mid D_r)\ll \exp[-(\psi-\delta)(n-r)],             \tag{4}
\]
where \(\delta\) can be chosen strictly smaller than \(\psi-\kappa\) by decreasing \(\epsilon>0\). In fact all eligible numerators in this cylinder lie in one progression modulo \(3^r\) of length \(O(3^{n-r})\). Put \(d=\min(n-r,n-1)\). Whether one can decode the last \(d\) letters with total at most \(\lfloor(b+\epsilon)d\rfloor\) depends on the numerator modulo \(2^{1+\lfloor(b+\epsilon)d\rfloor}\). For a uniform odd dyadic numerator the successive decoded exponents are independent geometric variables of law \(2^{-a}\), since subtracting the fixed odd term and stripping the exact power of two leaves a uniform odd quotient. At \(b<2\) the lower-tail Chernoff rate under this law equals \(b\log2-H=\psi\), by exponential tilting to the mean-\(b\) geometric distribution. The rate at \(b+\epsilon\) is continuous in \(\epsilon\). The binary modulus is \(O(3^{n-r})\), so each accepted binary residue costs at most \(O(3^{n-r}/2^{1+\lfloor(b+\epsilon)d\rfloor})\) progression terms. Dividing by \(3^{n-r}\) proves (4), with bounded \(d<K\) absorbed into its constant.

### How far away can the winning word be?

Write \(S_r=r\log3-A_r\log2\). Counting all competitors at a fixed depth \(r\) above a multiplier threshold gives
\[
   \sum_{|v|=r}3^{-r}\mathbf1_{\{S_r(v)\ge u\}}
          \ll \frac{e^{-\lambda u-\kappa r}}{\sqrt{r+1}}.       \tag{5}
\]
Indeed \(3^{-r}=p_\lambda(v)e^{-\lambda S_r(v)-\kappa r}\). The largest atom of a sum of \(r\) geometric variables is \(O(1/\sqrt{r+1})\). Under the exponential remainder in (5) the contributions from successive admissible lattice points sum geometrically.

Every target of \(G_n\) has \(\log M\ge sn\). For \(r<n-L\), apply (4) inside each competitor cylinder of (5) with \(u=sn\). The terms are bounded by
\[
 C e^{-In}(r+1)^{-1/2}\exp[-(\psi-\delta-\kappa)(n-r)] .
\]
Summing over \(r\) gives \(O(e^{-In}e^{-cL}/\sqrt n)\) for all sufficiently large \(n\) at each fixed \(L\), by splitting at \(r=n/2\). For \(r>n+L\), (5) alone gives \(O(e^{-In}e^{-\kappa L}/\sqrt n)\) after summing. Finally, at the remaining \(2L+1\) depths, use (5) with \(u=sn+K'\) to bound the mass with multiplier that large by \(O_L(e^{-In}e^{-\lambda K'}/\sqrt n)\). Choose \(L\) and then \(K'\) sufficiently large compared with the fixed lower constant in (3). On a set of Haar mass \(\gg e^{-In}/\sqrt n\), the selected all-depth winning word \(w_*\) therefore has
\[
             ||w_*|-n|\le L,\qquad sn\le\log M\le sn+K'.        \tag{6}
\]

As in the [exact word selection identity](BILATERAL_MINIMUM.md), the Haar mass of a selected word is the probability over uniform ternary origins of its event \(E_j\), times \(3^{-j}\). On the window (6) the change-of-measure factor \(3^{-j}/p_\lambda(w)=e^{-\lambda S_j-\kappa j}\) is comparable to \(e^{-In}\). Thus
\[
   \sum_{|j-n|\le L}\Pr_\lambda(E_j,\ sn\le S_j\le sn+K')\gg n^{-1/2}.
\]
For any fixed \(k\) and large \(n\), each term is at most \(C\Pr_\lambda(E_k)/\sqrt{j-k}\): use \(E_j\subset E_k\) and the uniform local bound for the independent remaining letters, also conditional on the ternary origin. Letting \(n\to\infty\) gives a positive lower bound on \(\Pr_\lambda(E_k)\) independent of \(k\). The nested limit gives (2).

## Dimension and ordinary density

The binary cylinder of a forward length-\(n\) word has depth \(1+A_n\). Under \(p_\lambda\), almost surely \(A_n/n\to b\) and \(-\log p_\lambda(w)/n\to H\). The gaps between successive depths are \(o(n)\) almost surely by the geometric tail. The induced dyadic law is therefore exact-dimensional of dimension \(H/(b\log2)\). By (2) a positive part of this law belongs to the dyadic projection, so its Hausdorff dimension is at least this number. Take \(\lambda\downarrow\lambda_c\). The resulting dimension is \(H_2(1/\log_2 3)=h\). For the reverse inequality, a surviving prefix has homogeneous multiplier at least one at its odd endpoints and at every intermediate shortcut clock: after the odd branch the intervening even branches only decrease the multiplier. At a binary precision \(m\) this requires at least \(m\log_3 2\) odd bits among the first \(m\) shortcut parities. These words each specify one residue modulo \(2^m\), and their number is at most \(2^{hm+o(m)}\).

To recover the ordinary-source exponent, ordinary word probabilities relative to \(p_\lambda\) have ratio
\[
          2^{-A_n}/p_\lambda(w)
           =\exp((\lambda-1)A_n\log2-n\log(2^\lambda-1)).
\]
The ordinary all-depth transfer in (3) of the bilateral minimum theorem applies termwise to these probabilities. On the positive-probability event \(E_\infty\) the logarithm of the displayed ratio divided by \(n\) tends to \(-\psi\) almost surely. Restricting to its typical window proves \(\liminf n^{-1}\log b_n\ge-\psi\). As \(\lambda\downarrow\lambda_c\), \(\psi\to(1-h)\log3\). For the other direction, at fixed depth the ordinary transfer bounds \(b_n\) by the geometric-\(2^{-a}\) probability of \(A_n\le n\log_2 3\), since the empty competitor must not win. Its lower-tail Chernoff exponent is exactly \((1-h)\log3\). This proves (1).
