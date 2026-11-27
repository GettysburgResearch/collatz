# Initial gaps of ordinary critical predecessor layers

**Status.** Source-qualified written proof. The inputs are the averaged joint ternary oscillation in Paper 5 and the positive shell comparison, stopping-location convergence, and source-window estimates in Paper 176. A separate stronger version uses the fractional excess precision theorem in Paper 48. The deconvolution and the application to a fixed actual disagreement are additional steps. All logarithms are natural. Write \(S\) for the positive odd Syracuse map and \(T\) for the one-division shortcut.

## Geometric deconvolution at excess ternary precision

Fix a terminal precision \(N\) and use \(G_N=\mathbb Z/3^N\). Let the reversed gaps \(e_i\) be independent with probabilities \(2^{-e}\), \(e\ge1\). Put \(D_j=\sum_{i\le j}e_i\) and \(B_j=\sum_{i=1}^j 3^{i-1}2^{-D_i}\) in \(G_N\) for every \(0\le j\le N\), including \(j<N\). Let \(\mu_j\) be the joint law of \((B_j,D_j)\) on \(G_N\times\mathbb Z\). Extend the law by zero to all integer totals. For \(1\le m\le N\) define
\[
 (E_m f)(z,t)=3^{m-N}\!\!\sum_{z'\equiv z\bmod3^m} f(z',t),\qquad
 {\rm JOsc}_{m,N}(B_j,D_j)=\|(I-E_m)\mu_j\|_{\ell^1(G_N\times\mathbb Z)} .
\]
The input is \({\rm JOsc}_{m,N}(B_N,D_N)\le C_A m^{-A}\) for every \(A>0\), uniformly in \(m,N\). [Weaver, Paper 5 v3, equation (1)](https://rstation.ai/problems/collatz/papers/5) · [Wren, Paper 10 v3, input (J)](https://rstation.ai/problems/collatz/papers/10/v3)

On signed measures write \(Qf(z,t)=f(z,t-1)\), \(K=\sum_{b\ge1}2^{-b}Q^b\), and let \(T_j\) denote pushforward by \((z,t)\mapsto(z+3^j2^{-t},t)\). Then
\[
 \mu_{j+1}=T_jK\mu_j,\qquad
 K^{-1}=2Q^{-1}-I,\qquad
 \mu_j=(2Q^{-1}-I)T_j^{-1}\mu_{j+1}.                         \tag{1}
\]
The series converges in operator norm. Multiplication on either side by the proposed inverse telescopes to the identity. All three operators commute with \(E_m\), since at a fixed \(t\) the shear is a group translation. The inverse shear is an isometry and \(\|K^{-1}\|\le3\). Iteration at the same ambient precision \(N\) gives
\[
 {\rm JOsc}_{m,N}(B_{N-L},D_{N-L})\le 3^L C_A m^{-A}.        \tag{2}
\]

For \(0\le L\le N-m\), let \(w=(g_1,\ldots,g_L)\) be the first \(L\) gaps in **forward source order**, and \(P_L(w)=2^{-\sum_i g_i}\). Reverse the length-\(N\) word. Given this mark, the first \(N-L\) reversed variables remain free and the remaining reversed variables are \(g_L,\ldots,g_1\). Appending a specified gap \(b\) shifts \(t\) by \(b\) and then applies \(T_j\), a permutation commuting with \(E_m\). If \(\sigma_{N,w}\) denotes the subprobability of the terminal offset with this mark, marginalization over totals in (2) gives
\[
 \sum_w\|\sigma_{N,w}-P_L(w)\,3^{m-N}\pi_m(\cdot\bmod3^m)\|_1
       \le 3^L C_A m^{-A}.                                     \tag{3}
\]
Here \(\pi_m\) is the natural depth-\(m\) residue law. The low-trit marginal of each conditional offset is exactly \(\pi_m\), since all steps past \(m\) change the offset by multiples of \(3^m\). The bound for each subprobability includes the factor \(P_L(w)\), paying for all countably many marks.

## Marking the physical stopping layer

For \(d\ge L\), write \(M_d(v)=3^d 2^{-D_d(v)}\) with the total on the actual forward odd orbit, and let \(w_L(v)\) be its initial gap mark. Define
\[
 W_d(z)=\sum_{S^d v=z}M_d(v),\qquad
 \Lambda_{d,L}(w,z)=\frac1{z(3z+1)}
       \sum_{\substack{S^d v=z\\w_L(v)=w}} M_d(v).
\]
The sums are over positive odd integers. Let \(D=\log(4/3)\). Use the finite stopping-location law \(\nu\) of Paper 176 Theorem 2, with mass at most one. For every fixed \(C<\infty\), uniformly over integers \(0\le L\le C\log(2+d)\),
\[
 \left\|\Lambda_{d,L}-P_L\otimes (D\nu/2)\right\|_1=o_C(1)
                 \qquad(d\to\infty).                            \tag{4}
\]
At a fixed odd \(z\) with \(h(z)=\lim_dW_d(z)>0\), the initial \(L\) gaps of a physical source sampled with probability \(M_d(v)/W_d(z)\) approach \(P_L\) in total variation. The unit atom floor gives \(h(z)>0\) for ordinary odd units. A multiple of three has an empty predecessor layer at positive depth. [Weaver, Paper 176 v1, §§2–4](https://rstation.ai/problems/collatz/papers/176/v1) · [Wren, Paper 10 v3, Theorem 2](https://rstation.ai/problems/collatz/papers/10/v3)

Set \(f_j(v)=\prod_{i<j}3S^iv/(3S^iv+1)\) and \(p_r(v;E)=f_r(v)\mathbf1_{S^rv\in E}/(3S^rv+1)\), with \(p_r=0\) at negative indices. Then \(f_d(v)/v=M_d(v)/S^dv\), and \(\sum_r p_r(v;\mathcal O)\le1\). The mass in (4) over any set \(\{(w,z):z\in E_w\}\) is \(\sum_v p_d(v;E_{w_L(v)})/v\).

Use the source log-height central block \([u,\gamma u)\) in Paper 176 §4, where \(\alpha=1.001,\ \gamma=\alpha^{1/2},\ \kappa=\alpha^{5/4},\ u=Dd/\sqrt\gamma,\ l=u/\kappa,\ x=e^l,\ \ell=\lfloor l^{4/5}\rfloor\). The shell consists of positive odd \(y\) satisfying \(|\log(y/x)-D\ell|\le l^{7/10}\) and whose first odd passage to \([1,x]\) takes exactly \(\ell\) steps. Its measure is \(\phi_x(y)=2W_\ell(y)/(Dy)\). The unmarked noncentral contribution tends to zero, hence controls the marked one by positivity. Specifically, the retained geometric blocks outside the center in Paper 176 (17) have total \(o_{R,B}(1)+O(R^{-1/10})\). The lower omitted tail contains finitely many sources at fixed \(R\), each with \(p_d(v;\mathcal O)\to0\). For sufficiently large fixed \(B\), the higher omitted tail is \(o(1)\) by that paper's §2 large-source estimate beyond \(\exp(Bd)\). First increase \(d\), then \(R\). At the center the bad-source contribution is \(O(u e^{-c u^{1/5}})\), and canonical prefix lengths \(k>d\) cost \(O(u/x)\), by the bounds preceding (15). All these bounds hold simultaneously over the marked test.

A good source has canonical prefix length \(k=\tau_x(v)-\ell\) comparable to \(l\), at most \(0.02l\), and shell state \(y=S^kv\). Use the eligible lengths in (16): \(D(k+\ell)\) is between \(u-l-O(u^{4/5})\) and \(\gamma u-l+O(u^{4/5})\), and \(\ell\le k\le0.02l,\ k\le d\). In particular \(\ell+L\le k\) for large \(d\), uniformly in the claimed mark range. For prefix total \(t\), the exact contribution from (15) is \(3^k2^{-t}p_{d-k}(y;E_w)/y\). Enlarge the canonical prefix sum to every legal word at each such \(k,y\). The marked residue sum becomes
\[
 \sum_{k,y,w}\frac{3^k}{y}\,\sigma_{k,w}(y\bmod3^k)\,
                                      p_{d-k}(y;E_w).
\]
The shell bound (10) in Paper 176 is \(\sum_y3^k|\sigma(y\bmod3^k)|/y\le C_0\|\sigma\|_1\), uniform throughout these lengths. Apply (3) with \(N=k,m=\ell\). Summing in \(w,k\) costs \(O_A(d\,3^L\ell^{-A})=o_C(1)\), by choosing a sufficiently large fixed \(A\) depending only on \(C\). The remaining sum is at most
\[
 \frac D2\sum_w P_L(w)\sum_y\phi_x(y)\sum_{r\ge0}p_r(y;E_w)
      =\frac D2\sum_w P_L(w)\nu(E_w)+o(1).
\]
Indeed, distinct \(k\)'s have distinct residual indices. The shell stopping-location law in Paper 176 §4 before (15) converges uniformly over all subsets of odd integers, and \(\sum_wP_L(w)=1\). This upper bound holds uniformly for every marked set. Apply the same bound to its complement and use unmarked total convergence to obtain (4).

## Positive linear source horizon with the stronger primary input

There is an absolute \(\lambda_*>0\) such that (4) holds uniformly for every \(L\le\lambda_*d\). Use Weaver and Wren's Paper 48 v2, Theorem 6, equations (65)–(66): for each fixed \(B>0\) there are \(\delta_B,C_B>0\) such that the original independent geometric offset of length \(N'\), together with its exact total, has joint oscillation at most \(C_B m^{-B}\) on ternary precision \(q=N'+K\), provided \(0\le K\le\delta_B N'\) and \(1\le m\le q\). The dependence of the allowable fraction on the desired power is retained. [Weaver and Wren, Paper 48 v2, §8](https://rstation.ai/problems/collatz/papers/48)

Set \(B=4\). In the central shell, \(k/d\) has a positive absolute lower bound \(c_0\) for all large \(d\). Indeed \(k\ge (u-l-O(u^{4/5}))/D-\ell\), with \(u=Dd/\sqrt\gamma,\ l=u/\kappa\). Any \(0<c_0<(1-1/\kappa)/\sqrt\gamma\) works eventually. Fix
\[
          0<\lambda_*<c_0\,\frac{\delta_4}{1+\delta_4}.
\]
For each eligible \(k\), take \(N'=k-L\), \(K=L\), \(q=k\), \(m=\ell\). Then \(K\le\delta_4 N'\), and \(\ell\le N'\) eventually. Theorem 6 applies directly to the free initial reversed letters at this ambient precision. The deterministic shifts and shears for the final reversed letters, the exact low-trit projection, and the summation with weights \(P_L(w)\) give (3) with right side \(C_4\ell^{-4}\). The shell comparison therefore costs \(O(d\ell^{-4})=o(1)\). The noncentral tails, complement argument, and positivity are identical to those already justified. This proves
\[
       \sup_{0\le L\le\lambda_*d}
       \|\Lambda_{d,L}-P_L\otimes(D\nu/2)\|_1\longrightarrow0.       \tag{4a}
\]
All constants here are independent of the fixed ordinary target subsequently conditioned on; that conditioning has a target-dependent error. The logarithmic proof above uses the weaker natural-depth oscillation premise. The two arguments use the same untilted geometric gap law. The shell stopping-location and source-tail errors are qualitative.

## Coalescence on the layer of every fixed ordinary target

Use \(s_p(X)\) from [the critical-layer definition](POINTWISE_CRITICAL.md), so the lower and upper arms travel the same physical clock, have \(p\) odd departures apiece, and end at \(X\) and \(3X-1\). Extend the same per-grade sum to every ordinary \(X\ge1\), allowing all paired paths even on a cycle. For every such fixed \(X\),
\[
                         \lim_{p\to\infty}s_p(X)=0.                \tag{5}
\]
Fix \(d_0=v_2(X)\) and \(V=2^{-d_0}X\). At \(p\ge1\), strip the initial \(a=v_2(Y)\) lower even clocks and append the \(d_0\) final lower even clocks. The resulting odd path from \(v=Y/2^a\) to \(V\) has odd depth \(p\), and its multiplier \(M_p(v)\) satisfies \(3^p2^{-H}=2^{d_0-a}M_p(v)\). For fixed \(a,v,p,X\) at most one physical length \(H\) is possible: the terminal \(V\) is the endpoint of precisely those \(p\) odd edges, and the fixed \(d_0\) determines the previous cut. If \(3\mid V\), the sum is empty.

After the \(a\) initial clocks, the actual pair is \((v,3^{a+1}v-1)\). There are at least \(p\) remaining shortcut clocks, since the lower arm still has \(p\) odd departures. The two terminal integers \(X\) and \(3X-1\) are distinct. Determinism therefore forbids synchronous equality on any of these remaining clocks. Failure of affine coalescence through \(L\le p\) is necessary, regardless of the basin labels or of later returns. This is a test of \(v\bmod2^L\), since the branch slopes on fixed residues determine whether the affine germs have fused. The odd-source initial \(L\) gap mark determines this residue: its total is at least \(L\), and a word of total \(t\) fixes an odd class modulo \(2^{t+1}\). Under \(P_L\) these bits have exactly odd Haar law by ordinary residue counting. Under unrestricted fair bits the affine fusion failure has probability \(O((a+2)/\sqrt L)\), from the general initial-state bound at rank \(a+1\), offset \(-1\). Restricting to the odd half of the sources costs at most a factor two. [PR146, general initial states in the elapsed-time bound](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md)

For \(3\nmid V\), (4) at \(z=V\) transfers this test to the \(M_p\)-weighted inverse layer, with unnormalized error \(o_V(1)\) uniform in the test and \(a\). Take \(L=\lfloor\lambda_*p\rfloor\) under (4a), or \(L=\lfloor\log(2+p)\rfloor\) under (4). Sum the bounds with weights \(2^{-a}/V\) over all \(a\ge0\), using \(\sum_a2^{-a}(a+2)<\infty\). This proves (5) without a source cutoff or averaging over \(p\). More positively, sample \(v\) from the entire one-arm inverse layer to fixed \(V\) with its normalized \(M_p\)-weights. For each fixed \(a\) the pair \((v,3^{a+1}v-1)\) fuses by \(\lfloor\log(2+p)\rfloor\) shortcut clocks (also by any growing \(L\le\lambda_*p\) under (4a)) with probability tending to one. This is actual equality at a common finite clock. When \(d_0>0\), this statement on all \(v\) does not require that truncating the last \(d_0\) halvings of the odd path has endpoint \(X\); only the upper bound on the paired subfamily uses that truncation.

Combined with the moving-target bound in [POINTWISE_CRITICAL.md](POINTWISE_CRITICAL.md), (5) gives \(c_0\) on the discrete set of all pairs \((X,p)\) with \(X\ge2\) and ordinary upper-good terminal: each fixed positive threshold is exceeded only finitely often. The theorem bounds individual grade layers. One-arm positivity does not count synchronized opposite-label arms. Convergence of the full sum \(\sum_p s_p(X)\), or a lower mass forcing a source below its original component minimum, remains open.

**Checked scope.** [GeometricDeconvolution.lean](GeometricDeconvolution.lean) verifies the exact unsheared count recursion and rational geometric law recovery, including the Syracuse specialization in a fixed ternary residue ring. The imported mixing and physical shell transfer are written arguments. [Strict Lean output](../../../reports/astra-sixhour-20261127/transport/geometric-deconvolution-lean.txt)
