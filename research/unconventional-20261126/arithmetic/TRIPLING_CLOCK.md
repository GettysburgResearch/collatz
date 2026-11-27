# A uniform joint clock for disjoint tripling orbits

**T1.** Let \(x\) be any positive odd rational number (reduced numerator and denominator odd). Follow the physical odd Syracuse orbits of \(x\) and \(3x\). Write \(S_0=T_0=0\) and let \(S_i,T_j\) be the cumulative numbers of shortcut divisions after respectively \(i,j\) odd steps. If the two orbits have no common odd state, then, for every integer \(K\ge1\),
\[
 \min(S_K,T_K)<(2K-1)(K+1)\log_2 3. \tag{1}
\]
The estimate is source-uniform and imposes no bound on individual division exponents. More locally, for successive distinct dates \(t<t'\) in the union of shortcut odd dates, let \(i,j\) be the last indices with \(S_i,T_j\le t\). Then
\[
 t'-t< \max(i+1,j+2)\log_2 3.                             \tag{2}
\]
These statements also hold with a finite hypothesis: the odd states \(U^{i+1}(x)\) and \(U^{j+1}(3x)\) must differ at each cut at issue. A common state may be visited on different odd or shortcut clocks.

**T2.** Suppose a positive odd rational \(x\) has reduced denominator \(D\) prime to six, its orbit and that of \(3x\) are disjoint, and both are eventually periodic. If each leg has at most \(K\) distinct odd states on its full forward orbit, then
\[
 D<3^{(2K-1)(K+1)}.
\]
For fixed \(K\) there are only finitely many such rational \(x\), even without any bound assumed on their real heights, reduced denominators or individual division exponents. In particular, an infinite family of genuinely distinct rational cycle-basin tripling disagreements with bounded-size certificates of both eventual periodic fates cannot be obtained by sending only their division exponents to infinity. An unbounded denominator forces a number of distinct odd states at least of order \(\sqrt{\log D}\) in one leg. Certificates with an unbounded odd clock and certificates of aperiodic fates are outside that conclusion.

## Proof of the local inequality

Let \(q_i=U^i(x)\) and \(r_j=U^j(3x)\). The dyadic telescoping identities are
\[
 -x=\sum_{a\ge0}{2^{S_a}\over3^{a+1}}
     =\sum_{b\ge0}{2^{T_b}\over3^{b+2}}\qquad\text{in }\mathbb Z_2.
\]
Indeed the physical affine identity after \(m\) odd steps reads
\[
 x+\sum_{a<m}{2^{S_a}\over3^{a+1}}
       ={2^{S_m}q_m\over3^m}.
\]
The right side has dyadic valuation \(S_m\ge m\), and the formula for the other leg follows by division by three. Each terminal is an actual odd rational. There are no hidden runtime constraints on the gaps.

Fix successive union dates \(t,t'\). Truncate both sums through date \(t\), leaving the respective tails at dates \(S_{i+1}\) and \(T_{j+1}\), both at least \(t'\). Define the real rational numbers
\[
 L=\sum_{a=0}^i2^{S_a}/3^{a+1},\qquad
 R=\sum_{b=0}^j2^{T_b}/3^{b+2}.
\]
Their reduced denominators are exactly \(3^{i+1}\) and \(3^{j+2}\) because only the last cleared term survives modulo three. Equality \(L=R\) would give \(i+1=j+2\) and then the exact endpoint identities
\[
 2^{S_{i+1}}q_{i+1}=3^{i+1}(x+L)
      =3^{j+2}(x+R)=2^{T_{j+1}}r_{j+1}.
\]
Since both endpoints are odd, the two powers of two are equal and \(q_{i+1}=r_{j+1}\). This is the coalescence alternative excluded at this cut. In fact the endpoint equality occurs at the same cumulative shortcut date. The argument uses the last retained term of *each* prefix and remains valid when the two last retained dates differ.

Put \(h=\max(i+1,j+2)\). In the other case \(H=3^h(L-R)\) is a nonzero ordinary integer. Each discarded tail starts at or after \(t'\), so \(2^{t'}\mid H\). At the real place, \(0<L<2^t/2\) and \(0<R<2^t/6\) by summing the positive geometric weights. Thus
\[
 2^{t'}\le |H|<3^h 2^t,
\]
which proves (2). The stronger upper bound \(3^h2^{t-1}\) is also available. The ordinary integer in this argument is the cross-difference of two truncated rational sums, even when the source has a very large reduced denominator.

## From local to global clocks

Put \(L_K=\min(S_K,T_K)\). At every union date \(t<L_K\), both last indices \(i,j\) are at most \(K-1\); hence \(h\le K+1\). In the half-open interval \([0,L_K)\), each leg contributes at most \(K\) dates and both share zero. Thus there are at most \(2K-1\) distinct union dates strictly below \(L_K\). The right endpoint is itself a union date. Summation of (2) proves (1).

If a leg has at most \(K\) distinct odd states, its first repeated state occurs by the \(K\)-th transition. It is then specified by a preperiod and one positive-length period contained in the first \(K\) gaps. Choose the leg with smaller clock in (1). If \(s\) is its cycle length and \(A\) the sum of the cycle gaps, then \(A\le\min(S_K,T_K)\). Every positive periodic phase is of the form \(C/(2^A-3^s)\), where \(C>0\) is its affine carry and \(2^A>3^s\). The reduced denominator of the leg is preserved for \(D\) prime to six, including under initial tripling. Thus \(D\le2^A-3^s<2^A\), giving T2's denominator bound. Finiteness of sources needs one additional observation: the entire first \(K\)-gap word of this same leg has a bounded positive integer sum. There are finitely many such words and first-repeat positions. For each prescribed period the affine fixed point is unique, since \(2^A\ne3^s\), and each prescribed preperiod lifts it uniquely by the inverse affine formulas. If this was the second leg, divide its unique source by three to recover \(x\). This proves finite cardinality without assuming a height bound.

## Scope and comparison

The rational-cycle affine formula and the odd-denominator extension are classical. Lagarias's fixed-numerator families explicitly give individual rational cycles with bounded odd periods and increasingly long division strings, so bounding one orbit by itself using only its odd period would fail. Here the additional hypothesis is the *simultaneous* rational tripling relation together with disjoint physical fates. We do not ascribe novelty to dyadic parity coding, rational-cycle classification or simple affine reconstruction. [Lagarias, Acta Arithmetica 56 (1990)](https://doi.org/10.4064/aa-56-1-33-53)

For a hypothetical ordinary least tripling disagreement from PR192, (1) applies because any common odd state would give the same convergence label. It gives no monotone height drop for the nonconvergent leg. In particular, the smaller-clock leg may be the convergent one. Long positive rational and ordinary trajectories may satisfy every finite joint-clock inequality. [PR192, least-tripling reduction](https://github.com/GettysburgResearch/collatz/blob/26f070c38ad9edd21ed7dac6efaab6554550c2a3/research/astra-minimum-source-20261124/minimal/MinimumFailure.lean)

## Exact controls and the zero branch

The distinction between a nonzero cross-difference and a merger is necessary even on ordinary positive inputs. For any \(N\ge8\), choose the positive odd \(c\le53\) with \(2^Nc\equiv19\pmod {27}\), and take \(x=(2^Nc-19)/27\). The cumulative odd dates for its first three gaps are \(0,1,2,N\), whereas those for the first two gaps from \(3x\) are \(0,4,N\). Both legs end at the exact odd integer \(c\). Substitution gives these assertions for every \(N\): the next preterminal expressions satisfy \(3U^2(x)+1=(27x+19)/4\) and \(3U(3x)+1=(27x+19)/16\). Thus deleting the merger alternative would allow arbitrarily late clocks already at \(K=3\). The carry coincidence \(19=2^4+3=2^2+2\cdot3+3^2\) is explicitly noted by Lagarias immediately after Corollary 2.1a. [Lagarias, Section 2](https://doi.org/10.4064/aa-56-1-33-53)

`check_tripling.py` verifies 20,261 local alternatives on 779 sampled rational sources, including denominator three, certifies the actual disjoint fates of all six PR200 pairs, and constructs the delayed ordinary mergers at prescribed dates up to 4096. It also exhausts the binary source cylinders for \(1\le K\le8\) after removing cylinders whose two shortcut affine maps have become identical. The resulting finite upper bounds on the smaller clock are 1, 4, 7, 12, 17, 22, 28, 33. They are bounds for possible disjoint sources; the maxima reported over unpruned cylinders need not be attained by sources with globally disjoint orbits. `TriplingCut.lean` proves the local integer coalescence-or-spacing step with the source's odd denominator, the exact odd terminal condition, and the ternary unit condition on the higher-power prefix. Neither the finite checker nor this local Lean result formalizes the entire asymptotic statement.
