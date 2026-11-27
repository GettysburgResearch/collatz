# A single summable budget for all synchronized residual replacements

**Written result.** On any nonperiodic ordinary component, the relative errors made by dyadically aligning successive marked sources with their residual representatives are absolutely summable along the delayed return dynamics. Sufficiently far forward, that alignment synchronizes the literal shortcut clocks as well as the odd clocks. The bound uses PR193's written transversal theorem. The synchronized half-script counts used for the residual return are checked separately in Lean.

## A transversal for the entire component

Fix a positive nonperiodic odd orbit \((q_i)_{i\ge0}\). Its component consists of the odd \(x\) such that \(U^a(x)=q_b\) for some \(a,b\ge0\). Define its **level** \(t(x)=b-a\). The injectivity of the base orbit makes this independent of the witness: compare two witnesses after advancing both to the larger \(a\). Also \(t(Ux)=t(x)+1\), including when \(a=0\). Two component points have the same level exactly when their accelerated iterates agree at some equal clock. For the converse, compare their two hits of the base orbit after advancing to a common clock at least as large as either hitting time.

For every represented level \(i\) write \(m_i\) for the smallest positive odd integer at that level. The set of minima is a transversal of synchronously distinct odd cores: all maps \(U^h\) are injective on it, for every \(h\ge0\), with no requirement that it be forward invariant. PR193's sharpened translated synchronization estimate therefore gives
\[
  \#\{i:m_i\le X\}\ \ll\ X^\theta/\sqrt{\log(2X)},\qquad
  \theta=H_2(\log 2/\log 3)<1 .
\]
Indeed on any given interval take the common clock of that theorem; distinct levels give distinct endpoints even there. The constant is absolute. Write \(M\) for the least positive odd integer in the component. Summing over dyadic intervals starting at \(M\) gives the **component-wide** budget
\[
  \sum_i\frac1{m_i}\ll
       \frac{M^{\theta-1}}{\sqrt{\log(2M)}}.                         \tag{1}
\]
For example the interval \([2^h M,2^{h+1}M)\) costs at most the cumulative count at its upper endpoint divided by \(2^h M\); the resulting geometric series converges. All represented levels, including negative ones, are included. The forward tails \(H_t=\sum_{i\ge t}1/m_i\) tend to zero. [PR193, translated packing and endpoint count](https://github.com/GettysburgResearch/collatz/blob/c6cb5e66516a86c33a757154983bbddc822510de/research/astra-universal-descent-20261124/escape.md)

## Archimedean alignment at equal levels

Define a positive real number at each ordinary state of this component by
\[
 L(x)=x\exp\left(\sum_{j\ge0}\log\left(1+\frac1{3U^j(x)}\right)\right).
\]
Every term is defined and \(0<\log(L(x)/x)\le H_{t(x)}/3\). This is uniform over all branches at a given level, including arbitrarily large predecessors coalescing with the original source. With \(A_J(x)\) the total binary exponent of its first \(J\) odd steps, telescoping the ordinary recurrence gives
\[
 L(U^Jx)=3^J 2^{-A_J(x)} L(x).
\]
If \(x,y\) coalesce at the exact same odd clock \(J\), then \(L(x)/L(y)=2^{A_J(x)-A_J(y)}\). Their relative corrections also satisfy the sharper finite-strip bound
\[
 \left|\log\frac{L(x)/x}{L(y)/y}\right|
 \le \frac13\sum_{i=t(x)}^{t(x)+J-1}\frac1{m_i}.                    \tag{2}
\]
Beyond their common endpoint the two sums are identical. Before that time each positive logarithm at level \(i\) lies between zero and \(1/(3m_i)\), so this bounds the absolute difference at that level.

Now suppose \(n,s\) are marked at the same level \(t\) and of octaves \(d,e\), respectively. Both octaves tend to infinity uniformly as \(t\to\infty\) because there are only finitely many integers below any fixed bound, each having just one level. Their marked offsets give
\[
 1\le L(n)/2^d\le (1+70/(d+1))e^{H_t/3}
\]
and the same bound with \(s,e\). Hence for all sufficiently late levels the ratio \((L(n)/2^d)/(L(s)/2^e)\) lies strictly between \(1/2\) and 2. This ratio is an integral power of two, so it equals 1. In particular
\[
 A_J(n)-A_J(s)=d-e.                                                   \tag{3}
\]
When \(d\ge e\), padding \(s\) to \(2^{d-e}s\) adds exactly \(d-e\) initial even shortcuts. Formula (3) proves simultaneous equality of the two literal shortcut endpoints after exactly \(A_J(n)\) literal steps, as well as equality of the odd clocks from \(n\) and \(s\). This statement applies uniformly to every pair of same-level marks, with the starting level threshold allowed to depend on the component.

## Disjoint strips along the residual return map

Use [the delayed residual return construction](ARITHMETIC_RETURN.md). Number the genuine marked orbit visits selected by that construction \(n_j\), with true levels \(t_j\); write \(d_j\) for their octaves, \(s_j=r(n_j)\) and \(e_j\) for the octaves of \(s_j\). The pair merges at \(J_j=R_{d_j}\) odd steps. The next marked selection occurs strictly after this settling, so \(t_{j+1}>t_j+J_j\). By (2) and (3), for every sufficiently late starting index \(j_0\),
\[
 \sum_{j\ge j_0}
   \left|\log\frac{n_j}{2^{d_j-e_j}s_j}\right|
 \le \frac13\sum_{i\ge t_{j_0}}\frac1{m_i}.
\]
Thus even if the octave drops \(d_j-e_j\) are large, the cumulative *relative mantissa error* has a finite budget tending to zero on tails. For every \(\eta>0\), indices at which the displayed absolute error is at least \(\eta/(d_j+1)\) have summable reciprocals \(1/(d_j+1)\). This statement does not presume independence between the replacements or between the comparison orbits.

Integer separation allows errors as small as order \(1/n_j\), already a summable scale. A literal local control is \(n=2^d+3\), \(d\ge4\), with \(v=2^{d-2}+1\), \(k=1\) and \(b=3v-1\equiv2\bmod4\). The mixed script terminates immediately. Both \(n\) and the positive odd partner \(s=(n-1)/2\) are marked, and \(n-2s=1\) exactly. The raw pair \(n,2s\) also synchronizes in literal time since the half arm needs one fewer raw step before its common endpoint. This example does not certify that the partner is the global residual representative, or that the example lies on an escaping trajectory.

There is no lower bound here forcing a nonsummable sequence of relative mantissa errors on a nonperiodic residual path. In particular the estimate does not by itself bound the number of dyadic octave drops or prove convergence. The transversal estimate is already supplied by PR193; the new deductions concern its simultaneous application across all synchronization levels, the integral identity (3), and the disjoint-strip cost of repeated ordinary residual replacements. These deductions are written proofs.
