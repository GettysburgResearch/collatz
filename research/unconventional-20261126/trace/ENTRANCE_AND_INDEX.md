# Uniform first-passage approximation and the index of a charged forward ray

**Status.** Proposed. The ordinary Collatz statements use the source-qualified analytic estimates identified below. The binary graph in the last section has independent elementary proofs.

### One finite set of ordinary starts approximates every target

Use the physical shortcut, either first-hit label \(w_v\), and the notation \(f_Y,f\) of [the annular current](ANNULAR_ESCAPE_CURRENT.md). The results here hold also for logarithmically sampled starts \(q\le Y\), with normalized weights proportional to \(1/q\).

At an integer barrier \(M\), first strip the initial powers of two, then stop at the first odd state at most \(M\). Let \(r_M(q)\) be that odd landing on success and assign the default value one on failure. Let \(\Lambda_M\) be its limiting probability law for either source sampling. Define the complete-future mixture
\[
 K_M(v)=\sum_{r\le M}\Lambda_M(r)w_v(r).
\]
The fixed-barrier landing laws converge in total variation by Valbuena's **ct-label-laws** and **ct-natural-density-upgrade**. The proof of **ct-basin-boundary**, through the displayed estimate for \(E_{M,m}\), gives \(a_M=\max_r\Lambda_M(r)\to0\), including the default label. The limit of the failure probability is \(\mu_{\min}((M,\infty))=e_M\to0\), since the odd and shortcut minima agree. These refer to the pinned [basin-density paper](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex). Its nonlocal input chain has not been rebuilt here.

For some absolute \(A\), all \(M\ge1\) satisfy
\[
 \sup_v|f(v)-K_M(v)|\le e_M+a_M+A M^{-1/40},
 \qquad
 \sup_v|f_Y(v)-f(v)|\longrightarrow0.                         \tag{1}
\]
The packing term can be omitted for unweighted hits. To see the uniformity, on a successful sample put \(r=r_M(q)\). If \(q\) hits \(v\) before that landing, necessarily
\[
 r=r_M(\operatorname{oddpart}(v)).
\]
This includes a target in the initial or final halving chain. Thus the probability of such an early hit is at most the single largest atom of the sampled landing law, independently of \(v\). On success without an early hit the indicators for \(q\) and \(r\) agree. Their weighted values differ by at most the loss in the prelanding product. The odd states in that finite simple prefix all exceed \(M\). By reciprocal packing and \(1-\prod(1-u_i)\le\sum u_i\), this loss is at most \(A M^{-1/40}\). The remaining failure event costs its probability. Therefore, uniformly in \(v\), \(f_Y(v)\) is within these three errors of the identical mixture under the empirical landing law. Replacing that law by \(\Lambda_M\) costs its total-variation distance. Take \(Y\to\infty\) at fixed \(M\), then \(M\to\infty\). This proves both conclusions. For the joint unweighted hit indicators of any \(k\) targets, any bounded test valued in \([0,1]\) incurs at most \(e_M+k a_M\) in the limiting replacement by the same finite mixture, by the union bound. The tuple of targets may vary with the source cutoff.

### Index and threshold crossing

For either limiting label \(f\), choose one physical forward ray \(R_C\) in each escaping component. Then
\[
 f-\sum_{C\ {\rm escaping}} b'_C\mathbf1_{R_C}\in c_0(\mathbb N_{>0}).  \tag{2}
\]
Indeed, all targets outside the forward paths from \([1,M]\) have \(f(v)\le d_v\le\varepsilon(M)\to0\) by the small-ancestor theorem. Only finitely many components are represented by these paths; in each represented escaping component every path shares a tail with its chosen ray, and its label tends to \(b'_C\). In unrepresented components, \(b'_C\le\varepsilon(M)\) because the small-ancestor bound holds all along the chosen ray. Represented periodic trajectories are finite. This proves (2) after a finite deletion for each prescribed accuracy. The sum in (2) is well-defined since the rays are disjoint; \(b'_C\le m_C\), and \(\sum m_C=1\).

Choose \(t>0\) different from all escaping charges. Since only finitely many charges exceed any fixed positive floor, (2) implies \(P_t=\mathbf1_{\{f>t\}}\) differs at only finitely many vertices from the indicator of the finitely many rays with \(b'_C>t\). On \(\ell^2(\mathbb N_{>0})\) put \(S e_n=e_{Tn}\), so \(\|S\|\le\sqrt2\), and use the same notation for a diagonal multiplier as for its sequence. Then
\[
 \operatorname{ind}\big(P_t S P_t + I-P_t\big)
       =-\#\{C:b'_C>t\}.                                      \tag{3}
\]
For the exact disjoint-ray projection the compressed operator is one unilateral forward shift per ray and the identity on the complement. A finite change of the projection changes the operator by finite rank. Equivalently, the **unweighted edge count** of marked sources exiting \([1,X]\) minus marked sources entering it is exactly the number on the right of (3) with positive sign, for all sufficiently large \(X\). Each ray has net outward count one as soon as its first state is below \(X\), by telescoping its visits; its positive integer states eventually exceed each fixed \(X\).

The source approximation (1) therefore recovers this Fredholm index already from a sufficiently accurate finite mixture. Indeed the threshold has a positive gap from the values of \(f\) outside a fixed finite set, by (2). The resulting projection agrees there. But the functions \(w_\bullet(r)\) in the mixture contain the complete forward trajectories of ordinary starts \(r\). The finite-source approximants need not have index zero. By contrast, truncating all those trajectories at a finite time gives finite-rank diagonals and zero index after compression with the exterior identity. On a ray of positive charge the latter truncations cannot converge in norm to the complete-future mixture.

The branch algebra result [O1](../operator/COMPONENT_OPERATORS.md) gives another way to see the loss of local approximation. Every Fredholm element of that algebra has index zero, since its full and essential spectra agree. The same is true after adding arbitrary compact corrections. If a threshold selects at least one ray, its compressed shift in (3) is outside that enlarged algebra. This uses the algebra's stated ordinary representation, with the periodic multipliers in O1. The mathematical problem is to force vanishing of (3) using additional arithmetic information.

### A deterministic binary countermodel

Here is a concrete graph on the *positive ordinary integers* in which the regularity of both source sampling and first passage is stronger than (1), while every source escapes. It has different arithmetic branches from the Collatz shortcut.

Write \(n=2^k+r\), \(0\le r<2^k\). Define
\[
 F(2^k)=2^{k+1},\qquad
 F(2^k+r)=2^{k-1}+(r\bmod2^{k-1})\quad (r>0).
\]
Before first reaching a power of two, the map removes exactly one level and retains the low bits. Its first power of two is \(2^{v_2(n)}\); it then follows the single escaping ray of powers of two. Each fiber has at most two elements. The distinct visited nodes include at most two members of any binary level, so their high reciprocal sum is \(O(1/H)\) uniformly in the source.

For \(a=2^k+r\), \(r>0\), the predecessor set is exactly \(\{x\ge 2^k:x\equiv r\pmod {2^k}\}\). At \(a=2^j\) it is precisely \(\{x:v_2(x)\le j\}\). These claims follow by following the low bits or the first power of two. Thus
\[
 d_{2^k+r}=2^{-k}\quad(0<r<2^k),\qquad d_{2^j}=1-2^{-j-1}.
\]
The uniform empirical approximation error for all unweighted targets is at most \(2/Y\). For a congruence class of step \(2^k\), the finite initial deletion costs at most one point in the class, and any residue count has error at most one. For \(a=2^j\), count multiples of \(2^{j+1}\) directly. Targets without an ancestor at most \(M\) are necessarily off the ray and have \(d_a<2/M\).

The threshold here is on all positive states. The probability under natural density of never reaching \([1,M]\) is \(2^{-\lfloor\log_2 M\rfloor-1}\). On successful first passage from above \(M\) the landing is greater than \(M/3\): a descending step satisfies \(x\le3F(x)\). At each fixed barrier, the first-passage law exists. In fact an off-ray first landing \(r\) requires the sample to belong to its fixed residue basin, then excludes the finitely many children also at most \(M\) and their basins. For a power-of-two landing \(2^j\) from above, the first power must be exactly \(2^j\), so its probability is at most \(2^{-j-1}\); that event also excludes those descendants passing a child at most \(M\), as can be checked from the level-\((j+1)\) low bits. The finitely many starts already below the barrier do not affect natural densities. Thus each successful landing has mass \(O(1/M)\), and so does the default atom after adding failure. Equivalently, to see existence for every landing without any boundary case, for a start at a level above \(k=\lfloor\log_2 M\rfloor+1\) the low \(k\) bits determine either its chain of off-ray ancestors down from that level or its failure if the low bits are all zero. The default-valued law therefore reduces, up to finitely many starts, to ordinary residue counting. The constants and exponents in these assertions pertain to this model.

For \(t=1/2\), the unweighted threshold picks precisely the powers \(2^j\) with \(j\ge1\). Its compressed shift has Fredholm index \(-1\). Its nonlinear outward-minus-inward current for the actual edges of \(F\) tends to one for every \(p>1\), by the same tree telescoping; this model does not obey the Collatz annular endpoints. No asymptotic smallness of the complete-orbit empirical error, tightness of minima, diffuseness of landing atoms, or convergence of the nonlinear defect in \(\ell^1\) alone forces the index to vanish.
