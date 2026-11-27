# Vanishing density of all periodic vertices in the homogeneous ceiling

Let \(H_N\) be the least dyadic lift of an odd integer at most \(N\) which is at least three times its input, for odd positive \(N\). Let \(P_N\) count all odd representatives in all periodic components of this finite odd-part map, including every component at a cutoff. Then, with an absolute implied constant,
\[
          P_N\ \ll\ N\sqrt{\frac{\log\log N}{\log N}}\qquad(N\to\infty).
\]
This is a restriction on the entire periodic set at each cutoff, independent of ordinary Collatz cycles or an irrationality measure. It permits a surviving component of polynomially sublinear size and does not bound a whole plateau of equal rotations across different cutoffs.

**Status:** independently reviewed written deduction. The coordinator and the source-mass lane reconstructed the proof. The accompanying enumeration checks finite instances only. This argument is not formalized in Lean.

## The integer rounding calendar

Normalize a positive dyadic ray of the grid to the unique integer \(Z\in(N/2,N]\). These are precisely the integers of that half-open octave. Every point of the pooled periodic set has a normalized transition
\[
 Z' = T_b(Z),\qquad T_b(z)=\left\lceil 3z/2^b\right\rceil,
 \qquad b\in\{1,2\}
\]
for large \(N\), where \(b\) is the actual octave winding. Its raw error above \(3Z\) is at most three, so the common rotation \(\theta\) satisfies \(0<\theta-\gamma\ll1/N\), \(\gamma=\log_2 3\), by multiplying the individual positive component equations. The strict sign follows from the impossibility of an exact all-tripling return.

The pooled periodic set is finite and \(H_N\) restricts to a permutation. Its nondecreasing lift therefore translates the sorted lifted ranks by the same integer for every vertex of the pool. Starting at normalized rank \(r\), \(0\le r<P_N\), the cumulative windings at time \(j\) are \(B_j=\lfloor r/P_N+j\theta\rfloor\). Consequently the \(n\)-step calendars split the pool into \(O(n+1)\) contiguous spatial rank intervals: only the \(n+1\) rotated integer cuts and their endpoints matter. In each interval all iterates of the actual selected integer starts follow its common calendar \((b_0,\ldots,b_{n-1})\). All normalized outputs at date \(n\) remain distinct on this pool.

Fix \(n=\lfloor (\log N)/(2\log4)\rfloor\). On every such calendar and at each \(0\le j\le n\), the scale
\[
                       m_j=3^j/2^{B_j}
\]
is bounded between \(1/3\) and \(2\) for all sufficiently large \(N\). Indeed \(|B_j-j\theta|<1\) and \(n(\theta-\gamma)=o(1)\). Write \(F_j=T_{b_{j-1}}\circ\cdots\circ T_{b_0}\) with \(F_0\) the identity on all integers. Off the selected starting set this composition is just an auxiliary monotone integer map; it need not follow the physical cutoffs.

## Adjacent integer starts coalesce

Choose an integer \(V\) uniformly modulo \(2^{B_n}\). The rounding remainders
\[
          d_j=2^{b_j}T_{b_j}(F_j(V))-3F_j(V)
                    \in\{0,\ldots,2^{b_j}-1\}
\]
are independent uniform digits on their respective alphabets. To see this, a given prefix determines \(V\) modulo \(2^{B_j}\) uniquely by iterating the affine equations and reducing modulo \(2^{B_j}\), after canceling \(3^j\). Conversely inputs congruent modulo \(2^{B_j}\) have that same prefix, since adding \(2^{B_j}\) translates each intermediate value by the corresponding integer exact lift. There are \(2^{B_j}\) possible digit strings and residue classes; the resulting injection of residue classes into strings is a bijection.

Set \(G_j=F_j(V+1)-F_j(V)\ge0\). With \(D=2^{b_j}\),
\[
                   G_{j+1}=\left\lceil\frac{3G_j-d_j}{D}\right\rceil.
\]
Conditional on the past this rounds \(3G_j/D\) down or up with probabilities giving exactly that mean. Thus \(Y_j=G_j/m_j\) is a nonnegative mean-one martingale, \(Y_0=1\); zero stays zero. If \(D\nmid G_j\), the fractional part of \(3G_j/D\) is one of \(1/4,1/2,3/4\). The conditional variance of the next \(Y\)-increment is consequently at least \(3/64\), since \(m_{j+1}\le2\). If \(D\mid G_j\) and \(G_j>0\), the next gap is deterministic and its dyadic valuation decreases by \(b_j\ge1\).

For \(K\ge2\), stop at the earliest of date \(n\), extinction, and \(Y_j\ge K\). The overshoot at a single step in \(Y\) is at most three, since \(m_j\ge1/3\). The stopped variable is between zero and \(K+3\), has mean one, and hence has second moment at most \(K+3\). The identity expressing the increase in the second moment as the sum of conditional variances shows that the expected number of nondeterministic steps taken before stopping is \(O(K)\). This identity follows directly by telescoping the conditional second-moment expansion at the finitely many dates.

The probability of reaching \(K\) is at most \(1/K\) by the stopped mean. On paths surviving to \(n\) without reaching \(K\), every gap is a positive integer at most \(2K\). No block of more than \(1+\lfloor\log_2(2K)\rfloor\) consecutive steps can be entirely deterministic by the dyadic-valuation decrease. Their number of nondeterministic steps is therefore at least \(\lfloor n/(2+\lfloor\log_2(2K)\rfloor)\rfloor\). Combining these estimates with \(K\asymp\sqrt{n/\log n}\) gives, uniformly over the calendars in question,
\[
              \Pr(G_n>0)\ll \sqrt{(\log n)/n}.
\]

## Pooling the spatial intervals

For a contiguous interval of \(D_0\) possible integer starts following one chosen calendar in the periodic set, the distinct outputs of its selected points are bounded by the number of different values of \(F_n\) on the entire contiguous interval. By monotonicity this is one plus the number of its internal unit gaps for which \(F_n(v+1)>F_n(v)\). That predicate is periodic in \(v\) modulo \(2^{B_n}\), because \(F_n(v+2^{B_n})=F_n(v)+3^n\). Its count on the interval is at most \(D_0\Pr(G_n>0)+2^{B_n}\). The convex hulls of the \(O(n+1)\) contiguous rank cells are disjoint integer intervals inside the one octave, so their lengths sum to \(O(N)\). Summing and using \(2^{B_n}\le4^n\le\sqrt N\) gives
\[
        P_N\ll N\sqrt{(\log n)/n}+(n+1)(1+\sqrt N),
\]
as claimed.

[Exact digit, adjacent-gap and pooled-rank controls](check_periodic_grid_density.py) · [Recorded controls](periodic_grid_density_controls.json)
