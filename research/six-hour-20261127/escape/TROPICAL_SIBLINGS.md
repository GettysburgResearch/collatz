# A fixed integer source forces summable isolation of its shortest inverse words

**Status.** Written specialization and proposed signed comparison on the ordinary odd map. The summability exponent one uses the uniform reciprocal antichain estimate of PR193. The exponent \(s>1\) uses only distinct positive integers and the bounded corrected height on the one source. The all-depth fresh-branch gain theorem of PR197 already implies this ordinary summability, including some powers below one. The present formulation retains the finite-depth ternary minimum as the test statistic and gives a signed periodic obstruction to a source-free comparison. [PR197, (4)–(7)](https://github.com/GettysburgResearch/collatz/blob/b0538639df0ab7edd239281bd897e705160f732c/research/ayh-resource-reset-20261124/unconventional/ENTRY_EDGE_GAINS.md)

For \(n\ge1\), let \(m_n(y)\) be the smallest total exponent of a legal inverse word of length \(n\) from a ternary target \(y\). Set \(m_0=0\), and \(m_n=\infty\) on a nonunit for \(n\ge1\). A unit has two possible unit predecessors among the legal exponents at most six, so its minimum is finite and attained. The quantity depends only on \(y\bmod3^n\). At a positive odd integer every such word reconstructs positive odd integers and the specified forward valuations. Let \(B^j y=4^jy+(4^j-1)/3\) for \(j\ge0\). In this section a relative weight with denominator \(2^\infty\) is zero.

## 1. Exact geodesic and a summable lateral cost

Start from one fixed positive escaping odd integer \(a_0\), set \(a_n=S^n a_0\) and \(A_n=\sum_{i<n}e(a_i)\). Its corrected height \(P\) satisfies \(x\le P(x)\le Cx\) on the component and \(P(a_n)=3^n2^{-A_n}P(a_0)\). For all \(n\),
\[
                  0\le A_n-m_n(a_n)\le\log_2 P(a_0).
\]
Indeed any minimizing ordinary source \(u\) has \(P(a_n)=3^n2^{-m_n(a_n)}P(u)\). Appending the next true edge also shows \(A_n-m_n(a_n)\) is nondecreasing. This integer defect is eventually constant. Choose any minimizing source at a time of stabilization. Its own path then stays globally minimum-cost to the subsequent endpoints, at the clock counted from that same initial grade. This does not say every arbitrarily truncated suffix is shortest when the initial grade changes. The component minimizer of corrected height used by PR192 already gives the stronger bound at every horizon: starting at that minimizer, \(m_h(a_n)\ge\lceil A_n+(h-n)\log_2 3\rceil\), with equality for \(h=n\). It also selects the largest affine carry among minimum-cost ties. [PR192, fixed-source arithmetic](https://github.com/GettysburgResearch/collatz/blob/1cb3e8496a6bd6092d3d0dc1dd043c3bcd662aca/research/astra-universal-step-20261124/arithmetic.md)

Moreover
\[
 \boxed{\quad
 \sum_{n\ge1}\sum_{j\ge1}
        4^{-j}2^{m_n(a_n)-m_n(B^j a_n)}<\infty .
 \quad}                                                                \tag{1}
\]
On the escaping component \(P(B^j a_n)=4^jP(a_n)\), since these are distinct odd parents of \(a_{n+1}\) and their exponents differ by \(2j\). Choose a minimum-cost \(n\)-step ordinary predecessor \(u_{n,j}\) of every unit \(B^j a_n\). Then
\[
 \frac{P(a_0)}{P(u_{n,j})}=4^{-j}2^{A_n-m_n(B^j a_n)}.               \tag{2}
\]
These sources are distinct. At clock \(n\) their path is the off-ray parent; at clock \(n+1\) it meets \(a_{n+1}\). Once it meets the reference path at equal clocks it stays there. It therefore cannot supply a different value of \(n\), or a different \(j\) at that same \(n\). All chosen sources are in the synchronous grade of \(a_0\). The [PR193 antichain bound, eq. (1)](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/global/POSTERIOR.md) bounds the sum of \(1/P(u)\) over that entire grade. Since \(m_n(a_n)\le A_n\), (1) follows. For every \(s>1\) the same terms raised to \(s\) are summable without the antichain input: \(P(u)\ge u\) and the selected positive integers are distinct. The corrected-height existence still enters (2).

The full posterior contains the same mechanism before minimizing. For every \(n\ge0\), put \(C_n=3^n2^{-A_n}\) and \(R_n=\rho_n(a_n)/C_n\). Include *all* other parents, allowing negative \(j\) when \(e(a_n)+2j\ge1\), in the following identity:
\[
 R_{n+1}-R_n={1\over C_n}
     \sum_{j\ne0,\ e(a_n)+2j\ge1} 4^{-j}\rho_n(B^j a_n).             \tag{3}
\]
The negative powers in (3) give genuine positive odd integers from the smaller permitted exponents. This is the exact finite residue recursion at \(a_{n+1}\). Equation (1) keeps only one best word at every larger sibling and is therefore a directly checkable tropical obstruction. Formula (3) retains every ancestor and has bounded total increments by the PR193 fixed-source posterior theorem.

**Direct missing comparison.** With \(1\le j\le J\) bounded and an available unit sibling, a bound
\[
             m_n(B^j a_n)\le m_n(a_n)+\log_2 n+O(1)
\]
on a set of \(n\) with divergent harmonic sum contradicts (1). Even positive upper natural density suffices: if the harmonic sum converged, the count through \(N\) divided by \(N\) would tend to zero by separating a fixed initial segment and bounding the remaining normalized count by the harmonic tail. Infinitely many indices by itself permits a convergent harmonic sum. For unbounded \(j=j(n)\), the cost \(2j\) must be added to the left side. A stronger source-free version could seek this comparison for globally calibrated positive paths with \(3^n2^{-m_n(a_n)}/a_n\) bounded away from zero. Neither a fixed-height estimate nor a one-depth example proves the needed divergence.

## 2. A signed geodesic with exponential isolation at every sibling

Let \(r\) be a phase of any genuine negative rational periodic Syracuse orbit with a common positive odd denominator \(d\) prime to three. Suppose its period has length \(p\) and total exponent \(A\). Then \(m=A/p<\alpha\), since the physical affine fixed point is negative and the carry is positive. Such a phase satisfies \(r\le-1\): the periodic source formula and the lower bound on exponents give \(-r\ge(1-(2/3)^p)/(1-2^A/3^p)\ge1\). Every \(B^j r,\ j\ge1\), is a different negative rational parent of \(Sr\); it is off-cycle. Its positive numerator magnitude in denominator \(d\) is \(O_r(4^j d)\).

For a negative transient target \(-b/d\), a length-\(n\) inverse word reconstructs distinct negative rationals with positive integer magnitudes \(b_i/d\). A repeated intermediate state would place the final target on its cycle. In chronological order \(2^{e_i} b_{i+1}=3b_i-d>0\), so
\[
 3^n2^{-\sum e_i}
   ={b\over b_{\rm start}}
     \prod_{i<n}(1-d/(3b_i))^{-1}\ \le\ b(n+1)^{O_d(1)} .
\]
Indeed \(-\log(1-d/(3u))\ll_d1/u\) on the indicated positive integer domain, and the \(b_i\) are distinct. This proves
\[
   m_n(B^j r)\ge\alpha n-2j-O_{r,d}(\log(n+1)),\qquad
   m_n(r)\le mn+O_p(1).
\]
The second inequality uses the periodic word itself. These are the signed first-hit product estimates of [PR193, DYADIC_INCREMENT.md](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/arithmetic/DYADIC_INCREMENT.md), used here without summing word weights and uniformly over the sibling index. Hence for some \(c>0\)
\[
       \sum_{j\ge1}4^{-j}2^{m_n(r)-m_n(B^j r)}=O_{r,d}(e^{-cn}).       \tag{4}
\]
For \(j\le n\) use the preceding lower bound, giving a polynomial times \(2^{-(\alpha-m)n}\). For \(j>n\) use \(m_n(B^j r)\ge n\) and the geometric tail, since \(m<2\). All nonunit terms vanish.

For clarity the signed cyclic target has an eventually periodic optimal cost,
\(m_{n+p}(r)=m_n(r)+A\) for large \(n\). In a minimizing path, write its final chronological portion on the cycle and let \(\ell\) be the preceding off-cycle length through first entry. That first-entry portion has distinct earlier vertices and bounded final numerator (one of finitely many cycle phases); its cost is at least \(\alpha\ell-O(\log(\ell+1))\) by the same product estimate. Its alternative on-cycle length-\(\ell\) path into the same phase costs at most \(m\ell+O_p(1)\). Thus \(\ell\) is bounded on every minimizing path. For large \(n\), append or delete a full final lap to compare minimizing paths in both directions.

Every positive odd lift of \(r\bmod3^n\) has the identical entire array of quantities in (4); the affine sibling maps preserve congruences modulo \(3^n\). Arbitrarily many such target lifts and copies of the indicated signed periodic input word also occur in true finite trajectories that converge to 1 by [ordinary routing](ORDINARY_DECODER_CONTROLS.md). The height condition making (1) a test of one fixed source is absent: for fixed negative \(r=-b/d\), any positive lift \(y\) satisfies \(dy+b\ge3^n\). The maximum possible \(3^n2^{-m_n(y)}/y\) on these lifts is \(O_{b,d}(2^{-n})\). Thus (4) is a precise obstruction to a universal finite-quotient sibling inequality and does not give a counterexample on macroscopic positive lifts.

## 3. The literal routing cost of preserving a previous word

The odometer \(B\) satisfies
\[
       B^j y-y={(4^j-1)(3y+1)\over3},\qquad
       v_3(B^jy-y)=v_3(j)
\]
for each positive ordinary \(y\) and \(j\ge1\). Thus preserving an entire inverse ternary word of length \(n\) by moving to a larger sibling requires \(3^n\mid j\). The first such sibling carries the factor \(4^{-3^n}\) in (1). The elementary same-word rerouting argument cannot produce a nonsummable charge: it must discover a different cheap inverse word at a much nearer sibling. Neither the signed control nor the fixed-source selection proves or disproves that remaining assertion.
