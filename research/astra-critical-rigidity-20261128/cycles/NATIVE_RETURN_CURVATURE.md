# A single sign of integer curvature on all native origins of a narrow run

**Proposed written theorem.** Put \(\gamma=\log_2 3\). Fix \(2<R<4\). Any chronological run of \(T\) **distinct** positive odd ordinary Collatz states in \([M,RM]\), \(M\ge2\), satisfies, for every positive integer \(s\),
\[
                 1\ \ll_R\ M\|s\gamma\|^2+\frac{s^2}{T}.              \tag{1}
\]
The constants are effective and no irrationality exponent or source-count theorem is used. Thus a sufficiently accurate return \(\|s\gamma\|\le c_R M^{-1/2}\) forces \(T\ll_R s^2\). For example, if \(b,b'\) are successive convergent denominators and \(b'\ge C_R\sqrt M\), then \(T\ll_R b^2\). This is most informative across an exceptionally large partial quotient. The [convergent-gap source bound](CONFINED_CONVERGENT_GAPS.md) is a separate restriction.

There is a simultaneous geometric conclusion at the actual integer level. Let \(h\) be a nearest integer to \(s\gamma\), and write \(V_t=2^{E_t}x_t\) for the genuine lift, where \(E_t\) is cumulative native division and \(E_0=0\). Provided
\[
    s\le T/10,\qquad \|s\gamma\|+s/M\le c_R,                           \tag{2}
\]
all the real quantities
\[
    2^{-2h}V_{t+2s}-2\,2^{-h}V_{t+s}+V_t,\qquad
                         s\le t\le T-1-2s,                             \tag{3}
\]
are nonzero and have the **same sign over every consecutive native origin**. Consequently all the deweighted strings \(2^{-kh}V_{r+ks}\), for all residue classes \(r\bmod s\), have strictly positive second differences on this interior, or all have strictly negative second differences there. This is an order restriction on real states of one chronological run, including comparisons between consecutive returns; no choice of a separate orientation per residue class is needed.

For a run of distinct positive odd rationals of a common complete reduced denominator \(q\) prime to six, the same sign statement holds whenever
\[
                            q\mid(3^s-2^h)^2 .                          \tag{4}
\]
In (1) replace \(T\) by \(\min(T,\lfloor M\rfloor)\) in this moving-denominator version. Condition (4) is automatic for ordinary integers. It can also hold without \(q\mid3^s-2^h\) when \(q\) contains repeated prime factors. This proof uses (4) only for integrality of the actual second comparison.

## The three true labels on a common binary chart

Use \(U_t=2^{E_t}\), so \(V_{t+1}=3V_t+U_t\), and \(D=2^{-h}\operatorname{shift}^s\). Choose \(L=M(1+R/4)\) and \(F_t=\lfloor\log_2(V_t/L)\rfloor\). On every allowed row the three rescaled labels are
\[
                 Y_{t,j}=2^{-F_t}(D^jV)(t)=C_{t,j}x_{t+js},
                    \qquad C_{t,j}=2^{-F_t}(D^jU)(t),\quad j=0,1,2 .
\]
Their logarithmic ratios to the base label have absolute value at most \(2\|s\gamma\|+O(s/M)\), by summing the true log correction. Since \(RM/2<L<2M\) has fixed positive relative margins, (2) makes each dyadic power \(C_{t,j}\) equal one or two. This construction uses only dates on the given run.

Put \(H_t=2^{-F_t}((D-1)^2 V)(t)\). It is an integer for ordinary inputs. For the extension, in \(\mathbb Z[1/2]/q\) one has \(qV_{t+s}\equiv3^s qV_t\), from the genuine recurrence after multiplying by \(q\). Thus \(qH_t\equiv2^{-F_t}(3^s2^{-h}-1)^2 qV_t\pmod q\). Condition (4) makes \(H_t\in\mathbb Z[1/2]\); also \(H_t\in q^{-1}\mathbb Z\) since the three tags are integral. As \(q\) is odd the intersection is \(\mathbb Z\). The individual labels need not be integers.

At every edge where the three labels are defined,
\[
  2^{F_{t+1}-F_t}H_{t+1}=3H_t+d_t,\qquad
            d_t=C_{t,2}-2C_{t,1}+C_{t,0}\in[-2,2]\cap\mathbb Z .
\]
Strict positive or negative integer sign persists forward, and a zero propagates backwards. Suppose \(H_t=0\) for some interior \(t\ge s\). All \(H_r\) vanish for \(t-s\le r\le t\), so \(d_r=0\) for \(t-s\le r<t\). Three members of \(\{1,2\}\) in arithmetic progression are identical. Hence \(((D-1)U)(r)=0\) for every one of those \(s\) dates. Write \(B=(D-1)V\). The actual recurrence now gives \(B(t)=3^s B(t-s)\), whereas \(H_{t-s}=0\) gives \(B(t)=2^h B(t-s)\). As \(s>0\), unique factorization implies \(B(t-s)=0\). Two distinct odd-state rays would then coincide: \(V_t=2^h V_{t-s}\), which makes the two physical states equal after multiplying by their common odd denominator and comparing the powers of two of their odd numerators. This contradicts distinctness. It proves all of (3), including the common orientation.

## Summing signed curvatures

For ordinary inputs distinctness implies \(T\le RM+1\). For rational inputs use the first \(\min(T,\lfloor M\rfloor)\) states and call that length \(T\) below. Cases where \(s>T/10\) or (2) fails give (1) after increasing a constant: if \(s/M\) is bounded below then \(s^2/T\gg_R1\), and if \(\|s\gamma\|\) is bounded below then \(M\|s\gamma\|^2\gg_R1\). It remains to work under (2).

Set \(G_t=3^{-t}V_t\). Then \(G_0=x_0\in[M,RM]\) and
\[
              G_{t+1}=G_t\left(1+\frac1{3x_t}\right).
\]
Since \(T=O_R(M)\), throughout the run \(M\le G_t\ll_R M\) and \(0<G_{t+1}-G_t\ll_R1\). In particular \(2^{F_t}/3^t=G_t/Y_{t,0}\gg_R1\). Write \(\lambda=3^s2^{-h}\), so \(|\lambda-1|\ll\|s\gamma\|\). The integer \(H_t\) has common nonzero sign on a consecutive interval \(I\) of length \(\gg T\) in (3). Therefore
\[
 T\ll_R\left|\sum_{t\in I}
       \big(\lambda^2 G_{t+2s}-2\lambda G_{t+s}+G_t\big)\right|.
\]
With \(\Delta_sG_t=G_{t+s}-G_t\), the summand is
\[
             \lambda^2\Delta_s^2G_t+
                  2\lambda(\lambda-1)\Delta_sG_t+(\lambda-1)^2G_t.
\]
The sum of the first signed differences of \(\Delta_sG_t\) has absolute value \(O_R(s^2)\): only two boundary intervals of at most \(s\) terms remain, each term \(O_R(s)\). The latter two contributions are \(O_R(Ts\|s\gamma\|+TM\|s\gamma\|^2)\). The mixed term is absorbed using \(s\|s\gamma\|\le (s^2/M+M\|s\gamma\|^2)/2\) and \(T=O_R(M)\). This proves (1). The argument applies even when the entire deweighted \(s\)-string passes across a dyadic chart boundary, since only a moving triple needs the binary chart.

The [four-sum rank-order analysis](FOUR_SUM_GEOMETRIC_SPACING.md) and the preceding [finite-tube rectangle argument](FROBENIUS_BAND_EXITS.md) concern general signed pairs. Here the repeated middle entry and the shared native time step give an exact competing-multiplier contradiction for every individual second difference, followed by a signed sum over the whole actual interval.
