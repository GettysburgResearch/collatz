# Relative minorization at growing resolution for ordinary ancestors

**PROPOSED.** Let \(M\) be the product of normalized odd binary Haar and full ternary Haar. Resolution \((b,r)\) records the odd source modulo \(2^{b+1}\) and the same source modulo \(3^r\). A set at this resolution is any union of the corresponding cells. The two coordinates of an ancestor below always come from the same positive integer.

For a fixed positive odd unit \(z\) put
\[
 \eta_n^{z}=\sum_{U^n x=z} 3^n2^{-S_n(x)}\delta_{(x,x)}.
\]
If \(b_n+r_n=o(n)\), then, uniformly over every set \(E\) at resolution \((b_n,r_n)\),
\[
              \eta_n^{z}(E)\ \ge\ \big(h(z)-o(1)\big)\,M(E).          \tag{1}
\]
Consequently the finite projected measures, normalized by their actual masses \(\rho_n(z)\), converge to the projected product Haar laws in total variation. The uniform assertion in (1) concerns the lower relative density, including in single very small cells. A relative upper estimate in every cell does not follow from the total-variation statement.

There is a moving-source version. In any escaping component let \(a_j=U^j a\), use grade zero at \(a\), and let
\(\mu_v=\sum_{g(x)=v}P(x)^{-1}\delta_{(x,x)}\).
Write \(H>0\) for its canonical grade flux. For \(k\to\infty\) and \(b+r=o(k)\), (1) holds with \((\eta_n^{z},h(z))\) replaced by \((\mu_{-k},H)\). For \(j,k\to\infty\) independently it also holds with
\[
                 \left(P(a_j)^{-1}\eta_{j+k}^{a_j},\,H\right).        \tag{2}
\]
Thus the available precision grows with the **overshoot \(k\)** past the ordinary seed's clock. Absolute minorization on bounded precision and individual-depth weak convergence were proved earlier. [Product transfer, especially (6)](../escape/FIRST_POWER_HAAR.md) · [Original ancestor law and the moving clock](../escape/ORDINARY_ANCESTOR_EQUILIBRIUM.md).

## Finite-window estimate

Write \(\widehat L\) for the geometric inverse transfer of the product theorem. Its adjoint fixes \(M\), and \(0\le\widehat L1\le2\,1_V\), where \(V\) denotes ternary units. There are absolute constants \(c>0,\delta>0\) and \(n_0\) such that
\[
 \widehat L^m 1_E \ge c\,M(E)\,1_V
 \quad \text{if}\quad m-b\ge n_0,\qquad b+r\le\delta(m-b)
                                                                         \tag{3}
\]
at the requested resolution. This is an unnormalized estimate on the actual geometric operator from fixed-total routing; no uniform bound on its row masses is presumed. [Weaver–Wren, hierarchical renewal, Lemma 7 and Theorem 8](https://rstation.ai/problems/collatz/papers/48/v2) · [Weaver, Paper 202, Input 2](https://rstation.ai/problems/collatz/papers/202).

Let \(\eta_i\) be finite positive measures satisfying \(\eta_{i+1}=\widehat L^*\eta_i\), with \(Z_i=\|\eta_i\|\). Given \(N\), a desired \((b,r)\), and \(R=1+b+r+n_0\), set \(H_*=\inf_{N/2\le i\le N}Z_i\), using integer indices. There are absolute constants \(C,\gamma>0\) depending only on the constants in (3), with
\[
       \eta_N(E)\ge H_*\left[1-C\left(\frac R N\right)^\gamma\right] M(E)
                 \qquad(N\ge1).                                        \tag{4}
\]
An initially negative right side supplies a trivial bound.

To see why a finite projected lower bound can be subtracted, suppose \(u\) inverse steps remain between an intermediate stage and the requested output. The value \(\widehat L^u1_E\) depends only on the input residues modulo \(3^{r+u}\) and \(2^{1+\max(b-u,0)}\). Each legal path has ternary expansion by \(3^u\) in the inverse direction, whose eligibility tests cost at most \(u\) extra ternary digits. Its binary input differences are multiplied by \(2^{S_u}\) with \(S_u\ge u\). Uniform convergence of the word sum preserves this finite dependence. Retain ternary precision \(r+u+1\) instead, so the single-step mass test \(\widehat L1\) is always visible.

Starting from the output, put \(u_0=0\), \(m_i=\lceil D(R+u_i)\rceil\), \(u_{i+1}=u_i+m_i\). Choose a fixed \(D>2+2/\delta\). Use exactly the blocks with \(u_{i+1}\le N/2\). They are applied in the reverse order, from time \(N-u_\ell\) towards time \(N\). A block of length \(m_i\) satisfies (3) at output resolution \((\max(b-u_i,0),r+u_i+1)\). Its pullbacks depend only on the retained input resolution at \(u_{i+1}\). All \(\ell\) blocks together leave at least half of the time window to the left.

Suppose the input finite projection of a stage dominates \(A M\). Replace that projection by the measure constant with respect to \(M\) on each cell, subtract \(AM\), and call the resulting nonnegative measure \(\tau\). It has unit mass at least \((Z_{t+1}-A)/2\) on \(V\), where \(t=N-u_{i+1}\) is this input time. Indeed \(\int\widehat L1\,d\tau=Z_{t+1}-A\) by finite dependence and Haar invariance. By (3), and by exact propagation of the subtracted Haar, the projected output therefore dominates
\[
                 [A+(c/2)(H_*-A)]M.
\]
Decrease \(c\) to ensure \(0<c/2<1\). Starting with \(A=0\), after \(\ell\) stages the coefficient reaches \(H_*[1-(1-c/2)^\ell]\). Since \(R+u_{i+1}\le(D+2)(R+u_i)\), maximality of \(\ell\) gives \((1-c/2)^\ell\ll_D(R/N)^\gamma\) with \(\gamma=-\log(1-c/2)/\log(D+2)>0\). This proves (4). The [finite Lean kernel](MesoscopicMinorization.lean) verifies the positive projection, the exact first-step mass subtraction, and the accumulated geometric gain. The analytic sampling input (3) is external.

For (1) use the ordinary row recursion and the fixed-target limit \(\rho_i(z)\to h(z)>0\). For the full grade replace \(\eta_i\) by \(\mu_{-i}\) and use \(Z_{-i}\to H\). For (2) apply (4) in the \(k\)-step window starting at \(\eta_j^{a_j}/P(a_j)\). Uniformly in \(k/2\le i\le k\), its masses differ from \(Z_{-i}\) by \(o_{j\to\infty}(1)\), by the [uniform physical trace profile](../../astra-unconventional-20261126/boundary/TRACE_PROFILE.md). In every case the endpoint mass tends to the same limit as the infimum. The nonnegative projected excess above the lower multiple of Haar therefore has mass tending to zero. This proves the asserted total-variation conclusions.

## The real mark on the same growing cells

In (2) attach \(F(x)=x/P(x)\). If \(I\) is an interval with \(\lambda_C(\partial I)=0\), then uniformly on the same growing spatial resolution,
\[
  \sum_{\substack{U^{j+k}x=a_j\\F(x)\in I}}\frac{1_E(x,x)}{P(x)}
            \ \ge\ [H\lambda_C(I)-o(1)]\,M(E).                           \tag{5}
\]
Here \(\lambda_C\) is the previous corrected real phase law. The corresponding projected law converges in total variation for any fixed finite partition into such real intervals and **all** unions of the resulting space–mark cells.

Fix \(\epsilon>0\). At sufficiently negative grade \(-m\) all vertices at that grade and earlier exceed a threshold tending to infinity with \(m\). Uniform reciprocal packing therefore makes \(|F(x)-F(z)|<\epsilon\) whenever \(g(x)\le-m\) and \(z\) is its descendant on grade \(-m\). Explicitly \(F(z)-F(x)\) is at most \(\sum 1/(3u)\) on that negative-grade segment. The canonical mass \(h(z)/P(z)\) at grade \(-m\) has \(F\)-marginal tending to \(H\lambda_C\). In the portion of \(I\) at distance more than \(\epsilon\) from its complement, choose a finite set of unit \(z\)'s capturing its mass up to \(\epsilon\). Each such \(z\) reaches \(a_j\) for all sufficiently large \(j\). The contribution of its depth-\((k-m)\) ancestors equals \(P(z)^{-1}\eta_{k-m}^z\) at the source coordinates, and every one of their marks belongs to \(I\). Apply (1) at those finitely many genuine \(z\)'s. Then take \(m\) large and \(\epsilon\) small, using an interior cutoff with null boundary. This proves (5). Applying it to each element of a fixed finite partition and using total mass convergence proves the projected total-variation assertion. The same proof holds for the full grade. [Corrected real phase and canonical flow](../escape/CORRECTED_PHASE.md).

## A physical limit on the accessible precision

For the full grade \(-k\), and for the original law in (2) after normalization, the actual positive integer \(X\) obeys
\[
                  \log_2 X/k\longrightarrow 2-\log_2 3
                         \quad\text{in probability}.                      \tag{6}
\]
To prove it, select a finite set of grade-zero units \(z\) whose canonical weights \(h(z)/P(z)\) capture \(H\) up to \(\epsilon\). The ancestors of these sites supply all but \(O(\epsilon)\) of the normalized mass for all large \(k,j\), since each \(\rho_k(z)\to h(z)\). At a fixed \(z\), the outward total \(S_k/k\to2\) in probability under the actual depth law. For the first \(k-1\) gaps this follows by the bounded Radon–Nikodym comparison to the canonical path from the [ordinary ancestor law](../escape/ORDINARY_ANCESTOR_EQUILIBRIUM.md). For the last gap, the ratio of the geometric weight of all \(e>E\) to \(\rho_1(y)\) is at most \(3\,2^{-E}\) at every allowed penultimate unit \(y\), so this extra gap divided by \(k\) tends to zero. On each simple path ending at \(z\), its real correction product is bounded below uniformly and at most one. Thus \(\log_2 X=S_k-k\log_2 3+\log_2 z+O(1)\). Let \(\epsilon\downarrow0\) to get (6).

For every fixed \(\epsilon>0\) and \(b+r\log_2 3\ge(2-\log_2 3+\epsilon)k\), the joint binary–ternary projection has total-variation distance tending to one from projected product Haar. There are \(2^b3^r\) equiprobable CRT cells. The positive odd integers up to \(2^{(2-\log_2 3+\epsilon/2)k}\) meet at most one cell per integer, so their cell union has Haar mass \(O(2^{-\epsilon k/2})\) and captures almost all of the physical mass by (6). This includes the binary-only obstruction at \(r=0\). This is compatible with (1)–(5). The unconditioned small-cell lower bounds at overshoot \(k\) concern initial digits of sources on grade \(-k\). The event that such a source joins the specified sibling at the remote positive grade \(j\) depends on its subsequent physical itinerary. No lower bound for that event follows here.
