# A fixed ordinary source and the linear profile of an almost invariant word

**PROPOSED written results.** The finite rotation estimate applies directly to the discrepancy of any finite word. It removes the high-phase assumption from the irrational-lag denominator bound. On a prefix of a single nonrepeating ordinary orbit it controls the deviation of log height from the line between the two *actual* endpoints. Macroscopic repetitions then force exponential endpoint growth at that same fixed source. In a specified initial-overlap case, every low-cost ternary anchor required by PR206 at the matched depth is provably absent. There is still no theorem forcing a suitable comparison on an arbitrary escaping orbit.

## The symbolic estimate

Let \(e_0,\ldots,e_{N-1}\ge1\) be any finite word. Extend the word periodically only to calculate its cyclic windows. This convention makes no dynamical assertion about the trajectory. Set \(E_i=\sum_{j<i}e_j,\ A=E_N,\ \theta=A/N,\ c=v/N\) for \(1\le v<N\). If \(B_i=E_{i+v}-E_i\) differs from an attained integer \(u\) at m indices modulo N, then define
\[
 F(i/N)=(i\theta-E_i)/N,\qquad
 W=\max_{0\le i<N}(i\theta-E_i)-\min_{0\le i<N}(i\theta-E_i).
\]
The linear, periodic interpolation of F has forward slope at most \(b=\theta-1\) and full oscillation \(W/N\le b\). Its lag change is \((v\theta-B_i)/N\). Since \(|v\theta-u|\le\theta m\), at good vertices this change is at most \(\theta m/N\) in absolute value. At bad vertices it is at most b. With \(G_K(c)\) as in the finite circle estimate (P7), its proof applied after a rotation to the minimum of F gives
\[
 \frac{W}{N}\le b(G_K(c)+r)+\frac{K(2\theta-1)m}{N r}
 \qquad(K\ge1,\ 0<r\le1).                                  \tag{F1}
\]
In particular, if \(m=o(N)\), \(\theta\to\theta_0<\infty\), and \(v/N\to c_0\), then
\[
 \limsup W/N\le(\theta_0-1)/q,
 \qquad
 q=\begin{cases}
 \text{reduced denominator of }c_0,&c_0\in\mathbb Q,\\
 \infty,&c_0\notin\mathbb Q .
 \end{cases}                                                  \tag{F2}
\]
Endpoint limits 0 and 1 have q=1. Here and below the reciprocal of infinity is zero. The concentration on an irrational lag works with no hypothesis that the exceptional indices themselves cluster. For every odd-time arc of length \(k=o(N)\), its native duration is at most \(\theta k+W=o(N)\) in that sector. This follows from the exact definition of F.

For a cyclic word with \(D=2^A-3^N>0,\ \theta\le L\), let d be its full reduced cycle denominator and h the largest cyclic spacing in the nonempty exception set. The companion toric-window manuscript's elementary inequality (9) is
\[
 \log_2 d\ge\theta h-W-|u-v\theta|-O_L(\log(2N)).
\]
Its proof uses the nonzero odd residual of Paper 22, a signed size estimate and two fixed logarithms; it imposes no restriction on the raw defect count. Combining with (F1) gives the entirely symbolic implication
\[
 \liminf\left(\frac{\log d}{\log D}-\frac hN\right)
 \ \ge -\frac{1-1/\theta_0}{q}                               \tag{F3}
\]
under the hypotheses of (F2). In particular the largest-gap fraction holds for every positive rational cycle at an irrational limiting lag with \(m=o(N)\), irrespective of its real phase heights. The estimate uses \(\log_2 D=A-O_L(\log(2N))\). [Weaver, Mahler and Wren, Paper 22 v4](https://rstation.ai/problems/collatz/papers/22/v4) · [Matveev](https://doi.org/10.1070/IM2000v064n06ABEH000314)

## Actual initial words from one ordinary source

Fix an ordinary positive odd integer \(x_0\) and suppose its accelerated orbit \(2^{e_i}x_{i+1}=3x_i+1\) never repeats. On the prefix through its actual state \(x_N\), put
\[
 L_i=\log_2 x_i,\quad S_i=\sum_{j<i}\log_2(1+1/(3x_j)),
 \quad\gamma_N=(L_N-L_0)/N .
\]
All sites are distinct positive odd integers, so \(0\le S_i\le S_N=O(\log(2N))\). Positivity and the one-step growth of \(x_i+1\) imply \(-O_{x_0}(1/N)\le\gamma_N\le\kappa+O_{x_0}(1/N)\), with \(\kappa=\log_2(3/2)\). Summing the recurrences gives exactly
\[
 A/N=\lambda-\gamma_N+S_N/N,\qquad
 L_i-L_0-i\gamma_N=NF(i/N)+S_i-(i/N)S_N,
 \quad \lambda=\log_2 3.                                    \tag{F4}
\]
In particular the native clock average of these prefixes is bounded uniformly, and \(F(0)=0\). If there are infinitely many prefixes with cyclic comparison count \(m_N=o(N)\) at \(v_N/N\to c_0\notin\mathbb Q\), then (F2), taking convergent subsequences of the bounded clock average as needed, gives
\[
 \max_{0\le i\le N}|L_i-L_0-i\gamma_N|=o(N).                 \tag{F5}
\]
The points on this line are the real log heights of the original trajectory up to the displayed error. The endpoint slope may vary with N.

Suppose in addition two genuine portions starting at \(0\le i<j\le N-H\) have H identical clocks, with \(H\ge\delta N\) for some fixed \(\delta>0\). Their distinct terminal states differ by a nonzero multiple of \(2\,3^H\). Applying (F5) at the two terminal dates gives
\[
 \gamma_N(j+H)\ge\lambda H-o(N),\qquad
 \liminf\gamma_N\ge\lambda\delta.                            \tag{F6}
\]
This follows also if an initial vanishingly negative \(\gamma_N\) is allowed: its size is \(O_{x_0}(1/N)\). Thus any prefix family with these two properties exhibits positive exponential growth at its actual endpoints and, by (F5), all its interior dates at a fixed positive fraction of N. A macroscopic clean cyclic spacing \(h_N\ge\delta N\) on the prefix suffices with \(\delta/3\) in the last inequality. The \(h_N-2\) identical cyclic edges contain at most two transitions across the artificially identified seam, one for each of the two starting positions. Removing these edges leaves at most three genuine contiguous matches. This deduction never treats the artificially periodic word as an ordinary cycle.

## The ternary anchor at the second terminal

A genuine shared word gives the exact anchor \(x_{j+H}\equiv x_{i+H}\pmod{3^H}\). PR206 proves a gain at a strict record with \(dx_k\equiv A_*\bmod 3^n\) when
\[
 C K^{718}(\lfloor |A_*|/d\rfloor+1+d^{19})\le n .
\]
In particular, a matched terminal that is a strict record at \(k=j+H\), with \(C K^{718}(x_{i+H}+2)\le H\), does inherit its stated record gain from the earlier site by taking \(d=1,\ n=H\). Agreement by itself supplies the precision but does not supply this small height. [PR206, ReturnOrbit at 640bf7e5](https://github.com/GettysburgResearch/collatz/blob/640bf7e511831a0ffc4f00462f12df81f8a8a619/research/clock-itineraries/ReturnOrbit.md)

In the sector of (F5)–(F6), suppose the earlier agreement starts at \(i=o(N)\). Then \(H\ge\delta N\) and
\[
 2^{\lambda\delta^2 N-o(N)}\le x_{i+H}
 \le (x_0+1)(3/2)^{H+o(N)} .
\]
The upper bound is exponentially smaller than \(3^H\). Therefore, for all sufficiently large such N, **there is no** integer \(d\) or signed integer \(A_*\) with
\[
 1\le d\le H^{1/19},\quad |A_*|\le dH,\quad
 d x_{j+H}\equiv A_*\pmod{3^H}.                              \tag{F7}
\]
Indeed \(0<d x_{i+H}-A_*<3^H\) throughout this whole range. The argument covers all representatives of the ternary residue and every denominator in the displayed range. It concerns the specific matched depth H. Less precise anchors, another record, or an independently constructed approximation could satisfy a different input. The same macroscopic matched word has coefficient gain \(2^{\gamma_N H+o(N)}\) under (F5), by (F4), so it does not itself supply a bounded two-sided coefficient strip.

No result here forces \(m_N=o(N)\), irrational normalized lag, an extensive genuine common word, or small endpoint growth on the same prefixes of an arbitrary divergent source. Paper 15 v2 gives lower bounds on the cost of a charged periodic dictionary for an ordinary path; those lower bounds do not furnish a low-defect lag. The positive rational dense-defect family in the cycle packet shows that clock means and high phases alone cannot furnish it. It does not disprove any statement that uses the ordinary nature of one fixed source. [Weaver, Paper 15 v2](https://rstation.ai/problems/collatz/papers/15/v2)
