# The stopped first-arrival clock at a moving escaping target

The full corrected-height local law in [PR 195, LOCAL_HEIGHT_LAW, (1)](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/LOCAL_HEIGHT_LAW.md) concerns an entire escaping component at each lattice cell. The following source-qualified deduction also applies when the original physical paths must have *already met a moving specified target*. The early-arrival and uniform signed-tail estimates are those in [the target-stopped source theorem](SHARP_UNIFORM_FIRST_ARRIVAL_ROWS.md). These written analytic inputs have not been formalized here.

Fix an escaping odd ray \(y_N=U^N a\), its actual native clock \(A_N\), \(P_0=P(a)\), \(P_N=P(y_N)=P_0 3^N2^{-A_N}\), and \(f_N=y_N/P_N\to1\). For odd starts put
\[
 m_{r,s}(y)=\frac{3^r2^{-s}}y
    \#\{x\ {\rm odd}:\operatorname{first}(x,y)=(r,s)\}.
\]
Extend it by zero at infeasible or negative clocks. For integers \(v,l\), put \(p=P_0 3^v2^l,\ r=N-v,\ s=A_N+l\), so \(p=P_N2^s/3^r\). Write \(M_v(l)\) for the number of all odd sources of this component at corrected height \(p\), divided by \(p\). Then
\[
 \lim_{\substack{N\to\infty\\ R\to\infty}}
 \ \sup_{\substack{v,l\in\mathbb Z\\p\ge R}}
 \sqrt{\log p}\,|f_N m_{N-v,A_N+l}(y_N)-M_v(l)|=0 .                 \tag{1}
\]
Both parameters may go to infinity independently. With the geometric clock kernel \(g_k(t)=\binom{t-1}{k-1}2^{-t}{\bf1}_{t\ge k}\) for \(k\ge1\), \(g_0=\delta_0\), \(g_k=0\) for \(k<0\), one thus has
\[
 \lim_{\substack{N\to\infty\\ R\to\infty}}
 \ \sup_{p\ge R}\sqrt{\log p}\,
 \left|m_{N-v,A_N+l}(y_N)-H_C g_{-v}(l)\right|=0.                    \tag{2}
\]
In particular the stopped odd row at lag \(r=N+k,\ s=A_N+2k\) has mass \(\sim H_C/\sqrt{4\pi k}\) in the independent limits \(k,N\to\infty\). The grade offset \(N\) and native clock offset \(A_N\) are both necessary in this comparison.

## Identical corrected weights and tight signed forcing

The stopped table \(M^N_v(l)=f_Nm_{N-v,A_N+l}(y_N)\) counts in units exactly \(1/p\). It is the restriction of \(M_v(l)\) to sources that ever meet \(y_N\). For any such source, its first-hit dates are unique because the ray is nonperiodic. These restrictions increase to the entire component. Any ordinary source on a merging orbit meets \(y_N\) for every sufficiently large \(N\). This gives literal equality of the tables from starts \(x<X\) once \(N\) exceeds a finite bound depending on \(X\) and the component.

Let \(B_v^a(l)=M_{v,a}(l)-M_v(l)/3\), with subscript \(a\) specifying the original source modulo 3. Define \(B^{N,a}\) from \(M^N\) using the same rule. Then
\[
 \sum_{a,v,l}|B_v^a(l)-B_v^{N,a}(l)|\longrightarrow0.               \tag{3}
\]
Indeed the parts from \(x<X\) agree eventually, including their weights. For the remaining parts the joint sum norms are \(O_A((1+\log X)^{-A})\) separately, by [PR 195, MARKED_FIBRES, (5)](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/MARKED_FIBRES.md) for the full component and equation (3) of the target-stopped theorem for the moving target, multiplied by \(f_N\le1\). The latter is uniform in \(N\).

Both arrays obey \(M_v=G*M_{v+1}+C_v\) where \(G(e)=2^{-e}{\bf1}_{e\ge1}\). In the full array \(C_v(l)=3\sum_e2^{-e}B_{v+1}^{2^{-e}\bmod3}(l-e)\). The stopped array has the same formula with \(B^{N}\), and also the terminal root impulse \(1/P_N\) at \((v,l)=(N,-A_N)\). This impulse tends to zero since \(y_N\to\infty\). There is no periodic lap. Thus
\[
 \Delta_N:=\|C^N-C\|_1\to0,\qquad
 \sum_{\substack{u,l_0\\p_0=P_0 3^u2^{l_0}\ge L}}
   (|C^N_u(l_0)|+|C_u(l_0)|)\ll_A(1+\log L)^{-A}.                  \tag{4}
\]
For the second bound, the full component has the physical-height tail in PR 195, LOCAL_HEIGHT_LAW (4). For the stopped array apply (6) of the target-stopped theorem: its source height before multiplying by \(f_N\) is \(f_Np_0\). The simple-path correction gives \(f_N\ge c_0>0\) uniformly, and \(f_N\le1\). This explains the uniformity even though the chosen base dates move.

Above grade \(N\) the stopped array vanishes. At \(+\infty\) the full array has grade mass tending to zero by the two-sided grade theorem used in PR 195. Iterating the two recurrences therefore represents their difference at \((v,l)\) by
\[
 \sum_{u\ge v,l_0}(C^N_u(l_0)-C_u(l_0))g_{u-v}(l-l_0).
\]
The terms with \(p_0<\sqrt p\) have kernel \(O((1+\log p)^{-1/2})\) by the real-height kernel estimate in PR 195 (6). The remaining terms have total absolute mass \(O_A((1+\log p)^{-A})\) uniformly in \(N\), by (4). After multiplying by \(\sqrt{\log p}\) the result is \(O(\Delta_N)+O_A((\log R)^{1/2-A})\), proving (1). The full pointwise asymptotic in PR 195 gives (2), since \(f_N\to1\) and \(\sqrt{\log p}\,g_{-v}(l)=O_{P_0}(1)\) as \(p\to\infty\).

## Initial halving clocks

For all positive integer starts, initial dyadic scaling contributes \(2^{-e}\) at native shift \(e\ge0\), without changing the odd grade. The analogue of (1) follows by summing these translates in each of the two arrays. For \(2^e\le\sqrt p\) use (1) at \(p/2^e\); the remaining terms are \(O(p^{-1/2})\) since the individual stopped and full positive odd tables are bounded by an absolute constant. The analogue of (2) has coefficient \(2H_C\). For each fixed \(e\) the translate \(g_{-v}(l-e)\) has the same leading profile as \(g_{-v}(l)\) by PR 195, LOCAL_HEIGHT_LAW (7). The geometric tail for \(e\) beyond a fixed cutoff is handled as in (1), using the point bound at \(p/2^e\) before \(2^e=\sqrt p\).

The inherited source itself corresponds to \(r=N,\ s=A_N,\ p=P_0\), independent of \(N\). Equations (1) and (2) control large original corrected heights and supply no decay at that fixed nonzero cell.
