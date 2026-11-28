# Arithmetic progressions and higher sumsets of endpoints with genuinely confined pasts

**Proposed written theorem.** Fix \(2<R<4\), let \(M\to\infty\), and fix a common complete denominator \(Q\) prime to six, which may vary with \(M\). Consider arbitrary distinct positive odd rational endpoints \(x\in[M,RM]\), each supplied with a genuine inverse history of \(n\) odd steps staying throughout the **same physical band** \([M,RM]\). The histories may start on different trajectories; if there are choices, select any one per endpoint.

There are effective constants \(c_R,\delta_R>0\) with the following finite obstruction at all sufficiently large \(M\). For any nonconstant physical arithmetic progression \(y-d,y,y+d\) in this endpoint population with \(\log_2((y+d)/(y-d))\le\delta_R\),
\[
               3^{\min(n,\lfloor c_R M\rfloor)}\ \mid\ Qd.             \tag{1}
\]
The right side is an integer. This is sharp in terms of its ternary valuation: for every \(n\ge1\) there are true positive ordinary progressions of endpoints with \(n\) genuine common-word pasts in such a band, arbitrarily small relative spread and \(v_3(d)=n\). In particular, a tightly clustered nonconstant progression of odd integers with spacing prime to three cannot even have one such past; a spacing exactly divisible by \(3^j\) allows at most \(j\) such dates when \(j<c_RM\).

There is an additive-structure assertion at all fixed orders admitted by a native return gap. Put \(\gamma=\log_23,\ \eta=\log_2(R/2)\). Choose a fixed integer \(L\ge1\) with
\[
                \eta<\min_{1\le j<L}\|j\gamma\|,                       \tag{2}
\]
where the minimum over the empty set is \(+\infty\). Fix \(2\le h<3^L\). Suppose \(\log(QM)=o(M)\), and every supplied history has at least
\[
           n+L-1\quad\hbox{edges},\qquad
            n=\lceil\log_3(16hRQM)\rceil+2 .
\]
Then every subset \(S\) of this arbitrary pooled endpoint set satisfies
\[
                         |hS|\ \gg_{R,L,h}\ |S|^{\log_2(h+1)},          \tag{3}
\]
with addition of actual rational values. On each of a bounded number of fixed relative-height bins the physical endpoints are Freiman-isomorphic of order \(h\) to a subset of a Boolean cube: equality between two sums of \(h\) physical sources, with arbitrary repetitions, holds precisely when every coordinate of their true backward tag words has equal sum. The rate in (3) is independent of \(Q\). In particular \(L=1\) always gives \(h=2\) and exponent \(\log_23=1.58496\ldots\). For \(R<8/3\) one may take \(L=2,\ h=8\); for \(R<9/4\) one may take \(L=5,\ h=242\). For each fixed \(h\), one of these conclusions holds at all \(R>2\) sufficiently close to two. The assumptions are on predecessors, not on an unobserved continuation at either end.

## A common genuine backward chart

Choose \(J=M\sqrt R\). Both \(RM/2<J\) and \(J<2M\) have fixed multiplicative margins. Partition \([M,RM]\) into a bounded number, depending only on fixed parameters, of height intervals \([Y,2^\delta Y]\) for a sufficiently small \(\delta>0\). For (1) use the single small interval starting at \(y-d\); for (3) the bins give the required partition. Let \(t=0\) be the endpoint date and normalize each initial \(E_{0,i}=0\). On the recorded past set \(E_{t+1,i}-E_{t,i}=v_2(3x_{t,i}+1)\), put \(V_{t,i}=2^{E_{t,i}}x_{t,i}\), and take the **same** floor calendar \(F_t=\lfloor\log_2(Y/J)+t\gamma\rfloor\) for the whole bin. Write
\[
 z_t=\{\log_2(Y/J)+t\gamma\},\qquad
 Z_{t,i}=2^{-F_t}V_{t,i}=C_{t,i}x_{t,i},\qquad
 C_{t,i}=2^{E_{t,i}-F_t}.
\]
For \(t\le0\),
\[
 \log_2(Z_{t,i}/J)=z_t+\log_2(x_{0,i}/Y)
             -\sum_{j=t}^{-1}\log_2(1+1/(3x_{j,i})).
\]
The sum lies between zero and \(|t|/(3M\ln2)\). Choosing \(\delta_R\) and \(c_R\) sufficiently small ensures that for (1), throughout the stated number of dates, \(RM/2<Z_{t,i}<4M\). For (3) the logarithmic horizon plus its fixed guard makes the error away from \(z_t\) at most \(\delta+o(1)\). Shrinking \(\delta\) if needed gives the same inequalities. More precisely the lower bound follows from \(J2^{-c_R/(3\ln2)}>RM/2\); the upper from \(2J2^{\delta_R}<4M\). As \(M\le x_{t,i}\le RM\), all powers \(C_{t,i}\) belong to \(\{1,2\}\), and \(QZ_{t,i}\) is integral. Also \(C_{0,i}=2^{-F_0}\) for every source in the bin.

Let a date be active if both tag values occur among the words. On such a date some label lies in \([M,RM]\) and another in \([2M,2RM]\), each within a factor \(2^{\delta+o(1)}\) of \(J2^{z_t}\). All active \(z_t\)'s therefore lie in the circle interval given by a \(\delta+o(1)\) enlargement on both sides of \([\log_2(2M/J),\log_2(RM/J)]\); its limiting unenlarged length is \(\eta\). Taking \(\delta\) small relative to the strict gaps in (2) puts every two distinct active dates at least \(L\) ordinary odd steps apart. If \(L=1\), no spacing condition is needed.

## Peeling the exact ternary divisor

For the signed difference between two sums of \(h\) such labels write \(H_t=\sum_{\rm left} Z_{t,i}-\sum_{\rm right}Z_{t,i}\) and \(d_t=\sum_{\rm left} C_{t,i}-\sum_{\rm right}C_{t,i}\), so \(|d_t|\le h\). The genuine edge equation is
\[
               2^{F_{t+1}-F_t} H_{t+1}=3H_t+d_t,\qquad QH_t\in\mathbb Z.
\]
If \(H_{t+1}=0\) and the preceding \(L-1\) dates \(t-L+1,\dots,t-1\) are inactive, then \(3^L\mid Qd_t\): indeed \(3QH_t=-Qd_t\) and the preceding homogeneous recurrence shows \(3^{L-1}\mid QH_t\), since all powers of two are ternary units. Thus if \(h<3^L\), coprimality forces \(d_t=0\) and \(H_t=0\). On an inactive date the same reverse step is immediate from \(d_t=0\). The \(L-1\) guard dates before the encoded word give the needed separation even at its left boundary.

For the special two-versus-two relation \((y-d)+(y+d)=2y\), use \(L=1\) on the finite interval of (1). The initial physical equality makes \(H_0=0\). It follows backwards that \(C_{t,-}+C_{t,+}=2C_{t,0}\) at every past date. An arithmetic progression in \(\{1,2\}\) is constant, so the three tags coincide separately on the entire interval. For any neighboring pair of the three labels its individual difference now obeys the homogeneous recurrence. Over \(k=\min(n,\lfloor c_R M\rfloor)\) edges this gives \(3^k\mid Q C_0 d\), where \(C_0\in\{1,2\}\) is the common endpoint multiplier. This proves the complete integer divisor (1).

To see sharpness, prescribe the mechanical valuations \(a_j=\lfloor(j+1)\gamma\rfloor-\lfloor j\gamma\rfloor\) over \(n\) forward dates, of total \(A=\lfloor n\gamma\rfloor\). There is an odd starting residue modulo \(2^{A+1}\) realizing these valuations: compose the true numerator relation and require the final numerator before division by \(2^A\) to be \(2^A\) modulo \(2^{A+1}\). The odd multiplier \(3^n\) is invertible there; reducing successively at each intermediate prefix verifies the actual valuations. Choose an arbitrarily large positive representative \(x\). The three starts \(x,x+2^{A+1},x+2\cdot2^{A+1}\) follow the same word and finish in a progression of spacing \(2\cdot3^n\). For each fixed \(n\), every homogeneous prefix gain lies in \([1,2)\), and all true additive corrections are bounded independently of the chosen lift. Consequently all three histories lie in \([x,Rx]\) for all sufficiently large lifts, and their endpoint relative spread tends to zero.

## Exact word isomorphism and physical expansion

Record \(C_{t,i}-1\in\{0,1\}\) for \(t=-n,\ldots,-1\). For \(h\) sources on each side, a physical sum equality implies \(H_0=0\); the reverse argument at active and inactive dates then gives \(d_t=0\) at all \(n\) encoded rows. Conversely, coordinatewise equality gives \(d_t=0\) there. By the homogeneous recurrence \(3^n\mid QH_0\). Its absolute value is at most \(2hRQM\), so the chosen \(n\) forces \(H_0=0\), which is precisely the physical equality because \(C_0\) is common. Applying the same divisibility to a single pair proves word injectivity. Hence the two \(h\)-fold sumsets have the same cardinality on each bin.

The binary cube sumset theorem of Becker, Ivanisvili, Krachun and Madrid gives \(|hA|\ge |A|^{\log_2(h+1)}\) for every subset \(A\subseteq\{0,1\}^n\), with ordinary coordinate addition. Apply it to the words in a bin containing at least a fixed fraction of \(S\). This gives (3). [Original paper, Theorem 1.1, arXiv:2404.04486](https://arxiv.org/html/2404.04486v1) · [General hypercube extension by Gonçalves and Radchenko](https://arxiv.org/html/2607.01458v1)

Weaver's Theorem 7 gives hereditary energy for finite subsets of the union of canonical-height-one ordinary cycles in a located integer interval, and exponent \(\log_2(8/3)\) for their doubled sumsets with polylogarithmic loss. It imports Kane–Tao's energy bound and transfers a forward source-modulus collision back to a segmented code. The [one-cycle two-grade theorem](TWO_GRADE_SIDON.md) gives a stronger binary Sidon statement on short ordered ranks of a single ordinary cycle. Here a true shared *past band* for a pool of possibly unrelated endpoints makes the ternary decoder exact on unscaled physical sums after the single bin-common endpoint normalization. [Weaver 145/v1, Lemma 3 and Theorem 7](https://rstation.ai/problems/collatz/papers/145/v1) · [Weaver 222/v1, maximal confined past and source progressions at factor two](https://rstation.ai/problems/collatz/papers/222/v1)
