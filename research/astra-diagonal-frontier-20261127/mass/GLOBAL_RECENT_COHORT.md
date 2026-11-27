# A relative first-moment loss on the entire recent principal cohort

**PROPOSED written theorem.** Let \(n=2^k\) and \(\gamma=(7/8)(7/6)^{3/4}\). For an old principal source, call its age the number of odd steps since it first became the least positive representative of its own passing word. At all sufficiently large \(k\), PR200's proposed relative loss of order \(1/(k+1)\) holds on the **entire cohort of principal sources of age less than**
\[
 s_k=\big\lfloor\log_{1/\gamma}(k+1)\big\rfloor .
\]
It also holds on the whole accepted row restricted to \(m/2^{A_n+1}\ge2^{-s_k}\). Both losses occur on the **very next actual odd step**. Both statements use the original weights \(1/m\). Birth age is an actual first-principal time, and the depth and modulus are computed separately for each physical source. The fixed bad source whose existence would prevent convergence eventually lies outside both cohorts.

## The original gate probability with its polynomial factor

Let \(P_n\) denote the probability that iid geometric gaps with probabilities \(2^{-e}\) pass \(4A_j\le7j\) for all \(j\le n\). Uniformly in \(n\ge1\),
\[
 P_n\asymp (n+1)^{-3/2}\gamma^n.                                    \tag{1}
\]
For the lower bound, at total \(k=\lfloor7n/4\rfloor\) rotate each length-\(n\) composition at a maximum of \(4A_j-7j\). This supplies at least \({k-1\choose n-1}/n\) passing words, each with mass \(2^{-k}\). Stirling's formula gives the lower estimate, including the bounded rounding factor.

For the upper bound use the classical fluctuation generating identity for the walk with iid increments \(4e-7\). Baxter's Example 3 counts strictly positive partial sums. Taking its count marker and spatial Fourier parameter both zero gives
\[
 \sum_{n\ge0}P_n z^n=\exp\left(\sum_{j\ge1}
       {z^j\over j}\Pr(4A_j\le7j)\right).                           \tag{2}
\]
This form uses the weak inequality on the right, since a zero partial sum is allowed throughout by the gate. Only its formal power-series coefficients are needed. [Baxter, *An analytic problem whose solution follows from a simple algebraic identity*, Pacific J. Math. 10 (1960), Example 3, pp. 741–742](https://msp.org/pjm/1960/10-3/pjm-v10-n3-p01-s.pdf).

For fixed \(j\) the chance of total \(a\) is \(b(a)={a-1\choose j-1}2^{-a}\). The ratio \(b(a-1)/b(a)=2(a-j)/(a-1)\) on \(j<a\le\lfloor7j/4\rfloor\) is at most \(9/10\) for all sufficiently large \(j\). Indeed the ratio increases with \(a\) and its endpoint tends to \(6/7\). The endpoint term is \(O(j^{-1/2}\gamma^j)\) by Stirling. Thus the coefficient of \(z^j\) inside the exponential in (2), after removing \(\gamma^j\), is at most \(C w_j\) with \(w_j=(1+j)^{-3/2}\). The positive convolution \((w*w)_n\le C_0 w_n\) follows by splitting the sum at \(n/2\), using summability of \(w\). The positive coefficients of the exponential are therefore bounded by \(w_n\sum_{m\ge1}C^m C_0^{m-1}/m!\) away from \(n=0\). This proves the upper estimate in (1).

## The sources lost at the boundary really are recent

Use the eight-letter family and notation of [the terminal leakage theorem](PRINCIPAL_TERMINAL_LEAKAGE.md). At \(4\mid n\), for **each** permissible tight suffix of length \(n-8\), there is a tight principal source whose actual terminal \(y=y_0+2Li\) has both \(y\equiv1\pmod4\) and \(i\ge Q/16\), \(Q=6561\). In fact the full 227-residue check gives maximum circular gap 2860 in every unit dilation. Within integers \(\lceil Q/16\rceil\le i<Q\), the required parity gives an arithmetic progression of length at least 3075. Dividing by two modulo \(Q\) produces a circular interval of that length, even after the common suffix's affine shift and unit dilation. It necessarily meets the prefix set. The 14-word Lean certificate independently gives maximum gap 2982, sufficient for the same height placement.

Equation (5) of the terminal leakage theorem gives \(m/2^{A_n+1}\ge 1/16-2^{-n-1}>1/32\) at these depths. Every such source first fails on step \(n+1\). Counting one source per suffix as there, followed by (1), gives the total next-step loss **from these high sources** at least \(c_0 P_n\) for some absolute \(c_0>0\), uniformly at \(4\mid n\), \(n\ge12\). They have not previously visited 1: if they had first visited it at some \(h\le n\), the exact orbit product at that hit and the passing gate would imply \(m\le(2^{7/4}/3)^h\). This contradicts \(m>2^{7n/4+1}/32\) for \(n\ge12\).

Let \(\mathcal B_{n,s}\) consist of the sources principal and passing at depth \(n\) which **were not principal at** \(n-s\). The entire earlier word of a survivor passes, and a principal source stays principal while passing because its dyadic modulus increases. Membership in \(\mathcal B_{n,s}\) agrees with age less than \(s\). For each step from \(j\) to \(j+1\), PR201's dyadic-sibling reciprocal estimate bounds all new principal mass by \(P_j\): each parent's children with a new least representative together cost at most its own original word probability \(2^{-A_j}\). No future conditional law is used. For \(1\le s\le n/2\) equation (1) gives
\[
 \sum_{m\in\mathcal B_{n,s}}\!{1\over m}
 \le\sum_{j=n-s}^{n-1}P_j
 \ll \gamma^{-s}P_n .                                                \tag{3}
\]
The implicit constant is independent of \(s,n\). Indeed \(j\ge n/2\) and \(\sum_{v=1}^s\gamma^{-v}\le \gamma^{-s}/(1-\gamma)\).

Write \(\mathcal L_{n,s}\) for the subrow \(m/2^{A_n+1}\ge2^{-s}\). Since \(A_n-A_{n-s}\ge s\), every such \(m\) is at least the full modulus \(2^{A_{n-s}+1}\) of its earlier word and so belongs to \(\mathcal B_{n,s}\). For \(5\le s\le n/2\), the preceding high-source losses lie in *both* \(\mathcal L_{n,s}\) and \(\mathcal B_{n,s}\). For either entire cohort \(V\) this proves
\[
 \sum_{m\in V}{\mathbf 1_{\{4A_{n+1}(m)>7(n+1)\}}\over m}
       \ \ge c\gamma^s\sum_{m\in V}{1\over m}.                       \tag{4}
\]
Choosing \(s=s_k\) gives \(\gamma^{s_k}\ge1/(k+1)\). The global height cutoff is within a constant factor of \((k+1)^{-1/(-\log_2\gamma)}\). A fixed permanent ordinary source has a fixed finite birth time, so its age at depth \(2^k\) is eventually nearly \(2^k\). The proof of (4) leaves the mass of those older sources uncontrolled.

## What forward re-anchoring would cost

The recent cohorts at consecutive sufficiently large dyadic depths have disjoint birth windows. Already (1) and (3) give their total mass at \(n=2^k\) at most \(O((k+1)n^{-3/2}\gamma^n)\) for \(s=s_k\). Consequently even an assignment using every vertex of every available ordinary orbit and predecessor tree, subject to bounded multiplicity and bounded change in reciprocal weights, can draw only a summable amount from those cohorts. It could not supply a divergent harmonic amount \(c/[m(k+1)]\) required from a persistent fixed source \(m\).

On one hypothetical bad component this obstruction extends to sources of *all ages*. Suppose \(B\) is a positive odd component disjoint from 1, with least odd integer \(m\ge3\). The terminal and every intermediate odd state of every source in \(B\) are at least \(m\). With
\[
 \beta_m={2^{7/4}\over3+1/m}>1,\qquad d=H_2(4/7)<1 ,
\]
any ordinary \(x\in B\) that fails the gate at clock \(j\) satisfies
\[
 2^{7j/4}<2^{A_j(x)}
  ={x\over U^j x}\prod_{i<j}(3+1/U^i x)
  \le{x\over m}(3+1/m)^j,\qquad x>m\beta_m^j.                    \tag{5}
\]
The lower bound \(\beta_m>1\) is uniform by \(10^4<128\cdot3^4\). [ComponentLoss.lean](ComponentLoss.lean) checks the finite same-trajectory product inequality and the uniform floor comparison.

If \(D\) is PR201's set of all finite-depth passing principal sources, its sparse-source bound gives \(\sum_{x\in D,\ x>X}1/x\ll X^{d-1}\). Thus the total reciprocal mass of **all distinct** \(D\)-sources of \(B\) whose first failure occurs after \(N\), even allowing every branch and arbitrary prior age, is
\[
 O\!\left(m^{d-1}\beta_m^{-(1-d)N}\right).                       \tag{6}
\]
The least odd \(m\) permanently passes and eventually is principal, so the component's accepted mass stays at least \(1/m\). In particular a component-preserving bounded-weight assignment cannot establish a \(c/(k+1)\) discharge from this component by moving the origin forward on its ray or pulling in its other ancestors. This is a conditional consequence for a putative component, not an example of one. The earlier prehit-tail argument uses the related source-height inequality with the universal floor three. Here the component minimum is retained and the restriction applies to an attempted re-anchoring using its entire basin.

The dyadic sibling bound, global trace and quantitative target are the project inputs, with their source conventions unchanged. [PR201, global prefix trace, inequality (8)](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md) · [PR200, same-source loss, proposed inequality (2)](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/NEXT_FIRST_MOMENT_TARGET.md)
