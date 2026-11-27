# How much of a true high-gain word a physical sibling can share

**PROPOSED.** Fix a genuine odd path of length \(j\) from an ordinary \(a\) to a ternary unit \(y\), with chronological valuation word \(w\), division total \(S\), and gain \(G=3^j2^{-S}\). Put \(s=4^d y+(4^d-1)/3\) for the true unit sibling, \(d\in\{1,2\}\). Assume \(y/G\le A\), with \(A\) fixed. This holds on an arbitrary hypothetical escaping ray from a fixed seed by the corrected-height identity. It also holds along each simple prefix from a fixed positive seed, with a constant depending on that seed, by reciprocal packing. In particular \(S\le j\log_2 3+\log_2 A\), since \(y\ge1\).

Give every length-\(j\) word \(w'\) of a positive physical ancestor of \(s\) weight \(3^j2^{-S'}\). Bounds below are relative to \(G\), so they also bound the mass relative to \(\rho_j(y)\ge G\).

## One long common bridge, allowing every head and tail

Let \(p_j+r_j=o(j)\). The total relative side mass of words sharing with \(w\) an aligned contiguous block after at most \(p_j\) initial gaps and before at most \(r_j\) terminal gaps is
\[
                                  2^{-j+o(j)}\quad\text{or smaller}.        \tag{1}
\]
The assertion includes arbitrary admissible heads, tails, and total valuations. In absolute whole-Haar density this family contributes at most \((3/4)^j2^{o(j)}\), because \(G\le(3/2)^j\).

For fixed actual head and tail lengths \(p,r\), the common block has \(l=j-p-r\) gaps and total \(S_B\ge l\). Let \(z,z'\) be the two positive ordinary states at the end of this block. They differ, since their remaining paths have equal length and end at the different sites \(y,s\). The affine-section identity gives \(2^{S_B}(z'-z)=3^l(b'-b)\) for the two starts of this block. Coprimality and oddness give \(2\cdot3^l\mid z'-z\). The positive affine tail formulas give \(z\le2^T y/3^r\), \(z'\le2^{T'}s/3^r\), where \(T,T'\) are their respective tail totals. Since \(s\le21y\),
\[
 \max(T,T')\ \ge\ \log_2(2\cdot3^{l+r}/s)
          \ \ge\ S-p\log_2 3-O_A(1).                                     \tag{2}
\]
The trunk has \(T\le S-j+r\). For \(p+r=o(j)\), (2) must therefore be paid by the competitor tail \(T'\). If \(r=0\) there is no such competitor for all large \(j\).

For \(r\ge1\), sum the head weights \(2^{-S_{\rm head}}\) over *all* heads, obtaining exactly one even when some are illegal. The remaining relative upper bound is
\[
   2^{S-S_B}\Pr(G_1+\cdots+G_r\ge S-p\log_2 3-O_A(1)),
 \qquad \Pr(G_i=e)=2^{-e}.
\]
The threshold is \(S-o(j)\asymp j\). At total \(t\) there are \(\binom{t-1}{r-1}\) compositions. The tail probability is \(2^{-S+o(j)}\), uniformly for these \(p,r\): at the first included total the binomial entropy is \(o(j)\), and successive summands have ratio at most \(2/3\) eventually. This proves (1) since \(S_B\ge j-o(j)\); summing over at most \((j+1)^2\) placements preserves it. Thus the positive constant floor for the full sibling row comes from other ordinary words. In [PR201's paired critical census](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/infinity-20261127/mass/CRITICAL_PAIRED_TRANSLATION.md), long common middle words can carry a positive fraction of the selected *rational* population. The proof of (1) uses the divisibility of two **ordinary** intermediate states.

## Dispersed changes at logarithmically many dates

Write \(L=\log_2 3>1\). For any fixed \(0<\epsilon<1\), the total relative mass of all compatible side words differing from \(w\) in no more than \((1-\epsilon)\log_L j\) positions satisfies
\[
                          \ll_{A,\epsilon} \exp(-c_{A,\epsilon}j^\epsilon)
                          \qquad(j\to\infty).                              \tag{3}
\]
The replacements can be anywhere and can use arbitrarily large positive exponents.

For two distinct-terminal physical paths starting from integers at most \(M\), every aligned run of \(\ell\) equal exponents starting at date \(t\) satisfies \(2^\ell\le |b_t-a_t|\le(M+1)(3/2)^t\). Indeed the starting-state difference is a nonzero multiple of the binary denominator of the run, and \(U(u)+1\le(3/2)(u+1)\). Following the run and one possible disagreement therefore moves the date to at most \(Lt+1+\log_2(M+1)\). If there are \(h\) mismatches, applying this bound to the \(h+1\) runs, allowing an extra final step, gives
\[
       j\le \big(1+\log_2(M+1)\big)\,
                            \frac{L^{h+1}-1}{L-1}.                         \tag{4}
\]
For a competitor from \(b\), positivity yields \(b\le2^{S'}s/3^j\le21A2^{S'-S}\). The trunk has \(a\le A\). For \(h\le(1-\epsilon)\log_L j\), (4) with \(M=\max(a,b)\) now forces
\[
                              S'-S\ge c_\epsilon j^\epsilon-O_A(1).
\]
Fix the \(h\) replacement slots; their old exponent sum \(E\) is \(O_A(j)\). The relative mass after allowing *all* their new exponents is at most
\[
      2^{E}\!\!\sum_{t\ge E+c_\epsilon j^\epsilon-O_A(1)}
                    \binom{t-1}{h-1}2^{-t}.
\]
For \(1\le h=O(\log j)\) the tail is bounded by a constant times its first summand, as above. Its binomial and all choices of the slots together cost at most \(\exp(O_A((\log j)^2))\). This proves (3), with the empty-replacement case excluded by the first ternary digit of the two different unit siblings.

The [finite separation kernel](WordSeparation.lean) checks the full ternary and binary difference divisibilities from the common physical section, the terminal tail payment, and the iterated disagreement-clock inequality. The section of an actual odd word is checked in [MovingScenery.lean](MovingScenery.lean). The negative-binomial entropy estimates are written arguments.

The [critical side flux](CRITICAL_SIBLING_SCENERY.md) would contradict any uniform inverse-harmonic lower comparison on a genuine escaping trunk. Equations (1) and (3) identify two aggregate families too small to supply that comparison. They leave unrestricted the population with widely distributed changes involving more than logarithmically many dates. The known off-diagonal pullback automaton counts shifted word pairs with fixed combined excess over all ternary residues; these estimates compare all competitors to one specified positive path under its physical height bound. [Paper 166, Theorem 1](https://rstation.ai/problems/collatz/papers/166/v1).
