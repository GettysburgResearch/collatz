# All moving-target first-clock Gaussian defects

**PROPOSED, source-qualified written theorem.** Let \(Q_X(y,u)\) be the proportion of positive \(n\le X\) for which the genuine shortcut orbit first hits the positive odd target \(y\) by \(\lfloor\mu\log X+ub_X\rfloor\), with \(\mu,b_X\) as in [the critical law](../CRITICAL_CORRECTION.md). Let \(d_y\) be the ordinary source density of the complete predecessor set of \(y\). Partition the escaping sources by eventual merging of their finite positive forward orbits into a shared infinite forward path. Let \(D_*\) be the largest population mass of one such component, with \(D_*=0\) if there is none. For every fixed real \(u\),
\[
 \begin{split}
  \sup_{y\ {\rm odd}}\big(Q_X(y,u)-d_y\Phi(u)\big)_+&\longrightarrow0,\\
  \sup_{y\ {\rm odd}}\big(d_y\Phi(u)-Q_X(y,u)\big)_+
                      &\longrightarrow D_*\Phi(u).                     \tag{1}
 \end{split}
\]
Both results continue to hold upon restricting the suprema to \(y\le X^\epsilon\) for any fixed \(\epsilon>0\). A nonzero \(D_*\) also forces a nonzero lower limit of the second supremum within \(y\le\exp(\eta b_X)\) for **each** fixed \(\eta>0\). The unrestricted defect detects escaped mass in the heaviest single component. It can vanish in the presence of additional bounded cycles.

The argument classifies the clock on every subsequence of targets with nonvanishing mass. It uses the prior finite-seed reduction, the every-target Gaussian and tight minimum inputs, and a uniform ordinary-source comparison for the complete predecessor indicator. It does not assume a local Gaussian theorem uniform over the targets. [PR211, finite-seed result and its source-qualified basin inputs](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/rigidity/phase12/FINITE_SEED_REDUCTION.md)

## Uniform ordinary sampling of the entire basin

For the odd map \(U\) put \(f_y(x)=1\) if the original odd \(x\) ever hits \(y\), otherwise zero. At every odd \(x\ne y\), \(f_y(x)=f_y(Ux)\). The edge from \(y\) can disagree if \(y\) never returns. Even inputs have the value at their odd part. Apply PR213's general sparse-exception label theorem at \(r=1\), with the two possible labels \(0,1\) and exceptional set \(\{y\}\). On any octave \([Z,2Z)\), its exception count is at most one, and
\[
  1\le C_A Z(1+\log Z)^{-A}\quad (Z\ge1)
\]
for a finite \(C_A\) independent of \(y\). Thus the source of the exceptional-edge sparsity is the **single target**, while the source variable in the conclusion ranges over all positives. Its all-positive octave estimate gives an absolute \(O((\log Z)^{-1/9})\) error from the limiting label probability, uniform in \(y\). Summing the octaves above \(\sqrt X\) and bounding the initial interval gives
\[
 \sup_{y\ {\rm odd}}\left|\frac1X\#\{n\le X:n\in P(y)\}-d_y\right|
             \ll(\log X)^{-1/9}.                                       \tag{2}
\]
The limiting label probability equals \(d_y\) by the fixed-target density definition. The positive source measure includes every starting integer. The bound is absolute, becoming relative on each sector \(d_y\ge\delta>0\). [PR213, general label theorem, (1)–(2), commit 5ac2b4a7](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/linear/renewal_landing.md)

In particular choose a single finite \(N\) with error below \(\delta/2\). Every odd \(y\) of density at least \(\delta\) lies on the future of some \(a\le N\). This recovers the finite-seed step also supplied by Weaver's preceding theorem. Convergent and periodic futures from these finite seeds contain finitely many sites. On any sequence of distinct growing positive-mass targets there is therefore a subsequence on a **single fixed escaping ray**.

## The clocks along an escaping ray

Write the physical ray as \(a,T a,T^2 a,\ldots\), where \(a\) escapes. Let \(C\) be its complete component, and let the integers \(i=i(X)\) tend to infinity at an arbitrary speed. Targets \(y_X=T^i a\) are now allowed to be even as well. The component density \(d_C\) is the sum of those minimum-cell masses \(p_m\) from (4) of the critical law whose fixed \(m\) eventually merges with the ray. This density exists by minimum tightness. Jointly in the ordinary source,
\[
 \Pr\{n\le X\text{ hits } y_X,\
       (\tau_{y_X}(n)-i-\mu\log X)/b_X\le z\}
                  \longrightarrow d_C\Phi(z) .                         \tag{3}
\]
Here and below the probability denotes the uniform source through \(X\).

For one fixed minimum \(m\) in \(C\), choose a merger \(T^j m=T^k a\). At all sufficiently large \(i\) the first hit of \(T^i a\) from \(m\) takes exactly \(i+j-k\) steps, by simplicity of the escaping path. A source in this minimum cell cannot already have seen \(T^i a\) before hitting \(m\), since then that same escaping site would be visited twice. On the whole cell the first clock to \(y_X\) is exactly \(\tau_m(n)+i+j-k\). On every other component it is infinite. Truncate first to finitely many minima and then release the truncation. Their joint Gaussian–minimum law proves (3), also with \(z\to\pm\infty\) by sandwiching. It proves convergence of the whole hit mass to \(d_C\). Independently, the fixed densities \(d_{T^i a}\) tend to \(d_C\) along odd sites, by nesting and the same finite-minimum argument. For that last statement, each fixed minimum in \(C\) contributes its full cell to all sufficiently far target basins, and no other component contributes.

It follows that if \(i/b_X\to\lambda\in[0,\infty]\), the unshifted deadline gives \(Q_X(y_X,u)\to d_C\Phi(u-\lambda)\), with value zero at \(\lambda=\infty\). The date \(i\) is the actual forward clock from the one fixed ordinary seed. No upper bound on its ratio to the logarithm of the target height is imposed.

## Taking the envelope

For arbitrary \(X\to\infty\) and odd targets, extract subsequences. A bounded target is eventually fixed, where the original Gaussian applies. If \(d_y\to0\), both quantities in the supremum difference tend to zero by (2). Otherwise pass to a positive density floor and use the finite-seed argument. The nonconstant growing case is exactly (3) on one ray. Its defect is nonpositive and its magnitude is at most \(d_C\Phi(u)\). These three cases prove the first limit and the required upper bound in the second.

Every escaping component has positive density under the positive-predecessor input, because its ray contains an odd ternary unit. The countable component masses sum to at most one, so if any escape exists the largest such mass is attained. Fix a unit odd \(a\) on a heaviest ray. Write \(x_j=U^j a=T^{i_j}a\) for its successive odd states. Then \(i_j\ge j\) and \(x_j\le 2^j a\). With \(j=\lceil b_X^{3/2}\rceil\) one has \(i_j/b_X\to\infty\) and \(x_j\le X^\epsilon\) for any fixed positive \(\epsilon\), proving the matching lower limit for both versions of (1). For the smaller height budget take \(j=\lfloor\eta b_X/(2\log2)\rfloor\). Then \(x_j\le\exp(\eta b_X)\) and the defect has lower limit at least
\[
     D_*[\Phi(u)-\Phi(u-\eta/(2\log2))]>0
\]
when \(D_*>0\). This uses the centered clock (3) and the deterministic inequality \(i_j\ge j\). The opposite bound in (1) also holds on these smaller search windows.

## Initial residue classes

The ordinary complete-basin law and the timed law can each be sampled on an original arithmetic progression with a uniform absolute comparison at small moduli. The counted-adjacent-merger input used in PR211 gives, up to a small fixed multiple \(J\) of \(\log X\), at most \(O(X/\sqrt{\log X})\) starting neighbors without the required synchronous merger, after the same elementary cut avoidance. For one specified \(y\), at most \(2^{J+1}\) integers hit \(y\) by time \(J\), by inverse binary branching. Outside the merger failures and those early-hit exceptions for either neighbor, their entire first-visit indicators at \(y\) agree for **any given deadline**, also for an infinite one. Thus the number of adjacent disagreements up to \(X\) has that same bound uniformly in \(y\) and the deadline, taking \(J\) small enough for the binary tree bound. On each block of \(h\) consecutive integers without a disagreement the chosen residue contributes exactly \(1/h\) of the total. Summing the other blocks and the endpoint remainder gives an absolute conditional source-frequency error \(O(h/\sqrt{\log X}+h/X)\), uniformly in the residue. The analogous positive odd comparison follows by using neighbors separated by two and the two underlying adjacent failures. Fixed moduli, or \(h=o(\sqrt{\log X})\), therefore preserve (1)–(3). This compares **original** residues. It leaves the final parent through which an escaping target receives its positive mass unspecified. [PR211 counted-adjacent source and time estimate](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/rigidity/phase3/CLOCK_DISPERSION.md)
