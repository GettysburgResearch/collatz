# Changing the eventual basins while following the true descent to Gaussian time resolution

Let \(T\) be the positive shortcut map. Write \(m_T(n)=\min_{k\ge0}T^k n\), and let \(\tau(n)\) be the first time at this minimum. Fix \(b\ge2\) and distinct odd integers \(q_0,\ldots,q_{b-1}\ge3\). There exists a map \(U\) of the positive integers with exact even halving, differing from \(T\) only at an odd set of natural density zero, with the following properties.

1. Every orbit enters one of the two-cycles \((q_i,2q_i)\). Each basin has density \(1/b\) and each of its two synchronous phases has density \(1/(2b)\), also relative to every fixed arithmetic progression.
2. Put \(Z(n)=\min\{k\ge0:U^{k+1}n\ne T^{k+1}n\}\). Then \(Z(n)\le\tau(n)\) for **every** positive integer \(n\). For uniform \(n\in[2,X]\),
   \[
                    \frac{\tau(n)-Z(n)}{\sqrt{\log n}}\ \longrightarrow\ 0
                    \quad\text{in probability}.                          \tag{1}
   \]
   The same holds relative to every fixed progression. In particular the complete genuine and modified paths agree, with probability tending to one, through every deadline \(\mu\log n-h(n)\) with \(h(n)/\sqrt{\log n}\to\infty\). Here \(\mu=2/\log(4/3)\).
3. For \(\sigma^2=2(\log3)^2/\log^3(4/3)\), every fixed real \(u\) and every positive integer \(r\), the density of starts with \(m_T(n)=r\) and \(Z(n)\le\mu\log n+u\sigma\sqrt{\log n}\) is \(p_r\Phi(u)\), where \(p_r\) is the genuine minimum law. For independent uniform starts the eventual equal-date collision probability under \(U\) tends to \((2b)^{1-k}\) for \(k\) samples.

The [fixed-affine construction](DENSITY_ZERO_BRANCH_PERTURBATIONS.md) preserves all fixed dilation phase equations. Here we require resonance only with the two actual shortcut multipliers, control the trajectories simultaneously up to a random physical deadline, and use the true minimum in the definition of the modified map. The construction makes no computability claim about deciding that minimum. The input on the genuine map is Leen's preprint *Brownian motion in Collatz orbits*, Main Theorem, Corollary «Time to the minimum», Proposition «Height processes», and the proper minimum law. These results concern the unmodified map. [Original preprint](https://doi.org/10.5281/zenodo.23269488)

## Integer frequencies and a slowly changing partition

Write \(\gamma=\log_2 3\). We need integers \(Q_j\to\infty\), each \(1\bmod 2b\), with \(Q'=Q_{j+1}=Q_j d,\ d\equiv1\bmod 2b\). After discarding finitely many indices they satisfy
\[
 Q_j^{j^2}\le Q'\le Q_j^{5j^2},\qquad
 \operatorname{dist}(Q'\gamma,2\mathbb Z)\le (Q')^{-1/6}.                \tag{2}
\]
For completeness, finiteness of approximants of exponent four to \(\gamma\) gives \(\|n\gamma\|\gg n^{-3}\) for all \(n\ge1\). This weak bound follows, for example, from the [audited log-ratio theorem](CHUDNOVSKY_LOGARITHM_IMPORT.md). Here \(\|\cdot\|\) is distance to an integer. For \(\alpha=bQ_j\gamma\), consecutive convergent denominators \(v,w\) obey \(w\ll_b (Q_jv)^3\) by \(\|v\alpha\|<1/w\). The first convergent denominator \(w\ge Q_j^{j^2}\) therefore has \(w\ll_b Q_j^{3j^2+3}\). The \(w\) iterates of \(\alpha\) beginning at \(w\alpha\) land within \(O(1/w)\) of every point of the circle: compare the first \(w\) translates to the grid of the reduced approximant with denominator \(w\), then translate the grid. Pick \(w\le k<2w\) with \(\|Q_j\gamma/2+k\alpha\|\ll1/w\), and put \(Q'=Q_j(1+2bk)\). These inequalities give (2) for large \(j\). We can start at a sufficiently large index with an arbitrary \(Q_j\equiv1\bmod2b\); the first finitely many frequencies are immaterial.

Use the partition \(L_Q(u)=\lfloor bQu\rfloor\bmod 2b\). Let \(G_{j,s}\) equal \(L_{Q'}\) where \(\{bQ_j u\}<s\), and \(L_{Q_j}\) elsewhere. The two floor functions and the selector give at most \(O_b(Q'+1)\) interval boundaries per unit interval. Translation by \(1/(bQ_j)\) adds one to both labels and keeps the selector, so every label occupies equal length in each period \(2/Q_j\). Translation by one adds \(b\). In particular the labels are unchanged by even integer translation of \(u\).

Set \(B_j=Q_{j-1}^{1/1000}\). The gaps \(\log\log B_{j+1}-\log\log B_j\) tend to infinity by (2). At scale \(B_j\le l\le B_{j+1}\) use \(G_l=G_{j,s(l)}\), where \(s\) interpolates linearly from zero to one in \(\log\log l\). At earlier scales use any initial pure pattern, so small nonnegative \(l\) are defined. At a common endpoint both definitions are the same pure pattern. Define
\[
 F(n)=G_{\lfloor\log_2\operatorname{oddpart}(n)\rfloor}(\log_2 n).
\]
Then \(F(2n)=F(n)+b\) exactly.

We give the uniform estimate needed for an entire path. Fix \(a>0,A>1\). On the source shell \(2^J\le n<2^{J+1}\), consider scales
\[
                         a\sqrt J\le l\le AJ.                             \tag{3}
\]
The \(\log\log\) length of this interval stays bounded. It meets at most two neighboring transition intervals for large \(J\). If it meets one, the total range of \(s\) there is \(o(1)\). If it meets two, the two parameters are uniformly \(o(1)\) from the common pure-pattern endpoints. For every frequency \(Q\) in these one or two transitions we have, uniformly,
\[
       J\,\operatorname{dist}(Q\gamma,2\mathbb Z)=o(1),\qquad
                              \log Q=o(\sqrt J).                          \tag{4}
\]
Indeed for a participating transition \(i\), \(B_i\le AJ\) and \(B_{i+1}\ge a\sqrt J\). Thus \(J\le a^{-2}Q_i^{2/1000}\) and \(J\ge A^{-1}Q_{i-1}^{1/1000}\). The first inequality and (2) control the two frequency errors, and \(\log Q_{i+1}\le 25 i^4\log Q_{i-1}\) for large \(i\) proves the other bound. Changing the absolute constant in the latter estimate has no effect.

For fixed \(c>0,C>0\), outside \(o(2^J)\) starts on the shell, the following statement holds for **all** \(l,l'\) in (3), all integers \(0\le g,k\le CJ\), and all \(|e|\le CJ\,2^{-c\sqrt J}\):
\[
                   G_{l'}(\log_2 n+g\gamma-k+e)
                         =G_l(\log_2 n)-bk \pmod{2b}.                    \tag{5}
\]
For each participating \(Q\), (4) shows that the distance of \(bQ(g\gamma+e)\) to \(2b\mathbb Z\) is \(o(1)\), uniformly in all variables. Remove from the initial angles \(\{bQ\log_2 n\}\) a strip of this width at the floor discontinuity. For a single transition also remove the selector's entire parameter range thickened by this width. For two transitions remove the corresponding small strips at zero or one for each selector; the chosen pattern is then the common pure pattern at both scales. There are at most three frequencies. On a logarithmic shell of length one, each strip of width \(o(1)\) occupies length \(o(1)+O(1/Q)\) and has \(O_b(Q)\) components. Counting integer points after exponentiating multiplies length by at most \(O(2^J)\) and adds \(O_b(Q)\). This proves (5) including arbitrary partial shells with the full-shell error. No union over the elapsed dates is needed.

The same counting shows that \(F\) is balanced, also on every fixed arithmetic progression. For all but \(O(2^{J-V}+1)\) starts on a shell, the actual scale differs from \(J\) by at most \(V\). Apply (5) at \(g=k=e=0\) and then let \(V\to\infty\). The comparison pattern \(G_J\) is periodic with length tending to zero and balanced on each period. The smooth exponential sampling weight on a log shell and the uniform \(O_b(Q_{i+1}+1)\) interval count therefore give label frequencies \(1/(2b)+o(1)\) on full or partial shells (absolute error relative to \(2^J\)); the same grid counting with fixed integer spacing gives the progression version. Summing dyadic shells yields the assertions at all cutoffs. Finally assign \(F(2^v q_i)=i+bv\bmod2b\) on the specified rays. These \(O(\log X)\) exceptions preserve densities and exact doubling.

## The actual first discrepancy and the terminal height window

Let \(S=\{r:m_T(r)=r\}\). Every member is odd, and \(S\) has natural density zero: for each \(K\), all its members above \(K\) have \(m_T(r)>K\), whose limiting upper density tends to zero by the proper minimum law. The first visit of any true orbit to \(S\) occurs at time \(\tau\). A prior visit would have a smaller future state at time \(\tau\).

For each label \(f\), let \(b_f\) denote the vertex of the designated cycles with that label. Use exact even halving and set \(U(q_i)=2q_i\). At other odd inputs outside \(S\) keep \(T(n)\) when \(F(T(n))=F(n)-b\), and otherwise redirect to \(b_{F(n)-b}\). At all other inputs in \(S\) redirect to either \(b_{F(n)-b}\) or \(4b_{F(n)-b}\), choosing an output different from \(T(n)\). Both choices follow exact halving or the designated cycle to the same target; in particular \(4b_f\) is even and has label \(f\). At each designated odd input the new branch differs from the true one because \(q_i\ne1\). Every first discrepancy now leads into a designated cycle in at most two further steps, and it occurs by \(\tau\) for every start. All labels advance by \(-b\) at every date. This proves the claimed component and phase structure. The next estimate implies directly that the odd branch-discrepancy set has density zero (it is \(\{Z=0\}\), and \(\tau/\log n\to\mu\) in probability).

For \(L=\log n,\ y_k=T^k n\), write \(H(k)=\log y_k-L+k/\mu\) through \(\tau\). Leen's height-process proposition gives
\[
 \tau=\mu L+O_P(\sqrt L),\quad \sup_{k\le\tau}|H(k)|=O_P(\sqrt L),\quad
 \sup_{|k-j|\le D\sqrt L,\;j,k\le\tau}|H(k)-H(j)|=o_P(\sqrt L)         \tag{6}
\]
for each fixed \(D\): the rescaled processes on \(k/\tau\in[0,1]\) converge to a continuous Brownian path. If \(v=v_2(y_k)\) then \(k+v\le\tau\) for \(k\le\tau\), since halving strictly decreases until the odd part and the global minimum is odd. Hence
\[
             H(k+v)-H(k)=-(\log2-1/\mu)v .
\]
The supremum bound in (6) first gives \(\max v=O_P(\sqrt L)\); its modulus bound then gives \(\max v=o_P(\sqrt L)\).

Fix \(\varepsilon>0\). Uniformly for \(0\le k\le\tau-\varepsilon\sqrt L\), with probability tending to one,
\[
    \log\operatorname{oddpart}(y_k)\ \ge\ \varepsilon\sqrt L/(3\mu),
                  \qquad \log y_k\le 2L,\quad k\le 2\mu L .              \tag{7}
\]
For the lower bound use \(\log y_k=\log m_T(n)+(\tau-k)/\mu+H(k)-H(\tau)\), with the nonnegative first term. On \(\tau-k\le D\sqrt L\) the error is \(o_P(\sqrt L)\). Beyond that window, choose \(D\) large against a tightness bound for \(2\sup|H|/\sqrt L\). The failure probability can be made arbitrarily small by first choosing that bound, then \(D\), and finally taking \(X\to\infty\). Subtract \((\log2)\max v=o_P(\sqrt L)\). The other two assertions follow directly from (6).

Through this window the log-affine expression is
\[
      \log_2 y_k=\log_2 n+g_k\gamma-k+e_k,\qquad
      0\le e_k=\sum_{\substack{j<k\\y_j\ {\rm odd}}}
                 \log_2(1+1/(3y_j))\ll_\varepsilon L\,2^{-c_\varepsilon\sqrt L}
\]
for some \(c_\varepsilon>0\). All scale indices of the \(y_k\) satisfy (3) on their **initial** shell \(J=\lfloor\log_2 n\rfloor\). None of these points is on a designated ray for large \(n\), by the lower bound on its odd part. Apply (5), which holds simultaneously even when \(g_k\) and the subsequent scales depend on \(n\). Summation of its shell errors gives a density-one event. Therefore \(F(y_k)=F(n)-bk\) for all the indicated dates. Before the minimum none lies in \(S\), so all genuine steps with both endpoints in this window are retained. In particular \(Z\ge\lfloor\tau-\varepsilon\sqrt L\rfloor\) except with probability tending to zero. Together with the pointwise opposite bound this proves (1). Density-zero exceptions remain null on any fixed progression. The true minimum-clock law and Slutsky's theorem give the joint Gaussian statement, without an independence assumption about the artificial phases and the clock.
