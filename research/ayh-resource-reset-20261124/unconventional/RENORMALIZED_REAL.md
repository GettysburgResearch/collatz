# A joint separation alternative for the ordinary renormalized real parameter

**Status.** Proposed written deduction using the finite simple-path reciprocal estimate and the fixed-place Subspace Theorem. This argument tracks one fixed ordinary source; its real limit and its dyadic limit enter at different places.

Fix a positive odd source \(a\) with an injective odd trajectory \(q_0=a,q_1,\ldots\). Let \(s_n\) be the total shortcut clock after \(n\) odd steps, \(M_n=3^n/2^{s_n}\), and \(2^{s_n}q_n=3^na+C_n\) the actual affine row. The ordinary simple-path reciprocal estimate gives
\[
 L=\lim_{n\to\infty} q_n/M_n
  =a\prod_{j\ge0}(1+1/(3q_j))\in(0,\infty).
\]
Indeed \(\sum_j1/q_j<\infty\) on this injective positive path. Define \(E_n=LM_n-q_n\). The identity
\[
 q_{n+1}/M_{n+1}-q_n/M_n=1/(3M_n)
\]
implies \(E_n=(1/3)\sum_{j\ge n}M_n/M_j\ge(1/3)\sum_{i\ge0}(2/3)^i=1\) for every \(n\), since each odd gap is at least one. Thus the natural partial-sum real error and the actual dyadic cancellation on the row by themselves leave the exact residual \(E_n\), which has this positive lower bound. [Finite simple-path reciprocal estimate, T-A3-651](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/astra-three-routes/pass3/FINITE_RECORDS.md)

Let \(b_\infty\) be a real algebraic number and \(b_p\) algebraic in \(\mathbb Q_p\) for \(p=2,3\). If \(L\) is algebraic, then for every \(\epsilon>0\) all sufficiently late indices satisfy
\[
 |E_n-b_\infty|\,|q_n-b_2|_2\,|q_n-b_3|_3
 \ \ge\ \exp(-\epsilon n).                                         \tag{1}
\]
Thus an exponential joint approach to these three fixed labels along a subsequence forces transcendence of the ordinary real parameter \(L\).

Use the primitive integer vectors \(X_n=(X,Y,Z)=(3^n,2^{s_n},C_n)\). Their sup-norm height \(H_n\) satisfies \(3^n\le H_n\le c_a3^n\) for a finite orbit-dependent constant: \(C_n/3^n=q_n/M_n-a\) is bounded and \(2^{s_n}/3^n=(q_n/M_n)/q_n\) is bounded. Every fixed proper rational plane contains only finitely many of these vectors. To see this, suppose \(rX+tY+wZ=0\) on an infinite subsequence, clearing coefficients to ordinary integers. The original row then gives
\[
              (r-wa)3^n+(t+wq_n)2^{s_n}=0.
\]
As \(2^{s_n}\mid(r-wa)\) and \(s_n\ge n\), one has \(r=wa\). The distinct ordinary \(q_n\) imply \(t=w=0\), hence \(r=0\).

Choose \(X,Y\) as two of the three linear forms at each of \(\infty,2,3\). Use the following third forms:
\[
 \begin{array}{ll}
 \infty: & Z-(L-a)X+b_\infty Y,\\
 2: & Z+aX-b_2Y,\\
 3: & Z+aX-b_3Y .
 \end{array}
\]
At each place the three forms are independent. Their coefficient conditions hold under the stated algebraicity assumption; each local target is used at its own place. The two coordinate factors \(X,Y\) have product of local norms one over these three places. The three other form values are \(Y(b_\infty-E_n),Y(q_n-b_2),Y(q_n-b_3)\), and their three \(Y\)-norms multiply to one. The entire local product is exactly the left side of (1).

For any \(\eta>0\), the Schlickewei Subspace Theorem puts indices with local product below \(H_n^{-\eta}\) in finitely many fixed proper rational subspaces. The plane exclusion proved above makes their union contribute finitely many indices. The comparison \(H_n\le c_a3^n\) gives (1) by choosing \(\eta\log3<\epsilon\). [Evertse, Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)

For bounded gaps of strict coefficient records, earlier record results bound \(E_n\) at the record indices. In this case (1) with \(b_\infty=0\) shows directly that exponential dyadic or ternary approach of those actual record states to any fixed local algebraic labels forces \(L\) to be transcendental (the other finite factor is bounded on ordinary integers). Compactness supplies no such exponential rate. Irrationality of a real limit alone also gives no statement about the rational dyadic source. Earlier two-place affine-plane saturation used a moving terminal coefficient; the plane exclusion here uses only fixed rational planes. [Bounded-record real error, PR201](https://github.com/GettysburgResearch/collatz/blob/94ce06ccbd312ccd0ce4450b567cc514a2f0b54a/research/killed-green-head-closure-20261124/record-renewal/README.md) · [Earlier affine-plane saturation](https://github.com/GettysburgResearch/collatz/blob/7270321fc774ba4bc92a4e0e58cdf8f7f7d2b131/research/least-counterexample-global/claims/L-6505-adelic-affine-plane-saturation.md)

## One-sided tests using the true local closing

Suppose that successive strict upper records of the coefficient \(M_n\) have an eventual bounded odd gap. Fix \(\gamma>0\). If \(L\) is algebraic, there is an \(\eta>0\) such that, for all sufficiently large \(n\), **each** of the following actual closings has reduced denominator at least \(e^{\eta n}\):

* Any word of \(m\) immediately preceding odd gaps, where \(\gamma n\le m\le n\).
* Any word of \(m\) immediately following odd gaps, where \(m\ge\gamma n\).

Consequently the occurrence, on either one side, of such words having \(\log d=o(n)\) on an unbounded subsequence forces \(L\) to be transcendental. The conclusion tests an actual rational closing built from the word, so no predetermined algebraic limit in the ternary record tree is required.

**Real bounds.** The bounded-gap ladder alphabet is finite. Each complete record block has real slope at least \(r_*>1\), and incomplete blocks at the ends of an interval have slopes bounded above and below by positive constants. Hence there are \(c,C>0\) with \(M_j/M_i\ge C^{-1}e^{c(j-i)}\) for \(j\ge i\), after adjusting \(C\) for the finite initial part. This gives \(q_n\ge c'e^{cn}\). The tail identity \(E_i=(1/3)\sum_{j\ge i}M_i/M_j\) makes \(E_i\) bounded. Put \(z_i=-E_i\); since \(M_i\) is transported multiplicatively, the \(z_i\) follow the same affine odd maps as \(q_i\). For a length-\(m\) interval with terminal \(j\), initial \(i\), real inverse multiplier \(A=M_i/M_j\), and true closing \(\zeta\),
\[
        z_i-\zeta=A(z_j-\zeta),\qquad
        \zeta=(z_i-Az_j)/(1-A).
\]
Thus \(\zeta\) is uniformly bounded in the real absolute value on every such interval of sufficiently large length. Its logarithmic height is \(\log d+O(1)\).

**Moving-label separation.** In (1) one may now allow the three algebraic labels to vary with \(n\), with respective logarithmic heights \(o(n)\) in a fixed number field. Keep \(L\) algebraic. To justify this extension use the same primitive projective vectors as above and a fixed finite Galois extension containing all coefficients. On any infinite coherent subsequence, every fixed rational expression in the coefficients of the moving forms has height \(o(n)\) wherever it is defined. Suppose a nonzero relation with such coefficients existed. After substituting the affine row it would give
\[
 (r_n-aw_n)3^n+(t_n+w_n q_n)2^{s_n}=0.
\]
At any place above two with the usual rational normalization, \(q_n\) is an integer, so
\[
 |r_n-aw_n|_2\le 2^{-s_n}\exp(o(n)).
\]
A nonzero element of a fixed number field and absolute logarithmic height \(o(n)\) has local norm at least \(\exp(-o(n))\): apply the definition of height to its inverse. As \(s_n\ge n\), one must have \(r_n=aw_n\) eventually. If \(w_n\ne0\), then \(q_n=-t_n/w_n\) would have height \(o(n)\), contradicting the exponential size already proved. Thus the coordinates are independent over every coherent coefficient field.

Take the collection of triples of forms consisting of the two coordinate forms \(X,Y\) and each of the possible third forms. Each triple is independent. At every archimedean or finite place above an original rational place choose the conjugate coefficients representing the specified local target in that embedding; a finite Galois extension allows all these choices. The number of slots is fixed. Each form has one coefficient equal to one. All finite local norms of the primitive vector are one. At a selected rational place, the weighted Weil-function sum therefore bounds below the corresponding contribution of minus the logarithm of the three-form product, together with the three local projective norms. Summing, using the product cancellations already displayed, gives \(3\log H_n-\log P_n\) as a lower bound for the total Weil sum, where \(P_n\) is the left side of (1) with these moving labels. Ru–Vojta gives the upper bound \((3+\varepsilon)\log H_n+O(1)\). The conjugate-place weights above each rational place sum to one. This proves the same separation statement. An exact zero among chosen form values infinitely often would itself be a moving-coefficient dependence on a coherent subsequence. [Vojta, Theorem 7.7](https://library.slmath.org/books/Book37/files/vojta.pdf)

**The past.** If preceding closings with \(m\ge\gamma n\) had reduced denominators \(e^{o(n)}\) along a subsequence, take \(b_3=\zeta\), \(b_2=b_\infty=0\). The actual ternary agreement gives \(|q_n-\zeta|_3\le3^{-m}\), the other finite factor is at most one, and \(E_n\) is bounded. This contradicts moving-label separation.

**The future.** If future closings had such denominators, use \(b_2=\zeta\), \(b_\infty=-\zeta\), \(b_3=0\). For the same physical word from \(n\) to \(n+m\) of total clock \(s\),
\[
 |E_n+\zeta|\,|q_n-\zeta|_2
 \le (2^s/3^m)|z_{n+m}-\zeta|\,2^{-s}
 \ll 3^{-m}.
\]
This again contradicts separation. If positive uniform \(\eta\) failed for either side, a subsequence with \(\log d/n\to0\) would supply exactly the contradiction proved above. The lower-growth assumption on \(q_n\) is essential to this moving-coefficient argument.
