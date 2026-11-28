# Full cofactor height at almost every ordered crossing, normalized by the number of unequal ranks

Use the notation of [Crossing mark arithmetic](CROSSING_MARK_ARITHMETIC.md). Every positive-determinant ordered cycle has grade \(p\), \(M\) unequal ordinal dates and total productive crossing weight \(I\). With the same fixed finite prime set \(P\supset\{2,3\}\), the following strengthens its bound (4). For every \(\epsilon>0\) there is \(C_{P,\epsilon}\) such that
\[
          \sum_{t\ {\rm productive}}[j_t-\log_3 b_P(A_t)]_+
                             \le\epsilon I+C_{P,\epsilon}M.            \tag{1}
\]
In particular \(I/M\to\infty\) suffices for \(b_P(A_t)\ge3^{(1-\delta)j_t}\) at all but \(o(I)\) of the individual crossings counted with their full multiplicities, for every fixed \(\delta>0\). The matched ordinal dates may dominate the grade. The constants here remain ineffective because the chronological and real-amplitude inputs use the Subspace Theorem.

## A large initial dyadic valuation forces the next fixed number of marks to be close in native time

Fix \(m\ge1\) and \(\xi>0\). Take a productive start \(s\) at level \(j\), and any later marked date \(e\) with at most \(m\) marks in \([s,e)\). Uniformly across such intervals,
\[
       v_2(A_s)\ge\xi j,\qquad j\to\infty
                          \quad\Longrightarrow\quad (e-s)/j\to0.      \tag{2}
\]
The statement concerns native dates, including all intervening common-even waits.

Suppose it fails along a sequence with \(e-s\ge c j\) and \(j\to\infty\), for some fixed \(c>0\). Thin to fix the number of marks up to and including \(e\), and to make all their ratios \((t-s)/j\) converge in the extended nonnegative reals. Let \(w\) be the first mark with positive limiting ratio. Earlier marks have offsets \(o(j)\). Choose a constant \(a>0\) smaller than that limit, and stop the expansion at \(s+d\), \(d=\lfloor aj\rfloor\), before \(w\) and after every earlier mark. For large \(j\) the orientation is constant and the level stays positive. At most \(m\) marked impulses already include the productive start.

The integer expansion from [equation (7)](CROSSING_MARK_ARITHMETIC.md) now has
\[
  2^d A_{s+d}-3^h A_s=3^{j-m-1}P_1-Q_1,\qquad
    0\le h\le m,\quad P_1>0,\quad Q_1\ge0,\qquad
                      \ln\max(P_1,Q_1)=o(j).                          \tag{3}
\]
Indeed each coefficient uses \(2^{t-s}\) only up to the last included marked date. Its other factors after extracting the common high power of three are bounded in terms of \(m\). This sharpens the earlier \(d\ln2+O_m(1)\) estimate in precisely this situation. The left side is divisible by \(2^{\min(d,v_2(A_s))}\), whose base-two logarithm is at least \((\min(a,\xi)+o(1))j\). If \(Q_1=0\), this contradicts the height of \(P_1\). If \(Q_1>0\), put \(z=3^{j-m-1}\) and \(A=P_1/Q_1\). Here \(h(A)=o(j)\) and \(v_2(Q_1)=o(j)\), so \(|1-Az|_2\le H(z)^{-\eta}\) for a fixed \(\eta>0\), for instance \(\eta=\min(a,\xi)\ln 2/(3\ln 3)\). The coefficient form of the Baker–Yu theorem gives \(h(z)\ll_\eta 1+h(A)=o(j)\), contradicting \(h(z)=(j-m-1)\ln3\). This proves (2), also covering exact equality through the same height conclusion. [Calegari–Dimitrov–Tang, ICM 2026, Theorem 1.1](https://math.uchicago.edu/~fcale/papers/ICM.pdf)

## Counting low-cofactor marks with one large specified prime inside a fixed packet

Fix a prime \(\ell\in P\setminus\{3\}\), \(\alpha>0\), and \(0<\delta<1\). In a packet of \(m\) consecutive marks, call a productive date \(t\) selected when
\[
   \log_3 b_P(A_t)\le(1-\delta)j_t,\qquad
                       v_\ell(A_t)\ln\ell\ge\alpha j_t\ln3.           \tag{4}
\]
There is an upper bound \(B_{\ell,\alpha}\) on the number selected whenever the maximum packet level tends to infinity for fixed \(m\). More exactly, for each fixed \(m,P,\ell,\alpha,\delta\), a finite height threshold suffices for that bound. The bound on the number is independent of \(m\).

To see this, let \(s\) and \(e\) be the first and last selected dates, where a single date needs no argument. All marked levels differ from \(j=j_s\) by at most \(m\). The [fixed-prime spacing estimate (8)](CROSSING_MARK_ARITHMETIC.md) says that two successive selected dates \(u<v\) are more than \(\tau_{\ell,\alpha}j_u\) native steps apart above a fixed threshold, with \(\tau_{\ell,\alpha}>0\) independent of \(m\). If \(v_2(A_s)\ge j\), (2) gives \(e-s=o(j)\) and permits no second selected date.

If \(v_2(A_s)< j\), apply the full [signed chronological estimate (3)](../ordinary/SPARSE_DISCREPANCY_BLOCKS.md) with \(\kappa=2\) to \([s,e)\). All earlier native partial sums are nonzero by the physical determinant, and there are at most \(2m\) pure interior terms. The terminal dyadic valuation is nonnegative. Thus
\[
 e-s \le 2\log_2[b_P(A_s)b_P(A_e)]+v_2(A_s)+C_{2m,P,2}
                    \le (4\log_2 3+1)j+O_{m,P}(1).                   \tag{5}
\]
The coefficient is independent of \(m\). At large levels \(j_u\ge j/2\) and (5) is at most \((4\log_2 3+2)j\). Hence one may take \(B_{\ell,\alpha}=2+\lceil2(4\log_2 3+2)/\tau_{\ell,\alpha}\rceil\). The two cases cover all possible first selected dates. No bound on total native period is used.

For any \(\eta>0\), (4) therefore has total weight at most \(\eta I+C_{P,\ell,\alpha,\delta,\eta}M\). Indeed complete \(m\)-mark packet maxima sum to at most \(2I/m+O_m(M)\), the last incomplete maximum is at most \(m\), and bounded-level packets contribute \(O_{m,P,\ell,\alpha,\delta}(M)\). Choose \(m>2B_{\ell,\alpha}/\eta\) before applying the resulting finite threshold.

Finally take \(\alpha=\delta/(2|P|)\). If the first inequality in (4) holds and \(\log_3 |A_t|\ge(1-\delta/2)j_t\), some \(\ell\in P\setminus\{3\}\) supplies its second inequality, since \(A_t\) is a ternary unit. The remaining low-cofactor marks have real deficit greater than \(\delta j_t/2\), and thus have total weight at most \(\eta I+C_{\delta,\eta}M\) by [the real bound (3)](CROSSING_MARK_ARITHMETIC.md), after choosing that bound's coefficient. The union over the fixed finite prime set preserves an arbitrarily small coefficient. At all other productive marks the cofactor deficit is at most \(\delta j_t\). First choosing \(\delta<\epsilon/2\) and then the small weight coefficients proves (1). The [finite arithmetic control](check_crossing_mark_arithmetic.py) checks the last-included-mark height and single-start dyadic divisibility in (3) on actual signed trajectories. Its finite ranges concern those exact formulas.
