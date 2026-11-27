# The smaller odd parent and fixed-grade distortion

**Status.** Written ordinary deductions. Finite residue searches are exploratory. This analysis keeps one hypothetical escaping component and the grade of its specified ordinary source.

## The actual parent and the loss it measures

For each odd integer \(y\), let \(D(y)\) be the odd integer with \(y=3D(y)+2b\) for \(b\in\{-1,0,1\}\). Let \(R f(v)=3\,2^{-e(v)}f(Sv)\) on positive odd integers, where \(e(v)=v_2(3v+1)\). The operator \(\mathcal A\) of [the grade comparison](ORDINARY_TRANSLATES.md) sends each source equally to its three ternary children. Thus exactly
\[
 (\mathcal K f)(v):=(R\mathcal A f)(v)=2^{-e(v)} f(D(Sv)).
\]
The inverse children of \(q=D(Sv)\), indexed by \(e\ge1\), are
\[
 v_e(q)=2^e q+\frac{(-1)^{e+1}2^{e+1}-1}{3},\qquad
 S(v_e(q))=3q+2(-1)^{e+1}.
\]
The congruence modulo three selects the displayed sign, and \(3v_e(q)+1=2^e(3q+2(-1)^{e+1})\) gives the exact valuation. Each child of a positive odd \(q\) is positive odd. Its parent is strictly smaller when \(v>1\): for \(q\ge3\), \(v_e(q)\ge 2^e(q-2/3)-1/3>q\); for \(q=1\) only a child equal to one can give equality. The column masses \(2^{-e}\) sum to one. Consequently \(\mathcal K\) is stochastic. Its parent map reaches one from every ordinary start.

On an escaping component with grade measure \(\eta_j=\mathbf1_{g(v)=j}/P(v)\), the corrected-height cocycle gives \(\eta_j=R\eta_{j+1}\), including zeros off the component. Therefore
\[
       (I-\mathcal K)\eta_j=R(\eta_{j+1}-\mathcal A\eta_j).        \tag{1}
\]
If \(q_j\) is the smallest vertex of grade \(j\), then \(D(Sq_j)<q_j\), so the left side evaluated at \(q_j\) is exactly \(1/P(q_j)\). This includes the original component minimum in its own grade. The larger norm on the right is a difference of ordinary one-arm measures. A source present on just one side contributes full weight to the norm and zero to a Hellinger affinity.

The good transient target \(z=5\) also has
\(\|m_{p-1,z}-\mathcal A m_{p,z}\|_1\to0\) with nonsummable errors as \(p\to\infty\). Indeed the masses tend to \(h(5)>0\), and \(1\) never reaches 5. For each fixed \(p\), \(\mathcal A^t m_{p+t,5}\) is supported above \(2\cdot3^t\). The contraction and disjoint-support argument in (5) of [the grade comparison](ORDINARY_TRANSLATES.md) force the entire tail sum of errors to exceed \(2h(5)-o_p(1)\) at every large starting depth. A summability proof specific to escape would have to use more information than this one-sided inverse-layer behavior.

## Limit spectrum in one fixed actual grade

Write \(R_C(v)=P(v)/v=\prod_{t\ge0}(1+1/(3S^tv))\) for positive odd \(v\) in the escaping component. Fix a grade \(j\). Given any distinct sequence \(v_i\) of that grade, pass to a subsequence on which each positive integer sequence \(S^t v_i\), for fixed \(t=0,1,\ldots\), is constant or tends to infinity. The initial sequence tends to infinity. If \(t\) is the first constant time with state \(u\), then the product of the first \(t\) factors tends to one, so
\[
            R_C(v_i)\longrightarrow R_C(u),\qquad R_C(v_i)>R_C(u).
\]
If every fixed-time state tends to infinity, fix a floor \(F\). The only possible times of a visit to an ordinary \(u\le F\) in this component are \(g(u)-j\ge0\), a finite list. Eventually no forward state is that small. The uniform distinct-path reciprocal bound gives \(\log R_C(v_i)\le T(F)/3\) with \(T(F)\to0\). Hence \(R_C(v_i)\to1\) from above. [Uniform simple-path tail and corrected heights](FIXED_FLOOR.md) · [Paper 176 v1, §1, source of the packing bound](https://rstation.ai/problems/collatz/papers/176/v1)

Thus every limit point is in the countable set \(\{1\}\cup\{R_C(u):g(u)>j\}\). There is no infinite strictly increasing sequence of grade-\(j\) ratios: a purported increasing sequence would have a subsequence strictly above its limit by the preceding alternatives. Every nonempty subset of their distinct values consequently has a largest member.

There is also a dyadic location statement. For any fixed \(\epsilon>0\), a grade-\(j\) source with \(R_C(v)\ge1+\epsilon\) must hit \([1,F_\epsilon]\), by the uniform simple-path bound. Its first such odd depth is bounded by a constant \(t_{j,\epsilon,C}\), since a visit to \(u\) has the prescribed grade difference. At each fixed depth \(t\), the set of all positive odd predecessors of a finite target occupies at most \(O_t((1+h)^t)\) residues modulo \(2^h\): in each inverse composition, replacing an exponent exceeding \(h\) by \(h\) preserves its residue as an affine map on the odd dyadics. Summing over the finite targets and depths gives the same polynomial bound with an enlarged exponent. In particular this positive-excess set has dyadic upper box dimension zero.

If a sequence of distinct grade-\(j\) sources also converges dyadically to an odd \(\xi\) with infinitely many odd departures under the shortcut, each fixed finite list of its odd gaps is eventually shared by the sources. The resulting affine map has positive slope, so their fixed-time real states tend to infinity. The preceding argument forces \(R_C(v_i)\to1\). A limiting dyadic point with finitely many odd departures lies in the backward orbit of \(0\), since a dyadic point divisible by every power of two is zero. Thus all positive-excess accumulation in this fixed grade occurs over a countable dyadic exceptional set.

### Two-sided isolation of the actual moving atom

In fact each individual odd \(v\) is isolated on both sides in the grade-\(j\) set of ratios, and has a unique value there. If two odd \(v,u\) have the same ratio, joining their forward trajectories gives
\[
                 u/v=P(u)/P(v)=2^h3^{g(u)-g(v)},\qquad h\in\mathbb Z.
\]
Oddness forces \(h=0\); in the same grade this gives \(u=v\). At a higher grade any such \(u\) is divisible by three. But the first constant iterate on a convergent sequence of distinct same-grade starts has positive odd depth and hence is a ternary unit. Its ratio cannot equal \(R_C(v)\); nor can the other possible limit \(1\). This proves the two-sided isolation.

Equivalently, for any fixed source \(v\) of grade \(j\), its word's real affine offset is uniformly isolated *after division by the moving ordinary terminal* from the offset of every other legal inverse word of the indicated odd depth. At large \(n\) all forward paths from \(v\) have joined \(a_n=S^n a_0\) by depth \(n-j\). For any source \(w\) in that layer, with its actual affine offset \(F(w,n)\),
\[
        F(w,n)/a_n=1-\frac{P(a_n)}{a_nR_C(w)} .
\]
The ratios are uniformly bounded and \(P(a_n)/a_n\to1\). The isolation of \(R_C(v)\) therefore gives a fixed positive separation in this displayed real coordinate for every \(w\ne v\) and every sufficiently large \(n\), regardless of the total division count. The existing posterior identifies the limiting atomic law of this coordinate; isolation concerns the complete support of the finite-depth fibres. [PR193, posterior source and affine intercept](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/global/POSTERIOR.md) · [Weaver, fixed-target stationary real fibres in Paper 19 v2](https://rstation.ai/problems/collatz/papers/19)

More precisely define \(K_j=\{1\}\cup\{R_C(u):3\nmid u,\ g(u)\ge j\}\), using positive odd \(u\). These subsets of the real line are compact and their sets of accumulation points obey
\[
                         K_j'=K_{j+1}.
\]
For an unbounded sequence of grades tending to positive infinity all future states eventually avoid each fixed floor, so all ratios tend to one uniformly. At bounded grades pass to one fixed grade and use the classification above; each limiting higher-grade state is a unit. Conversely, let \(u\) be a unit of grade \(j+t,\ t\ge1\). Choose an odd unit predecessor of \(u\) using arbitrarily large exponents in a suitable class modulo six, then take \(t-1\) bounded unit inverse steps (at each stage some exponent from \(1,\ldots,6\) leads to a unit). The new grade-\(j\) starts and their first \(t-1\) successors tend to infinity, hence the ratios of these distinct starts tend to \(R_C(u)\). Distinct unit vertices in all grades have distinct ratios, by the lattice calculation. The value one is also an accumulation point from the ray \(a_n\). Iterating gives \(K_j^{(t)}=K_{j+t}\) for finite \(t\), and their intersection is \(\{1\}\); one more derivative is empty. Here the superscript denotes successive sets of accumulation points, not an iterate of the Collatz map.

### A macroscopic offset requires almost the whole actual backward clock

For a legal inverse word of \(h\) odd steps from \(a_n\) with source \(v\), affine offset \(F\), and its \(h\) positive odd predecessors \(z_i\), one has
\[
        1-F/a_n=\prod_{i=1}^h(1+1/(3z_i))^{-1}.
\]
Their grades range from \(n-h\) to \(n-1\). For fixed \(\delta>0\), choose a floor \(F_\delta\) with \(T(F_\delta)/3<-\log(1-\delta)\). If \(F/a_n\ge\delta\), at least one \(z_i\le F_\delta\). Hence
\[
        h\ge n-G_{C,\delta},\qquad
        G_{C,\delta}=\max\bigl(\{g(u):u\in C,\ u\le F_\delta\}\cup\{0\}\bigr).
\]
In particular any \(O(\log a_n)\)-length prefix of a proposed backward steering route has relative offset tending uniformly to zero on a subexponential escape. This uses its actual supplied endpoint and all finite inverse words.

A related set equality holds simultaneously at all depths. Write \(D_j=\{R_C(v):g(v)=j\}\). For each \(\delta>0\), all sufficiently large \(n\) satisfy
\[
 \{R_C(v):S^hv=a_n\}\cap[1+\delta,\infty)
      =D_{n-h}\cap[1+\delta,\infty)\qquad(h\ge0).                    \tag{2}
\]
Choose a fixed floor forcing every source with \(R_C(v)\ge1+\delta\) to visit it. Every one of the finitely many component vertices through that floor joins the ray by a finite index. If \(n\) exceeds all these indices and grades, any such source of grade \(n-h\) traveling through the small vertex must visit \(a_n\) in exactly \(h\) odd steps. The other inclusion follows from the grade. Thus positive relative offsets reflect a fixed ordinary finite-height entrance, even when the endpoint grows without bound.

For an iid geometric backward word, \(\beta_n=\beta_h+\omega_h\beta'_{n-h}\), where the primed real offset is independent, \(\omega_h=3^h2^{-D_h}\), and \(\beta_n\) is the outermost-first real offset. If \(0<s<1\), then
\[
 E[(\beta_n-\beta_h)^s]\le C_s\rho_s^h,\qquad
 \rho_s=3^s/(2^{1+s}-1)<1,
\]
by subadditivity on the nonnegative series and independence. Take \(h=n-G_{C,\delta/2}-1\). Every prefix legal at \(a_n\) has \(\beta_h<\delta a_n/2\) by the physical bound above. Consequently all words in its actual fibre with \(\beta_n\ge\delta a_n\) belong to an unconditional event of probability at most
\[
                  C_{s,\delta,C} a_n^{-s}\rho_s^n.                  \tag{3}
\]
This remains exponential when \(a_n\) is polynomial in its odd index. The first reversed letters set the low ternary trits; freezing a large real excursion in these letters does not preserve the supplied terminal congruence. The proportional marked result instead freezes the *last* reversed letters. Bound (3) identifies the loss for a macroscopic real mark without asserting that an exponentially small unconditioned event is empty. [Weaver, Paper 9 v2, the real tail decomposition (B5)](https://rstation.ai/problems/collatz/papers/9)

There is a one-step marked consequence retaining an actual unit \(m=a_0\). Put \(r_m=1-1/R_C(m)>0\). For a continuous \(G:[0,1]\to[0,1]\) use the physical real-marked trace
\[
 \mathcal T_d(y;G)=\frac1{P(y)}\sum_{S^dv=y}
        3^d2^{-D_d(v)}G(F(v,d)/y).
\]
For each fixed integer \(j\), equations (3) in [the ordinary grade comparison](ORDINARY_TRANSLATES.md) and the uniform convergence \(P(a_n)/a_n\to1\) give
\[
 \mathcal T_{n-j}(a_n;G)\ \longrightarrow\
       \sum_{g(v)=j}\frac{G(1-1/R_C(v))}{P(v)} .
\]
All sums are bounded by the finite mass of the indicated grade. In grade zero the support point \(r_m\) is isolated and has weight \(1/P(m)\). There is no grade \(-1\) atom at exactly \(r_m\), since an odd point with that ratio would equal \(m/3\) and \(m\) is a unit. Choose a fixed continuous piecewise-linear bump equal to one at \(r_m\) and supported in a small enough neighborhood that the entire grade \(-1\) mass there is below \(1/(4P(m))\); this uses continuity of a finite measure from above. It follows that
\[
 \liminf_n [\mathcal T_n(a_n;G)-\mathcal T_{n+1}(a_n;G)]
                      \ge 3/(4P(m)).
\]
This distinguishes adjacent depths even if their total unmarked masses agree. Paper 19 gives fixed-root averaged real fibres and a stationary full-support law. Paper 9 gives real localization in Haar norms. Neither supplies a bound for this difference along the specified moving ordinary ray. [Paper 19 v2, (F3), (F9), (Q1) and its arithmetic scope](https://rstation.ai/problems/collatz/papers/19) · [Paper 9 v2, Theorem 18](https://rstation.ai/problems/collatz/papers/9)

## Realizing every early word in the same grade

This fixed-grade real restriction is compatible with complete dyadic richness. Let \(a_n=S^na_0\) be the escape ray whose grade origin is \(a_0\). There are absolute \(\delta>0,F,C\) such that, for any fixed grade \(j\), every sufficiently large \(n\), and every forward gap word \(w\) of length \(L\le\delta(n-j)\), a grade-\(j\) actual ancestor of \(a_n\) begins with \(w\). Here the word and its total can be prescribed with no individual gap cap. The *free* suffix has a logarithmic individual cap, bounded real affine offset and exact total twice its length.

To see this let \(b=n-j-L\), shrink \(\delta\) if needed, and use the proof of Paper 48 v2 Theorem 8, equations (76), (82)–(83), with the supplied integer \(a_n\). Its fixed-cylinder floor is spread to every unit residue at length \(b\), total exactly \(2b\), for all sufficiently large \(b\) and \(L\le\delta_*(b-1)\). Prescribe the inverse output \(y\) to lie in the unit class \(F_w\bmod3^L\), where \(F_w\) is the affine offset of the prescribed forward word. This residue is a unit for nonempty \(w\); \(L=0\) needs no restriction. The resulting positive odd \(y\) is the endpoint of a legal inverse lift of \(w\), yielding the claimed source \(v\). For the full forward word, its offset is bounded by
\[
          F_{\rm full}\le F+(3/4)^b(3/2)^L.
\]
This follows by composition with the suffix multiplier \(3^b2^{-2b}\) and the elementary bound \(F_w<(3/2)^L\) for all nonempty words. Choose \(\delta\) small enough to bound the last term. The corrected-height and affine identities now give
\[
             R_C(v)=\frac{P(a_n)}{a_n-F_{\rm full}}\longrightarrow1
\]
uniformly over the prescribed words. Thus these actual sources in *one fixed grade* may fill all allowed dyadic prefixes while their real ratios approach the single value \(1\). In particular each odd dyadic cylinder contains infinitely many actual sources of every one fixed escaping grade: extend a compatible initial word by suitably many \(1\)'s to force its odd length to infinity, keeping it within the linear range. Alternatively, already at fixed nonempty \(w\) the produced source heights tend to infinity since the fixed prefix slope times \((3/4)^b\) tends to zero and \(a_n\to\infty\). [Weaver and Wren, Paper 48 v2, §§8–9](https://rstation.ai/problems/collatz/papers/48)

## Branching test and an ordinary good control

Suppose a common-clock affine merger is available between \(q\) and \(3q+2(-1)^{e+1}\). At fusion the first arm has exactly one more odd departure, by the initial slope ratio. The child \(v_e(q)\) is therefore in the same grade as \(q\), with \(P(v_e(q))=2^eP(q)\). For even \(e\), \(v_e(q)<2^e q\), hence \(R_C(v_e(q))>R_C(q)\). There can be no infinite chain of such successful even children in a fixed escaping grade. More generally, for arbitrary successful exponents and \(E_t=\sum_{i=1}^t e_i\), \(P(v_t)=2^{E_t}P(q)\); uncountably many distinct limits of \(v_t/2^{E_t}\) are impossible by the countable spectrum. These observations do not assert that any child merger always exists.

Even a single uniformly certified even-child chain is obstructed on good ordinary points. If \(q\) reaches the cycle \(1,2\), set \(P_{\rm cyc}(q)=2^{H-2p}\) using any hit of 1 after \(H\) shortcut clocks and \(p\) odd departures. The value is independent of whole laps. The same child merger gives \(P_{\rm cyc}(v_e(q))=2^eP_{\rm cyc}(q)\). At an odd source reaching 1 for the first time in \(\tau\) odd steps, \(P_{\rm cyc}(q)/q=(3/4)^\tau/f_\tau(q)\), with \(f_\tau\) uniformly bounded below on the distinct first-hit path. Moreover \(v_t/2^{E_t}\le q+2\) along any child path, from the displayed affine formula and a convergent geometric sum. An infinite path therefore has its first-hit times uniformly bounded. At bounded odd depth, a subsequence with fixed \(\tau\) and each intermediate vertex constant or tending to infinity makes the ratio approach its limit from above whenever the positive starting vertices diverge. This excludes a strictly increasing sequence along even children and excludes uncountably many real asymptotic slopes on a uniformly successful perfect tree. Every nonempty initial dyadic cylinder contains a good point by the marked trace at \(z=1\).

For an explicit sparse family of necessary failures, fix a positive even integer \(a\), and put \(x_n=3^n a+1\). At infinitely many \(n\), \(x_n\) and \(x_{n+1}=3x_n-2\) admit no common-clock affine fusion. Otherwise all sufficiently late pairs have a common component and the indicated count difference of one at fusion. On escape, \(g(x_n)=g(x_N)+n-N\) and \(P(x_n)=3^{n-N}P(x_N)\). But the minimum future height tends to infinity on grades tending to positive infinity: for each fixed \(F\), all grades of states through \(F\) are bounded above, while future grades only increase. Thus \(R_C(x_n)\to1\), contradicting \(P(x_n)/x_n\to P(x_N)/(3^N a)>1\).

If the common component instead has a positive cycle, let \(\bar e\) be its ratio of shortcut period to odd count. Then \(2^{\bar e}>3\) from the strictly positive affine intercept per lap. Choose a cycle vertex \(c\); \(P_*(x)=2^{H-\bar e p}\) using any hit of \(c\) is well defined. At first hit the distortion gives \(2^H/3^p\ll_c x\), since the departing states are distinct; hence \(P_*(x)\ll_c x\). Each putative affine fusion gives \(P_*(x_{n+1})=2^{\bar e}P_*(x_n)\), whose repeated growth contradicts \(x_n=3^na+1\). A positive orbit is either eventually periodic or consists of distinct states tending to infinity, covering the two cases. This conclusion concerns the specified affine and clock condition; the two sources may lie in the same basin.

The [finite graph probe](probe_parent_graph.py) tested exact common-clock slope agreement modulo \(2^h\) for both signs, then removed vertices without any remaining certified child. No directed cycle survived at the tested depths. [Finite records](../../../reports/astra-sixhour-20261127/transport/parent_graph_probe.txt)

**Open step.** A source-specific upper bound on cumulative graded dilation loss, or positive-excess fixed-grade sources realizing an impossible increasing or uncountable real spectrum, would exclude the proposed escape. The known fractional-depth routing fills dyadic prefixes near real ratio one. Neither it nor fair one-arm coalescence bounds the cumulative loss at the original ordinary point.

**Checked scope.** [OddParent.lean](OddParent.lean) verifies the exact two parity classes of the positive odd-parent inverse-child identity. The compactness, source routing and real-trace deductions are written mathematics. [Strict Lean output](../../../reports/astra-sixhour-20261127/transport/odd-parent-lean.txt)
