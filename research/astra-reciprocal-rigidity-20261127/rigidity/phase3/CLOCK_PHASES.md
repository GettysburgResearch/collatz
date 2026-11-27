# Which frequencies can survive in the two ordinary clocks?

On the cut component trees in [the point-mass theorem](CLOCK_DISPERSION.md), let \(s\) be the signed shortcut clock. Choose an independent signed integer clock \(p\) with \(p(Tn)-p(n)={\bf1}_{n\ \mathrm{odd}}\) on each retained edge, using integration along the same undirected tree. On the known component with both clocks anchored to zero at one, \(-p\) counts the actual odd inputs before one. Choices of the two origins may vary arbitrarily across the components.

For \((\theta,\phi)\in(\mathbb R/2\pi\mathbb Z)^2\) and each component \(C\) form
\[
 A_X(C)=\frac1X\sum_{n\le X,\ C(n)=C} e^{i(\theta s(n)+\phi p(n))}.
\]
If there is **no** real \(u\) satisfying simultaneously
\[
                e^{-i\theta}=2^{iu},\qquad e^{i\phi}=3^{iu},       \tag{1}
\]
then \(\sum_C |A_X(C)|\to0\). In particular, for every fixed integer \(m\ge1\), the pair \((s,p)\pmod m\) equidistributes jointly within all component rows in the following unconditional-normalization sense:
\[
  \sum_C\sum_{r,t\bmod m}
   \left|\frac1X\#\{n\le X:C(n)=C,\ (s(n),p(n))\equiv(r,t)\}
                   -\frac1{m^2 X}\#\{n\le X:C(n)=C\}\right|\to0. \tag{2}
\]
For a single row of vanishing density this gives an absolute error tending to zero. A conditional limit within that row would require error small relative to its own mass.

**Status.** Written consequence of the same counted adjacent-synchronization input as the preceding note. The full nonresonance proof uses no positive density, timed passage law, Brownian limit, or terminal-law identification. The literature already studies detailed local laws and terminal phases with those stronger inputs; see the scope paragraph below.

## Joint labels under ordinary dilations

For an adjacent pair with a counted merger by clock \(J\) before the cuts, both \(s\) and \(p\) agree initially. The simultaneous cut avoidance estimate in the preceding note therefore gives the same \(O(X/\sqrt{\log X})\) number of neighboring disagreements for the triple \((C,s,p)\). Exactly on even inputs,
\[
          (s(2n),p(2n))=(s(n)-1,p(n)).
\]
The odd edge through \(2n-1\) and the neighboring agreements at \(2n-1,2n\) and \(3n-2,3n-1,3n\) give
\[
 (s(\lceil3t\rceil),p(\lceil3t\rceil))
       =(s(\lceil t\rceil),p(\lceil t\rceil)+1)
\]
away from the same small family of unit intervals. The component labels coincide on every good comparison. Writing \(A_Y\) as the vector in \(\ell^1(C)\) obtained by the real-cutoff ceiling interpolation, this proves
\[
 \|A_{2Y}-e^{-i\theta}A_Y\|_1+
 \|A_{3Y}-e^{i\phi}A_Y\|_1\ll1/\sqrt{\log(2Y)}.                 \tag{3}
\]
This error is independent of the clocks' componentwise phases. Also \(\|A_Y\|_1\le1\) and, for real \(U,V>0\),
\[
 \|A_U-A_V\|_1\le 2|U-V|/\max(U,V) .
\]
The latter follows by separating their common initial interval and the excess interval, using pointwise unit norm of the integrand.

## Characters of the two dilations

Let \(G=\mathbb Z\log2+\mathbb Z\log3\subset\mathbb R\). The two logs have irrational ratio by unique factorization. Thus \(G\) is dense and its integer coordinates are unique. The character
\[
         \chi(a\log2+b\log3)=e^{-ia\theta+ib\phi}
\]
is well defined. For every **fixed** \(g\in G\), (3) and telescoping give \(\|A_{e^g X}-\chi(g)A_X\|_1\to0\), using the inverse dilation identity for a negative exponent. It follows that
\[
  |1-\chi(g)|\limsup_{X\to\infty}\|A_X\|_1
                \le 2(1-e^{-|g|}).
\]
A positive limsup forces \(\chi\) to be continuous at zero on \(G\). By uniform continuity and completeness of the circle it extends to a continuous character of \(\mathbb R\). Every such character is \(g\mapsto e^{iug}\) for a real \(u\): choose a continuous small argument near zero, use the homomorphism law to obtain local additivity, and then use integer subdivision to extend the linear formula. This proves (1) as a necessary condition. For \(\theta,\phi\in(2\pi/m)\mathbb Z\), (1) implies that both \(m u\log2\) and \(m u\log3\) are integer multiples of \(2\pi\). Irrationality forces \(u=0\). Finite Fourier inversion on \((\mathbb Z/m\mathbb Z)^2\), with the componentwise absolute values summed afterwards, now proves (2).

There is a second equidistribution statement for any **fixed** input progression modulo \(d\). On complete intervals of \(d\) consecutive integers, all labels agree unless at least one adjacent pair fails. The total number of affected inputs in the first \(X\) is \(O_d(X/\sqrt{\log(2X)})\). Thus the joint measure of \((C,s,p)\) on an input residue has, with full-\(X\) normalization, total-variation distance \(o(1)\) from \(1/d\) times the unrestricted measure. Combining with (2) gives independence of the two clock residues and the input residue, up to the presently observed component masses. Earlier work of Leen treats independence of stable labels from growing input moduli. [David Leen, *Joint laws and local synchronization for Collatz minima and arrival times*, section 7](https://doi.org/10.5281/zenodo.23268759) · [Comparison and precise scope, section 1](https://rstation.ai/problems/collatz/papers/13/v1)

## The exceptional frequencies are genuine arithmetic phases

On one component define \(h(n)=\log n+s(n)\log2-p(n)\log3\). On a retained even edge this is constant. On a retained odd edge it increases by \(\log(1+1/(3n))\). The pathwise reciprocal packing recalled in the [ordinary normalization proof](../ORDINARY_SPECTRUM.md) therefore bounds \(h\) on every component after fixing the two origins. The bound allows different centers on different components. At a frequency satisfying (1) there is the exact identity
\[
            e^{i(\theta s(n)+\phi p(n))}
                         =n^{iu}e^{-iu h(n)}.                       \tag{4}
\]
Thus (1) leaves a concrete surviving observable. It does not guarantee a nonzero coefficient for every resonance. For nonzero squared-slope weights \(a_n\) anchored on this component, the precise relation is \(\log(n^2a_n)=2h(n)+\text{constant}\).

One can give a precise conditional nonvanishing statement. Let \(C\) be a fixed component and \(B_X=X^{-1}\sum_{n\le X,C(n)=C} e^{-iu h(n)}\). For every fixed \(v>0\),
\[
                           B_{vX}-B_X\to0.                           \tag{5}
\]
For \(v=2,3\) use the previous good comparisons. On a rounding cell, its arithmetic multiplier \(\lceil vt\rceil/(v\lceil t\rceil)\) gives a logarithmic error \(O(1/\lceil t\rceil)\); (1) cancels the clock shifts. This proves both generator cases with vanishing error. Inverting, multiplying, and using the cutoff continuity bound extend (5) from the dense two-generator subgroup to every \(v>0\). Since signed averages are uniformly bounded, applying (5) at the finitely many endpoints of step functions gives
\[
 \frac1X\sum_{n\le X,C(n)=C}(n/X)^{iu}e^{-iu h(n)}
                   - B_X\int_0^1 v^{iu}\,dv \to0 .
\]
Approximate on \([\epsilon,1]\) by step functions and bound the discarded interval by \(2\epsilon\). Combining with (4) gives \(X^{-iu}A_X(C)=B_X/(1+iu)+o(1)\). If \(C\) has positive upper density, boundedness of \(h\) shows \(\limsup |B_X|>0\) for all sufficiently small \(|u|\): rotate the phase by the midpoint of the bounded range and take its real part. Hence some nonzero resonances genuinely survive under this explicit density hypothesis.

**Literature and scope.** David Leen's 2026 Brownian and synthesis preprints give much sharper local arrival-clock and terminal-phase descriptions for the laws they cover. The 2026 terminal-law paper of Lyapunov Weaver uses these and develops dimension and singular-continuity results for positive-density orbit-minimum cells. The component signed-clock gauges here can also be chosen in escaping trees. Equations (1)–(3) provide a short consequence of the counted adjacent estimate, with error summed across all components. No priority is claimed for scalar local hitting-time bounds in the basin of one, for terminal phase laws, or for input-residue independence. The individual positive-density and timed-passage results have not been independently rebuilt here and are not assumptions of (1)–(3). [Leen, *Brownian motion in Collatz orbits*](https://doi.org/10.5281/zenodo.23252395) · [Leen, *The stochastic 3x+1 model is a theorem*](https://doi.org/10.5281/zenodo.23652463) · [Weaver, *Natural Collatz terminal laws, clock phase, and orbit minima*, sections 1, 9–11](https://rstation.ai/problems/collatz/papers/175/v1)
