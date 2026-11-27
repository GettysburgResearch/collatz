# Pointwise asymptotics for the sizes of actual corrected-height fibres

**Status.** Source-qualified written theorem. This note strengthens the
backward total-variation law in [the marked-fibre theorem](MARKED_FIBRES.md)
to a local limit. The inputs are that note's exact marked source, its
rapid physical tail estimate, and the two-sided grade profile. The
conclusion concerns ordinary positive integers in a single hypothetical
escaping component and holds uniformly across its occupied and empty
corrected-height cells. It gives a quantitative multiplicity required
by escape.

Use the notation of the marked-fibre theorem. Fix a base site in an
escaping component \(C\), with height \(P_0\), signed grade \(v\), lattice
coordinate \(l\), and \(p=P_0 3^v2^l\).
Let \(N_C(v,l)=\#\{x\in C:P(x)=p\}\), so \(m_v(l)=N_C(v,l)/p\).
Define \(g_n(t)=0\) for \(n<0\), \(g_0=\delta_0\), and
\(g_n(t)=\binom{t-1}{n-1}2^{-t}{\bf1}_{t\ge n}\) for \(n\ge1\).
Then
\[
 \sup_{\substack{v,l\in\mathbb Z\\P_0 3^v2^l\ge R}}
 \sqrt{\log(P_0 3^v2^l)}
 \left|\frac{N_C(v,l)}{P_0 3^v2^l}-H_C g_{-v}(l)\right|
                 \longrightarrow 0 \quad (R\to\infty).                 \tag{1}
\]
There is also an absolute constant, independent of the choice of
component or base point, for the one-sided estimate
\[
                  N_C(v,l)\ll p/\sqrt{1+\log p}\qquad(p\ge1).          \tag{2}
\]
In particular every escaping component, at *every sufficiently large*
\(n\), has
\[
 \#\{x\in C:P(x)=P_0(4/3)^n\}
            \sim \frac{H_C P_0(4/3)^n}{\sqrt{4\pi n}}.                 \tag{3}
\]
Bounds (1)–(3) refer to exact equalities of real corrected heights.
Members of a single cell eventually merge at one ordinary odd state
with both their odd-step counts and their native division counts equal.

## The signed forcing and its height tail

In the recurrence (8) of the preceding note, put \(c_u=b_{u+1}\),
regarding \(c_u(l)\) as sitting at \(p=P_0 3^u2^l\). Then, across all
components and all these cells,
\[
 \sum_{C,u,l}|c_u(l)|<\infty,\qquad
 \sum_{C,u,l:\,P_0 3^u2^l\ge L}|c_u(l)|\ll_A(1+\log L)^{-A}
 \quad(L\ge2).                                                         \tag{4}
\]
Indeed \(c\) is the sum over \(e\ge1\) of \(3\,2^{-e}\) times the
signed starting-residue errors \(m_{u+1,r_e}-m_{u+1}/3\),
at a height \(p'=3p2^{-e}\). Those errors already have the asserted
tail (6) in the preceding note. When \(p\ge L,\ p'<\sqrt L\) one
needs \(2^e>3\sqrt L\), whose geometric weights sum to \(O(L^{-1/2})\).
Every term is supported above \(p\ge2/3\), since \(p'\ge1\) at an
occupied actual target. Signed forcing may also occur at an empty cell.

The future grade masses tend to zero. Iterating
\(m_v=G*m_{v+1}+c_v\) to the future and taking its sum-norm limit gives
the absolutely convergent representation at each grade
\[
 m_v(l)=\sum_{u\ge v}\sum_{l_0\in\mathbb Z}
                      c_u(l_0)g_{u-v}(l-l_0),\qquad
                   \sum_{u,l_0}c_u(l_0)=H_C.                          \tag{5}
\]
For the last equality sum
\(\sum_l c_u(l)=Z_{C,u}-Z_{C,u+1}\) between finite limits, and use both
grade limits. Distinct starting components never mix in (5).

## Point bounds for the original clock

Write \(\alpha=\log_2 3\). A source atom of height
\(p_0=P_0 3^u2^{l_0}\) contributes to height \(p\) after
\(j=u-v\ge0\) steps only at \(t=l-l_0\), with
\(\log_2(p/p_0)=t-\alpha j\). Thus
\[
 \sup_{\substack{j\ge0,\ t\in\mathbb Z\\t-\alpha j\ge L}}
                 g_j(t)\ll(1+L)^{-1/2}\quad(L\ge1).                   \tag{6}
\]
For \(j\ge L/10\) the ordinary unimodal bound
\(\|g_j\|_\infty\ll j^{-1/2}\) suffices. For \(j<L/10\), use
\(\Pr(E_j\ge t)\le 3^j(2/3)^t\le 3^{L/10}(2/3)^L\).
In (5) the sources \(p_0<\sqrt p\) therefore have kernels
\(O((1+\log p)^{-1/2})\), while the remaining source mass is bounded
by (4). This proves (2).

For fixed integers \(u,l_0\), the two kernels from height
\(p_0=P_0 3^u2^{l_0}\) and from \(P_0\) satisfy
\[
 \sup_{\substack{v,l\\p\ge R}}\sqrt{\log p}
       |g_{u-v}(l-l_0)-g_{-v}(l)|\ \longrightarrow 0.                 \tag{7}
\]
To verify the smoothing required here, the geometric characteristic
function is \(\phi(\theta)=e^{i\theta}/(2-e^{i\theta})\), with
\(|\phi(\theta)|=(5-4\cos\theta)^{-1/2}\le e^{-c\theta^2}\) on
\([-\pi,\pi]\). Fourier inversion with one difference therefore gives
\(\sup_t|g_n(t+1)-g_n(t)|\ll n^{-1}\).
A fixed change of lag uses convolution with a fixed \(g_d\) of finite
first moment, so \(\sup_t|g_{n+u}(t-l_0)-g_n(t)|=O_{u,l_0}(n^{-1})\)
for \(n\) large. For \(n=-v\ge (\log_2 p)/20\) this proves (7).
For smaller nonnegative \(n\), and for the finitely shifted nonnegative
lag \(n+u\) when it exists, \(t-\alpha j=\log_2(p/p_0)\) is large
while \(j<(\log_2 p)/20+O_u(1)\). The geometric moment bound used
in (6) is exponentially small. Negative lags have kernel zero.

Finally keep finitely many terms of \(c\) with remainder signed
sum-norm below \(\varepsilon\). Use (7) termwise on the kept part.
Among omitted source atoms at \(p_0<\sqrt p\) use (6), giving at most
\(O(\varepsilon/\sqrt{\log p})\); at \(p_0\ge\sqrt p\) use (4).
The corresponding omitted scalar multiplying \(g_{-v}(l)\) is at most
\(\varepsilon\) in absolute value, and (6) applied to the fixed \(P_0\)
bounds this kernel by \(O(1/\sqrt{\log p})\) for all sufficiently
large \(p\). Let \(\varepsilon\downarrow0\) to obtain (1).
At \(v=-n,l=2n\), use \(\log p=\log P_0+n\log(4/3)\) and the
central binomial asymptotic
\(\binom{2n-1}{n-1}2^{-2n}\sim(4\pi n)^{-1/2}\) to prove (3).

An escape proof by this route would follow if, for each hypothetical
escaping component with some fixed ordinary base, one could establish
\(N_C(-n,2n)=o(P_0(4/3)^n/\sqrt n)\) on a subsequence. The source
mixing used above supplies exactly the leading term in (3), and gives
no such saving. Uniform compression for **one trajectory** bounds visits
to a translated physical interval. The inputs in (3) belong to different
trajectories before their eventual merger, so that compression cannot
be used to upper-bound this multiplicity.
