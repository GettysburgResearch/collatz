# How often a reflected cycle can supply a cheaper positive visitor

Let \(U(x)=(3x+1)/2^{v_2(3x+1)}\) be the accelerated map on positive odd integers, and \(F(x)=(3x-1)/2^{v_2(3x-1)}\) its reflected counterpart. For a nonnegative overhead \(h\), let \(S_h\) consist of the positive ranks \(s\) for which *some* matching-depth seven-phase class with \(3^s\mid n\) admits a positive visitor below its principal source by budget \(R+s+h\). The phase, lap count and cofactor may change with \(s\). The results below do not assume that all positive trajectories converge.

### The rank and fixed-source conclusions

Write \(\alpha=3/2\). There are absolute constants such that for every interval \(I\) of \(L\ge2\) positive ranks and every \(h\ge0\),
\[
 \#(S_h\cap I)\ll \alpha^h\frac{L}{\log(2+L)}.
\tag{1}
\]
On the published two-logarithm inequality of Wu and Wang, this improves to
\[
 \boxed{\quad \#(S_h\cap I)\ll\alpha^h L^{1-1/128}.\quad}
\tag{2}
\]
In particular each fixed \(S_h\) has zero upper Banach density, and (2) gives \(\sum_{s\in S_h}1/s<\infty\). A second conclusion controls recurring gaps. For fixed \(h\), only finitely many positive integers \(d\) have infinitely many representations \(d=s'-s\) with \(s,s'\in S_h\).

One can also consider one arbitrary fixed ordinary source, independently of the finite pool or the overhead. Put \(c_s=U^s(w)\). Call \(c_s\) a marked visit if for some \(D\ge1\), \(m=17\cdot2^D-c_s>0\) first reaches 17 under \(F\) after \((7\ell,11\ell+D)\) odd and physical clocks. If \(w\) is nonperiodic (its orbit never repeats), put \(M_s=\min_{i\ge s}c_i\). Then \(M_s\to\infty\). Two marked visits of this orbit at dates \(s,s+d\), \(d>0\), satisfy \(d\gg\log M_s\) for large \(M_s\), and on the Wu–Wang input,
\[
                     d\gg M_s^{1/640}.
\tag{3}
\]
In particular a nonperiodic source can return to the mark infinitely often only with inter-visit gaps tending to infinity. A positive eventually periodic orbit can make unboundedly many *raw* marked visits; its slope prevents unboundedly many successes at any fixed overhead.

Define \(H(s)=\min\{h:s\in S_h\}\). This is finite since \(w=1,c=1,D=1,m=33\) works whenever \(2(4/3)^s<\alpha^h\). For every \(0<\kappa<1/(128\log\alpha)\), (2) gives \(H(s)>\kappa\log s\) on a set of natural density one. Indeed on \(s\le X\) all exceptions lie in \(S_{\lfloor\kappa\log X\rfloor}\) by monotonicity, and are \(O(X^{1-1/128+\kappa\log\alpha})\). The self-contained (1) gives \(H(s)>\kappa\log\log s\) on a density-one set for \(0<\kappa<1/\log\alpha\).

### The grade and the funded positive history

The exact test in `ORDINARY_OVERHEAD_SPECTRUM.md` finds \(s\in S_h\) precisely when an ordinary positive odd \(w< K=17\alpha^h\) with \(c_s=U^s(w)\) makes a marked visit and satisfies
\[
              2^{D+E_s}/3^s<\alpha^h,
\tag{4}
\]
where \(E_s\) is its total division count through that date. We use necessity for (1)–(2). Sufficiency in the exact test constructs actual ordinary CRT visitors. It need not make an arbitrarily specified cofactor successful.

Write \(r=c_s/2^D=17-m/2^D\), \(\lambda=2048/2187\), and \(b=7\ell\). The reflected odd states before first 17 are distinct. Multiplying the reflected step identities and ordering these \(b\) positive states gives
\[
 \frac m{2^D}=\frac{17\lambda^\ell}{\prod_{j<b}(1-1/(3F^j(m)))}
 \le17(b+1)\lambda^\ell.
\tag{5}
\]
The product is bounded below by \(\prod_{i=1}^b i/(i+1)=1/(b+1)\). First arrival matters because padding at the mark could repeat its factors. This use of the distinct-state product comes from Weaver's Paper 108. [Paper 108, Lemmas 3–4](https://rstation.ai/problems/collatz/papers/108)

Let \(T,S\) denote the ordinary and reflected physical shortcut maps, with odd branches \((3x+1)/2,(3x-1)/2\). From \(c_s+m=17\,2^D\), the first \(D\) physical input parities of \(c_s\) and \(m\) agree. At clock \(D\), with their common odd count \(q\), one has
\[
                  T^D(c_s)+S^D(m)=17\cdot3^q.
\tag{6}
\]
This follows step by step: even inputs halve the sum, and odd inputs triple and halve it because the two affine increments cancel. Until clock \(D\) the displacement is even, as required. Since the signed first-arrival clock is \(D+11\ell\), \(q\le7\ell\). If \(T^D(c_s)\) is even, continue to its odd part by ordinary halvings; these add no odd departure. The result is an actual positive odd state reached from \(c_s\) within \(7\ell\) odd departures, of size at most \(17\cdot3^{7\ell}\). The formal version works for arbitrary complement coefficient and signed full count. [SignedGradeSplit.lean](SignedGradeSplit.lean)

For example \(m=(25\cdot2^{2k+1}+1)/3\), \(c=(4^k-1)/3\), \(D=2k\), \(k\ge1\), have \(b=7\), first passing from \(m\) to 25 and completing the six-edge cycle arc to 17. Here \(r\to1/3\), far from 17, but \(3c+1=4^k\) gives \(U(c)=1\). Bounded lap counts really can give large marked integers with other limiting normalized heights. Equation (6) shows why these cannot occur arbitrarily late on a fixed divergent orbit.

Put \(\omega=\log_2 3\), \(\theta_j=\log_2 c_j\pmod1\), and \(\epsilon_j=\log_2(1+1/(3c_j))>0\). Each positive odd step gives \(\theta_{j+1}=\theta_j+\omega+\epsilon_j\pmod1\). Crucially, at any **successful** date of this particular \(w\),
\[
  2^{\sum_{j<s}\epsilon_j}=(2^{E_s}/3^s)c_s/w<K/w.
\tag{7}
\]
Thus the accumulated logarithmic error before its last successful date in an interval is bounded by \(\log_2(K/w)\), even in a repeating positive orbit. Paper 180 uses this positive product to control a different inverse family; Paper 222 uses rotation of the binary phase on height-confined windows. [Paper 180, Sections 3–6](https://rstation.ai/problems/collatz/papers/180/v1) · [Paper 222](https://rstation.ai/problems/collatz/papers/222)

### Short signed paths force small states, long paths force a short phase arc

Fix \(w\), an interval \(I\) of length \(L\), and truncate its dates at the last success \(T\) for this root in \(I\). Roots with no success contribute zero. Choose \(J=\lfloor(\log_2 L)/12\rfloor\). When a date has several successful witnesses choose any one. At a success with \(\ell\le J\), (6) gives a positive state of size at most \(B=17\cdot3^{7J}\) within \(7J\) odd dates. Exclude the last \(7J+1\) dates; all charged states now occur before \(T\). Each such state costs at least \(\log_2(1+1/(3B))\gg1/B\) of the nonnegative error in (7). A given date can be charged by at most \(7J+1\) successful starts. Consequently the short-path contributions are
\[
          O\big((J+1)[1+B\log(K/w)]\big).
\tag{8}
\]
This counts occurrences, so a repeated small state consumes its error at its actual multiplicity. Since \(3^{28}<2^{45}\), \(B\ll L^{15/16}\).

For \(\ell>J\), (5) gives \(0<17-r\ll(J+1)\lambda^J\). The sequence \((7\ell+1)\lambda^\ell\) decreases after a fixed threshold. Since \((2187/2048)^{32}>8\), one has \(\log_2(2187/2048)/12>1/128\) with room to absorb the factor \(J+1\). For all sufficiently large \(L\), every such \(\theta_s=\log_2 r\pmod1\) lies in one arc of length \(O(L^{-1/128})\) abutting \(\log_2 17\). This does not assume a global lower bound for positive \(r\).

For an arbitrary circle arc \(V\), choose coprime \(p,q\) with \(1\le q\le Q\), \(|q\omega-p|\le1/Q\), by pigeonholing the first \(Q+1\) multiples of \(\omega\) and reducing the fraction. In each complete block of \(q\) dates the phases differ from a translate of the equally spaced grid \(ip/q\) by at most \(1/Q+\sum_{\rm block}\epsilon_j\) in circle distance. Enlarging \(V\) by this amount, summing the grid counts, and charging the final incomplete block gives
\[
   \#\{j\text{ on the truncated interval}:\theta_j\in V\}
   \le L|V|+O\big(L/q+L/Q+q[1+\log(K/w)]\big).
\tag{9}
\]
For (1) choose \(Q=\lfloor\sqrt L\rfloor\) at large \(L\). Since \(|3^q-2^p|\ge1\) and \(|q\omega-p|\le1/Q\), the mean value theorem gives \(|q\omega-p|\gg3^{-q}\); hence \(q\gg\log L\). For (2), Wu and Wang's Theorem 1 implies \(\|q\omega\|\gg q^{-5}\) by taking the constant coefficient zero in \(q\log3-p\log2\), choosing \(p\) nearest to \(q\omega\) and absorbing finitely many small denominators. With \(Q=\lfloor L^{3/4}\rfloor\), one gets \(q\gg L^{3/20}\), \(q\le L^{3/4}\). Sum (8) and (9) over the odd \(w<K\), using \(\sum_{1\le w<K}\log(K/w)=O(K)\) by integration. Both bounds follow, with constants uniform in \(h,I\). [Wu and Wang, *On the irrationality measure of log 3*, Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007)

### Gaps on one fixed positive trajectory

On a nonperiodic positive orbit all states are distinct, so its true future floor \(M_s\) tends to infinity. At a marked visit, (6) yields \(M_s\le17\cdot3^{7\ell}\). In particular the lap counts of any unbounded sequence of such visits tend to infinity. From (5) we get the quantitative localization
\[
     0<17-r\ll (1+\log M_s) M_s^{-\eta}\ll M_s^{-1/128},
   \qquad \eta=\frac{\log(2187/2048)}{7\log3}>1/128.
\tag{10}
\]
The last strict inequality is the integer comparison \((2187/2048)^{128}>3^7\). Here the exponentially decreasing right hand side of (5) is evaluated at the lower bound for \(\ell\), valid beyond a fixed threshold.

At two marked visits separated by \(d>0\), both logarithmic phases differ from \(\log_2 17\) by \(O(M_s^{-1/128})\); the \(d\) intervening phase errors sum to \(O(d/M_s)\). Thus
\[
                 \|d\omega\|\ll M_s^{-1/128}+d/M_s.
\]
Integer separation \(\|d\omega\|\gg3^{-d}\) gives \(d\gg\log M_s\) (split at \(d=M_s^{1/2}\)). With Wu–Wang's bound \(\|d\omega\|\gg d^{-5}\), either \(d\gg M_s^{1/640}\) or \(d\gg M_s^{1/6}\). This proves (3) for all pairs of marked visits and does not require the positive slope (4). Paper 180 proves a related spacing theorem for a different set of physical visits approaching \(2\cdot3^j\); it obtains a single limiting phase there by the special geometry of that set. The extra step here is (6), which forces the reflected 17-grade to have long lap count at late visits. [Paper 180, Sections 5–6](https://rstation.ai/problems/collatz/papers/180/v1)

To bound recurring differences of \(S_h\), keep only the finitely many roots \(w<K\) successful at unboundedly many dates. Each is nonperiodic, because any eventual cycle contributes a positive amount to the accumulated logarithmic error per lap, contradicting (7). By monotonicity, (7) implies the existence of the finite limit \(P_\infty(w)=2^{\sum_{j\ge0}\epsilon_j}\). Thus all its late successful dates obey
\[
        \operatorname{dist}(s\omega,\phi_w)\longrightarrow0,
        \qquad \phi_w=\log_2(17/[wP_\infty(w)])\pmod1.
\]
Let \(\Phi_h\) be the resulting finite set of phases. If a fixed \(d>0\) repeats as a difference infinitely often, then \(d\omega\in\Phi_h-\Phi_h\pmod1\) by passage to fixed roots. Irrationality gives at most one positive \(d\) per unordered pair of distinct phases: the opposite orientation cannot also yield a positive \(d'\), as \((d+d')\omega\) would be integral. Thus at most \(\binom{|\Phi_h|}{2}\) positive differences can recur. In particular no sum of two infinite sets of nonnegative integers can lie in \(S_h\).

### What recurrence would be sufficient

There exists a fixed \(h\) with \(S_h\) infinite **if and only if** some fixed nonperiodic positive ordinary source makes infinitely many marked visits. Forward implication follows from the finite positive pool. Conversely fix such a source \(w\). The resident finite simple-path reciprocal estimate T-A3-651 gives \(\sum_j1/c_j\le200\), and hence \(P_\infty(w)\le e^{200/3}\). In applying the result to its physical shortcut path, a repeated physical state would force the positive odd orbit to repeat. Equation (10) gives \(c_s/2^D\to17\) along its marked dates. Choose a fixed \(h\) with \(\alpha^h> e^{200/3}w/16\). On every sufficiently late marked date \(r>16\), so \(2^{D+E_s}/3^s=wP_s/r<\alpha^h\); the exact test now supplies a successful rank on each such date. This part uses the resident reciprocal-packing theorem or an equivalent source-qualified bound; (1)–(3) do not. Weaver's Paper 180 already uses reciprocal packing and positive distortion for its different converse from recurrence to failure. [Finite simple-path packing, T-A3-651](../../astra-three-routes/pass3/FINITE_RECORDS.md) · [Paper 180, Section 5](https://rstation.ai/problems/collatz/papers/180/v1)

### Adaptive choice among finitely many reflected cycles

The preceding method permits a mark selected after the positive endpoint is known, from any fixed finite family of actual positive odd reflected cycles. For a mark \(a\) with odd period \(b_0\) and total divisions \(p_0\), require \(m=a2^D-c>0\) to first reach \(a\) in \((b_0\ell,p_0\ell+D)\) clocks, with the positive slope in (4). Every cycle phase is a ternary unit and \(\lambda_a=2^{p_0}/3^{b_0}=\prod(1-1/(3x))<1\). Replace 17, 7, 11 by these marked data in (5) and (6). At small \(\ell\) one obtains an actual positive odd state at most \(a3^{b_0\ell}\), and at large \(\ell\) the complement approaches the single phase \(\log_2 a\). The comparison (7) holds with \(K=\alpha^h\max a\). Taking \(J=\lfloor\rho\log_2 L\rfloor\) with \(\rho b_0\log_2 3<1\) uniformly over the finitely many marks, the proof of (8)–(9) supplies some \(\delta>0\), depending on those cycle parameters, with \(O(\alpha^h L^{1-\delta})\) successful ranks in any length-\(L\) interval on the Wu–Wang input. The elementary version gives \(O(\alpha^h L/\log(2+L))\). There are finitely many phase arcs and small-state cutoffs, so an adaptive choice within the family is already covered.

On one fixed nonperiodic orbit the raw inter-visit gaps also tend to infinity for this union. If a fixed gap \(d>0\) recurred infinitely often, take a pair of fixed marks \(a,a'\) on a subsequence. Their limiting phases require \(a'/a=3^d2^k\) for some integer \(k\), impossible since both marks are ternary units. The finite recurring-difference conclusion for the union over roots follows as before using the finitely many phases \(\log_2(a/[wP_\infty(w)])\). This extension concerns the stated graded incidences. A general inverse minimum theorem for other cycles would require additional arguments.

These results allow infinitely many isolated marked visits and changes of cofactor in the cheaper-visitor witnesses. They do not force a single guaranteed cheaper merger for an arbitrary supplied starting integer.
