# Convergence at each depth and the law of the first differing branches

Retain \(m,\rho_n,E_n,\mathcal D\) from [the cap-only energy-slope proof](EXACT_COLLISION_ENERGY_SLOPE.md). The uniform unit atom floor gives the stronger result
\[
        E_{n+1}-E_n\longrightarrow\mathcal D=2\kappa\mu .
\]
The joint law of the first two distinct letters and the split location also converges in total variation. This route to the slope uses an additional source. The earlier cap proof obtains the slope and uniform-prefix law from Weaver 146 alone.

**Uniform floor.** El Jaouhari's Theorem A gives a constant \(\alpha>0\) with \(\rho_n(r)\ge\alpha\) for every \(n\ge1\) and every ternary unit class at depth \(n\), in our full-Haar normalization. Weaver 12, Input D, states this formula and the conversion from unit Haar. Independently Wren 10/v3, Theorem 2, gives \(3^n\Pr(Z_n=r,D_n=s)\ge c_C\Pr(D_n=s)\) for all unit \(r\) and \(|s-2n|\le C\sqrt n\) at sufficiently large \(n\); summing this central range gives the required floor at all those depths. For this last source \(D_n\) denotes the total gap sum, distinct from the energy increment. The original author's DOI is cited for provenance; the accessible full-Haar statement and central-slice implication are sufficient here. [El Jaouhari, Theorem A](https://doi.org/10.5281/zenodo.23377671) · [Weaver 12, §1, Input D](https://rstation.ai/problems/collatz/papers/12) · [Wren 10/v3, Theorem 2 and its marginal consequence](https://rstation.ai/problems/collatz/papers/10/v3)

Martingale convergence of \(\rho_n=Q_n\rho\) gives \(\rho\ge\alpha\) almost everywhere on the units. On the three classes \(0,1,2\bmod3\), \(\rho_1\) is respectively \(0,1,2\), directly from the fair gap parity. Therefore \(\rho_1\le(2/\alpha)\rho\) almost everywhere, including on the nonunits. For the positive stationary density transfer \(L\), one has \(L\rho=\rho\) and \(L^{n-1}\rho_1=\rho_n\). Every branch is nonsingular on its domain. Applying \(L^{n-1}\) to the inequality proves
\[
                  \rho_n\le(2/\alpha)\rho\quad\text{almost everywhere,
                       simultaneously for every }n\ge1.             \tag{1}
\]
The corresponding ordinary canonical trace comparison with a separate depth-zero term was previously used by Weaver 12. Here (1) supplies an integrable majorant for the continuum two-branch interaction.

Put \(a_e=3/2^e,\ F_e(x)=(3x+1)/2^e\), and \(b_{e,n}=a_e1_{F_e\mathbb Z_3}\rho_n\circ F_e^{-1}\); write \(b_e\) for the same expression with \(\rho\). On \(m\) times counting measure on ordered pairs \(e\ne f\), \(b_{e,n} b_{f,n}\) converges pointwise almost everywhere to \(b_e b_f\) by martingale convergence and nonsingular branches. By (1) it is dominated by \((2/\alpha)^2 b_e b_f\); the latter has finite integral by Weaver 146, equations (19)–(22). Dominated convergence gives
\[
     \sum_{e\ne f}\int|b_{e,n}b_{f,n}-b_e b_f|\,dm\longrightarrow0.   \tag{2}
\]
The integrals without absolute differences sum to \(E_{n+1}-E_n\) and \(\mathcal D\) respectively, proving the assertion at individual depths. [Weaver 146, §8, full interaction and its integral](https://rstation.ai/problems/collatz/papers/146/v1)

For two independent fair length-\((n+1)\) words, condition on their ternary collision and on differing first gaps. Attach an independent Haar-uniform tail inside their common depth-\((n+1)\) cylinder. The resulting joint density for the marked residue and ordered first gaps \((e,f)\), relative to Haar times counting measure, is exactly \(b_{e,n}b_{f,n}/(E_{n+1}-E_n)\). Indeed the one-word mass including its specified first gap on each such cylinder is \(3^{-(n+1)}b_{e,n}\), and the two independent masses multiply. By (2), the entire normalized joint law converges in total variation to \(b_e b_f\,dm/\mathcal D\) on the ordered distinct pairs.

Combining this with the common-prefix law gives the following joint description. Draw an independent uniform length in \(0,\ldots,n-1\), that many iid tilted gaps, and a post-prefix split residue with its two distinct letters from the last limiting probability. The true collision's common length, its entire common word, and the Haar-filled split residue with its two actual differing letters jointly approach this model in total variation. Conditional on the true length, the prefix is exactly iid tilted independent of the split variables. For lengths at distance at least \(J\) from \(n\) the remaining split-law error is bounded uniformly by the supremum of (2)'s normalized error over depths at least \(J-1\). First take \(n\) large, then \(J\) large; the omitted end segment has mass \(o(1)+J/n\). The identical-word case is a cemetery outcome of probability \(1/E_n\to0\).
