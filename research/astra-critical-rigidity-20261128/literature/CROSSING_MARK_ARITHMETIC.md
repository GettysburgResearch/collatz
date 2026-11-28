# Prime powers at the productive crossings of adjacent rational cycles

Use the [ordered-calendar notation and estimates](ORDERED_CALENDAR_CROSSINGS.md). The paired positive periodic phases start one unit apart. Their native period is \(L\), each arm has grade \(p\), and \(M\) is the number of unequal ordinal dates. At native time \(t\), write \(g,h\) for the two grades so far, \(j_t=|g-h|\), and \(A_t=3^{g-\min(g,h)}Y_t-3^{h-\min(g,h)}X_t\) for the nonzero signed **integer** difference. Mark the single-odd letters and the double-odd letters with \(j_t>0\). A productive mark is an inward single-odd step or a double-odd step at unequal grades. Its weight \(j_t\) counts the strict ordered calendar crossings owned by that later odd departure. Thus the total productive weight is \(I\), there are at most \(2M\) marks, and the sum of \(j_t\) over **all** marks is at most \(2I\).

For a fixed finite prime set \(P\supset\{2,3\}\), let \(b_P(a)\) be the positive part of \(|a|\) supported outside \(P\), with multiplicities. Write \([u]_+=\max(u,0)\) and \(\gamma=\log_2 3\).

**Proposed results.** On every individual productive edge as \(j_t\to\infty\), uniformly over all supplied cycles,
\[
          \log_3[b_P(A_t)b_P(A_{t+1})]\ge(1-o(1))j_t .               \tag{1}
\]
For each \(\theta<1/2\) and each \(\epsilon>0\), the **individual** low-cofactor productive marks satisfy
\[
     \sum_{\substack{t\ {\rm productive}\\b_P(A_t)\le3^{\theta j_t}}}j_t
                            \le \epsilon I+C_{P,\theta,\epsilon}M.    \tag{2}
\]
The real magnitudes obey a stronger average bound for every \(\epsilon>0\),
\[
       \sum_{t\ {\rm productive}}[j_t-\log_3|A_t|]_+
                            \le \epsilon I+C_\epsilon M.             \tag{3}
\]
Finally, at every \(\epsilon>0\),
\[
       \sum_{t\ {\rm productive}}[j_t-\log_3 b_P(A_t)]_+
                            \le \epsilon I+C_{P,\epsilon}p.           \tag{4}
\]
Thus along **any** sequence with \(I/p\to\infty\), almost all ordered crossings, counted with their multiplicities, occur at marks with \(b_P(A_t)\ge3^{(1-\delta)j_t}\), for every fixed \(\delta>0\). This applies in particular at the known lower scale \(L\ge c p\log p\). The [closed-pair theorem](ORDERED_CALENDAR_CROSSINGS.md) forces \(I/(p\log p)\to\infty\) on every such family. These factors belong to the true normalized difference, rather than to an unreduced affine numerator or to a formal Laurent polynomial.

## Fixed-length comparisons across the ternary exponent gap

At positive level the actual arms are ternary units, so \(3\nmid A_t\). Within an excursion of \(j_t\) above zero choose the sign of \(A\) to make the large productive impulses positive. Equation (4) of the [calendar calculation](ORDERED_CALENDAR_CROSSINGS.md) reads \(2A'=3^c A+B\) in this orientation. An outward step has \((c,B)=(1,-1)\), an inward step has \((c,B)=(0,3^{j-1})\), and an unequal-rank double odd has \((c,B)=(1,3^j-1)\). A common-even step has \((c,B)=(0,0)\). At the two ends of an excursion one may use the same orientation in the recurrence. In the interior no other unmarked steps occur.

Fix an integer \(m\ge1\). Consider \([s,e)\) containing at most \(m\) marks, including at least one productive mark, with starting level \(j=j_s>m+2\). The level remains positive and changes by at most \(m\). Unroll the recurrence. The endpoints have the two coefficients \(A_s,A_e\), and there are at most \(2m\) other signed pure two-three terms. The high ternary exponents are at least \(j-m-1\), and the corresponding summands all have the same sign. Every remaining ternary exponent is at most \(m\), including at the endpoints because they are ternary units. The high-group sum is nonzero.

For each \(\kappa>1\), this gives
\[
 (j-2m-1)\log_2 3\le
       \kappa\log_2[b_P(A_s)b_P(A_e)]+C_{m,P,\kappa}.                 \tag{5}
\]
Here is the exact use of the [earlier stable circuit argument, equation (4)](../ordinary/SPARSE_DISCREPANCY_BLOCKS.md). If there were no such constant, pass to a violating sequence with fixed term count, high group and endpoint labels, and a maximal fixed rational relation space. On this subsequence, for each minimal dependent sublist with fixed relation coefficients, its primitive relation tuple has multiplicative height at most a fixed constant times the product of its exceptional prime-to-\(P\) parts to power \(\kappa\). This follows with the coordinate forms and their sum at \(\infty\) and \(P\), as proved there. Decompose the all-ones relation into circuit relations. At least one used circuit crosses the displayed partition: otherwise restricting the decomposition to the high group would give zero at each example, contrary to its common nonzero sign. In a crossing circuit the ratio of valuations at three of the high and low entries pays at least \((j-2m-1)\log_2 3\) in the logarithm of the primitive tuple height, up to the constants of the fixed relation coefficients. The common gcd cancels from this valuation difference. Only the two endpoint integers can contribute to the exceptional parts. This contradicts the chosen sequence and proves (5). This use of the circuit argument needs no rearrangement of chronological nonzero-prefix conditions in the ternary ordering.

Take \(e=s+1\) to obtain (1), by first fixing \(\kappa>1\) and then letting it decrease to one. For (2) one may assume \(0\le\theta<1/2\). Choose \(\kappa>1\) with \(2\kappa\theta<1\). Two qualifying productive marks \(s<e\) in the same packet of at most \(m\) marks have \(|j_s-j_e|\le m\). At sufficiently large \(j_s\) their assumed small cofactors contradict (5). Partition the marked dates chronologically into packets of \(m\), except for the last possible incomplete one. Every complete packet's maximum level is at most its average plus \(m\). A final incomplete packet ends towards level zero and has maximum at most \(m\). At bounded levels the whole contribution is \(O_{m,P,\theta}(M)\). At high levels at most one qualifying mark per packet remains. Its weight, summed across packets, is at most \(2I/m+O_m(M)\). Choose \(m\) to prove (2).

## Removing large negative real corrections

A positive oriented integer \(A\) stays positive until the excursion ends, by the four recurrences above. Each excursion therefore has at most one suffix where the input to its steps is positive. The sum of the maximum levels of all excursions is at most the total number of outward steps, which is \(H/2\le M\).

In the negative part of an excursion a productive step with \(|A|<3^{j-1}/3\) sends \(A\) strictly positive. Indeed \(B\ge 3^{j-1}\) and \(3^c\le3\). Thus there is at most one such step per excursion. Charging it at cost \(j\) and charging at most two to \([j-\log_3|A|]_+\) on each other negative productive mark costs \(O(M)\) in total.

On every positive suffix consider the signed corrections
\[
        \Delta_t=\log_2\left|1+\frac{B_t}{3^{c_t}A_t}\right|.
\]
Every outward mark has \(\Delta_t\ge-\log_2(3/2)\). On a productive mark, \(B_t\ge3^{j_t-1}\) and \(3^{c_t}\le3\), so
\[
       \gamma[j_t-\log_3|A_t|]_+\le \Delta_t+2\gamma .
\]
The signed sum of corrections on the positive suffixes satisfies, for each fixed \(m\),
\[
            \sum_{\rm positive\ suffixes}\Delta_t
                         \le (12\gamma/m)I+O_m(M).                     \tag{6}
\]
For clarity, partition each such suffix separately into packets of \(m\) marks. The [low-endpoint packet proof](ORDERED_CALENDAR_CROSSINGS.md) bounds any packet's signed correction by \(6\gamma(j_*+1)+C_{2m}+m+1\), with \(j_*\) its greatest level. Its proof starts and ends its trimmed native interval at the first and last low marks, so it applies to arbitrary packets without full-period boundary hypotheses. For complete packets the sum of these maxima is at most \(2I/m+O_m(M)\). At most one incomplete packet per positive suffix remains. Charge its maximum to its excursion maximum and sum the bound \(H/2\) above. This proves (6). Adding the lower bound on the negative outward corrections and the cost of negative sectors proves (3).

## A fixed prime cannot contribute a positive fraction of the level twice on a short packet

Fix a prime \(\ell\ne3\) and \(\delta>0\). In the positive-level comparison from (5), now let \(s\) itself be productive and put \(d=e-s\). Independently of the signs of the endpoints, the integer recurrence also gives
\[
  2^d A_e-3^h A_s=3^{j-m-1}P_1-Q_1,\qquad 0\le h\le m,\quad
  P_1>0,\quad Q_1\ge0,\qquad
  \ln\max(P_1,Q_1)\le d\ln2+O_m(1).                                  \tag{7}
\]
Use the same sign orientation at both ends. Each positive term of the unrolled productive high group has a factor \(3^{j-m-1}\), leaving at most \(2^d3^{3m+2}\) per term. The negative low terms are generated by outward steps and the minus one of a marked double odd. All intervening slope multipliers contribute at most \(m\) extra powers of three. This proves (7).

There is \(\tau_{\ell,\delta}>0\), independent of \(m\), such that for each fixed \(m\) and all sufficiently large \(j\), two productive endpoints with
\[
  v_\ell(A_z)\ln\ell\ge\delta j_z\ln3\quad (z=s,e),\qquad
                            e-s\le\tau_{\ell,\delta}j_s               \tag{8}
\]
cannot occur in an interval with at most \(m\) marks before \(e\). Both terms on the left of (7) are divisible by \(\ell^v\) with \(v\ln\ell\ge\delta(j-m)\ln3\). For \(Q_1=0\) this already contradicts (7) if \(\tau\ln2<\delta\ln3/4\) and \(j\) is sufficiently large, since \(\ell\ne3\).

For \(Q_1>0\) use the following precise coefficient form of the Baker–Yu theorem. For fixed number field \(K\), place \(v\), finitely generated group \(\Gamma\subset K^\times\) and \(\varepsilon>0\), there is an effective \(C\) such that **for every** \(A\in K^\times\) and \(z\in\Gamma\),
\[
               |1-Az|_v\le H(z)^{-\varepsilon}
                    \quad\Longrightarrow\quad h(z)\le C(1+h(A)).
\]
Here \(h=\ln H\) is the logarithmic Weil height. Use \(K=\mathbb Q\), the place \(\ell\), \(\Gamma=\langle3\rangle\), \(\varepsilon=\delta/2\), \(z=3^{j-m-1}\), \(A=P_1/Q_1\). By (7), both \(v_\ell(Q_1)\ln\ell\) and \(h(A)\) are at most \(d\ln2+O_m(1)\). After the possible loss at the denominator in \(|1-Az|_\ell\), (8) gives the required smallness for all large \(j\). The conclusion \((j-m-1)\ln3\le C[1+d\ln2+O_m(1)]\) is impossible if also \(\tau\ln2<\ln3/(4C)\). This includes the case of exact equality \(Az=1\) by the same height comparison. The linear dependence on the **moving** coefficient height in this fixed-accuracy formulation is essential. Calegari, Dimitrov and Tang give the exact formulation and a new arithmetic-holonomy approach, crediting the earlier archimedean and nonarchimedean results to Baker and Yu. [Calegari–Dimitrov–Tang, ICM 2026, Theorem 1.1, (1.1)–(1.2), and accompanying history](https://math.uchicago.edu/~fcale/papers/ICM.pdf)

Partition all marks again into packets of \(m\). Ignore bounded maxima at cost \(O_{m,\ell,\delta}(M)\) in crossing weight. If a packet with maximum \(j_*\) has native distance between its first and last mark greater than \(\tau j_*/2\), its marks cost at most \(mj_*\) in weight. The sum of these native distances is at most \(L\) because the packets are disjoint. Their total cost is at most \(2mL/\tau\). In every remaining high packet, all marked levels exceed \(j_*/2\) and (8) permits at most one qualifying productive mark. Summing the maximum estimates as before gives
\[
 \sum_{\substack{t\ {\rm productive}\\v_\ell(A_t)\ln\ell\ge\delta j_t\ln3}}j_t
           \le 2I/m+2mL/\tau+O_{m,\ell,\delta}(M).                   \tag{9}
\]
At \(\ell=3\) the sum is empty. For each fixed \(m\), substitute the [calendar bound](ORDERED_CALENDAR_CROSSINGS.md) \(L\le\gamma p+\epsilon'I+C_{\epsilon'}M\), choosing \(\epsilon'\) after \(m,\ell,\delta\). Since \(M\le p\), (9) yields the following uniform form for every \(\zeta>0\):
\[
 \sum_{\substack{t\ {\rm productive}\\v_\ell(A_t)\ln\ell\ge\delta j_t\ln3}}j_t
                         \le\zeta I+C_{\ell,\delta,\zeta}p.           \tag{10}
\]

To obtain (4), outside the union of these events over \(\ell\in P\) the removed prime powers have total base-three logarithm at most \(|P|\delta j_t\). On the union the positive part in (4) is at most \(j_t\). Apply (3) and (10) with sufficiently small \(\delta,\zeta\) to get the stated coefficient \(\epsilon\). Markov's inequality for the weights \(j_t/I\) gives the announced threshold interpretation.

The constants in the combined bounds inherit the ineffective circuit threshold. The pointwise statement (1) and (2) allow \(p\) much larger than \(I\). The full threshold in (4) uses \(I/p\to\infty\) to discard the long native packets. Every prime set in these statements is fixed before taking the limit. The product outside it may be distributed over many prime powers. The estimates constrain supplied efficient ordered calendars and leave their unrestricted maximum length open.
