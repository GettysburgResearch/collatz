# One tested suffix on each selected head row

**PROPOSED written corollary.** Choose an integer \(M\ge4\), four distinct row residues \(c_0,c_1,c_2,c_3\bmod M\), any fixed integer \(Q\ge0\), and a nonempty open interval \(J_p\subset(7,8)\) for each \(p\). Use the suffixes \((r_0,r_1,r_2,r_3)=(0,27,45,57)\). Set \(a_0=A_0^*=0\) by convention, and work on positive head rows \(j\ge1\), with \(R_j=81^j\). As usual \(a_j\) is the full normalized number of original child-parent label disagreements. Count a child \(x=81m+r\) towards \(A_j^*\) only when it is truly discordant and for some \(p\)
\[
 j\equiv c_p\pmod M,\qquad x/R_j\in J_p,\qquad r=r_p,\qquad
 2^Q\mid x,\qquad m\equiv-1\pmod {2^p}.
\]
Normalize by \(R_j\) as in the full series, including on a restricted row. On every other row set \(A_j^*=0\). At most one suffix is tested per row. For **any** fixed choices above and any invariant label,
\[
 \sum_{j\ge1} a_j<\infty\quad\Longleftrightarrow\quad
 \sum_{j\ge1} A_j^*<\infty.
\]
The two-convolution bound (1) of [the full series comparison](FOUR_SUFFIX_EQUIVALENCE.md) also holds with \(A^*\) in place of \(A\), with constants depending on the fixed choices. In particular its little-o transfer at each fixed \(0<\alpha<1\) still holds.

For the proof, use the [exact routes](FOUR_SUFFIX_ROUTING.md). Write \(k=k_0+18t\) and choose \(t\ge\lceil Q/18\rceil\). In the explicit formulas \(x=2^{p+k}3^{4-p}u\) and \(m=2^p v-1\), this gives the required child divisibility and parent residue. Route the real logarithm on the circle **of length \(M\)**. For each \(p\) the desired arc on that circle is \(c_p+\log_{81}J_p\). The step \(18\log_{81}2\) divided by \(M\) is irrational, so every starting phase reaches that arc in a bounded number of steps, uniformly in \(u,k_0\). The four arcs yield one common finite bound. One may also omit any prescribed finite set of initial rows by increasing the lower bound on \(t\) a fixed amount. Every chosen scale still satisfies \(u\le x\le C u\). For each \(p\) the multiplier list is finite, so the original bounded-multiplicity counting proof and its factor \(1/81\) on the recursive term apply unchanged. The full-series comparison follows.

The allowed rows have density \(4/M\) among level indices and every tested child begins with at least \(Q\) even shortcut steps. Both parameters are fixed before applying the theorem. Allowing either to grow with the row would change the size and multiplicity constants used in the proof.
