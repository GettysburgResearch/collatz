# Ordinary entrance into the strict-record boundary

Use the odd map \(F_e(x)=(3x+1)/2^e\), with \(e=v_2(3x+1)\) at each ordinary odd source. A ladder word is the first strict upcrossing of zero by \(\sum_i(\log3-e_i\log2)\). Its positive length is the odd clock \(m\), and its total gap sum \(s\) is the shortcut clock. Fix the finite alphabet \(L_J\) of ladder words of length at most \(J\). Statements about arbitrary scripts below use the full symbolic shift. An ordinary script additionally requires integral positive starting and intermediate states at every depth.

## The three boundaries

Write \(F_w(x)=(3^m x+C_w)/2^s=r_wx+c_w\). The last gap of a ladder word is 1, so \(1<r_w\le3/2\). Its inverse \(g_w=(x-c_w)/r_w\) contracts over both the reals and \(\mathbb Z_2\) with respective ratios \(\lambda_w=2^s/3^m\) and \(d_w=2^{-s}\). At the ternary place the forward map contracts by \(3^{-m}\). The real and dyadic limits use the same future. The ternary limit uses the independent chronological past.

The real future projection is the whole interval \([-b_J,-1]\), where \(b_J=\max_w c_w/(r_w-1)\). Indeed every \(F_e\) preserves \([-1,\infty)\), hence \(b_w\ge1\), and equality occurs for the single gap 1. On the reflected interval \([1,b_J]\) the maps \(x\mapsto(x+c_w)/r_w\) preserve the interval. The images belonging to the extreme fixed points have lengths at least \(2(b_J-1)/3\), so these two alone cover it. For \(J\ge2\) the word \((2,1)\) gives \(b_w=7\). If \(R_J\) denotes the ternary past attractor in PR 201, the unrestricted two-sided set of real and ternary pairs is exactly \([-b_J,-1]\times R_J\). This follows by independently concatenating past and future scripts. It asserts neither independence under an orbit law nor realizability by positive integers.

There is no freedom to pair the dyadic future with an unrelated real future. Let \(G_J\) be their jointly coded graph in \(\mathbb R\times\mathbb Z_2\), with the maximum product metric. For \(J\ge2\) its Hausdorff and box dimensions are the unique \(D\in(1,2)\) such that
\[
  \sum_{w\in L_J}\lambda_w d_w^{D-1}=1 .
\]
Here \(\sum\lambda_w>1\) from the two extreme maps. Also \(\sum\lambda_w d_w=\sum3^{-m}<1\), by PR 201's strict ternary pressure bound. In the dyadic place a prefix of total clock \(S\) with odd terminal state occupies exactly one ball modulo \(2^{S+1}\). Different scripts that first differ before completion of that prefix cannot enter its ball, by unique odd-gap decoding and unique parsing at first strict records. In the real place distinct words of any fixed script length give distinct affine maps. Indeed equality of slopes fixes \(m,s\), and \(C_w=3^{m-1}+2^{e_1} C_{\rm tail}\), with \(C_{\rm tail}\) odd whenever \(m>1\). The numerator decodes \(e_1,\ldots,e_{m-1}\) and then \(s\) decodes \(e_m\).

For the upper dimension, stop prefixes when \(d=\prod d_w\) first drops below a small radius \(h\), so \(d\asymp h\). Each rectangular cylinder has real diameter \((b_J-1)\lambda\), where \(\lambda=\prod\lambda_w\ge d\), and can be covered by \(O_J(\lambda/h)\) product balls of comparable radius. The stopping cylinders partition probability for the Bernoulli weights \(p_w=\lambda_w d_w^{D-1}\). Summing gives the upper box bound \(O_J(h^{-D})\).

For the lower dimension set \(\chi_R=-\sum p_w\log\lambda_w\), \(\chi_2=-\sum p_w\log d_w\). The entropy is \(\chi_R+(D-1)\chi_2>\chi_R\). The real maps are algebraic and have no exact overlaps by the decoding above. Hochman's theorem on algebraic self-similar systems on the line implies that the real marginal \(\nu\) is exact dimensional of dimension one. For each \(\epsilon>0\) choose a positive-measure set of real points on which \(\nu(B(z,u))\le u^{1-\epsilon}\) uniformly for all sufficiently small \(u\). A typical script returns to its preimage at times \(n\) of positive asymptotic frequency, with successive return-time ratios tending to one. At those times set \(h_n=\prod_{i\le n} d_{w_i}/2\), \(\lambda_n=\prod_{i\le n}\lambda_{w_i}\). The dyadic coordinate forces the prefix; the remaining real tail falls in a ball of radius \(h_n/\lambda_n\). Thus the joint ball mass is at most \(\prod_{i\le n}p_{w_i}(h_n/\lambda_n)^{1-\epsilon}\). Since \(\chi_2>\chi_R\), the radii shrink in both coordinates. The strong law and bounded single-symbol clocks extend the resulting pointwise lower dimension \(D-\epsilon(1-\chi_R/\chi_2)\) to all radii. Letting \(\epsilon\) decrease proves the Hausdorff bound. The full unrestricted triple has dimension \(D+\dim R_J\), by independent pasts, the product Frostman lower bound, and the matching box upper bounds. No positive ordinary point has been produced in this argument.

## The first nontrivial ordinary entrance problem

For \(J=2\) there are exactly two blocks \(A=(1)\), \(B=(2,1)\). Every block endpoint is \(5\bmod 6\), since its last gap is 1. Write \(n=6t-1\) after the first block. Exact positive record dynamics on \(t\) are
\[
 A:\ 2u\longmapsto3u,\qquad B:\ 8u+7\longmapsto9u+8 .
\]
For \(A\), \(3n+1\) has valuation one precisely at even \(t\). For \(B\), the two required exact odd steps are equivalent to \(t\equiv7\bmod8\). The images \(0\bmod3\) and \(8\bmod9\) are disjoint, and both branches strictly increase every permitted positive source. Equivalently, the two maps have affine expressions \(F_A(t)=3t/2\), \(F_B(t)=(9t+1)/8\). Their dyadic inverse domains on \(\mathbb Z_2\) are exactly \(2\mathbb Z_2\) and \(7+8\mathbb Z_2\), hence an ordinary positive survivor exists exactly when their dyadic inverse attractor contains a positive integer. Their real inverse attractor is the entire interval \([-1,0]\).

An infinite positive script cannot become constant: arbitrary \(A\)-depth forces \(2^a\mid t\) for every \(a\), and arbitrary \(B\)-depth forces \(2^{3b}\mid t+1\) for every \(b\). For its real shadow \(z\), future shadows \(z_j\) therefore lie in \((-1,0)\). Indeed either endpoint has only the constant address. If \(a_j,b_j\) are the prefix counts, then with \(\xi=t-z\)
\[
 t_j=\left\lfloor \xi(3/2)^{a_j}(9/8)^{b_j}\right\rfloor .
\]
This follows by applying the identical affine word to \(t\) and \(z\) and retaining their difference. In the ternary place each \(t_j\) agrees with some point of the ternary past attractor modulo \(3^{a_j+2b_j}\), by completing the finite past with any left-infinite word. This depth eventually exceeds the entire physical ternary size of \(t_j\), since \(t_j<(t+1)(3/2)^j\). Dyadic prefixes and ternary suffixes carry dimensions \(e,d\) respectively, with \(2^{-e}+2^{-3e}=1\) and \(3^{-d}+3^{-2d}=1\). Their sum is below one, for instance \(e<0.552,d<0.439\). These are marginal dimensions. Counting integers that satisfy both conditions at physical precision requires an additional arithmetic estimate; even an \(X^{o(1)}\) octave estimate permits a single exponential orbit.

## Arithmetic coupling at every ordinary turn

Fix \(\epsilon>0\). At a junction \(t\) after \(a\) copies of \(A\) and before \(b\) copies of \(B\), ordinary integrality gives \(3^a\mid t\) and \(2^{3b}\mid t+1\). At a junction after \(b\) copies of \(B\) and before \(a\) copies of \(A\), we have \(3^{2b}\mid t+1\) and \(2^a\mid t\). Bugeaud–Evertse–Győry's Theorem 2.1(i) for the squarefree polynomial \(t(t+1)\) and the fixed set of primes \(\{2,3\}\) gives, at all sufficiently large junctions,
\[
 \begin{array}{ll}
 A^a|B^b:&a\log3+3b\log2\le(1+\epsilon)\log t,\\
 B^b|A^a:&2b\log3+a\log2\le(1+\epsilon)\log t.
 \end{array}
\]
Both divisibility conditions apply to the same integer. The threshold is ineffective. In particular a survivor with extremely long neighboring constant runs is subject to a stronger joint budget than separate valuation caps.

More generally fix two nonempty periodic blocks \(U,V\) in any \(L_J\) and write \(z_U,z_V\) for the real rational fixed points. Their reduced denominators are prime to six, since they divide \(3^{m}-2^s\). After \(k\) copies of \(U\), \(|t-z_U|_3\le 3^{-k m_U}\); before \(\ell\) copies of \(V\), \(|t-z_V|_2\le2^{-\ell s_V}\). Here \(t\) now denotes the ordinary odd state in the original coordinate, and no affine conjugation is needed. If the two centers are distinct, apply Theorem 2.1(i) to the product of their two primitive integral linear factors. If they coincide, their single integral linear factor already contains both prime powers. In either case
\[
 k m_U\log3+\ell s_V\log2\le(1+\epsilon)\log t
\]
at every sufficiently large such fixed-word junction. The implicit threshold may depend on the two words. Sparse-switch restrictions do not exclude a uniformly short-run script. Excluding every positive integer in the dyadic attractor, even at \(J=2\), remains open in this argument.

## Primary sources

- The record alphabet, ternary bounded overlap and strict dimension bound are in [PR 201](https://github.com/GettysburgResearch/collatz/blob/94ce06ccbd312ccd0ce4450b567cc514a2f0b54a/research/killed-green-head-closure-20261124/record-renewal/README.md).
- Michael Hochman, *On self-similar sets with overlaps and inverse theorems for entropy*, Annals of Mathematics 180 (2014), Theorem 1.1 for measures and the algebraic-separation argument in Theorem 1.5. [Paper](https://annals.math.princeton.edu/2014/180-2/p07)
- Yann Bugeaud, Jan-Hendrik Evertse and Kálmán Győry, *S-parts of values of univariate polynomials, binary forms and decomposable forms at integral points*, Acta Arithmetica 184 (2018), 151–185, Theorem 2.1(i). [Paper](https://arxiv.org/abs/1708.08290)
- Kurt Mahler, *An unsolved problem on the powers of 3/2*; Shigeki Akiyama, Christiane Frougny and Jacques Sakarovitch, *Powers of rationals modulo 1 and rational base number systems*; Shalom Eliahou and Jean-Louis Verger-Gaugry, *The number system in rational base 3/2 and the 3x+1 problem*. Their fixed-ratio number systems give related digit-avoidance questions. The variable multipliers and the two specific residue domains above require a separate ordinary entrance argument. [Mahler](https://doi.org/10.1017/S1446788700005371), [Akiyama–Frougny–Sakarovitch](https://math.tsukuba.ac.jp/~akiyama/papers/3half_H65fullTH-060406.pdf), [Eliahou–Verger-Gaugry](https://doi.org/10.5802/crmath.662)
