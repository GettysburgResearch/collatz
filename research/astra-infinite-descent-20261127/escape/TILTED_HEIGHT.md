# All-depth tilted mass at a positive integer target

For a positive odd target \(y\) prime to three, let \(A_p\) count positive odd unit-preserving inverse edges with weight \(3p(1-p)^{e-1}\), as in [the sparse clock calculation](SPARSE_TILT.md). Write \(a=3/2\),
\[
 s=-\log_2(1-p),\qquad D_s=3p(2/3)^s,\qquad
 \gamma=\frac{\log(3p)}{\log(3/2)}.
\]
For each fixed \(3/4<p<1\), one has \(2<\gamma<s\), \(D_s=a^{\gamma-s}<1\), and for every \(N>0\)
\[
 \sum_{d\ge0} A_p^d1(y)
 \ \ll_{p,N}\ \frac{y^\gamma}{(1+\log y)^N}. \tag{1}
\]
This is a target-height upper bound on the entire uncut, normalized inverse mass. It includes every visit at periodic targets. Weaver's stronger source estimate yields, for all sufficiently large \(y\),
\[
 \sum_{d\ge0} A_p^d1(y)
 \ \ll_p\ y^\gamma
 \exp[-c_p\log\log y\cdot\log\log\log y] \qquad(c_p>0). \tag{2}
\]
The critical fair law and the endpoint \(p=3/4\) have different bounds, given below.

## Archimedean size and the actual source

A compatible depth-\(d\) path from the positive ordinary source \(x\) to \(y\), with exponent sum \(S\), has multiplier \(\omega=3^d2^{-S}\). Its contribution is exactly \(D_s^d\omega^s\). Recovering the positive affine remainder gives \(x\omega\le y\); each of the \(d\) gaps is positive, so \(\omega\le a^d\). At fixed \(d\) and \(y\), each ordinary source occurs at most once by determinism. Since \(p>3/4\), \(s>2\); the identity \(D_s=3((2/3)^s-(1/3)^s)\) gives \(D_2=1\) and strict decrease for \(s\ge2\), while \(p>3/4\) gives \(\gamma>2\).

Summing \(\min((y/x)^s,a^{sd})\) over distinct positive integers gives the elementary bounds
\[
 A_p^d1(y)\ll_s \min(D_s^d y^s,\; y(2p)^d).
\]
For the second term split at \(x=y/a^d\) when this number is at least one; otherwise the first term suffices. Summation on both sides of \(d=\log_a y\) gives \(O_p(y^\gamma)\) without any arithmetic approximation theorem.

To sharpen this, use \(\omega\le a^d 2^{-J_d(x)}\), with \(J_d(x)\) the number of actual valuations at least two. Let \(H=\log_2(x+1)\). The positive-coordinate argument in [MAXIMAL_ASCENTS.md](MAXIMAL_ASCENTS.md) gives \(2^{-J_d(x)}\ll_M(1+d/H)^{-M}\) for every \(M\). A stronger published-in-project estimate follows directly from Weaver's rise-group theorem: the number \(t\) of maximal groups of unit valuations is at least \(c\log D\log\log D\) when \(D=(d-J_d)/(H+1)\) is sufficiently large, and \(t\le J_d+1\). If \(J_d\ge d/2\), one has a still stronger bound on \(2^{-J_d}\). Otherwise \(D\) is comparable to \(d/H\). Consequently, whenever \(d/H\) is large,
\[
 2^{-J_d(x)}\ll\exp[-c'\log(d/H)\log\log(d/H)] . \tag{3}
\]
These estimates concern one specified ordinary forward trajectory; they enter (1)–(2) before any summation over starting integers. [Weaver, *How rising steps are distributed in odd Collatz trajectories*, Theorem 1](https://rstation.ai/problems/collatz/papers/174/v1).

For clarity set \(R=y/x\ge1\), \(t=\log_a R\). For \(d<t/2\), the sum of the upper weights \(a^{\gamma d}\) is \(O_p(R^{\gamma/2})\). For \(d\ge t/2\), take any applicable uniform bound \(2^{-J_d(x)}\le F\le1\). Bounding all \(d\), including clocks at which this source never reaches \(y\), gives
\[
 \sum_{d\ge0}\min(a^{\gamma d}F^s,\ R^s a^{-(s-\gamma)d})
 \ll_p R^\gamma F^{s-\gamma}. \tag{4}
\]
Indeed, split the two geometric sums at \(a^d=R/F\). Formula (4) at \(F=1\) gives an unrefined \(O_p(R^\gamma)\) bound for all \(R\ge1\); at \(R<1\) the archimedean sum is \(O_p(R^s)\).

For (1), take \(x\le\sqrt y\) and \(F\le C_M(1+t/(2H))^{-M}\), truncated at 1. The early contribution sums to \(O_p(y^{\gamma/2})\) as \(\gamma/2>1\). The remaining sum is
\[
 \ll_{p,M} y^\gamma(1+\log y)^{-M(s-\gamma)}
       \sum_{x\ge1} x^{-\gamma}(1+\log(x+1))^{M(s-\gamma)} .
\]
The series converges. The unrefined bounds on \(\sqrt y<x\le y\) and \(x>y\) contribute \(O_p(y^{(\gamma+1)/2}+y)\). Choose \(M(s-\gamma)\ge N\). For (2), split the first range at \(x=\exp(\sqrt{\log y})\). Below that split \(t/H\gg\sqrt{\log y}\), and (3) in (4) gives the stated saving. Above the split, the unrefined bound contributes \(O_p(y^\gamma\exp[-(\gamma-1)\sqrt{\log y}])\) up to an absolute factor depending on \(p\), in addition to the preceding tails. This proves (2).

## Other fixed parameters and the boundary

For \(0<p<1/2\), one has \(0<s<1,\ D_s<1\). The latter follows from \(D_s=3((2/3)^s-(1/3)^s)\), which is strictly increasing up to \(s=1\), with \(D_1=1\). The part of the normalized depth-\(d\) mass whose actual initial integer is at most \(H\), for any real \(H\ge1\), obeys
\[
 A_p^d{\bf1}_{[1,H]}(y)
 \le D_s^d y^s\sum_{1\le x\le H}x^{-s}
 \ll_p D_s^d y^s H^{1-s}. \tag{5}
\]
This is exponential decay at fixed positive source cutoff and uniform for cutoffs below the indicated threshold. There is no estimate here on all sources at fixed \(p<1/2\) and unbounded depths.

At \(p=1/2\), Weaver's Corollary 5 already bounds all-depth ordinary row masses by a constant times \(y\) at a nonperiodic positive target and by a constant times \(y(3y+1)\) on a positive cycle, with sharper predecessor-density factors. It uses the uniform atom floor and a precursor antichain packing argument. At \(p=3/4\), \(s=2,\ D_s=1\) and the scalar weight is \(\omega^2\). Summability at positive targets, with a cycle-dependent geometric correction, is already known. The new estimates above cover a different open range of tilts and do not improve those endpoint results. [Weaver, Paper 12, §7](https://rstation.ai/problems/collatz/papers/12) · [Weaver, Paper 9, §8.1](https://rstation.ai/problems/collatz/papers/9).

At \(3/4<p<1\), the bound on a specified path includes the damping factor \(D_s^d\). An escaping trajectory can grow far slower than \(a^d\) and remains compatible with (1)–(5). Removing this depth damping while retaining a target-normalized estimate would require additional arithmetic control.
