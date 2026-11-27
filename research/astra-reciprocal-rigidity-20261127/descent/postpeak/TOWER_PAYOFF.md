# A smaller ordinary visitor on almost every protected exponent

Let \(P_r=3^rv-1\) for a fixed, positive odd cofactor \(v\). Take an exponent progression \(H=H_0+Ri\) whose difference \(R\) is twice an odd number. In any interval of \(N\ge2\) consecutive indices \(i\), take only terms \(H\ge J+1\), and set \(g=\lfloor\log_2N\rfloor+3\). For each \(J\ge1\), all but

\[
                 O\!\left(\frac{JN}{\sqrt{\log(2N)}}\right)
\]

of these terms have the following property. Every one of \(P_H,P_{H-1},\ldots,P_{H-J}\) has the same ordinary endpoint after exactly \(g\) shortcuts, with \(Q_g(P_{H-a})=Q_g(P_H)+a\) for each \(0\le a\le J\). The implied constant is absolute. The estimate is informative for \(J=o(\sqrt{\log N})\), and allows a growing \(J\). It applies at every interval location and independently of \(v\), \(H_0\), and the odd part of \(R\).

This is a written consequence of the existing uniform pair-absorption bound and dyadic rotation. The equal-clock and equal-grade conclusion refers to native endpoints on the stated ordinary inputs.

## Why the progression remains uniform at high ternary precision

The two adjacent peaks \(L=P_{r-1}\) and \(U=P_r\) satisfy \(U=3L+2\). The canonical affine pair process from PR146, at initial level 1 and offset 2, leaves at most \(C2^g/\sqrt g\) residue classes of \(L\bmod 2^g\) unabsorbed by clock \(g\). Absorption identifies both affine slopes and affine endpoints at a common native clock. Therefore \(Q_g(L)=Q_g(U)+1\), and equality persists through the specified clock \(g\). The initial pair may also be read as the two children \(T(2L)=L\) and \(T(2L+1)=U\).

As \(r=H-a\) varies through the arithmetic progression with fixed \(a\), its corresponding \(L+1=3^{r-1}v\) is multiplied by \(3^R\) at each index. Now \(v_2(3^R-1)=3\). Repeated squaring gives \(v_2((3^R)^{2^l}-1)=3+l\). Thus modulo \(2^g\) this multiplier has order \(2^{g-3}\) and generates all units equal to 1 modulo 8. One full period of the index visits every \(L\) in one fixed mod-8 class exactly once. Every interval of \(N\) indices is covered by two complete periods, including intervals cut down by the floor \(H\ge J+1\). The pair failure bound is consequently at most \(2C2^g/\sqrt g=O(N/\sqrt{\log(2N)})\) on each link. The union bound over \(J\) links proves the claim. No independence between different links is assumed.

If \(v\) is prime to 3, \(s\in\{0,1\}\), and \(K\ge1\), the condition \(2^Hv-1\equiv s\bmod 3^K\) selects exactly one exponent class of difference \(2\cdot3^{K-1}\), since 2 generates the units modulo \(3^K\). It therefore falls under the same bound with a constant **uniform in \(K\)**.

## Grade savings and return in the original source

Write \(n=2^Hv-1\), \(f=Q_g(P_H)\) and choose \(1\le a\le J\). Given \(d\ge0\) with \(3^d<2^{a+d}\) and \(p=H-a-d\ge1\), the explicit source

\[
           m=2^p3^dv-1<n
\]

takes \(p\) ordinary odd departures to \(P_{H-a}\). It reaches the endpoint of the original \(n\) at clock \(p+g\), using exactly \(H+f-d\) odds. Taking \(d=0\) reduces shifted height by an exact factor \(2^a\). Taking \(a=d=1\) gives \(m=3(n+1)/4-1\) with one odd departure saved. The entire simultaneous family trades the size reduction against odd-step cost. A convergence conclusion at \(n\) requires convergence of a smaller partner, as in ordinary strong induction.

For the specific original source \(m=11+162j\), \(v=1\), \(81z+271=128\cdot2^m\) in PR201, take \(J=5\). The difference 162 has exactly one factor of 2. For all but \(O(N/\sqrt{\log(2N)})\) indices in every \(N\)-index interval, there is therefore an actual same-clock merger from \(P_m\) to \(P_{m-5}\). Under the two original leastness implications in *A five-exponent cutoff for every original hard parent*, \(2^{m-5}-1\) reaches 1, so \(z\) reaches 1 as well. The two implications require convergence below the forty-bit floor and the canonical reverse implication at smaller canonical queries. The unconditioned result supplies the physical merger. It does not assert those leastness hypotheses at an arbitrary parent. The thin delayed subsequence \(m=12\cdot2^{18k}-1\) is not an arithmetic progression in \(k\).

## Precise dependencies

* PR146, `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/THREE_RAY_UPPER.md`, includes a self-contained derivation of the earlier uniform pair-absorption bound for the canonical process. `WITNESS_TRANSFER.md` uses that bound on another family. `AFFINE_RAYS.md` gives deterministic cylinder steering. `FIXED_POINT_EXIT.md` also applies a density estimate to positive exits of a signed \(-5\) checkpoint. These probability and steering results are prior work.
* PR206, `640bf7e511831a0ffc4f00462f12df81f8a8a619`, `research/clock-itineraries/TowerFrontierRotation.lean` and `TowerFrontier.md`, uses binary tower rotation and gives common endpoints at many consecutive ranks on towers \(3^r w\). Here the sites are \(3^r v-1\), the progression preserves a prescribed ternary depth of the original \(2^H v-1\), and the payoff is an explicit smaller odd source and a specified grade.
* PR201, `d21bac748e705a64b6b57a7996a8ad6282f0bcbf`, `research/six-hour-20261127/coupling/EARLIER_OFFSETS.md` and `EarlierOffsets.lean`, gives the conditional gap-five return for the original canonical parent. Its finite-class proof in `PEAK_RIGIDITY.md` shows why fixed-cofactor density estimates cannot be converted into a pointwise all-exponent claim.
