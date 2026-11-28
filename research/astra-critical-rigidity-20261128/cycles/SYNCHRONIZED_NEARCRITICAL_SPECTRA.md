# The whole denominator-rate interval at common nearcritical native clocks

**Proposed written theorem.** There is a single sequence of integer clock pairs \((p_n,A_n)\) and finite nonempty collections \(\mathcal C_n\) of genuine primitive positive rational odd cycles, **each** of least odd period \(p_n\) and total valuation \(A_n\), such that
\[
 \begin{split}
 &0<A_n-p_n\log_2 3\le p_n^{-1+o(1)},\\
 &\inf_{C\in\mathcal C_n}m(C)\ge p_n^{2-o(1)},\qquad
 \sup_{C\in\mathcal C_n}|X(C)/m(C)-2|\le p_n^{-1+o(1)},\\
 &\sup_{C\in\mathcal C_n}\left|\frac{\log_3 q(C)}{r(C)}-1\right|\to0,\\
 & d_{\mathrm H}\!\left(\left\{\frac{\log_3 q(C)}{p_n}:C\in\mathcal C_n\right\},
                                      [0,1]\right)\to0 .
 \end{split}                                                            \tag{1}
\]
Here \(q(C)\) is the whole reduced denominator and \(r(C)\) the minimal chronological recurrence degree. The same Hausdorff limit holds for the set of \(r(C)/p_n\). In particular, for every real-valued sequence \(\lambda_n\in[0,1]\), even when it depends on the chosen clock pairs, one can select a member \(C_n\in\mathcal C_n\) with \(\log_3 q(C_n)/p_n-\lambda_n\to0\). The same clock sequence works simultaneously for all such choices. [Nearcritical binary sheet-mask theorem and exact fixed-mask rates](NEARCRITICAL_DENOMINATOR_SPECTRUM.md)

Take the same fixed odd \(L\), \(a\ge2,\ g=2^aL\), two-power half-interval rows \(h_j\), and odd-factor singleton row \(v\) as in the cited construction. Always include \(v\), choose an arbitrary subset of \(v h_j\) for \(1\le j<a\), and use one of two rows at the largest level. If the largest row is \(h_a\), the proven active-frequency counts give rates
\[
                         \frac1{2L}+\frac{t+1}{2^a},
                              \qquad 0\le t<2^{a-1}.                    \tag{2}
\]
If instead it is \(v h_a\), its primitive two-power frequencies occur at every one of the \(L\) odd-factor frequencies. Its trivial two-power contribution is already supplied by \(v\); the change therefore adds exactly \((L-1)2^{a-1}\) frequencies. Its stabilizer is trivial: preserving \(v\) already forces the odd-factor translation to be zero, and then preserving this new row requires preservation of \(h_a\) on its nonempty odd-factor support. Thus the primitive clock is the same in both constructions. The resulting second set of rates is
\[
                          \frac12+\frac{t+1}{2^a},
                              \qquad 0\le t<2^{a-1}.                    \tag{3}
\]
In both displays the fractions are the exact \(r/p\) for all sufficiently large upper convergents \(B/P\), by the fixed-mask theorem. Every collection at these sheets uses the same \(gP,gB\), and all masks occupy at most \(a+1\) small rank positions. The union of (2) and (3) lies in \([0,1]\) and comes within \(1/(2L)+2^{-a}\) of every point there.

Now choose odd \(L_n\to\infty\), integers \(a_n\to\infty\), and \(\varepsilon_n\downarrow0\). At stage \(n\) the two arrays for all \(t\) form one finite family. By the [component-wise resultant and geometric bounds](NEARCRITICAL_DENOMINATOR_SPECTRUM.md), one common sufficiently large upper convergent ensures \(|\log_3 q/r-1|<\varepsilon_n\) for **every** member of this family. Enlarge it if necessary so \(\log(2^{a_n}L_n+a_n)=o(\log P_n)\), for example by demanding the left side be at most \((\log P_n)/n\). The uniform real height and width estimates and clock defect from the same construction give the first two lines of (1). Since \(r/p\le1\), the computed \(r/p\) mesh changes by at most \(\varepsilon_n\) at every member when it is replaced by the complete \(\log_3 q/p\). This proves the last two lines.
