# A finite common-exit experiment recovers ordinary component masses

**Source-qualified written theorem.** Use the shortcut map \(T(2x)=x,\ T(2x+1)=3x+2\). Components are defined by intersection of ordinary forward orbits at independently chosen clocks. A finite partition refines the actual component partition at every size. The total mass it separates from the largest piece in each true component tends to zero. The experiment distinguishes the mass of escaping components from that of bounded components even when the extra height threshold grows arbitrarily slowly.

## The experiment

For a positive integer \(X\), take \(K_X=436(1+\lfloor\log_2 X\rfloor)\) and any computable integers \(R_X\ge1\) tending to infinity. For each \(1\le n\le X\), compute the *least value* \(m_X(n)\) visited through clock \(K_X\), including the starting state. Restart at that observed value.

* If \(m_X(n)>R_X\), give this source a unique unresolved label.
* Otherwise follow the actual steps until the first state above \(R_X\), or until a state repeats. In the former case output the tagged exit integer. In the latter case output the tagged minimum of the detected cycle.

There are at most \(R_X\) additional steps since distinct states before either event lie in \([1,R_X]\). The table of admitted seeds can be shared across all sources. A bounded source can produce an exit at finite cutoff. **Equal labels of different sources always certify a physical meeting**, because both original paths reach that exit or the same cycle.

Write \(p_{C,X}=\#(C\cap[1,X])/X\). In each actual component \(C\) let \(p_{C,\ell,X}\) be the fraction carrying label \(\ell\), with the same denominator \(X\). Every nonempty label belongs to one true component. Then
\[
 E_X=\sum_C \bigl(p_{C,X}-\max_\ell p_{C,\ell,X}\bigr)
               \longrightarrow 0.                                      \tag{1}
\]
Absent components contribute zero. The fraction of sources whose output type disagrees with their true bounded/escaping type also tends to zero, counting unresolved outputs as errors. For example \(R_X=1+\lfloor\log_2(2+\lfloor\log_2 X\rfloor)\rfloor\) gives total physical duration \(O(\log X)\). The result provides no effective error modulus.

## A finite seed set captures the population

Mazur's raw-map theorem gives, for every \(f(n)\to\infty\), a natural-density-one set of starts finding a value below \(f(n)\) within \(436\log n\) unaccelerated steps, with the natural logarithm. A skipped raw value \(3u+1\) exceeds its preceding odd state \(u\). Thus a first strict visit below a threshold cannot be a skipped value, and the shortcut finds a visit within the same upper clock. Our integer clock exceeds it. [Mazur, July 2026, raw-map density theorem](https://www.proofatlas.ai/formalizations/natural-density-log-time-collatz/) · [Repository source audit at public revision ca3dd0d63920411213403092aecc6946619eb082](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/external/mazur-2026/natural-density-log-time.md)

Put \(g(n)=m_n(n)\). The stated theorem implies
\[
 \lim_{M\to\infty}\limsup_{X\to\infty}
 X^{-1}\#\{n\le X:m_X(n)>M\}=0.                                      \tag{2}
\]
Indeed \(m_X(n)\le g(n)\) for \(n\le X\). If the upper densities of \(g(n)>j\) exceeded a common positive \(\delta\) for every positive \(j\), choose increasing endpoints \(X_j\) so that at least \(\delta X_j/2\) indices in \((X_{j-1},X_j]\) satisfy \(g(n)>j\). Setting \(f(n)=j\) on these consecutive blocks contradicts Mazur's theorem.

Fix \(M\). All bounded starts through \(M\) have finite complete forward orbits. Above some common \(R(M)\) their continuations report their actual cycles. In every escaping component represented through \(M\), the finitely many represented seeds join one common ray. Choose a shared vertex after their physical mergers. Increase \(R(M)\) beyond all heights between those seeds and their shared vertex. For every \(R\ge R(M)\), the first exit from \(R\) exists and is the very same integer for those seeds. Distinct components cannot have a common exit. This proves existence of the onset without giving a uniform test for having reached it.

Since \(R_X\to\infty\), all sources with \(m_X(n)\le M\) eventually receive one common, correctly typed label per represented component. The remaining proportion in (2) bounds both \(E_X\) and the type error. Increase \(M\). Choosing the least observed value is material to this argument. An arbitrary first visit below the growing \(R_X\) can have value tending to infinity.

## Finite energy and spectrum

Let \(r_{\ell,X}\) be the empirical label masses. For two independent uniform original sources,
\[
 0\le\sum_C p_{C,X}^2-\sum_\ell r_{\ell,X}^2\le 2E_X.                 \tag{3}
\]
A pair in the same component but different pieces has at least one member outside its component's largest piece. The same argument for \(q\) independent sources gives \(qE_X\). For every real \(q\ge1\) the same bound follows by \(q\)-Lipschitz continuity of \(u^q\) on \([0,1]\), retaining the largest piece. The exit-only sum differs by \(o(1)\) from \(\sum_{C\ {\rm escaping}}p_{C,X}^q\): align one correctly typed good piece per component in the finite-seed proof and charge all remaining mass to (2).

Split each mass \(p_{C,X}\) into its output pieces. The decreasing rearrangements of the two lists, padded by zeros, have \(\ell^1\) distance at most \(2E_X\). Before rearrangement, align each largest piece with its original mass and charge every remaining piece twice. Sorting reduces or preserves the distance. The equality matrices \(A_{ij}=X^{-1}{\bf1}_{i,j\ {\rm eventually\ meet}}\) and \(B_{ij}=X^{-1}{\bf1}_{i,j\ {\rm have\ equal\ outputs}}\) have exactly these mass lists as their nonzero eigenvalues. Their squared Hilbert–Schmidt distance equals the left-hand difference in (3). The normalization by \(X\) is essential. For conditional-expectation projections normalized by each block size, even one strict split creates a unit vector in the finer range orthogonal to the coarser range, giving operator-norm distance one.

If each component has a natural density \(d_C\), then \(\sum_C|p_{C,X}-d_C|\to0\). Equation (2) places all but arbitrarily small mass in the finite set of components represented through a sufficiently large fixed \(M\). On each such finite list, ordinary natural convergence suffices. Consequently the ranked output spectrum converges in \(\ell^1\) to the decreasing component densities and
\[
 \sum_{\ell\ {\rm an\ exit}}r_{\ell,X}^q
     \longrightarrow \sum_{C\ {\rm escaping}}d_C^q,\qquad q\ge1.        \tag{4}
\]
The same good-piece alignment gives the type-specific ranked spectra and the mass of each specified cyclic component. The component natural-density premise is separate from (1)–(3). [Sultanow, Corollary 4 for completely invariant sets of positive 3x+1](https://www.preprints.org/manuscript/202610.2552) · [PR213, ordinary component density inputs at 5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/mass/DENSITY_COORDINATE_AND_TRACE.md)

## Two qualitative tests need only the two Mazur inputs

Mazur's separate positive-predecessor theorem gives a positive target-dependent lower natural density for the predecessor basin of every fixed target prime to three. Each component contains an odd unit target: after an odd departure its next odd landing is a ternary unit. A raw visit to an odd target survives shortcutting. Thus on the July and September inputs,
\[
 \begin{aligned}
 &\text{every positive orbit is bounded}
     &&\Longleftrightarrow\quad
        \liminf_X\sum_{\ell\ {\rm an\ exit}}r_{\ell,X}^2=0,\\
 &\text{every positive orbit reaches one}
     &&\Longleftrightarrow\quad
        \limsup_X\sum_\ell r_{\ell,X}^2=1 .
 \end{aligned}                                                         \tag{5}
\]
A single escaping component contains a positive lower fraction of the original sources, and the typed version of (3) retains its square. If there is any component besides the cycle of one, both have positive lower fractions. Even the true two-source meeting probability is then bounded below one by the two cross orders. The reverse implications follow from (1)–(3) when the respective boundedness or single-component condition holds. [Mazur, September 2026, fixed-target lower-density theorem](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

A separate prior capped-graph theorem uses the graph induced by \([1,X]\) for all starts through \(X\). It gives largest-component and escape criteria together with fixed-component masses scaled by an early-excursion constant \(\kappa\). That experiment permits an initial high excursion to split a component even in the limit. Our two-stage experiment reads the minimum before applying its slowly growing cap, recovering all the mass and an \(\ell^1\) partition approximation. [Weaver, discussion 111, capped-graph results and prior inputs](https://rstation.ai/r/collatz/posts/111)

PR211's fixed-basin short-arrival argument already explains why a logarithmic clock detects almost all members of the basin of one. Its separate superlogarithmic variance statistic compares odd frequencies. Its first-crossing budgets already count the eventual number of escaping components among fixed finite seeds. The experiment above recovers the whole population's component-mass partition without supplying component labels or aligning arrival clocks. **OPEN:** an independent estimate forcing either energy in (5) to the required endpoint. [PR211, source variance at 4b44cded44af5bb7c3ce67fb16a70c898ad505d5](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/descent/postpeak/stopped/SOURCE_VARIANCE.md) · [PR211, finite-seed first-crossing budgets](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/rigidity/phase10/FIRST_CROSSING_BUDGET.md)
