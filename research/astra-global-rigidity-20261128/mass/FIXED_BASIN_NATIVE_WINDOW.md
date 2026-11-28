# Natural-source clock fluctuations at one fixed ordinary target

**Source-qualified written deduction.** Let \(a\) be a fixed positive odd integer prime to three, \(B_a\) its actual shortcut predecessor set, and \(\tau=\tau_a(n)\) the first shortcut visit from \(n\) to \(a\). Write \(Q_j(n)\) for the number of odd departures through \(j\) shortcut steps. Put
\[
 D=\log(4/3),\quad \mu=2/D,\quad
 \sigma^2=2(\log3)^2/D^3,\quad \beta=D/(2\log3).
\]
Condition a uniform \(1\le n\le X\) on \(n\in B_a\). Then
\[
 H_X=(\tau-\mu\log X)/\sqrt{\log X}\ \Rightarrow\ N(0,\sigma^2).
                                                                    \tag{1}
\]
For every deterministic \(v_X=o(\log X)\), \(v_X\ge0\), one also has
\[
 \frac1{\sqrt{\log X}}\sup_{0\le r\le\min(\tau,v_X)}
 \left|Q_\tau(n)-Q_{\tau-r}(n)-r/2\right|
      \ \longrightarrow\ 0\qquad\text{in probability},               \tag{2}
\]
with integer \(r\). The statement monitors the final segment before this first ordinary hit. It makes no assertion about the subsequent orbit of \(a\).

The Gaussian in (1) is prior. David Leen's *Brownian motion in Collatz orbits*, v1, §1.3 “Every target” gives the fixed-target timed limit, reproduced with precisely this normalization as Weaver 179/v1, (A.8). The primary Leen file was unavailable in this pass. The following derivation uses the frozen PR213 kernel, first-arrival bridge and mark instead. In particular it does not assume a freely sampled continuation after a physical source arrives. [Leen, v1 DOI](https://doi.org/10.5281/zenodo.23252395) · [Weaver, exact statement (A.8)](https://rstation.ai/problems/collatz/papers/179/v1)

## Original row inputs

First restrict to positive odd starts and use the odd map \(U(x)=(3x+1)/2^{v_2(3x+1)}\). For grade \(j\) and native clock \(s\) at a first visit to \(a\), put \(p=a2^s/3^j\), and let \(m_{j,s}\) be the row count divided by \(p\). The frozen first-arrival source proves:

1. Every member \(x\) of this row has \(c_0p\le x\le p\) for an absolute \(c_0>0\).
2. \(m_{j,s}=\sum_{i,t}c_{i,t}g_{j-i}(s-t)\), with \(\sum_{i,t}|c_{i,t}|<\infty\). Here \(g_k(l)=\binom{l-1}{k-1}2^{-l}\) is the sum law of \(k\) independent positive geometric \((1/2)\) gaps, with \(g_0=\delta_0\) and negative grades zero.
3. Uniformly on compact standardized central totals \(z=(s-2j)/\sqrt j\), one has \(m_{j,s}/g_j(s)\to H_a>0\). On the uniform row the ratio \(F=x/p\) converges in law to a common probability \(V_a\) on \([c_0,1]\), independent of \(z\). The linearly interpolated path of centered outward gap totals \((S_{\lfloor jt\rfloor}-2\lfloor jt\rfloor)/\sqrt j\) is tight for \(0\le t\le1\) along all those totals and is zero at zero. These assertions hold on **first visits**, including when \(a\) is periodic. Removing the primitive reverse lap changes the coefficient and the real mark law; the same bridge tightness persists.

For (3), the real mark satisfies \(F=1-\beta_j/a\) for the outward affine offset \(\beta_j\). The frozen bridge theorem includes this offset and the stated first-visit restriction. Uniformity on compact \(z\)-intervals follows subsequentially by compactness of the scalar endpoint. Positivity holds at every fixed odd unit on the supplied trace inputs with a positive first-arrival coefficient. These are written, source-qualified ingredients, including the joint mixing premise (J). [PR213, sharp uniform rows, equations (5)–(7), at 5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/mass/SHARP_UNIFORM_FIRST_ARRIVAL_ROWS.md) · [PR213, pinned root bridge, exact total, real mark and final paragraph on first visits](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/inverse/pinned_root_bridge.md)

## A bounded-height band controls all noncentral rows

Take a fixed logarithmic height width \(w>0\). With independent geometric gaps \(G_i\), write \(Y_k=\sum_{i=1}^k(G_i\log2-\log3)\). The mean increment is \(D>0\). Uniformly in \(A\in\mathbb R\),
\[
 \mathbb E\sum_{k\ge0}{\bf1}_{[A,A+w]}(Y_k)\le C_w.                  \tag{3}
\]
After the first visit, the expected number of future visits is at most \(\sum_{k\ge0}\Pr(Y_k\le w)\), uniformly in the entrance point. This is finite by a small negative exponential moment and positive drift. If \(A\to\infty\), the contribution to (3) from \(|k-A/D|>B\sqrt A\) tends uniformly to zero as \(B\to\infty\) after \(A\to\infty\). For the early tail, a visit forces the centered increment martingale before \(A/D-B\sqrt A\) to rise at least \(DB\sqrt A-O(1)\). Its variance through that date is \(O(A)\). The maximal second-moment inequality bounds the probability by \(O(B^{-2})\), and (3) after first entrance bounds the expected count. For the late tail, at date \(\lceil A/D+B\sqrt A\rceil\) the walk is above \(A+DB\sqrt A/2\) outside probability \(O(B^{-2})\) in the indicated order of limits. A subsequent return to the band has probability exponentially small in \(B\sqrt A\), by the nonnegative exponential supermartingale for negative increments. Charge the expected number of subsequent visits using (3) again.

An original source in a fixed proportional interval \([\alpha X,\gamma X]\), \(0<\alpha<\gamma<\infty\), must have \(p\in[\alpha X,\gamma X/c_0]\). Its count divided by \(X\) is bounded by a constant times its row weight. In a kernel translated by \((i,t)\), this physical crop is precisely a strip in (3) with \(A=\log(\alpha X/p_0)\), \(p_0=a2^t/3^i\) and fixed width. First retain finitely many impulses in the signed representation. Their shifts are fixed, so their off-central counts, with \(|j-\log(X/a)/D|>B\sqrt{\log X}\), tend to zero in the same iterated limit. Equation (3) bounds the full omitted tail by \(C\sum_{\rm omitted}|c_{i,t}|\), independently of the physical heights of the omitted impulses. This justifies keeping only central rows for both (1) and (2).

## Local Gaussian kernel and the actual source variable

Use a nonnegative continuous source weight \(\chi(x/X)\) compactly supported away from zero. Set \(N=\log X\), \(j_*=\log(X/a)/D\), \(\lambda=\log_2 3,\ \gamma_0=2-\lambda\), and \(b=(j-j_*)/\sqrt N\). Within a fixed central cutoff write
\[
 u=\log_2(p/X)=s-\lambda j+\log_2(a/X).
\]
Only a fixed compact \(u\)-interval is needed. Then \(s-2j=-\gamma_0 b\sqrt N+u\), and \((s-\mu N)/\sqrt N=\lambda b+o(1)\) uniformly there. For each grade just \(O(1)\) total clocks occur. The geometric local limit (or Stirling's formula) gives
\[
 g_j(s)=\frac{\sqrt D}{\sqrt N}\left(\phi(-\gamma_0\sqrt D\,b)+o(1)\right),
 \qquad \phi(z)=(4\pi)^{-1/2}e^{-z^2/4}.
\]
Each first-hit row contributes \(2^u m_{j,s}\mathbb E_{\rm row}\chi(2^uF)\) to the count divided by \(X\). Compactness and input (3) from the row list let us replace the expectation by \(\int\chi(2^uf)\,dV_a(f)\), uniformly. This is also valid in the presence of atoms since \(\chi\) is continuous.

Summing these latter test factors over the integer values of \(s\) gives a continuous one-periodic function of the phase \(\log_2(a/X)-\lambda j\). Its mean over a period is \(\int_{\mathbb R}2^u\int\chi(2^uf)\,dV_a(f)\,du\), positive for a nonzero nonnegative \(\chi\). The irrational rotation by \(\lambda\) equidistributes uniformly in its initial phase on consecutive grade intervals of length tending to infinity. This follows by approximating a continuous periodic function by trigonometric polynomials and summing each nonconstant geometric progression. Partition the bounded \(b\)-interval into finitely many short subintervals, then use uniform continuity of the Gaussian and of any bounded continuous test of \(\lambda b\). Each subinterval contains order \(\sqrt N\) grades. Sending the mesh to zero proves that the scalar \(b\) has limiting density proportional to \(\phi(-\gamma_0\sqrt D\, b)\), independently of the smooth physical source weight. The off-central estimate supplies its full normalization. Consequently \(\lambda b\) has variance \(2\lambda^2/(\gamma_0^2D)=\sigma^2\).

Continuous upper and lower approximations to a proportional source interval lose no more than the unconditional fraction of sources in its endpoint strips. A fixed small initial interval \([1,\epsilon X]\) costs at most \(\epsilon\); let \(\epsilon\downarrow0\) after the limit. This gives (1) for all odd positive starts under their natural counting law, with positive basin mass. For all positive starts write \(n=2^e x\) with \(x\) odd. At fixed \(e\), losing \(e\) initial halvings and replacing \(X\) by \(X/2^e\) changes the centered normalized clock by \(o(1)\). All \(e\) above \(E\) cost at most \(2^{-E}\) of all starts. The mixture gives the same conditional law and a positive natural basin density on all starts. The physical source distribution has thus been retained throughout.

## The last portion before a true hit

In central rows from a fixed proportional source interval, \(j\asymp\log X\). For any deterministic \(v_X=o(\log X)\), bridge tightness at the outward origin implies
\[
 \max_{d\le v_X+1}|S_d-2d|=o_{\mathbb P}(\sqrt j)
\]
under the full uniform row, uniformly for its central clock range. To see uniformity, a violating sequence has a subsequence with convergent standardized terminal total, to which the continuous-path tightness and value zero at time zero apply. A crop or a source weight can only *decrease the absolute exceptional count*. Each full central row has at most \(O(X/\sqrt{\log X})\) sources in this physical range of \(p\), and there are \(O_B(\sqrt{\log X})\) such cells. Thus the exceptional count divided by \(X\) tends to zero, then the previous tail estimate removes the central cutoff.

For the final \(r\) shortcuts before the first hit, the number \(d\) of odd departures is the number of complete outward gaps in those \(r\) steps. Thus \(S_d\le r<S_{d+1}\) if \(d<j\), and \(d\le r\). The distance from \(r\) to \(2d\) is at most \(2+\max_{i\le r+1}|S_i-2i|\). Here \(r\le v_X<j\) on the central range for large \(X\). This proves (2) for odds. The fixed initial halving segment for general \(n\) is outside these final \(o(\log X)\) steps on central rows; truncate its length and remove the tail just as above. The uniform conclusion in (2) permits a random \(r=o_{\mathbb P}(\log X)\) as well, by bounding it in probability by some deterministic \(v_X=o(\log X)\).
