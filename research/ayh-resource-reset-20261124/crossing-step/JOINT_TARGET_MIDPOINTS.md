# Simultaneous centered neighbors of both smaller discordant heads

**PROPOSED written theorem.** This combines the [two-head graph](WEIGHTED_TWO_HEAD_GRAPH.md) with the centered-progression theorem for exact ordered future fibers. Its application is to the **two smaller heads together**, using a new parameter there. A single original native record can freeze all its later witnesses; generating siblings in that original record would not give distinct target edges.

Fix an open mantissa arc \(J\subset(7,8)\) and choose a smaller open \(J_0\) whose closure lies inside \(J\). In the graph construction use two shorter, separated slabs
\[
 I_1=[3d,3.003d]\cap\mathbb Z,\qquad I_2=[3.012d,3.015d]\cap\mathbb Z.
\]
They still have lengths comparable to \(d=\log_2R\). Use \(J_0\) for the original witnesses and \(J\) for the graph vertices. Set \(K=\lfloor2^{.01d}\rfloor\). For each \(A>1\), outside \(O_A(Rd^{-A})\) original children, **every** returned true pair in these two slabs with heads in \(J_0\) satisfies the following. Write \(v=t_2-t_1,\ w=k_2-k_1\). For at least
\[
                K\exp(-C_A(\log(d+2))^{12})
\]
distinct positive \(L\le K\), both pairs
\[
 (z_1-81\,2^vL,\ z_2-81\,3^wL),\qquad
 (z_1+81\,2^vL,\ z_2+81\,3^wL)
 \tag{1}
\]
are pairs of genuine discordant smaller heads, in the same respective rows and in \(J\). Each preserves the original ordered colors of all four child/parent integers, the same clock-gap and exponent labels in the arithmetic relation, and the very same bounded additive rounding difference there. In particular the off-diagonal graph inequality still holds after restricting its sum to target edges with these many centered neighbors on the same arithmetic branch, allowing fixed slack in the vertex height bands and error constant. The shifted edges are genuine color comparisons. Their realization as two new outputs of an original head row is not claimed.

**Four arms on one ordinary interval.** From the original two source approximations, \(z_2=3^w2^{-v}z_1+O_A(1)\) since \(3^w2^{-v}=2^{-av+O_A(\sqrt{d\log d})}<1\), \(a=1-(\log_2 3)/2\). Therefore
\[
 z_2=\lfloor3^w2^{-v}z_1\rfloor+b,\quad |b|\le C_A .
\]
For large \(d\), \(.009d-O(1)\le v\le.015d+O(1)\) and \(4\le w\le v\). Fix \(v,w,b\), the row \([7Y,8Y)\) of \(z_1\), and its residue \(s\) modulo \(81\,2^v\). Write \(z_1=81\,2^v q+s\). On this consecutive interval of \(q\)'s,
\[
 z_2=81\,3^w q+b_s,\qquad b_s=\lfloor3^w s/2^v\rfloor+b.
\]
Give the first head pair \(z_1,\lfloor z_1/81\rfloor\) exactly \(v\) shortcut steps. Their resulting ordinary forms in \(q\) have slopes \(81\,3^{p_1}\), \(3^{p_2}\) with \(0\le p_i\le v\), by the standard high-bit affine identity on this fixed prefix. Leave \(z_2,\lfloor z_2/81\rfloor\) at their initial clock, where they have slopes \(81\,3^w,3^w\). The four slopes are now positive odd integers bounded by \(81\,3^v\). Intercepts can be signed; all arms on the actual interval are positive for the relevant rows and bounded corrections.

Use complete blocks of length \(H=2^h,\ h=\lfloor.28d\rfloor\). The parent parameter interval has length \(Y/(81\,2^v)+O(1)\); from the first slab, \(\log_2Y=(1-3a)d+O(.003ad+\sqrt{d\log d})>.37d\) eventually. Discard partial end blocks. Uniformly in the chosen residue their relative cost is \(O(2^{-.07d})\). On a full block, each arm separately has a fair \(h\)-bit parity word, so the exceptional fraction with some new odd count exceeding \(.53h\) is \(O(e^{-c h})\). Thus the largest-slope parameter of the subsequent record satisfies
\[
 \log_2 F\ge h-(v+.53h)\log_2 3-\log_2 81 > .02d
\]
eventually. This explicit calculation replaces any fixed-coefficient asymptotic, since \(v\) grows with the source row.

Apply the ordered four-arm projection with a prescribed power discard \(O_M(d^{-M})\), followed by the centered-progression theorem with stride one and the displayed \(K\). Its constants depend on the number of arms and polynomial fiber density and diameter parameters, uniformly in the original odd slopes and intercepts. Here \(K\le F\) and \(K\ge\exp(C'_M(\log(h+2))^{12})\) eventually. All but \(O_M(d^{-M})\) of the actual \(q\)'s have at least the asserted number of shifts \(q\pm L\) with the same full ordered record as \(q\). Returning through the four labels gives (1); the slopes in the displayed formulas show the bounded rounding error is identical, even before taking logarithms. The changes in both smaller heads are \(2^{.04d+O(1)}\) or less, whereas both head values exceed \(2^{.3d}\). Their fixed interior margin therefore preserves the row and the arc \(J\).

**Transfer to all original sources.** For one row and \(v,w,b\), sum over all \(81\,2^v\) residues of \(z_1\). The relative small exception on each \(q\) interval costs a total \(O_M((d^{-M}+2^{-.07d})Y)\) possible \(z_1\), with at most one \(z_2\) per \(z_1\) for this fixed triple. In particular no exponential residue factor survives. There are \(O(d)\) first head rows and \(O_A(d^2)\) choices of \(v,w,b\). Each exceptional target pair is produced by at most \(O_A(R\sqrt{\log d}/z_1)\) original discordant source/time pairs, by the reverse count in the two-head graph proof (with the designated \(v,w\) already fixed). Taking \(M>A+5\) and summing gives \(O_A(Rd^{-A})\) original children having even one such exceptional pair. The same conclusion for true pairs with a concordant original source follows if desired by using the weaker raw strip count \(O_A(R\sqrt{d\log d}/z_1)\), which is still polynomially absorbable. Add the single previously stated original source-envelope exception. The original graph forward argument gives \(\gg d^2\) off-diagonal pairs on each remaining good discordant source, now with the midpoint property at both target heads.

This removes target graph regions with too few such exact parallel neighboring edges. Many translated edges on one arithmetic branch need not decrease its weighted degree. No estimate here bounds the full degree of the remainder.

**Sources.** The late-track and two-head papers pinned in this packet, PR 197 \(\mathtt{6eb986b0ce0b1836a356474d25d709ed4e948b67}\), ADAPTIVE_PAIRED_PROJECTION.md (four odd affine arms, with bounds uniform in their coefficients), and SYMMETRIC_FUTURE_FORKS.md as reconstructed at SHA-256 \(\mathtt{7857698938cf63ea0fef0efeb0a06a3fd9ea59446854bb9d1529ddab0c322128}\). The centered-progression count uses Bloom and Sisask, Theorem 21, DOI 10.2140/ent.2023.2.15. The density result about fixed target basins is not needed.
