# True event-height cost of edit returns on one fixed rational source

**Proposed written theorem.** Fix a nonperiodic signed rational Collatz trajectory. Start on a tail of constant sign with common denominator $q$ prime to six. Use either its raw shortcut parity word or its native odd valuation word. Write $y_j=q x_j$, $L(j)=\log_2(|y_j|+q)$ and $W(t)=\max_{0\le j\le t}L(j)$. Set $\gamma=\log_23$ and $\beta=\gamma-1$. Fix $0<a<(1-\beta)/\beta$. For $1\le\ell\le aP$ compare the first $P$ letters and their length-$P$ lag-$\ell$ block. For **every separated edit alignment** of these words, charge each unequal or one-sided column the sum $w_i$ of the two values of $L$ at its actual post-column states. Then, uniformly in the lag and these alignments,
$$
                  \frac1P\sum_{i\text{ an edit}} w_i\longrightarrow\infty.       \tag{1}
$$
For an ordinary Levenshtein minimum which may use agreeing physical states, fix also $0<b\le a$. Its unweighted distance $d_E$ satisfies
$$
    \inf_{bP\le\ell\le aP}
       \frac{d_E(w[0,P),w[\ell,\ell+P))\,W(\lfloor(1+a)P\rfloor)}{P}
              \longrightarrow\infty.                                             \tag{2}
$$
No lower bound on the lag is needed in (1) because separation is already imposed. The restriction in (2) avoids the alignment of cost at most $2\ell$ for every word whatsoever. This extends the [ordinary fixed-source weighted Hamming theorem](../ordinary/FIXED_SOURCE_MISMATCH_WEIGHT.md) to signed rational trajectories and actual insertions/deletions, including raw shortcut bits.

## Uniform endpoint deficit for the two native clocks

Let $G$ count alignment columns containing at least one odd-grade update. There are at most $2P$ columns. On the odd clock $G\ge P$, and the true common endpoint heights in the [edit-aligned theorem](EDIT_ALIGNED_ORBITS.md) obey
$$
 H_{\rm start}+h_{\rm end}\le L(\ell)+L(P)+O(1)
                 \le\beta(1+a)P+O_{x_0}(1).
$$
In the first inequality the constant covers the fixed initial height, including early lags. On the raw clock, $G\ge g(P)$, the actual odd count on the first track. The native logarithmic identity there gives $g(P)=(P+L(P)+o(P))/\gamma$. Consequently on either clock
$$
      G-H_{\rm start}-h_{\rm end}\ge (1-\beta-\beta a)P-o(P).            \tag{3}
$$
For the raw bound subtract $L(\ell)+L(P)+O(1)$ from $g(P)$ and use $L(j)\le\beta j+O(1)$, together with $(1-\beta^2)/\gamma=1-\beta$. The small error is uniform in the lag and the alignment. Fix $\epsilon>0$ small enough that $(1-\epsilon)G-H_{\rm start}-h_{\rm end}\ge\delta P$ for some fixed $\delta>0$ and all large $P$.

## Post-edit states and the true minimum over alignments

Mark the $N$ post-edit column boundaries strictly inside the path. A possible terminal edit is left in its last segment. For fixed $m\ge1$ make $m$ complete partitions by cutting after every $m$-th marked edit, once for each residue class of the mark index. Each segment has at most $m$ edits, keeps separation, and uses its genuine start and endpoint. Summing the uniform finite form of the [edit height inequality](EDIT_ALIGNED_ORBITS.md) over the $N+m$ segments in all partitions yields
$$
 m(1-\epsilon)G\le m(H_{\rm start}+h_{\rm end})
           +\sum_{i\text{ interior edit}}w_i+C_{m,\epsilon,q}(N+m).     \tag{4}
$$
The constant includes the fixed denominator charge.

Suppose the total event weight were $O(P)$ along a violating sequence. Assign each interior edit to a track which actually takes a step in that column. At least $N/2$ are assigned to one track; for that track the assigned post-step indices are distinct. The input orbit has distinct same-sign integral numerators, so the sum of the assigned log-heights is at least $\log_2(\lfloor N/2\rfloor!)$. Thus $N=o(P)$, including when the other side waits through many successive columns. Divide (4) by $P$ and use (3). The lower limit of the normalized event weight along this sequence is at least $m\delta$ for every previously fixed $m$. This contradicts its assumed boundedness and proves (1).

Every event has $w_i\le2W(\lfloor(1+a)P\rfloor)$. A minimum-cost equal-length alignment which pairs a repeated physical state must have spent at least $2\ell$ indels to accumulate and then undo its offset. In the band $bP\le\ell$, such a minimum already has $d_EW/P\ge2bW\to\infty$. All other minima are separated and (1) proves (2). The estimates concern one fixed actual source; $W(t)\to\infty$ because its rational states are distinct.

## Finite moving templates at the physical scale

Set $P=2M$, $\ell=M$. Let any length-$3M$ word $v$ over the appropriate alphabet have overlap distance
$$
          d_E(v[0,2M),v[M,3M))\le B
$$
for some fixed $B$, and let $E=d_E(w[0,3M),v)$. Restrict an optimal whole-prefix alignment to its first $2M$ input letters. Its corresponding template endpoint differs from $2M$ by at most $E$, so trimming or extending its template side gives $d_E(w[0,2M),v[0,2M))\le2E$. Restrict to the final $2M$ input letters in the same way to obtain $d_E(w[M,3M),v[M,3M))\le2E$. Triangular comparison gives actual overlap distance at most $4E+B$. Since $W(3M)=O_{x_0}(M)$, (2) implies
$$
                      \frac{E W(3M)}M\longrightarrow\infty.             \tag{5}
$$
This holds uniformly over the supplied templates, even when they have unrestricted internal factor complexity. For instance, it applies to three copies of any changing length-$M$ word. If $|x_j|\le C(j+1)^d$ on the chosen clock for fixed constants, (5) implies $E\log(M+2)/M\to\infty$.

A coding by interval labels of a circle rotation with at most $b_0$ boundary points has $B\le14b_0$ whenever $|\alpha-r/M|\le M^{-2}$ and $r/M$ is reduced. The [finite grid proof](../ordinary/FIXED_SOURCE_MISMATCH_WEIGHT.md) counts at most seven grid points within $3/M$ of each boundary over each length-$M$ lap; the two laps contain all possible disagreements. This applies directly either to the binary shortcut alphabet or to the odd-valuation alphabet. The angle, labels, phase and intervals can all change with $M$. Prior [Paper 173/v1](https://rstation.ai/problems/collatz/papers/173/v1) already excludes bounded edits on unbounded prefixes for a family with uniform $O(k)$ factor counts, by its full superlinear-complexity result. Formula (5) supplies a stronger height-dependent error scale; the unrelated three-copy family requires no uniform factor count. For orbits with $W(3M)$ proportional to $M$, (5) gives error tending to infinity with no effective rate.

## Integer controls and scope

The [exact ledger checker](check_edit_aligned_orbits.py) replays 843 physical two-track alignments using both clocks and both signs, including 412 negative paths. Normal and optimized runs agree on 24,899 columns, 1,851 one-sided edits, 6,482 one-sided nonzero-form contributions, 1,331 carry-free subblocks and 502 even raw carries. It checks every normalized partial state and the multiplicative one-envelope carry estimate with rational arithmetic. These controls cover the arithmetic ingredients; the Subspace Theorem, event partition and uniform limits are written arguments.

Arbitrary words need not have such short approximate returns, even when their cumulative odd frequency is prescribed. The proof supplies a necessary arithmetic event cost on a real orbit. It does not force a return contradicting that cost on every exceptional positive source.
