# An all-clock precursor test has arbitrarily high terminating controls

Use the shortcut map \(T\) and its physical odd-departure count \(Q_m\). For a positive integer \(z\), a source domain \(D\) equal either to all positive integers or to the positive odd integers prime to three, and \(0\le n\le m\), write
\[
 N^D_{n,m}(z)=\#\{x\in D:T^m x=z,\ Q_m(x)=n\}.
\]
This counts all actual integer sources with the indicated original shortcut clock, including initial halvings when the domain includes even integers. Distinct parity words giving this pair have distinct positive sources, by determinism. Targets in one finite class are distinct, so a fixed source contributes at most once to the class at a specified clock.

On [PR 212's fixed-target compact-null correction input](https://github.com/GettysburgResearch/collatz/blob/e082b95a503d622bbbd121801f6bcadcab50df05/research/astra-infinite-descent-20261127/escape/FAIR_CLOCK_DIFFUSION.md), for every \(M\) and either indicated choice of \(D\), there is a nonempty finite synchronized class \(G\subset D\) with all of the following properties.

* Its members and their **entire** positive-integer precursor trees lie above \(M\). Every member eventually reaches \(1\).
* There is a single positive nonperiodic odd unit \(a>1\) which every member first visits after the same number of physical shortcut steps and the same number of odd departures.
* At every clock and odd grade simultaneously,
\[
              3^n2^{-m}\sum_{z\in G}N^D_{n,m}(z)\ \le\ |G|.            \tag{1}
\]

In particular an all-clock *strict gain* opposite to (1) cannot hold for every finite synchronized high unit set, even when its full past avoids a prescribed finite region. This uses genuine positive integer orbits. The condition comes from the exact finite-class obstruction on the escape side, not from an independent replacement of any branch law.

### Attainment at a fixed nonperiodic target

For each \(b\le M\) that actually reaches 1, its full orbit is a finite set. Their union is finite, independently of the fate of any other \(b\le M\). Take \(k\) arbitrarily large with \(3\nmid k\), and put \(a=(4^k-1)/3\) above this union and above \(M\). It is odd, prime to three since \(4^k\not\equiv1\bmod9\), and reaches 1 after one odd-to-odd step. Take \(k>1\), so that \(a\) is nonperiodic. No \(b\le M\) reaches \(a\), since such a \(b\) would itself reach 1 and would have contributed that vertex to the finite union. Write \(B_a\) for the full tree of starts first hitting \(a\).

For \(x\in B_a\) let \((n_x,m_x)\) be its unique first-arrival odd count and shortcut time, and define \(P_a(x)=a2^{m_x}/3^{n_x}\). Its multiplicative simple-path correction is \(x/P_a(x)\in K\subset[c,1]\), where \(K\) is compact and Lebesgue null by the stated source. This includes initial powers of two, whose native steps add no correction. For each pair \((n,m)\), the corresponding first-arrival row \(G_{n,m}=D\cap\{x\in B_a:(n_x,m_x)=(n,m)\}\) is finite, since \(x\le P_a(x)\). Different clock/count pairs have different \(P_a\) by multiplicative independence of 2 and 3.

For any subset of a row, the mass of \(x>R\) in weights \(1/P_a(x)\) is at most \(|K_{1/R}|\), up to the immaterial convention for a two-sided neighborhood. Indeed write \(H=1/P_a(x)\), constant on the row. If the subset contains \(x>R\) then \(H\le1/x<1/R\). Its \(Hx\) are distinct points of \(K\), separated by \(H\). The disjoint half-open intervals of length \(H\) based at them lie in that neighborhood. Its length vanishes as \(R\to\infty\). A fixed-target compact-null correction set suffices here.

The root row contributes \(1/a>0\). Choose \(R\) with \(|K_{1/R}|<1/(2a)\). All rows disjoint from \([1,R]\) have mass below the root row. Only finitely many other rows exist, since each start in \([1,R]\) first reaches \(a\) at most once. Hence some \(G=G_{n_0,m_0}\) attains the positive maximum \(|G|/P_G\), \(P_G=a2^{m_0}/3^{n_0}\).

If \(T^m x=z\in G,\ Q_m(x)=n\), then \(x\) first visits \(a\) at \((n+n_0,m+m_0)\). An earlier visit would place \(a\) on a closed orbit when that later visit occurs, contrary to nonperiodicity. All such \(x\in D\) therefore belong to the same row with \(P=P_G2^m/3^n\). Comparing with the maximum gives (1), including the empty prefix and all-even prefixes. No conditioning on an exact source proportion or finite depth is involved.

### Why this is the same obstruction as on an escaping class

In an escaping component define \(P(x)=x\prod_{j\ge0,\ T^j x\ {\rm odd}}(1+1/(3T^j x))\), with initial even times harmless. Uniform simple-orbit reciprocal packing gives \(x\le P(x)\le K_0x\). At any clock, \(P(T^m x)=3^{Q_m(x)}2^{-m}P(x)\). Two members of the component have the same \(P\) exactly when they reach a common future vertex at one shortcut clock and one odd grade: take any common future and use multiplicative independence for the converse. The classes are finite. PR 212 proves attainment of the maximum normalized full-class mass by compact-null source tightness; the same argument works after restricting members to \(D\) in a component with eligible sources. For the fixed maximizing \(G\), every predecessor in (1) has corrected level \(P_G2^m/3^n\), so the identical comparison gives (1). Thus (1) alone cannot distinguish the two actual situations. A bound referring to unboundedly many *later forward phases* of the same class would add information absent from the terminating control.

### Arbitrarily long physically passing futures for gate-restricted comparisons

There is also a gated version. Fix \(N\), \(p\in(1/2,1)\), and require \(W_j(p)\) on every chronological prefix through each indicated date. One can choose the above \(a\) to have at least \(N\) initial odd shortcut departures in succession and still reach 1. Indeed choose \(b\ge N+1\) and a large odd multiple \(l\) of \(3^{b-1}\). Then \(2^l\equiv-1\bmod3^b\): \(2^{3^{b-1}}\equiv-1\bmod3^b\) follows inductively by cubing, and use the odd multiplier. Let \(u=(2^l+1)/3^b\), an odd positive integer and \(a=2^b u-1\). It has at least \(b\) initial odd shortcut departures since \(a\equiv-1\bmod2^b\). After \(b\) of them it equals \(3^b u-1=2^l\), and then reaches 1. If a unit root is requested, choose the odd multiplier in \(l\) divisible by 3, ensuring \(3\mid u\) by the same congruence one power deeper. Then \(a\equiv2\bmod3\), and arbitrarily large such \(a\) avoid the same finite union.

In each first-arrival row at this \(a\) retain only \(x\in D\) which pass every prefix through their first visit to \(a\). The root is retained, so the same tightness argument attains a positive restricted maximum. Every member of that finite maximizing class passes through the visit and also through the following \(N\) steps, because the continuation begins with \(N\) odd departures. In (1) now restrict \(N^D_{n,m}(z)\) to added prefixes which themselves pass through time \(m\). They concatenate with the old passing word, and the same row comparison proves (1) at *all* \(n,m\) for this restricted test. This last construction supplies any prescribed finite passing future, with no bound comparing \(N\) to \(\log a\); it does not give an immortal member or the unrestricted test for the very same gated maximizer.

### The fair exact-row source tail must decay slowly

The rate in the compact-null source-tightness step has a separate ordinary obstruction, already visible at the known nonperiodic target \(a=5\). Use [Weaver and Wren, Paper 200 v2, Input 3.3 (3.4)](https://rstation.ai/problems/collatz/papers/200), the fixed-total genuine offset floor with one excess ternary digit. As in [the fixed-clock ordinary entropy argument](ORDINARY_ENTROPY_BUDGET.md), for all large \(r\) and each integer \(|s-2r|\le\sqrt r\) it supplies at least \(c\,2^s/(3^r\sqrt r)\) genuine positive odd unit sources \(x\) first reaching \(a\) in \(r\) odd steps with shortcut total exactly \(s\). The prescribed residue modulo \(3^{r+1}\) forces the source to be \(1\bmod3\); nonperiodicity makes these first visits. No source sampling is restarted.

At \(s=2r\) put \(P_r=a(4/3)^r\). The simple-path product gives \(c_0P_r\le x\le P_r\), uniformly in these sources. Given sufficiently large \(R\), choose the first \(r\) with \(c_0P_r>R\). Then \(r\asymp\log R\), the starting interval is above \(R\) and below \(C R\), and this one exact row has normalized mass at least \(c_a/\sqrt{\log R}\). In particular
\[
 \sup_{y,n,m} \frac{3^n2^{-m}}{y}\#
 \{x>R:\text{first at }y\text{ at }(n,m)\}
 \ \ge\ \frac{c_a}{\sqrt{\log R}}\qquad(R\ \hbox{large}).            \tag{2}
\]
One may require \(x\) to be an odd unit and \(y=5\) in (2). The disjoint \(1/P_r\)-interval argument also gives \(|K_{1/R}|\ge c_a/\sqrt{\log R}\) for every large \(R\), for the universal \(K\) and even for the fixed-root correction closure at \(a\). Thus a faster-than-every-log-power source cutoff in this normalization would be false. The stronger marked lower for support neighborhoods at the first hit of 1, and its analogue in an escaping component, were already proved in [PR 193, CRITICAL_SUPPORT_NEIGHBORHOODS](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-six-hour-20261127/escape/CRITICAL_SUPPORT_NEIGHBORHOODS.md). The argument above records a single specified nonperiodic target with the optional unit-source restriction. The [uniform first-arrival theorem](SHARP_UNIFORM_FIRST_ARRIVAL_ROWS.md) gives the matching upper at all moving ordinary targets.

For this same target let \(w_{r,s}=3^r2^{-s} N^{\rm odd\,unit}_{r,s}(a)/a\), using exact native clock/grade and retaining only odd-to-odd arrivals for the lower. For each of the \(\asymp\sqrt r\) central totals the floor gives \(w_{r,s}\ge c_a/\sqrt r\). Consequently for \(0<t\le3\)
\[
 \sum_{r,s} w_{r,s}^{\,t}=\infty,\qquad
 \sum_{\substack{r\le L\\ |s-2r|\le\sqrt r}} w_{r,s}^{\,3}
          \gg_a\log L .                                              \tag{3}
\]
All contributing classes at this nonperiodic target are distinct. This is a lower statement; (3) supplies no upper threshold at powers above three. In any escaping component the identical lower holds in the full precursor tree of any one of its fixed ordinary units. An argument seeking finite cubic mass of the full synchronized classes would already contradict the terminating control.

### The precision cost of preserving an old ordinary origin

Suppose a particular escaping unit \(a\) reaches \(z\) after an odd prefix of \(j\) letters and shortcut total \(A\), then reaches \(y\) after a further \(n\) letters of total \(s\). Its corrected heights satisfy
\[
              \frac{2^s}{3^{n+j}}
                   =2^{-A}\frac{P(a)}{P(y)} .                        \tag{4}
\]
Replacing the suffix by other genuine exact-\(s\) inverse words from \(y\) and preserving the *same* original prefix back to a possible partner of \(a\) requires its reconstructed intermediate \(z'\) to agree with \(z\bmod 3^j\). Indeed the known prefix gives \(2^A z'=3^j a'+B_{\rm old}\), which is integral in its source precisely under that congruence; its positivity is an additional condition. The suffix equation then imposes one specified congruence at precision \(3^{n+j}\) on its inhomogeneous offset. There are \(\binom{s-1}{n-1}\) positive compositions. Averaging over all such ternary classes gives exactly \(\binom{s-1}{n-1}/3^{n+j}\) words, at most \(2^{-A}P(a)/P(y)\) by (4). This bound tends to zero for large old \(j\), even without the extra central \(n^{-1/2}\) cost; \(P(y)\ge1\). The inherited suffix certifies that its *specified* cell contains a word despite this small mean. A uniformly comparable-to-mean lower estimate thus cannot force a second word for the old cell, even if extended to that full precision. It would take a genuine multiple-occupancy result conditioned on the inherited word. Formula (4) is valid at arbitrary clocks and retains the exact same ordinary origin.
