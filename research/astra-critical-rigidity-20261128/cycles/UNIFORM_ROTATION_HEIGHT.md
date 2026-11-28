# Typical paired heights and arbitrary growing mismatch counts

Let \(p\) be the primitive odd period of a positive rational cycle, \(q\) its complete reduced denominator, and \(y_i/q\) its odd phases. Write
\[
 Z_i=\log_2(y_i+q),\qquad \bar Z=p^{-1}\sum_i Z_i,\qquad
 s_\ell=\#\{i:e_i\ne e_{i+\ell}\}\quad(0<\ell<p).
\]
On growing **ordinary integer** cycles, uniformly over proper lags, for every fixed \(K>0\),
\[
 \sup_{0<\ell<p}\frac1p\#\{i: Z_i+Z_{i+\ell}\le Kp/s_\ell\}
           \longrightarrow 0,\qquad
 \min_{0<\ell<p}\frac{s_\ell\bar Z}{p}\longrightarrow\infty.            \tag{1}
\]
This samples all true odd dates. Concentrating extreme heights at the mismatch boundaries cannot by itself satisfy (1).

The first assertion also holds along any sequence of proper lags of positive rational cycles with \(s=s_\ell=o(p)\) and \(s\log_2 q=o(p)\). Under the same hypotheses, or on the unrestricted ordinary cycles, the rotation order \(M=p/\gcd(p,\ell)\) determines a single-state consequence. For any fixed \(K>0\) and any fixed \(2\le J\le M\) eventually,
\[
       \limsup\frac1p\#\{i:Z_i\le Kp/s_\ell\}\le\frac1J.                \tag{2}
\]
Thus for orders tending to infinity the proportion on the left tends to zero. At each fixed order \(M\), all but \(o(p/M)\) of the rotation fibers contain at most one such low state. At denominator one, this includes every polynomial cutoff whenever \(s_\ell\log p=O(p)\).

A complementary **complete-denominator** bound uses only the mean, with no restriction on the locations or heights of the mismatches. Along any sequence of primitive positive rational cycles and proper lags with \(s_\ell\bar Z=O(p)\),
\[
                       \liminf\frac{s_\ell\log_2 q}{p}\ge\frac14.        \tag{3}
\]
The [event-height theorem](MISMATCH_EVENT_HEIGHT.md) gives the same coefficient when \(s_\ell=o(p)\) and the total post-mismatch height is \(O(p)\). In (3) the supplied bound concerns every date at its uniform spatial weight. Either sum may concentrate differently in an application. The period onsets are ineffective.

## All origins of a fixed chronological length

Write \(s=s_\ell,\ \gamma=\log_2 3,\ \beta=\gamma-1\). At time \(i\) the pair consists of \(y_i,y_{i+\ell}\); \(H_i,h_i\) are respectively the maximum and minimum of their two \(Z\)'s. Since \(e_i\ge1\),
\[
                     y_{i+1}+q\le\tfrac32(y_i+q).
\]
Consequently \(h_{i+L}\le h_i+\beta L\). The exact open-arc theorem says that for each fixed nonnegative integer \(m\) and \(0<\epsilon<1\), there is \(C(m,\epsilon)\) such that every \(L\)-step paired arc at this lag with at most \(m\) unequal exponents satisfies
\[
              (1-\epsilon)L\le H_i+h_{i+L}+4(m+1)\log_2q+C(m,\epsilon).
                                                                            \tag{4}
\]
The two tracks remain distinct at every recorded date by primitivity and the proper rotation, even for arcs longer than one lap. [Exact endpoint theorem, (1)–(3)](../ordinary/EXACT_ARC_ENDPOINTS.md)

For a given integer \(L\ge1\), denote the number of mismatches in the \(L\) steps starting at \(i\) by \(m_i(L)\). The identity \(\sum_{i\bmod p}m_i(L)=Ls\) holds with multiplicity if \(L>p\). Hence at most \(Ls/(m+1)\) starts have more than \(m\) mismatches. On every other start (4) gives
\[
       Z_i+Z_{i+\ell}\ge (1-\beta-\epsilon)L-4(m+1)\log_2q-C(m,\epsilon).
                                                                            \tag{5}
\]
Always \(1-\beta=2-\log_2 3>0\). Given \(K\), choose \(\epsilon\in(0,1-\beta)\) and fix \(D>K/(1-\beta-\epsilon)\). Put \(L=\lceil Dp/s\rceil\). If \(s=o(p)\) and \(s\log_2 q=o(p)\), then for **every fixed \(m\)** the right side of (5) exceeds \(Kp/s\) eventually. The limiting exceptional proportion is at most \(D/(m+1)\). Now take \(m\) arbitrarily large. The constant \(C(m,\epsilon)\) has only been applied at an already fixed budget.

For ordinary cycles a selected sequence of lags either has a subsequence with \(s=o(p)\), or a subsequence bounded below in relative mismatch density. In the latter case \(p/s\) stays bounded whereas the ordinary minimum tends to infinity, since each fixed positive minimum determines one forward orbit. Thus the first conclusion holds on both alternatives, uniformly by choosing any offending lag. The nonnegativity of all heights and (5)'s conclusion show that the mean of \(s(Z_i+Z_{i+\ell})/p\) tends to infinity, proving the second assertion of (1).

For (2) take the \(J\) consecutive translates \(i+j\ell,\ 0\le j<J\). Two low states in this tuple give a proper lag \(d\ell,\ 1\le d<J\), with \(s_{d\ell}\le d s_\ell\) by the triangle inequality. Both paired heights then sum to at most \(2K d p/s_{d\ell}\). In the rational case \(s_{d\ell}=o(p)\) and \(s_{d\ell}\log_2q=o(p)\) still hold. By (1)'s paired conclusion and a union bound over finitely many translates, only \(o(p)\) initial dates have two low states in their tuple. The expected number of low states in a tuple is \(J\) times their fraction, yielding (2). For fixed \(M\), taking \(J=M\) tests each entire fiber. No order-dependent constant is passed to a growing \(M\).

## An averaged complete-denominator lower bound

First \(s=o(p)\) under \(s\bar Z=O(p)\). Indeed the \(p\) distinct numerator states are positive integers; at least half are at least \(p/2\), so \(\bar Z\to\infty\). Work on a subsequence where \(s\log_2q/p\) tends to its finite lower limit \(\lambda\), the infinite case being immediate. Fix \(B\) with \(s\bar Z/p\le B\) there.

For \(a>0\) and an integer \(k\ge1\) choose \(L=\lceil kp/s\rceil\), \(m=\lceil(1+a)k\rceil\). For large periods the good fraction \(m_i(L)\le m\) is at least a fixed \(g_a>0\) independent of \(k\), for example \(g_a=a/[2(1+a)]\), by the preceding mismatch count. The mean of \(H_i+h_{i+L}\) over *all* starts equals \(2\bar Z\) by permutation. Thus one good start has \(H_i+h_{i+L}\le2\bar Z/g_a\). Insert that actual arc in (4), divide by \(kp/s\), then take the period limit with \(k,a,\epsilon\) fixed. This gives
\[
        1-\epsilon\le \frac{2B}{k g_a}+4(1+a+2/k)\lambda .
\]
Let \(k\to\infty\), then \(a,\epsilon\downarrow0\), proving (3).

The [mixed-divisor occupation bound](ROTATION_OCCUPATION.md) gives a constant lower bound on the normalized whole-cycle mean and a low-state bound with an explicit additive \(O_J(s\log(qY))\) term at a cutoff \(Y\). Here the diverging mean and the negligible probability of a low pair at every *fixed multiple* of \(p/s\) on the bit scale come from the exact open endpoint theorem and uniform-origin averaging. This does not specify the rate of the divergence in (1), or force a positive density of mismatches at an arbitrary lag.

[Exact all-origin checker](check_uniform_rotation_height.py) · [Finite receipt](uniform_rotation_height_controls.json). On 456 genuine primitive rational cycles it checks 14,812 choices of lag and window length and 54,424 local-budget selections, including complete physical endpoint products, growth of the lower height, and 4,942 lengths longer than one lap. The asymptotic endpoint inequality is the separate written theorem.
